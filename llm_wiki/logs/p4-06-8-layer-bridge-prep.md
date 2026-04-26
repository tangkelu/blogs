# P4-06 8-Layer Bridge Prep

Date: 2026-04-26

## Purpose

This control note prepares the first-wave `P4-06` evidence pack for the current `8-layer` blog without unlocking high-numeric-density reuse.

It is not a rewrite plan and not a readiness unlock.

It defines the safest evidence-pack boundary for future prompt execution against:

- `/code/hileap/frontendHIL/docs/hilpcb_blog_04.24/en/8-layer-pcb-manufacturing.md`

## Template Choice

Default first-wave template set:

- `prompts_template/shared/query.md`
- `prompts_template/shared/evidence-pack-template.md`
- `prompts_template/hilpcb/query-overlay.md`

Use `query` posture, not `pillar`, because the current page is still closest to a direct engineering/manufacturing decision page and still needs strong claim control.

## Scope

In scope for this bridge-prep note:

- conservative `8-layer` architecture framing
- material-family and exact-product example handling where official anchors already exist
- stackup / impedance / validation workflow posture
- controlled downgrade of internal capability language into planning-context language

Out of scope:

- full blog rewrite
- blog readiness upgrade
- new numeric recovery
- supplier-proof or HIL capability proof
- dynamic commercial or certification handling

## Governance Position

`8-layer-pcb-manufacturing` remains a first-wave bridge candidate because the article backbone can be reduced to supported material, stackup, and workflow framing.

It is still only `bridge_prep_only` for `P4-06` use because the current draft contains unsupported `B / C / D / E / F / G` numerics and HIL-specific assertions that must not enter a usable evidence pack.

## Allowed Claim Classes

Allowed in the usable first-wave pack:

- `A` material-property support only when tied to official product/family anchors and preserved with product identity and conditions
- non-numeric process and validation posture from governed method cards
- non-numeric stackup planning language
- non-numeric hybrid-material and rigid-flex boundary language when clearly framed as posture, not capability proof
- system-context references only when they stay descriptive and do not become board-performance guarantees

## Excluded Claim Classes

Exclude from the usable first-wave pack:

- `B` fabrication capability numerics: trace/space, drill, via, aspect ratio, annular ring, registration, board-thickness tolerance, backdrill, impedance tolerance tables
- `C` standards / acceptance numerics: IPC thresholds, plating minima, warpage limits, class tables, coupon-count rules
- `D` board-level SI / EMC outcome numerics: `dB` reduction, channel budgets, embedded-capacitance tables, exact impedance-target tables when used as manufacturing guarantees
- `E` HDI / build-up / rigid-flex / reliability numerics: bend radius, flex thickness, via minima, lamination counts, process-pressure modifiers, reflow-cycle heuristics
- `F` dynamic commercial numerics: lead time, cost uplift, scaling, same-day support, prototype windows
- `G` supplier-status or assurance assertions: stock claims, universal quality claims, certification-proof claims, “relied on by region” claims

## Must-Refresh Handling

For first-wave `8-layer`, the default should be stricter than normal refresh handling:

- dynamic commercial items should be excluded, not merely refreshed
- HIL capability numbers should be excluded, not refreshed from current blog text
- internal exact tolerance or validation-scope numbers should not enter the pack unless a separate governed capability layer exists
- if any future evidence pack keeps a dynamic item anyway, it must be marked `must_refresh: true` and tied to a current primary source

## Candidate Fact IDs

These are the safest current candidate fact cards for a first-wave `8-layer` evidence pack.

### Primary usable candidates

- `materials-fr4-official-source-coverage`
- `materials-non-isola-fr4-to-very-low-loss-coverage`
- `materials-panasonic-megtron-4-low-loss-product-coverage`
- `methods-controlled-impedance-tdr-verification-posture`
- `methods-high-layer-count-backdrill-and-registration-posture`
- `methods-spread-glass-and-controlled-impedance-planning`
- `methods-hybrid-rf-stackup-capability`
- `methods-rigid-flex-stackup-and-bend-reliability-posture`

### Usable as wiki/topic notes, not atomic facts

- `processes-advanced-pcb-fabrication-and-stackup-planning`
- `processes-hybrid-rf-stackup-strategy`
- `testing-validation-ladder-from-e-test-to-si-verification`

Notes:

- The three IDs above are wiki/topic pages. They can support pack notes and retrieval framing, but they should not be pretended to be atomic single-claim fact cards.
- Material cards should only support exact-product numerics where the underlying source card already preserves product identity and conditions.

## Candidate Source IDs

