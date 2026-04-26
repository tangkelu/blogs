# P4-06 6-Layer Bridge Prep

Date: 2026-04-26

## Purpose

This control note defines the first-wave `P4-06` bridge-prep posture for:

- `/code/hileap/frontendHIL/docs/hilpcb_blog_04.24/en/6-layer-pcb-manufacturing.md`

The goal is not to rewrite the blog.

The goal is:

- choose the safe prompt template for the first bridge
- define which claim classes are allowed into a future evidence pack
- identify stable `fact_id` and `source_id` candidates already present in `llm_wiki`
- map the current blog structure to `keep / downgrade / delete / exclude` bridge behavior
- prevent unsupported `B / C / D / E / F / G` numerics from entering prompt execution

This note is bridge-prep only.

It does not declare `high_numeric_density_ready`.

## Template Choice

Default first-wave template choice:

- `prompts_template/shared/query.md`
- with `prompts_template/shared/evidence-pack-template.md`
- plus `prompts_template/hilpcb/query-overlay.md`

Why:

- `6-layer` is in the first-wave queue for conservative bridging
- the current article is closer to an engineering decision/query page than a stable pillar page
- the safe bridge depends on pruning unsupported numerics rather than preserving the current blog density

## Scope

In scope for the future evidence pack:

- conservative `6-layer` engineering framing
- material-family selection framing
- stackup and planning posture
- validation and verification posture
- special-construction branching such as RF hybrid, thermal platform, and rigid-flex as controlled variants

Out of scope for the future evidence pack:

- direct reuse of current HIL capability banner claims
- board-level impedance geometry tables
- via-rule and aspect-ratio numeric tables
- cost, lead-time, and DFM turnaround marketing claims
- reliability thresholds presented as hard transferable rules

## Allowed Claim Classes

Allowed by default:

- `A` material datasheet numerics when backed by official product fact cards
- non-numeric process posture from existing methods cards
- non-numeric validation posture from existing methods cards
- non-numeric platform-selection framing from existing methods cards

Allowed only after downgrade into non-numeric wording:

- `E` reflow / thermal-use / flex-life / bend-reliability ideas
- RF / rigid-flex / thermal platform extension language when it stays at posture level
- architecture examples that remain clearly illustrative rather than default recipes

## Excluded Claim Classes

Do not allow into the usable `P4-06` pack:

- `B` fabrication capability numerics
- `C` standards / qualification / acceptance numerics
- `D` board-level impedance / channel / geometry numerics
- `E` reliability thresholds and hard process limits
- `F` dynamic commercial numerics
- `G` internal marketing numerics or supplier-positioning proof claims

Specific excluded clusters from the current `6-layer` draft:

- `±8%` impedance
- `3/3mil`
- `100% electrical testing`
- `30-40%` cost uplift
- `2+` reflows / `260 C`-style transferable reliability thresholds
- stackup recipe numbers such as copper weights and dielectric windows
- impedance width tables and distributed-capacitance numbers
- via-rule numerics such as aspect ratio, annular ring, or coupon counts

## Must-Refresh Handling

Per current evidence-pack policy, treat the following as refresh-sensitive or reject-if-unrefreshed:

- any HIL capability, service, turnaround, or same-day response claim
- any price, cost, uplift, lead-time, MOQ, or yield wording
- any live certification, listing, approval, or current capacity statement
- any value whose current truth depends on internal capability rather than official product documentation

Bridge rule:

- if a candidate claim depends on refresh-sensitive internal commercial or capability language, exclude it from the pack unless a governed refresh path exists

## Candidate `fact_id` Set

Safe primary candidates:

- `materials-fr4-official-source-coverage`
- `materials-iteq-it-180a`
- `materials-panasonic-megtron-6`
- `materials-rogers-ro4350b`
- `materials-rogers-rt-duroid-5880`
- `materials-agc-rf-10`
- `methods-pcb-stackup-special-process-and-baseline-families`
- `methods-controlled-impedance-tdr-verification-posture`
- `methods-rf-validation-capability`
- `methods-thermal-pcb-platform-selection-posture`
- `methods-rigid-flex-stackup-and-bend-reliability-posture`

