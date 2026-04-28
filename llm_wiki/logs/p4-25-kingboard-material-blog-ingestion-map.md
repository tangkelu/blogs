# P4-25 Kingboard Material Blog Ingestion Map

Date: 2026-04-27

## Purpose

This map audits the English material drafts under `/code/blogs/tmps/en` and defines how their Kingboard laminate data may be absorbed into `llm_wiki`.

This is a source-first ingestion pass. The blog drafts are useful claim inventories, but they are not authoritative sources for material values.

## Target Drafts

- `kingboard-pcb-laminate.md`
- `kb-6150-pcb.md`
- `kb-6160-pcb.md`
- `kb-6160a-pcb.md`
- `kb-6160f-kb-6160lc-pcb.md`
- `kb-6164-pcb.md`
- `kb-6165-pcb.md`
- `kb-6165c-kb-6165le-pcb.md`
- `kb-6165f-pcb.md`
- `kb-6167f-pcb.md`
- `kb-6167gmd-pcb.md`
- `kb-6167gld-pcb.md`
- `kb-6168le-pcb.md`
- `kb-6169gt-pcb.md`
- `kb-3200g-pcb.md`
- `hf-140-hf-170-pcb.md`
- `pi-515g-pi-520g-pcb.md`

## Baseline Finding

Current `llm_wiki` has no substantive Kingboard exact-product material fact layer yet. Existing Kingboard mentions are only future-gap notes in broader FR-4 and material-source coverage logs.

Therefore, the correct ingestion result for this pass is:

- create claim-family and per-draft dispositions
- identify official-source recovery priorities
- prevent draft-originated estimates from entering reusable facts
- defer product fact cards until official Kingboard / KBLaminates datasheets, product pages, processing guides, or stable official documents are registered as `source_id`s

## Disposition Contract

Use these dispositions for this batch:

- `source_recovery_priority`: worth searching official Kingboard / KBLaminates source records next.
- `candidate_source_scoped_fact`: may become a fact only after an official source is attached.
- `needs_official_source`: plausible but not usable yet.
- `estimated_or_blog_only_blocked`: draft explicitly estimates or derives the claim; do not reuse as fact.
- `audited_but_blocked`: inventoried and governed, but blocked from reusable claims.
- `public_site_claim_only`: may be page-scoped only if it comes from a current public HIL/APT page, not from draft prose.
- `reject_or_delete`: dynamic commercial, supplier-status, yield, lead-time, cost, market, or unsupported application-proof claim.

## Per-Draft Coverage Table

