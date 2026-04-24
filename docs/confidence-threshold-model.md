# GDI Confidence Threshold Model

The confidence threshold model applies proportional governance to AI-informed decisions. Governance overhead is calibrated to decision risk — low-risk decisions receive lightweight automated oversight, high-risk or uncertain decisions receive intensive human review.

This design draws from IEC 62304 risk-based classification in medical device software and the FDA's Predetermined Change Control Plans, which govern conditions under which AI systems can evolve rather than validating each output individually.

---

## The Three Zones

| Zone | Confidence Level | Behavior | Governance Requirement |
|------|-----------------|----------|----------------------|
| GREEN | High confidence | Decision aligns with established patterns and policy boundaries. Proceeds within pre-authorized parameters. | Standard GDR logged. Human review documented, may be asynchronous. Periodic batch audit. |
| AMBER | Moderate confidence | Decision falls in uncertain range, involves novel conditions, or approaches policy boundaries. | Synchronous human review required before action. Additional evidence gathering triggered. Full GDR with justification. |
| RED | Low / Out of bounds | Decision conflicts with policy, exceeds trained domain, or addresses conditions outside governed parameters. | Mandatory escalation. No action without explicit senior human authorization. Complete GDR with escalation record. |

---

## Threshold Boundaries

Threshold values are defined per vertical module. The core specification requires that thresholds exist and are enforced. Specific values are domain-dependent.

A pharmaceutical company's AMBER zone for an IND submission decision differs fundamentally from a telecom network's AMBER zone for an automated routing decision. What remains constant is the architectural pattern: every AI-informed decision is assessed against defined thresholds, and the governance response is proportional to the assessed risk.

**Default reference thresholds (adjust per domain):**

| Boundary | Default Value | Description |
|----------|--------------|-------------|
| GREEN floor | 0.80 | Below this, AMBER triggers |
| AMBER floor | 0.50 | Below this, RED triggers |
| RED | < 0.50 | Mandatory escalation |

---

## Why This Model Exists

Two documented failure modes motivate the threshold architecture.

**Automation bias** (Parasuraman and Manzey, 2010) causes humans to over-rely on AI recommendations, particularly in high-throughput environments where decision fatigue degrades oversight quality. The threshold model forces the system to classify its own confidence and escalate uncertain decisions before they reach a fatigued human reviewer.

**Algorithm aversion** (Dietvorst, Simmons, and Massey, 2015) causes humans to abandon algorithms after observing even small errors. The threshold model preserves human agency by making the AI's uncertainty visible, allowing humans to calibrate trust appropriately rather than oscillating between blind trust and blanket rejection.

---

## Relationship to Gate Classification

Confidence zone assessment feeds directly into gate classification. A decision in the RED zone always triggers Gate 4 (Hard Escalation). A decision in the AMBER zone triggers at minimum Gate 3 (Elevated Review). A decision in the GREEN zone may still trigger Gate 3 or Gate 4 based on tool class or institutional policy — confidence is one input to gate classification, not the only input.

See: [gate-taxonomy.md](gate-taxonomy.md)

---

## GDR Field

The confidence assessment is captured in the `confidence_assessment` object of the GDR:

```json
{
  "confidence_assessment": {
    "zone": "AMBER",
    "confidence_score": 0.72,
    "policy_threshold": 0.80,
    "zone_rationale": "Confidence score 0.72 falls below policy threshold 0.80. Novel conditions detected. Synchronous human review required before execution."
  }
}
```

See: [../schema/gdr.schema.json](../schema/gdr.schema.json)
