# Insurance Claims Processing — Gate Classification Walkthrough

This example demonstrates GDI gate classification across all four gate levels using an insurance claims processing agent as the reference scenario. It is the canonical worked example for understanding how gate levels differ and why each level exists.

---

## The Scenario

An AI agent processes incoming insurance claims. Microsoft AGT handles policy enforcement at the action layer — allow/deny before execution. The GDI gate classifier handles decision-layer accountability — what level of human deliberation does this decision require?

These are adjacent but not identical questions. AGT answers: "is this action permitted?" The gate classifier answers: "given that it is permitted, what governance applies to this specific decision?"

An action can be permitted by policy and still require human review before it executes. An action can be denied by policy and still require a governed record of why and what authority was escalated to. The gate classifier captures both.

---

## Running the Example

```bash
cd reference-implementation/gate-classifier
python examples/insurance_claims.py
```

No AGT installation required. The example uses a `MockPolicyInterceptor` that mirrors AGT's `PolicyInterceptor.intercept()` interface. Replace it with the real `BaseIntegration` subclass when AGT is installed.

**Output:** Four gate records printed to console. A `gate_records_insurance_claims.ndjson` file written with all four records, each SHA-256 hashed before execution.

---

## The Four Gates

| Scenario | Tool | Confidence | AGT Decision | Gate |
|----------|------|-----------|-------------|------|
| Retrieve claim file | `file_read` | 0.97 | Allow | Gate 1 — Routine Execution |
| Verify medical coding | `web_search` | 0.88 | Allow | Gate 2 — Documented Delegation |
| Write claim decision | `database_write` | 0.85 | Allow | Gate 3 — Elevated Review |
| Bulk delete records | `bulk_delete` | 0.91 | Deny | Gate 4 — Hard Escalation |

---

## Gate 1 — Routine Execution

Confidence 0.97 is GREEN. Tool is read-only. AGT allows. The decision is routine and pre-authorized. No human deliberation is required at decision time. The gate record is written automatically and the action proceeds.

This is the most common gate in high-throughput deployments. The governance overhead is minimal: a hash-sealed record exists before execution, enabling audit without requiring synchronous human involvement.

---

## Gate 2 — Documented Delegation

Confidence 0.88 is GREEN. Tool is informational. The action falls within a pre-authorized auto-approval policy (`AUTO-APPROVAL-POLICY-v2.3`). No human deliberation is required at decision time because a human authority previously deliberated and pre-authorized this decision class.

Gate 2 is the governed record of that delegation. The upstream human authority's prior deliberation covers this decision. The record references the delegation document, creating a traceable link between the pre-authorization and the specific action it covers.

---

## Gate 3 — Elevated Review

Confidence 0.85 is GREEN, but the tool is `database_write` — a consequential action modifying a claims decision record. AGT allows the action. The gate classifier flags it for elevated review because the tool class carries institutional weight beyond what the confidence score alone determines.

This is the key architectural distinction. Policy compliance and governance adequacy are not the same question. An action that is permitted may still require human review based on its category, context, or downstream consequences. Gate 3 captures decisions where the institution has determined that human acknowledgment is required regardless of confidence.

---

## Gate 4 — Hard Escalation

AGT policy denies `bulk_delete` outright. The gate classifier fires Gate 4. `EscalationRequired` is raised. Execution halts. The GDR is written to the audit log before the halt. Human authority is required before any retry.

```
>>> EXECUTION HALTED <<<
Human authority required before this action can proceed.
GDR written to audit log before halt.
```

Gate 4 produces a governed record of the halt: why the escalation triggered, what authority the decision was routed to, and (when resolved) what that authority decided. A halt without a record is indistinguishable from a failure. Gate 4 makes them distinguishable.

---

## What Each Record Contains

Every gate record is written before execution:

- `gate` — the classification outcome
- `gate_rationale` — institutional explanation
- `confidence_score` — against the policy threshold
- `reasoning_reconstruction` — plain-language derivation from structured fields only
- `record_hash` — SHA-256 of immutable fields at classification time
- `escalation_required` / `escalation_trigger` — populated when Gate 4 fires

The hash enables tamper detection. Any post-hoc modification of a record produces a hash mismatch.

---

## AGT and GDI Together

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

AGT and GDI answer different questions. Neither replaces the other.

---

*Part of the Governed Decision Intelligence (GDI) reference implementation. Apache 2.0.*
