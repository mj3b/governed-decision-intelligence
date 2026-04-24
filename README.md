# Governed Decision Intelligence (GDI)
## The Decision Architecture for Governed AI

<!-- GDI governance signals -->
[![Status: Open Specification](https://img.shields.io/badge/status-open%20specification-5b6cff)](#specification)
[![License: Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-green)](LICENSE)
[![Version](https://img.shields.io/badge/version-v2.0-blue)](#specification)
[![Framework Agnostic](https://img.shields.io/badge/framework-agnostic-orange)](#framework-compatibility)
[![Prior Art](https://img.shields.io/badge/prior%20art-RGDS%20170%2B%20commits-purple)](https://github.com/mj3b/rgds)

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

GDI is a domain-agnostic specification for governing AI-informed decisions at the point where a prediction becomes an action. It defines:

- **The Governed Decision Record (GDR)** — a schema-validated artifact capturing the reasoning, evidence, confidence, accountability chain, and escalation logic for a single consequential decision, written before execution
- **The Confidence Threshold Model** — Green/Amber/Red zones that apply proportional governance based on decision risk
- **The Gate Taxonomy** — five decision outcomes (Go, Conditional Go, Defer, No-Go, Escalate) as first-class governed artifacts
- **The CI/CD Governance Integration pattern** — governance embedded as infrastructure, not oversight
- **Vertical Modules** — domain-specific extensions for biopharma, financial services, telecom, healthcare, and manufacturing

GDI sits between the AI inference layer and the governance framework layer. Below GDI, data platforms and AI models produce outputs. Above GDI, governance frameworks define what should be governed. GDI is the implementation layer that connects "we have a policy" to "we can prove what happened."

---

## The Governed Decision Record

The fundamental unit of GDI is the GDR. A GDR captures a single consequential decision at the transition point where an AI prediction becomes a human-authorized action.

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

The GDR is written **before execution**. An artifact written after the fact is a narrative. An artifact written before execution is evidence.

---

## Why This Is Hard to Build Without GDI

Five structural reasons the decision layer is absent from current governance infrastructure:

1. **IT Governance Inheritance** — frameworks evolved from IT and data governance traditions that focus on systems and data quality; individual decisions were never the governed object
2. **Static-Dynamic Mismatch** — traditional compliance operates on quarterly audit cycles; AI decisions occur at millisecond speed
3. **Wrong Abstraction Layer** — the EU AI Act classifies systems by risk level; individual decisions within a high-risk system receive no independent governance treatment
4. **Policy-Proof Gap** — "humans remain accountable" is meaningless without an operational answer to: who had the right to delegate this action, and can you demonstrate what happened?
5. **Governance as Performance** — organizations perform oversight symbolically while real decisions occur outside formal channels

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

---

## Repository Structure

```
governed-decision-intelligence/
├── spec/
│   └── GDI_v2_The_Decision_Architecture_for_Governed_AI.pdf   ← Core specification
├── schema/
│   ├── gdr.schema.json        ← Governed Decision Record JSON Schema
│   └── gdr.schema.yaml        ← YAML companion for readability
├── reference-implementation/
│   └── gate-classifier/       ← Gate classification layer for Microsoft AGT
│       ├── gate_classifier.py
│       ├── GATE-TAXONOMY.md
│       └── examples/
│           └── insurance_claims.py
├── docs/
│   ├── confidence-threshold-model.md
│   ├── gate-taxonomy.md
│   └── framework-compatibility.md
└── .github/
    └── workflows/
        └── validate.yml
```

---

## Prior Art

GDI evolved from the **RGDS (Regulated Gate Decision Support)** framework, a biopharma reference implementation developed over approximately seven weeks to govern IND and BLA submission decisions.

| Repository | Purpose | Status |
|-----------|---------|--------|
| [mj3b/governed-decision-intelligence](https://github.com/mj3b/governed-decision-intelligence) | GDI Core Specification, schemas, reference implementation | This repo |
| [mj3b/rgds](https://github.com/mj3b/rgds) | Biopharma reference implementation. 170+ commits, 6 canonical examples, CI validation | v2.0.0 active |
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

## Reference Implementation: Gate Classifier

The `reference-implementation/gate-classifier/` directory contains a working Python implementation that extends [Microsoft's Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit) with decision-layer classification.

AGT governs what an agent **does** (action layer: allow/deny before execution).
The gate classifier governs what **category of decision** the agent was making (decision layer: what level of human deliberation does this require?).

These are adjacent but not identical questions. Both are necessary for institutional accountability.

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

## Status

GDI v2.0 is a published open specification. The schema and reference implementation are in active development.

**Contributions welcome:** vertical module proposals, schema extensions, integration examples, framework compatibility analysis.

---

*Mark Julius Banasihan | Apache 2.0 Licensed | March 2026*
*github.com/mj3b | [mj3b/rgds](https://github.com/mj3b/rgds) | [mj3b/rgds-ai-governance](https://github.com/mj3b/rgds-ai-governance)*