| Draft | Current status | Candidate source-scoped data if official source is found | Blocked / rejected content |
| --- | --- | --- | --- |
| `kingboard-pcb-laminate.md` | `audited_but_blocked` | None as a single aggregate fact. Decompose into per-product facts only. | Cross-portfolio ranking, cost multipliers, signal-speed mapping, portfolio counts, "verified" markers without source IDs, APTPCB sourcing/inventory claims. |
| `kb-6150-pcb.md` | `source_recovery_priority` | `KB-6150` exact-product Tg, Td, thermal stress, CTE, Dk/Df by frequency, CTI, dielectric breakdown, peel strength, flexural strength, moisture absorption, IPC slash sheet, UL file, specimen construction. | Lowest-cost rank, reflow survivability rules, layer-count/aspect-ratio/trace-space rules, cost deltas, volume economics, broad application-fit thresholds. |
| `kb-6160-pcb.md` | `source_recovery_priority` | `KB-6160` exact-product Tg, Td, T-260, Z-CTE, Dk/Df by frequency, resistivity, breakdown, peel/flexural/moisture values, `KB-6060` prepreg Dk/Df/thickness table, official lamination/storage guide values if sourced. | Lead-free pass-count heuristics, via/aspect-ratio limits, order-share claims, throughput claims, upgrade triggers as hard rules, quote/turnaround claims. |
| `kb-6160a-pcb.md` | `needs_official_source` | Product identity, UVB / double-sided positioning, core range only if official source is found. | Explicitly estimated material table, market/yield claims, automotive temperature claims, cost uplift, finished-thickness mapping. |
| `kb-6160f-kb-6160lc-pcb.md` | `needs_official_source` | Product identities and official Tg/Td/CTE/Dk/Df/prepreg compatibility only if individual official sources exist. | Explicitly estimated `KB-6160F`, `KB-6160LC`, and `KB-6160LC(C)` values, filler-size explanations as product proof, drill-cost percentages, impedance-shift percentages, cost deltas. |
| `kb-6164-pcb.md` | `source_recovery_priority` | `KB-6164` exact-product Tg, Td, T-260/T-288, Z-CTE, X/Y CTE, Dk/Df, resistivity, breakdown, CTI, peel/flexural/moisture values, `KB-6064` prepreg table, official lamination/storage guide values if sourced. | Replacement-at-no-charge claims, via-strain worked examples as fact, IST cycle claims unless source-backed, layer/aspect-ratio rules, cost index, competitor tables. |
| `kb-6165-pcb.md` | `source_recovery_priority_with_conflict_check` | `KB-6165` exact-product Tg, thermal stress, CTE, T-260/T-288, Td, Dk/Df, CAF test if official, breakdown, peel/flexural/moisture values, thickness/copper/panel availability if official and current. | Gbps/GHz suitability, reflow-margin math, trace-length rules, application service-life claims, inventory/lead-time claims, "no redesign" family-variant claims. |
| `kb-6165c-kb-6165le-pcb.md` | `needs_official_source` | Official `KB-6165C` and `KB-6165LE` material values only if individual sources exist. | Explicit estimates, OEM mandate claims, regional compliance claims, `10:1` / `2000+ cycles` reliability claims, `2-4 weeks` lead time, competitor comparisons. |
| `kb-6165f-pcb.md` | `source_recovery_priority` | `KB-6165F` exact-product Tg, Td, T-260/T-288, CTE, Dk/Df, resistivity, breakdown, CTI, peel/flexural/moisture values, `KB-6065F` prepreg table, official lamination guide values if sourced. | "Most widely used" market claims, unlimited-margin wording, reflow-count claims, impedance worked examples, drill-hit reductions unless official, layer-count and ambient heuristics. |
| `kb-6167f-pcb.md` | `source_recovery_priority` | `KB-6167F` exact-product high-Tg FR-4 values, IPC slash sheet, UL file, prepreg Dk/Df/thickness, official process/storage values if sourced. | OEM qualification claims, pricing advantage, competitor table, AEC / automotive cycle suitability, 30+ layer capability, PPAP / material traceability / outgoing test claims. |
| `kb-6167gmd-pcb.md` | `needs_official_source` | `KB-6167GMD` exact-product classification and Dk/Df/Tg/Td/CTE values only if official source exists. | Estimated values, uniqueness claims, OEM environmental-policy claims, PCIe/DDR/USB/Ethernet support claims, 6-inch loss math, "10 Gbps boundary", automotive central-compute claims. |
| `kb-6167gld-pcb.md` | `needs_official_source` | `KB-6167GLD` exact-product classification and electrical/thermal values only if official source exists. | Draft says no standalone official datasheet was independently verified. Block 25G/56G enablement, loss-budget analysis, VLP/HVLP rules, Megtron-equivalence and cost claims. |
| `kb-6168le-pcb.md` | `estimated_or_blog_only_blocked` | Product identity only if official source is found. | Draft explicitly estimates the core values. Block reliability-ceiling claims, aerospace/defense/downhole suitability, IST/cycle/life claims, high-aspect-ratio rules, hybrid-stackup strategy. |
| `kb-6169gt-pcb.md` | `estimated_or_blog_only_blocked` | Product identity and exact datasheet values only if an official standalone source exists. | Draft explicitly estimates the specs. Block all 56G/112G/PAM4 channel claims, trace-length limits, dB tables, Dk dispersion claims, HVLP-mandatory claims, 400G/AI/radar claims. |
| `kb-3200g-pcb.md` | `needs_official_source` | `KB-3200G` exact-product classification, IPC sheet, Tg DSC/DMA, Td, T-260/T-288, CTE, Dk/Df by frequency/method, CTI, UL file, official application list if sourced. | Roadmap claims, REACH/UL status for future products, 10G-25G/56G suitability, insertion-loss deltas, hybrid-stackup savings, HVLP/backdrill thresholds, pre-stock/lead-time claims. |
| `hf-140-hf-170-pcb.md` | `source_recovery_priority` | `HF-140` and `HF-170` exact-product values, IEC halogen-free claim if official, IPC sheets, Tg/Td/T-260/T-288/CTE, Dk/Df by method/frequency, CTI, UL file, prepreg tables, official applications. | RoHS/WEEE market narrative, OEM mandate claims, proprietary chemistry claims, regulatory compliance extrapolation, automotive/server suitability, spacing/voltage thresholds. |
| `pi-515g-pi-520g-pcb.md` | `split_status` | `PI-520G` exact-product Tg/Td/CTE/T-260/T-288/Dk/Df/UL/halogen-free/anti-CAF values if official source exists. | `PI-515G` estimated values, polyimide-cost comparisons, "highest in portfolio" claims without official portfolio source, via fatigue/stress math, application qualification, process temperature expectations, APTPCB quote/certificate claims. |

