# Contributing to Governed Decision Intelligence (GDI)

GDI is an open specification. Contributions that extend, validate, or implement the decision-layer governance architecture are welcome.

---

## What Contributions Are Welcome

**Vertical modules** — Domain-specific extensions of the GDR schema and gate taxonomy for financial services, telecom, healthcare, supply chain, or industrial/robotics environments. See Section 10 of the spec for the expansion map.

**Schema extensions** — Proposed additions or refinements to `schema/gdr.schema.json` with documented rationale. Every field must justify its existence by naming the governance failure it prevents.

**Integration examples** — Worked examples showing GDI integrated with agent frameworks (LangGraph, AutoGen, CrewAI) or governance toolkits (Microsoft AGT, others). Examples go in `reference-implementation/`.

**Framework compatibility analysis** — Mappings between GDR fields and requirements in governance frameworks not yet covered in `docs/framework-compatibility.md`.

**Research grounding** — Citations or analysis connecting GDI's architecture to published decision science, accountability theory, or regulated industry governance patterns.

---

## What Does Not Belong Here

- Contributions that modify AGT, NIST, ISO, or any third-party framework directly
- Autonomous or agentic components that make decisions without explicit human authorization
- Proprietary implementations requiring closed dependencies

---

## How to Contribute

1. Open an issue describing what you want to add and why before writing code or prose
2. For schema changes, include the governance rationale — what failure mode does this field prevent?
3. For integration examples, include a working test or worked example demonstrating the integration
4. For vertical modules, follow the structure in `reference-implementation/gate-classifier/` as a reference pattern
5. All contributions must be compatible with Apache 2.0

---

## AI Assistance Disclosure

If AI assistance materially influenced your contribution, disclose it in your PR description: which tool, what purpose, what human review was applied. This is consistent with GDI's own AI disclosure principles.

---

## Contact

Open an issue or discussion on this repository.

*Apache 2.0 — Copyright 2026 Mark Julius Banasihan*
