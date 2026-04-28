---
fact_id: "materials-parameter-scope-isola-high-speed-laminate-values"
title: "Isola high-speed laminate values are datasheet-scoped material parameters"
topic: "Isola high-speed laminate parameter scope"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-27"
source_ids:
  - "isola-i-speed-datasheet"
  - "isola-tachyon-100g-datasheet"
  - "isola-astra-mt77-datasheet"
  - "isola-astra-mt77-dk-df-table"
tags: ["isola", "high-speed-materials", "parameter-scope", "dk", "df", "tg", "td", "cte"]
---

# Canonical Summary

> Isola I-Speed, Tachyon 100G, and Astra MT77 provide source-backed material values that can improve high-speed and RF material context. These values remain datasheet-scoped; they do not prove channel margin, RF performance, or factory capability on a finished board.

## Source-Backed Values

| Product | Values captured in existing material cards | Scope |
| --- | --- | --- |
| `I-Speed` | headline `Tg 180 C`, `Td 360 C`, `Dk 3.63`, `Df 0.0060`; Dk by `IPC-TM-650 2.5.5.9` Bereskin stripline: `3.65 at 1 GHz`, `3.64 at 2 GHz`, `3.63 at 5 GHz`, `3.63 at 10 GHz`; Df: `0.0057 at 1 GHz`, `0.0059 at 2 GHz`, `0.0059 at 5 GHz`, `0.0060 at 10 GHz`; Z-axis CTE `45 ppm/C` pre-Tg and `230 ppm/C` post-Tg; X/Y CTE pre-Tg `16 ppm/C`; thermal conductivity `0.4 W/m.K`; moisture absorption `0.061%`; UL 94 `V-0` | Isola I-Speed datasheet context |
| `Tachyon 100G` | headline `Tg 215 C`, `Td 360 C`, `Dk 3.02`, `Df 0.0021`; positioned for high-speed digital applications up to and beyond `100 Gb/s`; electrical properties stated stable from `-55 C` to `+125 C` up to `100 GHz`; Dk by `IPC-TM-650 2.5.5.5`: `3.04 at 2 GHz`, `3.02 at 5 GHz`, `3.02 at 10 GHz`; Df `0.0021` at `2 GHz`, `5 GHz`, and `10 GHz` | Isola Tachyon 100G datasheet context |
| `Astra MT77` | `Tg 200 C` by DSC; `Td 360 C` by TGA at 5 percent weight loss; moisture absorption `0.1%`; UL 94 `V-0`; Dk `3.00` and Df `0.0017` across published `2 GHz`, `5 GHz`, `10 GHz`, `15 GHz`, and `20 GHz` table entries for listed core thicknesses | Isola Astra MT77 datasheet plus Dk/Df table context |

## Scope And Applicability Limits

- Use `I-Speed` primarily as a low-loss FR-4-compatible digital-material context.
- Use `Tachyon 100G` primarily as an ultra-low-loss high-speed digital and backplane material context.
- Use `Astra MT77` primarily as a very-low-loss RF/microwave material context.
- Keep measurement method, frequency, and table context attached wherever captured.

## Non-Generalization

- These values do not prove a PCIe, Ethernet, optical-module, backplane, antenna, or mmWave design will pass.
- They do not prove insertion-loss, return-loss, BER, eye-mask, jitter, thermal, or reliability results on a finished assembly.
- They do not authorize substitution across Isola products or between Isola, Panasonic, Rogers, AGC, Ventec, or other material systems.
- They do not prove HIL or APT factory capability, procurement approval, cost, lead time, or yield.

## Blog Usage

- Supports `high-speed-si`, `data-center-optical-module`, `ai-server-backplane`, and `5g-telecom` empty-image families as material-parameter context only.
- Pair with high-speed SI measurement cards before discussing TDR/VNA/eye/jitter.
- Pair with RF/mmWave boundary cards before using Astra MT77 in antenna or telecom drafts.

## Source Links

- https://www.isola-group.com/wp-content/uploads/data-sheets/i-speed-laminate-and-prepreg.pdf
- https://www.isola-group.com/wp-content/uploads/data-sheets/tachyon-100g-laminate-and-prepreg.pdf
- https://isola-group.com/wp-content/uploads/data-sheets/astra-mt77.pdf
- https://www.isola-group.com/wp-content/uploads/data-sheets/astra-mt77-laminate-and-prepreg__Dk_Df_Tables.pdf
