# Methods and Technical Notes

## Literature Search Methodology

The gap claim in Q1 and the original contribution claims in Q5 and Q6 rest on the assertion that no published specification addresses specific problems as of May 2026. This claim requires a defined search methodology.

**Search scope:** arxiv (cs.AI, cs.CR, cs.SE, stat.ML), Google Scholar, published regulatory instruments and their implementing acts, vendor documentation from major AI governance platform providers (Credo AI, Holistic AI, IBM OpenPages, OneTrust, Monitaur), and published blog posts from Oracle, Microsoft, Google DeepMind, and Anthropic through May 2026.

**Search terms used:**

- "governed decision record"
- "decision artifact AI governance"
- "individual decision schema AI"
- "accountability chain AI runtime"
- "evidence expiration governance"
- "conduct collapse AI"
- "comprehension threshold accountability"
- "eval-to-governance handoff"
- "decision-level specification AI"
- "Structured Decision Records"

**Search findings:** No published open specification defines a schema for individual AI-informed decision records containing options considered, evidence base, risk posture, accountability chain, and CI/CD integration as a single governed artifact. Oracle's OCI Agentic Governance Framework (April 2026) uses the term "Structured Decision Records" for a policy enforcement outcome artifact at a different governance layer. This distinction is analyzed in Q1.

Adjacent work that required precise differentiation:

- Oracle OCI AGF (April 2026): Structured Decision Records in L1 evidence layer
- Jain, R. (February 2026): Premise Governance (arXiv:2602.02378)
- Dalugoda, A. (March 2026): HDP protocol (arXiv:2604.04522)
- Right-to-Act (April 2026): Pre-execution non-compensatory decision boundary (arXiv:2604.24153)
- Kaptein et al. (March 2026): Policies on Paths (arXiv:2603.16586)

---

## Confidence Rating Methodology

| Rating | Criteria |
|--------|---------|
| <span class="conf-high">High</span> | Claim is verifiable from published specification text with operational implementation evidence from RGDS reference implementation |
| <span class="conf-med">Medium</span> | Claim is logically valid but lacks empirical validation, or depends on regulatory interpretation not yet available |
| <span class="conf-low">Low</span> | Claim is structural inference without published regulatory or specification signal |

---

## Technical Implementation

The RGDS reference implementation provides operational evidence for framework compatibility claims in Q9.

| Property | Value |
|----------|-------|
| Repository | [github.com/mj3b/rgds](https://github.com/mj3b/rgds) |
| Test suite | 114 tests |
| CI/CD | GitHub Actions — schema validation on every push |
| Releases | 7 (v1.0 through v2.0.0) |
| Decision examples | 6 canonical examples (go, conditional go, no-go, defer, regulatory interaction, AI-assisted) |
| License | Apache 2.0 |
| DOI | 10.5281/zenodo.20242004 |

The GDI canonical repository:

| Property | Value |
|----------|-------|
| Repository | [github.com/mj3b/governed-decision-intelligence](https://github.com/mj3b/governed-decision-intelligence) |
| Specification version | v3.0 |
| License | Apache 2.0 |

---

## Versioning and Update Cadence

This study publishes to Zenodo for a stable DOI establishing the prior art timestamp. The MkDocs site at `mj3b.github.io/gdi-independent-study/` is the living version with version tracking and explicit "last reviewed" dates per section.

Planned update cadence:

- **Quarterly:** Literature review of the gap claim and adjacent work
- **Annual:** Framework alignment audit as ISO 42001, NIST AI RMF, and EU AI Act implementing acts publish updates

When a new specification publishes that addresses any of the three original contributions — evidence expiration governance, conduct collapse detection, or the comprehension threshold problem — the relevant question page will be updated with an explicit note and the contribution claim revised accordingly.

The separation between the Zenodo DOI (stable, citable, timestamped) and the MkDocs site (living, updateable) is deliberate. Readers who need citability use the DOI. Readers who need current state use the site.