Most conservative first-wave source candidates:

- `isola-fr408-datasheet`
- `isola-fr408hr-datasheet`
- `panasonic-megtron-4-r5725-r5620`
- `panasonic-megtron-4-datasheet`
- `iteq-it-150da-page`
- `shengyi-s1000-2m-product-page`
- `frontendapt-materials-spread-glass-fr4-page-en`
- `frontendapt-materials-controlled-impedance-stackups-page-en`
- `frontendapt-materials-megtron-pcb-page-en`
- `frontendapt-pcb-pcb-impedance-control-page-en`
- `frontendapt-pcb-high-speed-pcb-page-en`
- `frontendapt-pcb-multilayer-pcb-page-en`
- `frontendapt-pcb-high-layer-count-pcb-page-en`
- `frontendapt-pcb-advanced-pcb-manufacturing-page-en`
- `frontendhil-high-speed-product-page-en`
- `frontendhil-hdi-pcb-product-page-en`
- `frontendhil-teflon-pcb-product-page-en`
- `frontendhil-rogers-product-page-en`
- `frontendhil-high-frequency-product-page-en`
- `frontendapt-high-frequency-pcb-page-en`
- `frontendapt-microwave-pcb-page-en`
- `frontendapt-pcb-rigid-flex-pcb-page-en`
- `frontendapt-pcb-flex-pcb-page-en`
- `frontendapt-pcba-flex-rigid-flex-page-en`
- `frontendhil-rigid-flex-pcb-product-page-en`
- `frontendhil-flex-pcb-product-page-en`

## Section-By-Section Bridge Guidance

Map future prompt execution to the current blog structure, but only within the following boundaries.

### 1. When 6 Layers Are Not Enough: The Case for 8

Allow:

- qualitative framing that `8-layer` gives more reference-plane and partitioning flexibility than thinner multilayer layouts
- mixed-signal, power-distribution, and EMI-control posture without exact outcome numbers

Exclude:

- `FCC Class B / CISPR 22 Class B` threshold or comparison numerics
- `10dB` or `6-12dB` emissions-reduction claims
- `25-35%` cost uplift
- any claim that `8-layer` is the default fix for certification failure

### 2. The Three Stack-Up Architectures Every Engineer Should Know

Allow:

- architecture vocabulary such as reference-plane adjacency, signal/plane pairing, and tradeoff framing
- stackup planning posture from `methods-spread-glass-and-controlled-impedance-planning` and `processes-advanced-pcb-fabrication-and-stackup-planning`

Exclude:

- `3-5mil` dielectric spacing
- `200-400pF/cm²` embedded-capacitance values
- `500MHz` discrete-capacitor crossover claim
- any pack language that turns one stackup diagram into a universal default construction table

### 3. Mixed-Signal Design: Analog and Digital on One Board

Allow:

- unified-ground versus split-ground caution at qualitative level
- placement and return-path framing

Exclude:

- `100MHz`, `15mm`, `1.5mm`, `λ/20`, or other via-fencing and slot-antenna numerics
- any universal mixed-signal geometry rule stated as manufacturing guidance

### 4. Material Systems for 8 Layer PCBs

Allow:

- FR-4 must stay family-level, not one generic numeric row
- product-grade examples such as `FR408`, `FR408HR`, `ITEQ IT-150DA`, `Shengyi S1000-2M`, and `MEGTRON 4` where tied to exact source conditions
- low-loss/hybrid framing without board-outcome promises

Exclude:

- generic `8-layer` thickness defaults as governed manufacturing windows
- ungoverned `Tg`, `Df`, `CTE`, reflow-count, pressure-modifier, or operating-temperature numbers lifted from the current blog body without exact fact/source mapping
- halogen-free processing modifiers such as `5-10% higher lamination pressure`
- PTFE mismatch numbers when not tied to exact product source and condition

### 5. 8 Layer PCBs for Wireless and RF Applications

Allow:

- hybrid RF stackup posture
- use of selective premium dielectric on signal-critical paths as a design strategy

Exclude:

- exact RF-material default prescriptions for all `8-layer` wireless boards
- via-transition geometry rules such as `4 ground vias within one via diameter`
- any board-level RF performance promise

### 6. 8 Layer Rigid-Flex for Medical and Aerospace

Allow:

- rigid-flex as a separate construction branch with its own stackup and bend-reliability posture
- qualitative statement that rigid-flex requires dedicated material/process review

Exclude:

- `8R-2F`, `25-50μm`, `±4mil`, `0.9mm`, `3mm`, or similar rigid-flex mechanical numbers
- medical/aerospace acceptance implications
- any phrasing that turns rigid-flex internal pages into qualification proof

