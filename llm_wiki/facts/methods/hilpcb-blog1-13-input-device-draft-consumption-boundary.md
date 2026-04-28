---
fact_id: "methods-hilpcb-blog1-13-input-device-draft-consumption-boundary"
title: "HILPCB Blog1-13 input-device drafts are topic inventory, not product-performance or capability evidence"
topic: "HILPCB Blog1-13 input-device draft consumption boundary"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids:
  - "frontendapt-pcba-smt-tht-page-en"
  - "frontendapt-pcba-turnkey-assembly-page-en"
  - "frontendhil-smt-assembly-product-page-en"
  - "frontendhil-through-hole-assembly-product-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-testing-quality-page-en"
  - "frontendapt-pcba-first-article-inspection-page-en"
  - "frontendapt-pcba-npi-assembly-page-en"
  - "frontendapt-pcb-flex-pcb-page-en"
  - "frontendapt-pcb-rigid-flex-pcb-page-en"
  - "frontendhil-flex-pcb-product-page-en"
  - "frontendhil-rigid-flex-pcb-product-page-en"
  - "frontendapt-pcb-hdi-pcb-page-en"
  - "frontendhil-hdi-pcb-product-page-en"
  - "usb-if-type-c-language-guidelines-2023"
  - "frontendapt-industry-industrial-control-page-en"
  - "frontendapt-industry-medical-page-en"
  - "iso-13485-2016-page"
  - "fda-qmsr-page"
  - "as9100d-qms-requirements-page"
  - "dfars-252-246-7008-sources-of-electronic-parts-page"
tags: ["hilpcb", "input-device", "keyboard", "mouse", "midi", "audio", "draft-boundary", "rewrite-gate"]
---

# Canonical Summary

> The HILPCB Blog1-13 draft batch under `/code/blogs/tmps/HILPCB-blog1-13/en` should be consumed only as topic intent, outline shape, and blocked-claim inventory. Existing `llm_wiki` cards can support generic PCB / PCBA / flex / HDI / USB-C / industrial-control process language, but the drafts do not prove product performance, protocol compatibility, certification, durability, regulated-sector qualification, HILPCB capability, cost, lead time, or yield claims.

## Stable Facts

- The batch contains 40 temporary English drafts spanning mechanical and custom keyboard PCBs, industrial / rugged / HMI keyboards, mouse PCBs, MIDI controllers, music keyboards, synthesizers, and audio-control panels.
- Existing `llm_wiki` support is strongest for generic PCBA assembly flow, layered inspection, NPI / FAI style gates, flex / rigid-flex posture, HDI vocabulary, USB Type-C wording discipline, industrial-control context, medical-sector quality-system vocabulary, and hi-rel procurement / traceability context.
- Existing support is not enough to recover keyboard-specific, mouse-specific, MIDI/audio-specific, rugged-product, wireless-product, compliance, certification, durability, or HIL capability claims from the draft prose.
- The four P4-30 lane logs classify the batch as partially reusable for process/context language and blocked for most product-specific facts.

## Conditions And Methods

- For keyboard, mouse, MIDI, audio, rugged, medical, or military input-device writing, use `logs/p4-30-hilpcb-blog1-13-ingestion-map.md` before building an evidence pack.
- Pull generic process wording from existing source-backed cards such as PCBA assembly flow, inspection stack, NPI / FAI gates, flex / rigid-flex posture, HDI posture, USB-C protocol-context boundaries, and industrial-control review gates.
- Treat draft-originated section structures as query and outline signals only.
- Stop and add a separate source lane when an article needs protocol behavior, certification status, regulated qualification, durability, RF performance, audio performance, firmware compatibility, or HILPCB-specific capability.

## Limits And Non-Claims

- This card does not verify QMK, VIA, hot-swap durability, switch-cycle life, RGB electrical behavior, Bluetooth, 2.4 GHz wireless behavior, RF range, latency, polling rate, DPI / CPI, battery life, or charging behavior.
- It does not verify MIDI, USB-MIDI, BLE-MIDI, DAW compatibility, keybed velocity, aftertouch, pad sensitivity, fader precision, encoder precision, DAC / ADC performance, THD, SNR, dynamic range, DSP, memory, storage, or polyphony claims.
- It does not prove IP67, IP68, IP69K, IEC 60529, IEC 60601, ISO 13485 status, FDA status, MIL-STD, AS9100, ITAR, FCC, CE, RED, Bluetooth qualification, USB-IF certification, RoHS, or REACH status for any product or supplier.
- It does not prove HILPCB cost, lead time, MOQ, inventory, yield, throughput, inspection coverage, test coverage, production scale, regulated-sector readiness, or shop capability.
- It does not authorize copying numeric values, process windows, tolerance tables, cycle counts, environmental ranges, acoustic metrics, RF metrics, or performance comparisons from the drafts into reusable facts.

## Open Questions

- Whether to create dedicated source lanes for QMK / VIA, Bluetooth / FCC / CE, MIDI Association, mouse sensor vendors, hot-swap socket vendors, and audio-control component vendors before writing product-specific articles from this batch.
- Whether HILPCB has dated capability records for any input-device-specific assembly, test, quality, regulated-sector, or commercial claims that should later be registered as scoped internal sources.

## Source Links

- /code/hileap/frontendAPT/public/static/pcba/en/smt-tht.json
- /code/hileap/frontendAPT/public/static/pcba/en/turnkey-assembly.json
- /code/hileap/frontendHIL/public/static/products/en/smt-assembly.json
- /code/hileap/frontendHIL/public/static/products/en/through-hole-assembly.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendAPT/public/static/pcba/en/testing-quality.json
- /code/hileap/frontendAPT/public/static/pcba/en/first-article-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/npi-assembly.json
- /code/hileap/frontendAPT/public/static/pcb/en/flex-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/rigid-flex-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/flex-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/rigid-flex-pcb.json
- /code/hileap/frontendAPT/public/static/pcb/en/hdi-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/hdi-pcb.json
- https://www.usb.org/sites/default/files/usb_type-c_language_product_and_packaging_guidelines_20230320.pdf
- /code/hileap/frontendAPT/public/static/industries/en/industrial-control-pcb.json
- /code/hileap/frontendAPT/public/static/industries/en/medical-pcb.json
- https://www.iso.org/standard/59752.html
- https://www.fda.gov/medical-devices/quality-system-qs-regulationmedical-device-current-good-manufacturing-practices-cgmp/quality-management-system-regulation-final-rule-amending-quality-system-regulation-frequently-asked
- https://saemobilus.sae.org/standards/as9100d-quality-management-systems-requirements-aviation-space-defense-organizations
- https://www.acquisition.gov/dfars/252.246-7008-sources-electronic-parts
