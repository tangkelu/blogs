# P4-06 6-Layer Evidence Pack

Date: 2026-04-26

## 1. Topic Summary

- Topic: `6-layer PCB manufacturing`
- Primary keyword: `6 layer PCB manufacturing`
- Secondary keywords:
  - `6 layer PCB stackup`
  - `6 layer PCB materials`
  - `6 layer PCB impedance control`
  - `6 layer rigid-flex PCB`
  - `6 layer RF PCB`
- Page type: `query`
- Search intent:
  - engineering decision
  - stackup and material selection
  - manufacturing planning
  - supplier communication
- Target reader:
  - hardware engineer
  - PCB designer
  - sourcing / NPI engineer
  - technical buyer
- Site: `HILPCB`

Working posture:

- This is a first-wave `P4-06` evidence pack.
- It is usable for a conservative `query` rewrite.
- It is not a readiness unlock for unsupported fabrication-capability numerics.

## 2. Traceable Pack Metadata

```yaml
topic: "6-layer PCB manufacturing"
scope:
  - "Conservative public explanation of what 6-layer construction changes in stackup planning, material selection, validation posture, and special-build branching."
  - "Allowed hard numerics are limited to official material datasheet or official product-page anchors already normalized into stable material fact cards."
  - "Internal site/process pages may support posture, workflow, and boundary control only."
fact_ids:
  - "materials-fr4-official-source-coverage"
  - "materials-iteq-it-180a"
  - "materials-panasonic-megtron-6"
  - "materials-rogers-ro4350b"
  - "materials-rogers-rt-duroid-5880"
  - "materials-agc-rf-10"
  - "methods-pcb-stackup-special-process-and-baseline-families"
  - "methods-controlled-impedance-tdr-verification-posture"
  - "methods-rf-validation-capability"
  - "methods-thermal-pcb-platform-selection-posture"
  - "methods-rigid-flex-stackup-and-bend-reliability-posture"
  - "methods-backdrill-control-capability"
source_ids:
  - "isola-fr408-datasheet"
  - "isola-fr408hr-datasheet"
  - "iteq-it-180a-page"
  - "panasonic-megtron-6-r5775n"
  - "panasonic-megtron-6-datasheet"
  - "rogers-ro4350b-product-page"
  - "rogers-ro4000-datasheet"
  - "rogers-rt-duroid-5880-product-page"
  - "rogers-rt-duroid-5870-5880-datasheet"
  - "agc-rf-10-product-page"
  - "agc-rf-10-datasheet"
  - "agc-rf-microwave-laminates-page"
  - "frontendapt-materials-spread-glass-fr4-page-en"
  - "frontendapt-materials-isola-pcb-page-en"
  - "frontendapt-pcb-fr4-pcb-page-en"
  - "frontendapt-pcb-high-tg-pcb-page-en"
  - "frontendapt-pcb-pcb-stack-up-page-en"
  - "frontendapt-pcb-multi-layer-laminated-structure-page-en"
  - "frontendapt-pcb-special-pcb-manufacturing-page-en"
  - "frontendapt-pcb-pcb-impedance-control-page-en"
  - "frontendapt-pcb-high-speed-pcb-page-en"
  - "frontendapt-pcb-multilayer-pcb-page-en"
  - "frontendapt-high-frequency-pcb-page-en"
  - "frontendapt-microwave-pcb-page-en"
  - "frontendapt-pcb-rigid-flex-pcb-page-en"
  - "frontendapt-pcb-flex-pcb-page-en"
  - "frontendapt-pcba-flex-rigid-flex-page-en"
  - "frontendapt-pcb-high-thermal-pcb-page-en"
  - "frontendapt-pcb-metal-core-pcb-page-en"
  - "frontendapt-pcb-ceramic-pcb-page-en"
  - "frontendhil-rigid-flex-pcb-product-page-en"
  - "frontendhil-flex-pcb-product-page-en"
  - "frontendhil-high-frequency-product-page-en"
  - "frontendhil-rogers-product-page-en"
  - "frontendhil-high-thermal-pcb-product-page-en"
  - "frontendhil-metal-core-pcb-product-page-en"
  - "frontendhil-ceramic-pcb-product-page-en"
  - "frontendhil-heavy-copper-pcb-product-page-en"
must_refresh:
  - claim: "Any HIL capability or service promise tied to tolerance, trace/space, drill size, coupon count, turnaround, geography, inventory, or testing coverage."
    value: true
  - claim: "Any price, cost uplift, lead time, MOQ, stock, or service-speed language."
    value: true
  - claim: "Any internal acceptance threshold or verification percentage presented as a transferable shop fact."
    value: true
  - claim: "Any exact geometry-derived impedance table or manufacturability number."
    value: true
conflicts:
  - "The current blog treats broad FR-4 families as if one generic numeric ladder were safe. The material coverage card requires product-specific handling instead."
  - "The current blog mixes internal validation posture with unsupported transferable tolerance and geometry numbers."
  - "The current blog mixes special-build posture with unsupported thermal, flex-life, drill, and DFM thresholds."
notes:
  - "Use wiki/process pages only as secondary framing support, not as atomic fact support."
  - "Do not invent or promote new fact_ids or source_ids during prompt execution."
  - "If a paragraph has no valid fact_id anchor, it is not eligible for publication."
```

