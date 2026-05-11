---
source_id: "microchip-crystal-layout-short-trace-and-no-under-routing"
title: "AN826: Crystal Oscillator Basics and Crystal Selection for rfPIC and PICmicro Devices"
organization: "Microchip Technology"
owner: "Microchip Technology"
source_type: "application_note"
url: "https://ww1.microchip.com/downloads/en/AppNotes/00826a.pdf"
jurisdiction: "global"
published_at: ""
checked_at: "2026-05-11"
retrieved_at: "2026-05-11"
trust_tier: "t1"
stability: "semi_stable"
must_refresh: true
original_source_language: "en"
authority_class: "manufacturer_application_note"
exact_data_class: "method_boundary"
scope_type: "vendor_scoped_crystal_oscillator_layout_guidance"
source_origin_path: "official Microchip application note PCB layout guidance for crystal oscillators"
source_page_range: "PCB layout guidance section"
confidence: "medium"
topic_tags: ["microchip", "crystal", "oscillator", "clock", "short-trace", "keepout", "layout"]
status: "active"
notes: "Official Microchip application note. Safe for guarded wording that crystal or oscillator traces should be short, that the crystal should stay close to the related device, and that no unrelated routing should run under the crystal region. Do not use it for exact capacitance values, drive-level tuning, or universal oscillator-success claims."
---

# Source Summary

## What It Covers

- PCB layout guidance for crystal-oscillator implementation
- keep the crystal close to the associated device
- keep oscillator traces short
- avoid unrelated routing under the crystal or oscillator region

## Why It Matters

- adds a second owner-backed source that matches the handbook's `clock / crystal` subfamily without reducing the lane to only a processor-specific TI guide

## Extraction Notes

- Safe for guarded statements that the crystal or oscillator should stay close to the related IC.
- Safe for wording that crystal or oscillator traces should be kept short.
- Safe for wording that unrelated traces should not be routed under the crystal or oscillator region.
- Do not use this source for load-capacitance values, start-up guarantees, or frequency-accuracy outcomes.

## Refresh Notes

- Refresh before publication if exact revision or figure numbering matters.
