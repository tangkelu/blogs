# Site Material Baseline Coverage

Date: 2026-04-24

## Purpose

This log tracks material families and product names that appear in non-blog `frontendAPT` and `frontendHIL` content, then maps them to the `llm_wiki` source/fact layer.

The goal is not to build an unlimited materials encyclopedia. The goal is narrower:

- if our own public non-blog pages mention a material family, brand, or model, `llm_wiki` should have at least a governance record for it
- official manufacturer sources should be added before product-level values are used
- internal pages should remain support/context sources, not primary datasheet truth

## Scan Scope

Included:

- `/code/hileap/frontendAPT/public/static/**/*.json`
- `/code/hileap/frontendHIL/public/static/**/*.json`
- `/code/hileap/frontendHIL/data/service-landings/**/*.json`
- English non-blog content only

Excluded:

- Blog markdown and blog payloads
- Non-English duplicates
- Generated build/cache/dependency files

## Material Families Found In Site Content

Already covered with strong or usable official source records:

- Rogers RO3000 / RO4000 / RO4835 / RT/duroid / TMM
- Isola Astra MT77 / Tachyon 100G / FR408 / FR408HR
- Panasonic MEGTRON 6 / 7 / 8
- Ventec VT-870 / VTM1000i / VT-464G / VT-4B7 / IMS family
- AGC RF-30A / RF-10 / RF-35HTC
- FR-4 baseline examples via Isola FR408 / FR408HR

Newly added in this baseline pass:

- Arlon official directory / 85N product anchor / laminate guide anchors
- Isola 370HR / I-Speed / I-Tera MT40 / IS410 official datasheet anchors
- Panasonic MEGTRON series and MEGTRON 4 official anchors
- Rogers RO4400 / RO4450F / RO4460G2 bondply anchors

Added in the follow-on pass:

- CeramTec ceramic substrate class-level anchor for ceramic / alumina / aluminum nitride context
- MARUWA Aluminum Nitride (AlN) substrate official anchor
- Ajinomoto / Ajinomoto Fine-Techno ABF official anchors
- Mitsubishi Gas Chemical BT materials official anchor
- Panasonic FELIOS flexible circuit-board material and FELIOS LCP official anchors

Added in the product-recovery pass:

- Arlon 33N / 35N / 37N / 45N / 47N / 84N official product-page anchors
- Arlon controlled-flow prepreg and heavy-copper layers official application anchors

Still gap-controlled, not parameter-ready:

- Taconic TLY / TLX / TLC / TLE / RF-35 product-level official datasheet anchors
- Arlon CLTE-XT / TC350 / AD250 / AD255 / AD300 / CuClad / DiClad product-level pages or datasheets
- Arlon 33N / 35N / 37N / 45N / 47N / 84N / 85N product parameters until current datasheets are registered or refreshed
- Direct PI-specific flexible-laminate supplier data if future blogs need polyimide values rather than class-level flex-material framing

## Coverage Rules

- Use official datasheets for product-level Dk, Df, Tg, Td, CTE, thermal conductivity, copper, thickness, and processing values.
- Use official product-family pages for family membership, naming, and source discovery.
- Use internal APT/HIL JSON pages only for public service positioning and application framing.
- Do not freeze inventory, stocking, current lead time, preferred supplier status, or distributor availability from internal pages.
- When a site page uses a numeric material value, the future blog evidence pack must re-check the exact manufacturer source before publication.

## Next Material Priority

Priority 1:

- Taconic product-level official source discovery.
- Arlon product-level official source discovery for the exact grades already named by APT.

Priority 2:

- Product-level datasheets for material classes only when a blog needs numeric comparison tables.

Priority 3:

- Additional FR-4 suppliers such as Ventec, Shengyi, ITEQ, and Kingboard if future blogs compare broad FR-4 options.

## Current Decision

This baseline pass is sufficient to make "site-mentioned material coverage" systematic, but it is not sufficient to publish product-level parameter tables for every named site material. The next material work should stay source-first and focus on official product pages or datasheets for the unresolved families above.
