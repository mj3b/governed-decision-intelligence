# Changelog

This repository uses a **governance-first change record**.

---

## Unreleased — DEAS applicability boundary

### Added

- Decision Evidence Applicability Specification (DEAS) v0.2.0 as the canonical cross-regime working specification
- Seven bounded determination states for evidence-to-requirement analysis
- Explicit applicability, local-evidence, sufficiency-boundary, and non-equivalence fields
- Adjacent-system boundaries against Microsoft Agent Governance Toolkit, ScopeBlind/Acta, and Credo AI
- DEAS migration note preserving earlier DEPS links without preserving the portability claim

### Changed

- Renamed Decision Evidence Portability Specification (DEPS) to Decision Evidence Applicability Specification (DEAS)
- Replaced the hypothesis that evidence can “travel” across regimes with a bounded claim about applicability, assurance use, local evidence conditions, insufficiency, and non-equivalence
- Updated the GDI README, research claim register, framework mapping, related-work analysis, limitations, and working-specification status language
- Clarified that runtime governors produce enforcement evidence, signed-receipt systems establish defined integrity properties, Credo AI provides policy-pack and control infrastructure, GDI records the decision, HIT evaluates practical human influence, and DEAS qualifies evidence use under a specified requirement

### Deprecated

- `working-specifications/decision-evidence-portability-v0.1.md` as a current specification; the file remains as a migration pointer
- Unqualified claims that governance, controls, findings, evidence, or legal conclusions are portable across regimes

### Research boundary

DEAS is a working specification. Its schema, authoritative mappings, overlays, cases, reviewer protocol, and validation suite remain in development. The rename does not establish legal compliance, standards conformity, certification, admissibility, evidence sufficiency, or independent review.

---

## v2.1.0 — Interoperability and examples expansion
**Date:** April 2026

### Added
- GDI conformance driver for `draft-farley-acta-signed-receipts` (IETF)
  (`examples/testvectors-interop/`) — GDI is the 5th cross-verifying
  implementation in `ScopeBlind/agent-governance-testvectors`
- Sample receipt demonstrating a blocked decision with GDR sealed before
  execution (`examples/testvectors-interop/sample-receipts/`)
- Insurance claims example README with four-gate walkthrough
  (`examples/insurance-claims/README.md`)
- Bilateral pattern documentation for pre/post-execution receipt chaining
  in regulated deployments (`docs/bilateral-pattern.md`)
- Fully populated GDR example, schema-validated (`schema/gdr.example.json`)
- GDI v3 Core Specification (`spec/GDI_v3_The_Decision_Architecture_for_Governed_AI.pdf`)
- Cross-references between `docs/gate-taxonomy.md` and
  `reference-implementation/gate-classifier/GATE-TAXONOMY.md`

### Interoperability
Conformance PR: [ScopeBlind/agent-governance-testvectors#7](https://github.com/ScopeBlind/agent-governance-testvectors/pull/7)
Discussion: [microsoft/agent-governance-toolkit#276](https://github.com/microsoft/agent-governance-toolkit/discussions/276)

---

## v2.0.0 — Initial public release of GDI Core Specification
**Date:** March 2026

First public commit establishing GDI as a canonical specification repository.

### Contents
- GDI v2.0 Core Specification (`spec/GDI_v2_The_Decision_Architecture_for_Governed_AI.pdf`)
- Governed Decision Record (GDR) JSON Schema (`schema/gdr.schema.json`)
- Gate Classification reference implementation (`reference-implementation/gate-classifier/`)
- Framework compatibility documentation
- Apache 2.0 license

### Prior Art
The following repositories contain the design evolution that led to GDI v2.0:

| Repository | Period | Significance |
|-----------|--------|--------------|
| `mj3b/rgds` | Dec 2025 – Mar 2026 | Biopharma reference implementation. First working GDR system. 170+ commits across v1.0–v2.0.0 |
| `mj3b/rgds-ai-governance` | Dec 2025 – Mar 2026 | Non-agentic AI governance covenants. Human authority boundaries |

The Git commit timestamps across these repositories are the prior art record for decision-level AI governance architecture.

---

## Roadmap
- **v2.2**: Financial services vertical module
- **v2.3**: Telecom vertical module
- **v3.0**: Runtime governance sidecar reference implementation (LangGraph + Langfuse)
