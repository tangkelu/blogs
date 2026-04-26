---
fact_id: "methods-20-layer-any-layer-vocabulary-vs-shop-capability-boundary"
title: "Public any-layer vocabulary for 20-layer boards supports architecture language, not shop-capability or production-approval claims"
topic: "20-layer any-layer vocabulary versus shop capability boundary"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-26"
source_ids:
  - "ipc-2226a-hdi-standard-page"
  - "ipc-jpca-4104-toc"
  - "ipc-2315-legacy-hdi-guide-page"
  - "ats-hdi-anylayer-page"
  - "ventec-ultrathin-build-up-datasheet-page"
  - "ventec-vt-47lt-datasheet-page"
  - "panasonic-felios-frcc-page"
  - "resonac-mcl-hs200-build-up-page"
  - "resonac-mcl-e700g-build-up-page"
  - "resonac-mcl-e705g-build-up-page"
  - "ajinomoto-fine-techno-abf-page"
  - "mgc-bt-materials-page"
  - "isola-sequential-lamination-in-pcbs-note"
tags: ["20-layer", "any-layer", "elic", "anylayer", "vippo", "sbu", "gap-control", "shop-capability-boundary"]
---

# Canonical Summary

> Current public any-layer, `ELIC`, `Anylayer`, `VIPPO`, and `SBU` source coverage is strong enough to preserve guarded architecture vocabulary for `20-layer` discussion. It is not strong enough to turn that vocabulary into shop-capability, geometry freedom, yield, registration, or production-approval claims.

## Stable Facts

- Public `HDI` and build-up sources are usable for guarded architecture vocabulary such as `any-layer`, `ELIC`, `Anylayer`, `SBU`, and microvia-based interconnection.
- Public any-layer vocabulary may remain in `20-layer` writing only as one possible architecture family, not as the default meaning of a `20-layer` board.
- Official supplier pages can show that `any-layer`, `sequential lamination`, and build-up material language coexist in public product positioning without proving generic rigid-board manufacturability.
- Official `AT&S` `Anylayer` wording is usable as supplier-side architecture language for microvia-based interconnection, not as proof of transferable fabrication freedom.
- Official Ventec Ultrathin and `VT-47LT` pages are usable as guarded anchors showing that prepreg-side any-layer and sequential-lamination wording exists on public manufacturer pages.
- Public build-up-material pages for Panasonic `FRCC`, Resonac build-up families, `ABF`, and `BT` are usable as material-form and architecture-context anchors, not as evidence that ordinary rigid `20-layer` boards should inherit any-layer constructions.
- Historical `IPC/JPCA-4104` and legacy `IPC-2315` visibility can support taxonomy or vocabulary context around `HDI` / microvia materials, not current maintained geometry or capability rules.
- Public any-layer or `ELIC` vocabulary does not establish laser-via size, capture-pad size, stacked-height, trace-space, or registration capability for a `20-layer` board.
- Public any-layer or `VIPPO` / `SBU` vocabulary does not establish yield, process stability, release readiness, or production approval for any supplier or route.
- Public supplier-side architecture language may support statements such as `one possible build-up approach`, `architecture variant`, or `publicly positioned as`, but not `factory can deliver`, `supports at scale`, or `approved for production`.
- Public any-layer vocabulary is especially high-risk when mixed with geometry, reliability, or capability claims, so it must stay isolated as architecture wording rather than pseudo-capability evidence.
- Under current governance, any-layer-style wording belongs to boundary control and prompt-safety containment, not numeric recovery or capability promotion.

## Conditions And Methods

- Use this card when a `20-layer` draft needs to mention `any-layer`, `ELIC`, `Anylayer`, `VIPPO`, or `SBU` without turning those terms into implied capability proof.
- Use it to keep architecture wording attached to `possible design approach`, `supplier-side positioning`, or `public vocabulary layer`, not to manufacturability promises.
- Pair it with `facts/methods/20-layer-any-layer-hdi-rewrite-guardrail.md`, `facts/methods/any-layer-hdi-public-boundary-for-20-layer.md`, and `facts/materials/20-layer-build-up-material-boundary-and-non-claims.md`.
- Prefer wording such as `may use`, `may be framed as`, `can involve`, `is publicly described as`, or `should be validated` over `supports`, `achieves`, `guarantees`, or `qualifies`.
- When `VIPPO` or `SBU` appears, keep it attached to architecture/process-family vocabulary rather than to via-geometry, registration, yield, or volume-production claims.
- When supplier material pages mention `high reliability`, `any-layer HDI`, or `sequential lamination`, keep those phrases attached to page-positioning context, not to shop approval or capability inheritance.

## Limits And Non-Claims

- This card does not prove that a `20-layer` board should use any-layer, `ELIC`, `VIPPO`, `SBU`, or stacked-microvia architecture.
- It does not establish geometry freedom, laser-via limits, capture-pad limits, registration control, aspect-ratio capability, or trace-space capability.
- It does not establish yield, cost, lead time, production stability, process maturity, or production approval for any any-layer route.
- It does not turn supplier-side `Anylayer`, `any-layer HDI`, or build-up-material wording into factory-capability evidence.
- It does not convert public vocabulary around build-up materials into qualification proof, accepted process windows, or manufacturing release authority.
- It does not convert historical `IPC` taxonomy or legacy design-reference visibility into current maintained rules for `20-layer` manufacture.

## Open Questions

- Decide whether a later follow-on card should isolate `VIPPO` and via-fill wording from any-layer architecture wording if prompt retrieval still collapses them into capability claims.
- Reassess only if future primary sources provide dated, scoped evidence for shop capability rather than architecture vocabulary alone.

## Source Links

- https://shop.electronics.org/ipc-2226/ipc-2226-standard-only/Revision-a/english
- https://www.electronics.org/TOC/IPC-JPCA-4104.pdf
- https://shop.electronics.org/ipc-2315/ipc-2315-standard-only/Revision-0/english
- https://ats.net/en/products/hdi-printed-circuit-boards/
- https://www.ventec-group.com/cht/products/special-applications/ultrathin/datasheet/
- https://www.ventec-group.com/cht/products/lead-free-assembly/vt-47lt/datasheet/
- https://na.industrial.panasonic.com/products/electronic-materials/circuit-board-materials/felios-series/series/133871
- https://eu.resonac.com/project/hs200/
- https://eu.resonac.com/project/e700gr/
- https://eu.resonac.com/project/e705g/
- https://www.aft-website.com/en/products/insulating_film-abf/
- https://www.mgc.co.jp/eng/products/sc/btprint/
- https://www.isola-group.com/wp-content/uploads/Sequential-Lamination-in-PCBs.pdf
