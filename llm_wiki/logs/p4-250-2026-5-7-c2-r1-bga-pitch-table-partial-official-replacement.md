# P4-250 C2-R1 BGA Pitch Table Partial Official Replacement

Date: 2026-05-07
Parent state: `after P4-249`
Execution mode: `c2_r1_partial_exact_data_landing`

## Purpose

Advance `/code/blogs/tmps/PCB资料` on the `C2-R1` package lane by replacing part of the handbook `BGA pitch-to-pad-diameter` table with a primary-source-backed exact-data artifact.

This pass is intentionally partial, not universal.

## Inputs Used

- `logs/p4-215c2-2026-5-6-package-lane-c2-pad-origin-pin1-keepout-drawings.md`
- local handbook image `cb091987d7d2b074.jpeg`
- official NXP application note `AN10778`

## Handbook Claim Inventory Reconfirmed

The local page-28 table remains complete enough for claim inventory and shows these visible rows:

- `1.50 -> 0.55 / 0.6`
- `1.27 -> 0.55 / 0.60 (0.60)`
- `1.00 -> 0.45 / 0.50 (0.48)`
- `0.80 -> 0.375 / 0.40 (0.40)`
- `0.75 -> 0.35 / 0.375`
- `0.65 -> 0.275 / 0.3`
- `0.50 -> 0.225 / 0.25`
- `0.40 -> 0.17 / 0.2`

This remains `secondary_pdf_claim_inventory_only`.

## What Landed

### New source record

- `sources/registry/methods/nxp-an10778-bga-footprints.md`

Reason:

- it is an official NXP application note
- it prints named-package BGA footprint rows with ball pitch and `PCB land pad diameter`
- it gives a primary-source replacement for several handbook pitch classes

### New exact-data fact card

- `facts/methods/nxp-bga-footprint-pitch-and-pcb-land-pad-examples.md`

Reason:

- this is a valid `part_scoped_exact_data` landing
- it preserves real package-scoped footprint numbers
- it explicitly prevents the handbook table from being rewritten as a universal industry rule

## What Was Replaced Versus Not Replaced

### Primary-source-backed partial replacement now available

- `1.0 mm` pitch:
  - NXP example with `PCB land pad diameter 0.45`
- `0.8 mm` pitch:
  - NXP examples with `PCB land pad diameter 0.35`
  - NXP examples with `PCB land pad diameter 0.30`
- `0.65 mm` pitch:
  - NXP example with `PCB land pad diameter 0.25`
- `0.5 mm` pitch:
  - NXP examples with `PCB land pad diameter 0.25`

### Still not replaced by this pass

- `1.50 mm` pitch handbook row
- `1.27 mm` pitch handbook row
- `0.75 mm` pitch handbook row
- `0.40 mm` pitch handbook row
- handbook `MIN / MAX / recommended` framing as a generic table shape

## Why This Was A Partial Landing Rather Than A Universal Card

- the NXP table is package-scoped, not pitch-universal
- the same `0.8 mm` pitch already maps to more than one `PCB land pad diameter` inside NXP's own examples
- that is strong evidence against promoting the handbook's table as a single generic industry rule

## Result Status

- `C2-R1`:
  - `partial_exact_data_artifact_landed`
  - `source_backed_fact_layer_partial`
- residual blocker state:
  - handbook still contains uncovered pitch classes and generic table framing not replaced by this pass

## Next Step

1. Only reopen `C2-R1` if a later pass can recover additional official pitch classes such as `1.27`, `0.75`, or `0.40`.
2. Otherwise, prefer another bounded lane instead of forcing a fake universal BGA rule.
3. Keep all handbook-only `MIN / MAX / recommended` rows blocked unless the exact row is replaced by stronger official package-owner evidence.
