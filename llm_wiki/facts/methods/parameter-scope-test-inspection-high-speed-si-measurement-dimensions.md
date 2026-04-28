---
fact_id: "methods-parameter-scope-test-inspection-high-speed-si-measurement-dimensions"
title: "High-speed SI pages support named impedance and measurement dimensions, but those values remain page-scoped validation vocabulary"
topic: "Test and inspection high-speed SI measurement dimensions"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-27"
source_ids:
  - "frontendapt-pcb-pcb-impedance-control-page-en"
  - "frontendapt-pcb-high-speed-pcb-page-en"
  - "frontendhil-high-speed-product-page-en"
  - "frontendhil-high-frequency-product-page-en"
  - "ipc-tm650-test-methods-index"
tags: ["tdr", "vna", "impedance", "high-speed", "si", "rf", "measurement", "methods"]
---

# Canonical Summary

> The current APT and HIL high-speed / high-frequency pages support explicit measurement vocabulary for `controlled impedance`, `TDR`, `VNA`, and related channel-review dimensions. They are useful for saying what kinds of structures or measurement windows are being discussed, but they are not neutral evidence that any given board has passed a channel, protocol, or interoperability requirement.

## Stable Facts

- The internal APT impedance-control page pairs controlled-impedance targets with `100% TDR` verification language and names multiple impedance-structure families.
- The internal APT high-speed page uses `TDR / VNA` and `S-parameter` language as part of its high-speed validation posture.
- The internal HIL high-speed page uses `TDR`, `VNA`, `Eye Diagram`, and `Jitter` as separate validation labels inside a high-speed product-page context.
- The internal HIL high-frequency page uses `coupon TDR` and `VNA S-parameter` language inside an RF / mmWave validation context.
- The IPC TM-650 index can only anchor public method identity, not detailed test limits or pass/fail criteria.

## Named Parameters And Method Dimensions

- `APT controlled-impedance page`:
  `single-ended`, `differential`, and `coplanar` structures; target families `50 / 75 / 90 / 100 ohm`; tolerance language `±5 ohm / ±7%`; and `100% TDR` are named in the page.
- `APT high-speed page`:
  `TDR / VNA validation`, `S-parameters`, `10–112 Gbps`, and `±5%` impedance language are named in the page, alongside high-speed build context such as `backdrill` and `VIPPO`.
- `HIL high-speed page`:
  `85 / 90 / 100 ohm ±5%` differential-impedance language, `TDR`, `VNA`, `Eye Diagram`, `Jitter`, `DC–40 GHz` VNA wording, and `35 ps` TDR-edge wording are named in the page.
- `HIL high-frequency page`:
  `controlled impedance ±5% verified by TDR`, `VNA S-parameter` sweeps `40–67 GHz`, and RF/mmWave context such as `sub-6 GHz` and `24–86 GHz` material-selection framing are named in the page.
- `IPC anchor`:
  `IPC TM-650` can be used as a public method-family identity anchor only.

## Scope And Non-Generalization

- Use these dimensions when a draft needs to say what kind of impedance structure, measurement type, or frequency window a page is talking about.
- Treat every numeric tolerance, frequency range, edge-rate value, and data-rate value here as page-scoped and refresh-sensitive.
- Do not convert internal page values into universal acceptance thresholds, lot-release criteria, or protocol-compliance proof.
- Do not infer insertion-loss limits, return-loss limits, BER pass/fail, eye-diagram pass/fail, or interoperability status unless a stronger current source explicitly supports that claim.
- Keep `TDR / VNA` measurement vocabulary separate from `boundary-scan / JTAG`, `FAI`, and generic optical-inspection claims.
- Do not infer IPC TM-650 procedures or limits from the public index alone.

## Blog Usage

- `high-speed SI`:
  Safe support for wording such as `the review package may specify impedance structure type, target ohm family, TDR correlation, and optional VNA frequency scope`. Not safe support for compliance-pass, BER-pass, eye-mask-pass, or reach claims.
- `boundary-scan / JTAG`:
  Safe companion support for saying that JTAG access and SI validation are different layers. This card, not the JTAG card, is where `TDR / VNA` vocabulary belongs.
- `FAI`:
  Safe companion support for saying first-build release does not replace impedance or channel validation.
- `type-c charger`:
  Use only if the charger article genuinely discusses high-speed interfaces on the board; otherwise keep this card out to avoid unnecessary SI inflation.

## Source Links

- /code/hileap/frontendAPT/public/static/pcb/en/pcb-impedance-control.json
- /code/hileap/frontendAPT/public/static/pcb/en/high-speed-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/high-speed-pcb.json
- /code/hileap/frontendHIL/public/static/products/en/high-frequency-pcb.json
- https://www.electronics.org/test-methods
