# P4-19 Material Parameter Scope Supplement

Date: 2026-04-27

## Purpose

Continue the empty-image data-first program by adding real material parameter cards with explicit scope control.

This round answers the user correction that the wiki should not only add boundaries. It should also preserve usable real values when the source is strong enough, while preventing those values from becoming generic capability, performance, or qualification claims.

## Files Added

- `facts/materials/parameter-scope-rogers-rf-laminate-values.md`
- `facts/materials/parameter-scope-isola-high-speed-laminate-values.md`
- `facts/materials/parameter-scope-panasonic-megtron-values.md`

## Parameter Coverage Added

### Rogers RF Laminate Values

Adds exact-product values for:

- `RO4003C`
- `RO4350B`
- `RT/duroid 5880`

Coverage includes Dk, Df, selected thermal / moisture / CTE values, and the product-specific scope needed to use those values safely.

### Isola High-Speed Laminate Values

Adds datasheet-scoped values for:

- `I-Speed`
- `Tachyon 100G`
- `Astra MT77`

Coverage includes Tg, Td, Dk, Df, CTE, thermal conductivity, moisture absorption, and frequency/method context where already captured in existing material fact cards.

### Panasonic MEGTRON Values

Adds grade-scoped values for:

- `MEGTRON 6 R-5775(N) / R-5670(N)`
- `MEGTRON 7 R-5785(N) / R-5680(N)`

Coverage includes Tg, Td, T288, Dk, Df, water absorption, thermal conductivity, and grade-level scope.

## Scope Discipline

All material values in this round are usable only as:

- exact-product or exact-grade material parameters
- source-backed laminate context
- input to material-selection and stackup-review discussion

They are not:

- HIL or APT factory capability
- finished-board RF, SI, optical, thermal, or reliability proof
- insertion-loss, return-loss, BER, eye-mask, jitter, antenna, EIRP, or chamber-test evidence
- procurement approval
- supplier qualification
- lead-time, cost, or yield evidence

## Empty-Image Impact

This improves parameter support for:

- `mmwave-5g-5g-telecom`
- `antenna-system-5g-telecom`
- `5g-base-station-5g-telecom`
- `turnkey-a-5g-6g-communication`
- `high-speed-ai-server-motherboard-ai-server-backplane`
- `dfm-dft-dfa-review-data-center-optical-module`
- `low-void-bga-reflow-data-center-optical-module`
- `first-article-inspection-fai-high-speed-si`
- adjacent high-speed, RF, AI-server, optical-module, and telecom empty-image rewrites

This does not make those topics automatically ready for performance-heavy drafts. It only gives prompts real material values that can be cited within a bounded engineering context.

## Verification Notes

- Values were reused from existing verified material fact cards and already registered source records.
- No new source registry records were added.
- Source IDs should be checked with scoped validation after controller integration.
