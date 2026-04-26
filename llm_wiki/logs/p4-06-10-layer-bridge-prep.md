# P4-06 10-Layer Bridge Prep

Date: 2026-04-26

## Purpose

This control note prepares the first-wave `10-layer` layer-count blog for future `P4-06` evidence-pack execution.

This file is not:

- a blog rewrite
- a readiness unlock
- permission to preserve the current numeric density

This file exists to define the narrowest governed bridge posture that can support future prompt execution without silently carrying unsupported `B / C / D / E / F / G` numerics into an evidence pack.

## Template Choice

Default template choice:

- `prompts_template/shared/query.md`

Required supporting templates:

- `prompts_template/shared/evidence-pack-template.md`
- `prompts_template/hilpcb/query-overlay.md`

Reason:

- `10-layer` is in the first safe bridge wave under `logs/p4-06-first-wave-bridge-queue.md`
- the page is closer to a direct engineering/manufacturing query page than to a stable pillar or hub page
- current bridge posture is conservative and section-driven, not a full topic-hub abstraction

## Scope

In scope for this prep note:

- the current blog at `/code/hileap/frontendHIL/docs/hilpcb_blog_04.24/en/10-layer-pcb-manufacturing.md`
- first-wave conservative bridge preparation only
- fact / source selection that can survive evidence-pack traceability rules today
- section-by-section keep / downgrade / exclude guidance for future prompt execution

Out of scope:

- unsupported fabrication capability recovery
- unsupported HDI / reliability / standards threshold recovery
- dynamic quote, lead-time, or cost refresh work
- `P4-06` readiness unlock beyond conservative bridge-prep

## Conservative Readiness Verdict

`10-layer` is suitable for `first-wave conservative bridge-prep` under `query` template discipline.

It is not suitable for high-numeric-density evidence-pack use.

Current posture:

- bridge-prep verdict: `allowed with pruning`
- readiness verdict: remains `mostly_ready` for conservative rewriting only
- numeric-density verdict: not unlocked

## Allowed Claim Classes

Allowed in the usable evidence pack:

- `A` material datasheet numerics tied to official product-grade cards and official source IDs
- non-numeric stackup / process-planning posture
- guarded HDI / multilayer / impedance / validation vocabulary
- guarded architecture examples rewritten as non-default, non-prescriptive context
- conservative material-family comparisons where existing fact cards already separate exact products and conditions

Allowed only as downgraded wording, not as retained numerics:

- `1+N+1`, `1+8+1`, `2+6+2`, and similar via-structure notation when clearly framed as architecture vocabulary rather than default recipe
- BGA-density pressure, signal-layer pressure, and power-plane pressure as design-context wording
- RF / high-speed material-family selection logic without board-level geometry or performance promises
- rigid-flex coexistence as variant scope rather than a default extension of the main article

## Excluded Claim Classes

Do not allow these into the usable pack:

- `B` fabrication capability numerics such as blind-via size, registration, annular ring, impedance tolerance, fine-line capability, or buried-via capability claims
- `C` standards / qualification / acceptance numerics
- `D` board-level SI or geometry-derived numerics, including impedance width implications or interface-budget interpretation
- `E` HDI / microvia / sequential-lamination reliability numerics, BGA escape recipe tables, and default build-up rules
- `F` dynamic commercial numerics such as cost adders, prototype windows, production lead time, and similar quote-stage claims
- `G` unsupported contextual numerics that function as hidden capability or approval proof

Specific exclusions from the current blog:

- `±50μm`
- `±8%`
- `0.1mm` blind-via capability claim
- cost uplift ranges such as `20-30%` and `15-30%`
- BGA pitch escape tables used as prescriptive routing rules
- sequential-lamination cost tables
- `50-80μm` `RCC` wording as a retained stackup default
- `3/3mil` and `2.5/2.5mil` feature-size claims
- `±4mil` rigid-flex transition accuracy
- all `prototype to production volumes`, `7 business days`, and similar delivery/sustainment claims
- `IPC Class 3 compliance` and similar assurance/compliance claims

## Must-Refresh Handling

Future prompt execution must mark `must_refresh: true` for any item that depends on:

- lead time
- quote-stage production range
- capability/tolerance banners from internal pages
- current certification or compliance status
- any live revision/status if used beyond the current stable fact layer

Default bridge rule:

- if a claim would require refresh and does not already have a governed `fact_id` plus stable `source_id`, exclude it from the usable pack

## Candidate `fact_id` Set

Primary candidate facts for a conservative pack:

