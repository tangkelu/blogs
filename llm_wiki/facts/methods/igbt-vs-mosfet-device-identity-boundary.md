---
fact_id: "methods-igbt-vs-mosfet-device-identity-boundary"
title: "IGBT versus MOSFET writing is source-backed for device identity and packaging boundaries, not for universal selection windows"
topic: "IGBT versus MOSFET device identity boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-29"
source_ids:
  - "st-power-mosfets-page"
  - "infineon-igbt-discretes-page"
  - "infineon-bjt-mosfet-igbt-difference-page"
tags: ["igbt", "mosfet", "power-semiconductor", "device-identity", "body-diode", "anti-parallel-diode", "selection-boundary"]
---

# Canonical Summary

> Official manufacturer sources support a conservative `IGBT vs MOSFET` boundary at device-class level: a power MOSFET is a voltage-controlled insulated-gate transistor with gate, drain, and source terminals, `RDS(on)` framing, and an intrinsic body-diode context; an IGBT is a separate gate-controlled power-device family with gate, collector, and emitter terminals, and its package may be offered with or without an anti-parallel diode. These sources do not authorize universal voltage, current, frequency, efficiency, EMI, or replacement rules.

## Stable Facts

- ST's official power MOSFET page describes MOSFETs as voltage-controlled devices with gate, drain, and source terminals.
- The same ST page uses `RDS(on)` and intrinsic body-diode language as part of the MOSFET device-class description.
- Infineon's official IGBT discrete-device page frames IGBTs as a distinct gate-controlled power-device family with collector, emitter, and gate terminals.
- Infineon's IGBT page shows that discrete IGBT offerings may come with or without an anti-parallel diode, so the diode treatment must be described as package- or topology-dependent rather than universal.
- Infineon's comparison page supports the high-level distinction that MOSFET and IGBT device classes differ in carrier behavior and should not be treated as interchangeable labels.
- The manufacturer pages support broad application-family context only: MOSFETs appear across switched-mode power supplies, motor control, lighting, automotive, and other power-conversion uses, while IGBTs appear in higher-power industrial contexts such as motor drives, solar, UPS, and welding.

## Conditions And Methods

- Use this card for `/code/blogs/tmps/2025.11.17/en/igbt-vs-mosfet.md` and adjacent power-device glossary or boundary drafts.
- Safe posture: explain terminal names, device-family identity, diode-boundary differences, and broad application context.
- Safe comparison posture: say the two device classes use different internal operating principles and packaging conventions, so exact substitution requires exact product and circuit review.
- If the draft moves into switching loss, conduction loss, safe operating area, gate-drive thresholds, freewheel strategy, short-circuit withstand, thermal performance, or waveform quality, stop and require narrower sources.

## Limits And Non-Claims

- This card does not authorize rules such as `use MOSFET below X volts` or `use IGBT above Y volts`.
- It does not authorize exact switching-frequency, efficiency, conduction-loss, turn-off-tail, EMI, or thermal-performance claims.
- It does not prove that every MOSFET has the same body-diode behavior or that every IGBT includes a diode.
- It does not support universal claims that one device is better, faster, cheaper, or more reliable than the other.
- It does not support direct replacement guidance without exact datasheets, circuit topology, and validation context.

## Open Questions

- Add exact vendor application notes if a future pass needs source-backed discussion of gate-drive strategy, freewheel paths, or switching-loss tradeoffs.
- Add standards-owner or textbook-grade glossary anchors if future drafts need a more neutral terminology source than manufacturer pages.

## Source Links

- https://www.st.com/content/st_com/en/products/power-transistors/power-mosfets.html
- https://www.infineon.com/products/power/igbt/igbt-discretes
- https://www.infineon.com/cms/en/about-infineon/company/research-and-development/power-semiconductors-what-is-the-difference-between-bjts-mosfets-and-igbts/
