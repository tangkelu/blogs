# P4-539 JCET PBGA PDF Now Directly Retrievable But Still No Reopen

Date: 2026-05-12
Parent surfaces:

- `logs/p4-521-2026-5-11-fresh-osat-package-house-1p50mm-scout-no-reopen.md`
- `logs/p4-529-2026-5-11-blocked-and-retrieval-limited-package-surfaces-no-state-change.md`
- `logs/p4-536-2026-5-12-date-rollover-1p50mm-current-public-candidate-recheck-no-reopen.md`
- `logs/p4-537-2026-5-12-current-state-completion-audit-successor-after-e7-closeout-and-1p50-recheck.md`
- `logs/backlog.md`
- `logs/phase-status.md`

Execution mode: `controller_owned_state_change_recheck`

## Purpose

Record one real state change on a previously retrieval-limited owner path:

- the official `JCET` `PBGA` family PDF is now directly retrievable in the current environment
- but the newly retrievable public content still does not clear the current `1.50 mm` reopen gate

## Candidate Gate

Reopen only if one current-public owner surface visibly provides both:

1. true `1.50 mm` pitch identity
2. same-surface printed PCB land-pattern or footprint geometry

## Surface Rechecked

- `https://www.jcetglobal.com/uploads/PBGA_22Dec2021.pdf`

## Findings

### 1. The official `JCET` PBGA PDF is now directly retrievable

- the official URL now returns `200 OK` in the current environment
- the current pass also successfully downloaded the PDF body rather than stopping at search-surface snippet level only
- this is a real state change relative to the earlier `retrieval-limited` wording in `P4-521` and `P4-529`

### 2. The retrievable PDF still exposes family-level package information, not one qualifying same-surface PCB geometry row

- the current publicly visible PDF content supports `PBGA` as a real official package-house family surface
- it visibly exposes family-level wording including:
  - `0.65, 0.80, 1.00, 1.27 and 1.50mm ball pitch`
- it also visibly exposes package-house family content such as:
  - package configurations
  - thermal-performance tables
  - reliability and construction framing
- however the currently reviewed public content still does not expose:
  - one printed PCB land-pattern geometry row
  - one same-surface footprint drawing with recommended PCB pad geometry
  - one package-scoped exact row above the current `NXP + Renesas + AMD` stack

## Gate Result

- `JCET` has improved from `retrieval-limited family candidate` to `directly reviewable family-level owner PDF`
- but it still does not reopen `1.50 mm` because the retrievable public surface stops at family-level pitch availability plus package-family framing, without same-surface PCB geometry

## What This Fixes

- future AI should no longer treat the official `JCET` `PBGA` PDF as merely retrieval-limited in the current environment
- future AI should also not promote this state change into `1.50 mm` reopen, because direct retrievability alone is still not enough without same-surface PCB footprint or land-pattern geometry
- `JCET` is now stronger than snippet-only family identity, but still below gate in the same way that `Amkor` family identity stayed below reopen

## Final Verdict

The official `JCET` `PBGA` PDF has changed from retrieval-limited to directly retrievable in the current environment, but it still stays below the current `1.50 mm` gate because the publicly visible content does not expose one same-surface PCB land-pattern or footprint-geometry row.
