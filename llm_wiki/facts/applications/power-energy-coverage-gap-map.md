---
fact_id: "applications-power-energy-coverage-gap-map"
title: "Power / Energy application coverage gap map: which board families have wiki-level routing and which remain overview-only"
topic: "Power and energy PCB/PCBA application coverage"
category: "applications"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
last_reconciled_at: "2026-05-03"
reconciliation_notes: "P4-185 initial build; sourced from wiki/applications/power-energy-pcb-pcba-review-boundaries.md (active as of P4-178), related power/energy standards and method cards"
source_ids:
  - "frontendapt-industry-power-energy-page-en"
  - "frontendapt-pcb-heavy-copper-pcb-page-en"
  - "frontendapt-pcb-high-thermal-pcb-page-en"
  - "frontendapt-pcb-metal-core-pcb-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-fct-test-page-en"
  - "iec-61851-1-2017-product-page"
  - "iec-61851-23-2023-product-page"
  - "iso-15118-1-2019-page"
  - "iso-15118-20-2022-page"
  - "sae-j1772-202401-recommended-practice-page"
  - "charin-iso-iec-15118-communication-standard-page"
  - "open-charge-alliance-ocpp-protocols-page"
tags: ["power-energy", "ev-charger", "inverter", "smart-meter", "renewable-energy", "thermal-platform", "coverage-map", "gap-map"]
---

# Canonical Summary

> As of 2026-05-03 after P4-185 initial build, the power/energy application family has a dedicated wiki boundary page (`wiki/applications/power-energy-pcb-pcba-review-boundaries.md`) and that page is now `active`. This fact card maps what the current internal and public source layer supports, which board families are addressable, and which compliance/performance layers remain blocked.

## Board Family Coverage State

### Supported at Scenario + Board-Class Level

All entries below are supported by the Tier-2 internal source (`frontendapt-industry-power-energy-page-en`) plus official standards-identity pages. They support board-class and execution-context vocabulary. They do NOT prove charging compliance, inverter efficiency, metrology approval, or field readiness.

| Board Family | Application Context | PCB/PCBA Vocabulary Supported |
|---|---|---|
| **Central Inverter Board** | Power stage, control, monitoring, interface, and thermal-planning context | Board partition review (power stage / control / monitoring), heavy copper, thermal vias, DFM/DFT/DFA vocabulary |
| **Ultra-Fast Charger Board** | Power-board plus control-board partitioning; cable/bus interfaces | Partition review, isolation/creepage design language, layered validation workflow vocabulary |
| **Type-C Charger Board** | Compact charger PCB; connector-access planning, functional test | Compact board assembly, connector-access planning, powered functional test vocabulary only |
| **Smart Meter PCB** | Metrology front-end board partitioning; AMI and utility-meter context | Guarded IEC 62052/62053/MID/ANSI C12.20 vocabulary; DLMS/COSEM/PRIME/G3-PLC/Wi-SUN/Zigbee/NB-IoT/LTE-M identity-only |
| **EV Charger Control Board** | Charger-board partitioning, protocol interface, backend connectivity | IEC 61851/ISO 15118/SAE J1772/CCS/NACS/OCPP identity-level vocabulary; NOT compliance or interoperability proof |
| **Boundary-Scan JTAG Inverter** | Digital test access on controller or communications subassemblies | Boundary-scan vocabulary for digital control boards; NOT power-stage correctness |
| **DFM/DFT/DFA Review** | Review sequencing, access planning, and validation gates | DFM/DFT/DFA gate vocabulary; NOT field reliability or standards approval |
| **Conformal Coating (EV/Automotive Power)** | Environment protection and masking/access planning | Coating workflow vocabulary; NOT automotive qualification or high-voltage proof |

### Thermal Platform Support

| Platform | What Is Supported |
|---|---|
| Heavy Copper PCB | Heavy-copper board vocabulary as a distinct route choice for high-current power stages; NOT recipe or universal recommendation |
| MCPCB (Metal Core PCB) | MCPCB board vocabulary as a distinct thermal option for LED/power boards; NOT thermal-outcome guarantee |
| High Thermal PCB | High-thermal board vocabulary as a distinct option family; NOT exact recipe or superiority claim |

### Fact Cards Supported

