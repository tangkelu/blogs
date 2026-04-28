---
fact_id: "materials-agc-n7000-2ht"
title: "AGC N7000-2HT laminate with N7000-3 prepreg polyimide material card"
topic: "N7000-2HT"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["agc-n7000-2ht-datasheet"]
tags: ["agc", "n7000-2ht", "n7000-3", "polyimide", "high-temperature", "laminate", "prepreg", "severe-condition"]
---

# Canonical Summary

> N7000-2HT is an AGC toughened polyimide laminate paired in the TDS with N7000-3 prepreg. The row supports exact-product high-temperature material framing, not finished-board severe-condition qualification.

## Stable Facts

- AGC describes N7000-2HT laminate and N7000-3 prepreg as a toughened polyimide laminate and prepreg material system.
- The TDS frames applications around backplanes, fine-line surface-mount and BGA multilayers, direct chip attach, underhood automotive, and burn-in boards.
- The TDS states N7000-2HT laminate has a `UL 94 V-0` flame rating and N7000-3 prepreg has a `UL 94 V-1` flame rating.
- The TDS states the product system meets `IPC-4101 /40`, `/41`, and `/42`, complies with old `GIJ` and `GIL` specifications, and lists UL file number `E36295`.
- The TDS lists dielectric constant of `3.5 at 2.5 GHz` and `3.5 at 10 GHz` by `IPC-TM-650 2.5.5.5`.
- The same TDS lists dissipation factor of `0.009 at 2.5 GHz` and `0.009 at 10 GHz`.
- The same TDS lists volume resistivity `10^7 MOhm-cm` at `C-96 / 35 / 90` and `10^7 MOhm-cm` at `E-24 / 125`.
- The same TDS lists surface resistivity `10^7 MOhm` at `C-96 / 35 / 90` and `10^7 MOhm` at `E-24 / 125`.
- The same TDS lists electric strength `4.7 x 10^4 V/mm` / `1200 V/mil`.
- The same TDS lists Tg `260 C` by DSC.
- The same TDS lists degradation temperature `376 C` at `5%` weight loss and `T-260 120+ minutes`.
- The same TDS lists thermal conductivity `0.45 W/mK`.
- The same TDS lists X/Y CTE from `-40 C to +125 C` of `9 / 12 ppm/C` and Z-axis expansion at `43% RC` of `< 2.5%` from `50 C to 260 C`.
- The same TDS lists moisture absorption `0.35 wt.%`.
- The TDS states N7000-2HT can be manufactured in laminate thickness from `2 mil / 0.05 mm` and up.

## Conditions And Methods

- Preserve the laminate/prepreg pairing: `N7000-2HT laminate` with `N7000-3 prepreg`.
- Keep `2.5 GHz` and `10 GHz` electrical values separate.
- Keep `43% RC` attached to the Z-axis expansion row.
- Treat all listed values as typical datasheet values, not guaranteed specification limits.

## Limits And Non-Claims

- This card does not prove finished-board backplane, BGA multilayer, direct-chip-attach, underhood automotive, burn-in-board, or severe-condition qualification.
- It does not prove a generic multilayer recipe, lamination count, stackup success, plated-through-hole reliability, or high-temperature lifetime.
- It does not prove APT, HIL, or any other supplier capability, certification, yield, lead time, stock, price, or qualification status.
- It does not replace or merge the separate `materials-agc-n7000-3` or `materials-agc-n7000-3f` cards.

## Source Links

- https://www.agc-multimaterial.com/agc-downloads/AGC_N7000-2HT_TDS.pdf
