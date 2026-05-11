# P4-209B EMC Handbook Lane Log: Impedance / Via / Slot Routing Intake

- Date: `2026-05-06`
- Model: `gpt-5.4`
- Purpose and lane: claim-inventory intake for `85页 PCB设计EMC设计指导书` limited to transmission-line / impedance / via / split-plane / slot-routing / connector / backplane-adjacent routing content. This log records what the handbook pages appear to claim, what `llm_wiki` already supports, what can be safely reused, and what remains blocked pending stronger sources.
- Final status label: `completed_at_claim_family_level`

## Exact pages inspected

- Inspected handbook pages `32-69` inclusive from `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-85页-PCB设计EMC设计指导书/pages/`.
- Main clusters:
  - `32`: split reference planes, isolation gap placement, avoid routing important nets across split regions.
  - `33-46`: transmission-line basics, microstrip / stripline, reflection, crosstalk, characteristic impedance, odd/even/differential impedance vocabulary.
  - `47-53`: stackup / prepreg / core effects, differential-spacing effects, guard-trace effects, impedance-control examples.
  - `53-57`: via models, parasitics, layer changes, return-path continuity, via-count cautions.
  - `57-63`: slot creation, return-current behavior, split-plane crossing, bridging, connector-area slot risk, quiet-ground crossing.
  - `65-69`: backplane slot planning, topology families, connector pin-field concerns, impedance discontinuities near connectors/vias/corners, backplane power/ground partitioning.

## Existing `llm_wiki` support found

- `facts/methods/rf-transmission-line-structure-vocabulary-boundary.md`
  Supports guarded `microstrip` / `stripline` structure vocabulary only. Does not support handbook formulas, geometry tables, or performance comparisons.
- `facts/methods/controlled-impedance-tdr-verification-posture.md`
  Supports conservative wording that controlled impedance is paired with verification workflow such as `TDR` / coupon-style checks.
- `facts/methods/ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity.md`
  Supports avoiding splits or slots in reference planes, keeping return current continuous, and using nearby ground vias when layers change.
- `facts/methods/backdrill-control-capability.md`
  Supports backdrill / stub-control posture for high-speed and RF-adjacent transitions, but not numeric stub limits or universal need.
- `facts/methods/press-fit-and-backplane-integration-posture.md`
  Supports connector-zone / press-fit / drilling / backdrill / validation as one integrated backplane workflow.
- `wiki/processes/backplane-execution-and-connector-integration.md`
  Supports connector-heavy backplane framing and blocks exact hole windows, residual-stub numbers, insertion-force claims, and universal architectures.
- `wiki/consumption/redundant-psu-backplane-impedance-control-evidence-pack.md`
  Supports conservative article framing around stackup intent, connector-zone review, reference continuity, layered validation, and blocked numerics.

## Claim families found in the handbook

- Transmission-line family:
  microstrip, stripline, embedded microstrip, delay, characteristic impedance, capacitance/inductance, reflection, overshoot, ringing, crosstalk.
- Impedance vocabulary family:
  input impedance vs characteristic impedance, reflection coefficient, traveling-wave framing, odd-mode, even-mode, differential impedance, matching language.
- Differential-coupling family:
  spacing effects, coupling to reference plane vs coupling to neighbor trace, common-mode suppression claims, guard-trace effects.
- Via-effects family:
  via capacitance/inductance models, impedance discontinuity, return-path change on layer transition, “same-reference-plane” vs changed-reference-plane cases, reduce via count.
- Split-plane / slot family:
  slots caused by plane partitioning or dense through-hole clearances, high-speed return current concentration, crossing-slot risks, bridging, quiet-ground crossing, keep external connectors off plane gaps.
- Connector / backplane-adjacent routing family:
  connector pin assignment / shielding suggestions, dense connector-via regions as return-path discontinuities, topology families, keep connector-to-device routes short, adjacent-layer orientation, backplane power/ground partitioning.

## Safe reuse classes

- `Vocabulary-only reuse`
  Safe to reuse `microstrip`, `stripline`, `characteristic impedance`, `differential pair`, `reference plane`, `return path`, `plane split`, `slot`, `backdrill`, `press-fit/backplane connector zone` as guarded engineering vocabulary.
