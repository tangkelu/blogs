# P4-525 Powertech Dedup To PTI And KYEC No Reopen

Date: 2026-05-11
Parent surfaces:

- `logs/p4-524-2026-5-11-fresh-package-house-followup-unisem-and-stats-chippac-no-reopen.md`
- `logs/p4-523-2026-5-11-fresh-package-house-followup-spil-and-pti-no-reopen.md`
- `logs/p4-520-2026-5-11-post-p4-519-materially-different-1p50mm-owner-class-recheck-no-new-class.md`
- `logs/backlog.md`
- `logs/phase-status.md`

Execution mode: `subagent_aided_followup_and_dedup`

## Purpose

Resolve one fresh package-house follow-up pair without accidentally counting one already-closed official class twice:

- dedup `Powertech` against the already-logged `PTI` official class
- evaluate `KYEC` as one more current-public package-house owner surface

## Candidate Gate

Reopen only if one current-public owner surface visibly provides both:

1. true `1.50 mm` pitch identity
2. same-surface printed PCB land-pattern or footprint geometry

## Candidate Classes Checked

### Powertech

- current-public official `Wire Bond BGA` capability surface:
  - `https://www.pti.com.tw/en/service/packaging/wire-bond-bga`
- adjacent official family surfaces:
  - `https://www.pti.com.tw/en/service/packaging/flip-chips`
  - `https://www.pti.com.tw/en/service/packaging/system-in-package`

### KYEC

- current-public official packaging service surface:
  - `https://www.kyec.com.tw/zh-tw/Service/%E5%B0%81%E8%A3%9D%E6%9C%8D%E5%8B%99`
- adjacent official English family surface:
  - `https://www.kyec.com.tw/en/Service/lga-land-grid-array`

## Findings

### 1. `Powertech` is not a new class for this lane; it collapses into the already-logged `PTI` official surface

- the surfaced current-public `Powertech` official package-house pages are under the present `PTI` official domain and match the already-checked `PTI` class
- the visible `Wire Bond BGA` pitch wording remains:
  - `0.3 to 1.0mm ball pitch available`
- this reconfirms the same result already landed in `P4-523`:
  - visible pitch stays below the current `1.50 mm` target
  - no same-surface printed PCB land-pattern or footprint geometry row was surfaced
- `Powertech` therefore should not be treated as one additional fresh owner class beyond the already-closed `PTI` lane

### 2. `KYEC` is a real current-public package-house surface, but it stays at family framing and package-dimension context only

- the surfaced official `KYEC` packaging service pages are real current-public package-house surfaces
- they visibly expose package-family or service framing such as:
  - `LFBGA`
  - `TFBGA`
  - `Mini BGA`
- one visible `1.5 mm` value appears in package-outline size context such as:
  - `14 mm x 14 mm x 1.5 mm`
- this does not satisfy the current reopen gate because the visible `1.5 mm` belongs to package dimension context rather than true pitch identity
- the surfaced current-public content also does not expose one same-surface printed PCB land-pattern or footprint geometry row
- `KYEC` therefore stays below reopen as a family-only and false-positive-filter owner surface

## Gate Result

- `Powertech` did not create one new candidate class because the surfaced official pages collapse into the already-logged `PTI` class, which remains below target pitch
- `KYEC` stayed below reopen because the surfaced official pages expose package-family framing and one body-dimension-style `1.5 mm` value, not one true `1.50 mm` same-surface exact-geometry row

## Non-Reopen Filters Reconfirmed

- official alias or brand-name variation should not be counted as a new package-house class when it resolves to the same already-logged official owner surface
- visible `1.5 mm` package dimensions do not count as true `1.50 mm` pitch identity
- package-service family pages without same-surface geometry do not clear the gate

## Final Verdict

No new package-house owner class cleared the `1.50 mm` reopen gate in this follow-up.

`Powertech` is now explicitly deduped back into the already-closed `PTI` official lane, while `KYEC` is now rechecked below gate on real current-public package-service surfaces only.
