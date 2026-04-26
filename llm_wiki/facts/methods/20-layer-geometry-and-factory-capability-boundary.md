---
fact_id: "methods-20-layer-geometry-and-factory-capability-boundary"
title: "20-layer any-layer, build-up, process, and reliability sources must not be rewritten as geometry or factory-capability proof"
topic: "20-layer geometry and factory capability boundary"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-26"
source_ids:
  - "ipc-2226a-hdi-standard-page"
  - "ipc-jpca-4104-toc"
  - "ipc-2315-legacy-hdi-guide-page"
  - "ipc-microvia-reliability-warning-2019"
  - "ipc-tr-486-ist-round-robin-page"
  - "ipc-tm650-test-methods-index"
  - "ipc-tm650-method-development-packet-page"
  - "ipc-standards-related-resources-page"
  - "nasa-nepp-program-overview-2019"
  - "nasa-workmanship-page"
  - "isola-sequential-lamination-in-pcbs-note"
  - "shengyi-s7439-processing-guide"
  - "is410-processing-guide"
  - "agc-fastrise-family-page"
  - "agc-bond-plies-prepregs-page"
  - "agc-meteorwave-1000nf-page"
  - "ventec-vt-47lt-datasheet-page"
  - "ventec-pro-bond-4c-vt-464lt-rcc-datasheet-page"
  - "ventec-ultrathin-build-up-datasheet-page"
  - "panasonic-felios-frcc-page"
  - "mitsui-rcc-engineered-materials-page"
  - "doosan-dsf-900sq-page"
  - "ats-hdi-anylayer-page"
tags: ["20-layer", "geometry", "factory-capability", "any-layer", "build-up", "process-window", "boundary", "gap-control"]
---

# Canonical Summary

> Public any-layer, build-up, process-guide, and interconnect-reliability sources are strong enough to support guarded `20-layer` containment wording in `llm_wiki`: dense multilayer structures can be more geometry-sensitive, more registration-sensitive, and more process-sensitive than simpler rigid multilayer builds. They are not strong enough to authorize trace/space, drill or via minima, aspect-ratio, annular-ring, registration, stack recipe, lamination-count, or factory-capability claims for a specific `20-layer` build.

## Stable Facts

- A conservative `20-layer` rewrite may state that dense multilayer and build-up-oriented structures create tighter geometry and registration sensitivity than simpler through-hole multilayer work.
- Public `HDI`, `any-layer`, `ELIC`, and build-up material pages support architecture and material-form vocabulary, not reusable feature-size or capability tables.
- Public reliability and method-governance pages support the idea that interconnect risk increases with more demanding structures, not that any public geometry value is approved or qualified.
- Public sequential-lamination and process-guide sources support sensitivity framing around drilling, desmear, lay-up, bonding layers, and repeated lamination, not transferable numeric manufacturing windows.
- Public `RCC`, `FRCC`, `bond ply`, `no-flow prepreg`, and ultrathin build-up pages support guarded material-form context, not dielectric-thickness defaults, laser-via rules, or stack recipes for ordinary rigid `20-layer` boards.
- Public supplier-side phrases such as `Any-layer HDI`, `Sequential Laminations`, `High Reliability for HDI Designs`, and similar positioning language must stay attached to supplier context rather than being promoted into generic shop capability.
- Public IPC method/report and resource metadata support named evaluation context, representative-coupon context, and method-governance context, not trace/space minima, via-size minima, or registration allowances.
- Public NASA workmanship and assurance-hierarchy vocabulary supports documented evaluation and controlled-process framing, not finished-board capability proof or transferable fabrication limits.
- These sources together support guarded wording such as `may require tighter geometry control`, `should be validated`, and `belongs in a higher-sensitivity planning context`.
- These sources do not support wording such as `supports 2.5/2.5 mil`, `supports 3 mil laser vias`, `supports N:1 aspect ratio`, `holds +/- X registration`, `uses N sequential laminations`, or `factory can reliably build this geometry`.

## Conditions And Methods

