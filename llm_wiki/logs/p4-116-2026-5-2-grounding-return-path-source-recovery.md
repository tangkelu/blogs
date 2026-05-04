# P4-116 2026-05-02 Grounding / Return-Path Source Recovery

Date: 2026-05-02

Status: `source_backed_fact_layer_partial`

## Purpose

Determine whether current official authority exists for a reusable grounding-and-return-path execution boundary, and only land lane-local grounding artifacts if the source layer supports a narrow reusable statement.

## Search Result

Current official authority does exist, but it is narrower than the original lane label.

Recovered current official sources:

- `analog-devices-mixed-signal-pcb-layout-guidelines`
- `ti-high-speed-layout-guidelines`

## What The Current Authority Safely Supports

- board-layer planning determines allowable return-current paths before routing
- a ground plane can be described as the low-impedance return reference for signals
- partitioning functional regions before routing is safer than treating grounding as a generic afterthought
- routing across splits or slots in the reference plane disrupts return-current continuity and enlarges loop area
- signal layer changes may need nearby ground-via support so the return current can stay close to the signal path

## Landed Lane-Local Outputs

- `sources/registry/methods/analog-devices-mixed-signal-pcb-layout-guidelines.md`
- `sources/registry/methods/ti-high-speed-layout-guidelines.md`
- `facts/methods/ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity.md`

## Exact Blocker Status

`partial_hold_remaining`: no current official authority was recovered for a reusable telecom-specific `shield contact strategy`, `partition-boundary grounding outcome`, or `field / EMC / RF result` claim. The lane only supports a narrow reference-plane / routing-continuity execution boundary.

## Disposition

- lane outcome: `source_backed_fact_layer_partial`
- lane shape: `fact_partial`
- safe next move: reuse the new fact card only for qualitative grounding and return-path execution language
- do not expand this lane into telecom performance, shielding outcome, compliance, or universal design-rule claims without new current authority
