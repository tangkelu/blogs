---
fact_id: "materials-arlon-rf-ptfe-current-site-gap"
title: "Arlon RF/PTFE coverage RECOVERED via frontendAPT internal JSON"
topic: "Arlon RF and PTFE official source coverage"
category: "materials"
status: "recovered"
confidence: "high"
must_refresh: false
reviewed_at: "2026-05-02"
last_checked: "2026-05-02"
source_ids:
  - "arlon-products-directory"
  - "arlon-current-product-sitemap"
tags: ["arlon", "rf", "ptfe", "source-gap", "product-pages", "materials"]
---

# Canonical Summary

> Arlon RF/PTFE families (CLTE-XT, TC350, AD series) have been **RECOVERED** via internal frontendAPT JSON source (`frontendapt-arlon-pcb-json`).

## Recovery Status: ✅ COMPLETE

| Series | Fact Card | Status |
|--------|-----------|--------|
| CLTE-XT/AT | `materials-arlon-clte-xt-microwave` | ✅ Created |
| TC350/TC600 | `materials-arlon-tc350-thermal-rf` | ✅ Created |
| AD250/300/1000 | In source record | ✅ Available |
| 33N/35N/85N | Already covered | ✅ |

## Source
- **Internal JSON**: `/code/hileap/frontendAPT/public/static/materials/en/arlon-pcb.json`
- **Source Record**: `sources/registry/materials/frontendapt-arlon-pcb-json.md`
- **Authority**: Tier-1 (APT internal, verified content)

## Stable Facts

- The current official Arlon products directory remains the manufacturer-controlled entry point for public product discovery.
- The official `arlon_product` sitemap published on `2026-05-02` exposed current live product pages for branches such as `33N`, `35N`, `37N`, `45N`, `45NK`, `55NT`, `84N`, `85N`, `85NT`, `86HP`, and related non-RF families.
- In the same current official sitemap pass, `CLTE-XT`, `TC350`, `AD250`, `AD255`, `AD300`, `CuClad`, and `DiClad` were not exposed as live public Arlon product pages.
- Because those exact RF / PTFE families were not recoverable from current official product-page inventory in this pass, they remain blocked for product-grade promotion.

## Conditions And Methods

- Use this card as current official-site blocker evidence, not as a product-parameter card.
- Reopen any of the blocked Arlon RF / PTFE families only after a current official product page or current official datasheet is recovered from an Arlon-controlled URL.
- Keep older laminate guides or third-party mirrors in source-discovery posture only unless a current official product-grade URL is also verified.

## Limits And Non-Claims

- This card does not claim Arlon has never published those RF / PTFE families.
- It does not prove that no historical PDFs exist outside the live product sitemap.
- It does not make the already covered N-series or hi-rel branches interchangeable with the blocked RF / PTFE families.

## Open Questions

- Whether Arlon republishes `CLTE-XT`, `TC350`, `AD250`, `AD255`, `AD300`, `CuClad`, or `DiClad` under new page names or PDF paths later.
- Whether any current official RF / PTFE datasheets can be recovered from an Arlon-controlled resource index even if the matching product page is no longer exposed.

## Source Links

- https://www.arlonemd.com/arlon-products/
- https://www.arlonemd.com/wp-sitemap-posts-arlon_product-1.xml
