# Research Protocol and Claim Register

## Purpose

This document defines what Governed Decision Intelligence claims, how those claims are tested, which evidence supports them, and what remains unresolved. It governs research statements across the specification, schemas, examples, reference implementation, framework mappings, and working specifications.

## Research object

GDI is a design-science artifact. The repository constructs and tests a decision-record architecture for AI-assisted and agent-mediated actions. The unit of analysis is one consequential decision at the point where an AI output may become an institutional action.

The primary research question is:

> Can a schema-validated record make the authority, evidence, uncertainty, alternatives, and intervention conditions of an AI-informed decision reconstructable before execution?

The current repository can test representation, validation, deterministic routing, and record integrity. It cannot yet establish institutional outcome improvement, legal sufficiency, or substantive human judgment in deployed settings.

## Bounded contribution

The repository contributes an open decision-record specification containing:

- a Governed Decision Record schema;
- a five-outcome decision taxonomy;
- a four-level deliberation gate taxonomy;
- a deterministic Python reference classifier;
- a signed-receipt interoperability experiment;
- a working specification for cross-regime decision-evidence applicability, sufficiency boundaries, and non-equivalence.

A literature search completed in May 2026 did not identify an open specification that combined the same record objects, validation rules, gate model, and pre-execution evidence pattern. Later or missed work may narrow that finding. The review must remain revisable.

## Method

The research program uses four methods.

### Artifact construction

The specification defines governance objects and their relationships. The JSON Schema turns those objects into a machine-checkable contract. The Python reference implementation demonstrates one executable interpretation of gate classification and record sealing.

### Literature and adjacent-work review

The review covers scholarly publications, official governance instruments, open technical specifications, and vendor documentation that defines adjacent runtime or assurance layers. Novelty statements use the form “the review did not identify” because absence cannot be proven exhaustively.

The current adjacent-system boundary distinguishes:

- Microsoft Agent Governance Toolkit as runtime action governance and policy enforcement;
- ScopeBlind/Acta as signed-receipt interoperability and cryptographic verification;
- Credo AI as policy-pack, control-mapping, workflow, evidence-collection, and runtime-governance infrastructure;
- GDI as the governed decision-record layer;
- Human Influence Telemetry as documentary assessment of practical human influence;
- Decision Evidence Applicability Specification as bounded evidence-to-requirement qualification.

### Technical validation

Repository validation checks:

1. JSON Schema validity under Draft 2020-12;
2. populated-example validation with format checking;
3. top-level contract parity between the JSON and YAML schema files;
4. deterministic gate-classifier behavior across the included test suite;
5. integrity failure after modification to sealed fields;
6. deterministic interoperability fixtures;
7. Ed25519 signature verification and receipt-chain linkage;
8. Citation File Format validity.

Passing tests establish behavior for the included artifacts and fixtures. They do not establish field performance or regulatory sufficiency.

### Comparative evidence mapping

Framework mappings connect GDR fields to evidence that may be relevant under external instruments. Every mapping must identify source authority, source type, legal or normative force, regulated actor, governed object, GDI evidence object, rationale, limitation, confidence, and review date.

The mapping output states evidence relevance. It never declares legal compliance.

DEAS strengthens this method by requiring one bounded assurance proposition, an applicability determination, local evidence conditions, a sufficiency boundary, and a point of non-equivalence. Applicability does not mean sufficiency, and structural reuse does not mean legal or normative portability.

## Evidence classes

| Class | Definition | Example |
|---|---|---|
| E1: Executable evidence | A repeatable test produces the stated result | GDR example validates against the schema |
| E2: Artifact evidence | A versioned artifact directly contains the claimed property | GDR requires an accountability chain |
| E3: External source evidence | An official instrument or scholarly publication supports the mapped concept | NIST AI RMF describes accountability and risk-management functions |
| E4: Comparative inference | A reasoned mapping links an external requirement to a GDI field | GDR logging fields may support an Article 12 evidence request |
| E5: Research hypothesis | The claim requires field data, independent review, or further implementation | GDI improves decision quality in deployment |

## Claim register

