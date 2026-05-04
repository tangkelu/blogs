---
fact_id: "applications-automotive-ev-coverage-gap-map"
title: "Automotive / EV application coverage gap map: which board families have wiki-layer routing and which remain overview-only"
topic: "Automotive and EV PCB/PCBA application coverage"
category: "applications"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
last_reconciled_at: "2026-05-03"
reconciliation_notes: "P4-157 initial build; sourced from frontendapt-industry-automotive-electronics-page-en (Tier-2), standards-automotive-medical-aerospace-application-qualification-boundary, and power-energy-pcb-pcba-review-boundaries.md"
source_ids:
  - "frontendapt-industry-automotive-electronics-page-en"
  - "iso-26262-road-vehicles-functional-safety-package"
  - "iatf-16949-overview-page"
  - "aec-documents-page"
tags: ["automotive", "ev", "bms", "adas", "ecu", "obc", "inverter", "coverage-map", "gap-map"]
---

# Canonical Summary

> As of 2026-05-03 after P4-168 activation review, the automotive / EV application family has a dedicated wiki boundary page (`wiki/applications/automotive-ev-pcb-pcba-boundary-map.md`) and that page is now `active`. This fact card maps what the current internal source supports, what adjacent routes still apply, and which standards/compliance layers remain blocked.

## Board Family Coverage State

### Supported at Scenario + Board-Class Level (Tier-2 Internal Source)

All entries below are extracted from `frontendapt-industry-automotive-electronics-page-en` (Tier-2). They support PCB/PCBA board-class vocabulary and engineering context. They do NOT prove certification, qualification, reliability, or OEM approval.

| Board Family | Application Context | PCB/PCBA Vocabulary Supported |
|---|---|---|
| **ECU / Vehicle Control** | Engine ECU, BCM, domain controllers, gateway ECUs | High-Tg materials, mixed-signal routing, CAN/LIN/FlexRay/Ethernet traces, connector interface geometry |
| **Inverter / Motor Control** | Traction inverters, e-axles, auxiliary drives | High-voltage creepage/clearance design language, thick copper, thermal vias, gate-driver / MCU / sensing integration, EMC-aware layout |
| **BMS (Battery Management)** | Pack-level BMS master, cell monitoring slave, LV/HV junction box | Differential cell-sense routing, isolation / slot / coating design, CAN/SPI/UART balancing interfaces |
| **OBC / DC-DC / Charger** | On-board charger, DC-DC converter, wallbox charger, fast DC charger | AC-DC / DC-DC power stage PCB layout, isolation/creepage, thermal-mechanical integration |
| **ADAS / Radar / Camera** | Radar modules, camera, domain controller, sensor fusion | RF/LVDS/MIPI front-end layout, exterior-mounting material/coating options, CAN/Ethernet network integration |
| **Infotainment / TCU** | Head unit, digital cluster, telematics, gateway | LVDS/MIPI/HDMI display links, 4G/5G/GNSS/Wi-Fi/Bluetooth antenna interface, CAN/Ethernet gateway |
| **Lighting / Body / BCM** | LED headlamp, DRL/tail lamp, BCM, seat/HVAC/window control | MCPCB/FR-4 LED boards, body control board routing, environmental/vibration/moisture design considerations |

### Quality/Test Steps Supported (Tier-2 Internal Source)

- SPI → AOI → X-ray (BGA/LGA/QFN) → ICT/flying-probe (where test points exist) → FCT → final inspection + traceability
- VIN-to-board traceability vocabulary supported at process-description level
- PPAP/validation phase staging referenced at description level only

### Standards Context Supported (Official Sources)

| Standard | What It Supports |
|---|---|
| `ISO 26262` | Road-vehicle E/E functional-safety vocabulary (system/software lifecycle); NOT PCB readiness proof |
| `IATF 16949` | Automotive QMS vocabulary; NOT certification status proof |
| `AEC-Q` document family | Electronic component qualification document-family discovery; NOT PCB or supplier qualification proof |

## Stable Facts

- The Tier-2 internal automotive source covers 7 distinct board families: ECU, inverter/motor-control, BMS, OBC/charger, ADAS/radar/camera, infotainment/connectivity, and lighting/body/BCM.
- The source supports board-class and assembly-context vocabulary, not performance or qualification claims.
- Thermal test vocabulary (-40 to 125 °C cycling) and vibration test vocabulary (5 Grms / 10 h) appear in the source but are described as capability context, not as guaranteed lot-level outcomes.
- Cleanliness vocabulary (ROSE ≤1.5 µg/cm²) appears in the source; treat as process-description level, not as published specification proof.
- EV charging board vocabulary (OBC, DC-DC, fast charger) overlaps with the power-energy wiki page; do not duplicate; route charger PCB prompts to `wiki/applications/power-energy-pcb-pcba-review-boundaries.md` for the EV-charger control-stack boundary.
- ADAS radar PCB vocabulary partially overlaps with `wiki/applications/sensor-navigation-imaging-pcb-review-boundaries.md` for radar front-end context.

## Conditions And Methods

- Use this card to confirm what vocabulary is safe before writing an automotive/EV PCB article.
- For EV charger control-stack protocol claims (IEC 61851, ISO 15118, SAE J1772, OCPP), route to the power-energy boundary page.
- For ADAS radar/sensor front-end PCB claims, confirm overlap with the sensor/navigation/imaging boundary page.
- Update `last_reconciled_at` when a new automotive-specific wiki boundary page is created.

## Limits And Non-Claims

- ISO 26262 (ASIL) compliance, functional safety allocation, or PCB ASIL rating claims are NOT supported.
- IATF 16949 certification validity, PPAP completion, or OEM approval is NOT supported.
- AEC-Q component qualification proof is NOT supported.
- Thermal cycling pass/fail, vibration pass/fail, or cleanliness test lot-level proof is NOT supported.
- Exact creepage, clearance, insulation, or high-voltage safety thresholds are NOT supported.
- Field reliability, warranty outcomes, customer satisfaction, or OEM program deployment is NOT supported.
- Yield, throughput, cost, or lead-time claims are NOT supported.

## Remaining Gaps

| Gap | Reopen Condition |
|-----|-----------------|
| Dedicated automotive/EV wiki boundary page | Closed — created in P4-157 and promoted to `active` in P4-168 |
| ISO 26262 / ASIL exact clause-level vocabulary | Official ISO 26262 part-level source recovery |
| IATF 16949 exact process-requirement vocabulary | IATF official certificate/audit language source |
| AEC-Q exact qualification test vocabulary | AEC-Q document-level source with test-method detail |
| Automotive EMC (CISPR 25, ISO 11452) boundary | New official EMC standard source |
| Automotive network protocol depth (CAN FD, Automotive Ethernet, FlexRay) | IEEE / CiA / OPEN Alliance source recovery |
| Dedicated automotive/EV wiki page status | Reopen only if the page later regresses and requires demotion from `active` |