Secondary framing support only:

- `/code/blogs/llm_wiki/wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`
- `/code/blogs/llm_wiki/wiki/testing/validation-ladder-from-e-test-to-si-verification.md`

## 3. Source Facts

### Existing hard information in the current article draft

- Topic cluster already present:
  - baseline `FR-4`
  - high-Tg `FR-4`
  - RF / hybrid laminates
  - thermal-platform variants
  - flex / rigid-flex variants
  - controlled impedance
  - via strategy
  - lamination / drilling / finish
  - DFM
- Existing hard-number pattern in draft:
  - material property numerics
  - stackup recipe numerics
  - impedance geometry numerics
  - via-rule numerics
  - cost / turnaround / testing numerics
- Existing test / verification language:
  - `TDR`
  - coupon verification
  - manufacturing review / DFM posture

### Usable hard anchors already available in `llm_wiki`

| Area | Safe anchor | fact_id | source_ids | Condition |
| --- | --- | --- | --- | --- |
| FR-4 family framing | FR-4 is a family, not one universal numeric material | `materials-fr4-official-source-coverage` | `isola-fr408-datasheet`, `isola-fr408hr-datasheet` | Use exact product names for hard values |
| High-Tg FR-4 example | `IT-180A` official page gives `Tg 175 C`, `Td 345 C`, `Dk 4.1`, `Df 0.017` | `materials-iteq-it-180a` | `iteq-it-180a-page` | Keep `10 GHz`, `RC 50%`, and method with dielectric values |
| Process-friendly low-loss example | `MEGTRON 6` public grade gives `Tg 185 C`, `Td 410 C`, `Dk 3.4`, `Df 0.002 / 0.004` | `materials-panasonic-megtron-6` | `panasonic-megtron-6-r5775n`, `panasonic-megtron-6-datasheet` | Keep exact grade context |
| RF hybrid example | `RO4350B` gives process `Dk 3.48 +/- 0.05` and `Df 0.0037` at `10 GHz / 23 C` | `materials-rogers-ro4350b` | `rogers-ro4350b-product-page`, `rogers-ro4000-datasheet` | Keep frequency, temperature, and method |
| Ultra-low-loss PTFE example | `RT/duroid 5880` gives `Dk 2.20 +/- 0.02`, `Df 0.0009 at 10 GHz` | `materials-rogers-rt-duroid-5880` | `rogers-rt-duroid-5880-product-page`, `rogers-rt-duroid-5870-5880-datasheet` | Use as PTFE product example, not universal RF rule |
| High-Dk RF example | `RF-10` gives `Dk 10.2 +/- 0.3`, `Df 0.0025 at 10 GHz`, thermal conductivity `0.85 W/mK` | `materials-agc-rf-10` | `agc-rf-10-product-page`, `agc-rf-10-datasheet` | Keep modified IPC method attached |
| Stackup / family routing | Internal pages split baseline FR-4, stackup planning, and special-process routes | `methods-pcb-stackup-special-process-and-baseline-families` | internal source set above | Framing only |
| Impedance validation | Internal pages repeatedly pair impedance targets with `TDR` or coupon verification | `methods-controlled-impedance-tdr-verification-posture` | internal source set above | Posture only, not exact tolerance grant |
| RF verification | Internal pages pair RF builds with `TDR`, `VNA`, coupon, and traceability language | `methods-rf-validation-capability` | internal source set above | Posture only |
| Thermal branching | Internal pages separate `MCPCB`, heavy copper, and ceramic as different thermal platforms | `methods-thermal-pcb-platform-selection-posture` | internal source set above | Posture only |
| Flex / rigid-flex posture | Internal pages treat bend reliability as a stackup and process issue | `methods-rigid-flex-stackup-and-bend-reliability-posture` | internal source set above | Posture only |
| Backdrill posture | Internal pages treat backdrill as a high-speed / RF control, not a default 6-layer promise | `methods-backdrill-control-capability` | internal source set above | Optional, posture only |

