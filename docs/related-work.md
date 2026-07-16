# Related Work and Scope Boundary

GDI occupies the decision-evidence layer between runtime controls and institutional assurance. Adjacent systems may enforce policy, evaluate models, establish cryptographic integrity, or define organizational duties. GDI records what the institution knew, authorized, and required around one consequential decision.

## Organizational governance frameworks

NIST AI RMF, ISO/IEC 42001, the OECD AI Principles, and the European Union Artificial Intelligence Act define governance functions, management processes, actor duties, or legal requirements. They provide the authority and assessment context. GDI is one possible source of operational evidence within those programs.

## Runtime agent governance

Microsoft Agent Governance Toolkit and Credo AI Agent Governor address harness-level controls such as permissions, policy checks, approval points, action boundaries, and enforcement events. Their central question is whether an agent action is permitted under configured policy.

GDI asks a related question: what decision was being made, which evidence and uncertainty shaped it, what human authority applied, which deliberation gate fired, and what record can later support audit, appeal, or repair?

The systems can interoperate through this sequence:

```text
external obligation or policy
        → configured runtime control
        → policy or enforcement event
        → Governed Decision Record
        → assurance, audit, appeal, or repair
```

GDI does not compile policy into an agent harness or prescribe a universal runtime governor.

## Signed receipts and cryptographic evidence

ACTA signed receipts and related receipt standards establish integrity, attribution, ordering, and chain linkage. They answer whether a record was altered and which issuer produced it. A GDR supplies the decision semantics placed inside or referenced by the receipt.

Cryptographic integrity and governance quality remain distinct. A valid signature can attest to a poor or inaccurate decision record. The interoperability experiment tests whether the two evidence layers can be combined.

## Model and system documentation

Model cards, system cards, data statements, evaluation reports, risk registers, and model inventories describe systems or releases. A GDR records one decision instance. It may reference those artifacts as evidence while preserving the local decision question, authority, outcome, and conditions.

## Accountability theory

Bovens' accountability model treats accountability as a relationship in which an actor must explain and justify conduct to a forum that can question and impose consequences. GDI operationalizes parts of that relationship through named roles, recorded reasons, escalation, and audit evidence. The forum, contest process, sanctions, and institutional legitimacy remain outside the core record.

## Meaningful human control and human influence

Meaningful human control research asks whether human reasons and responsibility remain connected to system behavior. Human Influence Telemetry extends this concern into observable workflow evidence: evidence access, independent reasoning, override capability, appeal ownership, repair responsibility, and system-change authority.

GDI records the declared authority structure. HIT tests whether that authority had practical force.

## Decision science and phase-gate methods

GDI draws on structured decision analysis and phase-gate practices that make alternatives, evidence, uncertainty, conditions, stopping, and approval explicit. The reference implementation adapts these ideas to AI-assisted and agent-mediated decisions. Domain calibration remains an institutional task.

## Decision Evidence Portability Specification

The working Decision Evidence Portability Specification asks which decision-evidence objects can support assurance across several governance regimes, where local overlays are required, and where apparent equivalence fails. Its schema, overlays, case studies, and review conditions remain in development.

## Contribution boundary

The project claims an integrated open artifact composed of a decision-record schema, gate taxonomy, reference classifier, and evidence-preservation pattern. It does not claim ownership of accountability theory, human oversight, runtime policy enforcement, cryptographic receipts, model documentation, or phase-gate decision methods.

The dated literature review did not identify an open specification combining the same elements. This finding remains provisional and must narrow when overlapping prior work is found.