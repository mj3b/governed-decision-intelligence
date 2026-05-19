# Results Overview

This page summarizes findings across all ten research questions. Each finding is stated at a specific confidence level with the mechanism that produces it.

---

## Summary Table

| Question | Finding | Confidence |
|----------|---------|-----------|
| [Q1: Decision-Layer Gap](q1.md) | Structural gap confirmed across 6 frameworks. None specifies a governed decision record schema. GDI is the first open specification to do so. | <span class="conf-high">High</span> |
| [Q2: Eval-to-Governance Handoff](q2.md) | No published specification defines the handoff. GDI's governance covenant is a partial structural response. Full resolution requires formal connection between evaluation scope and covenant derivation. | <span class="conf-high">High</span> |
| [Q3: Confidence Score Trustworthiness](q3.md) | Model-reported confidence is valid under three conditions: in-distribution operation, non-adversarial context, calibration currency. None of these conditions is currently verified by GDI's architecture. | <span class="conf-med">Medium</span> |
| [Q4: Comprehension Threshold Problem](q4.md) | Named human authorization is structurally insufficient when the authorizing human cannot evaluate the reasoning chain. GDI exposes this as an open problem. It does not resolve it. | <span class="conf-med">Medium</span> |
| [Q5: Evidence Expiration](q5.md) | No published specification formalizes evidence expiration as a decision-level governance trigger. GDI's evidence completeness fields and propagation map are the architectural foundation. The expiration mechanism is an original contribution requiring specification. | <span class="conf-high">High</span> |
| [Q6: Conduct Collapse Detection](q6.md) | Four observable signals in GDI's structured data precede conduct collapse. Their joint trend is a strong indicator. No published paper names or measures this failure mode. | <span class="conf-med">Medium</span> |
| [Q7: Delegation Provenance](q7.md) | Delegation protocols prove authorization. GDI's GDR proves accountability. These are different objects satisfying different requirements. Both are needed for a complete agentic governance architecture. | <span class="conf-high">High</span> |
| [Q8: Agentic Speed](q8.md) | Full synchronous GDR validation is compatible with decisions above 50ms latency. Below that threshold, asynchronous validation is required. Governance integrity is preserved by covenant-defined tier assignment. | <span class="conf-med">Medium</span> |
| [Q9: Framework Compatibility](q9.md) | GDI satisfies named requirements in NIST AI RMF, ISO 42001, EU AI Act, ARAF, and AIGN OS with operational evidence from RGDS for most mappings. EU AI Act Art. 86 mapping is theoretical pending enforcement. | <span class="conf-high">High</span> |
| [Q10: Regulatory Trajectory](q10.md) | EU AI Act Art. 86 creates enforceable demand August 2026. FDA Phase 2 guidance projected 2027–28. SR 11-7 evolution is speculative. Prior art advantage window is approximately 12–24 months from May 2026. | <span class="conf-med">Medium</span> |

---

## Three Original Contributions

These three problems are absent from the published literature as of May 2026.

**Evidence Expiration as a Governance Parameter (Q5).** No published specification treats the expiry of underlying evidence as a decision-level governance trigger that creates a review obligation and a new governed record. GDI's architecture provides the foundation. The mechanism definition is an original contribution.

**Conduct Collapse as a Runtime Governance Failure Mode (Q6).** The progressive degradation of human governance behavior in AI-assisted systems — maintained formal compliance while actual oversight migrates to the AI — has not been named or measured in the published literature. Four observable signals in GDI's structured data make it detectable.

**The Comprehension Threshold Problem (Q4).** The condition under which named human authorization is insufficient for meaningful accountability — when the authorizing human cannot evaluate the model's reasoning chain — is exposed by GDI's accountability chain requirement but unresolved by any published specification. The problem is named formally here for the first time.

---

## What GDI Cannot Do

These limitations are stated before the reader finds them.

GDI cannot detect deceptive alignment. A model producing governance-compliant outputs while pursuing misaligned objectives will produce valid GDRs. GDI addresses organizational accountability failures in systems that behave as declared.

GDI cannot verify confidence score integrity. If model-reported confidence is subject to reward hacking, the threshold model ingests a corrupted input. The gate fires correctly given the input. The input may not reflect the model's actual epistemic state.

GDI does not resolve the comprehension threshold problem it exposes. Named authorization satisfies the structural requirement. It does not satisfy the philosophical requirement for meaningful control when the authorizing human lacks the domain to evaluate the reasoning chain.

GDI introduces behavioral incentives it has not fully analyzed. Schema validation under pressure can produce checkbox behavior. Accountability chains can produce accountability diffusion. These induced failure modes require measurement in production deployment.

---

## Scope Boundaries

This study makes contribution claims against the state of the published literature in May 2026. The field is moving fast. The comparison table in Q1 may require updating as new specifications publish.

The three original contributions are the author's own formulations, logically derived from GDI's architecture and the search results. They have not been validated by peer review at time of publication. They are offered as falsifiable claims subject to challenge.

---

*[View full bibliography &rarr;](../references/bibliography.md)*