### 7. Via Architecture: From Through-Hole to Stacked Microvias

Allow:

- via-family vocabulary only: through-hole, blind, buried, stacked microvia
- statement that via architecture changes process route and review requirements

Exclude:

- `10:1`, `0.15mm`, `0.1mm`, `0.4-0.5mm pitch`, `15-25%`, `20-40%`
- any exact escape-routing or cost table
- any microvia-default language that could be read as transferable capability

### 8. Lamination Process and Thickness Control

Allow:

- symmetry, copper balance, and lamination planning as qualitative controls
- internal high-layer / stackup-planning posture

Exclude:

- exact press-cycle counts
- `±10%`, `±5-8%`, `0.75%`, or other tolerances and warpage thresholds
- any claim that current internal posture authorizes transferable thickness-control numbers

### 9. Impedance Control and Crosstalk Management

Allow:

- impedance control as a planning-plus-verification workflow
- TDR/coupon/post-build correlation posture
- crosstalk mitigation as routing/stackup planning vocabulary

Exclude:

- universal target tables such as `90Ω`, `100Ω`, `85Ω`, `40-60Ω`, `50Ω`
- `3W rule` isolation numbers
- any implication that the current corpus authorizes one reusable impedance table for all `8-layer` jobs

### 10. Testing, Tolerances, and Quality Verification

Allow:

- validation-ladder framing: electrical test, impedance verification, deeper SI validation are different evidence layers
- qualitative mention of cross-section, coupon, TDR, and optional deeper validation

Exclude:

- exact tolerance tables
- `100% electrical testing`
- `3-5` coupons per panel
- `25μm` plating minima
- `IPC Class 3` threshold use
- VNA scope framed as universal standard coverage

### 11. DFM Checklist for 8 Layer Designs

Allow:

- checklist-style qualitative manufacturing review prompts
- adjacency, symmetry, return-path, and stackup-review reminders

Exclude:

- `±20%`, `5GHz`, `3mm`, `≥3mil`, or other checklist numerics
- any geometry threshold that implies governed capability support

### 12. Starting Your 8 Layer Project with HILPCB

Allow:

- minimal CTA placeholder only after unsupported commercial/capability claims are stripped
- generic statement that project-specific review is needed for stackup and manufacturing route

Exclude:

- `±8%`, `±5%`, blind/buried-via capability claims, “full EMC-optimized stack-up engineering”
- stock/material-availability claims
- `3/3mil`, `0.1mm`, sequential-lamination capability claims
- `IPC-A-600 Class 2/3`, certification status, `48-hour`, same-day, region-specific customer reliance, production-scaling claims

## Refresh-Required Items

If later prompt work tries to retain any of the following, they require refresh and stronger sourcing first:

- current HIL capability values
- any HIL certification or approval status
- any lead-time, quick-turn, scaling, or same-day-support statement
- any exact impedance-tolerance offer
- any exact validation-scope percentage or coupon count
- any exact material stocking or availability statement

Current first-wave recommendation: keep these items out of the usable evidence pack instead of refreshing them.

## Open Gaps

The following gaps still prevent a denser `8-layer` evidence pack:

- no governed reusable `B` capability layer for impedance tolerance, registration, trace/space, drill/via, or thickness windows
- no safe reusable `C` threshold layer for IPC tolerance or plating/warpage limits
- no safe reusable `D` board-level EMC/SI outcome layer
- no safe reusable `E` rigid-flex / HDI / lamination-count numeric layer
- no governed HIL-specific supplier-proof layer for the closing section

## Stop Conditions

Do not treat `8-layer` as safe for prompt execution if any candidate pack still contains:

- unsupported `B / C / D / E / F / G` numerics from the current blog
- HIL-specific capability claims without a separate governed capability source layer
- internal page language rewritten as standards proof or product-level datasheet truth
- wiki/topic pages cited as if they were atomic numeric facts
- unsupported rigid-flex, HDI, EMC, or commercial numbers

## Conservative Readiness Verdict

Verdict: `bridge_prep_only`

`8-layer-pcb-manufacturing` is suitable for first-wave `P4-06` bridge preparation under the `query` template family only if the usable evidence pack is limited to:

- official material anchors with preserved product identity and conditions
- internal non-numeric process / stackup / validation posture
- explicit exclusion of unsupported capability, standards, SI/EMC, rigid-flex, HDI, and commercial numerics

It is not yet safe for high-numeric-density evidence-pack use, and this note does not change the broader readiness status beyond conservative first-wave preparation.