### Original draft weaknesses

- It uses unsupported internal capability numerics as if they are stable public facts.
- It treats recipe values and geometry tables as transferable defaults.
- It uses project-style engineering heuristics as if they were universal standards.
- It mixes valid material selection logic with unsupported fabrication-capability numbers.

## 4. Claim Extraction

### Current-draft claim classes and bridge treatment

| Current section | Representative claim or section pattern | Class | Disposition | Evidence-pack action |
| --- | --- | --- | --- | --- |
| Capability quote block | `±8%`, `3/3mil`, `100% electrical testing`, same-day support | `B / F / G` | `unsupported` | Exclude entirely |
| `Why 6 Layers?` | More planes and signal/reference separation improve planning options | public + judgment | `keep` | Keep as conservative engineering framing |
| `Why 6 Layers?` | `30-40%` board cost uplift | `F` | `unsupported` | Delete |
| Standard / mid-Tg / high-Tg FR-4 | Generic FR-4 numeric ladders and reflow thresholds | `A` mixed with `E` | `downgrade` | Keep family framing; hard numbers only on exact product anchors |
| Halogen-free FR-4 | Thresholds, pressure deltas, drill feed deltas | `C / E / B` | `unsupported` | Remove from usable hard-fact set unless separately sourced later |
| Stackup configurations | Named stackup families and adjacency logic | judgment | `keep` | Keep architecture logic only |
| Stackup tables | Copper weights, dielectric windows, distributed capacitance numerics | `B / D / E` | `unsupported` | Delete or rewrite without hard numbers |
| High-frequency section | Material family split between FR-4, RF hybrid, PTFE, low-loss laminates | public + judgment | `keep` | Keep with exact-product anchors |
| RF hybrid table | Layer-by-layer recipe with generic FR-4 Dk values | `A / D / B` | `downgrade` | Keep hybrid concept; remove recipe-style numeric table |
| Full high-frequency stackup | `Megtron 6`, `RO4350B`, `RT/duroid 5880` material examples | `A` | `keep` | Keep only with official product-card numerics and conditions |
| Impedance differences table | Geometry-to-50 ohm width table | `D / B` | `unsupported` | Delete |
| Thermal section | `MCPCB`, metal-base, ceramic as platform branches | judgment | `keep` | Keep platform-selection posture |
| Thermal section | Heat-flux thresholds, conductivity deltas, junction-temp gains | `B / E / D` | `unsupported` | Delete |
| Flex / rigid-flex section | Variant framing and stackup complexity | judgment | `keep` | Keep posture only |
| Flex / rigid-flex section | Bend-cycle ratios, bend-radius minima, Z-routing tolerances | `B / E` | `unsupported` | Delete or rewrite as non-numeric risk language |
| Impedance section | Controlled impedance depends on stackup, copper, dielectric, and material | public + judgment | `keep` | Keep |
| Impedance section | Microstrip / stripline width tables, variation budgets, tolerance targets, coupon counts | `D / B / G` | `unsupported` | Delete |
| Via strategies | Through-hole / blind / via-in-pad vocabulary and tradeoff logic | judgment | `keep` | Keep conceptually |
| Via strategies | Hole minima, aspect ratio, annular ring, cost uplift | `B / C / F` | `unsupported` | Delete |
| Lamination / drilling / finish | Basic workflow and finish-choice framing | judgment | `keep` | Keep as non-numeric process framing |
| Lamination / drilling / finish | RPM, aspect-ratio, shelf-life table | `B / F / C` | `unsupported` | Delete unless separately sourced later |
| DFM rules | Avoid routing over plane splits; match impedance target to actual stackup | judgment | `keep` | Keep |
| DFM rules | Copper density targets, feature-size tables, decoupling distances, return-via distances | `B / D / E` | `unsupported` | Delete |
| Cost section | Price and optimization numerics | `F` | `unsupported` | Exclude section |
| Final HIL CTA | inventory, solver, tolerance, drill, blind-via, quality, geography claims | `B / F / G` | `unsupported` | Replace with neutral next-step path only |

