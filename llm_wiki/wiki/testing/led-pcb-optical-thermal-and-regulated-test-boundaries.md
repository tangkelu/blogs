---
topic_id: "testing-led-pcb-optical-thermal-and-regulated-test-boundaries"
title: "LED PCB Optical, Thermal, And Regulated Test Boundaries"
category: "testing"
status: "draft"
last_reviewed_at: "2026-04-28"
fact_ids:
  - "standards-led-optical-lifetime-and-safety-boundary"
  - "standards-medical-and-automotive-led-pcb-boundary"
  - "methods-thermal-pcb-platform-selection-posture"
  - "methods-pcb-environmental-and-solderability-test-method-boundary"
source_ids:
  - "ies-lm79-24-store-page"
  - "ies-lm80-21-store-page"
  - "ies-tm21-21-store-page"
  - "iec-62471-photobiological-safety-page"
  - "iso-13485-2016-page"
  - "iso-14971-2019-page"
  - "iec-60601-1-medical-electrical-equipment-page"
  - "iatf-16949-overview-page"
  - "ipc-tm650-2672c-thermal-shock-cycle-continuity"
tags: ["led", "mcpcb", "ims", "thermal", "photometry", "lm-79", "lm-80", "tm-21", "medical", "automotive", "safety"]
---

# Definition

> LED PCB test writing must split four layers: finished SSL product photometry, LED-source lumen-maintenance projection, photobiological safety, and board / assembly reliability. MCPCB or IMS thermal design can support an LED application, but it does not automatically prove optical lifetime, regulated-market compliance, or finished-device safety.

## Why This Topic Matters

- The `/code/blogs/tmps/2025.8.22/en` LED drafts mix photometric testing, LED lifetime, MCPCB thermal design, medical-device language, automotive language, and reliability testing.
- Without this boundary, a blog can accidentally turn `LM-79`, `LM-80`, `TM-21`, `IEC 62471`, `ISO 13485`, `ISO 14971`, `IEC 60601-1`, or `IATF 16949` into a false board-level certification claim.
- This page gives blog-writing agents a single route for LED PCB facts while preserving unsupported draft numbers as blocked claims.

## Stable Facts

- `ANSI/IES LM-79-24` is the product-level solid-state-lighting optical and electrical measurement anchor.
- `ANSI/IES LM-80-21` is the LED-source maintenance-data anchor.
- `ANSI/IES TM-21-21` is the luminous, photon, and radiant flux maintenance projection anchor, not a lifetime guarantee by itself.
- `IEC 62471:2006` anchors photobiological safety of lamps and lamp systems, including LEDs and excluding lasers.
- `ISO 13485` is medical-device QMS context; `ISO 14971` is medical-device risk-management context; consolidated `IEC 60601-1:2005+AMD1:2012+AMD2:2020 CSV` is medical electrical equipment safety / essential-performance context.
- `IATF 16949` is automotive QMS context, not an LED PCB or MCPCB product qualification.
- IPC TM-650 board methods can anchor board-level environmental vocabulary, but test severity and acceptance criteria require a project requirement, application standard, or dated procedure.

## Engineering Boundaries

- Do not use `LM-79` as proof of LED package lumen maintenance or field lifetime.
- Do not use `LM-80` without the underlying source data and conditions, and do not use `TM-21` without projection conditions and limits.
- Do not use `IEC 62471` to support CRI, luminous flux, thermal resistance, medical efficacy, or FDA readiness.
- Do not use medical or automotive standards names as proof that a bare PCB, MCPCB, LED module, or supplier is qualified.
- Keep thermal-substrate selection separate from final LED junction temperature, optical stability, and lifetime claims unless the package, stackup, drive, fixture, and measurement conditions are sourced.

## Common Misreadings

- `50,000 h` or `L70` cannot be copied from a blog or marketing page into `llm_wiki` without the underlying source and projection basis.
- A medical LED board article can mention `ISO 13485`, `ISO 14971`, and `IEC 60601-1` only as domain anchors unless product-specific regulatory evidence exists.
- An automotive LED board article can mention `IATF 16949` as QMS context, not as proof that a board is automotive-grade.
- MCPCB thermal conductivity values from a material datasheet are material properties, not finished luminaire thermal performance.

## Must Refresh Before Publishing

- Current IES / IEC / ISO / IATF edition labels
- Any LED lifetime, `L70`, lumen-maintenance, color-shift, junction-temperature, thermal-resistance, or photobiological risk-group claim
- Any medical-device, automotive-grade, FDA, CE, AEC, PPAP, or supplier-certification statement
- Any exact reliability-test severity, soldering window, voiding target, or MCPCB material numeric value not tied to an exact source card

## Related Fact Cards

- `standards-led-optical-lifetime-and-safety-boundary`
- `standards-medical-and-automotive-led-pcb-boundary`
- `methods-thermal-pcb-platform-selection-posture`
- `methods-pcb-environmental-and-solderability-test-method-boundary`

## Primary Sources

- https://store.ies.org/product/optical-and-electrical-measurements-of-solid-state-lighting-products/
- https://store.ies.org/product/lm-80-21-measuring-maintenance-of-light-output-characteristics-of-solid-state-light-sources/
- https://store.ies.org/product/tm-21-21-projecting-long-term-luminous-photon-and-radiant-flux-maintenance-of-led-light-sources/
- https://webstore.iec.ch/en/publication/7076
- https://www.iso.org/standard/59752.html
- https://www.iso.org/standard/72704.html
- https://webstore.iec.ch/en/publication/2612
- https://www.iatfglobaloversight.org/iatf-16949/
- https://www.ipc.org/sites/default/files/test_methods_docs/2.6.7.2c.pdf
