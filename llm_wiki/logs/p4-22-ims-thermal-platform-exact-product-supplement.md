# P4-22 IMS Thermal Platform Exact-Product Supplement

Date: 2026-04-27

## Purpose

This supplement follows `P4-21` and targets the `IMS / thermal platform lane` from the `P4-20` layer-count coverage map.

The goal is to add exact-product thermal-platform material values that can support MCPCB, metal-core PCB, high-thermal PCB, LED, inverter, charger, and power-module writing without turning material datasheets into board-level thermal guarantees.

It does not write or rewrite blogs.

## Starting Gap

From `logs/p4-20-layer-count-claim-coverage-map.md`:

- Product-grade IMS / metal-core / thermally conductive dielectric anchors were still thin.
- `16-layer` and thermal-platform style drafts need exact-product rows if they keep numeric thermal comparisons.

## Landed Source Records

- `sources/registry/materials/ventec-vt-4bc-datasheet.md`
- `sources/registry/materials/ventec-vt-4bd-datasheet.md`

Existing source used as the baseline:

- `sources/registry/materials/ventec-vt-4b7-datasheet.md`
- `sources/registry/materials/ventec-ims-family-overview.md`

## Landed Fact Cards

- `facts/materials/ventec-vt-4bc.md`
- `facts/materials/ventec-vt-4bd.md`
- `facts/materials/parameter-scope-ventec-ims-material-values.md`

Existing fact used as the baseline:

- `facts/materials/ventec-vt-4b7.md`

## Claim-Family Impact

Disposition changes from `thin IMS product-grade support` to `partially_covered/source_scoped` for Ventec IMS material examples.

Allowed use:

- exact-product material rows for Ventec `VT-4B7`, `VT-4BC`, and `VT-4BD`
- material-level thermal conductivity, dielectric thickness, thermal impedance, `Tg`, `Td`, `Dk`, and `Df` values when product, method, thickness, and typical-data disclaimers are preserved
- MCPCB / metal-core / high-thermal platform examples in conservative blogs

Blocked use:

- board-level junction-temperature, thermal-resistance, LED-lifetime, inverter-reliability, or power-module qualification promises
- HIL or APT stocking, procurement, base-metal, copper-weight, dielectric-thickness, lead-time, cost, yield, or fabrication-capability claims
- supplier-neutral IMS comparison tables beyond the current Ventec exact-product scope
- automotive, medical, aerospace, military, or industrial compliance proof

## Net Result

This batch improves the thermal-platform data layer from one IMS product example to a small exact-product Ventec IMS material ladder:

- `VT-4B7`: `7.0 W/mK` class exact-product anchor
- `VT-4BC`: `10 W/mK` class exact-product anchor
- `VT-4BD`: `16 W/mK` class exact-product anchor, refresh-required for public comparison because the verified URL is localized

The batch still does not unlock generic thermal-platform superiority claims or finished-board thermal performance guarantees.