- `Execution-posture reuse`
  Safe to reuse that controlled-impedance work depends on stackup definition plus verification workflow; layer transitions need return-path continuity; signals should avoid crossing plane splits or slots; connector-heavy backplane work is an integrated drilling/connector/validation problem.
- `Boundary framing reuse`
  Safe to reuse that handbook formulas and case studies are not authority; any exact geometry, tolerance, validation coverage, or acceptance claim must be refreshed against official or current internal sources.
- `Article-spine reuse`
  Safe to reuse topic structure for future evidence-pack or wiki expansion: transmission-line vocabulary, reference continuity, via-transition control, split-plane routing risks, connector-zone planning, layered validation.

## Blocked claim classes

- `Handbook numeric formulas and thresholds`
  Block handbook-origin numeric rules such as `1/20 wavelength`, `1/6 rise-time`, delay values, impedance formulas, `20 dB` radiation deltas, `0.7 V` overshoot threshold, `40-75 ohm` generalization, `33 ohm` matching default, graph-derived odd/diff impedance numbers, `1 pF` via approximation, `6-7 ohm` TDR drop, `0.055` reflection coefficient, `2000 mil` connector-route limit, interface-speed cutoffs, `20H` uplift claims, and similar values.
- `Universal performance or acceptance claims`
  Block statements that differential routing inherently suppresses common-mode noise in all cases, guard traces always improve EMC, one via is negligible, inner layers are always better, or any routing choice guarantees EMI/ESD pass results.
- `Vendor / case-study / recommendation transfer`
  Block transfer of `Pulse`, `Intel`, `Lucent`, internal PON/DMU examples, or anecdotal `6000V` results into reusable fact language without current source recovery.
- `Connector-family and shielding specifics`
  Block 2mmHM/HS3 product-family recommendations, exact pin-field arrangements, shielding effectiveness, longer-ground-pin implications, and connector-specific EMC claims unless backed by connector-vendor documentation.
- `Backplane topology and interface capability claims`
  Block GTL+/LVDS/ECL/CML speed thresholds, topology prescriptions, and channel-success claims unless backed by current official app notes or vendor data.
- `Capability / certification / acceptance claims`
  Do not convert handbook content into fabrication capability, compliance, qualification, or “passes EMC” statements.

## Image / table pages that merit later selective vision pass

- `34-35`: transmission-line formula pages with equations and diagrams.
- `37`: crosstalk factors plus the “different conditions” table.
- `40-42`: microstrip vs stripline comparison and layer-priority examples.
- `48-52`: differential-spacing and guard-trace effect curves.
- `54`: via mathematical-model figure and formula layout.
- `57-62`: slot-creation, return-current, bridging, connector-placement, and quiet-ground diagrams.
- `66-69`: backplane topology sketches, connector model / pin-field figures, and backplane partitioning figures.

## Official-source gaps

- Need stronger official/public sources for `microstrip` / `stripline` formulas, geometry implications, and comparison language beyond current vocabulary-only support.
- Need an official source lane for odd-mode / even-mode / differential-impedance relationships if reusable formula-level writing is desired.
- Need official/public via-transition guidance for parasitic models, return-path handling, and same-reference-plane vs changed-reference-plane cases.
- Need official/public support for slot crossing, bridging, quiet-ground crossing, and connector-over-gap handling beyond the current general return-path boundary card.
- Need connector-vendor sources for `2mm hard-metric / 2mmHM / HS3` style pin-field, shielding, longer-ground-pin, and high-density connector guidance.
- Need current official sources for backplane topology families and interface-speed framing before any GTL+/LVDS/ECL/CML speed-positioning claims can be reused.
- Need current authority if anyone wants to reuse `20H` or `3W` as prescriptive rules instead of cautious historical heuristics.

## Lane conclusion

- The page span is useful as a claim-inventory map for impedance, via, return-path, slot-crossing, and connector-adjacent routing topics.
- `llm_wiki` already has partial support for vocabulary, return-path continuity, impedance-verification posture, and backplane connector integration posture.
- The main missing layer is official-source recovery for formula-level transmission-line content, via-transition specifics, slot-bridge specifics, and connector-vendor guidance.
- No reusable facts were added outside this lane log. This lane should be treated as intake completed at claim-family level, not authority-level learning.
