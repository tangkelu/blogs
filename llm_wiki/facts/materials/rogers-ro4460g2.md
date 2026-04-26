---
fact_id: "materials-rogers-ro4460g2"
title: "Rogers RO4460G2 exact-product bondply card"
topic: "RO4460G2"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-25"
source_ids:
  - "rogers-ro4400-bondply-datasheet"
  - "rogers-ro4400-bondply-page"
tags: ["rogers", "ro4460g2", "bondply", "ro4400", "hybrid-stackup", "exact-product", "materials"]
---

# Canonical Summary

> `RO4460G2` is an official Rogers exact-product bondply with a high-`Dk` bonding-layer profile and condition-bound datasheet values that must remain separate from both `RO4450F` and Rogers RF core-laminate rows.

## Stable Facts

- Rogers publishes an official `RO4400 Series Bondply` datasheet that includes `RO4460G2` as a named exact product.
- The datasheet describes `RO4460G2` as a `6.15 Dk` bonding layer inside the `RO4400` bondply family.
- `Dielectric constant` is `6.15 ± 0.15` at `10 GHz` by `IPC-TM-650 2.5.5.5` under `23 C @ 50% RH`.
- `Dissipation factor` is `0.004` at `10 GHz` by `IPC-TM-650 2.5.5.5` under `23 C @ 50% RH`.
- `Volume resistivity` is `9.1 x 10^8 Mohm-cm` by `IPC-TM-650 2.5.17.1` under `C-96/35/90`.
- `Surface resistivity` is `1.53 x 10^8 Mohm` in `X,Y` by `IPC-TM-650 2.5.17.1` under `C-96/35/90`.
- `Electrical strength` is `1000 V/mil` in `Z` by `IPC-TM-650 2.5.6.2` under `D-48/50`.
- `Td` is `405 C` by `IPC-TM-650 2.3.40` at `5% weight loss` after `2 hrs @ 105 C`.
- `Tg` is `170 C` by `IPC-TM-650 2.4.24.5` with `TMA A`.
- `CTE-x` is `15 ppm/C`, `CTE-y` is `18 ppm/C`, and `CTE-z` is `43 ppm/C` from `-55 C to 288 C` by `IPC-TM-650 2.4.41`.
- `Thermal conductivity` is `0.67 W/(m.K)` in the `z` direction at `80 C` by `ASTM D5470`.
- `Copper peel strength after thermal stress` is `1.04 N/mm (5.0 lbs/in)` in `Z` with `35 um foil` after `10s @ 288 C` by `IPC-TM-650 2.4.8`.
- `Resin content` is `79`.
- `Flammability` is `UL 94 V-0`.
- `Moisture absorption` is `0.05%` by `IPC-TM-650 2.6.2.1` under `D24/23`.
- `Lead free process compatible` is listed as `Yes`.

## Conditions And Methods

- Keep every value tied to the official `RO4400 Series Bondply` datasheet and its stated method, direction, and condition.
- Treat all listed values as typical datasheet values rather than universal guaranteed specification limits.
- Keep `RO4460G2` separate from `RO4450F`; they are distinct bondply products with different `Dk`, thermal, and peel-strength profiles.
- Use this card only when a draft explicitly needs a Rogers high-`Dk` bondply row in a hybrid or multilayer RF context.

## Limits And Non-Claims

- This card does not let `RO4460G2` values stand in for `RO4003C`, `RO4350B`, `RO4835`, or other Rogers core laminates.
- It does not prove a complete hybrid stackup recipe, lamination window, board-level impedance outcome, or via-reliability result.
- It does not prove that a draft should default to a `6.15 Dk` bondply.
- It does not turn family or application wording into generic manufacturability, stock, or capability claims.

## Source Links

- https://rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/data-sheets/ro4400-series-bondply-data-sheet---ro4450f-and-ro4460g2-bondply.pdf
- https://www.rogerscorp.com/advanced-electronics-solutions/prepregs-and-bondplys
