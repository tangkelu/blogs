---
fact_id: "materials-arlon-official-source-coverage"
title: "Arlon coverage: N-series and 86HP have official source anchors; CLTE-XT/TC350/AD/CuClad are internal-only recovered; RF/PTFE official datasheets remain blocked"
topic: "Arlon official source coverage and recovery state"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
source_ids:
  - "arlon-products-directory"
  - "arlon-current-product-sitemap"
  - "arlon-33n-product-page"
  - "arlon-35n-product-page"
  - "arlon-37n-product-page"
  - "arlon-45n-product-page"
  - "arlon-47n-product-page"
  - "arlon-84n-product-page"
  - "arlon-85n-product-page"
  - "arlon-85n-datasheet"
  - "arlon-55nt-product-page"
  - "arlon-55nt-datasheet"
  - "arlon-85nt-product-page"
  - "arlon-85nt-datasheet"
  - "arlon-86hp-product-page"
  - "arlon-86hp-datasheet"
  - "arlon-controlled-flow-prepreg-application-page"
  - "arlon-heavy-copper-layers-application-page"
  - "arlon-laminate-guide"
  - "frontendapt-materials-arlon-pcb-page-en"
tags: ["arlon", "agc", "polyimide", "ptfe", "rf", "source-coverage", "source-gap", "86hp", "clte-xt", "tc350", "ad-series"]
---

# Canonical Summary

> Arlon coverage is now split into three tiers: (1) official product-page + datasheet anchors for N-series (33N–85N) and 86HP hi-rel polyimide; (2) internal-only recovery for CLTE-XT, TC350, AD250/300/1000, and CuClad/DiClad/IsoClad RF/PTFE families via APTPCB JSON; (3) still-blocked official datasheets for the entire RF/PTFE group. The current official Arlon product sitemap (checked 2026-05-02) does not expose CLTE-XT, TC350, AD, CuClad, or DiClad as live public product pages.

## Coverage State By Family

| Family | Official Source | Fact Card | Use Tier |
|--------|----------------|-----------|----------|
| 33N / 35N / 85N (Polyimide) | ✅ Official product page + datasheet | `arlon-85n-exact-product` | Standard |
| 45N / 47N (Epoxy) | ✅ Official product page | `arlon-official-source-coverage` | Standard |
| 55NT / 85NT (Thermount) | ✅ Official product page + datasheet | `arlon-55nt`, `arlon-85nt-exact-product` | Standard |
| 86HP (Hi-Rel Polyimide) | ✅ Official product page + datasheet (2024/02) | `arlon-86hp-exact-product` | Standard |
| CLTE-XT / CLTE-AT | ❌ No current official page or datasheet | `arlon-detailed-material-specs-recovery` | Internal only |
| TC350 / TC600 | ❌ No current official page or datasheet | `arlon-detailed-material-specs-recovery` | Internal only |
| AD250 / AD300 / AD1000 | ❌ No current official page or datasheet | `arlon-detailed-material-specs-recovery` | Internal only |
| CuClad / DiClad / IsoClad | ❌ No current official page or datasheet | `arlon-detailed-material-specs-recovery` | Internal only |
| 37N / 38N / HF-50 (Bondply) | ⚠️ 37N product page only | `arlon-official-source-coverage` | Limited |

## Stable Facts

- APT's Arlon page covers polyimide, epoxy, Thermount, and microwave/PTFE material families.
- Arlon's official products directory (`arlonemd.com/arlon-products/`) is a live manufacturer-controlled discovery anchor.
- The official Arlon product sitemap (2026-05-02) exposes live pages for: 33N, 35N, 37N, 45N, 45NK, 47N, 55NT, 84N, 85N, 85NT, 86HP, and related non-RF families.
- 86HP has a current official product page (published 2022-11-10) and a current official datasheet (`86HP-v-1.6.pdf`, path `2024/02`).
- CLTE-XT, TC350, AD250/AD300/AD1000, CuClad, DiClad, and IsoClad are **not** exposed as live public Arlon product pages in the current (2026-05-02) sitemap.
- Material specifications for CLTE-XT, TC350, AD250, and CuClad families have been **internally recovered** via APTPCB JSON (P4-143); those values are Tier-2 internal authority, not official Arlon/AGC-published datasheet values.
- Arlon controlled-flow prepreg and heavy-copper application pages are available as official application-context anchors.
- The Arlon laminate guide supports family discovery, but is not a substitute for current grade-level datasheets.

