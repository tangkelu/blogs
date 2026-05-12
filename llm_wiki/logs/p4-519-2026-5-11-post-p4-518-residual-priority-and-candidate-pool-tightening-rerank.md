## P4-519 Post-P4-518 Residual Priority And Candidate-Pool Tightening Rerank

Date: 2026-05-11
Parent surfaces:

- `logs/p4-515-2026-5-11-post-p4-514-residual-priority-and-completion-gap-rerank.md`
- `logs/p4-516-2026-5-11-new-vendor-cluster-1p50mm-owner-same-surface-scout.md`
- `logs/p4-517-2026-5-11-new-vendor-cluster-1p50mm-owner-same-surface-scout-2.md`
- `logs/p4-518-2026-5-11-new-vendor-cluster-0p75mm-owner-same-surface-scout.md`
- `logs/backlog.md`
- `logs/phase-status.md`

Execution mode: `controller_owned_residual_priority_rerank`

## Purpose

Rerank the remaining open residual lanes after the latest three broad owner-cluster scouts, while also deciding whether another same-shape cluster scout is still the best bounded continuation.

Note: this rerank predates `P4-530` / `P4-531`. `Infineon` later changed from blocked to publicly retrievable-but-wrong-pitch; keep the blocked wording below as a snapshot of the state at that time.

## Changed Files

- `logs/p4-519-2026-5-11-post-p4-518-residual-priority-and-candidate-pool-tightening-rerank.md`

## Residual Lanes Checked

### 1. `1.50 mm` package exact-geometry lane

- still the top remaining reopen lane
- `P4-516` and `P4-517` close two more owner-cluster classes without surfacing one qualifying same-surface `true 1.50 mm pitch + printed PCB land-pattern geometry` row
- `P4-508` still keeps the current Infineon package-portal URLs blocked rather than retrievable at that snapshot
- `P4-509` still keeps Amkor at near-hit only because pitch identity appears without same-surface footprint geometry
- `P4-511` through `P4-514` keep body-size `1.50` and wrong-pitch same-surface package pages from being mistaken for the target lane
- `P4-507` still raises the public standards-adjacent geometry framing, but not to a universal closeout row

### 2. `0.75 mm` package-row lane

- still open, but still secondary to `1.50 mm`
- `P4-518` further tightens the lane by showing that even true `0.75 mm` owner pitch identity from Micron and Fujitsu is still not enough without one same-surface geometry row that exceeds the current `Microchip + Renesas + NXP + Intel` stack
- no new owner class or public official geometry surface cleared the current `0.75 mm` gate in the latest scout

### 3. `connector-origin` / `installation mark` doctrine lane

- still open as layered support, not universal closure
- nothing in `P4-516` to `P4-518` produced a materially stronger doctrine-side authority surface
- this lane remains watch-only behind the package-side exact-geometry gaps

### 4. `194页 handbook` residual lane

- still below `full_corpus_closed_without_open_residual_authority_gaps`
- nothing in `P4-516` to `P4-518` changes the current handbook ceiling
- this lane remains watch-only rather than the best next reopen target

## Candidate-Pool Tightening Result

- the latest three broad owner-cluster scouts did not open a new candidate class above the current gates
- the main value of `P4-516` to `P4-518` is therefore candidate-pool tightening, not discovery of a new reopen lane
- another same-shape broad vendor-cluster scout is now lower-yield than holding the current gate unless one materially different owner surface appears

## Recommended Next Lane

Proceed only on this bounded continuation:

- keep `1.50 mm` as the first reopen lane, but only when a materially different current-public owner surface appears that can plausibly expose both true `1.50 mm` pitch identity and same-surface printed PCB land-pattern geometry
- treat previously blocked owner pages as reevaluation candidates only if they become publicly retrievable
- do not spend the next pass on another blind broad vendor-cluster scout with the same filters unless a genuinely new owner class is identified first

## Non-Reopen Filters Reconfirmed

- visible `1.50` in package body-size context is not pitch identity
- same-surface geometry without true `1.50 mm` pitch identity is not enough
- true pitch identity without same-surface footprint or land-pattern geometry is not enough
- family pages, module pages, materials pages, technical reports, and generic BGA guides are not reopen signals
- current access-blocked owner URLs remain blocked candidates only
- true `0.75 mm` pitch identity alone does not beat the current owner stack

## Rerank Result

- `1.50 mm` exact-geometry recovery remains the highest-priority open residual lane
- `0.75 mm` remains open but secondary
- doctrine and handbook remain below the package-side residuals in reopen priority
- the current candidate pool is tighter than it was at `P4-515`, so the next useful pass should be candidate-class-gated rather than another broad cluster sweep by default

## Completion Gap Note

The repo still does not satisfy `full_corpus_closed_without_open_residual_authority_gaps`.

The smallest meaningful remaining gap is still a genuine public owner surface with both true `1.50 mm` pitch identity and same-surface footprint or land-pattern geometry, but the recent broad owner-cluster sweeps now also show that repeating the same scout shape is lower-yield unless a materially different candidate class appears first.
