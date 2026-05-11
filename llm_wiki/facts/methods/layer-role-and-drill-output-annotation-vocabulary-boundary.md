---
fact_id: "methods-layer-role-and-drill-output-annotation-vocabulary-boundary"
title: "Layer-role and drill-output annotation vocabulary can be reused at released-output level without turning tool labels into universal rules"
topic: "layer role and drill output annotation vocabulary boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-10"
source_ids:
  - "ipc-t50-terms-and-definitions-toc"
  - "ucamco-gerber-format-page"
  - "ipc-dpmx-ipc-2581-consortium-home-page"
  - "kicad-official-pcb-design-suite-page"
tags: ["layers", "drill", "annotation", "top-layer", "bottom-layer", "multilayer", "npth", "gerber", "eda", "methods"]
---

# Canonical Summary

> Current official and tool-owner coverage is strong enough to support one narrow released-output vocabulary boundary: top / bottom / multilayer identity and common released-data layer-role terms such as solder mask, legend, and drill may be reused as design-intent and handoff vocabulary, while tool-side labels such as `Drillguide`, `Drilldrawing`, `Drl`, `NPTH`, and blind / buried layer-pair naming may be reused only as output-annotation examples rather than as universal standards or capability proof.

## Stable Facts

- Public IPC terminology-family metadata supports the existence of a controlled terminology context for electronics and interconnection vocabulary.
- Ucamco, as Gerber format owner, publicly supports fabrication-data layer vocabulary such as copper, solder mask, legend, drill, and route data.
- IPC-DPMX / IPC-2581 public identity supports manufacturing-description and transfer-method vocabulary for PCB and assembly handoff context.
- Official KiCad coverage supports vendor-scoped PCB layout and design-tool feature identity, which is enough to keep tool-side naming and released manufacturing data as separate layers.
- Existing repo-backed layer and CAM boundary cards already support the distinction between board-family identity, released manufacturing-data layer families, and tool-side output labels that are useful examples but not neutral standards truth.
- From those layers together, the repo can safely preserve one narrow `E2` rule: layer-role and released-output annotation vocabulary may be reused, but tool-side labels must not be rewritten as universal naming law or process-capability proof.

## Conditions And Methods

- Use this card when a draft needs conservative layer-definition wording for `E2` article rewrites.
- Treat the safe reusable rule as:
  - top layer, bottom layer, and multilayer are safe board-family or layer-role identity surfaces
  - solder mask, legend, and drill are safe released manufacturing-data layer families
  - `Drillguide`, `Drilldrawing`, `Drl`, and `NPTH` may be used as output-annotation vocabulary examples
  - blind / buried layer-pair names may be used as released-output examples only
  - tool naming must stay separate from universal standards or manufacturing closure
- Pair this card with:
  - [ipc-solder-mask-layer-and-pad-definition-boundary.md](/code/blogs/llm_wiki/facts/methods/ipc-solder-mask-layer-and-pad-definition-boundary.md)
  - [cam-data-exchange-format-boundary.md](/code/blogs/llm_wiki/facts/methods/cam-data-exchange-format-boundary.md)
  - [pcb-design-tool-official-feature-identity-boundary.md](/code/blogs/llm_wiki/facts/methods/pcb-design-tool-official-feature-identity-boundary.md)
  - [rigid-board-family-and-layer-boundaries.md](/code/blogs/llm_wiki/wiki/processes/rigid-board-family-and-layer-boundaries.md)
- Keep this card at vocabulary and handoff-annotation level only; if a prompt needs exact drill depth, stackup, layer count, spacing, keepout, or process capability, escalate to narrower primary sources.

## Safe Blog Usage

- Explain that layer names carry design-intent and released-output meaning, not just UI labels.
- Explain that top / bottom / multilayer wording is safe as board-family and layer-role identity.
- Explain that drill and `NPTH` can be discussed as output-annotation vocabulary in handoff packages.
- Explain that tool-side naming examples are useful for communication, but not proof of universal standards or manufacturability.

## Limits And Non-Claims

- This card does not authorize hole-size, board-thickness, layer-count, stackup, or spacing numerics.
- It does not authorize blind / buried capability closure, drill-depth rules, or buildability claims.
- It does not authorize keepout, DRC, or acceptability thresholds.
- It does not authorize claims that tool naming habits are universal standards.
- It does not authorize supplier capability, cost, quality, or schedule claims.
- It does not authorize exact impedance, manufacturability, or CAM-completeness claims.

## Provenance Boundary

- `P4-380` contributes the demand signal that the article groups layer-role names and drill-output labels together.
- Authority comes from the existing public IPC terminology-family metadata, official Gerber and IPC-DPMX format-identity layers, and the official tool-owner boundary already landed in repo.

## Open Questions

- Add a later narrower source lane only if the repo needs stronger official support for named drill-file labels across specific CAD/CAM ecosystems.
- Add a later standards-owner lane only if universal layer-name normalization becomes a public writing requirement.

## Source Links

- https://www.electronics.org/TOC/IPC-T-50N_TOC.pdf
- https://www.ucamco.com/en/gerber
- https://www.ipc2581.com/
- https://www.kicad.org/
