---
fact_id: "methods-capacitor-parasitic-self-resonance-and-antiresonance-boundary"
title: "Official vendor guidance supports capacitor role vocabulary plus SRF and antiresonance boundaries, but not universal decoupling recipes"
topic: "Capacitor parasitic, self-resonance, and antiresonance boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-05-06"
source_ids:
  - "analog-devices-decoupling-capacitors-on-power-pins"
  - "murata-capacitor-impedance-frequency-faq"
  - "tdk-mlcc-antiresonance-decoupling-guide"
tags: ["capacitor", "decoupling", "bypass", "bulk", "esr", "self-resonance", "antiresonance", "pdn", "methods"]
---

# Canonical Summary

> Current official vendor guidance is strong enough to support a narrow capacitor boundary: `decoupling / bypass / bulk` role language is legitimate, capacitor impedance and ESR vary with frequency, the self-resonant frequency marks the minimum-impedance region, and parallel MLCC combinations can create antiresonance peaks. The same source mix does not authorize universal capacitor values, count rules, dielectric recipes, or placement formulas.

## Stable Facts

- Analog Devices uses `decoupling / bypass capacitors` and `bulk capacitors` as separate role-level vocabulary in processor power-pin context.
- Analog Devices states that decoupling capacitors suppress high-frequency noise on power-supply signals.
- Murata states that capacitor impedance magnitude and ESR vary with frequency.
- TDK states that the minimum point of the impedance-frequency curve is the self-resonant frequency `SRF`.
- TDK states that parallel MLCCs with different SRFs can form an antiresonant condition that creates impedance peaks and can reduce noise rejection at that frequency.

## Conditions And Methods

- Use this card when a draft needs safe language about capacitor non-ideal behavior, decoupling vocabulary, or why multi-capacitor planning cannot be reduced to ideal-capacitor assumptions.
- Keep the language at `role boundary` and `frequency-dependent behavior` level.
- Pair this card with a specific semiconductor datasheet or power-design application note before selecting exact values, counts, packages, or placement priorities for a named device.

## Limits And Non-Claims

- This card does not authorize exact capacitor values, value ratios, or `small/medium/large capacitor` recipes.
- It does not authorize universal dielectric recommendations such as `X7R` versus `Y5V` versus `Z5U`.
- It does not authorize exact ESR, ESL, SRF, or antiresonance frequencies for unnamed parts.
- It does not prove regulator stability, EMC compliance, or production readiness by itself.

## Open Questions

- A later lane can add narrower semiconductor-vendor power-distribution records if future prompts need device-family-specific decoupling placement guidance.
- A later lane can add part-level capacitor datasheet records if exact package or impedance-curve examples are needed.

## Source Links

- https://ez.analog.com/dsp/sharc-processors/adsp-sc59x/w/documents/33676/what-is-the-use-of-decoupling-capacitors-on-power-pins
- https://www.murata.com/en-us/support/faqs/capacitor/ceramiccapacitor/char/0036
- https://product.tdk.com/en/techlibrary/solutionguide/mlcc_replace-guide.html
