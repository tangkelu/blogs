---
wiki_id: "wiki-materials-internal-material-family-coverage-and-refresh-rules"
title: "Internal material family coverage and refresh rules"
category: "materials"
status: "active"
last_reviewed_at: "2026-05-03"
fact_ids:
  - "materials-internal-material-family-coverage-map"
  - "materials-apt-rogers-internal-framing"
  - "materials-hil-base-laminate-and-build-stage-family-map"
  - "materials-ptfe-rf-material-processing-posture"
  - "methods-spread-glass-and-controlled-impedance-planning"
  - "methods-internal-json-coverage-boundary"
  - "materials-taconic-official-source-coverage-gap"
  - "materials-arlon-official-source-coverage"
  - "materials-flex-exact-product-anchor-map"
source_ids:
  - "frontendapt-materials-index-en"
  - "frontendapt-materials-rf-rogers-page-en"
  - "frontendapt-materials-rogers-pcb-manufacturing-page-en"
  - "frontendapt-materials-arlon-pcb-page-en"
  - "frontendapt-materials-isola-pcb-page-en"
  - "frontendapt-materials-megtron-pcb-page-en"
  - "frontendapt-materials-taconic-pcb-page-en"
  - "frontendapt-materials-teflon-pcb-page-en"
  - "frontendapt-materials-spread-glass-fr4-page-en"
  - "frontendapt-materials-controlled-impedance-stackups-page-en"
  - "frontendhil-fr4-pcb-product-page-en"
  - "frontendhil-halogen-free-pcb-product-page-en"
  - "frontendhil-high-tg-pcb-product-page-en"
  - "frontendhil-multilayer-pcb-product-page-en"
  - "frontendhil-single-double-layer-pcb-product-page-en"
  - "frontendhil-teflon-pcb-product-page-en"
  - "frontendhil-rogers-product-page-en"
  - "frontendapt-materials-remaining-index-en"
  - "frontendapt-resources-index-en"
tags: ["materials", "internal", "refresh", "governance", "ptfe", "high-speed", "rf", "source-governance"]
---

# Use This Page For

- Governing how future agents consume internal material-family pages from APT and HIL.
- Separating `internal framing`, `official exact-product truth`, and `internal-only recovery` before any draft or fact card is promoted.
- Deciding when a material family is ready for routing only, exact-product use, or still requires stronger official anchors.

# Core Governance Rule

- Internal material-family coverage is a discovery and routing layer, not default datasheet truth.
- A material family mentioned in APT or HIL proves topic coverage and service framing first.
- Exact product properties, final comparisons, and publishable numeric claims require official manufacturer-controlled anchors unless the lane is explicitly marked internal-only.

# Coverage Tiers

## Tier 1: Internal Family Framing

- Use APT and HIL material pages to identify which laminate families, stackup families, and process-adjacent material topics are already represented in the local corpus.
- This tier is valid for:
  topic discovery, routing, service framing, prompt evidence-pack support, and draft scope control.
- This tier is not valid for:
  final Dk/Df/Tg/CTE/thermal values, stock claims, qualification claims, or product-grade equivalence.

## Tier 2: Official Exact-Product Truth

- Promote a family into exact-product writing only when a local fact card is anchored by manufacturer-controlled pages or datasheets.
- Current examples now include:
  parts of Arlon N-series and 86HP, plus flex-adjacent exact-product anchors such as `UPILEX-S`, `Kapton HN`, `85N`, `85NT`, `N7000-3F`, and Panasonic `R-F705S`.
- This tier allows source-scoped exact-product language, but not generic finished-board or qualification inflation.

## Tier 3: Internal-Only Recovery

- Some families remain usable only through internal JSON recovery or internal framing.
- Taconic RF laminate families are currently governed as recovered through internal APT JSON, not as official public datasheet truth.
- Arlon RF/PTFE families such as `CLTE-XT`, `TC350`, `AD250/300/1000`, and `CuClad/DiClad/IsoClad` remain internal-only even though adjacent Arlon families have official anchors.
- This tier is valid for internal planning and controlled routing only, not for public numeric publication as official vendor truth.

# How To Read Material Family Coverage

## Baseline Families

- HIL baseline pages such as `single/double-layer`, `FR-4`, `high-Tg`, `halogen-free`, and `multilayer` are routing aids for standard laminate posture.
- Use them to decide whether a draft belongs in baseline laminate framing before escalating into specialty material lanes.

## Specialty RF / PTFE / High-Speed Families

