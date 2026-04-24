# Changelog

This repository uses a **governance-first change record**.

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

- **v2.1**: GDR JSON Schema validation tooling and CI integration
- **v2.2**: Financial services vertical module
- **v2.3**: Telecom vertical module
- **v3.0**: Runtime governance sidecar reference implementation (LangGraph + Langfuse)