Secondary support candidates:

- `methods-backdrill-control-capability`

Notes:

- `methods-backdrill-control-capability` is optional support only; `6-layer` does not need backdrill to be a core bridge theme.
- No current atomic fact card was found for generic `Isola 370HR`; do not invent one.
- If future prompt work needs broader process framing, the following are wiki pages, not atomic fact cards:
  - `processes-advanced-pcb-fabrication-and-stackup-planning`
  - `testing-validation-ladder-from-e-test-to-si-verification`

## Candidate `source_id` Set

Primary official material-source candidates:

- `isola-fr408-datasheet`
- `isola-fr408hr-datasheet`
- `iteq-it-180a-page`
- `panasonic-megtron-6-r5775n`
- `panasonic-megtron-6-datasheet`
- `rogers-ro4350b-product-page`
- `rogers-ro4000-datasheet`
- `rogers-rt-duroid-5880-product-page`
- `rogers-rt-duroid-5870-5880-datasheet`
- `agc-rf-10-product-page`
- `agc-rf-10-datasheet`
- `agc-rf-microwave-laminates-page`

Internal posture-support source candidates:

- `frontendapt-materials-spread-glass-fr4-page-en`
- `frontendapt-materials-isola-pcb-page-en`
- `frontendapt-pcb-fr4-pcb-page-en`
- `frontendapt-pcb-high-tg-pcb-page-en`
- `frontendapt-pcb-heavy-copper-pcb-page-en`
- `frontendapt-pcb-pcb-stack-up-page-en`
- `frontendapt-pcb-multi-layer-laminated-structure-page-en`
- `frontendapt-pcb-special-pcb-manufacturing-page-en`
- `frontendapt-pcb-pcb-impedance-control-page-en`
- `frontendapt-pcb-high-speed-pcb-page-en`
- `frontendapt-pcb-multilayer-pcb-page-en`
- `frontendapt-high-frequency-pcb-page-en`
- `frontendapt-microwave-pcb-page-en`
- `frontendapt-pcb-rigid-flex-pcb-page-en`
- `frontendapt-pcb-flex-pcb-page-en`
- `frontendapt-pcba-flex-rigid-flex-page-en`
- `frontendapt-pcb-high-thermal-pcb-page-en`
- `frontendapt-pcb-metal-core-pcb-page-en`
- `frontendapt-pcb-ceramic-pcb-page-en`
- `frontendhil-rigid-flex-pcb-product-page-en`
- `frontendhil-flex-pcb-product-page-en`
- `frontendhil-high-frequency-product-page-en`
- `frontendhil-rogers-product-page-en`
- `frontendhil-high-thermal-pcb-product-page-en`
- `frontendhil-metal-core-pcb-product-page-en`
- `frontendhil-ceramic-pcb-product-page-en`
- `frontendhil-heavy-copper-pcb-product-page-en`

## Section-By-Section Bridge Guidance

### Front Matter And Capability Banner

Current section(s):

- page description
- capability quote block

Bridge posture:

- exclude from the first-wave evidence pack

Why:

- current wording contains unsupported `B / F / G` claims:
  - `±8%`
  - `3/3mil`
  - `100% electrical testing`
  - same-day DFM feedback
  - geography-linked service marketing

Allowed replacement direction:

- use a non-numeric sentence that `6-layer` is a common entry point into true multilayer fabrication and usually involves stackup review, material choice, and verification planning

### `Why 6 Layers? The Engineering Case`

Bridge posture:

- keep with conservative wording

Allowed support:

- `methods-pcb-stackup-special-process-and-baseline-families`
- `methods-controlled-impedance-tdr-verification-posture`

Downgrade rules:

