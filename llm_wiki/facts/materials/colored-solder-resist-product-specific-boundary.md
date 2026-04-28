---
fact_id: "materials-colored-solder-resist-product-specific-boundary"
title: "Colored PCB claims must be tied to named solder-resist products, not generalized from board color"
topic: "Colored solder resist product-specific boundary"
category: "materials"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-28"
source_ids:
  - "peters-elpepcb-solder-resists"
  - "peters-elpepcb-overview"
  - "peters-led-optical-requirements-paper"
tags: ["solder-mask", "solder-resist", "colored-pcb", "white-pcb", "black-pcb", "led-pcb", "peters"]
---

# Canonical Summary

> Colored PCB articles should treat color as a solder-resist or coating product attribute. Color alone is not a substrate property, an LED-efficiency guarantee, an inspection-yield guarantee, or an application qualification.

## Stable Facts

- Peters' ELPEPCB portfolio provides official examples of colored printed-circuit coating and solder-resist products.
- Peters' `2467 series` is listed with color options including colourless transparent, black, white, dark green, blue, yellow, and red in the official product-family text captured for this pass.
- Peters' `2491 TSW series` is a white solder-resist family with yellowing-resistance framing tied to lead-free reflow and high thermal load in the product-family text captured for this pass.
- Peters' `SD 2446 / SD 2496 TSW` product-family text ties black/white color availability and reflectivity / yellowing-resistance statements to those exact product lines.
- Any optical, reflectivity, yellowing, thermal-load, thick-copper, or flexible-circuit statement must remain product-specific and source-specific.

## Conditions And Methods

- Use this fact when writing black, blue, green, red, white, yellow, transparent, or purple PCB articles.
- Write `colored solder resist` or `colored solder mask` unless a source explicitly says the laminate/substrate itself is colored.
- For LED articles, preserve the exact solder-resist product family and optical-test basis; do not say `white PCB` alone improves LED performance.

## Limits And Non-Claims

- This card does not claim all black, white, red, yellow, blue, green, purple, or transparent solder masks have the same process behavior.
- It does not prove color consistency, reflectivity, emissivity, inspection yield, solderability, assembly yield, thermal performance, medical suitability, automotive suitability, or UV/weathering life for a finished PCB.
- It does not prove HILPCB / APTPCB / Highleap offers every color, stocks every coating, or can meet any color tolerance or lead time.

## Open Questions

- Add Taiyo, Tamura, Electra, or other official solder-mask vendors to avoid a single-vendor color boundary.
- Refresh the Peters LED optical PDF before extracting reflectivity or yellowing numeric values.

## Source Links

- https://peters.de/elpepcb-cats-2/elpepcb-solder-resists/
- https://peters.de/elpepcb/
- https://peters.de/wp-content/uploads/2024/05/ref-166e_000_SL_LPISM_VU_for_LEDs.pdf
