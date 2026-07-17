# Framework Evidence Mapping

## Purpose

This document maps Governed Decision Intelligence artifacts to evidence that may be relevant under external governance instruments. It records an evidentiary relationship. It does not declare certification, conformity, endorsement, or legal compliance.

Each mapping asks: which source creates the requirement, which actor and context it governs, which GDI record may supply evidence, what remains outside GDI, and what confidence the mapping earns.

## Mapping statuses

| Status | Meaning |
|---|---|
| Direct evidence relationship | The GDI artifact records information expressly requested by the source |
| Interpretive relationship | The artifact may support the source, subject to implementation or qualified interpretation |
| Hypothesis | The relationship lacks sufficient review or testing |
| Outside scope | GDI does not address the requirement |

These statuses describe evidence relevance only. They do not establish sufficiency.

## NIST AI Risk Management Framework 1.0

Official source: https://www.nist.gov/itl/ai-risk-management-framework

| Function | GDI evidence object | Relationship | Limitation |
|---|---|---|---|
| GOVERN | Accountability chain, authority scope, governance covenant, escalation path | Direct evidence relationship | GDI does not establish the full governance program |
| MAP | Decision question, scope, affected systems, evidence base, data provenance | Direct evidence relationship | System and societal context may extend beyond one decision record |
| MEASURE | Risk posture, evidence confidence, model confidence, gate rationale | Interpretive relationship | Model confidence may be uncalibrated; GDI does not perform the underlying evaluation |
| MANAGE | Outcome, conditions, escalation, stopping, downstream propagation | Direct evidence relationship | Control effectiveness and residual-risk acceptance require institutional review |

Mapping confidence: moderate. Sufficiency depends on the organization's RMF profile and implementation.

## ISO/IEC 42001:2023

Official source: https://www.iso.org/standard/81230.html

GDI can operate as one source of documented operational evidence within an artificial-intelligence management system.

| Management-system concern | GDI evidence object | Relationship | Limitation |
|---|---|---|---|
| Roles, responsibilities, and authority | Accountability chain and authority scope | Interpretive relationship | Organization-wide role design remains outside one GDR |
| AI risk assessment and treatment | Evidence base, risk posture, conditions, residual-risk statement | Interpretive relationship | GDI does not replace the management-system risk process |
| Operational planning and control | Gate classification, governance covenant, escalation path | Interpretive relationship | Control design and effectiveness require implementation evidence |
| Monitoring, measurement, and evaluation | Audit metadata, downstream propagation, monitoring records where implemented | Hypothesis | The current core schema has limited post-deployment monitoring structure |
| Documented information | Schema-validated GDR and version metadata | Direct evidence relationship | Record validity does not establish management-system conformity |

Mapping confidence: low to moderate. Clause-level conclusions require the licensed standard and qualified review.

## European Union Artificial Intelligence Act

Official source: https://eur-lex.europa.eu/eli/reg/2024/1689/oj

The Act assigns obligations according to system classification, actor role, use context, and application date. This table identifies records that may support evidence under selected provisions. It does not determine applicability.

| Provision | GDI evidence object | Relationship | Limitation |
|---|---|---|---|
| Article 12, record-keeping | Timestamps, model identity, decision context, outcome, audit metadata | Interpretive relationship | Required technical logs may contain events beyond the GDR |
| Article 13, transparency and information | AI prediction, limitations, evidence sources, decision scope | Interpretive relationship | Provider instructions and system-level information remain separate obligations |
| Article 14, human oversight | Named human authority, reviewers, escalation path, intervention gate | Interpretive relationship | A record does not prove reviewer competence, understanding, or practical influence |
| Article 26, deployer obligations where applicable | Human authority, monitoring, input-data context, incident and escalation records | Interpretive relationship | Applicability depends on actor, system, and use context |
| Article 86, explanation where applicable | Decision rationale, evidence references, system influence, authority record | Interpretive legal relationship | The right is conditional; explanation sufficiency requires legal analysis |

Mapping confidence: moderate for evidence relevance, low for legal sufficiency.

## OECD AI Principles

Official source: https://oecd.ai/en/ai-principles

| Principle | GDI evidence object | Relationship | Limitation |
|---|---|---|---|
| Transparency and responsible disclosure | Model identity, limitations, evidence, rationale | Principle-level relationship | Disclosure requirements vary by audience and context |
| Robustness, security, and safety | Risk posture, escalation, stopping, monitoring record | Principle-level relationship | GDI does not conduct security or safety evaluation |
| Accountability | Named authority, review roles, audit trail, repair ownership where implemented | Direct conceptual relationship | Accountability also requires a forum, consequences, and institutional practice |

## Decision Evidence Applicability Specification

The working Decision Evidence Applicability Specification develops a stricter evidence-to-requirement record.

Every DEAS determination must record:

- one identified evidence artifact;
- one authoritative requirement;
- the source authority, source type, and legal or normative force;
- the regulated actor and governed object;
- the decision or lifecycle stage;
- one bounded assurance proposition;
- the applicability rationale;
- required and supplied evidence;
- the assurance test;
- a determination state;
- local evidence conditions;
- the sufficiency boundary;
- at least one point of non-equivalence where applicable;
- mapping confidence, reviewer competence, and update conditions.

DEAS does not make evidence portable. It may conclude that an artifact is applicable, applicable only with local evidence, insufficient, non-equivalent, not applicable, or indeterminate.

That work remains in development. It cannot be cited as a completed cross-regime assurance method until its schema, authoritative mappings, overlays, cases, reviewer protocol, and review conditions are satisfied.

## Non-equivalence rules

A mapping fails when shared terminology hides a material difference in legal force, regulated actor, governed object, timing, evidence burden, assurance method, procedural posture, enforcement consequence, or remedy.

Structural reuse is not legal or normative equivalence. Cryptographic integrity is not assurance sufficiency. A policy-pack control mapping is not automatically an authoritative legal interpretation.

Every mature mapping must record at least one point of divergence or an evidenced explanation for why no material divergence applies.

## Adjacent-system boundary

- Microsoft Agent Governance Toolkit produces runtime policy, approval, identity, capability, enforcement, and audit events.
- ScopeBlind/Acta establishes signed-receipt schema, canonicalization, signature, attribution, ordering, and chain-verification properties.
- Credo AI provides policy packs, control mappings, governance workflows, evidence collection, compliance mapping, monitoring, and runtime governance.
- GDI structures one consequential decision record.
- HIT evaluates practical human influence.
- DEAS evaluates the bounded assurance use of a defined evidence artifact under a specified requirement.

No layer inherits another layer's claims merely because artifacts are linked.

## Review status

| Source | Last reviewed | Reviewer status |
|---|---:|---|
| NIST AI RMF 1.0 | 2026-07-16 | Author review; external review pending |
| ISO/IEC 42001:2023 | 2026-07-16 | Public-summary review; licensed-standard review pending |
| EU AI Act | 2026-07-16 | Author review; qualified legal review pending |
| OECD AI Principles | 2026-07-16 | Author review; external review pending |
| Microsoft Agent Governance Toolkit | 2026-07-17 | Public repository review; external confirmation pending |
| ScopeBlind/Acta | 2026-07-17 | Public repository and interoperability review |
| Credo AI | 2026-07-17 | Public product and Policy Pack documentation review |

Part of the Governed Decision Intelligence research repository. Apache License 2.0.
