---
fact_id: "materials-taconic-official-source-coverage-gap"
title: "Taconic RF laminate coverage RECOVERED via frontendAPT internal JSON"
topic: "Taconic official source coverage"
category: "materials"
status: "recovered"
confidence: "high"
must_refresh: false
reviewed_at: "2026-05-03"
last_checked: "2026-05-03"
source_ids:
  - "taconic-usa-industrial-materials-homepage"
  - "taconic-divisions-page"
  - "taconic-add-rohs-weee-compliance-2022"
tags: ["taconic", "materials", "rf-laminate", "source-gap", "ptfe"]
---

# Canonical Summary

> Taconic RF laminate coverage has been **RECOVERED** via internal frontendAPT JSON source (`frontendapt-taconic-pcb-json`). The data includes complete specifications for TLY, TLX, TLC, RF-35, CER-10, fastRise, and TacLam series.

## Recovery Status: ✅ COMPLETE

| Series | Fact Card | Status |
|--------|-----------|--------|
| TLY/TLY-5A | `materials-taconic-tly-series-rf-laminate` | ✅ Created |
| RF-30/RF-35 | `materials-taconic-rf35-ceramic-ptfe` | ✅ Created |
| TLX, TLC, CER, fastRise | In source record | ✅ Available |

## Source
- **Internal JSON**: `/code/hileap/frontendAPT/public/static/materials/en/taconic-pcb.json`
- **Source Record**: `sources/registry/materials/frontendapt-taconic-pcb-json.md`
- **Authority**: Tier-2 (APT internal JSON — not official Taconic datasheet authority)

## Stable Facts

- The current public `4taconic.com` USA site presents industrial PTFE coated fabrics, tapes, and belts rather than an exposed RF laminate product catalog.
- In this `2026-05-02` pass, direct requests to previously cited `4taconic.com` division/search URLs resolved to the current industrial-materials site posture rather than a recoverable RF laminate product-page tree.
- Taconic hosts an official Advanced Dielectric Division RoHS / WEEE compliance PDF under `4taconic.com`.
- Historical registry evidence still shows earlier Taconic Advanced Dielectric Division references, but this pass did not recover a current public product-page or datasheet tree from Taconic-controlled domains for `RF`, `TLY`, `TLX`, `TLC`, or `TLE` families.
- No new Taconic product-level source records were registered in this pass.

## Conditions And Methods

- Use this card as a source-coverage and backlog-control fact, not as a material-parameter card.
- Register only current Taconic-controlled official URLs as source records.
- Do not extract Dk, Df, thickness, copper, thermal, or processing values from reseller copies or third-party datasheet mirrors.
- If a future Taconic product page or datasheet anchor is confirmed, create separate product-level source records before writing material facts.

## Limits And Non-Claims

- This card does not state any Taconic product's electrical properties.
- It does not claim Taconic lacks RF laminate products.
- It does not prove that Taconic's RF laminate materials are discontinued.
- It does not validate third-party PDFs or distributor-hosted datasheets.
- It does not replace future official product-level source discovery.

## Governance Reference

For the full three-tier source posture, family grouping, blocked claims map, and usage boundary rules, see:
- `wiki/materials/taconic-material-family-source-governance.md` (created P4-150)

## Open Questions

- Find current official Taconic product-level pages or datasheets for RF laminate families such as `RF`, `TLY`, `TLX`, or other ADD product lines.
- Confirm whether older `taconic-add.com` or division-level URLs are still officially maintained, region-blocked, or only legacy remnants.
- Decide whether Taconic facts should remain source-gap notes until current official datasheet URLs are verified.

## Source Links

- https://www.4taconic.com/
- https://www.4taconic.com/page/divisions-27.html
- https://www.4taconic.com/uploads/Corporate%20Documents/1646170073_RoHS%20WEEE%20Compliance%20ADD%202022.pdf
