---
fact_id: "materials-isola-tachyon-100g"
title: "Isola Tachyon 100G baseline material card"
topic: "Tachyon 100G"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids: ["isola-tachyon-100g-datasheet"]
tags: ["isola", "tachyon-100g", "high-speed", "ultra-low-loss", "backplane"]
---

# Canonical Summary

> Tachyon 100G is an Isola ultra-low-loss laminate and prepreg system positioned for very high-speed digital designs, especially backplanes and daughter cards that need stable electrical behavior, thermal reliability, and low-profile copper options.

## Stable Facts

- Isola describes Tachyon 100G as an `Ultra Low Loss Laminate and Prepreg`.
- The public datasheet states `Tg 215 C`, `Td 360 C`, `Dk 3.02`, and `Df 0.0021` in its headline property block.
- The datasheet positions Tachyon 100G for very high-speed digital applications up to and beyond `100 Gb/s`.
- The same datasheet states Tachyon 100G electrical properties are stable from `-55 C` to `+125 C` up to `100 GHz`.
- The typical-values table lists Dk by `IPC-TM-650 2.5.5.5` as `3.04 at 2 GHz`, `3.02 at 5 GHz`, and `3.02 at 10 GHz`.
- The same table lists Df by `IPC-TM-650 2.5.5.5` as `0.0021` at `2 GHz`, `5 GHz`, and `10 GHz`.
- The datasheet lists `IPC-4103 /17`, `IPC-4101 /102`, and UL file number `E41625`.
- Isola states Tachyon 100G supports laminate and prepreg forms, low-Dk glass, spread glass, and low-profile copper options such as HVLP / HVLP3.

## Conditions And Methods

- Keep the Dk / Df values tied to the Isola datasheet and stated IPC-TM-650 method.
- Treat application framing as manufacturer positioning, not design approval.
- Use this card for high-speed digital material selection, not as a generic RF antenna laminate default.

## Limits And Non-Claims

- This card does not prove Tachyon 100G is lower loss than every RF PTFE material.
- It does not claim one headline Dk / Df value applies to every construction or copper option.
- It does not replace stackup-level SI modeling.

## Open Questions

- Add a future comparison card for `Tachyon 100G vs MEGTRON 8 vs VT-464G` once the current batch is stable.

## Source Links

- https://www.isola-group.com/wp-content/uploads/data-sheets/tachyon-100g-laminate-and-prepreg.pdf
