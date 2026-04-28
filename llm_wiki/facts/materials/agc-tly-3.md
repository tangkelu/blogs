---
fact_id: "materials-agc-tly-3"
title: "AGC TLY-3 very-low-Dk PTFE laminate material card"
topic: "TLY-3"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["agc-tly-3-datasheet"]
tags: ["agc", "tly-3", "ptfe", "very-low-dk", "low-loss", "rf-materials", "laminate"]
---

# Canonical Summary

> TLY-3 is an AGC very-low-Dk woven-glass-reinforced PTFE laminate. Its 77 GHz and OEM comparison wording must remain application / test-vehicle context, not finished-board performance proof.

## Stable Facts

- AGC identifies TLY-3 laminates as very-low-Dk materials manufactured with very lightweight woven fiberglass.
- AGC frames TLY-3 around automotive radar, satellite / cellular communications, power amplifiers, LNBs / LNAs / LNCs, aerospace, and Ka / E / W band contexts.
- At `10 GHz`, the TDS lists dielectric constant `2.33 +/- 0.02` by `IPC-650 2.5.5.5`.
- At `10 GHz`, the TDS lists dissipation factor `0.0012` by `IPC-650 2.5.5.5`.
- The same TDS lists thermal conductivity `0.22 W/mK` by `ASTM F 433`.
- The same TDS lists CTE from `25 C to 260 C` as X `26 ppm/C`, Y `15 ppm/C`, and Z `217 ppm/C` by `ASTM D3386 (TMA)`.
- The same TDS lists specific gravity `2.19`, moisture absorption `0.02%`, and NASA outgassing rows of TML `0.01%`, CVCM `0.01%`, and WVR `0.01%`.
- The same TDS lists UL-94 flammability `V-0` and dimensional stability for `10 mil` material as MD `-0.038 mm/M` and CD `-0.038 mm/M`.
- The sheet lists typical thicknesses from `0.0035 in / 0.09 mm` to `0.0600 in / 1.52 mm` and multiple sheet sizes.

## Conditions And Methods

- Preserve `10 GHz` and IPC-650 `2.5.5.5` on Dk / Df values.
- Treat NASA outgassing rows as source-scoped material test values, not space qualification.
- Treat 77 GHz and drop-in / OEM comparison wording as blocked finished-board / test-vehicle context.
- Treat all data as typical values, matching the source note.

## Limits And Non-Claims

- This card does not prove automotive-radar, satellite, cellular, power-amplifier, LNB / LNA / LNC, aerospace, Ka-band, E-band, or W-band finished-board performance.
- It does not prove insertion loss, antenna performance, radar readiness, space qualification, OEM drop-in equivalence, manufacturing yield, or supplier build capability.
- It does not prove APT, HIL, or any other supplier certification, yield, price, MOQ, stock, or lead time.

## Source Links

- https://www.agc-multimaterial.com/agc-downloads/AGC_TLY-3_TDS.pdf
