# GDI Confidence Threshold Model

Proportional governance requires a mechanism for calibrating oversight intensity to decision risk. The confidence threshold model provides that mechanism by classifying every AI-informed decision into one of three zones before execution, then routing it to a governance response appropriate to that zone.

The design draws from two converging bodies of evidence: IEC 62304 risk-based classification in medical device software, which defines three safety classes requiring proportionally different development rigor; and FDA Predetermined Change Control Plans, which govern conditions under which AI systems can evolve without re-validation of each output. Both establish that governance overhead proportional to risk is not a concession to practicality. It is the architecturally correct response.

---

## The Three Zones

| Zone | Confidence Level | Governance Requirement |
|------|-----------------|------------------------|
| GREEN | High (above GREEN floor threshold) | Standard GDR logged. Human review documented; may be asynchronous. Periodic batch audit. |
| AMBER | Moderate (between AMBER floor and GREEN floor) | Synchronous human review required before action. Additional evidence gathering triggered. Full GDR with justification. |
| RED | Low or out of bounds (below AMBER floor) | Mandatory escalation. No action without explicit senior human authorization. Complete GDR with escalation record. |

---

## Threshold Boundaries

Threshold values are defined per vertical module. The core specification requires that thresholds exist and are enforced. Specific values are domain-dependent: a pharmaceutical company's AMBER zone for an IND submission decision differs from a telecom network's AMBER zone for an automated routing decision.

**Default reference thresholds (adjust per domain):**

| Boundary | Default Value | Interpretation |
|----------|--------------|----------------|
| GREEN floor | 0.80 | Scores below this enter AMBER |
| AMBER floor | 0.50 | Scores below this enter RED |
| RED | Below 0.50 | Mandatory escalation, no exceptions |

These defaults are starting points. Vertical modules override them based on domain-specific error cost analysis. In a clinical hold context, the GREEN floor may be 0.92. In a routine customer service context, it may be 0.65. The architecture is the same; the calibration is domain-specific.

---

## Why This Model Exists

Two documented failure modes motivate the threshold architecture.

Automation bias (Parasuraman and Manzey, 2010) causes humans to over-rely on AI recommendations, particularly in high-throughput environments where decision fatigue degrades oversight quality. The threshold model forces the system to classify its own confidence and route uncertain decisions to escalation before they reach a fatigued human reviewer who may not recognize the uncertainty.

Algorithm aversion (Dietvorst, Simmons, and Massey, 2015) causes humans to abandon algorithmic support after observing even small errors. The threshold model preserves human agency by making the AI's uncertainty visible at decision time, allowing humans to calibrate trust based on disclosed confidence rather than oscillating between uncritical acceptance and blanket rejection.

Both failure modes produce worse outcomes than proportional governance. Automation bias produces over-reliance on outputs that should have been escalated. Algorithm aversion produces under-reliance on outputs that are reliable. The threshold architecture corrects both by making confidence legible and routing governance accordingly.

---

## Relationship to Gate Classification

Confidence zone assessment is one input to gate classification, not the only one. A RED zone decision always triggers Gate 4 (Hard Escalation). An AMBER zone decision triggers at minimum Gate 3 (Elevated Review). A GREEN zone decision may still trigger Gate 3 or Gate 4 based on tool class or institutional policy override — a high-confidence write to a regulated financial record may require elevated review regardless of confidence score.

See: [gate-taxonomy.md](gate-taxonomy.md)

---

## GDR Field

The confidence assessment is captured in the `confidence_assessment` object of every GDR:

```json
{
  "confidence_assessment": {
    "zone": "AMBER",
    "confidence_score": 0.72,
    "policy_threshold": 0.80,
    "zone_rationale": "Confidence score 0.72 falls below policy threshold 0.80. Novel conditions detected: no prior precedent for this claim category in training corpus. Synchronous human review required before execution."
  }
}
```

See: [../schema/gdr.schema.json](../schema/gdr.schema.json)

---

*Part of the Governed Decision Intelligence (GDI) specification. Apache 2.0.*
*[https://github.com/mj3b/governed-decision-intelligence](https://github.com/mj3b/governed-decision-intelligence)*
