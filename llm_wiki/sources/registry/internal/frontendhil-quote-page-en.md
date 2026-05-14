---
source_id: "frontendhil-quote-page-en"
title: "HILPCB English Quote Page"
organization: "HILPCB"
source_type: "internal_form_page"
url: "/code/hileap/frontendHIL/pages/quote.vue"
jurisdiction: "internal"
published_at: ""
checked_at: "2026-05-13"
trust_tier: "t2"
stability: "semi_stable"
must_refresh: false
topic_tags: ["internal", "hilpcb", "quote", "rfq", "prototype", "procurement", "intake-form"]
status: "active"
notes: "Internal HIL quote page with canonical route, intake-field taxonomy, file-upload support, sourceUrl propagation, and product-context handoff."
---

# Source Summary

## What It Covers

- Canonical `/en/quote` intake route for HILPCB
- Quote-intake fields for contact info, layers, dimensions, thickness, material, surface finish, quantity, urgency, and special requirements
- File-upload handling plus source-product and `sourceUrl` context capture

## Why It Matters

- Provides HIL-owned authority for quote-intake and package-completeness wording
- Supports conservative public framing around project-specific intake rather than instant pricing

## Extraction Notes

- Safe for input-field taxonomy and release-package completeness language
- Safe for describing `/en/quote` as a project-intake route tied to fabrication and assembly context
- Do not turn urgency fields, upload support, or form presence into lead-time, response-time, or quote-speed promises

## Refresh Notes

- Re-check when the quote form fields, canonical path, or upload flow changes