## 5. Classification

### A. Publicly Verifiable Facts

| Claim | Why it matters | Source type | fact_id | source_ids | Verification status |
| --- | --- | --- | --- | --- | --- |
| FR-4 should be treated as a family topic, not as one fixed property table | Prevents false universal FR-4 numbers | official datasheet | `materials-fr4-official-source-coverage` | `isola-fr408-datasheet`, `isola-fr408hr-datasheet` | verified |
| `IT-180A` official page lists `Tg 175 C`, `Td 345 C`, `Dk 4.1`, `Df 0.017` | Gives one exact high-Tg FR-4 anchor | official product page | `materials-iteq-it-180a` | `iteq-it-180a-page` | verified |
| `MEGTRON 6` public grade lists low-loss and high-heat numeric anchors | Supports process-friendly low-loss branch | official model page + datasheet | `materials-panasonic-megtron-6` | `panasonic-megtron-6-r5775n`, `panasonic-megtron-6-datasheet` | verified |
| `RO4350B` is positioned as low-loss RF laminate with epoxy/glass-style processing and has published process `Dk / Df` values | Supports RF hybrid branch | official product page + datasheet | `materials-rogers-ro4350b` | `rogers-ro4350b-product-page`, `rogers-ro4000-datasheet` | verified |
| `RT/duroid 5880` is a PTFE composite with published ultra-low-loss properties | Supports PTFE branch | official product page + datasheet | `materials-rogers-rt-duroid-5880` | `rogers-rt-duroid-5880-product-page`, `rogers-rt-duroid-5870-5880-datasheet` | verified |
| `RF-10` is a high-Dk RF laminate with published `Dk`, `Df`, and thermal conductivity | Supports high-Dk RF branch | official product page + datasheet | `materials-agc-rf-10` | `agc-rf-10-product-page`, `agc-rf-10-datasheet` | verified |
| Internal process pages consistently frame stackup choice as an early architecture decision | Supports conservative stackup-planning wording | internal process pages | `methods-pcb-stackup-special-process-and-baseline-families` | internal source set | verified |
| Internal pages repeatedly pair controlled impedance with `TDR`-style verification, not just design intent | Supports validation wording | internal process / product pages | `methods-controlled-impedance-tdr-verification-posture` | internal source set | verified |
| Internal RF pages pair `TDR`, `VNA`, coupons, and traceability as the RF verification posture | Supports RF validation wording | internal process / product pages | `methods-rf-validation-capability` | internal source set | verified |
| Internal thermal pages split metal-core, heavy-copper, and ceramic into different thermal-platform routes | Supports thermal branch wording | internal process / product pages | `methods-thermal-pcb-platform-selection-posture` | internal source set | verified |
| Internal flex pages treat bend reliability as a stackup / process issue | Supports rigid-flex branch wording | internal process / product pages | `methods-rigid-flex-stackup-and-bend-reliability-posture` | internal source set | verified |

### B. Project-Level Judgments

| Judgment / control point | Scope | Safe wording |
| --- | --- | --- |
| 6-layer is often the point where plane allocation, reference continuity, and stackup planning become more explicit | general engineering framing | A 6-layer board is usually chosen when routing separation and plane planning matter more than keeping the layer count minimal |
| Material choice should follow signal-loss, thermal, and mechanical constraints rather than the phrase `6-layer` alone | all variants | `6-layer` describes layer count, not one universal material system |
| Hybrid RF stackups are often sensible when only part of the design needs low-loss laminate | RF + digital mixed boards | Use specialty laminate only where RF or high-speed loss justifies it, then review bonding and stackup interactions project by project |
| Thermal builds should be split into platform choices rather than treated as one generic multilayer upgrade | thermal path problems | When heat removal becomes the main driver, metal-core, ceramic, and heavy-copper routes should be evaluated separately |
| Flex and rigid-flex sections should be written as stackup and reliability planning topics, not as generic variants of standard FR-4 fabrication | flex / rigid-flex | Bend reliability depends on stackup, copper type, coverlay, and transition design, so it should be framed as a separate design and process decision |
| Impedance writing should emphasize model-to-stackup alignment and measurement planning | controlled-impedance sections | Controlled impedance should be tied to stackup definition and verification planning, not just to nominal target labels |
| Via architecture should be framed as a density / cost / SI tradeoff, not as a universal default ladder | through-hole vs blind vs VIP | Choose the via structure around escape density, transition behavior, and fabrication complexity |

