#!/usr/bin/env python3
"""Deterministic local checks for the GDI signed-receipt driver."""

from __future__ import annotations

import json
from pathlib import Path

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

from gdi_driver import PUBKEY_HEX, build_receipt, jcs, sha256p

ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "fixtures" / "inputs"


def main() -> None:
    fixture_paths = sorted(FIXTURES.glob("*.json"))
    assert fixture_paths, f"no fixtures found in {FIXTURES}"

    public_key = Ed25519PublicKey.from_public_bytes(bytes.fromhex(PUBKEY_HEX))
    previous_canonical = None

    for index, fixture_path in enumerate(fixture_paths, start=1):
        fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
        receipt, canonical = build_receipt(
            fixture,
            fixture.get("sequence", index),
            previous_canonical,
        )

        assert receipt["payload"]["decision"] == fixture["expected_decision"]
        assert receipt["payload"]["gdr"]["gate_classification"] == fixture["expected_gate"]
        assert receipt["payload"]["result_hash"] == sha256p(jcs(receipt["payload"]["gdr"]))

        expected_parent = sha256p(previous_canonical) if previous_canonical else None
        assert receipt["parent_receipt_hash"] == expected_parent
        assert receipt["payload"]["prev_hash"] == expected_parent

        unsigned = dict(receipt)
        signature = bytes.fromhex(unsigned.pop("signature"))
        public_key.verify(signature, jcs(unsigned))

        receipt_again, canonical_again = build_receipt(
            fixture,
            fixture.get("sequence", index),
            previous_canonical,
        )
        assert receipt_again == receipt
        assert canonical_again == canonical

        previous_canonical = canonical

    print(f"interop driver: PASS ({len(fixture_paths)} deterministic receipts)")


if __name__ == "__main__":
    main()
