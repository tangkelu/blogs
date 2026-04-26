---
topic_id: "processes-apt-resource-layer-for-dfm-faq-and-download-retrieval"
title: "APT Resource Layer For DFM FAQ And Download Retrieval"
category: "processes"
status: "draft"
last_reviewed_at: "2026-04-24"
fact_ids:
  - "methods-internal-resource-layer-prompt-support-corpus"
  - "methods-pcba-npi-to-mass-production-gates"
  - "methods-pcba-stencil-selective-solder-and-fine-pitch-controls"
  - "methods-internal-json-coverage-boundary"
source_ids:
  - "frontendapt-resources-index-page-en"
  - "frontendapt-dfm-guidelines-resource-page-en"
  - "frontendapt-downloads-materials-resource-page-en"
  - "frontendapt-downloads-resource-page-en"
  - "frontendapt-faq-resource-page-en"
  - "frontendapt-glossary-terms-resource-page-en"
tags: ["processes", "internal-source", "resources", "dfm", "faq", "glossary", "downloads", "prompt-support"]
---

# Definition

> The APT resource layer is the site's internal support corpus for DFM intake, quick-answer retrieval, document-library navigation, and terminology normalization. It is valuable because it improves prompt grounding without pretending that every resource entry is a primary technical authority.

## Why This Topic Matters

- A wiki that only stores process and material pages misses the support layer that real prompts often need: checklists, short answers, vendor-library pointers, and consistent terminology.
- The APT resources section already exposes these support functions as a visible information architecture: DFM guidance, downloads, tools, glossary, and FAQ.
- Without explicit boundaries, this layer is easy to misuse as if it were a live policy system or an official datasheet repository.

## Stable Facts

- The resources overview page is a stable navigation map for knowledge packs, downloads, tools, glossary content, and FAQ access.
- The DFM guidelines page is the most substantive source in this layer; it acts as a long-form manufacturability checklist across bare-board, assembly, testing, and reliability review dimensions.
- The FAQ page is a short-answer layer around quoting, file submission, capability windows, testing, logistics, compliance, and response handling.
- The glossary dataset provides large-scale term normalization across PCB and PCBA vocabulary and abbreviations.
- The materials-downloads page is a vendor-grouped retrieval surface for PDFs and process notes, not a governed fact table.
- The downloads registry JSON currently contributes structural awareness more than substantive technical evidence.

## Engineering Boundaries

- Use the DFM page for intake structure, not for freezing every numeric rule as a permanent fact.
- Use FAQ content to route or summarize common questions, but refresh operational answers before publication.
- Use glossary entries for normalization and expansion of abbreviations, not for contested technical definitions.
- Use downloads pages to locate supporting files; validate any parameter from the underlying document before turning it into a fact or wiki statement.
- Keep this resource layer separate from standards, manufacturer datasheets, and live commercial commitments.

## Common Misreadings

- A downloadable file listed in the library is not automatically an approved source fact.
- A FAQ answer is not equivalent to a current sales policy or production commitment.
- Glossary coverage does not mean the definition is standards-grade.
- A rich resources hub does not prove the engineering team has validated every linked document recently.

## Must Refresh Before Publishing

- Lead time, expedite, MOQ, payment, warranty, and response-time statements
- Capability windows or impedance statements surfaced through FAQ rather than dedicated engineering review
- Update-cadence claims for the library
- Any parameter copied from a linked PDF without checking the underlying source
- Any compliance, certification, or document-availability promise

## Related Fact Cards

- `methods-internal-resource-layer-prompt-support-corpus`
- `methods-pcba-npi-to-mass-production-gates`
- `methods-pcba-stencil-selective-solder-and-fine-pitch-controls`
- `methods-internal-json-coverage-boundary`

## Primary Sources

- /code/hileap/frontendAPT/public/static/resources/en/index.json
- /code/hileap/frontendAPT/public/static/resources/en/dfm-guidelines.json
- /code/hileap/frontendAPT/public/static/resources/en/downloads-materials.json
- /code/hileap/frontendAPT/public/static/resources/en/downloads.json
- /code/hileap/frontendAPT/public/static/resources/en/faq.json
- /code/hileap/frontendAPT/public/static/resources/en/glossary-terms.json
