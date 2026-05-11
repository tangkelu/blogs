---
fact_id: "methods-ti-bga-pad-geometry-guidelines-1p27-and-1p0-mm-pitch"
title: "TI BGA pad geometry values are reusable only as 1.27 mm and 1.0 mm pitch NSMD/SMD guideline rows"
topic: "TI BGA pad geometry guidelines for 1.27 mm and 1.0 mm pitch"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-05-07"
exact_data_class: "part_scoped_exact_data"
scope_type: "vendor_scoped_bga_pad_geometry_guidelines"
canonical_unit_policy: "Preserve original TI millimeter values and the NSMD/SMD distinction. Do not normalize them into a generic vendor-neutral BGA pitch conversion table."
source_ids:
  - "ti-an1126-bga-pad-geometry-guidelines"
tags: ["ti", "bga", "pad-geometry", "nsmd", "smd", "pcb-pad-diameter", "1.27-mm-pitch", "1.0-mm-pitch", "exact-data"]
---

# Canonical Summary

> TI's `AN-1126` is strong enough to support one narrow exact-data layer for `C2-R1`: the local corpus may reuse TI's printed `1.27 mm` and `1.0 mm` BGA pad-geometry guideline rows when the `NSMD` versus `SMD` land-pattern distinction is preserved. This card is a vendor-scoped guideline example only. It does not authorize a universal `BGA pitch -> pad diameter` table.

## Exact Data Scope

- exact for:
  - TI's printed `Table 1` rows
  - `1.27 mm` and `1.0 mm` pitch classes only
  - the `NSMD` versus `SMD` distinction
  - TI's printed solder ball, PCB pad, and solder mask opening diameters
- not exact for:
  - `0.75 mm`, `0.65 mm`, `0.5 mm`, `0.4 mm`, or `1.5 mm` generic pitch rules
  - all vendors
  - all BGA package families
  - handbook `MIN / MAX / recommended` framing

## Admitted Data

- TI prints these `1.27 mm pitch` rows:
  - `NSMD`:
    - solder ball diameter `0.75 mm`
    - PCB pad diameter `0.64 mm`
    - solder mask opening diameter `0.78 mm`
  - `SMD`:
    - solder ball diameter `0.75 mm`
    - PCB pad diameter `0.78 mm`
    - solder mask opening diameter `0.64 mm`
- TI prints these `1.0 mm pitch` rows:
  - `NSMD`:
    - solder ball diameter `0.63 mm`
    - PCB pad diameter `0.46 mm`
    - solder mask opening diameter `0.60 mm`
  - `SMD`:
    - solder ball diameter `0.63 mm`
    - PCB pad diameter `0.60 mm`
    - solder mask opening diameter `0.46 mm`
- TI states `NSMD` is preferred.

## Conditions And Methods

- Treat this card as one TI package-layout guideline card for BGA pad geometry.
- Keep the `NSMD` versus `SMD` distinction attached to every value.
- Use this card when a prompt needs a primary-source `1.27 mm` or `1.0 mm` pitch pad-geometry example and can stay inside TI's guideline framing.
- Pair this card with [nxp-bga-footprint-pitch-and-pcb-land-pad-examples.md](/code/blogs/llm_wiki/facts/methods/nxp-bga-footprint-pitch-and-pcb-land-pad-examples.md) when the prompt benefits from seeing both package-scoped and land-pattern-scoped primary-source evidence.

## Limits And Non-Claims

- This card does not authorize a universal BGA conversion table.
- It does not authorize handbook `1.5`, `0.75`, `0.65`, `0.5`, or `0.4` pitch rows by itself.
- It does not authorize cross-vendor assembly yield, routing success, or manufacturability guarantees.
- It does not authorize removing the `NSMD/SMD` context from the values.

## Relationship To Local PCB资料 Intake

- This card replaces the `1.27 mm` handbook pitch pressure with a primary-source TI row set.
- It also provides a second primary-source `1.0 mm` row set that differs in shape from the handbook's simple `MIN / MAX / recommended` framing.
- Together with `P4-250`, the local batch now has stronger primary-source support for:
  - `1.27 mm`
  - `1.0 mm`
  - `0.8 mm`
  - `0.65 mm`
  - `0.5 mm`
- `1.5 mm`, `0.75 mm`, and `0.4 mm` remain unreplaced by this card.

## Provenance

- origin batch:
  - `/code/blogs/tmps/PCB资料`
- motivating secondary-PDF candidate:
  - `P4-215C2` page-28 `bga pitch-to-pad-diameter table`
- authority replacement used here:
  - official TI `AN-1126` `Table 1`
- exact-data shape:
  - vendor-scoped BGA pad-geometry guideline rows

## Source Links

- https://www.ti.com/lit/pdf/snoa021
