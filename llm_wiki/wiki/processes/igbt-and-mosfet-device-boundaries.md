---
wiki_id: "wiki-processes-igbt-and-mosfet-device-boundaries"
title: "IGBT and MOSFET device boundaries"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-03"
fact_ids:
  - "methods-igbt-vs-mosfet-device-identity-boundary"
  - "methods-power-energy-inverter-charger-rewrite-boundary"
source_ids:
  - "st-power-mosfets-page"
  - "infineon-igbt-discretes-page"
  - "infineon-bjt-mosfet-igbt-difference-page"
tags: ["igbt", "mosfet", "power-device", "power-electronics", "device-identity", "terminal-vocabulary", "packaging-boundary"]
---

# Use This Page For

- Routing `IGBT vs MOSFET` drafts into a safe device-boundary explanation.
- Separating device identity, terminal vocabulary, diode/packaging boundary, and broad application context from unsupported design-selection rules.
- Preventing power-device comparison drafts from turning into universal threshold, efficiency, or replacement guides.

# Core Boundary Rule

- Start with device-class identity, not with selection thresholds.
- `MOSFET` and `IGBT` are adjacent but distinct power-device classes.
- The current local corpus supports conservative explanation of:
  terminal names, broad device behavior vocabulary, diode/packaging boundary, and category-level application routing.
- It does not support universal design-choice rules.

# Device Identity

## MOSFET

- Route `MOSFET` language through voltage-controlled device identity with gate, drain, and source terminal vocabulary.
- `RDS(on)` and intrinsic body-diode wording are safe at device-class level only.
- Do not turn body-diode vocabulary into a universal statement about identical reverse-recovery or freewheel behavior across all MOSFETs.

## IGBT

- Route `IGBT` language through distinct gate-controlled power-device identity with gate, collector, and emitter terminal vocabulary.
- Safe local support exists for the boundary that IGBT packages may be offered with or without an anti-parallel diode.
- Do not flatten package-dependent diode treatment into a universal built-in feature claim.

# Terminal Vocabulary

| Device class | Safe terminal vocabulary | Safe adjacent vocabulary |
| --- | --- | --- |
| MOSFET | gate, drain, source | `RDS(on)`, intrinsic body diode |
| IGBT | gate, collector, emitter | anti-parallel diode may be package-dependent |

- Use terminal naming to explain why the two device classes should not be casually collapsed into one generic `power switch` story.
- If a draft needs gate-drive voltage, drive current, dead time, SOA, or protection timing, stop and require narrower sources.

# Packaging And Diode Boundary

- The current local support is strong enough to explain that diode treatment differs by device class and package context.
- Safe wording:
  MOSFETs are commonly described with intrinsic body-diode vocabulary, while IGBT offerings may appear with or without an anti-parallel diode depending on package or topology.
- Unsafe wording:
  every MOSFET has the same usable diode behavior, or every IGBT includes the same freewheel-path arrangement.

# Safe Routing Into Application Context

- Broad application-family language is safe only at category level.
- Route inverter, charger, UPS, motor drive, solar, welding, and adjacent power-conversion context through `methods-power-energy-inverter-charger-rewrite-boundary`.
- Use application context to describe where these device classes appear, not to publish topology-independent best-choice rules.

| Draft signal | Safe route | Block if draft asks for |
| --- | --- | --- |
| `what is MOSFET vs IGBT` | device identity and terminal vocabulary | exact thresholds, efficiency tables, replacement guidance |
| `IGBT in inverter` | power-energy application context plus device boundary | switching-loss, thermal, current, power, or standards proof |
| `MOSFET for charger` | category-level charger context plus device boundary | universal frequency, voltage, or efficiency rule |
| `can I replace IGBT with MOSFET` | exact-part and topology review warning | direct replacement advice |

# Safe Selection Language

- Write `distinct power-device classes` instead of implying one universal switch ladder.
- Write `terminal naming and packaging differences` instead of claiming one device is broadly superior.
- Write `exact substitution requires exact part and circuit review` instead of publishing family-level replacement advice.
- Write `broad application context` instead of universal inverter/charger design thresholds.

# Unsafe Selection Language

- Do not publish `MOSFET below X volts, IGBT above Y volts` style rules from this boundary layer.
- Do not claim one device is always faster, more efficient, lower loss, or better for high power.
- Do not claim a MOSFET and an IGBT are direct replacements in most circuits.
- Do not turn manufacturer category pages into universal switching-frequency, conduction-loss, thermal, or EMI guidance.

# Blocked Claims

- universal selection thresholds
- switching-loss and efficiency guarantees
- direct replacement claims
- cost/lead-time/yield claims

# Must Refresh Before Publishing

- Any exact voltage, current, power, frequency, switching-loss, conduction-loss, thermal, EMI, SOA, or gate-drive claim
- Any diode reverse-recovery, freewheel-path, protection-strategy, or short-circuit withstand claim
- Any current product-family comparison, pricing, availability, or replacement table
- Any statement framed as current best choice or universal design rule

# Related Fact Cards

- `methods-igbt-vs-mosfet-device-identity-boundary`
- `methods-power-energy-inverter-charger-rewrite-boundary`

# Local Source Records

- `st-power-mosfets-page`
- `infineon-igbt-discretes-page`
- `infineon-bjt-mosfet-igbt-difference-page`