### C. Site-Specific Capability References

| Capability or promise | Site path / source | Allowed wording | must_refresh |
| --- | --- | --- | --- |
| HIL capability banner with tolerance, line/space, testing, same-day support | `/code/hileap/frontendHIL/docs/hilpcb_blog_04.24/en/6-layer-pcb-manufacturing.md` | Do not reuse in the evidence pack; replace with neutral next-step wording only | true |
| Internal impedance-verification posture | `methods-controlled-impedance-tdr-verification-posture` | May be used only as `controlled impedance should be paired with verification such as TDR or coupon measurement` | true for exact thresholds |
| Internal RF validation posture | `methods-rf-validation-capability` | May be used only as `RF work often adds VNA/TDR/coupon validation planning` | true for frequency ceilings and scope |
| Internal thermal, flex, and special-process branches | related method cards above | May be used only as branch-selection framing | true for any numeric capability or guarantee |

### D. Unsupported / Unclear

| Claim | Why unclear | Downgrade method |
| --- | --- | --- |
| `±8%` impedance, `±5%` advanced impedance, `3/3mil`, drill minima, blind-via minima | internal capability numerics without governed refresh path | delete |
| `100% electrical testing`, coupon counts, exact verification coverage | internal service/capability scope | delete or rewrite to generic verification posture |
| `30-40%` cost uplift, `15-25%` blind-via cost, `20-30%` via-in-pad cost, material premium percentages | commercial and project-specific | delete |
| Generic FR-4 Dk/Df ladders, standard-vs-mid-Tg reflow counts, temperature-use ceilings | not anchored to one official exact product under one method | rewrite as family-level selection framing |
| Halogen thresholds, lamination-pressure deltas, drill-feed deltas | standards/process claims not anchored here for this first-wave pack | delete |
| Stackup copper-weight, dielectric-window, distributed-capacitance, and impedance-width tables | recipe leakage and geometry-derived numerics | delete |
| Thermal conductivity comparisons used as direct board-temperature promises | performance leakage from platform selection | delete or keep only platform differentiation without outcome numerics |
| Flex bend-cycle multipliers, bend-radius minima, rigid-to-flex accuracy | internal or project-specific capability / design-rule numbers | delete |
| Via minima, aspect ratio, annular ring, solder-mask dam, copper-balance targets, decoupling distances | capability, standards, and cookbook-threshold mixture | delete |
| Inventory, region support, same-day review, stocked-material claims | dynamic commercial status | delete |

## 6. Primary Sources

### Official manufacturer sources

| Company | source_id | Why it belongs in the pack | Best use |
| --- | --- | --- | --- |
| Isola | `isola-fr408-datasheet` | official FR-4-family exact-product anchor | FR-4 family boundary control |
| Isola | `isola-fr408hr-datasheet` | official FR-4-family exact-product anchor | FR-4 family boundary control |
| ITEQ | `iteq-it-180a-page` | official exact-product high-Tg FR-4 page | high-Tg FR-4 example |
| Panasonic | `panasonic-megtron-6-r5775n` | official exact-grade public page | low-loss multilayer example |
| Panasonic | `panasonic-megtron-6-datasheet` | official family datasheet | condition and grade control |
| Rogers | `rogers-ro4350b-product-page` | official RF laminate page | RF hybrid branch |
| Rogers | `rogers-ro4000-datasheet` | official RO4000 data sheet | process `Dk / Df` values |
| Rogers | `rogers-rt-duroid-5880-product-page` | official PTFE laminate page | PTFE branch |
| Rogers | `rogers-rt-duroid-5870-5880-datasheet` | official PTFE data sheet | exact PTFE values |
| AGC | `agc-rf-10-product-page` | official high-Dk RF page | high-Dk RF branch |
| AGC | `agc-rf-10-datasheet` | official TDS | exact `Dk / Df / thermal conductivity` |
| AGC | `agc-rf-microwave-laminates-page` | official lineup page | family placement only |

### Secondary framing support only

These are not atomic fact sources for hard numeric claims:

- `methods-pcb-stackup-special-process-and-baseline-families`
- `methods-controlled-impedance-tdr-verification-posture`
- `methods-rf-validation-capability`
- `methods-thermal-pcb-platform-selection-posture`
- `methods-rigid-flex-stackup-and-bend-reliability-posture`
- `methods-backdrill-control-capability`
- `/code/blogs/llm_wiki/wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`
- `/code/blogs/llm_wiki/wiki/testing/validation-ladder-from-e-test-to-si-verification.md`

