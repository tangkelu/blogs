---
source_id: "coilcraft-lpd3015-common-mode-chokes-datasheet"
title: "LPD3015 Series Low-Profile Common Mode Chokes"
organization: "Coilcraft"
source_type: "manufacturer_datasheet"
url: "https://www.coilcraft.com/getmedia/1003995d-683a-4e70-9051-f551c755e012/lpd3015_cm.pdf"
jurisdiction: "global"
published_at: ""
checked_at: "2026-05-07"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
topic_tags: ["coilcraft", "common-mode-choke", "lpd3015", "common-mode", "differential-mode", "impedance-curve", "attenuation-curve"]
status: "active"
notes: "Official Coilcraft datasheet for a named common-mode choke family. Safe for family-scoped curve identity, family member identity, and directly published electrical context only."
---

# Source Summary

## What It Covers

- `Coilcraft LPD3015 Series` low-profile common-mode choke family identity
- family member tables with `inductance`, `DCR max`, `Irms`, `interwinding isolation`, and common-mode peak-impedance fields
- `Typical Impedance vs Frequency` curves with both `common mode` and `differential mode` traces
- `Typical Attenuation (Ref: 50 Ohms)` curves with both `common mode` and `differential mode` traces
- measurement and condition notes including `25°C`, `100 kHz`, `0.1 Vrms`, `0 Adc`, and the datasheet's differential-mode cutoff definition

## Why It Matters

- gives the local corpus a named owner-backed common-mode choke family that shows both `common-mode` and `differential-mode` behavior on the same primary source path
- supports exact family-scoped curve recovery without relying on the secondary handbook figure

## Extraction Notes

- safe for named family identity and owner-backed evidence that one published family includes both `common-mode` and `differential-mode` traces
- safe for directly published table fields and condition notes when they stay family-scoped or part-scoped
- do not generalize this datasheet into universal attenuation, interface-suitability, placement, compliance, or signal-integrity claims
- do not infer exact curve values for family members that are not explicitly plotted

## Refresh Notes

- refresh before using current family lineup, ordering codes, or exact electrical rows in new prompt outputs
