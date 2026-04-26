---
fact_id: "materials-arlon-official-source-coverage"
title: "Arlon site-mentioned materials now have official discovery anchors but remain parameter-limited"
topic: "Arlon official source coverage"
category: "materials"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-24"
source_ids:
  - "arlon-products-directory"
  - "arlon-33n-product-page"
  - "arlon-35n-product-page"
  - "arlon-37n-product-page"
  - "arlon-45n-product-page"
  - "arlon-47n-product-page"
  - "arlon-84n-product-page"
  - "arlon-85n-product-page"
  - "arlon-controlled-flow-prepreg-application-page"
  - "arlon-heavy-copper-layers-application-page"
  - "arlon-laminate-guide"
  - "frontendapt-materials-arlon-pcb-page-en"
tags: ["arlon", "agc", "polyimide", "ptfe", "source-coverage", "source-gap"]
---

# Canonical Summary

> Arlon is a real site-mentioned material family and now has official discovery anchors in `llm_wiki`, but product-level facts should stay conservative until current datasheets for exact grades are registered.

## Stable Facts

- APT's Arlon page mentions Arlon polyimide, epoxy, Thermount, and microwave/PTFE material families.
- Arlon's official products directory is available as a manufacturer-controlled source-discovery anchor.
- Arlon 33N, 35N, 37N, 45N, 47N, 84N, and 85N have official product-page anchors.
- Arlon controlled-flow prepreg and heavy-copper application pages are available as official application/source-discovery anchors.
- The Arlon laminate guide can support family discovery, but product datasheets are still preferred for numeric material values.

## Conditions And Methods

- Use this card when a draft mentions Arlon as part of APT's public material coverage.
- Use product-level datasheets before extracting values for 33N, 35N, 37N, 45N, 47N, 84N, 85N, CLTE-XT, TC350, AD250, AD255, AD300, CuClad, DiClad, or similar grades.
- Treat internal stocking, lead-time, and process claims as refresh-required.

## Limits And Non-Claims

- This card does not state Arlon Dk, Df, Tg, CTE, moisture, copper, or thickness values.
- It does not validate APT's internal stock claims.
- It does not prove that every Arlon grade named by APT has a current public datasheet or product page.

## Open Questions

- Find stable current product-level datasheets for the Arlon grades named by APT, especially RF/PTFE families not recovered in P4-09.
- Confirm how AGC / Arlon domain ownership and product literature should be cited in future material tables.

## Source Links

- https://www.arlonemd.com/arlon-products/
- https://www.arlonemd.com/arlon_product/33n-flame-retardant-polyimide/
- https://www.arlonemd.com/arlon_product/35n-flame-retardant-polyimide/
- https://www.arlonemd.com/arlon_product/37n-low-flow-polyimide-prepreg/
- https://www.arlonemd.com/arlon_product/45n-multifunctional-epoxy/
- https://www.arlonemd.com/arlon_product/47n-modified-epoxy-low-flow-prepreg/
- https://www.arlonemd.com/arlon_product/84n-filled-polyimide-prepreg/
- https://www.arlonemd.com/arlon_product/85n-high-temperature-polyimide/
- https://www.arlonemd.com/applications/controlled-flow-prepreg/
- https://www.arlonemd.com/applications/heavy-copper-layers/
- https://www.arlonemd.com/wp-content/uploads/2020/05/Laminate-Guide.pdf
- /code/hileap/frontendAPT/public/static/materials/en/arlon-pcb.json