## Conditions And Methods

- Use this card when a draft mentions Arlon as part of APT's public material coverage.
- For N-series (33N–85N) and 86HP: official product pages and/or datasheets exist — use the relevant exact-product fact cards.
- For CLTE-XT, TC350, AD250/300/1000, CuClad/DiClad/IsoClad: use `arlon-detailed-material-specs-recovery` for internal stackup planning only; do not publish as official Arlon datasheet values.
- Treat stocking, lead-time, and manufacturing-readiness claims as refresh-required.

## Limits And Non-Claims

- CLTE-XT, TC350, AD250/300/1000, CuClad, DiClad, IsoClad property values in this knowledge base are from APTPCB internal JSON, **not** from official Arlon/AGC-published datasheets.
- This card does not validate current Arlon/AGC product-line continuity for RF/PTFE families.
- It does not prove current product availability or pricing.
- It does not prove that every Arlon grade named by APT has an active production run.

## Open Questions

- Whether official Arlon/AGC product pages or datasheets for CLTE-XT, TC350, AD250/300/1000, CuClad, DiClad, IsoClad are republished under new URLs.
- Whether AGC Inc. continues to produce these RF/PTFE families under the Arlon brand.
- Confirm how AGC / Arlon domain ownership should be cited when both `arlonemd.com` and AGC branding appear.

## Related Fact Cards

- `arlon-86hp-exact-product` — 86HP hi-rel polyimide, official source backed
- `arlon-85n-exact-product` — 85N high-temperature polyimide, official source backed
- `arlon-55nt` — 55NT Thermount, official source backed
- `arlon-85nt-exact-product` — 85NT Thermount, official source backed
- `arlon-hi-rel-branch-normalization` — N-series and hi-rel branch overview
- `arlon-detailed-material-specs-recovery` — CLTE-XT/TC350/AD/CuClad internal recovery
- `arlon-rf-ptfe-current-site-gap` — current blocker evidence for RF/PTFE families
- `arlon-clte-xt-microwave` — CLTE-XT microwave boundary
- `arlon-tc350-thermal-rf` — TC350 thermal RF boundary
- `arlon-ad-series-antenna` — AD series antenna boundary

## Source Links

- https://www.arlonemd.com/arlon-products/
- https://www.arlonemd.com/wp-sitemap-posts-arlon_product-1.xml
- https://www.arlonemd.com/arlon_product/33n-flame-retardant-polyimide/
- https://www.arlonemd.com/arlon_product/35n-flame-retardant-polyimide/
- https://www.arlonemd.com/arlon_product/37n-low-flow-polyimide-prepreg/
- https://www.arlonemd.com/arlon_product/45n-multifunctional-epoxy/
- https://www.arlonemd.com/arlon_product/47n-modified-efoxy-low-flow-prepreg/
- https://www.arlonemd.com/arlon_product/84n-filled-polyimide-prepreg/
- https://www.arlonemd.com/arlon_product/85n-high-temperature-polyimide/
- https://www.arlonemd.com/applications/controlled-flow-prepreg/
- https://www.arlonemd.com/applications/heavy-copper-layers/
- https://www.arlonemd.com/wp-content/uploads/2020/05/Laminate-Guide.pdf
- /code/hileap/frontendAPT/public/static/materials/en/arlon-pcb.json
