# Insurance Claims Processing — Gate Classification Example

This example demonstrates GDI gate classification across all four gate levels
using an insurance claims processing agent as the reference scenario.

---

## The Scenario

An AI agent processes incoming insurance claims. Microsoft AGT handles policy
enforcement at the action layer -- allow/deny before execution. The GDI gate
classifier handles decision-layer accountability -- what level of human
deliberation does this decision require?

These are adjacent but not identical questions. AGT answers: "is this action
permitted?" The gate classifier answers: "given that it is permitted, what
governance applies to this specific decision?"

---

## Running the Example

```bash
cd reference-implementation/gate-classifier
python examples/insurance_claims.py
```

No AGT installation required. The example uses a `MockPolicyInterceptor` that
mirrors AGT's `PolicyInterceptor.intercept()` interface. Replace it with the
real `BaseIntegration` subclass when AGT is installed.

**Output:** Four gate records printed to console. A `gate_records_insurance_claims.ndjson`
file is written with all four records, each SHA-256 hashed before execution.

---

## The Four Gates

| Scenario | Tool | Confidence | AGT Decision | Gate |
|----------|------|-----------|-------------|------|
| Retrieve claim file | `file_read` | 0.97 | Allow | Gate 1 — Routine |
| Verify medical coding | `web_search` | 0.88 | Allow | Gate 2 — Documented Delegation |
| Write claim decision | `database_write` | 0.85 | Allow | Gate 3 — Elevated Review |
| Bulk delete records | `bulk_delete` | 0.91 | **Deny** | Gate 4 — Hard Escalation |

### Gate 1 — Routine Execution
Confidence 0.97 is GREEN. Tool is read-only. AGT allows. Decision is routine
and pre-authorized. No deliberation required. Record written, action proceeds.

### Gate 2 — Documented Delegation
Confidence 0.88 is GREEN. Tool is informational. Action falls within a
pre-authorized auto-approval policy (`AUTO-APPROVAL-POLICY-v2.3`). The
upstream human authority's prior deliberation covers this decision. Record
references the delegation document.

### Gate 3 — Elevated Review
Confidence 0.85 is GREEN but the tool is `database_write` -- a consequential
action that modifies a claims decision record. AGT allows the action. The gate
classifier flags it for elevated review because the decision category
(recording a financial approval) carries institutional weight beyond what the
confidence score alone determines.

### Gate 4 — Hard Escalation
AGT policy denies `bulk_delete` outright. The gate classifier fires Gate 4.
`EscalationRequired` is raised. Execution halts. The GDR is written to the
audit log before the halt. Human authority is required before any retry.

```
>>> EXECUTION HALTED <<<
Human authority required before this action can proceed.
Record written to audit log before halt.
```

---

## What the Record Captures

Each GateRecord is written **before execution** and contains:

- `gate` -- the classification outcome
- `gate_rationale` -- institutional explanation
- `confidence_score` -- against the policy threshold
- `reasoning_reconstruction` -- plain-language derivation from structured fields only
- `record_hash` -- SHA-256 of immutable fields at classification time
- `escalation_required` / `escalation_trigger` -- when Gate 4 fires

The hash enables tamper detection. Any post-hoc modification produces a
mismatch. The record is evidence, not narrative.

---

## AGT + GDI Together

```
Agent action
     │
     ▼
AGT PolicyInterceptor.intercept()   ← Action layer: allow / deny
     │
     ▼ (if allowed)
GDI GateClassifier.evaluate()       ← Decision layer: what governance applies?
     │
     ├── Gate 1/2: proceed
     ├── Gate 3: proceed + flag for review
     └── Gate 4: halt + raise EscalationRequired
```

AGT and GDI are complementary. Neither replaces the other.
