---
topic_id: "processes-selective-solder-fixture-and-access-planning"
title: "Selective Solder Fixture and Access Planning"
category: "processes"
status: "draft"
last_reviewed_at: "2026-04-27"
fact_ids:
  - "methods-selective-solder-design-access-checks"
  - "methods-selective-wave-solder-and-mixed-technology-sequencing"
  - "methods-tht-heavy-assemblies-power-and-medical-context"
  - "methods-pcba-mixed-technology-assembly-flow"
  - "methods-mixed-technology-lane-b-rewrite-gate"
source_ids:
  - "frontendapt-pcba-pcb-selective-soldering-page-en"
  - "frontendapt-pcba-smt-tht-page-en"
  - "frontendhil-through-hole-assembly-product-page-en"
  - "frontendapt-blog-selective-solder-design-en"
  - "frontendapt-blog-wave-solder-fixture-intro-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-fct-test-page-en"
tags: ["selective-solder", "wave-solder", "fixture", "access-planning", "mixed-technology", "medical", "inverter"]
---

# Definition

> Selective-solder fixture and access planning is the review step that decides whether mixed-technology through-hole joints are reachable and supportable by selective solder, palletized wave solder, or manual exceptions without breaking nearby SMT protection, board support, or downstream verification.

## Why This Topic Matters

- Route-selection articles get weak when they say `use selective solder for dense boards` without explaining what makes a joint reachable in production.
- The current corpus can support a stronger, practical frame: access, shielding, support, thermal demand, and inspection handoff are the real planning variables.
- This topic gives later medical and inverter rewrites a way to discuss design review inputs without drifting into unsupported numeric process windows.

## Stable Facts

- Selective solder is supported in the corpus as a targeted mixed-technology route for through-hole joints that should not be exposed to blanket wave conditions.
- Wave solder remains supported where through-hole populations and layout make broader exposure practical, especially when fixtures can shield vulnerable areas and support the board.
- Fixtures and pallets solve one class of problem while introducing another: they can protect bottom-side SMT and stabilize the board, but poor opening geometry or wall placement can create shadowing and incomplete solder reach.
- Access review is both geometric and thermal. A reachable joint can still be a poor candidate if nearby mass, copper attachment, or hardware overhang makes localized heating uneven.
- Inspection and electrical validation remain part of the same process route; the solder plan should be checked against how joints will later be inspected, sampled, and electrically verified.

## Route-Selection Checklist

- Identify the exact through-hole population: localized connectors and terminals, repeated rows, power hardware, or mixed one-off joints.
- Review component neighborhoods around each joint group: nearby SMT, tall bodies, sensitive devices, shields, brackets, and connector housings.
- Decide whether the board needs localized solder access only, broader wave exposure with shielding, or a mixed route with manual exceptions.
- Review board support needs: thin sections, uneven mass, double-sided population, panel rails, and whether a fixture or carrier changes reachability.
- Review thermal demand grouping: heavy copper ties, large pins, magnetic parts, and chassis-linked hardware that may pull heat away from some joints.
- Define the verification handoff: visual review, X-ray sampling, ICT/FCT accessibility, and any release checkpoints that should influence route choice upstream.

## How To Use In Lane B Rewrites

- For `selective-wave-soldering-medical-imaging-wearable`, write the article as a compact mixed-technology routing guide: localized through-hole joints, nearby SMT protection, and inspection handoff.
- For `tht-through-hole-soldering-medical-imaging-wearable`, use this topic to explain why some interfaces stay through-hole inside a mostly SMT product and how access or shielding affects the route.
- For `tht-through-hole-soldering-renewable-energy-inverter`, use this topic to explain how larger terminals or magnetic hardware change support and thermal-demand review without turning the article into a numeric power-design piece.

## Must Not Publish From This Topic Alone

- Exact keep-out distances, nozzle diameters, fixture-opening dimensions, wall thickness, chamfer angles, preheat temperatures, dwell times, or pot settings
- Barrel-fill thresholds, plating-thickness requirements, cleanliness thresholds, or IPC class-specific acceptability values
- Cost, lead-time, throughput, yield, or universal reliability claims
- Medical compliance, sterilization compatibility, current rating, efficiency, thermal-rise, or lifetime claims

## Related Facts

- `methods-selective-solder-design-access-checks`
- `methods-selective-wave-solder-and-mixed-technology-sequencing`
- `methods-tht-heavy-assemblies-power-and-medical-context`
- `methods-mixed-technology-lane-b-rewrite-gate`

## Primary Sources

- /code/hileap/frontendAPT/public/static/pcba/en/pcb-selective-soldering.json
- /code/hileap/frontendAPT/public/static/pcba/en/smt-tht.json
- /code/hileap/frontendHIL/public/static/products/en/through-hole-assembly.json
- /code/hileap/frontendAPT/public/static/blogs/2025/12/en/selective-solder-design.md
- /code/hileap/frontendAPT/public/static/blogs/2025/12/en/wave-solder-fixture-intro.md
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendAPT/public/static/pcba/en/fct-test.json
