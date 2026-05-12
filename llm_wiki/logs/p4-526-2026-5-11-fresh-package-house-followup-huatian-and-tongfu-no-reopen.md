# P4-526 Fresh Package-House Follow-Up Huatian And Tongfu No Reopen

Date: 2026-05-11
Parent surfaces:

- `logs/p4-525-2026-5-11-powertech-dedup-to-pti-and-kyec-no-reopen.md`
- `logs/p4-524-2026-5-11-fresh-package-house-followup-unisem-and-stats-chippac-no-reopen.md`
- `logs/p4-523-2026-5-11-fresh-package-house-followup-spil-and-pti-no-reopen.md`
- `logs/p4-521-2026-5-11-fresh-osat-package-house-1p50mm-scout-no-reopen.md`
- `logs/backlog.md`
- `logs/phase-status.md`

Execution mode: `subagent_aided_fresh_official_source_followup`

## Purpose

Follow up the fresh non-chip-vendor package-house lane with one more bounded pass on two additional current-public official classes:

- one package-house family and capability owner surface
- one package-house owner product series surface with visible pitch range

## Candidate Gate

Reopen only if one current-public owner surface visibly provides both:

1. true `1.50 mm` pitch identity
2. same-surface printed PCB land-pattern or footprint geometry

## Candidate Classes Checked

### Huatian

- current-public official company and package-family surfaces:
  - `https://www.ht-tech.com/html/about/index.html`
  - `https://www.ht-tech.com/html/fzcp/index.html`
  - `https://www.ht-tech.com/html/fc/index.html`

### Tongfu

- current-public official English product-series surface:
  - `https://en.tfme.com/product/50.html`
- current-public official download surfaces:
  - `https://www.tfme.com/companyfile/15/`
  - `https://www.tfme.com/companyfile/18/`

## Findings

### 1. Huatian is a real current-public package-house surface, but it stays at family and capability framing only

- the surfaced official Huatian pages are real current-public package-house owner surfaces
- they visibly expose package-family or capability framing such as:
  - `FBGA / TFBGA / LFBGA`
  - `LGA`
  - `EHS-FBGA`
  - `FCBGA / HFCBGA / CFCBGA`
- the surfaced `FC` page also exposes `I/O` and product-size range context
- however the current-public content does not expose:
  - one true `1.50 mm` pitch identity
  - one same-surface printed PCB land-pattern or footprint geometry row
- Huatian therefore stays below reopen as a family-only current-public package-house surface

### 2. Tongfu is a real current-public package-house surface, but the visible pitch range stays below target

- the surfaced official Tongfu `WBBGALGA(HS)PBGAB Series` page is a real current-public owner surface
- its visible pitch wording states:
  - `0.35, 0.4, 0.5, 0.65, 0.75, 0.80 & 1.0 mm`
- this is strong enough to classify the current-public surface directly
- however it still stays below the current `1.50 mm` gate because:
  - the visible pitch range stops at `1.0 mm`
  - the page also does not expose one same-surface printed PCB land-pattern or footprint geometry row
- adjacent official download surfaces did not overturn this below-target-pitch reading in the current public layer
- Tongfu therefore stays below reopen as a below-target-pitch owner surface

## Gate Result

- Huatian stayed below reopen because the retrievable official owner surfaces expose package-family and capability framing only, not one true `1.50 mm` same-surface exact-geometry row
- Tongfu stayed below reopen because the retrievable official owner surface visibly stops at `1.0 mm` pitch and does not expose same-surface geometry

## Non-Reopen Filters Reconfirmed

- package-house family and capability pages without one visible true `1.50 mm` pitch row do not clear the gate
- package-house owner series pages that visibly stop at `1.0 mm` pitch do not strengthen the current `1.50 mm` residual
- same-surface geometry is still required even after one real current-public owner surface is recovered

## Final Verdict

No new package-house owner class cleared the `1.50 mm` reopen gate in this follow-up.

`Huatian` is now rechecked below gate on real current-public family and capability surfaces, while `Tongfu` is now rechecked below target pitch on a real current-public owner series surface.
