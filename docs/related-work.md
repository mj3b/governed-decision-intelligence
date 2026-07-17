# Related Work and Scope Boundary

GDI occupies the decision-evidence layer between runtime controls and institutional assurance. Adjacent systems may enforce policy, evaluate models, establish cryptographic integrity, harmonize governance requirements, or define organizational duties. GDI records what the institution knew, authorized, and required around one consequential decision.

## Organizational governance frameworks

NIST AI RMF, ISO/IEC 42001, the OECD AI Principles, and the European Union Artificial Intelligence Act define governance functions, management processes, actor duties, or legal requirements. They provide authority and assessment context. GDI is one possible source of operational evidence within those programs.

## Runtime agent governance

Microsoft Agent Governance Toolkit addresses runtime action governance through policy evaluation, identity and capability checks, approval controls, action interception, sandboxing, allow or deny decisions, and audit events.

Credo AI provides policy packs, policy-to-code translation, risk and control mappings, governance workflows, evidence collection, compliance mapping, monitoring, and runtime agent-governance capabilities.

Their central runtime question is whether an agent action is permitted, constrained, escalated, or sanctioned under configured governance.

GDI asks a different question: what consequential decision was being made, which evidence and uncertainty shaped it, what human or institutional authority applied, which deliberation gate fired, and what record can later support audit, appeal, repair, or reassessment?

The systems can interoperate through this sequence:

```text
external requirement or institutional policy
        → configured runtime control
        → policy or enforcement event
        → Governed Decision Record
        → human-influence assessment
        → evidence-applicability determination
        → assurance, audit, appeal, repair, or reassessment
```

GDI does not compile policy into an agent harness, provide policy packs, prescribe a universal runtime governor, or automate compliance.

## Signed receipts and cryptographic evidence

ScopeBlind agent-governance test vectors and Acta signed receipts address schema, canonicalization, signature validity, attribution, ordering, and chain linkage across implementations.

A GDR can supply decision semantics inside or referenced by a receipt. The receipt layer can attest to defined integrity properties of the payload or event sequence.

Cryptographic integrity and governance quality remain distinct. A valid signature can attest to a poor, incomplete, or inaccurate decision record. Receipt interoperability does not establish that the payload satisfies a legal, institutional, or assurance requirement.

The GDI interoperability experiment tests whether the two evidence layers can be composed. It does not claim that GDI defines the receipt protocol.

## Model and system documentation

Model cards, system cards, data statements, evaluation reports, risk registers, and model inventories describe systems or releases. A GDR records one decision instance. It may reference those artifacts as evidence while preserving the local decision question, authority, outcome, and conditions.

## Accountability theory

Bovens' accountability model treats accountability as a relationship in which an actor must explain and justify conduct to a forum that can question and impose consequences. GDI operationalizes parts of that relationship through named roles, recorded reasons, escalation, and audit evidence. The forum, contest process, sanctions, and institutional legitimacy remain outside the core record.

## Meaningful human control and human influence

Meaningful human control research asks whether human reasons and responsibility remain connected to system behavior. Human Influence Telemetry extends this concern into observable workflow evidence: evidence access, independent reasoning, override capability, appeal ownership, repair responsibility, and system-change authority.

GDI records the declared authority structure. HIT evaluates whether that authority retained practical force.

## Decision science and phase-gate methods

GDI draws on structured decision analysis and phase-gate practices that make alternatives, evidence, uncertainty, conditions, stopping, and approval explicit. The reference implementation adapts these ideas to AI-assisted and agent-mediated decisions. Domain calibration remains an institutional task.

## Decision Evidence Applicability Specification

The working Decision Evidence Applicability Specification asks whether a defined evidence artifact is relevant to one identified governance requirement, what bounded assurance proposition it may support, what additional local evidence is required, where it is insufficient, and where apparent equivalence fails.

DEAS does not claim that governance, controls, findings, evidence, or legal conclusions are portable across regimes.

DEAS also does not replace:

- Microsoft AGT runtime enforcement;
- ScopeBlind/Acta receipt interoperability and cryptographic verification;
- Credo AI policy packs, control mappings, governance workflows, or runtime capabilities;
- GDI decision-record construction;
- HIT assessment of practical human influence.

Its schema, authoritative mappings, overlays, cases, reviewer protocol, and validation suite remain in development.

## Contribution boundary

The project claims an integrated open artifact composed of a decision-record schema, gate taxonomy, reference classifier, evidence-preservation pattern, and working evidence-applicability method. It does not claim ownership of accountability theory, human oversight, runtime policy enforcement, cryptographic receipts, policy-pack governance, model documentation, phase-gate decision methods, or legal interpretation.

The dated literature review did not identify an open specification combining the same elements. This finding remains provisional and must narrow when overlapping prior work is found.

## Public references reviewed

- Microsoft Agent Governance Toolkit: https://github.com/microsoft/agent-governance-toolkit
- ScopeBlind agent-governance test vectors: https://github.com/ScopeBlind/agent-governance-testvectors
- Credo AI: https://www.credo.ai/
- Credo AI Policy Packs: https://www.credo.ai/glossary/credo-ai-policy-pack
