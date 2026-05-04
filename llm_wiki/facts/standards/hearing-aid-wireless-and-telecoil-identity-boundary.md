---
fact_id: "standards-hearing-aid-wireless-and-telecoil-identity-boundary"
title: "LE Audio, Auracast, telecoil, and induction-loop sources support hearing-assistance identity, not interoperability or readiness proof"
topic: "Hearing-aid wireless and telecoil identity boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-01"
source_ids:
  - "bluetooth-le-audio-page"
  - "bluetooth-le-audio-hearing-page"
  - "bluetooth-auracast-page"
  - "iec-60118-4-2014-a1-2017-csv-page"
  - "nidcd-hearing-aids-page"
tags: ["hearing-aid", "le-audio", "auracast", "telecoil", "induction-loop", "assistive-listening", "bluetooth", "iec-60118-4"]
---

# Canonical Summary

> Current Bluetooth SIG, IEC, and NIDCD public pages support one narrow hearing-aid identity lane only. `LE Audio` may be used as the named Bluetooth audio family that adds hearing-aid support and introduces `Auracast` broadcast audio. `Auracast` may be used as the named Bluetooth broadcast-audio capability and as hearing-assistance context, but not as proof of deployed assistive-listening readiness. `telecoil` may be used as the named magnetic-coil feature used in some hearing aids. `induction loop systems` may be used as the named system family described by `IEC 60118-4` for hearing-aid purposes and by NIDCD as telecoil-adjacent hearing-assistance context. None of these sources prove that a specific PCB, hearing aid, module, antenna, supplier, or venue is qualified, interoperable, compliant, available, or product-ready.

## Stable Facts

- Bluetooth SIG publicly identifies `LE Audio` as the next generation of Bluetooth audio, adds support for hearing aids, and introduces `Auracast` broadcast audio.
- Bluetooth SIG publicly frames `LE Audio` hearing support as hearing-assistance context and positions `Auracast` as the next generation of assistive listening systems.
- Bluetooth SIG publicly identifies `Auracast` as a Bluetooth broadcast-audio capability within the broader Bluetooth audio ecosystem.
- IEC publicly identifies `IEC 60118-4:2014+AMD1:2017 CSV` as `Electroacoustics - Hearing aids - Part 4: Induction-loop systems for hearing aid purposes - System performance requirements`.
- The IEC `60118-4` page publicly states that the standard applies to induction-loop systems intended to provide an input signal for hearing aids operating with an induction pick-up coil, also called a `telecoil`.
- NIDCD publicly describes a `telecoil` as a small magnetic coil feature that may be present in some hearing aids and links telecoil use to `induction loop systems`.

## Conditions And Methods

- Use this card when a rewrite needs exact hearing-assistance nouns such as `LE Audio`, `Auracast`, `telecoil`, `induction loop systems`, or `hearing assistance`.
- Keep layer separation explicit:
  treat `LE Audio` as the Bluetooth audio family name; treat `Auracast` as a broadcast-audio capability name within Bluetooth hearing-assistance context; treat `telecoil` as a hearing-aid feature noun; treat `induction loop systems` as the named system family used with telecoil-equipped hearing aids.
- Safe `hearing-assistance` posture:
  use `hearing assistance`, `assistive listening`, or `hearing-aid support` only as technology-context vocabulary from Bluetooth SIG, IEC, or NIDCD. Do not turn those terms into product qualification or deployment proof.
- Safe `telecoil` posture:
  use `telecoil` only as feature identity and hearing-aid input context. Do not infer exact coil geometry, PCB implementation, shielding method, orientation rule, or finished-device performance from this card.
- Pair this card with `facts/standards/interface-wireless-and-positioning-product-level-boundary.md` when a rewrite also needs generic Bluetooth boundary language, and pair it with medical manufacturing-control boundaries only if the rewrite separately needs regulated-documentation posture.

## Limits And Non-Claims

- This card does not authorize `LE Audio qualified`, `Auracast ready`, `telecoil compliant`, `IEC 60118-4 compliant`, `assistive-listening certified`, or equivalent product claims.
- It does not authorize exact interoperability, compatibility, conformance, readiness, qualification, certification, or deployment claims for any hearing aid, PCB, wireless subsystem, venue, or supplier.
- It does not authorize `LC3` numerics, RF path-loss numerics, body-loss numerics, battery-life numerics, latency numerics, or antenna-performance numerics.
- It does not authorize public-venue availability claims, rollout claims, adoption claims, or market-coverage claims for `Auracast`, `LE Audio`, telecoil systems, or induction-loop systems.
- It does not authorize telecoil field-strength thresholds, exact frequency-response claims, intelligibility thresholds, magnetic-performance thresholds, or measurement claims from `IEC 60118-4`.
- It does not authorize `IEC 60118-13`, `FDA class`, `ISO 13485`, supplier capability, supplier certification, or medical-device release claims from the same draft.
- It does not authorize treating `LE Audio`, `Auracast`, `telecoil`, and `induction loop systems` as interchangeable same-layer concepts.

## Open Questions

- Add a later split only if a future rewrite genuinely needs narrower source-backed treatment for hearing-aid immunity, charging, biocompatibility, or regulated medical-device role boundaries.
- Add `IEC 60118-13`, charging-family, or biocompatibility sources only if a future rewrite truly must keep those exact nouns.

## Source Links

- https://www.bluetooth.com/learn-about-bluetooth/feature-enhancements/le-audio/
- https://www.bluetooth.com/learn-about-bluetooth/feature-enhancements/le-audio/hearing/
- https://www.bluetooth.com/auracast/
- https://webstore.iec.ch/en/publication/61949
- https://www.nidcd.nih.gov/health/hearing-aids
