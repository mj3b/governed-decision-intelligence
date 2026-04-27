# The Bilateral Pattern

## What It Is

The bilateral pattern binds both sides of a governed decision into the
cryptographic receipt chain: the pre-execution GDR (intent) and the
post-execution result (outcome) are sealed as separate, chained receipts.

```
Receipt 1: sha256(JCS(GDR))        ← sealed before execution
     │
     │  previous_receipt_hash
     ▼
Receipt 2: sha256(JCS(result))     ← sealed after execution
```

Receipt 1 proves what the agent intended and why. Receipt 2 proves what
actually happened. The chain link between them proves the two receipts
belong to the same decision event and that Receipt 1 was not produced
after the fact.

---

## Why It Matters

A single post-execution receipt proves the action occurred and was
policy-compliant. It does not prove the reasoning that preceded it was sound.

A single pre-execution receipt proves the reasoning was sound at decision
time. It does not prove the action that followed matched the intent.

The bilateral pattern closes both gaps simultaneously. It is the minimum
evidence structure for regulated deployments where auditors need to verify
both the quality of the decision and the fidelity of execution.

---

## When to Use It

The bilateral pattern is warranted when:

- The deployment is in a regulated vertical (pharma, financial services,
  telecom, healthcare, insurance) where regulators distinguish intent from
  outcome in audit proceedings
- The agent has authority to execute consequential actions autonomously
  (Gate 2 or Gate 3 decisions)
- A third party -- regulator, counterparty, auditor -- needs to verify both
  sides independently without trusting the operator's infrastructure
- The threat model includes disputes about whether execution matched the
  authorized intent

For Gate 1 routine decisions at low risk, a single receipt is sufficient.
For Gate 4 escalations, execution halts before a second receipt is needed.
The bilateral pattern is most directly applicable to Gate 2 and Gate 3.

---

## How It Composes with the GDR

The GDR is the payload of Receipt 1. It carries pre-decision reasoning state:
confidence score, gate classification, evidence completeness, accountability
chain, and reasoning reconstruction.

```
Receipt 1 payload:
  result_hash = sha256(JCS(GDR))
  gdr.gate_classification = "elevated_review"
  gdr.confidence_score = 0.85
  gdr.reasoning_reconstruction = "..."
  gdr.accountability_chain = [...]
  signed before execution
```

Receipt 2 carries the execution result: what the tool returned, whether it
matched the authorized scope, and any deviation from the pre-execution intent.

```
Receipt 2 payload:
  result_hash = sha256(JCS(execution_result))
  previous_receipt_hash = sha256(JCS(Receipt 1))
  execution_matched_intent = true | false
  signed after execution
```

The chain link is the integrity guarantee. Receipt 2 cannot reference a
Receipt 1 that does not exist, and Receipt 1 cannot be backdated without
breaking the chain.

---

## Implementation Sketch

```python
# Pre-execution: seal the GDR into Receipt 1
gdr = build_gdr(tool_name, tool_input, context, decision, policy_id, ...)
receipt_1 = build_receipt(gdr_payload=gdr, prev_hash=None)
receipt_1_canonical = jcs(receipt_1)
receipt_1["signature"] = private_key.sign(receipt_1_canonical).hex()
write_to_log(receipt_1)

# Execute the action
result = execute_tool(tool_name, tool_input)

# Post-execution: seal the result into Receipt 2, chained to Receipt 1
receipt_2 = build_receipt(
    result_payload=result,
    prev_hash=sha256(receipt_1_canonical),
)
receipt_2_canonical = jcs(receipt_2)
receipt_2["signature"] = private_key.sign(receipt_2_canonical).hex()
write_to_log(receipt_2)
```

Both receipts verify independently against `@veritasacta/verify`. The chain
link is verified by walking `previous_receipt_hash` back to the genesis receipt.

---

## Relationship to the v1.1 Spec

The bilateral pattern is under active discussion in the Veritas Acta receipt
spec. The v1.1 spec introduces a `references` array that makes bilateral
composition explicit:

```json
{
  "references": [
    {
      "receipt_id": "rcpt-pre-execution",
      "relationship": "pre_execution_intent"
    }
  ]
}
```

See [VeritasActa/verify#1](https://github.com/VeritasActa/verify/issues/1)
and [VeritasActa/verify#8](https://github.com/VeritasActa/verify/issues/8)
for the closure notes and v1.1 deliverables.

GDI's pre-execution GDR is the natural payload for the `pre_execution_intent`
reference. The bilateral pattern in GDI is designed to be composable with the
v1.1 `references` array when it ships.

---

## Relationship to Regulated Vertical Requirements

| Regulation | Requirement | Bilateral Coverage |
|------------|------------|-------------------|
| EU AI Act Art. 12 | Automatic logging of decisions | Receipt 1 (intent) + Receipt 2 (outcome) |
| EU AI Act Art. 14 | Human oversight with ability to intervene | Receipt 1 seals the accountability chain before execution |
| SOC 2 Type II | Evidence of controls operating effectively | Chained receipts provide tamper-evident bilateral evidence |
| ISO 42001 A.6.2.8 | Event logs for AI system actions | Both receipts written to immutable log |
| NIST AI RMF GOVERN | Accountability structures | Receipt 1 names the accountability chain at decision time |

The bilateral pattern does not replace human review. It provides the
cryptographic infrastructure that makes human review verifiable after the fact.

---

*Part of the Governed Decision Intelligence (GDI) specification.*
*Apache-2.0. https://github.com/mj3b/governed-decision-intelligence*