## 7. Usable Technical Facts

Only the following facts are cleared for the first-wave article draft.

| Fact | fact_id | Source type | How to write it safely |
| --- | --- | --- | --- |
| `6-layer` is a layer-count architecture, not one material class | `methods-pcb-stackup-special-process-and-baseline-families` | internal framing | A 6-layer PCB is better treated as a stackup-planning category that can branch into baseline FR-4, RF hybrid, thermal, or flex routes |
| FR-4 should stay at family level unless one exact product is named | `materials-fr4-official-source-coverage` | official datasheet | FR-4 is a family label, so hard values should be tied to named products such as FR408, FR408HR, or IT-180A rather than generalized across all FR-4 |
| `IT-180A` high-Tg example | `materials-iteq-it-180a` | official product page | ITEQ lists `IT-180A` with `Tg 175 C`, `Td 345 C`, and `Dk 4.1 / Df 0.017` at `10 GHz` with `RC 50%` |
| `MEGTRON 6` low-loss example | `materials-panasonic-megtron-6` | official page + datasheet | Panasonic publishes a public MEGTRON 6 grade with `Tg 185 C`, `Td 410 C`, and low-loss dielectric values, but grade and frequency context should stay attached |
| `RO4350B` RF hybrid example | `materials-rogers-ro4350b` | official page + datasheet | Rogers publishes `RO4350B` as a low-loss RF laminate with epoxy/glass-style processing and a process `Dk 3.48 +/- 0.05` at `10 GHz / 23 C` |
| `RT/duroid 5880` PTFE example | `materials-rogers-rt-duroid-5880` | official page + datasheet | Rogers publishes `RT/duroid 5880` with `Dk 2.20 +/- 0.02` and `Df 0.0009 at 10 GHz`, making it a useful PTFE benchmark |
| `RF-10` high-Dk RF example | `materials-agc-rf-10` | official page + datasheet | AGC publishes `RF-10` as a high-Dk RF laminate with `Dk 10.2 +/- 0.3` and `Df 0.0025 at 10 GHz` |
| Controlled impedance should be paired with verification | `methods-controlled-impedance-tdr-verification-posture` | internal posture | Controlled impedance should be described as a stackup-and-measurement workflow, often paired with TDR or coupon-style validation, not just nominal target labels |
| RF work may require an RF-specific validation layer | `methods-rf-validation-capability` | internal posture | RF and mixed RF/digital programs may add coupon, TDR, VNA, and traceability planning, depending on project scope |
| Thermal 6-layer variants should be split by platform | `methods-thermal-pcb-platform-selection-posture` | internal posture | When heat removal dominates, metal-core, ceramic, and heavy-copper options should be evaluated as separate build platforms rather than one generic 6-layer upgrade |
| Rigid-flex 6-layer variants should be split by stackup and bend reliability | `methods-rigid-flex-stackup-and-bend-reliability-posture` | internal posture | A 6-layer rigid-flex build should be framed around stackup, transition design, and bend reliability planning rather than generic layer-count capability |

Not cleared as usable hard facts:

- any geometry-derived width table
- any via-size ladder
- any shop capability number
- any cost or lead-time number
- any verification coverage percentage

## 8. Article Data Targets

- Target minimum official technical facts: `8`
- Target minimum early official anchors in body: `4`
- Early fact table required: `yes`
- Second structured information layer required: `yes`
- Recommended second layer format:
  - one early decision table
  - one 4-column comparison block
- Glossary needed: `no`
- Supplier checklist needed: `yes`

Recommended early table:

- `Build route | What changes at 6 layers | Best material / process anchor | What to verify before release`

Recommended second early structure:

- `Baseline FR-4`
- `RF / low-loss hybrid`
- `Thermal platform`
- `Flex / rigid-flex`

## 9. In-Body Citation Plan

