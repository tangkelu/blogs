# P4-364 E3 Intel NSMD/SMD Vendor Terminology Boundary

Date: 2026-05-09
Parent lane: `P4-311` and `P4-363`
Execution mode: `narrow_vendor_scoped_terminology_recovery`

## Purpose

Advance the `E3` solder-mask and pad-definition subfamily one step further without overstating the current source layer.

This pass does not close the missing IPC definition gap.
It lands only one narrower vendor-scoped terminology boundary showing that `NSMD` and `SMD` are real owner-guidance land-pad distinction terms in Intel `AN 114`.

## Inputs

- existing `E3` controller and recovery logs:
  - `logs/p4-311-2026-5-8-pcb-article-e3-usage-route-integration.md`
  - `logs/p4-363-2026-5-9-e3-ipc-solder-mask-terminology-boundary-recovery.md`
- existing owner-source support already in repo:
  - `sources/registry/methods/intel-an114-bga-land-pad-dimensions.md`
  - `facts/methods/intel-bga-land-pad-guidelines-common-pitches-and-vbga.md`
- contrast sources checked but not chosen as primary terminology anchor:
  - `sources/registry/methods/ti-an1126-bga-pad-geometry-guidelines.md`
- gap-control boundary preserved:
  - `facts/methods/ipc-solder-mask-layer-and-pad-definition-boundary.md`

## What Landed

### New boundary fact card

- `facts/methods/intel-nsmd-smd-land-pad-terminology-boundary.md`

### Resume-surface integration

Updated:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`

## What Landed Safely

- one owner-scoped official terminology boundary that `NSMD` and `SMD` are real BGA land-pad distinction terms in Intel guidance
- one narrow reusable wording layer that, in Intel `AN 114`, `SMD` pads match BGA pad size and `NSMD` pads are about `15%` smaller
- one tighter reuse posture for later `E3` writing:
  - `NSMD/SMD` can now be named through a concrete official owner source
  - but only as vendor-scoped package-guideline vocabulary

## What Did Not Land

- no exact public IPC definition for `NSMD`, `SMD`, `mask-defined`, `non-solder-mask-defined`, `via tenting`, or `solder mask bridge`
- no universal cross-vendor equivalence rule
- no pad-type preference rule
- no solder-mask opening, bridge, or via-treatment numerics
- no reliability, yield, manufacturability, or process-capability outcome claim

## Final Status

- lane result:
  - `narrow_vendor_scoped_terminology_boundary_landed`
- continuation state:
  - `intel_now_provides_reusable_nsmd_smd_owner_vocabulary_boundary`
  - `ipc_level_definition_gap_remains_explicit`