- `materials-iteq-it-180a`
- `materials-panasonic-megtron-4`
- `materials-panasonic-megtron-6`
- `materials-shengyi-s1000-2`
- `materials-fr4-official-source-coverage`
- `methods-pcb-stackup-special-process-and-baseline-families`
- `methods-hdi-microvia-and-vippo-process-posture`
- `methods-controlled-impedance-tdr-verification-posture`
- `methods-advanced-validation-scope-segmentation`
- `methods-high-layer-rigid-board-manufacturability-context`
- `methods-high-layer-count-backdrill-and-registration-posture`
- `methods-pcb-prototype-quickturn-and-volume-routing`
- `methods-rigid-flex-stackup-and-bend-reliability-posture`

Notes:

- `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md` is a usable topic wiki candidate for pack notes, but it is not an atomic `fact_id`.
- `wiki/testing/validation-ladder-from-e-test-to-si-verification.md` is also a usable topic wiki candidate for pack notes, but it is not an atomic `fact_id`.
- Do not pretend wiki pages are facts inside the evidence pack.

## Candidate `source_id` Set

Primary candidate source IDs for the conservative pack:

- `iteq-it-180a-page`
- `panasonic-megtron-4-r5725-r5620`
- `panasonic-megtron-4-datasheet`
- `panasonic-megtron-6-r5775n`
- `panasonic-megtron-6-datasheet`
- `shengyi-s1000-2-product-page`
- `isola-370hr-datasheet`
- `frontendapt-pcb-fr4-pcb-page-en`
- `frontendapt-pcb-high-tg-pcb-page-en`
- `frontendapt-pcb-pcb-stack-up-page-en`
- `frontendapt-pcb-multi-layer-laminated-structure-page-en`
- `frontendapt-pcb-hdi-pcb-page-en`
- `frontendapt-pcb-advanced-pcb-manufacturing-page-en`
- `frontendhil-hdi-pcb-product-page-en`
- `frontendapt-pcb-pcb-impedance-control-page-en`
- `frontendapt-pcb-high-speed-pcb-page-en`
- `frontendapt-pcb-multilayer-pcb-page-en`
- `frontendhil-multilayer-pcb-product-page-en`
- `frontendapt-pcb-pcb-prototype-page-en`
- `frontendapt-pcb-quick-turn-pcb-page-en`
- `frontendhil-pcb-prototype-landing-en`
- `frontendhil-quick-turn-pcb-landing-en`
- `frontendapt-pcb-rigid-flex-pcb-page-en`
- `frontendhil-rigid-flex-pcb-product-page-en`

## Section-By-Section Bridge Guidance

### 1. Title, deck, intro, and quick quote

Current structure:

- title and description emphasize `HDI vias`, `BGA escape routing`, and manufacturing constraints
- quick quote includes unsupported HIL capability numerics and delivery claims

Bridge rule:

- keep `10-layer`, `HDI`, `BGA escape routing`, and dense-routing framing
- delete the inline HIL capability quote from the usable pack
- rewrite the intro around architecture pressure, stackup planning, and validation posture rather than capability banners

Allowed support:

- `methods-hdi-microvia-and-vippo-process-posture`
- `methods-pcb-stackup-special-process-and-baseline-families`
- `methods-controlled-impedance-tdr-verification-posture`

### 2. Why designs move to 10 layers

Current structure:

- mixes useful architectural rationale with unsupported pin-count, plane-count, and cost deltas

Bridge rule:

- keep the logic that dense packages and multi-rail systems can push designs from `8-layer` toward `10-layer`
- downgrade pin-count, pitch, and plane-count numerics into non-numeric design-pressure wording
- delete cost uplift percentages

Allowed support:

- `methods-pcb-stackup-special-process-and-baseline-families`
- `methods-high-layer-rigid-board-manufacturability-context`

### 3. HDI via types and manufacturing process

Current structure:

- useful blind/buried-via distinction, but loaded with unsupported via-size, aspect-ratio, and laser-process numerics

Bridge rule:

- keep blind-via versus buried-via versus build-up workflow distinctions
- downgrade `1+N+1` style notation into architecture vocabulary
- exclude all exact via diameters, aspect ratios, and process-capability implications

Allowed support:

- `methods-hdi-microvia-and-vippo-process-posture`
- `methods-high-layer-rigid-board-manufacturability-context`

### 4. BGA escape routing strategy

Current structure:

- heavily numeric and recipe-driven by pitch bucket

Bridge rule:

- do not use the pitch-by-pitch numeric table logic in the usable pack
- retain only the high-level point that finer-pitch BGAs can push escape routing toward denser via strategies and more careful layer planning
- delete route-count, pitch-threshold, and microvia-default prescriptions

Allowed support:

- `methods-hdi-microvia-and-vippo-process-posture`

### 5. Stack-up design and layer assignment

Current structure:

- useful planning section, but current layer-by-layer table reads like a default recipe

Bridge rule:

- keep the idea that signal layers, reference planes, and power planes need explicit planning in a `10-layer` design
- convert the specific layer table into general stackup-planning guidance
- do not keep exact layer assignment as universal default

