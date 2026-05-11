---
source_id: "murata-low-esl-capacitors-loop-impedance-article"
title: "How can the mounting area be reduced? - Methods of using low-ESL capacitors -"
organization: "Murata"
owner: "Murata"
source_type: "manufacturer_technical_article"
url: "https://article.murata.com/en-us/article/methods-of-using-low-esl-capacitors"
jurisdiction: "global"
published_at: "2013-05-28"
checked_at: "2026-05-07"
retrieved_at: "2026-05-07"
trust_tier: "t1"
stability: "dynamic"
must_refresh: true
original_source_language: "en"
authority_class: "manufacturer_technical_article"
exact_data_class: "method_scoped_exact_data"
scope_type: "vendor_scoped_low_esl_structure_method_example"
source_origin_path: "official Murata technical article"
source_page_range: "HTML sections 3 to 5 and figures 5 to 9"
confidence: "medium"
topic_tags: ["murata", "low-esl", "loop-impedance", "3-terminal-capacitor", "reverse-capacitor", "bypass", "decoupling", "method-example"]
status: "active"
notes: "Official Murata technical article. Safe for low-ESL structure comparison, loop-impedance framing, and component-count / area-reduction examples under Murata's stated assumptions. Do not rewrite this as a universal antiresonance artifact or universal capacitor-reduction rule."
---

# Source Summary

## What It Covers

- Murata explains `loop impedance` in IC/LSI power-supply bypass use
- Murata compares normal MLCC, `LW reverse capacitor`, and `3-terminal capacitor` structures
- Murata gives recoverable relative `ESL` and high-frequency impedance comparison values
- Murata gives a component-count and mounting-area reduction example under a same-loop-impedance assumption

## Why It Matters

- Gives `/code/blogs/tmps/PCB资料` a real owner-backed fallback artifact when the stricter antiresonance-exact-data lane remains blocked
- Preserves a reusable low-ESL / loop-impedance method example that later blog-writing agents can compose without inventing universal cookbook rules

## Extraction Notes

- Safe for Murata's printed comparison that, at the same `1 uF` capacitance:
  - `LW reverse capacitor` has about `1/3` the `ESL` of a normal MLCC
  - `3-terminal capacitor` has about `1/10` the `ESL` of a normal MLCC
- Safe for Murata's figure-6 structure example:
  - `LW reverse capacitor`: `1.0 × 0.6 mm`, `4.3 uF`
  - `3-terminal capacitor`: `1.0 × 0.5 mm`, `4.3 uF`
  - comparator MLCC: `0.6 × 0.3 mm`, `1 uF`
  - high-frequency impedance equivalence:
    - `LW reverse capacitor` equals about `two` such MLCCs
    - `3-terminal capacitor` equals `four or more` such MLCCs
- Safe for Murata's system-level example:
  - original design: `100` MLCCs
  - reduced design: `32`
  - reduction: `68`
  - mounting-area reduction: about `35 mm^2`
- Safe for Murata's setup framing:
  - `IC/LSI power supply`
  - simple structure of `via-hole, wiring, and a capacitor`
  - same `loop impedance` / same `voltage fluctuation level` assumption
- Do not rewrite this article into universal antiresonance, universal package ranking, or universal board-area reduction rules

## Refresh Notes

- Refresh before using current-product or lineup implications because the page is dynamic
- Preserve Murata's structure-comparison and same-loop-impedance assumption when reusing any exact values