| Article section | Claim to support | Planned fact / source anchor |
| --- | --- | --- |
| Intro / quick answer | `6-layer` is a stackup-planning category rather than one fixed product | `methods-pcb-stackup-special-process-and-baseline-families` |
| Early materials table | FR-4 is a family; exact hard values should stay product-specific | `materials-fr4-official-source-coverage` |
| High-Tg FR-4 example | `IT-180A` exact product numeric example | `materials-iteq-it-180a` / `iteq-it-180a-page` |
| Low-loss multilayer example | `MEGTRON 6` exact-grade numeric example | `materials-panasonic-megtron-6` / `panasonic-megtron-6-r5775n` |
| RF hybrid branch | `RO4350B` exact product example | `materials-rogers-ro4350b` / `rogers-ro4000-datasheet` |
| PTFE branch | `RT/duroid 5880` exact product example | `materials-rogers-rt-duroid-5880` / `rogers-rt-duroid-5870-5880-datasheet` |
| High-Dk compact RF branch | `RF-10` exact product example | `materials-agc-rf-10` / `agc-rf-10-datasheet` |
| Controlled-impedance section | impedance should be tied to verification workflow | `methods-controlled-impedance-tdr-verification-posture` |
| RF validation section | RF builds can require coupon / TDR / VNA planning | `methods-rf-validation-capability` |
| Thermal branch | `MCPCB`, ceramic, and heavy-copper are different platform choices | `methods-thermal-pcb-platform-selection-posture` |
| Rigid-flex branch | rigid-flex introduces stackup and bend-reliability planning | `methods-rigid-flex-stackup-and-bend-reliability-posture` |

## 10. AI-SEO Evidence Primitives

### A. Quick Answer / Definition Material

| Field | Content |
| --- | --- |
| Core definition | A 6-layer PCB is a multilayer stackup category that gives designers more room to separate signals, planes, and special material zones, but it does not imply one default material set or one factory capability envelope |
| When it matters | It matters when a 4-layer stackup starts forcing tradeoffs between routing density, reference continuity, thermal path, RF loss, or bend architecture |
| Deciding factor | The main decision is not the number `6` alone, but which stackup branch the design actually needs: baseline FR-4, low-loss hybrid, thermal platform, or rigid-flex |
| Safe short version | A 6-layer PCB is usually the first multilayer step where stackup architecture becomes the main engineering decision. The safe way to specify it is to separate material choice, validation method, and special-build route instead of treating `6-layer` as one universal recipe. |

### B. Inline Citation Handles

| Claim cluster | Inline citation handle | Source URL basis | Safe sentence pattern |
| --- | --- | --- | --- |
| FR-4 family boundary | `根据 Isola 官方 FR408 / FR408HR 资料` | `isola-fr408-datasheet`, `isola-fr408hr-datasheet` | 根据 Isola 官方 FR408 / FR408HR 资料，`FR-4` 更适合作为材料家族标签，而不是一组固定数值 |
| High-Tg FR-4 example | `ITEQ 的 IT-180A 官方页面列出` | `iteq-it-180a-page` | ITEQ 的 `IT-180A` 官方页面列出 `Tg 175 C` 和 `10 GHz` 条件下的介电参数，可作为高-Tg FR-4 的公开产品锚点 |
| Process-friendly low-loss example | `Panasonic 公布的公开级别 MEGTRON 6 数据显示` | `panasonic-megtron-6-r5775n`, `panasonic-megtron-6-datasheet` | Panasonic 公布的公开级别 `MEGTRON 6` 数据显示，该材料在高耐热和低损耗之间提供了适合高速多层板的平衡 |
| RF hybrid example | `Rogers 在 RO4350B 官方数据中给出` | `rogers-ro4000-datasheet` | Rogers 在 `RO4350B` 官方数据中给出 `10 GHz / 23 C` 条件下的工艺介电常数和损耗值 |
| PTFE example | `Rogers 的 RT/duroid 5880 官方资料显示` | `rogers-rt-duroid-5870-5880-datasheet` | Rogers 的 `RT/duroid 5880` 官方资料显示其低介电常数和低损耗更适合更高频的 PTFE 路线 |
| High-Dk RF example | `AGC RF-10 官方 TDS 给出` | `agc-rf-10-datasheet` | `AGC RF-10` 官方 TDS 给出了 `10 GHz` 条件下的高 Dk / 低损耗参数，可用来说明高 Dk RF 层压板的另一条路线 |
| Validation posture | `现有工艺资料反复把阻抗目标和 TDR / coupon 验证绑定在一起` | `methods-controlled-impedance-tdr-verification-posture` | 现有工艺资料反复把阻抗目标和 `TDR / coupon` 验证绑定在一起，因此阻抗章节应强调验证流程而不是几何表格 |

### C. Authority / Reviewer Inputs

