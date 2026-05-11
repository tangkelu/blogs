---
fact_id: "methods-procurement-release-identity-completeness-and-controlled-source-boundary"
title: "Procurement-ready BOM release should keep identity complete and treat controlled source review as governance, not proof of supply outcome"
topic: "procurement release identity completeness and controlled source boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-10"
source_ids:
  - "altium-activebom-managing-solutions-manufacturer-supplier-identity"
  - "altium-activebom-manufacturer-link-fields-dialog"
  - "altium-365-bom-portal-identity-and-sourcing-columns"
  - "frontendapt-pcba-component-sourcing-page-en"
  - "frontendapt-pcba-components-bom-page-en"
  - "ipc-1782b-traceability-standard-page"
  - "as6171a-counterfeit-test-methods-page"
  - "dfars-252-246-7008-sources-of-electronic-parts-page"
tags: ["procurement", "bom", "manufacturer-part-number", "supplier-link", "traceability", "controlled-source", "counterfeit-boundary", "methods"]
---

# Canonical Summary

> Current official and internal coverage is strong enough to support one narrow procurement-release boundary: a procurement-ready BOM review should keep manufacturer identity explicit, keep manufacturer part number distinct from supplier-facing sourcing or link fields, and treat alternate control, traceability, and authenticity review as governance layers rather than as proof of availability, correctness, or supplier approval.

## Stable Facts

- Official Altium documentation supports keeping structured manufacturer identity and supplier-facing sourcing identity as separate BOM review surfaces rather than collapsing them into one uncontrolled part string.
- Internal PCBA BOM and component-sourcing pages support the posture that sourcing review belongs to a governed release flow together with lifecycle review, authenticity posture, and traceability context.
- Public `IPC-1782B` metadata supports traceability as a manufacturing and supply-chain vocabulary layer rather than as a live-stock or delivery guarantee.
- Public `DFARS 252.246-7008` metadata supports preferred-source hierarchy and traceability-aware procurement governance as a responsibility layer, not as a generic market-outcome promise.
- Public `AS6171A` metadata supports the boundary that testing or screening does not by itself prove authenticity without known chain of custody.
- From those layers together, the repo can safely preserve one narrow `E6` rule:
  procurement release should check complete part identity first, then govern alternates, traceability, and authenticity as controlled review layers.

## Conditions And Methods

- Use this card when a draft needs conservative procurement-risk wording for `E6` BOM review or sourcing-release posture.
- Treat the safe reusable rule as:
  - keep `Manufacturer Name` explicit
  - keep `Manufacturer Part Number` explicit
  - keep supplier-facing sourcing, order-link, or seller identity as a separate downstream review surface
  - resolve alternates through controlled review rather than casual substitution
  - treat traceability and authenticity review as governance layers, not outcome guarantees
- Pair this card with:
  - [bom-identity-field-separation-manufacturer-part-and-supplier-link-boundary.md](/code/blogs/llm_wiki/facts/methods/bom-identity-field-separation-manufacturer-part-and-supplier-link-boundary.md)
  - [pcba-bom-sourcing-and-traceability-posture.md](/code/blogs/llm_wiki/facts/methods/pcba-bom-sourcing-and-traceability-posture.md)
  - [avl-and-alternate-control-posture.md](/code/blogs/llm_wiki/facts/methods/avl-and-alternate-control-posture.md)
  - [high-reliability-traceability-and-counterfeit-control-metadata.md](/code/blogs/llm_wiki/facts/standards/high-reliability-traceability-and-counterfeit-control-metadata.md)
- Keep this card at procurement-release governance level only; if a prompt needs live availability, distributor status, pricing, lead time, package numerics, or seller approval, require narrower primary sources.

## Safe Blog Usage

- Explain that procurement mistakes often begin with incomplete part identity rather than with logistics alone.
- Explain that manufacturer identity, manufacturer part number, and supplier-facing sourcing identity should remain separate review fields.
- Explain that alternates, traceability, and authenticity checks belong to controlled release governance.
- Explain that sample-stage or inquiry-stage visibility is not the same thing as production-release readiness.

## Limits And Non-Claims

- This card does not prove stock, shortage state, lead time, MOQ, replenishment, or price.
- It does not prove supplier quality, channel superiority, supplier approval, or delivery reliability.
- It does not prove that any marketplace, seller, or workflow guarantees authenticity or avoids counterfeit outcomes.
- It does not authorize package-width, body-size, suffix-taxonomy, or dimensional examples from article-origin content.
- It does not prove continuity from sample stage to mass-production release.
- It does not replace a live AVL review, sourcing decision, or project-specific procurement check.

## Provenance Boundary

- `P4-338` contributes the demand signal that procurement-risk articles repeatedly mix identity ambiguity, alternates posture, and authenticity vocabulary.
- Authority comes from the current-public Altium documentation, the internal sourcing/BOM pages, and the public traceability / authenticity metadata layers listed above.

## Open Questions

- Add a future narrower card only if the repo later needs official lifecycle-status fields, approved alternate-class labeling, or authorized-distribution status language.
- Add a future refreshed source lane only if a later prompt requires current market availability or seller-status data.

## Source Links

- https://www.altium.com/documentation/altium-designer/activebom/managing-solutions
- https://www.altium.com/documentation/altium-designer/activebom-dlg-manufacturerlinkfieldsdialogdefine-manufacturer-link-fields-ad
- https://www.altium.com/documentation/altium-365/bom-portal
- /code/hileap/frontendAPT/public/static/pcba/en/component-sourcing.json
- /code/hileap/frontendAPT/public/static/pcba/en/components-bom.json
- https://shop.electronics.org/ipc-1782/ipc-1782-standard-only/Revision-b/english
- https://saemobilus.sae.org/standards/as6171a-test-methods-standard-general-requirements-suspect-counterfeit-electrical-electronic-electromechanical-parts
- https://www.acquisition.gov/dfars/252.246-7008-sources-electronic-parts.
