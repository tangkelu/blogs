---
fact_id: "materials-isola-i-speed"
title: "I-Speed baseline material card"
topic: "I-Speed"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-25"
source_ids: ["isola-i-speed-datasheet"]
tags: ["isola", "i-speed", "high-speed", "low-loss", "fr-4-compatible"]
---

# Canonical Summary

> I-Speed is an Isola low-loss epoxy laminate and prepreg system positioned for multilayer PWBs that need stronger thermal and electrical performance than baseline FR-4-family materials while remaining FR-4 process compatible.

## Stable Facts

- Isola describes I-Speed as a `Low Loss, Epoxy Laminate and Prepreg`.
- The public datasheet headline block states `Tg 180 C`, `Td 360 C`, `Dk 3.63`, and `Df 0.0060`.
- The same datasheet identifies I-Speed against `IPC-4101 /98 /99 /101 /126` and UL file number `E41625`.
- The typical-values table lists `Tg 180 C` by `DSC` and `Tg 195 C` by `DMA`.
- The same table lists `Td 360 C` by `TGA @ 5% weight loss` and `T260 / T288 >60 minutes` by `TMA`.
- The typical-values table lists Dk by `IPC-TM-650 2.5.5.9` Bereskin stripline as `3.65 at 1 GHz`, `3.64 at 2 GHz`, `3.63 at 5 GHz`, and `3.63 at 10 GHz`.
- The same table lists Df by `IPC-TM-650 2.5.5.9` Bereskin stripline as `0.0057 at 1 GHz`, `0.0059 at 2 GHz`, `0.0059 at 5 GHz`, and `0.0060 at 10 GHz`.
- The same table lists `Z-axis CTE` as `45 ppm/C` pre-Tg, `230 ppm/C` post-Tg, and `2.5%` total expansion from `50 to 260 C`, plus `X/Y-axis CTE pre-Tg 16 ppm/C`.
- The datasheet also lists thermal conductivity `0.4 W/m·K`, moisture absorption `0.061%`, and UL 94 `V-0` flammability.
- Isola markets I-Speed as lead-free assembly compatible, FR-4 process compatible, compatible with multiple lamination cycles, and HDI technology compatible.

## Conditions And Methods

- Keep all electrical values tied to the Isola datasheet and its stated `IPC-TM-650 2.5.5.9` Bereskin stripline method.
- Keep thermal values tied to the listed methods such as `DSC`, `DMA`, `TGA`, and `TMA`.
- Treat I-Speed application and process language as manufacturer positioning, not as automatic approval for any stackup.

## Limits And Non-Claims

- This card does not claim one I-Speed value applies to every construction, copper option, or laminate/prepreg build.
- It does not prove a specific channel budget, insertion-loss target, or high-speed reach on a finished board.
- It does not make I-Speed a universal replacement for all FR-4, MEGTRON, PTFE, or other low-loss materials.
- It does not replace stackup-specific impedance, loss, thermal, or reliability modeling.

## Open Questions

- Add a future comparison card for `I-Speed vs FR408HR vs MEGTRON 4` if H1 follow-on work needs a tighter mid-loss digital-material ladder.

## Source Links

- https://www.isola-group.com/wp-content/uploads/data-sheets/i-speed-laminate-and-prepreg.pdf