| Fact Card | What It Supports |
|---|---|
| `methods-power-energy-inverter-charger-rewrite-boundary` | General power/energy inverter and charger rewrite boundary |
| `methods-pcba-dfm-dft-dfa-review-gate-positioning` | DFM/DFT/DFA review gate positioning |
| `methods-pcba-boundary-scan-jtag-positioning` | Boundary-scan / JTAG test-access positioning |
| `methods-conformal-coating-lane-b-rewrite-gate` | Conformal coating Lane B rewrite gate |
| `methods-thermal-pcb-platform-selection-posture` | Thermal PCB platform selection posture |
| `methods-tht-pressfit-terminal-route-boundary` | THT, press-fit, and terminal route boundary |
| `standards-smart-meter-standards-and-metrology-identity-boundary` | Smart meter standards and metrology identity boundary |
| `standards-smart-meter-communication-protocol-identity-boundary` | Smart meter communication protocol identity boundary |
| `standards-ev-charger-control-stack-and-protocol-identity-boundary` | EV charger control stack and protocol identity boundary |

### Standards Context Supported (Official Sources)

| Standard/Protocol | What It Supports |
|---|---|
| `IEC 61851-1/-23/-24` | EV charging system architecture vocabulary; conductive charging context; NOT compliance, interoperability, payment |
| `ISO 15118 (V2X/V2G)` | Vehicle-to-grid communication vocabulary; high-level protocol identity; NOT plug-and-charge interoperability |
| `SAE J1772 / J3400 (CCS/NACS)` | North American charging connector/communication identity; NOT connector protocol behavior |
| `OCPP 2.0.1` | Open charge point protocol identity; backend connectivity context; NOT payment integration or interoperability |
| `IEC 62052/62053 (Smart Meter)` | Metrology standard-family vocabulary; utility-meter context; NOT exact compliance or accuracy classes |
| `MID / MI-003 / ANSI C12.20` | Metrology regulation/regime identity; NOT metrology approval or service-life guarantees |
| `DLMS/COSEM / PRIME / G3-PLC / Wi-SUN / Zigbee / NB-IoT / LTE-M` | AMI communication technology identity only; NOT protocol interoperability or network behavior |

## Stable Facts

- The Tier-2 internal source supports 8 distinct power/energy board families at scenario and board-class level.
- All three thermal platform families (heavy copper, MCPCB, high thermal) are supported as distinct route choice vocabulary, not as exact recipes or universal recommendations.
- EV charger protocol vocabulary (IEC 61851, ISO 15118, SAE J1772, OCPP) is supported at identity-level only; compliance, interoperability, and payment claims are NOT supported.
- Smart meter vocabulary (IEC 62052/62053, MID, DLMS/COSEM) is supported at document-family/identity level only; exact accuracy classes, compliance proof, and interoperability claims are NOT supported.
- Boundary-scan vocabulary is limited to digital control/monitoring boards, not the main power path.

## Conditions And Methods

- Use this card to confirm what vocabulary is safe before writing a power/energy PCB/PCBA article.
- For EV charger protocol vocabulary, route to `facts/standards/ev-charger-control-stack-and-protocol-identity-boundary`.
- For smart meter standards vocabulary, route to `facts/standards/smart-meter-standards-and-metrology-identity-boundary`.
- For thermal platform selection vocabulary, route to `facts/methods/thermal-pcb-platform-selection-posture`.
- For heavy copper / high-current vocabulary, route to `facts/methods/current-carrying-trace-width-and-copper-boundary`.
- For EV/automotive power overlap, route to `wiki/applications/automotive-ev-pcb-pcba-boundary-map.md`.
- Update `last_reconciled_at` when a new power/energy wiki boundary page is created.

## Limits And Non-Claims

- Charging speed, cable current, or connector protocol behavior claims are NOT supported.
- Inverter efficiency, power density, insulation, or grid compliance claims are NOT supported.
- Smart meter accuracy class, MID marking, ANSI C12.20 approval, or metrology certification is NOT supported.
- EV charger IEC 61851/ISO 15118/SAE J1772/CCS/NACS/OCPP compliance or interoperability is NOT supported.
- Coating qualification (ASIL, ISO 26262, creepage, qualification outcomes) is NOT supported.
- Thermal platform universal recipe or superiority claims are NOT supported.
- Yield, throughput, cost, or lead-time claims are NOT supported.

## Remaining Gaps

| Gap | Reopen Condition |
|---|---|
| Dedicated power/energy wiki boundary page | Closed — created and promoted to `active` in P4-178 |
| Companion fact card (this file) | Closed — created in P4-185 |
| IEC 61851 exact clause-level vocabulary | Official IEC publication page with stable public URL |
| ISO 15118 exact protocol vocabulary | Official ISO document page with stable public URL |
| SAE J1772 / J3400 exact connector specification | Official SAE document page with stable public URL |
| IEC 62052/62053 exact metrology test vocabulary | Official IEC metrology standard page with stable public URL |
| Grid code / UL / EMC (CISPR 32, IEC 61000) vocabulary | Official UL or IEC publication page with stable URL |
| Coating qualification (creepage, clearance, insulation) vocabulary | IEC 60664 or UL official publication page recovery |
