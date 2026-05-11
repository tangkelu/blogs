---
fact_id: "methods-nxp-bga-footprint-pitch-and-pcb-land-pad-examples"
title: "NXP BGA footprint values are reusable only as named-package pitch and PCB-land-pad examples"
topic: "NXP BGA footprint pitch and PCB land pad examples"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-05-07"
exact_data_class: "part_scoped_exact_data"
scope_type: "vendor_scoped_named_package_bga_footprint_examples"
canonical_unit_policy: "Preserve original NXP millimeter values, package names, and column meanings such as ball pitch, ball diameter, BGA substrate land diameter, PCB land pad diameter, and solder mask diameter. Do not normalize these rows into a universal pitch-to-pad table."
source_ids:
  - "nxp-an10778-bga-footprints"
tags: ["nxp", "bga", "footprint", "pcb-land-pad", "ball-pitch", "land-pattern", "named-package", "exact-data"]
---

# Canonical Summary

> NXP's `AN10778` is strong enough to support one narrow exact-data layer for the `C2-R1` package lane: the local corpus may reuse named-package BGA footprint example rows that tie ball pitch to package-specific `PCB land pad diameter` values in `Table 2`. This card is a vendor-scoped named-package example only. It does not authorize the handbook's generic `pitch -> pad diameter` table as a universal industry rule.

## Exact Data Scope

- exact for:
  - NXP's printed `Table 2` rows
  - NXP package names
  - NXP column meanings for pitch, ball diameter, substrate land diameter, PCB land pad diameter, and solder mask diameter
- not exact for:
  - cross-vendor generic BGA land-pattern defaults
  - handbook rows with no matched primary source
  - all packages at the same pitch
  - universal `min / max / recommended` pitch tables

## Admitted Data

- NXP prints these named-package footprint examples in `Table 2`:
  - `(L)BGA256`:
    - ball pitch `1.0`
    - ball diameter `0.50`
    - BGA substrate land diameter `0.45`
    - PCB land pad diameter `0.45`
    - solder mask diameter `0.6`
  - `TFBGA100`, `TFBGA144`, `TFBGA180`, and `TFBGA208 (SOT950-1)`:
    - ball pitch `0.8`
    - ball diameter `0.45`
    - BGA substrate land diameter `0.4`
    - PCB land pad diameter `0.35`
    - solder mask diameter `0.5`
  - `LFBGA208`, `LFBGA256`, and `LFBGA324`:
    - ball pitch `0.8`
    - ball diameter `0.45`
    - BGA substrate land diameter `0.4`
    - PCB land pad diameter `0.30`
    - solder mask diameter `0.42`
  - `TFBGA296`:
    - ball pitch `0.8`
    - ball diameter `0.45`
    - BGA substrate land diameter `0.4`
    - PCB land pad diameter `0.35` with one-trace routing row
    - PCB land pad diameter `0.30` with two-trace routing row
  - `TFBGA208 (SOT930-1)`:
    - ball pitch `0.65`
    - ball diameter `0.4`
    - BGA substrate land diameter `0.26`
    - PCB land pad diameter `0.25`
    - solder mask diameter `0.37`
  - `TFBGA180 (SOT640-1)`:
    - ball pitch `0.5`
    - ball diameter `0.3`
    - PCB land pad diameter `0.25`
    - solder mask diameter `0.36`
  - `LFBGA320`:
    - ball pitch `0.5`
    - ball diameter `0.3`
    - BGA substrate land diameter `0.25`
    - PCB land pad diameter `0.25`
    - solder mask diameter `0.36`

## Conditions And Methods

- Treat this card as a package-scoped footprint example set from one manufacturer application note.
- Keep the rows attached to the named NXP package families.
- Use this card when a prompt needs real primary-source BGA footprint numbers and can stay inside vendor/package scope.
- Use this card to challenge the handbook's apparent generic `pitch -> pad diameter` framing by showing that the same pitch can map to different PCB land pad diameters depending on package family and routing assumptions.

## Limits And Non-Claims

- This card does not authorize a universal `BGA pitch -> pad diameter` conversion rule.
- It does not authorize handbook rows for `1.5`, `1.27`, `0.75`, or `0.4` pitch where no matched primary source was landed here.
- It does not authorize the handbook's `MIN / MAX / recommended` framing as generic standards truth.
- It does not authorize cross-vendor manufacturing limits, assembly yield expectations, or routing guarantees.
- It does not authorize package-library defaults outside the named NXP package examples.

## Relationship To Local PCB资料 Intake

- This card partially replaces the `P4-215C2` handbook `bga pitch-to-pad-diameter table` claim inventory.
- The handbook table remains useful only as claim inventory for these visible rows:
  - `1.50`
  - `1.27`
  - `1.00`
  - `0.80`
  - `0.75`
  - `0.65`
  - `0.50`
  - `0.40`
- After this landing, only the `1.0`, `0.8`, `0.65`, and `0.5` pitch classes have primary-source-backed partial replacement here, and even those remain package-scoped rather than universal.

## Provenance

- origin batch:
  - `/code/blogs/tmps/PCB资料`
- motivating secondary-PDF candidate:
  - `P4-215C2` page-28 `bga pitch-to-pad-diameter table`
- authority replacement used here:
  - official NXP `AN10778` `Table 2`
- exact-data shape:
  - vendor-scoped named-package BGA footprint examples

## Source Links

- https://www.nxp.com/docs/en/application-note/AN10778.pdf
