---
fact_id: "materials-iteq-digital-laminate-ladder-normalization"
title: "ITEQ digital laminate ladder should stay product-specific from IT-180A through the 968 and 988 ultra-low-loss branches"
topic: "ITEQ digital laminate ladder"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-25"
source_ids:
  - "iteq-it-180a-page"
  - "iteq-it-150da-page"
  - "iteq-it-150da-datasheet"
  - "iteq-it-602g-datasheet"
  - "iteq-it-968-page"
  - "iteq-it-968-datasheet"
  - "iteq-it-968se-page"
  - "iteq-it-968se-datasheet"
  - "iteq-it-988g-page"
  - "iteq-it-988g-datasheet"
  - "iteq-it-988gl-page"
  - "iteq-it-988gl-datasheet"
  - "iteq-it-988gse-page"
  - "iteq-it-988gse-datasheet"
  - "iteq-it-988glse-page"
tags: ["iteq", "normalization", "selector", "low-loss", "very-low-loss", "ultra-low-loss", "materials"]
---

# Canonical Summary

> `llm_wiki` can now support a guarded ITEQ digital-material ladder, but it must stay product-specific: `IT-180A` as the mainstream high-Tg FR-4 anchor, `IT-150DA` as the low-loss entry step, `IT-968` and `IT-602G` as separate very-low-loss branches, and `IT-968SE / IT-988G / IT-988GL / IT-988GSE / IT-988GLSE` as exact-name ultra-low-loss rows rather than one flattened ITEQ average.

## Stable Facts

- `IT-180A` should be treated as the ITEQ mainstream high-Tg FR-4 starting point rather than as a proxy for every ITEQ FR-4 system.
- `IT-150DA` should be treated as the low-loss entry step in the current public ITEQ digital ladder.
- `IT-968` should be treated as the numerically explicit bridge from low-loss into very-low-loss ITEQ material coverage.
- `IT-602G` should remain a parallel very-low-loss branch anchor with guarded `HDI` and `multiple lamination` context rather than being forced into a pure scalar loss ranking.
- `IT-968SE`, `IT-988G`, `IT-988GL`, `IT-988GSE`, and `IT-988GLSE` should be treated as separate ultra-low-loss exact-product rows.
- A conservative same-condition ultra-low-loss ordering by current public `Df @ 10 GHz` is supportable for the current exact rows: `IT-988GL (0.0033)`, `IT-988G (0.0032)`, `IT-968SE (0.0028)`, `IT-988GLSE (0.0025)`, and `IT-988GSE (0.0022)`.
- `IT-968SE` is the lowest-`Dk` public row in this recovered ITEQ set at `Dk 2.86 @ 10 GHz, RC 70%`, while `IT-988GSE` is the lowest-`Df` public row at `Df 0.0022 @ 10 GHz, RC 70%`.
- `IT-988GL` and `IT-988G` are deceptively close electrically, but their `CTE 50-260 C` values differ at `1.7%` versus `2.5%`, so they should stay separate.
- `IT-988GLSE` and `IT-988GSE` are also deceptively close, but `IT-988GLSE` holds the lower expansion profile while `IT-988GSE` holds the stronger public `Dk/Df` endpoint.

## Conditions And Methods

- Use this card to place ITEQ grades into a guarded branch ladder before drafting any material-comparison prose.
- Keep `IT-150DA` separate from the later `968` and `988` rows because its public dielectric values are tied to `RC 50%`, while the later rows use `RC 70%`.
- Keep `IT-968` and `IT-602G` in the very-low-loss bucket, but do not write them as interchangeable because only `IT-968` currently acts as the clear numeric bridge row while `IT-602G` also carries guarded `HDI / multiple lamination` positioning.
- Keep the ultra-low-loss rows grouped only for branch placement and conservative same-condition ordering; pair this card with the exact product cards before carrying values into tables.
- Use exact grade names every time; do not rely on suffix inference to guess performance, construction, or interchangeability.

## Limits And Non-Claims

- This card does not create a universal ITEQ performance rank across every frequency, resin content, glass style, copper condition, or stackup.
- It does not make `IT-968`, `IT-968G`, and `IT-968SE` interchangeable.
- It does not make `IT-988G`, `IT-988GL`, `IT-988GSE`, and `IT-988GLSE` interchangeable.
- It does not revive unconfirmed public naming such as `IT-988SE` as a substitute for current exact-product rows.
- It does not turn `56Gbps+`, `PAM-2/PAM-4`, `100G/400G switch`, `backplane`, `HDI`, or hybrid `RF/microwave` wording into channel-budget, manufacturability, or fabricator-capability proof.
- It does not create a drop-in substitution table for other vendors' low-loss or ultra-low-loss materials.

## Source Links

- https://www.iteqcorp.com/product/product/high-tg-std-loss/?lang=en
- https://www.iteqcorp.com/product/product/high-tg-low-loss/?lang=en
- https://s3.ap-northeast-1.wasabisys.com/cdn.iteqcorp.com/2026/02/W-CTE-1002-16B_Data-sheet-IT-150DA.pdf
- https://s3.ap-northeast-1.wasabisys.com/cdn.iteqcorp.com/2026/03/W-CTE-1002-78B_Data-sheet-IT-602G.pdf
- https://www.iteqcorp.com/product/product/high-tg-very-low-loss/?lang=en
- https://s3.ap-northeast-1.wasabisys.com/cdn.iteqcorp.com/2026/02/W-CTE-1002-01B_Data-sheet-IT-968.pdf
- https://www.iteqcorp.com/product/product/high-tg-ultra-low-loss/?lang=en
- https://s3.ap-northeast-1.wasabisys.com/cdn.iteqcorp.com/2026/02/W-CTE-1002-11B_Data-sheet-IT-968SE.pdf
- https://s3.ap-northeast-1.wasabisys.com/cdn.iteqcorp.com/2026/02/W-CTE-1002-08B_Data-sheet-IT-988G.pdf
- https://s3.ap-northeast-1.wasabisys.com/cdn.iteqcorp.com/2026/03/w3YLn4xH-W-CTE-1002-65C_Data-sheet-IT-988GL.pdf
- https://s3.ap-northeast-1.wasabisys.com/cdn.iteqcorp.com/2026/02/W-CTE-1002-05B_Data-sheet-IT-988GSE.pdf
