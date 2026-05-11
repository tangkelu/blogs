---
fact_id: "methods-intel-bga-land-pad-guidelines-common-pitches-and-vbga"
title: "Intel BGA land-pad values are reusable only as Intel package-guideline rows plus one 0.4 mm VBGA example"
topic: "Intel BGA land pad guidelines for common pitches and 0.4 mm VBGA"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-08"
exact_data_class: "part_scoped_exact_data"
scope_type: "vendor_scoped_bga_land_pad_guidelines"
canonical_unit_policy: "Preserve original Intel millimeter values, package-family labels, and the SMD versus NSMD distinction. Do not normalize them into a vendor-neutral BGA pitch conversion table."
source_ids:
  - "intel-an114-bga-land-pad-dimensions"
tags: ["intel", "bga", "vbga", "wlcsp", "ubga", "mbga", "land-pad", "smd", "nsmd", "exact-data"]
---

# Canonical Summary

> Intel's `AN 114` is strong enough to support one more narrow exact-data layer for the `PCB资料` package lane: the local corpus may reuse Intel's printed BGA land-pad recommendation rows when the package-family label and `SMD/NSMD` framing stay attached. This card is vendor-scoped guidance only. It does not authorize the handbook's generic `pitch -> pad diameter` table as a universal industry rule.

## Exact Data Scope

- exact for:
  - Intel's printed `SMD` and `NSMD` recommendation rows in `AN 114`
  - Intel's package-family labels such as `PBGA`, `UBGA`, `MBGA`, and `VBGA`
  - the separate `0.4 mm VBGA (WLCSP)` row
- not exact for:
  - all vendors
  - all packages at the same pitch
  - handbook `MIN / MAX / recommended` generic framing
  - residual `0.75 mm` or `1.50 mm` handbook pitch classes

## Admitted Data

- Intel prints these `1.27 mm` rows:
  - `PBGA / SBGA / TBGA`:
    - BGA pad opening `0.60`
    - recommended `SMD` pad size `0.60`
    - recommended `NSMD` pad size `0.51`
  - `flip-chip`:
    - BGA pad opening `0.65`
    - recommended `SMD` pad size `0.65`
    - recommended `NSMD` pad size `0.55`
- Intel prints these `1.00 mm` rows:
  - `wire-bond`:
    - BGA pad opening `0.45`
    - recommended `SMD` pad size `0.45`
    - recommended `NSMD` pad size `0.38`
  - `flip-chip`:
    - BGA pad opening `0.55`
    - recommended `SMD` pad size `0.55`
    - recommended `NSMD` pad size `0.47`
- Intel prints these `0.80 mm` rows:
  - `UBGA (wire-bond)`:
    - BGA pad opening `0.40`
    - recommended `SMD` pad size `0.40`
    - recommended `NSMD` pad size `0.34`
  - `UBGA (flip-chip)`:
    - BGA pad opening `0.425` or `0.45`
    - recommended `SMD` pad size `0.425` or `0.45`
    - recommended `NSMD` pad size `0.36` or `0.38`
- Intel prints this `0.50 mm MBGA` row:
  - BGA pad opening `0.30`
  - recommended `SMD` pad size `0.27`
  - recommended `NSMD` pad size `0.26`
- Intel prints this `0.4 mm VBGA (WLCSP)` row:
  - `NSMD` PCB Cu pad size `0.22`
  - `NSMD` solder mask opening `0.32`
  - `SMD` PCB Cu pad size `0.32`
  - `SMD` solder mask opening `0.22`

## Conditions And Methods

- Treat this card as Intel package-layout guidance, not as a generic standards table.
- Keep every value attached to the Intel package-family row and the `SMD/NSMD` distinction.
- Use this card when a prompt needs one more official owner-scoped BGA or `0.4 mm VBGA/WLCSP` land-pad example.
- Pair this card with:
  - [nxp-bga-footprint-pitch-and-pcb-land-pad-examples.md](/code/blogs/llm_wiki/facts/methods/nxp-bga-footprint-pitch-and-pcb-land-pad-examples.md)
  - [ti-bga-pad-geometry-guidelines-1p27-and-1p0-mm-pitch.md](/code/blogs/llm_wiki/facts/methods/ti-bga-pad-geometry-guidelines-1p27-and-1p0-mm-pitch.md)
  - [microchip-csp-bga-solder-land-and-pitch-examples.md](/code/blogs/llm_wiki/facts/methods/microchip-csp-bga-solder-land-and-pitch-examples.md)

## Limits And Non-Claims

- This card does not authorize a universal cross-vendor `pitch -> pad diameter` table.
- It does not replace the residual handbook `0.75 mm` or `1.50 mm` pitch classes.
- It does not authorize package-library defaults outside Intel's documented package guidance.
- It does not authorize assembly-yield, routing-yield, or solder-joint reliability guarantees outside Intel's documented context.

## Relationship To Local PCB资料 Intake

- This card adds another official replacement surface for the blocked handbook `BGA pitch-to-pad-diameter` table from page `28`.
- It is especially useful for the `0.4 mm` package class because the repo now has a direct official `VBGA/WLCSP` row instead of only secondary-PDF pressure.
- It does not close the remaining residual handbook pitch classes `0.75 mm` and `1.50 mm`.

## Provenance

- origin batch:
  - `/code/blogs/tmps/PCB资料`
- motivating secondary-PDF candidate:
  - `P4-215C2` page-28 `bga pitch-to-pad-diameter table`
- authority replacement used here:
  - official Intel `AN 114` section `1.3.1 Surface Land Pad Dimension`
- exact-data shape:
  - vendor-scoped BGA and VBGA land-pad guideline rows

## Source Links

- https://www.intel.co.jp/content/www/jp/ja/docs/programmable/683481/current/surface-land-pad-dimension