- keep the engineering logic of dedicated planes, cleaner routing separation, and better planning discipline
- delete the `30-40%` cost uplift framing
- avoid absolute claims that `6-layer` always eliminates split-plane compromises or always avoids shielding components

### `FR-4 Based 6 Layer PCBs: The Industry Workhorse`

Bridge posture:

- keep, but only through product-grade and family-controlled material framing

Allowed support:

- `materials-fr4-official-source-coverage`
- `materials-iteq-it-180a`

Downgrade or exclude:

- do not preserve unsupported broad FR-4 vendor numeric ladders as if one table fits all FR-4
- do not keep generic lead-free reflow counts or hard operating-temperature rules as universal thresholds
- do not keep halogen-threshold language unless future prompt execution explicitly uses the official source and conditions

Safe bridge direction:

- present standard FR-4, higher-Tg FR-4, and halogen-free FR-4 as family / selection context
- attach hard numbers only to exact product cards already present in `llm_wiki`

### `Three Standard 6 Layer FR-4 Stack-Up Configurations`

Bridge posture:

- downgrade heavily

Allowed support:

- `methods-pcb-stackup-special-process-and-baseline-families`

Exclude:

- copper weight tables
- dielectric windows
- distributed capacitance numbers
- claims that one listed configuration should be the universal starting default

Safe bridge direction:

- retain only the idea that common `6-layer` stackups trade off routing density, shielding, and power-plane organization

### `High-Frequency 6 Layer PCBs: Rogers, PTFE & Hybrid Builds`

Bridge posture:

- keep as a controlled material-selection branch

Allowed support:

- `materials-rogers-ro4350b`
- `materials-rogers-rt-duroid-5880`
- `materials-panasonic-megtron-6`
- `materials-agc-rf-10`
- `methods-rf-validation-capability`

Downgrade or exclude:

- board-level insertion-loss examples
- exact geometry-conversion tables that turn material Dk into guaranteed trace widths
- claims that a particular hybrid stackup is a default manufacturing recipe

Safe bridge direction:

- retain the principle that some RF / high-speed `6-layer` builds use hybrid material strategies
- keep official product values only with exact material name, frequency, and method context

### `Aluminum-Core and Metal-Base 6 Layer PCBs`

Bridge posture:

- keep only as platform-selection posture with tightly limited numerics

Allowed support:

- `methods-thermal-pcb-platform-selection-posture`

Downgrade or exclude:

- board-level thermal-drop comparisons
- universal lifetime or temperature-reduction outcomes
- exact base-thickness defaults unless directly tied to a material/platform source and still needed

Safe bridge direction:

- preserve the distinction between aluminum-base, copper-base, and other thermal platforms
- present them as different thermal routes rather than as guaranteed thermal outcomes

### `6 Layer Flex and Rigid-Flex Constructions`

Bridge posture:

- keep only as posture and variant framing

Allowed support:

- `methods-rigid-flex-stackup-and-bend-reliability-posture`

Downgrade or exclude:

- explicit bend-radius formulas
- bend-life thresholds
- transition accuracy numbers
- statements that dynamic-flex reliability is source-backed at a fixed numeric threshold

Safe bridge direction:

- retain that `6-layer` can extend into flex / rigid-flex variants and that stackup, copper type, coverlay, and bend reliability matter

### `Impedance Control: Microstrip and Stripline at 6 Layers`

Bridge posture:

- keep only as verification posture, not as a geometry-number section

Allowed support:

- `methods-controlled-impedance-tdr-verification-posture`
- `methods-rf-validation-capability`

Exclude:

- `50 ohm / 100 ohm` width tables
- dielectric-thickness-to-trace-width formulas
- distributed-capacitance numerics
- `±8-10%` achievable-tolerance claims
- panel coupon-count numerics

Safe bridge direction:

- preserve that controlled impedance at `6-layer` depends on stackup planning plus verification such as `TDR` / coupon correlation

