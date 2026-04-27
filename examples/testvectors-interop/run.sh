#!/usr/bin/env bash
# GDI (Governed Decision Intelligence) conformance driver.
#
# Reads fixtures from ../../fixtures/inputs/
# Writes v2 envelope receipts (with embedded GDR payload) to ../../receipts/gdi/
#
# Signature verification requires --key because GDI uses the shared fixture
# keypair directly rather than a hosted JWKS endpoint. Pass the fixture
# public key to @veritasacta/verify:
#
#   npx @veritasacta/verify ../../receipts/gdi/*.json \
#     --key 4cb5abf6ad79fbf5abbccafcc269d85cd2651ed4b885b5869f241aedf0a5ba29
#
# Apache-2.0. https://github.com/mj3b/governed-decision-intelligence

set -uo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

command -v python3 >/dev/null 2>&1 || { echo "skip: python3 not found"; exit 77; }
python3 -c "from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey" \
    2>/dev/null || { echo "skip: pip install cryptography"; exit 77; }

python3 "$SCRIPT_DIR/gdi_driver.py"
