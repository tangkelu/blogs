# P4-523 Fresh Package-House Follow-Up SPIL And PTI No Reopen

Date: 2026-05-11
Parent surfaces:

- `logs/p4-522-2026-5-11-fresh-package-house-followup-utac-and-chipmos-no-reopen.md`
- `logs/p4-521-2026-5-11-fresh-osat-package-house-1p50mm-scout-no-reopen.md`
- `logs/p4-519-2026-5-11-post-p4-518-residual-priority-and-candidate-pool-tightening-rerank.md`
- `logs/backlog.md`
- `logs/phase-status.md`

Execution mode: `controller_owned_fresh_official_source_followup`

## Purpose

Follow up the fresh non-chip-vendor package-house lane with one more bounded pass on two additional candidate classes:

- one current-public package-house family-listing surface
- one current-public package-house BGA capability surface

## Candidate Gate

Reopen only if one current-public owner surface visibly provides both:

1. true `1.50 mm` pitch identity
2. same-surface printed PCB land-pattern or footprint geometry

## Candidate Classes Checked

### SPIL

- current-public official package-family surface:
  - `PBGA`
  - `EDHS-PBGA`
  - `TFBGA / VFBGA`
  - `LGA`
  - `FCBGA`
  - `FCCSP`
  - `WLCSP`

### PTI

- current-public official `Wire Bond BGA` capability surface with visible pitch range

## Findings

### 1. SPIL is a real current-public package-house surface, but it stays below the `1.50 mm` gate

- the surfaced official SPIL page is a real package-house family-listing surface
- it usefully confirms that SPIL publicly exposes package families including:
  - `PBGA`
  - `EDHS-PBGA`
  - `TFBGA / VFBGA`
  - `LGA`
  - `FCBGA`
  - `FCCSP`
  - `WLCSP`
- however the visible current-public content does not expose:
  - one true `1.50 mm` pitch identity
  - one same-surface PCB footprint or land-pattern geometry row
- SPIL therefore stays below reopen for the current package exact-geometry residual

### 2. PTI is a real current-public package-house surface, but the visible pitch range stays below target

- the surfaced official PTI `Wire Bond BGA` page is a real package-house capability surface
- its visible pitch wording states:
  - `0.3 to 1.0mm ball pitch available`
- this is useful because it is stronger than search-noise or speculative vendor-name expansion
- however it still stays below the current `1.50 mm` gate because:
  - the visible pitch range does not reach true `1.50 mm`
  - the page also does not expose one same-surface PCB footprint or land-pattern geometry row
- PTI therefore stays below reopen as a below-target-pitch owner surface

## Gate Result

- SPIL stayed below reopen because the retrievable official family-listing surface exposes package classes only, not one true `1.50 mm` same-surface exact-geometry row
- PTI stayed below reopen because the retrievable official capability surface visibly stops at `1.0 mm` ball pitch and does not expose same-surface geometry

## Non-Reopen Filters Reconfirmed

- package-house family listings without one visible true `1.50 mm` pitch row do not clear the gate
- package-house capability pages that visibly stop below `1.50 mm` do not strengthen the current residual
- same-surface geometry is still required even after a real official owner surface is found

## Final Verdict

No new package-house owner class cleared the `1.50 mm` reopen gate in this follow-up.

`SPIL` is now rechecked below gate on a real official family-listing surface, while `PTI` is now rechecked below target pitch on a real official capability surface.
