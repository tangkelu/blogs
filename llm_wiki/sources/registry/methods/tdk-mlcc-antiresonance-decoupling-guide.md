---
source_id: "tdk-mlcc-antiresonance-decoupling-guide"
title: "Solution Guide: Replacing Electrolytic Capacitor with MLCC, Revised Guide"
organization: "TDK"
source_type: "manufacturer_solution_guide"
url: "https://product.tdk.com/en/techlibrary/solutionguide/mlcc_replace-guide.html"
jurisdiction: "global"
published_at: ""
checked_at: "2026-05-06"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
topic_tags: ["tdk", "mlcc", "decoupling", "self-resonant-frequency", "antiresonance", "esr"]
status: "active"
notes: "Official TDK solution guide. Use for antiresonance and SRF vocabulary in MLCC decoupling context only; do not convert it into universal capacitor-selection rules."
---

# Source Summary

## What It Covers

- TDK warns that low-ESR MLCC use can trigger abnormal oscillation or antiresonance
- TDK states that decoupling often uses multiple capacitors in parallel
- TDK explains that the bottom of the impedance `V` curve is the self-resonant frequency `SRF`
- TDK states that MLCCs with different SRFs in parallel can form an antiresonant LC condition and create impedance peaks

## Why It Matters

- Gives the local corpus a current manufacturer anchor for `SRF` and `antiresonance` vocabulary in decoupling work
- Supports blocking simplistic `parallel more capacitors is always better` rules

## Extraction Notes

- Safe for narrow statements about SRF, antiresonance, and impedance-peak risk when parallel MLCCs are combined
- Safe to say that antiresonance can reduce noise rejection at the affected frequency
- Do not use this guide for exact capacitor values, dielectric-family prescriptions, regulator-stability recipes, or broad replacement guarantees

## Refresh Notes

- Refresh before using it for product-family or design-example discussions
