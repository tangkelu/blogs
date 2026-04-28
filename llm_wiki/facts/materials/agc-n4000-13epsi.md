---
fact_id: "materials-agc-n4000-13epsi"
title: "AGC N4000-13 EP SI lead-free signal-integrity epoxy material card"
topic: "N4000-13 EP SI"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["agc-n4000-13epsi-datasheet"]
tags: ["agc", "n4000-13epsi", "epoxy", "lead-free", "signal-integrity", "high-speed", "laminate", "prepreg"]
---

# Canonical Summary

> N4000-13 EP SI is an AGC lead-free high-speed multifunctional epoxy laminate and prepreg that uses SI glass for signal-integrity and controlled-impedance material positioning. Its values must remain exact-product and condition scoped.

## Stable Facts

- AGC describes N4000-13 EP SI as an enhanced epoxy resin system engineered for lead-free requirements.
- The TDS states N4000-13 EP SI uses `SI` glass for applications requiring signal integrity and precise impedance control.
- The TDS frames applications around high-speed storage networks, internet switches / routing systems, wireless communication infrastructure, and backplanes.
- The TDS lists dielectric constant at `50% resin content` of `3.2 at 2.5 GHz` by split-post cavity and `3.2 at 10 GHz` by stripline / `IPC-TM-650 2.5.5.5`.
- The same TDS lists dissipation factor at `50% resin content` of `0.008 at 2.5 GHz` by split-post cavity and `0.008 at 10 GHz` by stripline / `IPC-TM-650 2.5.5.5`.
- The same TDS lists volume resistivity `10^8 MOhm-cm` at `C-96 / 35 / 90` and `10^8 MOhm-cm` at `E-24 / 125`.
- The same TDS lists surface resistivity `10^7 MOhm` at `C-96 / 35 / 90` and `10^7 MOhm` at `E-24 / 125`.
- The same TDS lists electric strength `3.9 x 10^4 V/mm` / `1000 V/mil`.
- The same TDS lists Tg `240 C` by DMA `Tan d Peak`.
- The same TDS lists degradation temperature `350 C` at `5%` weight loss, `T-260 30+ minutes`, and `T-288 10+ minutes`.
- The same TDS lists thermal conductivity `0.294 W/mK`.
- The same TDS lists X/Y CTE from `-40 C to +125 C` of `9 / 13 ppm/C`, Z-axis CTE Alpha 1 of `65 ppm/C`, Z-axis CTE Alpha 2 of `275 ppm/C`, and Z-axis expansion `3.4%`.
- The same TDS lists moisture absorption `0.1 wt.%`.
- The TDS states N4000-13 EP SI meets `UL 94V-0` and `IPC-4101 /29`, `/98`, `/99`, and `/101`, with UL file number `E36295`.
- The TDS states N4000-13 EP SI can be manufactured in laminate thickness from `2 mil / 0.05 mm` and up.

## Conditions And Methods

- Preserve `50% resin content` when using the Dk / Df rows.
- Keep `2.5 GHz` split-post-cavity and `10 GHz` stripline rows separate.
- Treat all listed values as typical datasheet values, not guaranteed specification limits.
- Do not substitute N4000-13 EP SI values for `N4000-13`, `N4000-13 EP`, or `N4000-13 SI`.

## Limits And Non-Claims

- This card does not prove finished-board impedance tolerance, insertion-loss budget, storage-network performance, switch/router performance, backplane performance, RF performance, or wireless-infrastructure qualification.
- It does not prove lead-free assembly success, maximum reflow survival, CAF reliability, or released-lot acceptance for a specific stackup or supplier.
- It does not prove APT, HIL, or any other supplier capability, certification, yield, lead time, stock, price, or qualification status.
- It does not provide a reusable lamination recipe for suppliers or designs.

## Source Links

- https://www.agc-multimaterial.com/agc-downloads/AGC_N4000-13EPSI_TDS.pdf
