---
fact_id: "materials-isola-fr4-to-low-loss-family-ladder"
title: "Isola now has an evidence-backed family ladder from mainstream FR-4 through lower-loss multilayer materials"
topic: "Isola FR-4 to low-loss family ladder"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids:
  - "isola-is410-datasheet"
  - "isola-370hr-datasheet"
  - "isola-fr408-datasheet"
  - "isola-fr408hr-datasheet"
  - "isola-i-speed-datasheet"
  - "isola-i-tera-mt40-datasheet"
tags: ["isola", "fr-4", "high-tg", "lower-loss", "high-speed", "family-ladder"]
---

# Canonical Summary

> The current `llm_wiki` corpus can now support a conservative Isola material ladder for layer-count writing: `IS410` and `370HR` as baseline/high-Tg FR-4-family anchors, `FR408 / FR408HR` as stronger FR-4-family examples, and `I-Speed / I-Tera MT40` as lower-loss digital laminate examples.

## Stable Facts

- `IS410` and `370HR` now give the corpus official product-level anchors for mainstream and high-Tg FR-4-family examples.
- `FR408` and `FR408HR` remain valid official anchors when a draft needs better-defined FR-4-family examples without pretending FR-4 is one universal material.
- `I-Speed` and `I-Tera MT40` provide official lower-loss and high-speed digital laminate anchors within the same vendor family.
- Product-level material values must stay tied to the exact datasheet and test conditions instead of being flattened into one cross-family table.

## Conditions And Methods

- Use this card when a layer-count article needs to move from `baseline FR-4` to `higher-Tg` or `lower-loss digital laminate` choices without jumping straight to PTFE or ultra-low-loss backplane materials.
- Pair this card with the exact datasheet-backed material cards or source records before inserting numeric values.
- Use this card to organize family progression, not to force one specific ranking across every program.

## Limits And Non-Claims

- This card does not provide a vendor-neutral FR-4 ranking.
- It does not claim any single Isola family is stocked, approved, or automatically required for a given layer count.
- It does not replace stackup-specific impedance, loss, or thermal modeling.

## Open Questions

- Add a similar family ladder for a second vendor once broader non-Isola FR-4/high-Tg sources are formalized.
- Decide whether `IS420`, `IS550H`, or `IS680` need dedicated anchors for future multilayer blog work.

## Source Links

- https://www.isola-group.com/wp-content/uploads/data-sheets/is410-fr-4-epoxy-laminate-and-prepreg.pdf
- https://www.isola-group.com/wp-content/uploads/data-sheets/370hr-laminate-prepreg.pdf
- https://www.isola-group.com/wp-content/uploads/data-sheets/fr408-laminate-and-prepreg.pdf
- https://www.isola-group.com/wp-content/uploads/data-sheets/fr408hr-laminate-and-prepreg.pdf
- https://www.isola-group.com/wp-content/uploads/data-sheets/i-speed-laminate-and-prepreg.pdf
- https://www.isola-group.com/wp-content/uploads/data-sheets/i-tera-mt40.pdf
