# GDI Framework Compatibility

GDI does not compete with existing AI governance frameworks. It completes them.

The following mappings show how GDI's Governed Decision Records satisfy specific requirements of the major frameworks in production today. Organizations can adopt GDI alongside any combination of governance frameworks without conflict.

---

## Compatibility Principle

GDI is the decision-architecture layer that sits inside any governance framework. It is the implementation artifact that turns framework requirements into governed system behavior.

Organizations adopting GDI do not need to choose between frameworks. They need to implement the decision layer that makes their chosen framework enforceable at the point where AI predictions become consequential actions.

---

## Framework Mappings

### NIST AI RMF

| RMF Function | Relevant Requirement | GDI Implementation |
|-------------|---------------------|-------------------|
| GOVERN | Establish accountability structures and policies | GDR accountability chain: named decision owner, reviewers, approvers, authority scope, and escalation path |
| MAP | Contextualize AI systems in organizational and regulatory context | Decision context, evidence base, and data provenance fields in every GDR |
| MEASURE | Analyze and assess AI risk | Confidence threshold model produces quantified risk assessment per decision |
| MANAGE | Prioritize and address AI risk | Gate taxonomy routes decisions to appropriate human oversight based on assessed risk |

---

### ISO/IEC 42001

| Requirement | GDI Implementation |
|------------|-------------------|
| Risk management for AI systems | GDR risk posture and residual risk fields. Explicit risk acceptance required field. |
| Documented evidence of governance processes | Schema validation provides process evidence. Every GDR is machine-readable proof of governance execution. |
| Control A.6.2.8 event logs | GDRs are the event logs. Written before execution. Immutable after. SHA-256 integrity verification. |
| Human oversight requirements | Accountability chain requires named humans. Gate 3 and Gate 4 enforce synchronous human review architecturally. |

---

### EU AI Act

| Article | Requirement | GDI Implementation |
|---------|------------|-------------------|
| Article 12 | Automatic logging of events relevant to high-risk AI systems | GDRs satisfy Art. 12. Every consequential decision produces a schema-validated log record before execution. |
| Article 14 | Human oversight measures for high-risk AI systems | Accountability chains satisfy Art. 14. Gate 3 and Gate 4 make human oversight architecturally enforced, not policy-dependent. |
| Article 86 | Right to explanation of individual decisions | Decision rationale and reasoning reconstruction fields in every GDR satisfy Art. 86's per-decision explanation requirement. |
| Article 13 | Transparency and provision of information | AI prediction disclosure fields: model identity, confidence score, known limitations. |

---

### ARAF v3.0

| ARAF Principle | GDI Implementation |
|---------------|-------------------|
| Reconstructability principle: decisions must be reconstructable from contemporaneous governance records | GDRs are the contemporaneous governance records ARAF requires. Written before execution, immutable after. |
| Chain-complete evidence across the Decision Supply Chain | GDR data provenance fields span structured and unstructured sources. Every link in the evidence chain is captured. |
| Decision Supply Chain traceability | Downstream propagation fields identify what must change if this decision changes, with named owners. |

ARAF's reconstructability principle is the closest existing work to GDI's core claim. GDI is positioned as the artifact layer that makes reconstructability mechanically achievable rather than aspirationally required.

---

### AIGN OS

| Layer | Requirement | GDI Implementation |
|-------|------------|-------------------|
| Layer 4: Governance Implementation | Translate governance duties into operational workflows | GDI provides decision-level implementation for Layer 4. The GDR is the workflow artifact that proves governance execution. |
| Layer 1: Trust Infrastructure | Audit-ready evidence of governance | Schema-validated GDRs with SHA-256 integrity verification provide Layer 1 audit artifacts. |

---

### OECD AI Principles

| Principle | GDI Implementation |
|----------|-------------------|
| Transparency and explainability | AI disclosure protocol: tool identity, purpose, human review tiers, confidence band, cautions. |
| Accountability | Accountability chain requires named human decision owner. No delegation to systems. |
| Human-centered values | Confidence threshold model and gate taxonomy enforce human review at proportional points. AI assists; humans decide. |
| Robustness and safety | Gate 4 hard escalation ensures autonomous action cannot proceed outside governed parameters. |

---

## What Framework Compatibility Does Not Mean

GDI compatibility with a framework means GDI's artifacts satisfy specific requirements of that framework. It does not mean:

- Adopting GDI automatically certifies compliance with any framework
- GDI replaces the organizational, process, and assessment requirements of any framework
- GDI is endorsed by or affiliated with any framework organization

Organizations remain responsible for their own compliance assessments. GDI provides the decision-layer artifacts that support those assessments.

---

## Three Governance Altitudes

| Altitude | What It Governs | Who Has Built This | Status |
|----------|----------------|-------------------|--------|
| Organizational | Roles, policies, risk registers, board oversight, maturity assessment | NIST AI RMF, ISO 42001, AIGN OS, EU AI Act, OECD Principles | Mature |
| System | Model cards, bias audits, data lineage, model lifecycle, observability | OneTrust, IBM OpenPages, Credo AI, model registries | Emerging |
| Decision | Individual AI-informed decisions with provenance, accountability, and audit trail | **GDI** | This specification |

GDI occupies the decision altitude. The organizational and system altitudes are necessary but not sufficient. Without the decision layer, governance frameworks cannot produce proof of what happened at the moment a prediction became a consequential action.