## Claim-Family Rules

### Exact Material Values

May become `source_scoped_fact` only with official Kingboard / KBLaminates source records.

Required context:

- exact product name and suffix
- source ID
- specimen construction or resin content where stated
- test method
- frequency for Dk/Df
- temperature / condition for CTE, T-260, T-288, peel, moisture, thermal stress, CTI, and resistivity
- typical-versus-spec distinction

### Prepreg And Processing Tables

Prepreg Dk/Df, resin content, pressed thickness, lamination cycle, pressure, storage, and shelf-life values are useful, but they require official datasheets or processing guides.

Do not generalize one prepreg family into another product suffix.

### Standards And Compliance

IPC slash sheets, UL file references, IEC halogen-free language, RoHS/WEEE, REACH, IATF, ISO, AEC, automotive, medical, aerospace, and defense claims require separate source handling.

Allowed:

- standard or compliance vocabulary when source-scoped
- official product positioning when source-scoped

Blocked:

- certification proof
- supplier approval
- accepted-lot proof
- OEM mandate claims
- regulatory compliance proof for finished boards
- current certification status without refresh

### High-Speed / SI / Channel Claims

Material Dk/Df values do not prove board-level channel compliance.

Blocked unless project-specific or primary engineering evidence exists:

- PCIe / USB / DDR / Ethernet / PAM4 compliance
- 10G / 25G / 56G / 112G support claims
- insertion-loss budgets
- eye / BER / jitter / compliance margin
- trace-length limits
- copper-roughness mandates as universal rules
- VNA / S-parameter production-lot promises

### Fabricator Capability And Commercial Claims

Default disposition: `reject_or_delete`.

This includes:

- APTPCB stocking or inventory
- direct sourcing relationship
- lead time
- quote response time
- pre-stock programs
- cost multipliers
- yield, scrap, throughput, drill-hit savings
- maximum layer count or aspect ratio as HIL/APT proof
- PPAP, traceability, IST, microsection, VNA, or lot documentation promises unless backed by a dated internal/public capability source

## Recovery Priority

### Priority 1: Datasheet-Like Product Rows

Search official Kingboard / KBLaminates sources first for:

- `KB-6150`
- `KB-6160`
- `KB-6164`
- `KB-6165`
- `KB-6165F`
- `KB-6167F`
- `HF-140`
- `HF-170`
- `PI-520G`

### Priority 2: High-Speed / Halogen-Free Rows

Search only if near-term blogs need these specific products:

- `KB-3200G`
- `KB-6167GMD`
- `KB-6167GLD`

### Priority 3: Hold Until Official Product Proof

