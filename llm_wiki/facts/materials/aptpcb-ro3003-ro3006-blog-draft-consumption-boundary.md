---
fact_id: "materials-aptpcb-ro3003-ro3006-blog-draft-consumption-boundary"
title: "APTPCB RO3003 / RO3006 draft batch is a rewrite-intent inventory, not a material fact source"
topic: "APTPCB RO3003 / RO3006 draft consumption boundary"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids:
  - "rogers-ro3000-datasheet"
  - "rogers-ro3003-product-page"
  - "rogers-ro3006-product-page"
  - "rogers-ro3000-fabrication-guidelines"
  - "frontendapt-materials-rf-rogers-page-en"
  - "frontendapt-materials-rogers-pcb-manufacturing-page-en"
tags: ["rogers", "ro3003", "ro3006", "aptpcb", "draft-boundary", "rewrite-gate"]
---

# Canonical Summary

> The APTPCB RO3003 / RO3006 draft batch under `/code/blogs/tmps/APTPCB_blog2603/en` should be used as a topic-intent and blocked-claim inventory. Reusable material values must come from Rogers official source-backed cards, while fabrication, assembly, supplier, cost, lead-time, certification, and finished-board RF performance claims need separate source lanes.

## Stable Facts

- Current `llm_wiki` already has Rogers official source-backed cards for `RO3003`, `RO3006`, their direct comparison, and RO3000 process handling.
- The draft batch repeatedly targets RO3003 low-loss / 77 GHz / mmWave intent and RO3006 higher-Dk compact RF intent.
- The batch also contains many draft-level worked examples, formulas, supplier-checklist items, process windows, cost claims, lead-time claims, quick-turn claims, and certification or qualification phrases.
- APT internal Rogers pages are usable as site-positioning support for Rogers-family RF manufacturing, hybrid stackups, PTFE-aware processing, and RF validation framing.
- APT internal Rogers pages and temporary blog drafts do not override Rogers official datasheets or product pages for Dk, Df, TcDk, CTE, moisture absorption, thermal conductivity, UL, lead-free compatibility, or product positioning.

## Conditions And Methods

- For material-property writing, use `materials-rogers-ro3003`, `materials-rogers-ro3006`, `materials-rogers-ro3003-vs-ro3006`, and `materials-rogers-ro3003-vs-ro3006-vs-ro3010-vs-ro3035`.
- For process framing, pair Rogers' RO3000 fabrication guide with existing internal process cards before writing about PTFE handling, drilling, hybrid stackups, surface finish, or RF validation.
- For future rewrite prompts, consume `logs/p4-29-aptpcb-ro3003-ro3006-blog-ingestion-map.md` as the blocked-claim map before drafting.
- Keep all formulas, calculations, and examples out of reusable facts unless a later source-specific card is created.

## Limits And Non-Claims

- This card does not verify draft-originated dielectric-loss calculations, guided-wavelength examples, trace-width estimates, patch-size estimates, center-frequency-shift examples, or copper-roughness loss percentages.
- It does not prove APTPCB stocking, quick-turn availability, material sourcing relationships, lead time, cost savings, yield, throughput, or quote commitments.
- It does not prove IATF, automotive, defense, Class 3, ESS, NDI, FAI, TDR, VNA, X-ray, IPC-1601, or IPC-6012 compliance for any supplier, lot, stackup, or finished board.
- It does not authorize using temporary blog prose as a primary source for Rogers material values.

## Open Questions

- Whether to create a dedicated RO3003 / RO3006 rewrite gate for APTPCB March 2026 articles.
- Whether to register selected live APT blog URLs as `internal_blog_post` records after they are published or moved out of `/tmps`.

## Source Links

- https://rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/data-sheets/ro3000-laminate-data-sheet-ro3003----ro3006----ro3010----ro3035.pdf
- https://www.rogerscorp.com/advanced-electronics-solutions/ro3000-series-laminates/ro3003-laminates
- https://www.rogerscorp.com/advanced-electronics-solutions/ro3000-series-laminates/ro3006-laminates
- https://www.rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/fabrication-information/fabrication-guidelines-ro3000-and-ro3200-series-high-frequency-circuit-materials.pdf
- /code/hileap/frontendAPT/public/static/materials/en/rf-rogers.json
- /code/hileap/frontendAPT/public/static/materials/en/rogers-pcb-manufacturing.json
