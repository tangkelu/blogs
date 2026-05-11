# P4-249 B1-R1 ESD Workstation Grounding Exact-Data Landing

Date: 2026-05-07
Parent state: `after P4-248`
Execution mode: `b1_r1_exact_data_landing`

## Purpose

Advance `/code/blogs/tmps/PCB资料` beyond planning by landing the first real exact-data artifact from the `B1` PCBA inspection branch.

This pass targets the narrowest recoverable item outside the partially stalled `A1 capacitor` lane:

- `ESD workstation grounding topology`
- `1 megohm` wrist-strap resistor context

## Inputs Used

- `logs/p4-248-2026-5-7-pcb-pdf-post-a1-b1-r1-resume-entry.md`
- `logs/p4-247-2026-5-7-post-a1-next-exact-data-lane-selection-b1-over-c2.md`
- `logs/p4-215b1-2026-5-6-pcba-lane-b1-eos-esd-handling-pages.md`
- official ESDA fundamentals page
- official Desco `1 Megohm Resistor` article

## What Landed

### New source records

- `sources/registry/methods/esda-part-3-basic-esd-control-procedures-and-materials.md`
- `sources/registry/methods/desco-1-megohm-resistor-esd-grounding-article.md`

Reason:

- the ESDA page provides public association-backed workstation-grounding topology and `common point ground` terminology
- the Desco page provides public standards-adjacent reinforcement for the `1 megohm` wrist-strap and work-surface grounding context
- together they cleanly replace the secondary handbook page-11 figure as authority for one narrow method example

### New exact-data fact card

- `facts/methods/esd-workstation-grounding-topology-and-wrist-strap-resistor-method-example.md`

Reason:

- this is a valid `method_scoped_exact_data` landing
- it captures real handling-control data rather than only vocabulary or local image inventory
- it keeps the `1 megohm` and `1.0 x 10^6` to `1.0 x 10^9` values inside a tightly bounded workstation-grounding method scope

### New local supporting asset linkage

- `p4-221a` now has a new row for the page-11 workstation grounding image pair as:
  - `supporting_local_asset_only`
  - `structural_context_only`

Reason:

- the local handbook figure is still useful for provenance and later prompt consumption
- but it remains non-authoritative and stays attached to the newly landed fact card instead of floating as a standalone truth source

## What Did Not Land

- page-10 handbook resistance-limit and discharge-time tables did not land
- page-8 device-family sensitivity ranges did not land
- page-7 inspection-magnification table did not land
- no full `ANSI/ESD S20.20` or `IEC 61340-5-1` compliance claim was landed

## Result Status

- `B1` lane:
  - `first_exact_data_artifact_landed`
  - `source_backed_fact_layer_partial`
- `PCB资料` batch:
  - now includes a real exact-data landing outside `EMC A1`
  - still not complete for all handbook formulas, thresholds, and numeric tables

## Why This Was The Right First B1 Landing

- it is the cleanest authority-replaceable `B1` target
- it preserves real exact data and method structure from public primary sources
- it avoids the trap of reconstructing blocked standards tables from the secondary handbook
- it gives later blog-writing agents a reusable ESD-control method card plus a traceable local image relationship

## Next Step

1. Keep `B1` page-10 resistance/discharge rows blocked unless stronger public authority is found.
2. Keep `C2-R1` as the next fallback lane if `B1` does not yield another clean bounded recovery.
3. If more `B1` work is needed later, prefer symbol-identity recovery before generic family-sensitivity or magnification tables.
