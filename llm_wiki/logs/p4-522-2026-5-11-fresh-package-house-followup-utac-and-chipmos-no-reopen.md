# P4-522 Fresh Package-House Follow-Up UTAC And ChipMOS No Reopen

Date: 2026-05-11
Parent surfaces:

- `logs/p4-521-2026-5-11-fresh-osat-package-house-1p50mm-scout-no-reopen.md`
- `logs/p4-519-2026-5-11-post-p4-518-residual-priority-and-candidate-pool-tightening-rerank.md`
- `logs/backlog.md`
- `logs/phase-status.md`

Execution mode: `controller_owned_fresh_official_source_followup`

## Purpose

Follow up the fresh non-chip-vendor package-house lane with one more bounded pass on two additional candidate classes:

- one current-public package-house packaging overview
- one official-site retrieval-limited package-house candidate

## Candidate Gate

Reopen only if one current-public owner surface visibly provides both:

1. true `1.50 mm` pitch identity
2. same-surface printed PCB land-pattern or footprint geometry

## Candidate Classes Checked

### UTAC

- current-public official packaging overview:
  - `https://utacgroup.com/packaging/`

### ChipMOS

- current-public official English homepage:
  - `https://www.chipmos.com/english/`

## Findings

### 1. UTAC is a real current-public package-house surface, but it stays below the `1.50 mm` gate

- the current-public UTAC packaging overview is retrievable and official
- the surfaced package classes are:
  - `Leadframe`
  - `Laminate`
  - `Mems & Sensors`
  - `Image Sensor`
  - `SiP`
  - `WLCSP And Bumping`
  - `Power`
- this is useful package-house context, but it does not expose:
  - one visible `1.50 mm` BGA or PBGA pitch identity
  - one same-surface PCB footprint or land-pattern geometry row
- UTAC therefore stays below reopen for the current package exact-geometry residual

### 2. ChipMOS is currently retrieval-limited in the present environment

- the current-public official English homepage request returned `403`
- this means the present pass did not recover one retrievable owner package page, datasheet, or package-family surface strong enough to evaluate the `1.50 mm` gate directly
- current safe handling therefore is:
  - do not treat ChipMOS as a verified new owner class for the lane
  - do not promote any pitch or geometry claim from unretrieved surfaces
  - keep ChipMOS as retrieval-limited only

## Gate Result

- UTAC stayed below reopen because the retrievable official packaging surface exposes package-house category framing rather than one `1.50 mm` same-surface exact-geometry row
- ChipMOS stayed below reopen because the current official surface was retrieval-limited before any qualifying package evidence could be verified

## Non-Reopen Filters Reconfirmed

- package-house packaging overview pages without one visible `1.50 mm` BGA or PBGA row do not clear the gate
- official-site retrieval failure does not count as owner evidence
- unretrieved package-house pages must stay blocked or retrieval-limited rather than being promoted from search-level hints

## Final Verdict

No new package-house owner class cleared the `1.50 mm` reopen gate in this follow-up.

`UTAC` is now rechecked below gate on a real official packaging page, while `ChipMOS` is currently retrieval-limited only.
