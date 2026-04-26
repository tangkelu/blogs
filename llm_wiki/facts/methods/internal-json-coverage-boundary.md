---
fact_id: "methods-internal-json-coverage-boundary"
title: "Internal JSON coverage now separates page inventory from extracted fact cards"
topic: "Internal JSON source coverage boundary"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids:
  - "frontendapt-capabilities-index-en"
  - "frontendapt-industries-index-en"
  - "frontendapt-resources-index-en"
  - "frontendapt-materials-remaining-index-en"
  - "frontendapt-pcb-remaining-index-en"
  - "frontendapt-pcba-remaining-index-en"
  - "frontendhil-remaining-products-index-en"
  - "frontendhil-service-landings-index-en"
tags: ["internal", "json", "coverage", "source-governance", "inventory"]
---

# Canonical Summary

> The internal JSON layer should distinguish source inventory from extracted facts. APT and HIL English non-blog JSON pages are now registered either as individual high-value source records or as directory-level index records, while fact cards are reserved for reusable engineering claims rather than one-page summaries.

## Stable Facts

- The APT capabilities, industries, resources, remaining materials, remaining PCB, and remaining PCBA groups are registered as internal JSON index sources.
- The HIL remaining product pages and service-landing pages are registered as internal JSON index sources.
- High-value PCBA, PCB fabrication, materials, RF/high-speed, finish, and validation pages have individual source records where they support durable fact cards.
- Grouped index records are intended for source coverage, prompt intake, and future extraction planning.

## Conditions And Methods

- Use individual source records when a fact card depends on a specific page.
- Use grouped index records when a prompt only needs to know whether a topic exists in the internal site corpus.
- Promote a grouped page to an individual source record if it becomes important enough for a dedicated fact card or wiki section.

## Limits And Non-Claims

- This card does not claim every indexed page has been fully converted into fact cards.
- It does not validate dynamic lead-time, certification, inventory, or volume claims.
- It does not replace official manufacturer, standards, or regulatory sources.

## Open Questions

- Add a small audit script later to compare `internal-json-source-spine.md` against registered source URLs automatically.
- Decide whether industry pages deserve dedicated application wiki pages after PCBA / advanced fabrication wiki aggregation is complete.

## Source Links

- /code/hileap/frontendAPT/public/static/capabilities/en
- /code/hileap/frontendAPT/public/static/industries/en
- /code/hileap/frontendAPT/public/static/resources/en
- /code/hileap/frontendAPT/public/static/materials/en
- /code/hileap/frontendAPT/public/static/pcb/en
- /code/hileap/frontendAPT/public/static/pcba/en
- /code/hileap/frontendHIL/public/static/products/en
- /code/hileap/frontendHIL/data/service-landings/en
