---
fact_id: "methods-padstack-origin-pin1-and-footprint-review-governance-boundary"
title: "Padstack, origin, pin-1, and footprint-review vocabulary can be reused as governance language while exact geometry remains blocked"
topic: "Padstack origin pin-1 and footprint review governance boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-07"
source_ids:
  - "frontendapt-glossary-terms-resource-page-en"
  - "frontendapt-dfm-guidelines-resource-page-en"
  - "frontendapt-blog-assembly-drawing-essentials-en"
  - "frontendapt-blog-smt-component-polarity-en"
  - "kicad-getting-started-guide"
  - "kicad-library-conventions-footprint-orientation-and-marking"
  - "frontendapt-resources-index-en"
tags: ["padstack", "origin", "pin-1", "footprint-review", "pad", "solder-mask", "paste-mask", "thermal-relief", "anti-pad", "toe", "heel", "side-clearance"]
---

# Canonical Summary

> Current internal APT resource coverage, the official KiCad getting-started guide, and the reviewed package-lane provenance inventory support a boundary-level governance vocabulary for footprint review: pad-centered terminology, polarity and assembly-document control, guarded CAD-library origin handling, keep-out awareness, and non-numeric review dimensions such as toe, heel, side clearance, pad length, pad width, and inner spacing. The current source layer does not support exact equations, keepout offsets, numeric threshold bands, or vendor-rule workflow claims.

## Stable Facts

- The internal glossary supports reusable layout vocabulary including `Pad`, `Footprint`, `Drill`, `Via`, `Solder Mask`, `Thermal Relief`, and `Keepout`.
- The internal DFM guideline treats pad design as a controlled review topic and routes exact pad requirements to `IPC standards` or `manufacturer-recommended specifications`.
- The internal DFM guideline expects assembly data to include polarity-aware drawings and special process instructions such as coating keep-out areas.
- The internal DFM guideline also treats footprint libraries and package choice as part of PCBA DFM review, which supports a governance posture for origin / marking / package-review completeness.
- The internal `Assembly Drawing Essentials` blog strengthens the documentation-governance posture that pin-1, polarity, and special assembly notes should be explicit in the released assembly package rather than left to operator inference.
- The internal `SMT Component Polarity` blog strengthens the qualitative posture that pin-1 indicators, zero-orientation discipline, and assembly-drawing polarity annotation belong to controlled footprint and inspection workflow, while exact package-specific rules remain outside this card.
- The official KiCad getting-started guide adds a CAD-owner convention that the documented through-hole footprint workflow places `pin 1` at `(0,0)` and orients `pin 1` at the top left, which is useful as software-library convention support rather than package-owner or standards-owner truth.
- The same KiCad guide explicitly points readers to `KLC` as the basis for official KiCad symbol and footprint libraries, which strengthens the idea that footprint origin and documentation choices live inside controlled library conventions.

## Conditions And Methods

- Use `pad`, `drill`, `via`, `solder mask`, `paste mask`, `thermal relief`, and `anti pad` as review vocabulary, not as numeric defaults.
- Use `origin`, `pin-1 mark`, `polarity mark`, and `installation mark` as documentation-governance markers that help keep footprint intent auditable.
- Use the KiCad through-hole `pin 1 @ (0,0)` pattern only as guarded CAD-library convention support when discussing origin discipline or library review posture.
  Do not rewrite it as a universal industry mandate.
- Use `toe`, `heel`, and `side clearance` as non-numeric lead-to-pad review dimensions.
- Use `pad length`, `pad width`, and `inner spacing` as non-numeric chip-footprint review dimensions.
- Use review-band labels such as `optimal`, `general`, `risk`, and `danger` only as local severity vocabulary if needed for internal checklist wording.
  Do not import any handbook threshold values behind those labels.
