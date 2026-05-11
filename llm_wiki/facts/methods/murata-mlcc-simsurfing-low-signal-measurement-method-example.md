---
fact_id: "methods-murata-mlcc-simsurfing-low-signal-measurement-method-example"
title: "Murata SimSurfing capacitance-frequency data is reusable only with named-part and low-signal measurement scope preserved"
topic: "Murata MLCC SimSurfing low-signal measurement method example"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-07"
exact_data_class: "method_scoped_exact_data"
scope_type: "vendor_scoped_named_part_low_signal_frequency_characteristic_measurement_example"
canonical_unit_policy: "Preserve original Murata units and labels such as uF and mVrms. Do not normalize these example values into universal MLCC impedance, antiresonance, or dielectric ranking rules."
source_ids:
  - "murata-mlcc-simsurfing-capacitance-frequency-measurement-context-faq"
tags: ["murata", "mlcc", "simsurfing", "capacitance-frequency", "low-signal-measurement", "ac-voltage", "method-example", "exact-data"]
---

# Canonical Summary

> Murata's official MLCC FAQ is strong enough to support one narrow exact-data layer for the `A1 capacitor` lane: the local corpus may reuse Murata's named-part SimSurfing measurement-context example for `GRM155B30J225KE95`, including the relationship between nominal capacitance, low-signal `capacitance-frequency` data, and the printed `10 mVrms` AC-voltage characteristic example. This card is a vendor-scoped method example only. It does not authorize universal MLCC antiresonance peaks, generic SRF numbers, or broad capacitor-selection rules.

## Exact Data Scope

- exact for:
  - Murata's printed named-part example in this FAQ
  - Murata's stated low-signal measurement explanation for SimSurfing `capacitance-frequency` data
  - Murata's printed capacitance values for nominal, `capacitance-frequency`, and `10 mVrms` example conditions
- not exact for:
  - universal impedance-frequency behavior for all MLCCs
  - antiresonance peak frequencies
  - generic package-level capacitance or impedance behavior
  - cross-vendor measurement rules

## Admitted Data

- Murata uses this named-part example:
  - `GRM155B30J225KE95`
- Murata states these printed example values:
  - nominal capacitance: `2.2 uF`
  - capacitance-frequency plot value: `1.68 uF`
  - AC voltage characteristic at `10 mVrms`: `1.66 uF`
- Murata states this measurement-context boundary:
  - released `capacitance-frequency` data for SimSurfing is measured at low signal voltages
  - high dielectric constant MLCCs can show lower capacitance under those low-signal measurement conditions than under nominal-capacitance measurement conditions

## Conditions And Methods

- Treat this card as one Murata measurement-method example for reading SimSurfing `capacitance-frequency` plots against nominal capacitance.
- Keep `GRM155B30J225KE95` tied to Murata's own example context.
- Use this card when a prompt needs a real vendor-backed explanation for why displayed `capacitance-frequency` curves can sit below nominal capacitance.
- Pair this card with [capacitor-parasitic-self-resonance-and-antiresonance-boundary.md](/code/blogs/llm_wiki/facts/methods/capacitor-parasitic-self-resonance-and-antiresonance-boundary.md) when a prompt needs broader conservative vocabulary about impedance, ESR, SRF, or antiresonance.

## Limits And Non-Claims

- This card does not authorize exact SRF or antiresonance frequencies.
- It does not authorize extrapolating this part example into all high-dielectric MLCCs.
- It does not authorize generic impedance-curve ranking by dielectric, package, or vendor.
- It does not authorize handbook antiresonance formulas, package tables, or value-pair recipes.
- It does not authorize compliance, stability, or product-readiness outcomes.

## Relationship To Other Cards

- Use [tdk-yff-series-low-esl-and-insertion-loss-method-example.md](/code/blogs/llm_wiki/facts/methods/tdk-yff-series-low-esl-and-insertion-loss-method-example.md) for low-ESL and insertion-loss examples.
- Use [tdk-mlcc-output-capacitor-structure-method-example.md](/code/blogs/llm_wiki/facts/methods/tdk-mlcc-output-capacitor-structure-method-example.md) for output-capacitor transient-response and phase-compensation examples.
- Use this card specifically for named-part SimSurfing `capacitance-frequency` measurement-context discussion.

## Provenance

- origin batch:
  - `/code/blogs/tmps/PCB资料`
- motivating secondary-PDF candidates:
  - `Figure 3-12` antiresonance and impedance-curve interpretation pressure from `P4-215A1`
  - general capacitor frequency-characteristic interpretation pressure from the `85页 EMC` handbook
- authority replacement used here:
  - official Murata `SimSurfing capacitance-frequency differs from nominal capacitance` FAQ
- exact-data shape:
  - vendor-scoped named-part low-signal measurement example

## Source Links

- https://www.murata.com/en-us/support/faqs/capacitor/ceramiccapacitor/char/0041