| Field | Content |
| --- | --- |
| Author entity | `HILPCB content team` |
| Reviewer entity | `llm_wiki engineering review workflow` |
| Credentials or scope | multilayer stackup framing, official material-source normalization, and unsupported-claim removal |
| Public profile / entity URL | none specified in this pack |
| Safe fallback wording | Reviewed against official material datasheets and internal `llm_wiki` method cards for stackup, validation, thermal-platform, and rigid-flex posture |

### D. FAQ Query Phrasing Seeds

| User query style | Mapped FAQ question | Source / evidence basis |
| --- | --- | --- |
| `what is a 6 layer pcb used for` | What changes when a design moves from 4 layers to 6 layers? | stackup + posture fact cards |
| `best material for 6 layer pcb` | Does a 6-layer PCB always use standard FR-4? | FR-4 family boundary + product-grade material cards |
| `6 layer pcb impedance control` | Why should impedance on a 6-layer board be tied to stackup and verification instead of one width table? | impedance posture fact card |
| `6 layer rf pcb material` | When does a 6-layer board need low-loss or PTFE laminate instead of FR-4? | Rogers / Panasonic / AGC material cards |
| `6 layer rigid flex pcb` | Is a 6-layer rigid-flex board just a normal 6-layer PCB that bends? | rigid-flex posture fact card |
| `6 layer pcb thermal design` | When should a 6-layer thermal design move from FR-4 into metal-core, heavy-copper, or ceramic routes? | thermal-platform posture fact card |

## 11. Handoff To Template

- Recommended template:
  - `prompts_template/shared/query.md`
  - `prompts_template/shared/evidence-pack-template.md`
  - `prompts_template/hilpcb/query-overlay.md`
- Recommended title type:
  - query + engineering decision
- Suggested title direction:
  - `What Is a 6-Layer PCB and When Should You Use One?`
  - or `6 Layer PCB Manufacturing: How to Choose Stackup, Materials, and Validation Path`
- Recommended modules:
  - `none`
  - optional lightweight comparison block only
- Recommended early table type:
  - `Route | What 6 layers solve | Safe material anchor | What to verify`
- Recommended second-layer structure:
  - `Baseline FR-4`
  - `RF / low-loss hybrid`
  - `Thermal platform`
  - `Flex / rigid-flex`
- Recommended site handoff links:
  - product pages only, used conservatively
  - prioritize `high-frequency-pcb`, `rigid-flex-pcb`, `high-thermal-pcb`, and `impedance-calculator`

### Current-blog section bridge map for prompt execution

| Current structure | Prompt action |
| --- | --- |
| Front matter and capability quote block | exclude |
| `Why 6 Layers?` | keep, but remove price and absolute-performance claims |
| `FR-4 Based 6 Layer PCBs` | keep with family-level framing plus exact-product anchors only |
| `Three Standard 6 Layer FR-4 Stack-Up Configurations` | rewrite into non-numeric architecture comparison |
| `High-Frequency 6 Layer PCBs` | keep with exact material cards and no geometry tables |
| `Aluminum-Core and Metal-Base 6 Layer PCBs` | keep only as platform-selection posture |
| `6 Layer Flex and Rigid-Flex Constructions` | keep only as posture and tradeoff framing |
| `Impedance Control` | keep only as stackup + verification logic |
| `Via Strategies` | keep only vocabulary and tradeoff logic |
| `Lamination, Drilling & Surface Finish` | keep as qualitative workflow framing |
| `DFM Rules` | keep only the non-numeric engineering checks |
| `Cost Factors and How to Optimize Them` | exclude |
| `Getting Your 6 Layer Project Started with HILPCB` | replace with neutral next-step / RFQ preparation guidance |

## 12. Final Preflight

- Hard information extracted: `yes`
- `public facts / project judgments / site-specific capability references / unsupported` separated: `yes`
- Primary official sources present for all usable hard numerics: `yes`
- Unsupported numerics flagged for deletion rather than silent reuse: `yes`
- Wiki pages kept as secondary framing only: `yes`
- Early citation plan prepared: `yes`
- Quick answer material prepared: `yes`
- Inline citation handles prepared: `yes`
- Authority / reviewer fallback prepared: `yes`
- FAQ query phrasing seeds prepared: `yes`
- Template choice fixed to `query`: `yes`

Conservative verdict:

- This pack is usable for a first-wave `query` rewrite of the `6-layer` blog.
- It is not cleared for fabrication-capability numerics, geometry tables, cost numbers, or service-claim reuse.
