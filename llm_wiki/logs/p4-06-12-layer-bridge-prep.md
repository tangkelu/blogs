# P4-06 12-Layer Bridge Prep

Date: 2026-04-26

## Purpose

This control note prepares the current `12-layer` layer-count blog for second-wave `P4-06` evidence-pack use.

It does not:

- rewrite the blog
- unlock high-numeric-density reuse
- approve unsupported `B / C / D / E / F / G` numerics

Its purpose is to define the safest bridge posture for future prompt execution against:

- `/code/hileap/frontendHIL/docs/hilpcb_blog_04.24/en/12-layer-pcb-manufacturing.md`

## Template Choice

Default template choice:

- `prompts_template/shared/query.md`

Required supporting templates:

- `prompts_template/shared/evidence-pack-template.md`
- `prompts_template/hilpcb/query-overlay.md`

Reason:

- `12-layer` sits at the front of the second safe bridge wave under `logs/p4-06-first-wave-bridge-queue.md`
- the page is still best treated as a direct engineering/manufacturing query page, not a pillar page
- the current draft needs heavier section-level pruning than the first-wave pages because unsupported `B` and `D` numerics are denser

## Scope

In scope for this prep note:

- the current blog at `/code/hileap/frontendHIL/docs/hilpcb_blog_04.24/en/12-layer-pcb-manufacturing.md`
- second-wave conservative bridge preparation only
- section-level keep / downgrade / exclude rules for future evidence-pack assembly
- safe fact / source candidates already present in `llm_wiki`

Out of scope:

- fabrication-capability recovery
- board-level SI / timing / skew numeric recovery
- standards-threshold restoration
- prototype / production timing restoration
- readiness upgrade beyond conservative prompt bridging

## Conservative Readiness Verdict

`12-layer` is suitable for `second-wave conservative bridge-prep` with heavier pruning than `6 / 8 / 10-layer`.

It is not suitable for high-numeric-density evidence-pack use.

Current posture:

- bridge-prep verdict: `allowed with heavy pruning`
- readiness verdict: remains `mostly_ready` for conservative rewriting only
- primary blocker classes: `B` fabrication-capability numerics and `D` high-speed / interconnect numerics

## Allowed Claim Classes

Allowed in the usable evidence pack:

- `A` material datasheet numerics when tied to exact official product/family sources
- non-numeric high-layer stackup / signal-integrity planning posture
- non-numeric controlled-impedance and validation workflow posture
- ecosystem interface context when clearly framed as demand-side design pressure rather than board-performance proof
- non-numeric HDI / rigid-flex branch vocabulary when clearly separated from capability tables

Allowed only as downgraded wording, not as retained numerics:

- `DDR4 / DDR5`, `PCIe`, `10G`, `USB4`, `HDMI`, and `DisplayPort` as system-context examples only
- `1+10+1`, `12R-4F`, and related architecture patterns only as non-default examples
- power-plane and signal-layer pressure as design-context wording, not as stackup defaults

## Excluded Claim Classes

Do not allow these into the usable pack:

- `B` fabrication capability numerics such as backdrill depth, impedance tolerance, stack-thickness windows, drill-program counts, hole-size counts, copper-balance thresholds, and board-thickness tolerance claims
- `C` standards / qualification / acceptance numerics such as `IPC-A-600 Class 3`, `100%` testing as an assurance banner, or delivery/quality claims disguised as quality proof
- `D` board-level SI / timing / geometry numerics such as skew budgets, timing budgets, impedance width tables, width/spacing defaults, training-margin numbers, or `3GHz` / `5Gbps` style thresholds used as backdrill rules
- `E` HDI / rigid-flex / build-up numerics such as BGA escape defaults, default pitch breakpoints, or representative constructions presented as universal recipes
- `F` dynamic commercial numerics such as prototype days, production days, or cost-saving percentages
- `G` unsupported contextual numerics that act as hidden capability proof

Specific exclusions from the current blog:

- `±8mil`
- `±8%`
- `5ps`
- `20GHz`
- `2.0mm+`
- `3GHz`
- `±5mil`, `±25mil`, `±10mil`
- `80Ω`, `40Ω/80Ω`
- `±1 UI`, `±150ps`, `±0.5mil`, `2-inch`
- `40-50%`
- `3-5` drill programs, `≤4` hole sizes
- `±15%`, `50mil`, `≤10:1`, `0.2mm`
- `5-day` and `15-day`

## Must-Refresh Handling

Future prompt execution must mark `must_refresh: true` for any item that depends on:

- prototype or production timing
- any internal capability / tolerance banner
- live service positioning
- revision-sensitive compliance or acceptance posture

Default bridge rule:

- if a claim would require refresh and does not already have a governed `fact_id` plus stable `source_id`, exclude it from the usable pack

## Candidate `fact_id` Set

Primary candidate facts for a conservative pack:

- `materials-high-speed-digital-material-ladder-normalization`
- `materials-fr4-official-source-coverage`
- `materials-panasonic-megtron-4`
- `materials-panasonic-megtron-6`
- `materials-isola-i-tera-mt40`
- `materials-isola-astra-mt77`
- `methods-high-speed-interface-system-context`
- `methods-controlled-impedance-tdr-verification-posture`
- `methods-advanced-validation-scope-segmentation`
- `methods-high-layer-rigid-board-manufacturability-context`
- `methods-high-layer-count-backdrill-and-registration-posture`
- `methods-spread-glass-and-controlled-impedance-planning`
- `methods-hdi-microvia-and-vippo-process-posture`
- `methods-rigid-flex-stackup-and-bend-reliability-posture`

