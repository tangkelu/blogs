---
source_id: "agc-meteorwave-4000m-datasheet"
title: "AGC METEORWAVE 4000M TDS"
organization: "AGC Inc."
source_type: "datasheet"
url: "https://www.agc-multimaterial.com/agc-downloads/AGC_METEORWAVE_4000M_TDS.pdf"
jurisdiction: "global"
published_at: "2024-11"
checked_at: "2026-04-28"
trust_tier: "t1"
stability: "semi_stable"
must_refresh: false
topic_tags: ["agc", "meteorwave-4000m", "ultra-low-loss", "laminate", "automotive-radar", "caf", "datasheet"]
status: "active"
notes: "Official AGC technical data sheet for METEORWAVE 4000M high-frequency laminate. Local provenance copy observed at /code/blogs/tmps/materias_pdf/AGC_METEORWAVE_4000M_TDS.pdf during P4-33 source recovery."
---

# Source Summary

## What It Covers

- Electrical, thermal, mechanical, and physical properties for `METEORWAVE 4000M`
- High-frequency / ultra-low-loss laminate positioning for automotive radar material context
- Public processing posture, CAF framing, UL94 / IPC-4101 framing, and UL file reference

## Why It Matters

- Adds a source-backed AGC automotive-radar-oriented material row while keeping radar performance claims separate from material datasheet values.

## Extraction Notes

- Keep `10 GHz` and `77 GHz` Dk values separate.
- Preserve copper / resonator notes for `77 GHz` Dk rows instead of averaging them.
- Keep TMA and DMA Tg values separate.
- Treat 24 GHz / 77 GHz radar wording as material-positioning context, not proof of finished-board radar performance, antenna performance, or automotive qualification.
- The datasheet states all test data are typical values, not specification values.

## Refresh Notes

- Refresh before using exact values in comparison tables or customer-facing evidence packs.
