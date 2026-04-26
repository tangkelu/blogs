---
fact_id: "methods-internal-resource-layer-prompt-support-corpus"
title: "APT resources pages form an internal prompt-support corpus across DFM, downloads, FAQ, and glossary layers"
topic: "Internal resource layer and prompt-support corpus"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids:
  - "frontendapt-resources-index-page-en"
  - "frontendapt-dfm-guidelines-resource-page-en"
  - "frontendapt-downloads-materials-resource-page-en"
  - "frontendapt-downloads-resource-page-en"
  - "frontendapt-faq-resource-page-en"
  - "frontendapt-glossary-terms-resource-page-en"
tags: ["internal", "resources", "dfm", "downloads", "faq", "glossary", "prompt-support", "retrieval"]
---

# Canonical Summary

> The APT `resources` layer is best treated as an internal prompt-support corpus. It provides retrieval structure for DFM checklists, downloadable material libraries, FAQ shortcuts, and glossary normalization, but it is not a substitute for standards, official datasheets, or current commercial commitments.

## Stable Facts

- The resources overview page groups the knowledge layer into DFM/DFA guidance, downloads and templates, online tools, glossary content, blog-style engineering notes, and FAQ access.
- The DFM guidelines page is a long-form checklist resource spanning stackup, fabrication, assembly, testing, and reliability review stages.
- The materials-downloads page is organized as a vendor-grouped library for datasheets and process-note retrieval rather than as a validated fact table.
- The downloads registry JSON currently behaves more like a structural container than a substantive knowledge source.
- The FAQ page provides short operational answers across quoting, files, capability, quality, testing, logistics, DFM, compliance, and support topics.
- The glossary dataset is a large internal terminology list that helps normalize PCB and PCBA language, abbreviations, and quick definitions.

## Conditions And Methods

- Use this card when a prompt needs support material around intake, terminology normalization, or quick customer-facing guidance.
- Prefer the DFM page for checklist structure, the FAQ page for short operational routing, and the glossary page for term normalization.
- Treat downloads pages as retrieval and library-context support; validate any substantive technical claim from the underlying PDF or official source before reuse.
- Keep resource-layer support separate from standards authority, manufacturer property data, and live commercial policy.

## Limits And Non-Claims

- This card does not certify that the downloads library is complete, current, or internally validated.
- It does not freeze lead times, update cadence, warranty posture, compliance availability, or supported formats as durable facts.
- It does not elevate glossary definitions or FAQ answers to standards-grade authority.

## Open Questions

- A future batch may need dedicated extraction from the DFM guidelines page if prompt work starts requiring chapter-level intake heuristics.
- The downloads registry can be ignored for fact extraction unless the JSON begins carrying substantive file metadata.

## Source Links

- /code/hileap/frontendAPT/public/static/resources/en/index.json
- /code/hileap/frontendAPT/public/static/resources/en/dfm-guidelines.json
- /code/hileap/frontendAPT/public/static/resources/en/downloads-materials.json
- /code/hileap/frontendAPT/public/static/resources/en/downloads.json
- /code/hileap/frontendAPT/public/static/resources/en/faq.json
- /code/hileap/frontendAPT/public/static/resources/en/glossary-terms.json
