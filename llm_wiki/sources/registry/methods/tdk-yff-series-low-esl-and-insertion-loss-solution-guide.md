---
source_id: "tdk-yff-series-low-esl-and-insertion-loss-solution-guide"
title: "How to use the \"YFF Series\" 3-Terminal Feed-through filter for noise suppression and reducing the number of MLCCs"
organization: "TDK"
owner: "TDK"
source_type: "manufacturer_solution_guide"
url: "https://product.tdk.com/en/techlibrary/solutionguide/yff-series.html"
jurisdiction: "global"
published_at: ""
checked_at: "2026-05-07"
retrieved_at: "2026-05-07"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
original_source_language: "en"
authority_class: "manufacturer_solution_guide"
exact_data_class: "method_scoped_exact_data"
scope_type: "vendor_scoped_structure_and_named_part_example"
source_origin_path: "official TDK HTML solution guide"
source_page_range: "HTML figure references 2, 11, and 13"
confidence: "medium"
topic_tags: ["tdk", "yff", "3-terminal-feed-through-filter", "low-esl", "insertion-loss", "decoupling", "noise-suppression", "method-example"]
status: "active"
notes: "Official TDK solution guide. Safe for structure-scoped ESL comparison and named-part example results only. Do not convert these examples into universal capacitor package rules, generic decoupling recipes, or cross-vendor superiority claims."
---

# Source Summary

## What It Covers

- TDK compares representative ESL ranges for three structures:
  - standard `2-terminal MLCC`
  - `reverse geometry capacitor`
  - `3-terminal feed-through filter`
- TDK gives named-part example results for `YFF18AC1A104M` and `YFF18AC0G106M` in DC/DC-converter noise-suppression examples
- TDK publishes insertion-loss and voltage-waveform comparison values under stated converter conditions

## Why It Matters

- Gives the local corpus an official narrow path to absorb exact `low-ESL` and `insertion-loss` example data without pretending the handbook's generic package/ESL table is authority
- Converts one `A1` candidate class from `/code/blogs/tmps/PCB资料` into a source-backed exact-data artifact

## Extraction Notes

- Safe for the representative structure-scoped ESL comparison printed by TDK:
  - standard `2-terminal MLCC`: about `200-300 pH`
  - reverse geometry capacitor: about `80-100 pH`
  - `3-terminal feed-through filter`: about `20-30 pH`
- Safe for named-part example values tied to TDK's own `YFF18...` configurations and stated converter conditions
- Do not rewrite the structure comparison into a universal package-to-ESL table
- Do not generalize the example attenuation or waveform results to all capacitors, all `3-terminal` filters, or all converters

## Refresh Notes

- Refresh before using current-product or lineup implications because the page is dynamic
- Preserve TDK's named-part and converter-condition scope when reusing any exact values
