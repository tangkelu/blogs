# P4-222 EMC Owner-Curve Recovery Controller Integration

Date: 2026-05-07
Parent queue: `p4-220a`
Execution mode: `owner_backed_exact_curve_recovery`

## Purpose

Integrate the first post-`P4-221` `EMC` owner-curve recovery pass.

This pass tests the two highest-value lanes from `P4-220A`:

- ferrite-bead exact-part or exact-family recovery
- common-mode-choke owner-backed `common-mode` and `differential-mode` curve recovery

## Inputs Used

- `logs/p4-220a-2026-5-7-emc-authority-recovery-queue-and-source-priority.md`
- `logs/p4-221-2026-5-7-pcb-pdf-post-p4-220-controller-integration-and-next-resume-entry.md`
- `facts/methods/ferrite-bead-vendor-guidance-boundary.md`
- `facts/methods/common-mode-choke-vs-ferrite-bead-vendor-boundary.md`
- owner-backed source scouting results for Murata and Coilcraft

## What Landed

### Common-mode choke owner-backed family curve recovery

Landed as reusable local source support:

- `sources/registry/methods/coilcraft-lpd3015-common-mode-chokes-datasheet.md`

Reason:

- the official Coilcraft `LPD3015 Series` datasheet is a named owner-backed family source
- it includes both `common-mode` and `differential-mode` traces on the same source path
- it also exposes directly published family and part-level context such as `inductance`, `DCR max`, `Irms`, isolation, and measurement conditions

Promotion posture:

- family-scoped and part-scoped only
- no universal claims beyond the published family

### Ferrite-bead owner-backed exact-part recovery

Did not land as exact-part recovery.

What was established safely:

- Murata current-public owner endpoints did not return a clean owner-backed match for the historical handbook label `BLA3216A102SG4`
- Murata current-public owner material does support a clearly labeled family-equivalent fallback candidate:
  - `BLA31AG102SN4#`
- no owner-backed alias or cross-reference was recovered that proves `BLA3216A102SG4` and `BLA31AG102SN4#` are the same exact part

Landed as a controlled fallback source only:

- `sources/registry/methods/murata-bla31ag102sn4-family-equivalent-ferrite-bead-specification.md`

Promotion posture:

- `exact_part_unresolved`
- `family_equivalent_fallback_only`

## Minimal Fact-Layer Effect

This pass justifies only minimal `fact` deltas:

- add the Coilcraft family datasheet as an owner-backed common-mode choke curve source
- clarify in the ferrite-bead boundary that exact-part recovery for `BLA3216A102SG4` remains blocked, while a family-equivalent Murata fallback now exists

This pass does not justify:

- a new broad `EMC` rule card
- universal common-mode choke attenuation claims
- exact-part ferrite-bead curve claims for `BLA3216A102SG4`

## Claims That Must Stay Blocked

- handbook ferrite-bead curve by itself as promotable exact data
- handbook common-mode-choke curve by itself as promotable exact data
- ferrite beads as broadly better high-frequency filters than ordinary inductors
- generalized low-`Q` ferrite explanation as reusable rule text
- common-mode choke claims that differential current passes without attenuation as a universal statement
- low-pass topology selection recipes by source/load impedance
- interface-specific suitability, compliance outcomes, EMI pass claims, and layout-placement rules not explicitly published by the owner source
- any cross-vendor generalization from a single owner family
- all previously blocked `A3` cookbook-routing and formula claims

## Result Status

- ferrite-bead exact-part lane:
  - `exact_part_recovery_not_reached`
  - `family_equivalent_fallback_recovered`
- common-mode-choke curve lane:
  - `owner_backed_family_curve_recovered`

## Next Step

1. Keep `BLA3216A102SG4` exact-part recovery open only if a later Murata alias or archived owner cross-reference is recoverable.
2. Use the new Coilcraft family source for minimal owner-backed common-mode choke curve deltas.
3. Do not reopen handbook-only curve interpretation now that an owner-backed common-mode choke family source has landed.
