#!/usr/bin/env python3
"""
GDI (Governed Decision Intelligence) driver for agent-governance-testvectors.

Produces v2 structured-envelope receipts with a GDR payload embedded in
`payload.gdr`. The GDR captures pre-decision reasoning state: confidence
score, gate classification, evidence completeness, and accountability chain.

Wire format: v2 envelope conforming to draft-farley-acta-signed-receipts.
Verified by @veritasacta/verify.

Apache-2.0. https://github.com/mj3b/governed-decision-intelligence
"""

from __future__ import annotations
import base64, hashlib, json, sys, time
from pathlib import Path
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

# Conformance keypair -- testing only
SEED = bytes.fromhex("0000000000000000000000000000000000000000000000000000000000000001")
_PRIV = Ed25519PrivateKey.from_private_bytes(SEED)
_PUB  = _PRIV.public_key().public_bytes_raw()
PUBKEY_HEX = _PUB.hex()
_KID = base64.urlsafe_b64encode(hashlib.sha256(_PUB).digest()[:16]).rstrip(b"=").decode()


def evaluate_cedar(tool_name: str, context: dict) -> str:
    destructive = {"rm -rf", "dd", "mkfs", "shred"}
    safe_bash   = {"git", "npm", "ls", "cat", "pwd", "echo", "node", "python"}
    if tool_name == "Bash":
        cmd = context.get("command_pattern", "")
        if cmd in destructive: return "deny"
        if cmd in safe_bash:   return "allow"
        return "deny"
    if tool_name in {"Read", "Glob", "Grep", "WebSearch"}: return "allow"
    if tool_name in {"Write", "Edit"}:
        return "allow" if context.get("path_starts_with") == "./" else "deny"
    return "deny"


GATE_MAP = {
    ("allow","Read"):      ("routine",              0.92),
    ("allow","Glob"):      ("routine",              0.90),
    ("allow","Grep"):      ("routine",              0.90),
    ("allow","WebSearch"): ("routine",              0.88),
    ("allow","Bash"):      ("elevated_review",      0.78),
    ("allow","Write"):     ("elevated_review",      0.75),
    ("allow","Edit"):      ("elevated_review",      0.75),
    ("deny", "Bash"):      ("blocked",              0.15),
    ("deny", "Write"):     ("mandatory_escalation", 0.22),
    ("deny", "Edit"):      ("mandatory_escalation", 0.22),
}

def build_gdr(tool_name, tool_input, context, decision, policy_id,
              session_id, sequence, timestamp):
    gate_class, confidence = GATE_MAP.get((decision, tool_name), ("deferred", 0.50))
    evidence_sources = []
    if tool_input:
        evidence_sources.append({"completeness":"complete",
            "fields_present":sorted(tool_input.keys()), "source":"tool_input"})
    if context:
        evidence_sources.append({"completeness":"complete",
            "fields_present":sorted(context.keys()), "source":"context"})
    reasoning = (
        f"{tool_name} evaluated against {policy_id}. Gate: {gate_class}. "
        + (f"Confidence {confidence:.2f} meets threshold. Action approved."
           if decision == "allow"
           else f"Confidence {confidence:.2f} below threshold or forbid matched. Action blocked.")
    )
    return {
        "accountability_chain": [
            {"identity": f"session:{session_id}", "responsibility": "policy_evaluation", "role": "agent_runtime"},
            {"identity": "human:operator",        "responsibility": "threshold_approval",  "role": "governance_owner"},
        ],
        "confidence_score":         confidence,
        "decision":                 decision,
        "evidence_sources":         evidence_sources,
        "gate_classification":      gate_class,
        "gdr_timestamp":            timestamp,
        "gdr_version":              "2.0",
        "policy_id":                policy_id,
        "reasoning_reconstruction": reasoning,
        "sequence":                 sequence,
        "session_id":               session_id,
        "tool_input":               tool_input,
        "tool_name":                tool_name,
    }

def jcs(obj) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",",":"), ensure_ascii=False).encode()

def sha256p(data) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def build_receipt(fixture: dict, sequence: int, prev_canonical: bytes | None):
    tool_name  = fixture["tool_name"]
    tool_input = fixture.get("tool_input", {})
    context    = fixture.get("context", {})
    session_id = fixture.get("session_id", "testvectors-session-001")
    policy_id  = "autoresearch-safe"
    decision   = evaluate_cedar(tool_name, context)
    timestamp  = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    gdr = build_gdr(tool_name, tool_input, context, decision, policy_id,
                    session_id, sequence, timestamp)

    parent_receipt_hash = sha256p(prev_canonical) if prev_canonical else None

    # Assemble complete receipt (all fields) BEFORE signing
    # The verifier hashes the full object minus the signature field
    receipt = {
        "algorithm":           "ed25519",
        "issued_at":           timestamp,
        "issuer":              "gdi:governed-decision-intelligence",
        "kid":                 _KID,
        "parent_receipt_hash": parent_receipt_hash,
        "payload": {
            "action":        {"kind": tool_name, "target": session_id},
            "decision":      decision,
            "gdr":           gdr,
            "params_hash":   sha256p(jcs(tool_input)) if tool_input else None,
            "policy_digest": sha256p(jcs({"id": policy_id})),
            "policy_id":     policy_id,
            "prev_hash":     parent_receipt_hash,
            "reason_code":   "policy_match" if decision == "allow" else "policy_deny",
            "sequence":      sequence,
            "session_id":    session_id,
            "tier":          "evidenced",
            "timestamp":     timestamp,
            "tool":          tool_name,
            "type":          "scopeblind.receipt.v2",
        },
        "pubkey":   PUBKEY_HEX,
        "sequence": sequence,
        "type":     "decision_receipt",
        "v":        2,
    }

    # Sign JCS of receipt without the signature field
    canonical_bytes = jcs(receipt)
    receipt["signature"] = _PRIV.sign(canonical_bytes).hex()

    return receipt, canonical_bytes


def main():
    repo_root    = Path(__file__).resolve().parents[2]
    fixtures_dir = repo_root / "fixtures" / "inputs"
    if not fixtures_dir.exists():
        print(f"No fixture files found in {fixtures_dir}", file=sys.stderr)
        sys.exit(1)

    out_dir = repo_root / "receipts" / "gdi"
    out_dir.mkdir(parents=True, exist_ok=True)

    prev_canonical = None
    count = 0
    for f in sorted(fixtures_dir.glob("*.json")):
        fixture  = json.loads(f.read_text())
        sequence = fixture.get("sequence", count + 1)
        receipt, canonical = build_receipt(fixture, sequence, prev_canonical)
        (out_dir / f.name).write_text(json.dumps(receipt, indent=2))
        prev_canonical = canonical
        count += 1

    print(f"gdi: {count} receipts in {out_dir}")

if __name__ == "__main__":
    main()
