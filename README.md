# Governed Decision Intelligence (GDI)
## The Decision Architecture for Governed AI

[![Status: Open Specification](https://img.shields.io/badge/status-open%20specification-5b6cff)](#specification)
[![License: Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)
[![Version](https://img.shields.io/badge/version-v3.0-blue)](#specification)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20244601-blue)](https://doi.org/10.5281/zenodo.20244601)
[![Framework Agnostic](https://img.shields.io/badge/framework-agnostic-orange)](#framework-compatibility)
[![Prior Art](https://img.shields.io/badge/prior%20art-RGDS%20170%2B%20commits-purple)](https://github.com/mj3b/rgds)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0001--8121--2878-brightgreen)](https://orcid.org/0009-0001-8121-2878)

> *"Every governance framework tells organizations what to govern. Every platform gives tools to manage governance processes. No published specification defines the governed decision record itself."*
>
> — The GDI Thesis

---

## The Decision Layer Gap

AI governance operates at two altitudes today:

**Organizational** — NIST AI RMF, ISO 42001, EU AI Act, AIGN OS, OECD Principles govern roles, policies, risk registers, and maturity assessment. These frameworks are mature.

**System** — Model cards, bias audits, data lineage, and model lifecycle management govern AI systems. This space is emerging rapidly.

**Decision** — The individual AI-informed decision, where a specific prediction is evaluated, contextualized, and acted upon, remains ungoverned infrastructure. **No published specification defines what a governed decision record contains or how it works mechanically.**

GDI fills that gap.

---

## What GDI Is

GDI is a domain-agnostic open specification for governing AI-informed decisions at the point where a prediction becomes an action. It defines:

- **The Governed Decision Record (GDR)** — a schema-validated artifact capturing the reasoning, evidence, confidence, accountability chain, and escalation logic for a single consequential decision, written *before* execution
- **The Confidence Threshold Model** — Green/Amber/Red zones applying proportional governance based on decision risk
- **The Gate Taxonomy** — five decision outcomes (Go, Conditional Go, Defer, No-Go, Escalate) as first-class governed artifacts
- **The CI/CD Governance Integration pattern** — governance embedded as infrastructure, not oversight
- **Vertical Modules** — domain-specific extensions for biopharma, financial services, telecom, healthcare, and manufacturing

GDI sits between the AI inference layer and the governance framework layer. Below GDI, data platforms and AI models produce outputs. Above GDI, governance frameworks define what should be governed. GDI is the implementation layer that connects "we have a policy" to "we can prove what happened."

---

## The Governed Decision Record

The fundamental unit of GDI is the GDR — a single governed decision artifact written before execution.

| Element | Description |
|---------|-------------|
| Decision Question | The specific question being decided, with deadline and scope |
| AI Prediction | Model output with structured disclosure: model identity, confidence, limitations |
| Options Considered | At least two options evaluated, including inaction |
| Evidence Base | Supporting evidence with completeness classification per item |
| Risk Posture | Accepted risks, residual risks, tolerance rationale |
| Decision Outcome | Go, Conditional Go, Defer, No-Go, or Escalate |
| Accountability Chain | Named decision owner, reviewers, approvers — no delegation to systems |
| Data Provenance | Structured and unstructured sources with freshness and governance status |
| Escalation Record | Triggers, paths, and outcomes of any escalation |
| Downstream Propagation | What must change if this decision changes, with named owners |

> An artifact written after the fact is a narrative. An artifact written before execution is evidence.

---

## Framework Compatibility

GDI does not compete with existing governance frameworks. It completes them.

| Framework | Requirement | GDI Implementation |
|-----------|-------------|-------------------|
| NIST AI RMF | GOVERN: accountability structures. MAP: contextualize AI systems | GDR accountability chain satisfies GOVERN. Decision context and data provenance satisfy MAP |
| ISO/IEC 42001 | Risk management. Documented governance evidence. Control A.6.2.8 event logs | GDR risk posture fields. Schema validation provides process evidence. GDRs are the event logs |
| EU AI Act | Art. 12: automatic logging. Art. 14: human oversight. Art. 86: right to explanation | GDRs satisfy Art. 12. Accountability chains satisfy Art. 14. Decision rationale satisfies Art. 86 |
| ARAF v3.0 | Reconstructability principle: decisions reconstructable from contemporaneous records | GDRs are the contemporaneous governance records ARAF requires |
| AIGN OS | Layer 4: translate duties into workflows. Layer 1: audit-ready evidence | GDI provides decision-level implementation for Layer 4. Schema-validated GDRs provide Layer 1 artifacts |

Full mapping: [`docs/framework-compatibility.md`](docs/framework-compatibility.md)

---

## Reference Implementation

The `reference-implementation/gate-classifier/` directory contains a working Python implementation extending [Microsoft's Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit) with decision-layer classification.

AGT governs what an agent **does** (action layer: allow/deny before execution).
The gate classifier governs what **category of decision** the agent was making (decision layer: what level of human deliberation does this require?).

```python
from gate_classifier import GateClassifier, Gate

classifier = GateClassifier()
record = classifier.evaluate(
    policy_allowed=True,
    policy_confidence_threshold=0.8,
    agent_id="claims-agent-001",
    tool_name="database_write",
    tool_args={"table": "claims_decisions"},
    confidence_score=0.85,
)
# record.gate == Gate.ELEVATED_REVIEW
# record.record_hash  # SHA-256, written before execution
```

114 tests, all passing. Run standalone without AGT installed.

---

## Interoperability: Veritas Acta Receipt Standard

GDI is the 5th conforming implementation in [ScopeBlind/agent-governance-testvectors](https://github.com/ScopeBlind/agent-governance-testvectors), the cross-implementation conformance repo for [`draft-farley-acta-signed-receipts`](https://datatracker.ietf.org/doc/draft-farley-acta-signed-receipts/) (IETF). Other implementations: TypeScript (`protect-mcp`), Python (`protect-mcp-adk`), Rust (`sb-runtime`), and the APS governance hook.

The GDI driver embeds a full GDR in the receipt's signed payload before execution:

```json
result_hash = sha256(JCS(GDR))
```

All three conformance checks pass: schema validation, Ed25519 signature verification, and hash-chain integrity.

**Conformance PR:** [`ScopeBlind/agent-governance-testvectors#7`](https://github.com/ScopeBlind/agent-governance-testvectors/pull/7)
**Discussion:** [`microsoft/agent-governance-toolkit#276`](https://github.com/microsoft/agent-governance-toolkit/discussions/276)

---

## Repository Structure

```
governed-decision-intelligence/
├── spec/
│   └── GDI_v3_The_Decision_Architecture_for_Governed_AI.pdf   ← Core specification
├── schema/
│   ├── gdr.schema.json        ← Governed Decision Record JSON Schema
│   ├── gdr.schema.yaml        ← YAML companion for readability
│   └── gdr.example.json       ← Fully populated example, schema-validated
├── reference-implementation/
│   └── gate-classifier/       ← Gate classification layer for Microsoft AGT
│       ├── gate_classifier.py
│       ├── test_gate_classifier.py (114 tests)
│       └── examples/
│           └── insurance_claims.py
├── examples/
│   ├── insurance-claims/      ← Four-gate walkthrough
│   └── testvectors-interop/   ← IETF draft-farley-acta conformance driver
├── docs/
│   ├── bilateral-pattern.md
│   ├── confidence-threshold-model.md
│   ├── framework-compatibility.md
│   └── gate-taxonomy.md
├── CHANGELOG.md
├── CITATION.cff
├── CONTRIBUTING.md
├── LICENSE                    ← Apache 2.0
└── NOTICE
```

---

## Prior Art

GDI evolved from **RGDS (Regulated Gate Decision Support)**, a biopharma reference implementation developed to govern IND and BLA submission decisions.

| Repository | Purpose | Status |
|-----------|---------|--------|
| [mj3b/governed-decision-intelligence](https://github.com/mj3b/governed-decision-intelligence) | GDI Core Specification, schemas, reference implementation | This repo |
| [mj3b/rgds](https://github.com/mj3b/rgds) | Biopharma reference implementation. 170+ commits, 6 canonical examples, CI validation | v2.0.0 active |
| [mj3b/rgds-independent-study](https://github.com/mj3b/rgds-independent-study) | Ten-question independent study on FDA reconstructability and AI governance | Published · [DOI: 10.5281/zenodo.20242004](https://doi.org/10.5281/zenodo.20242004) |
| [mj3b/rgds-ai-governance](https://github.com/mj3b/rgds-ai-governance) | AI governance covenants. Non-agentic boundaries, human ownership requirements | Reference governance |

The Git commit history across these repositories provides date-stamped evidence of the design evolution. The timestamps are the prior art.

---

## Design Principles

**AI generates predictions. Humans exercise judgment.** No component in the architecture is permitted to silently decide, approve, or accept risk.

**The decision is the primary artifact.** Everything else — evidence, analysis, models, data — serves the decision record.

**Governance is infrastructure, not oversight.** Schemas, validation pipelines, and enforcement logic operate continuously and automatically.

**Risk determines rigor.** Low-risk decisions receive lightweight automated governance. High-risk decisions receive full human review with complete GDR documentation.

**Stopping early is risk reduction.** Defer and no-go are first-class governed outcomes with the same structural rigor as go decisions.

**AI assistance is optional and removable.** Every governed decision must remain defensible if all AI outputs are removed.

---

## Why This Is Hard to Build Without GDI

Five structural reasons the decision layer is absent from current governance infrastructure:

1. **IT Governance Inheritance** — frameworks evolved from IT and data governance traditions that focus on systems and data quality; individual decisions were never the governed object
2. **Static-Dynamic Mismatch** — traditional compliance operates on quarterly audit cycles; AI decisions occur at millisecond speed
3. **Wrong Abstraction Layer** — the EU AI Act classifies systems by risk level; individual decisions within a high-risk system receive no independent governance treatment
4. **Policy-Proof Gap** — "humans remain accountable" is meaningless without an operational answer to: who had the right to delegate this action, and can you demonstrate what happened?
5. **Governance as Performance** — organizations perform oversight symbolically while real decisions occur outside formal channels

---

## Citation

```bibtex
@software{banasihan2026gdi,
  author    = {Banasihan, Mark Julius},
  title     = {{GDI} v3: The Decision Architecture for Governed {AI}},
  year      = {2026},
  month     = {4},
  version   = {3.0},
  doi       = {10.5281/zenodo.20244601},
  url       = {https://doi.org/10.5281/zenodo.20244601},
  license   = {Apache-2.0}
}
```

---

## Status

GDI v2.1 is a published open specification. The schema, reference implementation, and conformance driver are in active development.

**Contributions welcome:** vertical module proposals, schema extensions, integration examples, framework compatibility analysis. See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## License

Copyright © 2026 Mark Julius Banasihan. Licensed under the [Apache License 2.0](LICENSE).

---

## Author

**Mark Julius Banasihan**
Decision governance systems for regulated, high-stakes environments.

[GitHub](https://github.com/mj3b) · [LinkedIn](https://linkedin.com/in/markjuliusbanasihan) · [ORCID](https://orcid.org/0009-0001-8121-2878) · Atlanta, Georgia, United States
