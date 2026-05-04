---
fact_id: "standards-midi-usb-midi-ble-midi-compatibility-boundary"
title: "MIDI Association and Bluetooth SIG sources support MIDI / USB-MIDI / BLE-MIDI transport identity and compatibility-boundary wording, not DAW or performance proof"
topic: "MIDI, USB-MIDI, and BLE-MIDI compatibility boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-02"
source_ids:
  - "midi-specifications-page"
  - "midi-usb-midi-page"
  - "midi-ble-midi-page"
  - "bluetooth-core-specification-page"
  - "bluetooth-qualification-process-page"
tags: ["midi", "usb-midi", "ble-midi", "bluetooth", "transport", "compatibility", "boundary", "music-controller"]
---

# Canonical Summary

> Current MIDI Association and Bluetooth SIG public pages support one narrow MIDI lane only. `MIDI` may be used as standards-owner protocol identity. `USB-MIDI` may be used as named transport vocabulary where USB Class Definitions for MIDI Devices define how USB transports MIDI data. `BLE-MIDI` may be used as the named wireless MIDI transport specification over Bluetooth Low Energy. Bluetooth may be used as standards-owner wireless terminology and qualification-entry framing. None of these sources prove DAW support, universal host compatibility, no-driver behavior, latency, jitter, timing accuracy, pad sensitivity, keybed performance, audio quality, Bluetooth qualification status, or HILPCB capability.

## Stable Facts

- The MIDI Association publicly maintains the official MIDI specification hub and frames MIDI specifications as the layer that makes MIDI products work together.
- The MIDI Association publicly provides `USB-MIDI` as a named transport page and states that USB Class Definitions for MIDI Devices define how USB transports MIDI data.
- The MIDI Association publicly provides `BLE-MIDI` as a named transport page and states that the specification defines a method for encoding and decoding MIDI data over Bluetooth Low Energy connections.
- `USB-MIDI` and `BLE-MIDI` are transport-level MIDI nouns and should not be collapsed into generic product-compatibility promises.
- Bluetooth SIG publicly provides Bluetooth identity and a separate qualification-process entry page, so Bluetooth terminology and Bluetooth qualification must remain separate layers.

## Conditions And Methods

- Use this card when a music-device PCB article needs exact nouns such as `MIDI`, `USB-MIDI`, `BLE-MIDI`, or Bluetooth Low Energy transport context.
- Safe `MIDI` posture:
  use `MIDI` as standards-owner protocol-family identity and interoperability vocabulary only.
- Safe `USB-MIDI` posture:
  use `USB-MIDI` as transport-class vocabulary for carrying MIDI over USB, not as proof that an unnamed PCB or product is universally class-compliant across hosts.
- Safe `BLE-MIDI` posture:
  use `BLE-MIDI` as the named MIDI transport specification over Bluetooth Low Energy, not as proof of app support, OS support, or wireless-performance outcomes.
- Safe Bluetooth posture:
  use Bluetooth as standards-owner wireless terminology, and keep Bluetooth qualification wording separate from transport identity.
- Pair this card with `facts/standards/interface-wireless-and-positioning-product-level-boundary.md` when broader Bluetooth boundary wording is needed.

## Limits And Non-Claims

- This card does not authorize `DAW-compatible`, `plug-and-play`, `driverless`, `class-compliant on all hosts`, `works with iOS/macOS/Windows/Android`, or similar claims for an unnamed PCB, controller, keypad, or keyboard.
- It does not authorize latency, jitter, timing-resolution, scan-rate, pad-sensitivity, velocity, aftertouch, encoder-precision, or fader-response claims.
- It does not authorize DAC / ADC, `THD`, `SNR`, dynamic-range, sample-rate, bit-depth, DSP, CPU, memory, storage, or polyphony claims.
- It does not authorize Bluetooth qualification proof, wireless range, coexistence, battery life, or RF-performance claims.
- It does not authorize HILPCB capability, lead time, inspection, quality, regulated-program, or certification-status claims.

## Open Questions

- Add an OS-vendor class-support split later only if a future rewrite genuinely needs bounded host-support wording beyond protocol-owner transport identity.
- Add separate DAW / control-surface / audio-path lanes later if future drafts require exact protocol or component-owner proof there.
- Do not stretch this card into synthesizer-engine, audio-fidelity, or generic Bluetooth-product compliance claims.

## Source Links

- https://midi.org/specs
- https://midi.org/usb-midi
- https://midi.org/midi-over-bluetooth-low-energy-ble-midi
- https://www.bluetooth.com/specifications/specs/core-specification/
- https://www.bluetooth.com/develop-with-bluetooth/qualify/