| ID | Claim | Evidence | Current status | Update condition |
|---|---|---|---|---|
| C1 | The GDR schema can represent the included decision objects in one machine-readable record | Schema, example, CI | Demonstrated for included fixtures | Revise when schema changes or a required object cannot be represented |
| C2 | The reference classifier produces deterministic gate outcomes for the included rules | Test suite | Demonstrated internally | Revise after rule changes, failed tests, or external replication |
| C3 | Modification to sealed gate-record fields can be detected | Hash tests | Demonstrated for the current hash profile | Revise when canonicalization or the sealed-field set changes |
| C4 | GDI can embed decision evidence in signed receipts | Local interoperability fixtures | Demonstrated locally | Upgrade after external conformance acceptance |
| C5 | GDI is an accepted conforming implementation of the ACTA test-vector suite | Open external pull request | Pending | Upgrade only after external acceptance |
| C6 | GDR evidence may support selected NIST, ISO, EU, and OECD governance requirements | Official sources and interpretive mapping | Provisional | Revise after qualified standards or legal review |
| C7 | A completed GDR proves substantive human judgment | No direct evidence | Unsupported | Requires Human Influence Telemetry and field observation |
| C8 | GDI improves institutional outcomes | No comparative deployment study | Unresolved | Requires pre-registered field evaluation or credible comparative study |
| C9 | GDI is the first specification of its kind | May 2026 literature review | Provisional novelty claim | Narrow when prior or later work covers the same contribution |
| C10 | A defined decision-evidence artifact can be evaluated for applicability, local evidence conditions, sufficiency boundaries, and non-equivalence under a specified governance requirement | DEAS v0.2.0 working specification | Working hypothesis | Requires schema, authoritative mappings, overlays, cases, reviewer protocol, and external review |
| C11 | Decision evidence is legally or normatively portable across governance regimes | No valid general evidence | Unsupported | Would require a bounded regime pair and proof that authority, actor, scope, threshold, procedure, and consequence remain equivalent |

## Construct definitions

### Reconstructability

A decision is reconstructable when a reviewer can identify the decision question, available evidence, alternatives, stated uncertainty, applicable authority, required deliberation, outcome, and downstream obligations from contemporaneous records. Reconstructability does not establish truth, legality, fairness, or good judgment.

### Human authority

Human authority means a named person or institutional role holds the power to authorize, reject, stop, escalate, appeal, repair, or change the governing system. Automated actors may execute within documented delegation. The delegating human authority remains identifiable.

### Decision evidence

Decision evidence is the set of contemporaneous records used to assess how an AI-informed action was framed and authorized. It includes source provenance, decision context, control events, review actions, recorded reasons, and integrity metadata.

### Evidence applicability

Evidence applicability is the relationship between one defined artifact and the actor, object, stage, scope, and assurance proposition governed by one identified external requirement.

Applicability means relevance. It does not establish sufficiency, conformity, certification, admissibility, or legal compliance.

### Gate classification

Gate classification is an institutional rule assigning a required level of deliberation to a proposed action. It is independent of the model being governed. Model confidence may enter the rule as one input.

## Threats to validity

The novelty review can miss unpublished work, proprietary systems, non-English sources, newly released material, or work using different terminology. A complete record may capture ceremonial oversight. Model-reported confidence may be absent or poorly calibrated. A valid hash proves consistency of sealed fields, not truth. Included examples do not establish performance in other domains. Framework mappings require qualified review. Compromised telemetry or governance-layer bypass can defeat the record.

Cross-regime evidence work adds further threats: shared terms may hide different actor duties or legal force; vendor taxonomies may be mistaken for authoritative requirements; cryptographic integrity may be mistaken for substantive sufficiency; policy-pack reuse may be mistaken for legal equivalence; and an evidence relationship accepted in one jurisdiction may fail under another.

## Review protocol

Internal validation supports “demonstrated in the included implementation.” External replication supports “independently reproduced.” Accepted conformance supports “conforming to the tested profile.” Qualified legal or standards review supports a bounded conformity interpretation. Comparative field evidence supports outcome claims.

DEAS determinations require review competence appropriate to the source authority. A technical reviewer may evaluate schema and provenance behavior. Legal sufficiency requires qualified legal review. Standards conformity requires access to the authoritative standard and qualified interpretation.

Repository language must be downgraded when the supporting condition no longer holds.

## Release criteria

A stable research release requires all validation checks to pass, synchronized schemas and examples, migration notes for normative changes, an updated claim register and limitations, accurate external-review status, matching citation metadata, and a DOI pointing to the exact released artifact.

A release containing DEAS work must also preserve the adjacent-system boundaries, prohibit unqualified portability claims, and distinguish evidence relevance from assurance sufficiency.

## Update cadence

Adjacent-work review is quarterly. Framework-source review occurs at least annually and after material legal or standards changes. The claim register is reviewed for every numbered release.
