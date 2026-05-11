---
fact_id: "methods-esd-workstation-grounding-topology-and-wrist-strap-resistor-method-example"
title: "ESD workstation grounding can safely reuse a narrow common-point-ground and 1-megohm wrist-strap method example"
topic: "ESD workstation grounding topology and wrist-strap resistor method example"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-07"
exact_data_class: "method_scoped_exact_data"
scope_type: "standards_adjacent_esd_workstation_grounding_method"
canonical_unit_policy: "Preserve original labels and values such as common point ground, 1 megohm, and 1.0 x 10^6 to 1.0 x 10^9. Do not normalize them into universal compliance thresholds beyond the named workstation-grounding method context."
source_ids:
  - "esda-part-3-basic-esd-control-procedures-and-materials"
  - "desco-1-megohm-resistor-esd-grounding-article"
tags: ["esd", "workstation", "grounding", "common-point-ground", "wrist-strap", "worksurface", "1-megohm", "method-example", "exact-data"]
---

# Canonical Summary

> The local corpus may now reuse one narrow, source-backed ESD workstation grounding method example: operator grounding and workstation grounding can be described through a `common point ground` structure that links the wrist strap and ESD protective worksurface to the same electrical potential, with the wrist-strap current-limiting resistor most commonly described as `1 megohm` in the cited public guidance. This is a standards-adjacent method example only. It does not prove full `ANSI/ESD S20.20` or `IEC 61340-5-1` compliance by itself.

## Exact Data Scope

- exact for:
  - `common point ground` topology language in the admitted sources
  - wrist-strap structure as wristband plus ground cord
  - the public `1 megohm` wrist-strap resistor wording
  - the public worksurface resistance-to-ground range of `1.0 x 10^6` to `1.0 x 10^9`
- not exact for:
  - full audit criteria for an ESD protected area
  - all possible allowed grounding topologies
  - discharge-time requirements
  - page-10 handbook resistance or time-limit tables

## Admitted Data

- ESDA states that workstation components and personnel should first be grounded to the same electrical ground point called the `common point ground`.
- ESDA states that the second step is to connect the `common point ground` to the equipment grounding conductor.
- ESDA states that wrist straps have two major components:
  - the wristband
  - the ground cord that connects the wristband to the `common point ground`
- ESDA states the resistor in most wrist-strap ground cords is most commonly `one megohm`.
- Desco's public standards-adjacent article states that a nominal `1 megohm` resistor is commonly used in wrist straps and to ground work surfaces.
- Desco's public standards-adjacent article states that a wrist-strap cord shall incorporate at least one insulated current-limiting resistor and, when one resistor is used, it is incorporated into the wrist end of the cord.
- ESDA states that ESD protective worksurfaces with a resistance to ground of `1.0 x 10^6` to `1.0 x 10^9` provide a controlled path to ground and are connected to the `common point ground`.
- ESDA states that a typical ESD protective workstation includes:
  - a static dissipative worksurface
  - a means of grounding personnel, usually a wrist strap
  - a `common point ground`

## Conditions And Methods

- Treat this card as one standards-adjacent workstation-grounding method example for ESD-controlled handling of exposed ESDS items.
- Keep the admitted topology attached to the source context:
  - operator grounding
  - common-point grounding
  - grounded worksurface
  - equipment-ground connection
- Use this card when a prompt needs a real public grounding-topology example instead of the secondary PDF page-11 figure alone.
- Pair this card with local asset provenance when the prompt also needs the preserved handbook workstation sketch.

## Limits And Non-Claims

- This card does not authorize page-10 handbook resistance-limit or discharge-time tables.
- It does not authorize generic claims that any pictured workstation is fully compliant with `ANSI/ESD S20.20` or `IEC 61340-5-1`.
- It does not authorize generic device-family sensitivity ranges from handbook page `8`.
- It does not authorize microscope-magnification rules from handbook page `7`.
- It does not authorize reconstructing paid standards text or full conformance criteria from public excerpts.

## Relationship To Local PCB资料 Intake

- This card is the authority-backed replacement for the `B1` page-11 local image lane:
  - `wrist strap`
  - `1 MΩ` path
  - tabletop / worksurface
  - floor mat context
  - `common ground point`
- The preserved local images remain supporting provenance only:
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/a53c51c299b52b94.jpeg`
  - `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-158页-PCBA检验规范汇总/images/f5f2ef8e68729c65.jpeg`

## Provenance

- origin batch:
  - `/code/blogs/tmps/PCB资料`
- motivating secondary-PDF candidate:
  - `P4-215B1` page-11 `ESD-safe workbench grounding layout`
- authority replacement used here:
  - official ESDA fundamentals guidance
  - official Desco standards-adjacent resistor guidance
- exact-data shape:
  - standards-adjacent ESD workstation grounding method example

## Source Links

- https://www.esda.org/esd-overview/esd-fundamentals/part-3-basic-esd-control-procedures-and-materials/
- https://desco.descoindustries.com/Articles/1MegohmResistor.aspx