- APT material pages for Rogers, Taconic, Arlon, Teflon/PTFE, Megtron, spread-glass, and controlled-impedance planning are strong for internal framing.
- They are not interchangeable with official material catalogs.
- Family mentions plus stackup/planning language support routing and topic decomposition, not automatic product-grade publication.

## Flex And Adjacent Narrow Anchors

- Flex material coverage now has some narrow exact-product anchors, which means future agents should not flatten all flex/polyimide/LCP discussion into one generic lane.
- Keep generic `polyimide`, `adhesiveless flex`, and `LCP` family language separate from exact-product rows unless the specific product source is attached.

# Refresh And Promotion Rules

## Safe To Promote Without New Source Recovery

- Internal material family routing pages
- Topic-scope governance
- Service-posture summaries that stay non-numeric
- Draft cleanup that replaces unsupported numbers with family-level framing

## Must Stop And Recheck Before Promotion

- Any exact material parameter row
- Any cross-brand comparison table
- Any claim that a family is complete, current, or fully sourced across all products
- Any claim that a material is stocked, low-cost, fast-turn, approved, or qualification-ready
- Any attempt to turn internal JSON recovery into official vendor authority

## Family-Specific Governance Notes

- Taconic:
  treat current RF laminate coverage as internal recovery plus governance, not public official exact-product completeness.
- Arlon:
  split between officially anchored N-series / 86HP branches and internal-only RF/PTFE recovery branches.
- Flex:
  exact-product anchors exist, but they do not authorize generic bend-life, rigid-flex reliability, or supplier capability claims.

# Decision Rules For Future Agents

| If the draft asks for | Use | Do not infer |
| --- | --- | --- |
| broad family coverage | internal APT/HIL family framing | exact product values or current stock posture |
| exact product identity with official local anchor | exact-product fact card | generic family equivalence |
| Taconic RF parameters | internal-only recovery posture | official Taconic datasheet authority |
| Arlon RF/PTFE parameters | internal-only recovery posture | official live RF/PTFE product continuity |
| flex PI/LCP example | narrow exact-product anchor if present | universal flex-material performance |

# Blocked Claims

- exact-product completeness claims
- supplier-capability claims
- performance guarantees
- cost/lead-time/yield claims

# Common Failure Modes

- Treating internal material index coverage as if every family has exact-product closure.
- Publishing internal JSON recovery as official vendor-controlled numeric truth.
- Merging baseline laminate routing, RF/PTFE families, and flex exact-product anchors into one undifferentiated material layer.
- Converting family-level site framing into guaranteed manufacturing capability or qualification posture.

# Must Refresh Before Publishing

- Any Dk, Df, Tg, CTE, thermal conductivity, dielectric thickness, or copper-weight row
- Any current stocking, inventory, MOQ, lead-time, prototype-speed, or sourcing claim
- Any material ranking, insertion-loss, skew, impedance, or validation-scope claim
- Any statement that a family is fully complete, currently available, or approved for regulated or customer-qualified use
- Any Taconic or Arlon RF/PTFE product-level parameter presented as official manufacturer truth

# Related Fact Cards

- `materials-internal-material-family-coverage-map`
- `materials-apt-rogers-internal-framing`
- `materials-hil-base-laminate-and-build-stage-family-map`
- `materials-ptfe-rf-material-processing-posture`
- `methods-spread-glass-and-controlled-impedance-planning`
- `methods-internal-json-coverage-boundary`
- `materials-taconic-official-source-coverage-gap`
- `materials-arlon-official-source-coverage`
- `materials-flex-exact-product-anchor-map`

# Local Source Records

- `frontendapt-materials-index-en`
- `frontendapt-materials-rf-rogers-page-en`
- `frontendapt-materials-rogers-pcb-manufacturing-page-en`
- `frontendapt-materials-arlon-pcb-page-en`
- `frontendapt-materials-isola-pcb-page-en`
- `frontendapt-materials-megtron-pcb-page-en`
- `frontendapt-materials-taconic-pcb-page-en`
- `frontendapt-materials-teflon-pcb-page-en`
- `frontendapt-materials-spread-glass-fr4-page-en`
- `frontendapt-materials-controlled-impedance-stackups-page-en`
- `frontendhil-fr4-pcb-product-page-en`
- `frontendhil-halogen-free-pcb-product-page-en`
- `frontendhil-high-tg-pcb-product-page-en`
- `frontendhil-multilayer-pcb-product-page-en`
- `frontendhil-single-double-layer-pcb-product-page-en`
- `frontendhil-teflon-pcb-product-page-en`
- `frontendhil-rogers-product-page-en`
- `frontendapt-materials-remaining-index-en`
- `frontendapt-resources-index-en`
