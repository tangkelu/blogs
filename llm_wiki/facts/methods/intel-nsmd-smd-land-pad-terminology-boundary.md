---
fact_id: "methods-intel-nsmd-smd-land-pad-terminology-boundary"
title: "Intel AN 114 supports NSMD and SMD only as Intel-scoped BGA land-pad distinction vocabulary"
topic: "Intel NSMD and SMD land-pad terminology boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-09"
exact_data_class: "boundary_convention"
scope_type: "manufacturer_scoped_nsmd_smd_land_pad_terminology_boundary"
canonical_unit_policy: "Preserve Intel's original `NSMD` and `SMD` wording plus the documented relationship that `SMD` pads match BGA pad size and `NSMD` pads are about `15%` smaller in this guidance context. Do not normalize this into IPC terminology or a cross-vendor rule."
source_ids:
  - "intel-an114-bga-land-pad-dimensions"
tags: ["intel", "nsmd", "smd", "bga", "land-pad", "terminology", "pad-definition", "vendor-scoped-boundary"]
---

# Canonical Summary

> The local corpus may now reuse one narrower official terminology boundary for `NSMD` and `SMD`, but only inside Intel's `AN 114` BGA land-pad guidance context. Intel's owner documentation is strong enough to show that these are real land-pad distinction terms in manufacturer guidance, that `SMD` pads match the BGA pad size in this documented framing, and that `NSMD` pads are about `15%` smaller. This card does not authorize IPC-defined terminology, universal pad-type selection rules, or cross-vendor equivalence.

## Stable Facts

- Intel `AN 114` publishes printed BGA land-pad recommendation rows under explicit `SMD` and `NSMD` framing.
- Intel's documented guidance context states that `SMD` pads should match the BGA pad size.
- Intel's documented guidance context states that `NSMD` pads should be about `15%` smaller than the BGA pad size.
- Intel's source treats `NSMD` and `SMD` as real land-pad distinction vocabulary inside package-owner guidance.

## Exact Data Scope

- exact for:
  - Intel's use of `NSMD` and `SMD` as official owner-scoped land-pad distinction terms
  - Intel's documented relation that `SMD` pads match BGA pad size in this guidance context
  - Intel's documented relation that `NSMD` pads are about `15%` smaller in this guidance context
- not exact for:
  - IPC terminology definitions
  - all vendors
  - all package families outside Intel's documented guidance context
  - universal preference rules for `NSMD` versus `SMD`

## Conditions And Methods

- Use this card when a prompt needs a named official owner source showing that `NSMD` and `SMD` are real package-guideline terms rather than article-invented labels.
- Keep the wording tied to Intel `AN 114` and BGA land-pad guidance.
- Use this card as vendor-scoped terminology support only.
- Route exact geometry needs to:
  - [intel-bga-land-pad-guidelines-common-pitches-and-vbga.md](/code/blogs/llm_wiki/facts/methods/intel-bga-land-pad-guidelines-common-pitches-and-vbga.md)
  - [ti-bga-pad-geometry-guidelines-1p27-and-1p0-mm-pitch.md](/code/blogs/llm_wiki/facts/methods/ti-bga-pad-geometry-guidelines-1p27-and-1p0-mm-pitch.md)
  - [nxp-bga-footprint-pitch-and-pcb-land-pad-examples.md](/code/blogs/llm_wiki/facts/methods/nxp-bga-footprint-pitch-and-pcb-land-pad-examples.md)

## Safe Blog Usage

- Safe to say that Intel officially uses `NSMD` and `SMD` as BGA land-pad distinction vocabulary in `AN 114`.
- Safe to say that, in Intel's documented guidance context, `SMD` pads match BGA pad size and `NSMD` pads are about `15%` smaller.
- Safe to say that this is owner-scoped guidance vocabulary, not an IPC-normalized definition layer.

## Limits And Non-Claims

- This card does not provide IPC definitions for `mask-defined`, `non-solder-mask-defined`, `NSMD`, or `SMD`.
- It does not authorize universal cross-vendor equivalence between Intel's terminology and other manufacturers' wording.
- It does not authorize universal pad-type selection rules, reliability claims, yield claims, or manufacturability outcome claims.
- It does not authorize solder-mask opening numerics, bridge numerics, via-tenting rules, or acceptance criteria.

## Relationship To E3 Solder-Mask And Pad-Definition Recovery

- This card upgrades the current `E3` solder-mask and pad-definition lane from:
  - `vendor-scoped vocabulary exists in principle`
  - to:
  - `Intel owner guidance gives one narrow reusable terminology boundary for NSMD/SMD`
- It keeps the larger gap explicit:
  - no exact public IPC definitions are yet available in the repo for `mask-defined`, `non-solder-mask-defined`, `via tenting`, or `solder mask bridge`

## Source Links

- https://www.intel.co.jp/content/www/jp/ja/docs/programmable/683481/current/surface-land-pad-dimension
