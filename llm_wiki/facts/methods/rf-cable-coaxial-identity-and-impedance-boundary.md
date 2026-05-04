---
fact_id: "methods-rf-cable-coaxial-identity-and-impedance-boundary"
title: "RF cable writing is source-backed only for coaxial-centered identity and impedance context, not for universal taxonomy or selection rules"
topic: "RF cable coaxial identity and impedance boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-30"
source_ids:
  - "amphenol-rf-coaxial-cable-guide"
  - "times-microwave-semi-rigid-coaxial-cables-page"
  - "te-connectivity-bnc-connectors-page"
  - "keysight-vna-system-impedance-help"
  - "keysight-e5055a-measurement-parameters-help"
  - "frontendapt-pcba-cable-assembly-page-en"
tags: ["rf-cable", "coaxial-cable", "semi-rigid", "micro-coax", "50-ohm", "75-ohm", "impedance-boundary"]
---

# Canonical Summary

> Current official cable-owner, connector-owner, and measurement-owner sources support a conservative RF-cable boundary only at coaxial-centered identity level: coaxial cable structure vocabulary, semi-rigid and micro-coax as coaxial-family variants, and impedance-matching context including official `50 ohm` and `75 ohm` coaxial ecosystems. These sources do not authorize broad RF-cable taxonomy, application-fit rules, performance comparisons, or supplier-selection claims.

## Stable Facts

- Amphenol RF's official guide supports coaxial cable structure vocabulary centered on a center conductor, dielectric, metallic shield, and outer insulating layer.
- The same Amphenol RF guide supports naming `semi-rigid` and `micro-coaxial` as coaxial-family variants.
- Times Microwave Systems' official family page supports `semi-rigid coaxial cables` as a real cable-owner family.
- TE Connectivity's official BNC connector family page supports the existence of both `50 ohm` and `75 ohm` coaxial connector variants.
- The current Keysight measurement-source layer supports `50 ohm` as a measurement-reference context and supports related RF reflection vocabulary such as return loss, SWR, and impedance as measurement-family terms.
- The current internal APT cable-assembly page remains useful only as adjacent integration context for cable fabrication and assembly, not as proof of RF performance or custom-cable service claims.

## Conditions And Methods

- Use this card for `/code/blogs/tmps/2025.11.10/en/radio-frequency-cable.md` only after reducing the article to coaxial-centered identity and interconnect-boundary wording.
- Safe posture: describe coaxial cable structure, note that semi-rigid and micro-coax are coaxial-family variants, and keep impedance matching at boundary level.
- Safe impedance posture: say characteristic impedance matters in RF interconnect paths and that official coaxial ecosystems include both `50 ohm` and `75 ohm` variants.
- Pair this card with measurement-boundary layers if a draft also mentions return loss, SWR, TDR, or VNA vocabulary.
- Require narrower owner datasheets or dated capability records before publishing product-family comparisons, attenuation claims, or custom-cable service language.

## Limits And Non-Claims

- This card does not authorize a full generic RF-cable taxonomy covering `coaxial`, `semi-rigid`, `micro-coax`, `twinax`, and `triax` as equally supported article branches.
- It does not authorize `RG-58`, `RG-213`, `LMR`, or similar example-family application-fit claims.
- It does not authorize universal rules such as `50 ohm for communications` or `75 ohm for broadcast`.
- It does not authorize low-loss, shielding-effectiveness, crosstalk, durability, long-distance, or environmental-suitability claims.
- It does not authorize sector application mapping for telecom, aerospace, medical, automotive, IoT, or test equipment.
- It does not prove sourcing difficulty, custom-manufacturer quality, lead time, integration capability, or any HIL/APT RF cable service claim.

## Open Questions

- Add a stronger official `twinax` identity source only if future drafts must keep that branch.
- Add a stronger official `triax` identity source only if future drafts must keep that branch outside instrumentation context.
- Add exact cable-owner or connector-owner sources only if future drafts need bounded attenuation, VSWR, or product-family language.

## Source Links

- https://www.amphenolrf.com/en-us/engineering-center/engineering-resources/coaxial-cable-guide/
- https://timesmicrowave.com/cable-families/semi-rigid-coaxial-cables/
- https://www.te.com/en/products/connectors/rf-connectors/coax-connectors/intersection/bnc-connectors.html
- https://helpfiles.keysight.com/csg/N52xxB/System/System_Impedance.htm
- https://helpfiles.keysight.com/csg/e5055a/S1_Settings/Measurement_Parameters.htm
- /code/hileap/frontendAPT/public/static/pcba/en/cable-assembly.json