### `Via Strategies: Through-Hole, Blind, and Via-in-Pad`

Bridge posture:

- downgrade to architecture vocabulary only

Allowed support:

- `methods-pcb-stackup-special-process-and-baseline-families`

Exclude:

- minimum finished hole sizes
- aspect-ratio rules
- annular-ring numbers
- class-linked via acceptance implications

Safe bridge direction:

- retain only that through-hole, blind-via, and via-in-pad choices trade routing density, manufacturability, and cost

### `Lamination, Drilling & Surface Finish`

Bridge posture:

- keep only as qualitative process-route framing

Allowed support:

- `methods-pcb-stackup-special-process-and-baseline-families`
- `processes-advanced-pcb-fabrication-and-stackup-planning`

Notes:

- `processes-advanced-pcb-fabrication-and-stackup-planning` is a wiki page, not an atomic fact card

Exclude:

- exact lamination recipe numbers
- drill-window numerics
- surface-finish performance numbers if not tied to exact official sources

### `DFM Rules That Prevent Costly Respins`

Bridge posture:

- heavily prune

Allowed support:

- `methods-pcb-stackup-special-process-and-baseline-families`

Exclude:

- minimum feature-size numbers
- spacing rules
- via-rule numbers
- copper-balance percentages
- rigid DFM thresholds masquerading as universal manufacturing rules

Safe bridge direction:

- keep only that manufacturability review should address copper balance, stackup realism, routing density, and chosen process family

### `Cost Factors and How to Optimize Them`

Bridge posture:

- exclude from first-wave bridge pack

Why:

- current section is dominated by `F` dynamic commercial numerics and pricing heuristics

### `Getting Your 6 Layer Project Started with HILPCB`

Bridge posture:

- exclude direct service and turnaround claims

Allowed replacement direction:

- if the future prompt needs a closing section, keep it non-numeric and non-committal

## Refresh-Required Items

If any of the following are requested later, they must be refreshed or removed:

- HIL impedance tolerance
- HIL minimum trace/space
- HIL electrical-test scope
- same-day DFM turnaround
- cost uplift versus `4-layer`
- any quick-turn or prototype timing
- any coupon-count, TDR-coverage, or VNA-frequency commitment
- any current stock / recommendation / availability wording tied to a specific material family

## Open Gaps

- No governed capability-number layer exists yet for `6-layer` fabrication numerics such as impedance tolerance, line/space, via limits, or coupon counts.
- No safe static policy exists yet for dynamic commercial claims in this branch.
- FR-4 family coverage is improved, but the current article still names supplier/material ladders more broadly than the existing exact-product fact layer fully covers.
- Internal posture cards are usable for process and validation framing, but they are not substitutes for authoritative capability numbers.

## Stop Conditions

Do not approve a `6-layer` evidence pack for `P4-06` if any of the following remain:

- unsupported `B` fabrication capability numbers
- unsupported `C` standards / acceptance numbers
- unsupported `D` impedance-geometry or board-interpretation numbers
- unsupported `E` reliability thresholds
- unsupported `F` cost or lead-time numbers
- unsupported `G` HIL marketing or supplier-proof claims
- any claim lacking a traceable `fact_id` and `source_id`
- any wiki page used as if it were an atomic fact instead of clearly marked secondary support

## Conservative Readiness Verdict

Current verdict for this bridge-prep note:

- `6-layer` is suitable for first-wave `P4-06` bridge-prep under the `query` template only
- it is suitable only for a conservative evidence pack that keeps:
  - material-selection facts
  - non-numeric stackup/process posture
  - non-numeric validation posture
  - controlled variant framing for RF, thermal, and rigid-flex branches
- it is not suitable for carrying forward the current blog's capability banner, cost numerics, impedance geometry tables, via-rule numbers, or dynamic service claims

This is a conservative bridge-prep `go` for controlled evidence-pack assembly, not a high-numeric-density unlock.
