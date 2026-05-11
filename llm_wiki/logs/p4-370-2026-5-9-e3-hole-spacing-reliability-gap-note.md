# P4-370 E3 Hole-Spacing Reliability Gap Note

Date: 2026-05-09
Parent lane: `P4-311`
Execution mode: `controller_owned_negative_result_boundary_note`

## Purpose

Preserve one high-value negative result for `E3-H` so future `/goal` work does not reopen weak `hole-spacing reliability` recovery attempts without a materially stronger official or standards-adjacent source layer.

## Inputs

- `logs/p4-311-2026-5-8-pcb-article-e3-usage-route-integration.md`
- `logs/p4-283e3-2026-5-7-pcb-article-e3-claim-family-boundary-map.md`
- `/code/blogs/tmps/PCB资料/PCB文章/PCB设计孔间距的DFM可靠性.pdf`
- current repo-wide `sources/registry/`, `facts/`, and `logs` grep for:
  - `hole spacing`
  - `breakout`
  - `structural weakness`
  - `CAF`
  - `reliability`

## What This Pass Confirmed

- the current repo is strong enough for one controller-level posture:
  - hole-to-hole spacing belongs to a reliability and failure-risk review family
- the current article also reinforces that spacing-sensitive failure language exists around:
  - breakout-like damage
  - weakened annular-ring or hole-surround context
  - spacing-sensitive short-risk narratives
- however, the current repo still does not contain one clean official or standards-adjacent terminology anchor that would justify a new reusable `hole-spacing reliability` boundary fact

## Why This Is Not A Clean Boundary Landing

- the strongest currently visible support remains article-side and threshold-heavy
- the article mixes:
  - explicit spacing numerics
  - fabrication thresholds
  - workmanship-style failure narratives
  - one quoted `IPC-A-600` reference that is not preserved in a reusable official source layer inside repo
- there is still no local source record or fact card that cleanly closes:
  - breakout or structural-weakness terminology
  - spacing-sensitive reliability wording
  - standards-owner acceptance framing

## Safest Reuse Boundary

- safe to reuse only as:
  - hole-to-hole spacing as a reliability and review topic
  - spacing-sensitive failure risk as a guarded review-family label
- not safe to reuse as:
  - official or standards-adjacent reliability terminology boundary
  - numeric spacing rule
  - breakout, CAF, annular-ring, or short-risk threshold rule
  - acceptance or supplier-capability claim

## Final Status

- lane result:
  - `negative_result_boundary_note_landed`
- continuation state:
  - `hole_spacing_reliability_remains_controller_level_taxonomy_only`
  - `future_reopen_should_require_a_real_official_or_standards_adjacent_reliability_anchor`
