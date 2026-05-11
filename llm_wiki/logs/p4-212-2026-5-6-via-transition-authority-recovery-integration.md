# P4-212 Via Transition Authority Recovery Integration

Date: 2026-05-06

## Purpose

Integrate the stronger source recovery for the `via-transition / return-path continuity` part of the `P4-210C` EMC residual lane.

This pass is intentionally narrow. It promotes via-transition boundary language only and leaves `slot bridging` / `quiet ground` as still-blocked until a stronger source lane is available.

## Inputs

- `logs/p4-210c-2026-5-6-emc-source-lane-transmission-line-via-return-slot.md`
- `sources/registry/methods/ti-high-speed-layout-guidelines.md`
- `sources/registry/methods/analog-devices-mixed-signal-pcb-layout-guidelines.md`
- `sources/registry/methods/nxp-an11397-ptn3363-pcb-layout-guidelines.md`

## What Landed

### Via-transition boundary

Landed as reusable local knowledge:

- `sources/registry/methods/nxp-an11397-ptn3363-pcb-layout-guidelines.md`
- `facts/methods/via-transition-return-path-continuity-boundary.md`

Reason:

- the source mix is strong enough to support `via-transition`, `parasitic`, `stub`, and `nearby ground vias` vocabulary
- the source mix is not strong enough for universal geometry tables or bridge-style routing rules

## What Remains Reused Only

### Slot-crossing / quiet-ground boundary

No new fact card was created for this subtopic.

Continue to reuse:

- `facts/methods/ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity.md`
- `facts/methods/rf-transmission-line-structure-vocabulary-boundary.md`
- `facts/methods/pcb-impedance-and-rf-measurement-method-boundary.md`

Reason:

- the current source mix supports split/slot avoidance and return-path continuity
- it does not yet support a distinct slot-bridging or quiet-ground execution recipe as a reusable fact

## Next Recommended Moves

1. Only open a new `slot bridging` lane if a stronger primary source appears.
2. Keep `quiet ground` as a routing-language detail inside the existing return-path boundary for now.
3. Do not promote handbook numerics or connector-field recipes without stronger authority.

## Final Status

- `via-transition / return-path`: `source_backed_fact_layer_partial`
- `slot-crossing / quiet-ground`: `existing_fact_layer_reused_only`
