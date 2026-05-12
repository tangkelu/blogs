# P4-524 Fresh Package-House Follow-Up Unisem And STATS ChipPAC No Reopen

Date: 2026-05-11
Parent surfaces:

- `logs/p4-523-2026-5-11-fresh-package-house-followup-spil-and-pti-no-reopen.md`
- `logs/p4-522-2026-5-11-fresh-package-house-followup-utac-and-chipmos-no-reopen.md`
- `logs/p4-521-2026-5-11-fresh-osat-package-house-1p50mm-scout-no-reopen.md`
- `logs/p4-519-2026-5-11-post-p4-518-residual-priority-and-candidate-pool-tightening-rerank.md`
- `logs/backlog.md`
- `logs/phase-status.md`

Execution mode: `subagent_aided_fresh_official_source_followup`

## Purpose

Follow up the fresh non-chip-vendor package-house lane with one more bounded pass on two additional candidate classes:

- one current-public package-house array-package offering surface with linked official PDF
- one current-public package-house technology and applications framing surface

## Candidate Gate

Reopen only if one current-public owner surface visibly provides both:

1. true `1.50 mm` pitch identity
2. same-surface printed PCB land-pattern or footprint geometry

## Candidate Classes Checked

### Unisem

- current-public official array-package offering surface:
  - `https://www.unisemgroup.com/package-offerings/array/fbga-lga/`
- linked current-public official package configuration PDF:
  - `https://www.unisemgroup.com/wp-content/uploads/2016/03/FBGALGAconfig.pdf`

### STATS ChipPAC

- current-public official technology surface:
  - `https://www.statschippac.com/technology-flip-chip-packaging-technology`
- current-public official applications surface:
  - `https://www.statschippac.com/applications-computing`

## Findings

### 1. Unisem is a real current-public package-house surface, but the visible pitch stays below target

- the surfaced official Unisem `FBGA / LGA` page is a real package-house owner surface
- its visible pitch wording states:
  - `Solder Ball Pitch: 0.5mm and 0.8mm`
- the linked official `Package Configurations` PDF is useful as an owner-adjacent supporting surface, but this pass still did not surface:
  - one true `1.50 mm` pitch identity
  - one same-surface printed PCB land-pattern or footprint geometry row
- Unisem therefore stays below reopen as a below-target-pitch owner surface

### 2. STATS ChipPAC is a real current-public package-house surface, but it stays at family framing only

- the surfaced official STATS ChipPAC pages are real current-public package-house surfaces
- they visibly expose package-family or application framing such as:
  - `WB-BGA`
  - `fcBGA`
  - `FBGA`
- however the current-public content does not expose:
  - one true `1.50 mm` pitch identity
  - one same-surface printed PCB land-pattern or footprint geometry row
- STATS ChipPAC therefore stays below reopen as a family-only current-public surface

## Gate Result

- Unisem stayed below reopen because the retrievable official owner surface visibly stops at `0.5mm and 0.8mm` solder ball pitch and does not expose same-surface geometry strong enough for the current lane
- STATS ChipPAC stayed below reopen because the retrievable official surfaces expose package-family framing only, not one true `1.50 mm` same-surface exact-geometry row

## Non-Reopen Filters Reconfirmed

- package-house owner surfaces that visibly stop at `0.5 mm` or `0.8 mm` ball pitch do not strengthen the current `1.50 mm` residual
- package-house technology or applications pages that expose family names only do not clear the gate
- same-surface geometry is still required even after one real current-public owner surface is recovered

## Final Verdict

No new package-house owner class cleared the `1.50 mm` reopen gate in this follow-up.

`Unisem` is now rechecked below target pitch on a real official owner surface, while `STATS ChipPAC` is now rechecked below gate on real current-public family-framing surfaces only.
