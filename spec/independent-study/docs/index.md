<div class="hero-banner">
<h1>Governed Decision Intelligence</h1>
<p>An independent research study on the decision-layer gap in AI governance. Ten questions establishing whether the gap is real, what GDI provides to close it, where GDI's limits lie, and which three problems the specification exposes that the published literature has not yet named.</p>
</div>

*Mark Julius Banasihan &middot; Independent Research &middot; May 2026*

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.PENDING-blue)](https://github.com/mj3b/governed-decision-intelligence)
[![License](https://img.shields.io/badge/License-Apache_2.0-teal)](https://github.com/mj3b/governed-decision-intelligence/blob/main/LICENSE)
[![Spec Version](https://img.shields.io/badge/GDI_Spec-v3.0-0D9488)](https://github.com/mj3b/governed-decision-intelligence)

---

!!! warning "Regulatory Status — May 2026"
    EU AI Act Article 86 enforcement for high-risk AI systems begins August 2026. This article creates an enforceable right to explanation of individual AI-informed decisions. No major governance framework currently specifies what artifact satisfies that requirement. This study establishes whether GDI's Governed Decision Record does.

---

## The Problem

No published open specification treats the individual AI-informed decision as a governed artifact at runtime.

Governance frameworks govern organizations — roles, policies, risk registers. Model registries and audit tools govern systems — model cards, bias audits, data lineage. At the decision altitude, where a specific AI prediction meets a specific human and produces a consequential action, the governed artifact does not exist in any published open specification.

This gap is structural. It has specific intellectual roots. It produces a specific, observable failure: a compliance reviewer reading a system-level audit trail can answer one question — was this AI system approved for this use case. They cannot answer the question regulators, auditors, and courts will ask with increasing frequency: who specifically authorized this system to take this class of action, on what evidence, under what risk acceptance, and what is the governed record of that decision.

## The Framework

**GDI (Governed Decision Intelligence)** proposes a single structural response: treat the individual AI-informed decision as a governed artifact with a defined schema, enforced accountability chain, and CI/CD integration that makes governance continuous rather than periodic.

The specification defines five components: the Governed Decision Record (GDR), the Confidence Threshold Model, the Gate Taxonomy, the AI Assistance Disclosure Protocol, and the CI/CD Governance Integration pattern.

The reference implementation — `mj3b/rgds`, the biopharma-focused RGDS framework — provides 170+ commits, 7 releases, a 114-test suite, and CI/CD validation via GitHub Actions demonstrating the architecture is operational, not theoretical.

## Key Findings

<div class="stat-grid">
<div class="stat-card">
<span class="stat-number">6</span>
<span class="stat-label">Major frameworks examined. None specifies a decision-level governed artifact schema.</span>
</div>
<div class="stat-card">
<span class="stat-number">3</span>
<span class="stat-label">Original contributions absent from the published literature as of May 2026.</span>
</div>
<div class="stat-card">
<span class="stat-number">114</span>
<span class="stat-label">Tests validating the reference implementation. CI/CD enforced via GitHub Actions.</span>
</div>
<div class="stat-card">
<span class="stat-number">4</span>
<span class="stat-label">Governance failure modes GDI addresses that no other published specification addresses.</span>
</div>
</div>

| Question | Focus | Confidence |
|----------|-------|-----------|
| [Q1: The Decision-Layer Gap](questions/q1.md) | Systematic gap analysis across six frameworks | <span class="conf-high">High</span> |
| [Q2: Eval-to-Governance Handoff](questions/q2.md) | Missing connection between pre-deployment evals and runtime governance | <span class="conf-high">High</span> |
| [Q3: Confidence Score Trustworthiness](questions/q3.md) | Validity of model-reported confidence as governance input | <span class="conf-med">Medium</span> |
| [Q4: The Comprehension Threshold Problem](questions/q4.md) | When human authorization is structurally insufficient | <span class="conf-med">Medium</span> |
| [Q5: Evidence Expiration](questions/q5.md) | Evidence expiration as a decision-level governance trigger | <span class="conf-high">High</span> <span class="orig">Original</span> |
| [Q6: Conduct Collapse Detection](questions/q6.md) | Observable signals preceding governance theater | <span class="conf-med">Medium</span> <span class="orig">Original</span> |
| [Q7: Delegation Provenance Completeness](questions/q7.md) | GDI versus cryptographic delegation protocols | <span class="conf-high">High</span> |
| [Q8: CI/CD Governance at Agentic Speed](questions/q8.md) | Latency and frequency thresholds for synchronous validation | <span class="conf-med">Medium</span> |
| [Q9: Framework Compatibility](questions/q9.md) | Operational evidence for six framework mappings | <span class="conf-high">High</span> |
| [Q10: Regulatory Trajectory](questions/q10.md) | Which instruments create the first mandatory demand | <span class="conf-med">Medium</span> |

[Results at a glance &rarr;](questions/results-overview.md)

---

## Scope and Limitations

This study examines GDI across one foundational claim: that the decision layer of AI governance is architecturally absent from every major published specification, and that GDI is the first open specification to address it.

The study does not claim GDI solves the AI alignment problem. GDI addresses organizational and regulatory accountability failures in systems that behave as declared. It does not address alignment faking, reward hacking, or the failure modes where systems actively deceive their governance layer. Those are addressed at a different layer by different methods. This study is explicit about where GDI stops.

Contribution claims are stated as "absent from the literature as of May 2026" with an explicit search methodology described in [Methods and Technical Notes](references/methods.md). This framing is accurate at writing time and does not become false when later work appears.

---

## Contents

- [Research Questions Q1–Q10](questions/index.md)
- [Results Overview](questions/results-overview.md)
- [Bibliography — 26 primary sources](references/bibliography.md)
- [Methods and Technical Notes](references/methods.md)
- [About the Author](references/about-the-author.md)
- [Acknowledgements](references/acknowledgements.md)

---

## Related Repositories

- **[mj3b/governed-decision-intelligence](https://github.com/mj3b/governed-decision-intelligence)** — GDI Core Specification, schemas, vertical modules, compatibility mappings (canonical home)
- **[mj3b/rgds](https://github.com/mj3b/rgds)** — Biopharma reference implementation. 170+ commits, 6 canonical decision examples, CI/CD validation
- **[mj3b/rgds-ai-governance](https://github.com/mj3b/rgds-ai-governance)** — AI governance covenants and non-agentic boundary definitions

All repositories are licensed under the Apache License 2.0.

---

## Citation

```bibtex
@software{banasihan2026gdi,
  author    = {Banasihan, Mark Julius},
  title     = {{GDI}: Governed Decision Intelligence — Independent Research Study},
  year      = {2026},
  month     = {5},
  version   = {1.0},
  doi       = {10.5281/zenodo.PENDING},
  url       = {https://mj3b.github.io/gdi-independent-study/},
  license   = {Apache-2.0}
}
```
