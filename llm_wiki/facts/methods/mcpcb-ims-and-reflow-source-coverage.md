---
fact_id: "methods-mcpcb-ims-and-reflow-source-coverage"
title: "MCPCB assembly evidence needs both IMS material anchors and solder-paste-specific reflow guidance"
topic: "MCPCB IMS and reflow source coverage"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids:
  - "ventec-ims-family-overview"
  - "ventec-vt-4b7-datasheet"
  - "indium-reflow-profile-to-paste-spec"
  - "indium-8-9hf-solder-paste-pds"
  - "kester-standard-reflow-profile"
  - "frontendapt-pcb-metal-core-pcb-page-en"
  - "frontendhil-metal-core-pcb-product-page-en"
  - "frontendapt-pcb-high-thermal-pcb-page-en"
tags: ["mcpcb", "ims", "metal-core", "thermal-management", "reflow", "solder-paste", "source-coverage"]
---

# Canonical Summary

> MCPCB assembly should be framed as a combined thermal-platform and soldering-process problem: IMS/metal-core materials define thermal and dielectric context, while reflow profiles must be matched to solder paste, assembly thermal mass, and process validation.

## Stable Facts

- Ventec tec-thermal provides official IMS / metal-base laminate family context.
- Ventec VT-4B7 provides a product-level IMS datasheet anchor for MCPCB/thermal-management examples.
- Indium's reflow guidance supports matching a measured reflow profile to the solder-paste specification.
- Product-specific solder-paste data sheets can provide example profile windows, but those windows are not universal process rules.
- Internal APT/HIL metal-core and high-thermal PCB pages support service-context framing, not product-material guarantees.

## Conditions And Methods

- Use this card for MCPCB, high-thermal PCB, LED board, and thermal assembly articles.
- Separate material selection, stencil/paste selection, reflow profiling, inspection, and thermal validation.
- Refresh numeric material or profile windows before publication and keep them tied to product datasheets.

## Limits And Non-Claims

- This card does not define a universal MCPCB reflow profile.
- It does not claim a specific IMS thermal conductivity, dielectric thickness, paste window, or thermal-resistance limit unless the product datasheet is cited directly.
- It does not replace assembly trial profiles, thermocouple profiling, or customer qualification plans.

## Open Questions

- Add additional IMS suppliers before publishing supplier-neutral IMS comparison tables.
- Add product-specific solder-paste sources if a blog draft recommends a named paste or alloy.

## Source Links

- https://www.ventec-group.com/products/tec-thermal-thermal-management-ims/
- https://www.ventec-group.com/products/tec-thermal-thermal-management-ims/vt-4b7/datasheet/
- https://www.indium.com/blog/matching-a-reflow-profile-to-a-solder-paste-spec/
- https://www.indium.com/wp-content/uploads/2025/01/Indium8.9HF-High-Reliability-Solder-Paste-PDS-99702-R7.pdf
- https://www.kester.com/Portals/0/Documents/Knowledge%20Base/Standard_Profile.pdf
- /code/hileap/frontendAPT/public/static/pcb/en/metal-core-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/metal-core-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/high-thermal-pcb.json
