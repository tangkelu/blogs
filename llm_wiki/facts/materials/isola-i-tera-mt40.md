---
fact_id: "materials-isola-i-tera-mt40"
title: "I-Tera MT40 baseline material card"
topic: "I-Tera MT40"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-25"
source_ids: ["isola-i-tera-mt40-datasheet"]
tags: ["isola", "i-tera-mt40", "high-speed", "very-low-loss", "rf-microwave"]
---

# Canonical Summary

> I-Tera MT40 is an Isola very low-loss laminate and prepreg system positioned for high-speed digital and RF/microwave designs that need stable dielectric behavior across frequency and temperature without PTFE-style through-hole processing requirements.

## Stable Facts

- Isola describes I-Tera MT40 as a `Very Low-Loss Laminate and Prepreg`.
- The public datasheet headline block states `Tg 215 C`, `Td 360 C`, `Dk 3.45`, and `Df 0.0031`.
- The same datasheet identifies I-Tera MT40 against `IPC-4103 /17`, `IPC-4101 /102`, and UL file number `E41625`.
- Isola states I-Tera MT40 has a dielectric constant that is stable from `-55 C` to `+125 C` up to `W-band` frequencies.
- The typical-values table lists `Tg 215 C` by `DSC`, `Tg 230 C` by `DMA`, and `Tg 210 C` by `TMA`.
- The same table lists `Td 360 C` by `TGA @ 5% weight loss` and `T260 / T288 >60 minutes` by `TMA`.
- The same table lists `Dk 3.45` at `2 GHz`, `5 GHz`, and `10 GHz` by `IPC-TM-650 2.5.5.5`.
- The same table lists `Df 0.0031` at `2 GHz`, `5 GHz`, and `10 GHz` by Bereskin stripline.
- The typical-values table lists `Z-axis CTE` as `55 ppm/C` pre-Tg, `290 ppm/C` post-Tg, and `2.8%` total expansion from `50 to 260 C`, plus `X/Y-axis CTE pre-Tg 12 ppm/C`.
- The same table lists thermal conductivity `0.61 W/m·K`, peel strength `1.0 N/mm (5.7 lb/inch)` for `1 oz. EDC foil`, and CTI `Class 3`.
- Isola markets I-Tera MT40 as CAF resistant, lead-free assembly compatible, FR-4 process compatible, multiple reflow capable, and compatible with multiple lamination cycles.

## Conditions And Methods

- Keep Dk / Df values tied to the Isola datasheet and the stated frequency points.
- Keep thermal values tied to the listed `DSC`, `DMA`, `TMA`, and `TGA` methods.
- Treat high-speed digital and RF/microwave application framing as manufacturer positioning, not as proof of finished-board channel compliance.

## Limits And Non-Claims

- This card does not prove I-Tera MT40 meets a specific insertion-loss, PCIe, or 56G/112G channel budget in a finished stackup.
- It does not claim I-Tera MT40 is a drop-in substitute for every PTFE, Rogers, or Panasonic laminate.
- It does not collapse all laminate and prepreg constructions into one universal electrical value.
- It does not replace stackup-specific SI modeling, copper-roughness handling, or fabrication validation.

## Open Questions

- Add a future comparison card for `I-Tera MT40 vs Tachyon 100G vs MEGTRON 7` if the high-speed digital ladder needs a tighter very-low-loss comparison set.

## Source Links

- https://www.isola-group.com/wp-content/uploads/data-sheets/i-tera-mt40.pdf