Allowed support:

- `methods-pcb-stackup-special-process-and-baseline-families`
- note: `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md` may be referenced in pack notes only

### 6. Sequential lamination and cost

Current structure:

- mixes a usable process description with unsupported cycle-count and cost-premium numerics

Bridge rule:

- keep sequential lamination as guarded process vocabulary
- delete cost premiums and cycle-count comparisons
- keep process sensitivity as manufacturability posture only

Allowed support:

- `methods-high-layer-rigid-board-manufacturability-context`
- `methods-hdi-microvia-and-vippo-process-posture`

### 7. Material selection across construction types

Current structure:

- strongest section for conservative bridge use
- still needs numeric pruning on unsupported buildup-layer defaults and board-level implications

Bridge rule:

- keep official material cards for mainstream high-Tg and low-loss examples
- keep exact product numerics only where a governed material fact already exists
- convert hybrid and build-up material guidance into cautious material-selection posture
- do not keep `RCC` thickness defaults or generic low-loss outcome claims

Preferred candidate facts:

- `materials-iteq-it-180a`
- `materials-shengyi-s1000-2`
- `materials-panasonic-megtron-4`
- `materials-panasonic-megtron-6`
- `materials-fr4-official-source-coverage`

### 8. High-frequency / RF applications

Current structure:

- blends material constants with derived board-geometry and RF stackup implications

Bridge rule:

- keep RF / high-speed hybrid stackup as a possible variant path
- retain only official material-positioning or datasheet-backed constants through existing fact cards
- exclude derived geometry implications and unsupported bondply/stack interpretation

Allowed support:

- material facts above
- note: RF/hybrid wiki or fact pages can be referenced in notes if needed, but not invented as missing fact IDs

### 9. Rigid-flex constructions

Current structure:

- valid as branch context, but current numeric configuration example is too specific

Bridge rule:

- keep rigid-flex as a scope-expansion variant only
- do not preserve exact `10R-4F` or tolerance claims in the usable pack
- use only posture language around bend-sensitive stackup and integration complexity

Allowed support:

- `methods-rigid-flex-stackup-and-bend-reliability-posture`

### 10. DFM rules

Current structure:

- heavily populated with unsupported feature-size, registration, annular-ring, and copper-balance numerics

Bridge rule:

- do not allow current DFM numeric tables into the usable pack
- convert the whole section into qualitative `review with fabricator`, `registration matters`, `annular-ring margin matters`, and `copper balance matters` wording if retained at all
- if exact rules are needed later, they must wait for governed H2 capability recovery, not this first-wave bridge

Allowed support:

- `methods-high-layer-count-backdrill-and-registration-posture`
- `methods-high-layer-rigid-board-manufacturability-context`

### 11. CTA and service banner

Current structure:

- dominated by unsupported capability, QA, compliance, and lead-time claims

Bridge rule:

- exclude current numeric service banner from the usable evidence pack
- future CTA copy, if any, must be rebuilt from allowed non-numeric posture only

Allowed support:

- `methods-pcb-prototype-quickturn-and-volume-routing` for guarded routing posture only
- `methods-advanced-validation-scope-segmentation`
- `methods-controlled-impedance-tdr-verification-posture`

## Refresh-Required Items

The following must not enter the pack unless refreshed under stronger policy:

- any prototype or production lead-time wording
- any explicit impedance tolerance or registration number
- any via-size or feature-size claim
- any `100% electrical test` or equivalent coverage percentage
- any `IPC Class 3` or compliance-style banner
- any volume / sustainment / NPI-to-production claim

## Open Gaps

- no governed `B` capability layer exists yet for `10-layer` feature-size, via-geometry, registration, or impedance numerics
- no governed `E` layer exists for reusable HDI / microvia / sequential-lamination numeric rules
- current internal pages still support process posture more strongly than numeric authority
- current blog structure is still over-indexed on tables and quote-style claims that do not survive first-wave bridge rules

## Stop Conditions

Reject the future `10-layer` evidence pack if any of the following remain true:

- unsupported `B` capability numerics remain in the pack
- unsupported `E` HDI / reliability numerics remain in the pack
- unsupported `F` cost or lead-time numerics remain in the pack
- any claim lacks a traceable stable `fact_id`
- any used `fact_id` lacks a registered supporting `source_id`
- internal posture pages are being used as if they were dated capability records
- current quote-banner language is being preserved rather than rebuilt conservatively

## Current Decision

`10-layer` belongs in the first `P4-06` bridge wave only as a conservative `query`-template prep target.

Usable bridge posture:

- material-property support may remain
- process and validation posture may remain
- architecture vocabulary may remain after downgrade

Blocked from the usable pack:

- unsupported capability numerics
- unsupported HDI / reliability numerics
- dynamic commercial numerics
- unsupported compliance or approval claims
