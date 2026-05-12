# P4-521 Fresh OSAT Package-House 1.50 mm Scout No Reopen

Date: 2026-05-11
Parent surfaces:

- `logs/p4-519-2026-5-11-post-p4-518-residual-priority-and-candidate-pool-tightening-rerank.md`
- `logs/p4-520-2026-5-11-post-p4-519-materially-different-1p50mm-owner-class-recheck-no-new-class.md`
- `logs/p4-508-2026-5-11-infineon-p-bga-pg-bga-current-access-blocker-no-reopen.md`
- `logs/p4-509-2026-5-11-amkor-pbga-1p50mm-family-near-hit-no-reopen.md`
- `logs/backlog.md`
- `logs/phase-status.md`

Execution mode: `controller_owned_fresh_official_source_scout`

## Purpose

Run one fresh official-source surfacing pass outside the current repo to see whether a materially different OSAT / package-house owner class can reopen the still-open `1.50 mm` package residual.

This pass does not assume that repo-log exhaustion means the public web has no further candidates.
It checks one fresh structurally different candidate family only.

## Candidate Gate

Reopen only if one current-public owner surface visibly provides both:

1. true `1.50 mm` pitch identity
2. same-surface printed PCB land-pattern or footprint geometry

## Fresh Candidate Classes Checked

- ASE current-public package-house BGA and substrate pages
- JCET current-public package-house PBGA family surface

## Sources Surfaced

### ASE

- `https://ase.aseglobal.com/wire-bond-bga/`
- `https://ase.aseglobal.com/packaging-substrate/`
- `https://ase.aseglobal.com/flip-chip-packaging/`

### JCET

- `https://www.jcetglobal.com/uploads/PBGA_22Dec2021.pdf`
- search surfaced the official JCET PBGA PDF as a current-public family page

## Findings

### 1. ASE is a fresh structurally different owner class, but the current public surfaces stay below reopen

- ASE current-public `Wire Bond BGA` and `Packaging Substrate` pages are real official package-house surfaces
- they expose PBGA family identity, applications, package-size range, and package-house capability framing
- but they do not expose one same-surface `1.50 mm` pitch row with printed PCB land-pattern or footprint geometry
- ASE current-public `Flip Chip Packaging` capability table is stronger than generic marketing prose because it exposes explicit BGA package classes and ball-pitch ranges
- however the surfaced ASE flip-chip BGA classes stop at:
  - `0.5 ~ 1.00`
  - `0.8 ~ 1.27`
  - `1.0 / 1.27`
- so ASE currently stays below reopen for the `1.50 mm` gate

### 2. JCET is a fresh structurally different owner class, but the surfaced family identity still does not clear the gate

- current search surfacing exposed an official JCET PBGA PDF with visible family-level wording including:
  - `0.65, 0.80, 1.00, 1.27 and 1.50mm ball pitch`
- this makes JCET stronger than blind vendor-name speculation because a real official package-house PBGA family PDF is now surfaced
- however the current environment did not yield one directly retrievable same-surface page or PDF body through the browser-open step; the official URL stayed retrieval-limited in this pass
- even from the surfaced official snippet, the visible value is still only family-level pitch availability, not one printed PCB land-pattern or footprint geometry row
- JCET therefore stays below reopen in the same way that family identity alone stayed below reopen for Amkor

## Gate Result

- no checked fresh OSAT / package-house owner class cleared the `1.50 mm` reopen gate
- ASE stayed below reopen because the visible package classes stop at `1.27` or expose family/capability framing without same-surface geometry
- JCET stayed below reopen because the surfaced official family PDF exposed `1.50 mm` pitch availability but not a retrievable same-surface geometry row in this pass

## Non-Reopen Filters Reconfirmed

- package-house family identity without same-surface footprint geometry is not enough
- capability tables that stop at `1.27 mm` do not strengthen the `1.50 mm` lane
- surfaced official search snippets are not enough to promote exact geometry without a retrievable owner surface
- blocked or retrieval-limited official package-house PDFs remain candidate notes only

## Final Verdict

Fresh official-source surfacing did identify two materially different package-house candidate classes, `ASE` and `JCET`, but neither class cleared the current `1.50 mm` gate.

This pass therefore narrows the fresh non-chip-vendor candidate pool without reopening the residual.
