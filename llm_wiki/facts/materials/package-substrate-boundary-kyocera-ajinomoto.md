---
fact_id: "materials-package-substrate-boundary-kyocera-ajinomoto"
title: "KYOCERA FC-BGA and Ajinomoto ABF sources define a package-substrate context distinct from ordinary HDI PCB claims"
topic: "package substrate and IC substrate boundary context"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-28"
source_ids:
  - "kyocera-fcbga-package-substrate-page"
  - "ajinomoto-abf-innovation-story"
  - "ajinomoto-fine-techno-abf-page"
tags: ["package-substrate", "ic-substrate", "fcbga", "abf", "build-up", "kyocera", "ajinomoto", "2025-10-25"]
---

# Canonical Summary

> KYOCERA's build-up FC-BGA page and Ajinomoto's ABF pages support a package-substrate context that should not be flattened into ordinary HDI PCB language. KYOCERA provides a specific FC-BGA package-substrate example with fine build-up geometry and flip-chip context; Ajinomoto frames ABF as an interlayer insulation material for complex circuit substrates used in high-performance CPU / semiconductor package substrates. These sources do not define a universal PCB-vs-IC-substrate cutoff or prove any supplier's IC-substrate capability.

## Stable Facts

- KYOCERA frames build-up FC-BGA substrates as semiconductor package substrates for next-generation flip-chip LSI.
- KYOCERA's FC-BGA page lists example product-family specifications including more than `3,000 I/Os`, build-up line/space `9 um / 12 um`, via land diameter `85 um`, core line width `30 um`, core space `45 um`, and flip-chip pitch `100 um`.
- KYOCERA's FC-BGA page mentions laser via technology and thermosetting epoxy in the package-substrate context.
- Ajinomoto frames ABF as an interlayer insulation material used in complex circuit substrates for high-performance CPUs.
- Ajinomoto Fine-Techno frames ABF as an insulating film for semiconductor and high-performance CPU substrate contexts.

## Conditions And Methods

- Use this card when a `2025.10.25` HDI or IC-substrate-adjacent draft needs to explain that package substrates are a different context from ordinary board-level HDI marketing.
- Keep KYOCERA numeric examples tied to the KYOCERA FC-BGA product-family page.
- Use ABF language at class / product-family level unless grade-specific Ajinomoto sources are added.

## Limits And Non-Claims

- This card does not set a universal line/space, via, bump-pitch, I/O-count, layer-count, or warpage cutoff between HDI PCBs and IC substrates.
- It does not prove HILPCB, Highleap, or APTPCB can manufacture KYOCERA-style FC-BGA substrates, ABF substrates, SAP structures, stacked vias, or flip-chip packages.
- It does not authorize 2.5D, fan-out, AI, GPU, server, or advanced-package readiness claims unless separately sourced.
- It does not provide price, lead time, MOQ, stock, yield, throughput, or qualification claims.

## Open Questions

- Add SHINKO or other official package-substrate sources if future writing needs semi-additive process, stacked-via, or interposer-build-up integration context.
- Add a public IC-substrate boundary wiki page if package-substrate topics become recurring blog targets.

## Source Links

- https://global.kyocera.com/prdct/organic/prdct/package/fcbga/std/
- https://www.ajinomoto.com/innovation/our_innovation/buildupfilm
- https://www.aft-website.com/en/products/insulating_film-abf/
