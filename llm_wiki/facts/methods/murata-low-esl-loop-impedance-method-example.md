---
fact_id: "methods-murata-low-esl-loop-impedance-method-example"
title: "Murata low-ESL capacitor comparisons are reusable only as a loop-impedance method example"
topic: "Murata low-ESL loop-impedance method example"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-07"
exact_data_class: "method_scoped_exact_data"
scope_type: "vendor_scoped_low_esl_structure_method_example"
canonical_unit_policy: "Preserve original Murata units and labels such as uF, mm, and mm^2, and preserve relative statements like 1/3, 1/10, two, and four or more. Do not normalize these values into universal ESL, antiresonance, or capacitor-count rules."
source_ids:
  - "murata-low-esl-capacitors-loop-impedance-article"
tags: ["murata", "low-esl", "loop-impedance", "3-terminal-capacitor", "reverse-capacitor", "bypass", "decoupling", "method-example", "exact-data"]
---

# Canonical Summary

> Murata's official low-ESL capacitor article is strong enough to support one narrow exact-data layer for the `A1 capacitor` lane: the local corpus may reuse Murata's structure-scoped low-ESL and loop-impedance method examples for normal MLCC, `LW reverse capacitor`, and `3-terminal capacitor` under Murata's stated IC/LSI bypass assumptions. This card is a vendor-scoped method example only. It does not authorize universal antiresonance peaks, universal package rankings, or generic capacitor-count reduction rules.

## Exact Data Scope

- exact for:
  - Murata's printed structure comparisons in this article
  - Murata's stated IC/LSI bypass and same-loop-impedance framing
  - Murata's printed size, capacitance, and component-count example values
- not exact for:
  - universal antiresonance behavior
  - exact part-number performance across Murata's whole lineup
  - universal loop-impedance outcomes on unrelated layouts
  - generic board-area reduction promises

## Admitted Data

- Murata states that when each structure has the same capacitance of `1 uF`:
  - `LW reverse capacitor` has about `1/3` the `ESL` of a normal MLCC
  - `3-terminal capacitor` has about `1/10` the `ESL` of a normal MLCC
- Murata states these figure-6 example structures:
  - `LW reverse capacitor`: `1.0 × 0.6 mm`, `4.3 uF`
  - `3-terminal capacitor`: `1.0 × 0.5 mm`, `4.3 uF`
  - comparator MLCC: `0.6 × 0.3 mm`, `1 uF`
- Murata states these high-frequency equivalence claims for that figure-6 example:
  - the `LW reverse capacitor` equals about `two` such MLCCs
  - the `3-terminal capacitor` equals `four or more` such MLCCs
- Murata states this same-loop-impedance component-reduction example:
  - original design: `100` MLCCs
  - reduced design: `32`
  - reduction: `68`
  - mounting-area reduction: about `35 mm^2`

## Conditions And Methods

- Treat this card as one Murata low-ESL method example for IC/LSI power-supply bypass planning.
- Keep the article's setup framing attached to the values:
  - `IC/LSI power supply`
  - `loop impedance`
  - simple structure of `via-hole, wiring, and a capacitor`
  - same `loop impedance` / same `voltage fluctuation level`
- Use this card when a prompt needs real owner-backed low-ESL structure and loop-impedance language plus exact example comparisons.
- Pair this card with [capacitor-parasitic-self-resonance-and-antiresonance-boundary.md](/code/blogs/llm_wiki/facts/methods/capacitor-parasitic-self-resonance-and-antiresonance-boundary.md) when a prompt also needs conservative non-ideal capacitor vocabulary.

## Limits And Non-Claims

- This card does not authorize handbook antiresonance frequencies or antiresonance-peak claims.
- It does not authorize universal claims that all `3-terminal` capacitors outperform all normal MLCCs in every layout.
- It does not authorize generic component-count reduction rules or board-area guarantees.
- It does not authorize extrapolating these examples into all Murata `LLL`, `LLC`, or `NFM` parts.
- It does not authorize compliance, stability, or finished-product readiness outcomes.

## Relationship To Other Cards

- Use [tdk-yff-series-low-esl-and-insertion-loss-method-example.md](/code/blogs/llm_wiki/facts/methods/tdk-yff-series-low-esl-and-insertion-loss-method-example.md) for TDK's named-part low-ESL and insertion-loss comparisons.
- Use [tdk-mlcc-output-capacitor-structure-method-example.md](/code/blogs/llm_wiki/facts/methods/tdk-mlcc-output-capacitor-structure-method-example.md) for output-capacitor transient-response and phase-compensation examples.
- Use [murata-mlcc-simsurfing-low-signal-measurement-method-example.md](/code/blogs/llm_wiki/facts/methods/murata-mlcc-simsurfing-low-signal-measurement-method-example.md) for Murata's low-signal `capacitance-frequency` measurement-context example.

## Provenance

- origin batch:
  - `/code/blogs/tmps/PCB资料`
- motivating secondary-PDF candidates:
  - `Figure 3-12` and `Figure 3-15` pressure to explain capacitor high-frequency behavior from `P4-215A1`
  - handbook capacitor-quantity / low-ESL preference pressure
- authority replacement used here:
  - official Murata low-ESL capacitor technical article
- exact-data shape:
  - vendor-scoped low-ESL structure and loop-impedance method example

## Source Links

- https://article.murata.com/en-us/article/methods-of-using-low-esl-capacitors
