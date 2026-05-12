# P4-527 Package-House Candidate-Pool Exhaustion Rerank

Date: 2026-05-11
Parent surfaces:

- `logs/p4-521-2026-5-11-fresh-osat-package-house-1p50mm-scout-no-reopen.md`
- `logs/p4-522-2026-5-11-fresh-package-house-followup-utac-and-chipmos-no-reopen.md`
- `logs/p4-523-2026-5-11-fresh-package-house-followup-spil-and-pti-no-reopen.md`
- `logs/p4-524-2026-5-11-fresh-package-house-followup-unisem-and-stats-chippac-no-reopen.md`
- `logs/p4-525-2026-5-11-powertech-dedup-to-pti-and-kyec-no-reopen.md`
- `logs/p4-526-2026-5-11-fresh-package-house-followup-huatian-and-tongfu-no-reopen.md`
- `logs/backlog.md`
- `logs/phase-status.md`

Execution mode: `controller_owned_residual_rerank`

## Purpose

Absorb the fresh package-house follow-up chain from `P4-521` through `P4-526` into one current exhaustion view.

The goal here is not to reopen anything.
The goal is to stop treating the current package-house lane as if it still has a clearly queued new class by default.

Note: this note predates `P4-530` / `P4-531`. `Infineon` later changed from blocked to publicly retrievable-but-wrong-pitch; keep the blocked wording here as a historical snapshot, not live state.

## Current Residual Gate

Reopen only if one current-public owner surface visibly provides both:

1. true `1.50 mm` pitch identity
2. same-surface printed PCB land-pattern or footprint geometry

## Classes Now Rechecked Below Gate or Closed by Dedup

- `ASE` - below gate
- `JCET` - family identity only, retrieval-limited on same-surface geometry
- `UTAC` - below gate
- `ChipMOS` - retrieval-limited only
- `SPIL` - below gate
- `PTI` - below target pitch
- `Unisem` - below target pitch
- `STATS ChipPAC` - family-only
- `Powertech` - deduped into `PTI`
- `KYEC` - family-only plus package-dimension false-positive filter
- `Huatian` - family-only
- `Tongfu` - below target pitch
- `Amkor` - stronger family-level near-hit only
- `Infineon package-portal` - blocked at the time

## Rerank Result

1. `1.50 mm` remains the top residual because no fresh package-house class has cleared the gate.
2. `0.75 mm` remains second and still needs its own same-surface geometry bar.
3. Doctrinal / handbook lanes remain below the package-side exact-geometry gap.
4. Another blind package-house vendor sweep is now lower value than:
   - a genuinely new current-public owner surface not already in the above list
   - or a blocked/retrieval-limited owner path becoming publicly retrievable

## What This Rerank Fixes

- future AI should not assume that the named package-house pool still has an obvious unreviewed next class
- future AI should not treat `Powertech` as separate from `PTI`
- future AI should not treat package-dimension `1.5 mm` values as true `1.50 mm` pitch identity
- future AI should not default to another blind broad package-house scout unless a new owner surface is actually surfaced first

## Final Verdict

The current package-house candidate pool is now exhausted at the present evidence layer.

The safe continuation is to wait for a genuinely new owner surface or a blocked path to become retrievable, not to keep cycling the same named package-house class space.
