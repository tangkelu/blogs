# P4-255 P4-06 Batch 1 Topic-To-Prompt Mapping

Date: 2026-05-07
Parent state: `after P4-121`
Scope: `P4-06 Phase 5 Batch 1`

## Purpose

Convert the first-wave `6-layer / 8-layer / 10-layer` evidence packs into a direct prompt-consumption handoff so later AI workers can draft articles without redoing the same bridge audit.

This note does not reopen source recovery.
It only maps already-governed pack content into `prompts_template/shared/query.md` + `prompts_template/hilpcb/query-overlay.md`.

## Operating Rule

- consume only `verified` and `framing_only`
- keep `must_refresh` and `supplier_scoped_dated_only` out of article body generation
- never upgrade unsupported numerics, supplier proof, standards thresholds, or commercial claims
- keep one article per pack; do not merge the three first-wave packs into one blended output

## Batch 1 Prompt Routes

### `6-layer`

Use:

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

Write as:

- baseline FR-4 family framing
- exact-product material examples
- stackup and planning posture
- controlled-impedance / validation posture
- RF, thermal, and rigid-flex as bounded branches

Do not write:

- capability numbers
- impedance geometry tables
- via-rule numerics
- cost / lead-time claims
- standards thresholds

### `8-layer`

Use:

- `materials-fr4-official-source-coverage`
- `materials-non-isola-fr4-to-very-low-loss-coverage`
- `materials-panasonic-megtron-4-low-loss-product-coverage`
- `methods-controlled-impedance-tdr-verification-posture`
- `methods-high-layer-count-backdrill-and-registration-posture`
- `methods-spread-glass-and-controlled-impedance-planning`
- `methods-hybrid-rf-stackup-capability`
- `methods-rigid-flex-stackup-and-bend-reliability-posture`

Write as:

- multilayer planning logic
- material-family selection
- conservative impedance / validation posture
- hybrid RF and rigid-flex as branch paths

Do not write:

- standards thresholds
- rigid-flex mechanical numerics
- HDI / via tables
- cost claims
- service claims

### `10-layer`

Use:

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

Write as:

- dense multilayer architecture framing
- material-selection ladder
- high-layer manufacturability posture
- staged validation scope
- HDI and backdrill as guarded workflow context

Do not write:

- BGA escape recipes
- drill / registration capability numbers
- timing or budget tables
- public quality banners
- prototype / production promise numerics

## Prompt Consumption Notes

- `query` template only for this batch
- use the HILPCB overlay requirement for the inline quote component
- keep the first early fact table narrow and source-backed
- place the quote component in the middle or lower half of the article, not only at the top
- use `DATA_GAP` internally only when the article structure would otherwise need unsupported numerics

## Handoff Result

- The first-wave packs are now direct prompt inputs.
- No further bridge audit is needed before drafting `6-layer`, `8-layer`, or `10-layer` conservative articles.
- Later AI should resume from this mapping note rather than re-reading the same bridge-prep files first.
