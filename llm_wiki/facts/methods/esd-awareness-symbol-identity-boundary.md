---
fact_id: "methods-esd-awareness-symbol-identity-boundary"
title: "ESD awareness symbols can safely reuse standard-scoped identity and application meanings only"
topic: "ESD awareness symbol identity boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-07"
exact_data_class: "standard_scoped_exact_data"
scope_type: "esd-awareness-symbol-identity-and-usage"
canonical_unit_policy: "Preserve the exact public symbol names and their identity-level application meanings. Do not normalize them into packaging or compliance conclusions."
source_ids:
  - "esda-part-3-basic-esd-control-procedures-and-materials"
  - "desco-esd-awareness-symbols-page"
tags: ["esd", "symbols", "s8.1", "esd-susceptibility", "esd-protective", "common-point-ground", "identity", "exact-data"]
---

# Canonical Summary

> The local corpus may now reuse one narrow standard-scoped identity layer for ESD awareness symbols: the `ESD Susceptibility Symbol` identifies ESDS items, the `ESD Protective Symbol` identifies materials or equipment intended to provide ESD protection, and the `ESD Common Point Ground` symbol marks an acceptable common point ground location. This card supports symbol identity and basic application only. It does not prove packaging conformance or full `ANSI/ESD S8.1` compliance.

## Exact Data Scope

- exact for:
  - the public symbol names
  - the public identity-level meanings
  - the basic application split among susceptible items, protective materials, and common point ground
- not exact for:
  - full graphical-spec conformance rules
  - packaging-material qualification
  - label size, placement, or compliance sufficiency in every context

## Admitted Data

- `ANSI/ESD S8.1` covers:
  - `ESD Susceptibility Symbol`
  - `ESD Protective Symbol`
  - `ESD Common Point Ground`
- ESDA explains the `ESD Susceptibility Symbol` as a triangle with a reaching hand and a slash through the hand.
- ESDA explains that the susceptibility symbol is applied directly to integrated circuits, boards, and assemblies that are ESD susceptible.
- ESDA explains the `ESD Protective Symbol` as the reaching hand in the triangle with an arc around the outside in place of the slash.
- ESDA explains that the protective symbol is applied to mats, chairs, wrist straps, garments, packaging, and other items that provide ESD protection.
- Desco explains that the `ESD Common Point Ground` symbol should be used to indicate the location of an acceptable common point ground.

## Conditions And Methods

- Treat this card as one standard-scoped identity card for ESD awareness symbol meanings.
- Use this card when a prompt needs to distinguish:
  - ESD-sensitive item labeling
  - ESD-protective material or equipment labeling
  - common-point-ground location marking
- Pair this card with:
  - [esd-workstation-grounding-topology-and-wrist-strap-resistor-method-example.md](/code/blogs/llm_wiki/facts/methods/esd-workstation-grounding-topology-and-wrist-strap-resistor-method-example.md)
  when the prompt also needs the grounding-method context behind the common point ground symbol.

## Limits And Non-Claims

- This card does not authorize claims that a specific bag, box, mat, or label is compliant simply because a symbol appears on it.
- It does not authorize packaging-performance or shielding-performance claims.
- It does not authorize reconstructing full ANSI/ESD S8.1 graphics requirements, dimensions, or conformance checks from the public summaries.
- It does not authorize using the page-9 handbook images as independent authority.

## Relationship To Local PCB资料 Intake

- This card is the authority-backed replacement for the `B1` page-9 symbol inventory.
- The local page-9 images remain supporting provenance only:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/21847698245d64c1.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/8efef94d0f70554f.jpeg`

## Provenance

- origin batch:
  - `/code/blogs/tmps/PCB资料`
- motivating secondary-PDF candidate:
  - `P4-215B1` page-9 `ESD warning and protection symbols`
- authority replacement used here:
  - official ESDA fundamentals guidance
  - official Desco symbol reference page
- exact-data shape:
  - standard-scoped symbol identity and application meanings

## Source Links

- https://www.esda.org/esd-overview/esd-fundamentals/part-3-basic-esd-control-procedures-and-materials/
- https://desco.descoindustries.com/ESDSymbols.aspx
