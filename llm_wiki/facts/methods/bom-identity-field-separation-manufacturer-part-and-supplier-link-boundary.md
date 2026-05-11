---
fact_id: "methods-bom-identity-field-separation-manufacturer-part-and-supplier-link-boundary"
title: "BOM identity should separate manufacturer part identity from supplier-facing link fields, while procurement outcomes remain out of scope"
topic: "BOM identity-field separation boundary"
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
tags: ["bom", "manufacturer-part-number", "supplier-part", "identity-fields", "sourcing", "alternate-control", "methods"]
---

# Canonical Summary

> Current official and internal coverage is strong enough to support one narrow BOM identity-field boundary: a BOM should keep manufacturer identity explicit, preserve manufacturer part number as a distinct mapped field, and treat supplier-facing sourcing links as a separate downstream surface rather than collapsing everything into one ambiguous part string. This boundary supports identity hygiene and sourcing-review posture only. It does not authorize automatic matching sufficiency, live availability, price, lead time, or supplier-approval claims.

## Stable Facts

- Official Altium ActiveBOM documentation treats `Manufacturer Part` and linked `Supplier Part` identities as separate BOM-side objects in the solutions flow.
- Official Altium manufacturer-link field documentation exposes explicit mapped fields for `Manufacturer Name` and `Manufacturer Part Number`.
- Official Altium 365 BOM Portal documentation reinforces that BOM review can keep structured identity and sourcing-oriented columns visible together.
- Internal APT BOM and sourcing pages already support the broader posture that BOM review, sourcing review, alternates control, and traceability belong to one governed manufacturing flow.
- From those sources together, the repo can safely preserve one narrow review rule for `E6`:
  design/electrical identity, manufacturer identity, and supplier-facing sourcing identity should not be silently collapsed into one uncontrolled BOM text field.

## Conditions And Methods

- Use this card when a draft needs conservative BOM identity guidance for procurement-ready review posture.
- Treat the safe reusable rule as:
  - keep `Manufacturer Name` explicit
  - keep `Manufacturer Part Number` explicit
  - keep supplier-facing sourcing or order-link identity as a separate downstream review surface
  - resolve alternates and source identity through controlled review rather than by overloading one free-text field
- Explain that sourcing review depends on structured identity fields but is not the same thing as structured identity fields.
- Pair this card with:
  - [pcba-bom-sourcing-and-traceability-posture.md](/code/blogs/llm_wiki/facts/methods/pcba-bom-sourcing-and-traceability-posture.md)
  - [avl-and-alternate-control-posture.md](/code/blogs/llm_wiki/facts/methods/avl-and-alternate-control-posture.md)
  - [bom-and-hdi-complexity-boundary.md](/code/blogs/llm_wiki/facts/methods/bom-and-hdi-complexity-boundary.md)
- Keep this card at identity-field hygiene level; if a prompt needs ERP schema closure, PLM integration specifics, or distributor API behavior, escalate to narrower primary sources.

## Safe Blog Usage

- Explain that BOM normalization starts by separating manufacturer identity from supplier-facing sourcing identity.
- Explain that manufacturer part number should remain an explicit controlled field rather than being buried in comments or merged into ambiguous labels.
- Explain that sourcing review and alternate-control decisions depend on clean identity fields.
- Explain that structured BOM identity reduces reconciliation risk, but does not itself prove procurement success.

## Limits And Non-Claims

- This card does not prove automatic BOM matching completeness or accuracy.
- It does not prove availability, lead time, MOQ, price, or supplier approval.
- It does not authorize generic counterfeit-detection, sourcing-guarantee, or delivery-window claims.
- It does not define one universal ERP, PLM, or CAD schema for every organization.
- It does not replace a live AVL review, alternates review, or sourcing decision.

## Provenance Boundary

- `P4-336` and the `E6` article lane can safely contribute the demand signal that BOM ambiguity matters.
- They do not act as authority for workflow promises, quote outcomes, stock claims, or software sufficiency.

## Open Questions

- Add a future narrower card if the repo later needs official field guidance for lifecycle status, distributor SKU, or approved alternate-class labeling.
- Add a future standards-adjacent metadata lane only if BOM exchange schema authority becomes a high-value public writing requirement.

## Source Links

- https://www.altium.com/documentation/altium-designer/activebom/managing-solutions
- https://www.altium.com/documentation/altium-designer/activebom-dlg-manufacturerlinkfieldsdialogdefine-manufacturer-link-fields-ad
- https://www.altium.com/documentation/altium-365/bom-portal
- /code/hileap/frontendAPT/public/static/pcba/en/component-sourcing.json
- /code/hileap/frontendAPT/public/static/pcba/en/components-bom.json
