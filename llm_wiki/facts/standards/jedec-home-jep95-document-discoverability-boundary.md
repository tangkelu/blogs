---
fact_id: "standards-jedec-home-jep95-document-discoverability-boundary"
title: "Public JEDEC homepage shows document-search and JEP95 discoverability, not recoverable geometry content"
topic: "JEDEC homepage JEP95 discoverability boundary"
category: "standards"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-12"
source_ids:
  - "jedec-home-document-search-and-jep95-discoverability"
tags: ["jedec", "jep95", "registered-outlines", "document-search", "discoverability", "boundary"]
---

# Canonical Summary

> The public JEDEC homepage is strong enough to show that JEDEC officially exposes document-search discoverability and publicly names `Registered Outlines: JEP95` as a standards/publication family. This strengthens the standards-side discoverability wording for the `1.50 mm` package lane. It does not recover public geometry content, land-pattern criteria, or one exact `1.50 mm` row.

## Stable Facts

- Public JEDEC homepage access exists.
- The public homepage visibly exposes:
  - `Search & Download JEDEC Documents`
  - `Search by keyword or document number`
- The public homepage visibly lists:
  - `Registered Outlines: JEP95`
- The public homepage therefore gives the repo one official JEDEC discoverability anchor above generic `JEDEC primary lane exists` wording alone.

## Conditions And Methods

- Use this card when a prompt needs to explain that JEDEC official-public discoverability for `JEP95` is real, even though recoverable exact BGA geometry is still not in hand.
- Pair this card with:
  - [bga-1p50mm-pitch-standards-existence-boundary.md](/code/blogs/llm_wiki/facts/methods/bga-1p50mm-pitch-standards-existence-boundary.md)
  - [j-std-013-cbga-pbga-land-pattern-topic-visibility-boundary.md](/code/blogs/llm_wiki/facts/standards/j-std-013-cbga-pbga-land-pattern-topic-visibility-boundary.md)
  - [ipc-7095e-bga-clause-title-visibility-boundary.md](/code/blogs/llm_wiki/facts/standards/ipc-7095e-bga-clause-title-visibility-boundary.md)
- Keep the safe reusable rule at:
  - public JEDEC homepage = document-search and JEP95 discoverability
  - public JEDEC homepage != JEP95 geometry payload
  - public JEDEC homepage != exact replacement row

## Limits And Non-Claims

- This card does not provide `1.50 mm` land-pattern geometry.
- It does not provide JEP95 outline dimensions, pad diameters, or solder-mask criteria.
- It does not prove public free access to JEP95 contents.
- It does not reopen the `1.50 mm` residual by itself.

## Relationship To Local PCB资料 Intake

- This card narrows the JEDEC side from a vague primary-lane hypothesis to one official-public discoverability anchor.
- It helps explain that `JEP95` is not imaginary or purely secondary-search noise, while still keeping the current repo below public-geometry recovery.

## Source Links

- https://www.jedec.org/
