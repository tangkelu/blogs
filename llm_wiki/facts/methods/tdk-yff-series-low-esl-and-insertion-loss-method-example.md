---
fact_id: "methods-tdk-yff-series-low-esl-and-insertion-loss-method-example"
title: "TDK YFF series low-ESL and insertion-loss example data is reusable only as a vendor-scoped method example"
topic: "TDK YFF series low-ESL and insertion-loss method example"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-07"
exact_data_class: "method_scoped_exact_data"
scope_type: "vendor_scoped_structure_and_named_part_example"
canonical_unit_policy: "Preserve original TDK units and labels such as pH, dB, dBuVmax, mVpp, V, A, MHz, 0402/0603, and mm/inch package notation. Do not normalize these example values into generic package rules."
source_ids:
  - "tdk-yff-series-low-esl-and-insertion-loss-solution-guide"
tags: ["tdk", "yff", "3-terminal-feed-through-filter", "low-esl", "insertion-loss", "method-example", "exact-data", "decoupling"]
---

# Canonical Summary

> TDK's official `YFF Series` solution guide is strong enough to support one narrow exact-data layer for the `A1 capacitor` lane: the local corpus may reuse TDK's printed structure-scoped ESL comparison and two named-part DC/DC-converter example result sets for `YFF18AC1A104M` and `YFF18AC0G106M`. This card is a vendor-scoped method example only. It does not authorize universal capacitor-package ESL rankings, generic insertion-loss comparisons across capacitor technologies, or broad decoupling recipes.

## Exact Data Scope

- exact for:
  - TDK's printed structure comparison in the `YFF Series` solution guide
  - TDK's own named-part example configurations
  - TDK's own stated DC/DC-converter conditions and measured/simulated result labels
- not exact for:
  - generic `2-terminal` versus `3-terminal` capacitor families across vendors
  - unnamed MLCC packages
  - handbook package/ESL tables
  - universal decoupling placement, value, or quantity rules

## Admitted Data

- TDK prints the following representative ESL comparison by structure:
  - standard `2-terminal MLCC`: about `200-300 pH`
  - reverse geometry capacitor: about `80-100 pH`
  - `3-terminal feed-through filter`: about `20-30 pH`
- In one input-side DC/DC-converter example, TDK compares:
  - `2-terminal MLCC`:
    - `1005 mm / 0402 inch`
    - `100 nF`
    - `50 V`
    - `x1 pc`
  - `3-terminal feed-through filter`:
    - `YFF18AC1A104M`
    - `1608 mm / 0603 inch`
    - `100 nF`
    - `10 V`
    - `x1 pc`
- TDK states the input-side converter conditions for that example as:
  - input voltage `5 V`
  - output voltage `0.8 V`
  - switching frequency `2 MHz`
  - output current `4 A`
- For that input-side example, TDK prints:
  - voltage waveform comparison:
    - `2-terminal 0.1 uF x1 pc`: `1.64 Vpp`
    - `3-terminal 0.1 uF x1 pc`: `0.92 Vpp`
  - conducted noise comparison:
    - `2-terminal 0.1 uF x1 pc`: `65 dBuVmax`
    - `3-terminal 0.1 uF x1 pc`: `60 dBuVmax`
- In one output-side DC/DC-converter example, TDK compares:
  - `2-terminal MLCC 1 uF x5 pcs`
  - `3-terminal YFF18AC0G106M 10 uF x1 pc`
  - `3-terminal YFF18AC0G106M 10 uF x3 pcs`
- TDK states the output-side converter conditions for that example as:
  - input voltage `5 V`
  - output voltage `1.8 V`
  - switching frequency `2 MHz`
  - output current `2 A`
- For that output-side example, TDK prints:
  - insertion loss comparison:
    - `2-terminal 1 uF x5 pcs`: `-48.4 dB`
    - `3-terminal 10 uF x1 pc`: `-50.5 dB`
    - `3-terminal 10 uF x3 pcs`: `-65.9 dB`
  - voltage waveform comparison:
    - `2-terminal 1 uF x5 pcs`: `19 mVpp`
    - `3-terminal 10 uF x1 pc`: `15 mVpp`
    - `3-terminal 10 uF x3 pcs`: `5 mVpp`

## Conditions And Methods

- Treat the ESL comparison as a TDK structure-scoped printed comparison, not as a universal package ranking.
- Treat the converter comparisons as named-part and named-configuration examples only.
- Keep `YFF18AC1A104M` and `YFF18AC0G106M` tied to TDK's own examples and stated conditions.
- Treat these values as method/example evidence for `low-ESL` and `insertion-loss` discussion, not as proof that a specific filter should always replace a given MLCC count.

## Limits And Non-Claims

- This card does not authorize the handbook-style generic `package -> ESL` table as a reusable fact.
- It does not authorize cross-vendor claims that all `3-terminal` filters outperform all `2-terminal` MLCCs.
- It does not authorize universal insertion-loss rankings across capacitor technologies or capacitance values.
- It does not authorize universal component-count reduction rules.
- It does not authorize EMC-compliance, converter-stability, or finished-product reliability outcomes.
- It does not authorize extrapolating these example values to other frequencies, voltages, currents, or layouts not printed by TDK.

## Relationship To Other Cards

- Use [capacitor-parasitic-self-resonance-and-antiresonance-boundary.md](/code/blogs/llm_wiki/facts/methods/capacitor-parasitic-self-resonance-and-antiresonance-boundary.md) for conservative non-ideal capacitor vocabulary, SRF, and antiresonance boundary wording.
- Use this card only when a prompt specifically benefits from TDK's vendor-scoped `low-ESL` or `insertion-loss` example data.
- Keep the handbook-derived `A1` generic package/ESL table and generic insertion-loss comparison blocked unless matched by stronger family-scoped or part-scoped official sources.

## Provenance

- origin batch:
  - `/code/blogs/tmps/PCB资料`
- motivating secondary-PDF candidates:
  - `Table 3-1` package / ESL table from `P4-215A1`
  - `Figure 3-13` insertion-loss comparison from `P4-215A1`
- authority replacement used here:
  - official TDK `YFF Series` solution guide
- exact-data shape:
  - vendor-scoped structure comparison plus named-part method examples

## Source Links

- https://product.tdk.com/en/techlibrary/solutionguide/yff-series.html
