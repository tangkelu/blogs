---
source_id: "murata-mlcc-simsurfing-capacitance-frequency-measurement-context-faq"
title: "The capacitance-frequency characteristics displayed by SimSurfing differ from the nominal capacitance. What is the reason for this?"
organization: "Murata"
owner: "Murata"
source_type: "manufacturer_technical_faq"
url: "https://www.murata.com/en-us/support/faqs/capacitor/ceramiccapacitor/char/0041"
jurisdiction: "global"
published_at: ""
checked_at: "2026-05-07"
retrieved_at: "2026-05-07"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
original_source_language: "en"
authority_class: "manufacturer_technical_faq"
exact_data_class: "method_scoped_exact_data"
scope_type: "vendor_scoped_named_part_low_signal_frequency_characteristic_measurement_example"
source_origin_path: "official Murata HTML FAQ"
source_page_range: "HTML FAQ body and figures 1 to 3"
confidence: "medium"
topic_tags: ["murata", "mlcc", "simsurfing", "capacitance-frequency", "ac-voltage", "low-signal-measurement", "capacitance", "method-example"]
status: "active"
notes: "Official Murata FAQ. Safe for the narrow distinction between nominal capacitance and low-signal capacitance-frequency measurement context in SimSurfing for one named part example. Do not rewrite this into universal antiresonance, SRF, or capacitor-selection rules."
---

# Source Summary

## What It Covers

- Murata explains why SimSurfing `capacitance-frequency` characteristics can differ from nominal capacitance
- Murata ties the difference to lower measurement voltage in released frequency-characteristics data
- Murata gives one named-part example:
  - `GRM155B30J225KE95`
- Murata prints example capacitance values from:
  - nominal capacitance
  - capacitance-frequency plot
  - AC-voltage characteristic at `10 mVrms`

## Why It Matters

- Gives `/code/blogs/tmps/PCB资料` a real owner-backed measurement-context artifact for `capacitance-frequency` interpretation instead of leaving all capacitor-curve discussion at generic vocabulary level
- Preserves named-part and test-voltage-scoped behavior that later blog-writing agents can cite without inventing universal rules

## Extraction Notes

- Safe for Murata's named-part example:
  - `GRM155B30J225KE95`
- Safe for Murata's printed example values:
  - nominal capacitance `2.2 uF`
  - capacitance-frequency plot example `1.68 uF`
  - AC voltage characteristic at `10 mVrms`: `1.66 uF`
- Safe for Murata's measurement-context explanation:
  - released frequency-characteristics data is measured at low signal voltages
  - high dielectric constant MLCCs can show reduced capacitance under those low-signal conditions compared with nominal-capacitance measurement conditions
- Do not generalize this FAQ into universal antiresonance-peak data, SRF values, or package-level impedance rules

## Refresh Notes

- Refresh before using current-product or lineup implications because the page is dynamic
- Preserve Murata's named-part and low-signal measurement-context scope when reusing any exact values or curve descriptions
