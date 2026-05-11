---
source_id: "esda-part-3-basic-esd-control-procedures-and-materials"
title: "EOS/ESD Fundamentals Part 3 - Basic ESD Control Procedures and Materials"
organization: "EOS/ESD Association, Inc."
owner: "EOS/ESD Association, Inc."
source_type: "association_technical_guidance"
url: "https://www.esda.org/esd-overview/esd-fundamentals/part-3-basic-esd-control-procedures-and-materials/"
jurisdiction: "global"
published_at: "2020"
checked_at: "2026-05-07"
retrieved_at: "2026-05-07"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
original_source_language: "en"
authority_class: "association_technical_guidance"
exact_data_class: "method_scoped_exact_data"
scope_type: "standards_adjacent_esd_workstation_grounding_method"
source_origin_path: "official ESDA fundamentals page"
source_page_range: "Grounding, Wrist Straps, Flooring, Workstations and Work Surfaces sections"
confidence: "medium"
topic_tags: ["esd", "workstation", "grounding", "common-point-ground", "wrist-strap", "worksurface", "flooring", "1-megohm", "method-example"]
status: "active"
notes: "Official ESDA fundamentals page. Safe for workstation-grounding topology, common-point-ground terminology, wrist-strap structure, common 1 megohm wrist-strap resistor wording, and worksurface-to-ground resistance range under ESDA's educational framing. Do not treat this page as clause-complete ANSI/ESD S20.20 proof."
---

# Source Summary

## What It Covers

- ESDA explains `common point ground` as the same electrical ground point for workstation components and personnel
- ESDA states that wrist straps are the primary means of grounding seated personnel handling exposed ESDS items
- ESDA states that wrist straps have a wristband and a ground cord connected to the `common point ground`
- ESDA states the current-limiting resistor in most wrist-strap cords is most commonly `one megohm`
- ESDA states a typical workstation includes a static dissipative worksurface, personnel grounding, a common point ground, and signage
- ESDA states ESD protective worksurfaces with resistance to ground of `1.0 x 10^6` to `1.0 x 10^9` provide a controlled electrical path to ground and are connected to the `common point ground`

## Why It Matters

- Gives `/code/blogs/tmps/PCB资料` a strong public association-backed replacement for the page-11 workstation-grounding topology shown in the secondary PCBA handbook
- Supports English-only canonical storage for `common point ground`, `wrist strap`, `worksurface`, and coordinated operator/workstation grounding structure

## Extraction Notes

- Safe for the two-step grounding method:
  - ground workstation components and personnel to the same `common point ground`
  - then connect that `common point ground` to the equipment grounding conductor
- Safe for wrist-strap structure:
  - wristband
  - ground cord
  - connection to `common point ground`
- Safe for ESDA's wording that the wrist-strap resistor is most commonly `one megohm`
- Safe for worksurface grounding range:
  - `1.0 x 10^6` to `1.0 x 10^9`
- Safe for workstation elements:
  - dissipative worksurface
  - personnel grounding
  - `common point ground`
  - optional monitors and accessories
- Do not use this page to reconstruct complete standards tables, audit criteria, or clause-level compliance acceptance

## Refresh Notes

- Refresh before reusing for current standards cross-reference wording because the page is dynamic educational guidance
- Keep all admitted values and topology claims tied to ESDA's educational workstation method framing