- Use this card when a `20-layer` draft mentions `any-layer`, `ELIC`, `stacked microvias`, `sequential lamination`, `RCC`, `FRCC`, `bond ply`, `ultrathin build-up`, or `HDI process` near geometry or capability language.
- Pair this card with `facts/methods/20-layer-any-layer-hdi-rewrite-guardrail.md`, `facts/methods/20-layer-process-window-and-recipe-boundary.md`, and `facts/methods/20-layer-method-vs-qualification-boundary.md`.
- Prefer wording such as `geometry-sensitive`, `registration-sensitive`, `process-sensitive`, `may require tighter control`, and `requires case-specific validation`.
- Keep supplier-page, process-guide, and reliability-page wording attached to architecture context, material-form context, or workflow context rather than capability numerics.
- Use this card to block prompt-side leakage from build-up vocabulary into `trace/space`, `drill/via`, `aspect ratio`, `feature size`, `registration`, `stack recipe`, or `factory capability` claims.

## Limits And Non-Claims

- This card does not provide trace/space minima, drill minima, laser-via diameters, capture-pad sizes, annular-ring values, aspect-ratio limits, registration tolerances, copper-thickness windows, or stacked-via height limits.
- It does not provide stack recipes, lamination counts, bake/cure windows, via-fill recipes, or accepted build sequences for a `20-layer` board.
- It does not turn `HDI`, `any-layer`, `ELIC`, `RCC`, `FRCC`, `bond ply`, or supplier build-up positioning into factory-capability proof.
- It does not turn method names, coupon-resource wording, reliability warnings, or workmanship vocabulary into manufacturability guarantees, approval, or production-readiness claims.
- It does not authorize evidence-pack reuse of feature-size numbers or shop promises unless those exact claims are separately supported by current primary authority.

## Open Questions

- Add a narrower follow-on only if future work needs a dedicated split between `geometry leakage` and `shop capability leakage`.
- Reassess `20-layer` readiness only after current primary sources exist for the exact feature-size or factory-capability claim class.

## Source Links

- https://shop.electronics.org/ipc-2226/ipc-2226-standard-only/Revision-a/english
- https://www.electronics.org/TOC/IPC-JPCA-4104.pdf
- https://shop.electronics.org/ipc-2315/ipc-2315-standard-only/Revision-0/english
- https://www.ipc.org/news-release/ipc-issues-electronics-industry-warning-printed-board-microvia-reliability-high
- https://shop.electronics.org/technical-reports-white-papers/studytechnical-report
- https://www.electronics.org/test-methods
- https://www.ipc.org/ipc-tm-650-method-development-packet
- https://www.ipc.org/ipc-standards-related-resources
- https://ntrs.nasa.gov/citations/20190001800
- https://sma.nasa.gov/sma-disciplines/workmanship
- https://www.isola-group.com/wp-content/uploads/Sequential-Lamination-in-PCBs.pdf
- https://www.syst.com.cn/uploadfiles/2018/10/20181027173559031.pdf
- https://www.isola-group.com/wp-content/uploads/is410-laminate-and-prepreg-processing-guide.pdf
- https://www.agc-multimaterial.com/fastrise/
- https://www.agc-multimaterial.com/bond-plies-prepregs/
- https://www.agc-multimaterial.com/meteorwave-1000nf/
- https://www.ventec-group.com/cht/products/lead-free-assembly/vt-47lt/datasheet/
- https://www.ventec-group.com/cht/products/bondply/pro-bond-4c-vt-464lt-rcc/datasheet/
- https://www.ventec-group.com/cht/products/special-applications/ultrathin/datasheet/
- https://na.industrial.panasonic.com/products/electronic-materials/circuit-board-materials/felios-series/series/133871
- https://www.mitsui-kinzoku.com/en/seihin/engineered_materials/
- https://www.doosanelectronics.com/en/product/Copper_Clad_Laminate/DSF-900SQ
- https://ats.net/en/products/hdi-printed-circuit-boards/