- When exact geometry is needed, route prompts to package-owner recommendations, manufacturer-recommended land patterns, or named standards rather than this boundary card.
- For BGA or CSP geometry already replaced by official owner sources in this repo, route to:
  - [nxp-1p50mm-bga225-reflow-footprint.md](/code/blogs/llm_wiki/facts/methods/nxp-1p50mm-bga225-reflow-footprint.md)
  - [nxp-bga-footprint-pitch-and-pcb-land-pad-examples.md](/code/blogs/llm_wiki/facts/methods/nxp-bga-footprint-pitch-and-pcb-land-pad-examples.md)
  - [ti-bga-pad-geometry-guidelines-1p27-and-1p0-mm-pitch.md](/code/blogs/llm_wiki/facts/methods/ti-bga-pad-geometry-guidelines-1p27-and-1p0-mm-pitch.md)
  - [microchip-csp-bga-solder-land-and-pitch-examples.md](/code/blogs/llm_wiki/facts/methods/microchip-csp-bga-solder-land-and-pitch-examples.md)
  - [microchip-0p75mm-tfbga-land-pattern-4lx.md](/code/blogs/llm_wiki/facts/methods/microchip-0p75mm-tfbga-land-pattern-4lx.md)
  - [microchip-0p75mm-tfbga-land-pattern-7g.md](/code/blogs/llm_wiki/facts/methods/microchip-0p75mm-tfbga-land-pattern-7g.md)
  - [microchip-0p75mm-tfbga-land-pattern-bab.md](/code/blogs/llm_wiki/facts/methods/microchip-0p75mm-tfbga-land-pattern-bab.md)
  - [renesas-0p75mm-fbga-package-land-pattern-bcg48d1.md](/code/blogs/llm_wiki/facts/methods/renesas-0p75mm-fbga-package-land-pattern-bcg48d1.md)
  - [intel-bga-land-pad-guidelines-common-pitches-and-vbga.md](/code/blogs/llm_wiki/facts/methods/intel-bga-land-pad-guidelines-common-pitches-and-vbga.md)
- For connector-origin and installation-mark wording that needs stronger official support than local handbook context, route to:
  - [connector-origin-and-installation-mark-boundary.md](/code/blogs/llm_wiki/facts/methods/connector-origin-and-installation-mark-boundary.md)
- For standards-owner zero-orientation wording in CAD-library construction, route to:
  - [iec-zero-orientation-cad-library-construction-boundary.md](/code/blogs/llm_wiki/facts/methods/iec-zero-orientation-cad-library-construction-boundary.md)
- For stronger public `pin-1` and polarity-identification wording at component-specification level, route to:
  - [iec-smd-component-marking-boundary.md](/code/blogs/llm_wiki/facts/methods/iec-smd-component-marking-boundary.md)

## Safe Blog Usage

- Explain that footprint review checks both geometry meaning and documentation completeness.
- Explain that pad and mask terms identify different layers or review objects, not automatically approved dimensions.
- Explain that polarity, pin-1, and origin information should be explicit in the design package.
- Explain that leaded and chip-package reviews use different geometric dimensions and should not be collapsed into one generic check.

## Provenance Inventory From Secondary-PDF Lanes

The following logs are provenance inventory only and do not act as authority:

- `/code/blogs/llm_wiki/logs/p4-215c2-2026-5-6-package-lane-c2-pad-origin-pin1-keepout-drawings.md`
- `/code/blogs/llm_wiki/logs/p4-215c3-2026-5-6-package-lane-c3-library-governance-and-hole-pad-examples.md`
- `/code/blogs/llm_wiki/logs/p4-219-2026-5-7-pcb-pdf-post-round-3-promotion-review-resume-entry.md`

What they contribute safely:

- claim inventory for padstack layer-role vocabulary
- structural-context inventory for non-numeric review dimensions
- evidence that vendor UI screenshots and handbook thresholds must stay blocked

## Limits And Non-Claims

- This card does not authorize pad / drill formulas or compensation equations.
- It does not authorize exact keepout distances, silkscreen offsets, or grouped-pin mark sizes.
- It does not authorize exact BGA pitch-to-pad tables or package-family-specific land-pattern dimensions.
- It does not authorize threshold numerics for `toe`, `heel`, `side clearance`, `pad length`, `pad width`, or `inner spacing`.
- It does not authorize any vendor `DFM` workflow, menu path, or rule-management UI as neutral authority.
- It does not authorize universal connector-origin defaults, package-owner land-pattern origin mandates, or standards-grade installation-mark conventions.

## Open Questions

- Recover stronger authority later for package-family-specific marking conventions and package-land-pattern conventions if later prompts need package-owner or fully licensed standards wording beyond the current zero-orientation and public component-marking layers.
- Recover stronger source support later for lead-to-pad and chip-pad dimension terminology if those terms will be used outside guarded governance contexts.
- Add a narrower exact-data lane later only when package-owner or standards-owner sources exist for numeric land-pattern guidance.

## Source Links

- /code/hileap/frontendAPT/public/static/resources/en/glossary-terms.json
- /code/hileap/frontendAPT/public/static/resources/en/dfm-guidelines.json
- /code/hileap/frontendAPT/public/static/blogs/2025/06/en/assembly-drawing-essentials.md
- /code/hileap/frontendAPT/public/static/blogs/2025/06/en/smt-component-polarity.md
- /code/hileap/frontendAPT/public/static/resources/en/index.json
