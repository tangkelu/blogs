# P4-510 Post-P4-509 Residual Rerank Keep 1.50 mm But Tighten Candidate Class

Date: 2026-05-11
Parent surfaces:

- `logs/p4-503-2026-5-11-completion-audit-successor-after-handbook-nine-route-state.md`
- `logs/p4-507-2026-5-11-ipc-public-bga-csp-1p50mm-pitch-and-0p75ball-geometry-boundary.md`
- `logs/p4-508-2026-5-11-infineon-p-bga-pg-bga-current-access-blocker-no-reopen.md`
- `logs/p4-509-2026-5-11-amkor-pbga-1p50mm-family-near-hit-no-reopen.md`
- `logs/p4-492-2026-5-11-0p75mm-owner-and-standards-candidate-scout-no-reopen-successor.md`

Execution mode: `subagent_aided_controller_rerank`

## Purpose

Refresh the next continuation priority again after `P4-507`, `P4-508`, and `P4-509`.

This pass does not land new `sources/`, `facts/`, or `wiki/`.
It only records the cleanest restart rule so future AI does not demote the whole `1.50 mm` lane merely because two concrete sub-classes were tightened below reopen.

## Rechecked Surfaces

1. the current `1.50 mm` package ceiling after `P4-507`
2. the current `1.50 mm` Infineon package-portal access state after `P4-508`
3. the current `1.50 mm` Amkor family-identity near-hit after `P4-509`
4. the current `0.75 mm`, doctrine, handbook, and article residual position after `P4-492` and `P4-503`

## Findings

### 1. `1.50 mm` remains the best current reopen lane

- `P4-507` raised the public non-owner side of the lane again through one IPC-hosted geometry boundary.
- the lane therefore still has real upward movement above:
  - `IEC` existence and family framing
  - multiple owner exact rows
- this keeps `1.50 mm` ahead of the other still-open residuals.

### 2. What got demoted is not the lane itself, but two concrete candidate classes

- `P4-508` keeps the current Infineon package-portal concrete URLs below reopen because the current environment only returns `HTTP/2 202` plus `x-amzn-waf-action: challenge`.
- `P4-509` keeps the current Amkor `PBGA/TEPBGA` family page below reopen because it exposes true `1.50 mm` family identity without same-surface footprint geometry.
- these two results tighten the candidate filter.
- they do not justify demoting the entire `1.50 mm` lane below `0.75 mm`, doctrine, handbook, or article residuals.

### 3. `0.75 mm`, doctrine, handbook, and article residuals still rank below current `1.50 mm`

- `0.75 mm` remains a watch-only residual below `1.50 mm` on the current stack.
- doctrine remains a tightened near-hit set without a stronger current-public authority surface.
- the `194页 handbook` remains not the current main reopen target.
- article residuals remain broadly re-audited closed at the current authority layer.

### 4. The next-action rule must now be even narrower

- the next valid `1.50 mm` reopen should not come from:
  - package-family identity alone
  - package-portal structure alone
  - metadata-only standards pages
  - TOC or front-matter visibility
- the next valid candidate class should be:
  - one current-public owner package drawing or datasheet surface
  - with true `1.50 mm` package identity
  - and same-surface printed PCB land-pattern / footprint geometry row or drawing

## Audit Result

- no new residual lane was landed
- no per-PDF state changed
- tracker wording required refresh because the reopen class is now narrower than the earlier generic `candidate-gated` wording

## Recommended Residual Order

If `/goal` continues from here, use this order:

1. `1.50 mm` package exact-geometry residual
   - but only as `owner same-surface exact-geometry candidate-gated recovery`
   - reopen only if a candidate visibly exposes:
     - true `1.50 mm` package identity
     - and printed PCB land-pattern / footprint geometry in the same public owner surface
2. `0.75 mm` package exact-data residual
   - only if a candidate clearly exceeds the current `Microchip + Renesas + NXP + Intel` ceiling
3. doctrine and handbook residuals
   - only if a genuinely stronger authority surface appears above the current tightened near-hit sets

## What This Pass Fixes

- future AI should not demote the whole `1.50 mm` lane just because current Infineon and Amkor sub-classes stayed below reopen
- future AI should not reopen `1.50 mm` on package-family identity or package-portal structure alone
- future AI should treat `owner same-surface exact geometry` as the only clean next candidate class for `1.50 mm`
