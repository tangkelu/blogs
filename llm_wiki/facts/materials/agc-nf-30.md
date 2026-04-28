---
fact_id: "materials-agc-nf-30"
title: "AGC NF-30 baseline material card"
topic: "NF-30"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["agc-nf-30-datasheet"]
tags: ["agc", "nf-30", "ptfe", "ceramic-filled", "non-reinforced", "mmwave", "automotive-radar", "microvia"]
---

# Canonical Summary

> NF-30 is an AGC non-reinforced ceramic-filled PTFE composite positioned for microwave and mmWave designs, including automotive radar and passive RF components, with a datasheet that includes both 10 GHz IPC values and 77 GHz microstrip-resonator context.

## Stable Facts

- AGC describes NF-30 as a copper-clad, non-reinforced ceramic-filled PTFE composite.
- The TDS frames applications around automotive radar sensors, aerospace components, GPS antennas, and passive components such as dividers, filters, and couplers.
- The TDS states NF-30 offers stable performance over a wide frequency range, especially the `77-79 GHz` range.
- The TDS lists `Dk 3.00 +/- 0.04 at 10 GHz` by `IPC-650 2.5.5.5.1 (Mod.)`.
- The same TDS lists `Dk 2.98 at 77 GHz` by microstrip resonator.
- The same TDS lists `Df 0.0013 at 10 GHz` by `IPC-650 2.5.5.5.1 (Mod.)`.
- The same TDS lists thermal coefficient of Dk `-4.07 ppm/C` from `-55 C to 150 C` by `IPC-650 2.5.5.5`.
- The same TDS lists `Td 515 C` at `2%` weight loss and `Td 530 C` at `5%` weight loss.
- The same TDS lists unclad thermal conductivity `0.5 W/mK` by `IPC-650 2.4.50`.
- The same TDS lists CTE from `50 C to 150 C` of `X 11~15 ppm/C`, `Y 11~15 ppm/C`, and `Z 30 ppm/C`.
- The same TDS lists `T288 >120 min`, moisture absorption `0.05 wt.%`, methylene chloride resistance `0.21% wt. chg.`, lead-free process compatibility `Yes`, and flammability `V-0`.
- The TDS states NF-30 can be manufactured in increments of `0.005 in / 0.127 mm` and lists standard panel size `18 in x 24 in / 457 mm x 610 mm`.

## Conditions And Methods

- Keep `10 GHz` IPC values separate from the `77 GHz` microstrip-resonator Dk value.
- Do not extract exact graph values from the response plots unless a separate tabulated source is available.
- Treat desmear, drilling, plating, and CO2 laser ablation notes as AGC processing guidance, not proof of any fabricator's process capability.
- Treat the values as typical datasheet values, not guaranteed specification limits.

## Limits And Non-Claims

- This card does not prove a finished board meets automotive radar, aerospace, GPS, mmWave, insertion-loss, or antenna-performance requirements.
- It does not prove laser-microvia yield, plasma desmear capability, dense PTH manufacturability, or multilayer reliability for a supplier or design.
- It does not prove APT, HIL, or any other supplier capability, certification, yield, lead time, or qualification status.

## Open Questions

- Whether to add NF-30 to an mmWave material selector alongside Rogers, Taconic, Shengyi, and AGC RF rows after those branches are recovered.

## Source Links

- https://www.agc-multimaterial.com/agc-downloads/AGC_NF-30_TDS.pdf
