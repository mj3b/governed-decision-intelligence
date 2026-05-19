# Acknowledgements

This study builds on the RGDS independent research (Banasihan, 2026, DOI: 10.5281/zenodo.20242004), which established the biopharma-focused reference implementation that GDI generalizes.

The ten research questions were stress-tested against the published literature before writing began, with particular attention to Oracle's April 2026 OCI Agentic Governance Framework and Raunak Jain's Premise Governance paper (arXiv:2602.02378). Both represent genuine adjacent work that required precise differentiation rather than dismissal.

The METR research team's published work on reward hacking, monitorability evaluations, and time horizon measurement provided the AI safety literature foundation that distinguishes this study from enterprise AI governance work.

The alignment faking research published by Anthropic (2024) and the International AI Safety Report 2026 provided the epistemic context for the limitations stated in Q3, Q4, and the Results Overview.

This study was developed with AI assistance (Claude, Anthropic). Per research transparency requirements: the author directed the analysis, reviewed every claim against source materials, and takes responsibility for all findings, framings, and limitations stated. The specific findings — the gap claim, the Oracle distinction, the Premise Governance differentiation, the three original contributions — represent the author's own intellectual contribution. AI assistance supported drafting and organizational structure; it did not generate the research questions or the pressure-test conclusions.

---

# Methods and Technical Notes

## Literature Search Methodology

The gap claim in Q1 and the original contribution claims in Q5 and Q6 rest on the assertion that no published specification addresses specific problems as of May 2026. This claim requires a defined search methodology.

**Search scope:** arxiv (cs.AI, cs.CR, cs.SE, stat.ML), Google Scholar, published regulatory instruments and their implementing acts, vendor documentation from major AI governance platform providers (Credo AI, Holistic AI, IBM OpenPages, OneTrust, Monitaur), and published blog posts from Oracle, Microsoft, Google DeepMind, and Anthropic through May 2026.

**Search terms used:** "governed decision record," "decision artifact AI governance," "individual decision schema AI," "accountability chain AI runtime," "evidence expiration governance," "conduct collapse AI," "comprehension threshold accountability," "eval-to-governance handoff," "decision-level specification AI," "Structured Decision Records."

**Findings:** No published open specification defines a schema for individual AI-informed decision records with options considered, evidence base, risk posture, accountability chain, and CI/CD integration. Oracle's OCI Agentic Governance Framework (April 2026) uses the term "Structured Decision Records" for a different artifact at a different governance layer. This distinction is analyzed in Q1.

**Confidence rating methodology:** High confidence is applied where the claim is verifiable from published specification text with operational implementation evidence. Medium confidence is applied where the claim is logically valid but lacks empirical validation or depends on regulatory interpretation. Low confidence is applied where the claim is structural inference without published signal.

## Technical Implementation

The RGDS reference implementation provides operational evidence for framework compatibility claims in Q9. Repository: [github.com/mj3b/rgds](https://github.com/mj3b/rgds). Test suite: 114 tests. CI/CD: GitHub Actions. Releases: 7 (v1.0 through v2.0.0). Decision examples: 6 canonical examples demonstrating all five gate outcomes. License: Apache 2.0.

The GDI canonical repository: [github.com/mj3b/governed-decision-intelligence](https://github.com/mj3b/governed-decision-intelligence). Version: 3.0. License: Apache 2.0.

## Versioning and Update Cadence

This study publishes to Zenodo for a stable DOI. The MkDocs site at `mj3b.github.io/gdi-independent-study/` is the living version with version tracking and explicit "last reviewed" dates per section.

Planned update cadence: quarterly literature review of the gap claim and adjacent work; annual framework alignment audit as ISO 42001, NIST AI RMF, and EU AI Act implementing acts publish updates.

When a new specification publishes that addresses any of the three original contributions (evidence expiration, conduct collapse, comprehension threshold), the relevant question page will be updated with an explicit note and the contribution claim revised accordingly.