Usable as wiki/topic notes, not atomic facts:

- `processes-advanced-pcb-fabrication-and-stackup-planning`
- `testing-validation-ladder-from-e-test-to-si-verification`
- `materials-high-speed-material-family-selection`

## Candidate `source_id` Set

Primary candidate source IDs for the conservative pack:

- `panasonic-megtron-4-r5725-r5620`
- `panasonic-megtron-4-datasheet`
- `panasonic-megtron-6-model-r5775n`
- `panasonic-megtron-6-datasheet`
- `isola-i-tera-mt40-datasheet`
- `isola-astra-mt77-datasheet`
- `isola-astra-mt77-dk-df-table`
- `jedec-ddr5-standard-business-wire-2020`
- `jedec-ddr5-standard-business-wire-2021`
- `jedec-ddr5-standard-business-wire-2024`
- `micron-ddr5-sdram-page`
- `pcisig-pcie-4-faq`
- `pcisig-pcie-5-faq`
- `pcisig-pcie-6-faq`
- `frontendapt-pcb-high-speed-pcb-page-en`
- `frontendhil-high-speed-product-page-en`
- `frontendapt-pcb-pcb-impedance-control-page-en`
- `frontendapt-pcb-multilayer-pcb-page-en`
- `frontendhil-multilayer-pcb-product-page-en`
- `frontendapt-pcb-hdi-pcb-page-en`
- `frontendhil-hdi-pcb-product-page-en`
- `frontendapt-pcb-pcb-stack-up-page-en`
- `frontendapt-pcb-multi-layer-laminated-structure-page-en`
- `frontendapt-pcb-rigid-flex-pcb-page-en`
- `frontendhil-rigid-flex-pcb-product-page-en`

## Section-By-Section Bridge Guidance

### 1. Intro, title, and capability banner

Allow:

- `12-layer` as the point where routing density, plane allocation, and validation complexity increase
- architecture-pressure framing around dense digital systems

Exclude:

- `±8mil`, `±8%`, `5ps`, `20GHz`
- `100% electrical testing` when used as a reusable assurance banner
- prototype / production delivery claims

### 2. Why designs move to 12 layers

Allow:

- the qualitative point that denser packages, more rails, and cleaner reference-plane management can push designs beyond lower-layer boards
- system-context references as background only

Exclude:

- any preserved `MT/s`, lane-speed, or interface-rate number presented as board-proof
- cost or schedule deltas

### 3. Backdrill, routing density, and signal-integrity pressure

Allow:

- backdrill as a possible high-speed planning control
- the idea that stub management, plane continuity, and return-path planning matter more as density rises

Exclude:

- `2.0mm+`
- `3GHz`
- `backdrill above 5Gbps`
- any depth-control or residual-stub numeric

### 4. Stackup architecture and planning

Allow:

- general stackup framing around signal layers, planes, and symmetry
- non-numeric signal-layer / power-plane planning posture

Exclude:

- `6 signal layers`, `3-4 power planes`
- `1.6-2.4mm`, `2.0mm`
- any representative stackup recipe treated as a default manufacturing table

### 5. DDR and high-speed sections

Allow:

- DDR / PCIe / high-speed buses as ecosystem context
- controlled-impedance and validation-ladder posture

Exclude:

- width/spacing tables
- skew / delay / timing / training-budget numerics
- `80Ω`, `40Ω/80Ω`, and similar reused target tables when presented as universal board outputs

### 6. Material sections

Allow:

- official material-family and exact-product comparison using current supported digital-material cards
- conservative low-loss / very-low-loss framing

Exclude:

- generic material-speed ladders unless each numeric row maps cleanly to official product-grade support
- cost-saving percentages from hybrid-material selection

### 7. HDI / rigid-flex variants

Allow:

- `1+10+1` and `12R-4F` only as architecture examples
- the statement that HDI and rigid-flex change the process route

Exclude:

- `0.5mm` pitch presented as a reusable threshold
- any representative construction count presented as a default or capability proof

### 8. Fabrication, testing, and closing sections

Allow:

- verification workflow posture
- the idea that more complex builds need tighter planning and review

Exclude:

- drill-program counts
- hole-size counts
- `20GHz` VNA or `>10Gbps` test numerics
- `100%` testing, `5-day`, `15-day`, or similar closing banners

## Open Gaps That Stay Controlled

- `B` capability numerics around backdrill, board thickness, drill-program complexity, and tolerance handling remain `needs_source`
- `D` SI and timing numerics remain excluded rather than downgraded into pseudo-evidence
- `C` quality and acceptance phrasing must not be reconstructed from internal verification language
- `F` delivery and commercial timing claims remain excluded

## Stop Conditions

Do not assemble a future `12-layer` evidence pack if any of the following remain true:

- interface-rate numerics are being used as proof of board-level SI performance
- backdrill thresholds or depth windows are still present
- stackup recipe numbers are still presented as reusable defaults
- verification presence is being converted into numeric capability or acceptance proof
- prototype / production timing numerics remain in the usable pack

## Current Decision

`12-layer` may enter second-wave `P4-06` evidence-pack assembly only under:

- heavy pruning of `B` and `D` numerics
- strict separation between ecosystem context and board guarantees
- strict separation between verification posture and capability / acceptance proof
