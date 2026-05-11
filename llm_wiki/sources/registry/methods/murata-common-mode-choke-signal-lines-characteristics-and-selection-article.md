---
source_id: "murata-common-mode-choke-signal-lines-characteristics-and-selection-article"
title: "Characteristics of common mode choke coils for signal lines and how to choose one"
organization: "Murata Manufacturing"
source_type: "manufacturer_article"
url: "https://article.murata.com/en-global/article/characteristics-cmcc-for-signal-lines-and-how-to-choose"
jurisdiction: "global"
published_at: "2016-12-13"
checked_at: "2026-05-07"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
topic_tags: ["murata", "common-mode-choke", "signal-lines", "common-mode", "differential-mode", "sdd21", "scc21", "insertion-loss"]
status: "active"
notes: "Official Murata technical article. Use for vendor-scoped mode-behavior and insertion-loss vocabulary only; do not convert its examples, reference guideline, or interface examples into universal EMC rules."
---

# Source Summary

## What It Covers

- Murata explains common-mode and differential-mode signals in paired differential transmission lines
- Murata states that a common-mode choke inserted across a differential pair attenuates common-mode noise while the wanted differential signal passes through with some attenuation dependence on frequency
- Murata names `differential mode insertion loss Sdd21` and `common mode insertion loss Scc21` as the relevant frequency-characteristic views
- Murata gives a signal-line selection example and says the `cutoff frequency at least 3 times the signal frequency` rule is only a reference guideline

## Why It Matters

- Gives the local corpus a stronger vendor-backed correction to overly absolute handbook wording such as `differential current passes without attenuation`
- Supports a safer common-mode choke boundary that stays tied to insertion-loss framing and interface-specific validation

## Extraction Notes

- Safe for vendor-scoped wording that common-mode choke behavior should be discussed through `Sdd21` and `Scc21`, not as a no-loss universal rule
- Safe for the boundary that differential-mode attenuation also exists and increases with frequency
- Safe for the boundary that any `3x signal frequency` cutoff rule is only a Murata reference guideline and final suitability depends on the interface's own signal-quality criteria
- Do not use this article for universal selection recipes, compliance outcomes, wireless-performance guarantees, or current-product recommendations
- Do not reuse the discontinued product example as a current part recommendation

## Refresh Notes

- Refresh before reusing current lineup implications, recommendation lists, or application examples because the article is dated and explicitly warns that some information may differ from the latest information
