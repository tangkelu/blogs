# P4-329 1.50 mm Legacy PBGA Boundary Note

Date: 2026-05-09
Parent lane: `P4-309`
Execution mode: `controller_owned_negative_result_boundary_note`

## Purpose

Preserve one genuinely useful current-public near-hit for the still-open `1.50 mm` package residual without overstating it as a clean exact-geometry recovery.

## Inputs

- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `logs/p4-315-2026-5-8-package-residual-authority-recovery.md`
- `logs/p4-318-2026-5-8-iec-1p50mm-bga-standards-existence-boundary.md`
- `logs/p4-319-2026-5-8-1p50mm-public-exact-geometry-recheck.md`
- `logs/p4-323-2026-5-8-1p50mm-search-filter-note.md`
- current public NXP-hosted archived application note `AN1231: Plastic Ball Grid Array (PBGA)`

## What This Pass Confirmed

- a current public owner-scoped named-document route does exist above the pure standards-metadata layer:
  - `https://www.nxp.com/docs/en/application-note/AN1231.pdf`
- that note explicitly discusses PBGA bottomside solder pads on constant `1.5 mm` pitch
- that same note also contains family-level motherboard pad guidance for most Motorola `1.5 mm` and `60.0 mil` pitch PBGA designs:
  - `25 mil` solderable surface diameter
  - `25 mil` copper
  - at least `1 mil` soldermask clearance around that copper
- the same note explicitly says the exact diameter for any given PBGA design should be obtained before layout

## Why This Is Not A Clean Exact-Geometry Landing

- the document is legacy Motorola/Freescale PBGA family guidance, only currently hosted on the NXP domain
- it is not a named-package `RECOMMENDED LAND PATTERN` drawing
- it does not print a handbook-style universal `1.50 mm -> pad diameter` row
- the note itself blocks overclaim by requiring package-specific diameter confirmation before layout

## Why This Advances The Lane

- `P4-318` only proved standards-owner existence and scope metadata for `1.50 mm` package guidance
- this pass adds one concrete current-public owner-scoped near-hit with real `1.5 mm` pitch and motherboard-pad wording
- this is materially stronger than `P4-319`, which did not preserve any current public `1.50 mm` document with PCB land-geometry content
- however, this still does not justify source/fact promotion as a clean exact-geometry closure in this constrained pass

## Safest Reuse Boundary

- safe to reuse only as:
  - a current-public named-document route above `P4-318`
  - a warning that real `1.5 mm` pitch near-hits can exist without giving clean named-package closure
- not safe to reuse as:
  - a generic cross-vendor `1.50 mm` land-pattern rule
  - a named-package replacement row
  - exact-geometry closure for the handbook lane

## Final Status

- lane result:
  - `negative_result_boundary_note_landed`
- continuation state:
  - `1p50_mm_has_one_current_public_owner_scoped_near_hit_above_p4_318`
  - `1p50_mm_still_below_exact_geometry_closure`
