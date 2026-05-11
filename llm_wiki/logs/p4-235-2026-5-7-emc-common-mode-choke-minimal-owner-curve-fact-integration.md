# P4-235 EMC Common-Mode Choke Minimal Owner-Curve Fact Integration

Date: 2026-05-07
Parent state: `after P4-222 and P4-223`
Execution mode: `minimal_owner_backed_exact_data_landing`

## Purpose

Land the smallest justified exact-data artifact now that:

- ferrite-bead exact-part recovery is intentionally blocked at `P4-223`
- `Coilcraft LPD3015 Series` already provides owner-backed common-mode choke family curves and part-row table data

## Inputs Used

- `logs/p4-222-2026-5-7-emc-owner-curve-recovery-controller-integration.md`
- `logs/p4-223-2026-5-7-ferrite-bead-exact-part-recovery-blocked-at-family-equivalent-ceiling.md`
- `sources/registry/methods/coilcraft-lpd3015-common-mode-chokes-datasheet.md`
- `facts/methods/common-mode-choke-vs-ferrite-bead-vendor-boundary.md`

## Integration Decision

This turn should land a new fact card.

Reason:

- the existing `common-mode-choke-vs-ferrite-bead-vendor-boundary` card is still the right boundary card for family distinction and conservative vendor-scoped wording
- the Coilcraft source now supports a narrower family-scoped and part-row-scoped exact-data layer that should not be mixed into the broader boundary card

## What Landed

- `facts/methods/coilcraft-lpd3015-common-mode-choke-family-exact-data.md`

This new card allows:

- family identity for the named `LPD3015 Series`
- published part-row and family table fields
- published measurement and condition notes
- owner-backed existence of both `common-mode` and `differential-mode` curves on the same source path

## What Did Not Reopen

- `BLA3216A102SG4` ferrite-bead exact-part recovery
- handbook-only ferrite-bead or common-mode-choke curve promotion
- universal attenuation wording such as `differential current passes without attenuation`
- broad `EMC` cookbook rules
- low-pass topology-selection interpretation

## Result Status

- common-mode choke lane:
  - `owner_backed_family_curve_recovered`
  - `minimal_exact_data_fact_landed`
- ferrite-bead lane:
  - `exact_part_unresolved`
  - `family_equivalent_fallback_only`

## Next Step

1. Reuse the new `LPD3015` fact card only when a prompt specifically needs family-scoped or part-row-scoped owner-backed exact data.
2. Keep broad common-mode choke recommendations blocked unless stronger multi-owner or standards-adjacent support is intentionally recovered.
3. Keep ferrite-bead exact-part work closed unless exact new Murata evidence appears.
