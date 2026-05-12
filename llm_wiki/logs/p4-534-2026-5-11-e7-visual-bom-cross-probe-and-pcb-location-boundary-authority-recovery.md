# P4-534 E7 Visual BOM Cross-Probe And PCB Location Boundary Authority Recovery

Date: 2026-05-11
Lane owner: `E7 narrow authority recovery`
Execution mode: `source_fact_log_tracker`
Target PDF:
- `/code/blogs/tmps/PCB资料/PCB文章/华秋DFM可视化BOM交互焊接工具，SMT工厂、PCB工程师的福音来了！.pdf`

Parent surfaces:

- `logs/p4-290-2026-5-7-pcb-article-e1-e7-controller-integration.md`
- `logs/p4-283c-2026-5-7-pcb-article-manufacturing-data-exchange-and-vendor-tool-hold-map.md`
- `logs/p4-458-2026-5-11-e7-residual-route-reaudit-and-no-write-closeout.md`
- `facts/methods/package-to-footprint-and-pin-count-alignment-review-boundary.md`
- `facts/methods/pcba-test-method-input-package-boundary.md`

## Purpose

Advance one `E7` lane beyond `claim_family_level_only_with_explicit_hold_reason` by landing a current-public official boundary for visual-BOM navigation between BOM items and PCB-context review.

This pass is intentionally narrow.
It does not try to close assembly correctness, hand-soldering correctness, inventory-checking outcomes, or software sufficiency.

## New Official Source Support

This pass adds two Altium official documentation surfaces:

1. `altium-bomdoc-cross-select-and-cross-probe-between-bom-and-pcb`
   - supports the boundary that a `BomDoc` selection can cross-select or cross-probe corresponding design objects in schematic and PCB documents

2. `altium-activebom-column-settings-pcb-location-rotation-side`
   - supports the boundary that BOM-visible columns can include PCB-derived location, rotation, and side-of-board metadata

## What Was Promoted

Promoted into reusable `facts/` coverage:

- a visual BOM surface may navigate to corresponding PCB objects for review context
- BOM-visible review may expose PCB position context such as location, rotation, and board side
- BOM-linked PCB context is a review-navigation surface rather than proof of package correctness or assembly correctness

## What This Pass Does Not Promote

This pass still does not authorize:

- automatic BOM matching sufficiency
- pad-level or all-pad-position visibility claims
- pin-1 marker, polarity-proof, or `已焊接 / 空贴` progress-marking correctness claims
- IQC material-counting guarantees
- repair-speed, hand-soldering efficiency, or assembly-correctness claims
- universal BOM-viewer behavior across tools

## E7 Lane Effect

`华秋DFM可视化BOM交互焊接工具，SMT工厂、PCB工程师的福音来了！.pdf` is now improved from:

- `claim_family_level_only_with_explicit_hold_reason`

to:

- `official_fact-backed` for one narrow `visual BOM cross-probe and PCB location context` surface

The rest of the PDF remains hold-only and blocked as before.

## Deliverables Created

- `sources/registry/methods/altium-bomdoc-cross-select-and-cross-probe-between-bom-and-pcb.md`
- `sources/registry/methods/altium-activebom-column-settings-pcb-location-rotation-side.md`
- `facts/methods/bomdoc-cross-probe-and-pcb-location-context-boundary.md`

## Tracker Implication

This pass is strong enough to refresh:

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`
- `logs/backlog.md`
- `logs/phase-status.md`
- `logs/update-log.md`

## Verification Target

- source IDs resolve cleanly inside the new fact card
- the per-PDF `E7` entry for `华秋DFM可视化BOM交互焊接工具，SMT工厂、PCB工程师的福音来了！.pdf` no longer understates the lane as hold-only
- current tracker wording no longer says the article residual set is still three branded-tool `E7` hold-only PDFs
- `git diff --check -- /code/blogs/llm_wiki` should pass after tracker refresh
