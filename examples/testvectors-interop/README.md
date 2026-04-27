# GDI Conformance Driver — Veritas Acta Receipt Standard

This directory contains the GDI conformance driver for
[`ScopeBlind/agent-governance-testvectors`](https://github.com/ScopeBlind/agent-governance-testvectors),
the cross-implementation conformance repo for
[`draft-farley-acta-signed-receipts`](https://datatracker.ietf.org/doc/draft-farley-acta-signed-receipts/) (IETF).

**Conformance PR:** [ScopeBlind/agent-governance-testvectors#7](https://github.com/ScopeBlind/agent-governance-testvectors/pull/7)
**Discussion:** [microsoft/agent-governance-toolkit#276](https://github.com/microsoft/agent-governance-toolkit/discussions/276)

---

## What This Demonstrates

Standard conformance drivers produce receipts that capture the policy outcome
(allow/deny), the policy identifier, and chain integrity fields.

The GDI driver goes further. It embeds a full **Governed Decision Record (GDR)**
in the receipt's `payload.gdr` field, sealing the pre-decision reasoning state
before the tool fires:

| GDR Field | What It Captures |
|-----------|-----------------|
| `confidence_score` | Numeric score against institutional thresholds |
| `gate_classification` | `routine`, `elevated_review`, `mandatory_escalation`, `blocked`, or `deferred` |
| `reasoning_reconstruction` | Plain-language explanation of the decision |
| `evidence_sources` | Completeness classification per input source |
| `accountability_chain` | Named roles and responsibilities |

The binding:

```
result_hash = sha256(JCS(GDR))
```

Receipt integrity (attribution, ordering, tamper detection) is independent of
payload semantics. An auditor verifies the receipt offline with
`@veritasacta/verify`; a governance reviewer reads GDR fields from the
attested payload.

---

## The Layer Distinction

The receipt answers: **was this record tampered with?**

The GDR answers: **was this decision sound before it reached policy evaluation?**

These are adjacent, not identical questions. Both are necessary for
institutional accountability in regulated deployments.

---

## Sample Receipt

`sample-receipts/003-deny-bash-destructive.json` shows a blocked decision:
a `Bash` tool call attempting `rm -rf /` evaluated against the
`autoresearch-safe` Cedar policy.

Key fields in the sealed GDR:

```json
"gate_classification": "blocked",
"confidence_score": 0.15,
"reasoning_reconstruction": "Bash evaluated against autoresearch-safe. Gate: blocked. Confidence 0.15 below threshold or forbid matched. Action blocked.",
"tool_input": { "command": "rm -rf /" }
```

The full GDR is sealed inside the signed receipt. The signature was produced
before execution. The action never fired.

---

## Running Locally

**Requirements:** Python 3.10+, `pip install cryptography`

```bash
# From the repo root
python3 examples/testvectors-interop/gdi_driver.py
```

Receipts are written to `receipts/gdi/` (mirroring the testvectors repo layout).

**Verify signatures:**

```bash
npx @veritasacta/verify receipts/gdi/*.json \
  --key 4cb5abf6ad79fbf5abbccafcc269d85cd2651ed4b885b5869f241aedf0a5ba29
```

The keypair is the shared conformance test keypair from
`agent-governance-testvectors/fixtures/keys/README.md`. Do not use in production.

---

## Conformance Results

All three checks pass against the `ScopeBlind/agent-governance-testvectors`
conformance suite:

| Check | Result |
|-------|--------|
| Schema (v2 envelope) | PASS |
| Ed25519 signatures (`@veritasacta/verify`) | PASS |
| Chain order + `parent_receipt_hash` linkage | PASS |