Do not promote values until official sources are found:

- `KB-6160A`
- `KB-6160F`
- `KB-6160LC`
- `KB-6160LC(C)`
- `KB-6165C`
- `KB-6165LE`
- `KB-6168LE`
- `KB-6169GT`
- `PI-515G`

## Known Conflict / Review Notes

- `KB-6165` `Td` appears inconsistently across drafts. Treat it as `needs_review` until official source is checked.
- `KB-3200G` is described inconsistently across drafts versus `KB-6169GT`. Do not use portfolio-tier ranking without official product data.
- `PI-515G` is explicitly estimated in the draft. Do not reuse its numeric values.
- `KB-6168LE`, `KB-6169GT`, and `KB-6167GLD` drafts explicitly contain estimates or state that no standalone official datasheet was independently verified. Do not use their values as facts.

## Completion Status

This batch is absorbed at claim-family disposition level.

`P4-26` and `P4-28` later recovered official Kingboard / KBLaminates source records and exact-product fact cards for all product names in this batch.

## Final Draft Status After P4-28

| Draft | Final status | Notes |
| --- | --- | --- |
| `kingboard-pcb-laminate.md` | `selector_only_not_aggregate_fact` | Use `kingboard-laminate-selection-and-boundaries`; do not create portfolio ranking, cost ladder, or generic aggregate values. |
| `kb-6150-pcb.md` | `fully_learned_at_exact_product_level` | Exact-product material facts available. |
| `kb-6160-pcb.md` | `fully_learned_at_exact_product_level_with_value_correction` | Current official values supersede stale draft values. |
| `kb-6160a-pcb.md` | `fully_learned_at_exact_product_level` | Exact-product material facts available after P4-28. |
| `kb-6160f-kb-6160lc-pcb.md` | `fully_learned_at_exact_product_level` | `KB-6160F`, `KB-6160LC`, and `KB-6160LC(C)` all have exact-product facts. |
| `kb-6164-pcb.md` | `fully_learned_at_exact_product_level` | Exact-product material facts available. |
| `kb-6165-pcb.md` | `fully_learned_at_exact_product_level_with_td_conflict_resolved` | Current official `Td 348 C` supersedes draft conflict. |
| `kb-6165c-kb-6165le-pcb.md` | `fully_learned_at_exact_product_level` | `KB-6165C` and `KB-6165LE` both have exact-product facts. |
| `kb-6165f-pcb.md` | `fully_learned_at_exact_product_level` | Exact-product material facts available. |
| `kb-6167f-pcb.md` | `fully_learned_at_exact_product_level` | Exact-product material facts available. |
| `kb-6167gmd-pcb.md` | `fully_learned_at_material_property_level_but_channel_claims_blocked` | Material values available; PCIe / DDR / Ethernet / channel-speed claims remain blocked. |
| `kb-6167gld-pcb.md` | `fully_learned_at_material_property_level_but_channel_claims_blocked` | Material values available; PAM4 / PCIe / loss-budget claims remain blocked. |
| `kb-6168le-pcb.md` | `fully_learned_at_material_property_level_but_reliability_claims_blocked` | Material values available; mission / cycle / lifetime claims remain blocked. |
| `kb-6169gt-pcb.md` | `fully_learned_at_material_property_level_but_channel_claims_blocked` | Material values available; 56G / 112G / PAM4 / channel-budget claims remain blocked. |
| `kb-3200g-pcb.md` | `fully_learned_at_material_property_level_but_channel_claims_blocked` | Material values available; interface support claims remain blocked. |
| `hf-140-hf-170-pcb.md` | `fully_learned_at_exact_product_level` | Exact-product material facts available for both products. |
| `pi-515g-pi-520g-pcb.md` | `fully_learned_at_exact_product_level` | `PI-515G` and `PI-520G` both have exact-product facts; generic polyimide claims remain blocked. |

Next useful execution step: write or rewrite Kingboard material blogs only through the selector/wiki layer and exact-product fact cards.
