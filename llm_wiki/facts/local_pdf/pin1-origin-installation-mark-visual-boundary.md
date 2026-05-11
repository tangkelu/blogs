---
fact_id: "local-pdf-pin1-origin-installation-mark-visual-boundary"
title: "A curated local PCB资料 text excerpt may support pin-1, polarity, installation-mark, and origin documentation context only"
authority_class: "local_pdf_curated"
allowed_for: "blog_body"
not_allowed_for:
  - "official standard wording"
  - "manufacturer-recommended land-pattern defaults"
  - "supplier capability proof"
  - "universal footprint-origin rules"
evidence_ids:
  - "pcbziliao-package-pin1-origin-installation-mark-text-boundary"
scope_type: "local_documentation_governance_context"
confidence: "medium"
topic: "pin-1 origin installation-mark visual boundary"
must_refresh: false
reviewed_at: "2026-05-08"
related_official_fact_ids:
  - "methods-padstack-origin-pin1-and-footprint-review-governance-boundary"
tags: ["local-pdf", "package", "pin-1", "origin", "installation-mark", "polarity", "documentation", "connector", "structural-text"]
limits_and_non_claims:
  - "local handbook context only"
  - "not a standards or package-owner recommendation"
  - "not a universal connector-origin rule"
---

# Canonical Summary

This accepted local PDF text excerpt may support a narrow blog-body explanation that package documentation should make `pin-1`, polarity, installation-mark, and origin intent explicit. The preserved handbook text also shows local origin-placement examples that distinguish regular-shape parts, through-hole parts, and connectors. This card is local-context only. It does not authorize universal origin rules, official naming conventions, or any numeric silkscreen and clearance guidance from the same pages.

## Curated Local-PDF Fact

- The preserved local text explicitly calls out `pin-1` marking near the first pin.
- The preserved local text explicitly calls out polarity marking and installation-mark visibility when the component carries such markers.
- The preserved local text distinguishes origin-placement examples for regular-shape devices, through-hole devices, and connector cases.

## Safe Blog Usage

- Explain that package and assembly documentation should keep orientation intent auditable rather than implicit.
- Use the preserved local text as scoped support when describing why `pin-1`, polarity, and installation markers need to be visible in the documentation package.
- Explain that origin handling may differ by package form, but route any universal or owner-grade rule to stronger authority.

## Limits And Non-Claims

- Do not restate the handbook wording as IPC, CAD-owner, or component-manufacturer authority.
- Do not convert the connector-origin examples into one default library rule.
- Do not pull silkscreen line-width, spacing, keepout, or hole-table numerics from the same pages through this card.

## Evidence Links

- [pin1-origin-installation-mark-text-boundary.md](/code/blogs/llm_wiki/pdf_evidence/pcb_ziliao/package/pin1-origin-installation-mark-text-boundary.md)

## Related Official Facts

- [padstack-origin-pin1-and-footprint-review-governance-boundary.md](/code/blogs/llm_wiki/facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md)
