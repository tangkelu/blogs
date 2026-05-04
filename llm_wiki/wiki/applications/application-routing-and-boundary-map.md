---
topic_id: "applications-application-routing-and-boundary-map"
title: "Application Routing And Boundary Map"
category: "applications"
status: "active"
last_reviewed_at: "2026-05-03"
fact_ids:
  - "applications-application-coverage-gap-map"
  - "applications-apt-pcb-industry-applications-overview"
  - "methods-internal-application-scenario-coverage-map"
source_ids:
  - "frontendapt-industry-aerospace-defense-page-en"
  - "frontendapt-industry-automotive-electronics-page-en"
  - "frontendapt-industry-communication-equipment-page-en"
  - "frontendapt-industry-drone-uav-page-en"
  - "frontendapt-industry-industrial-control-page-en"
  - "frontendapt-industry-medical-page-en"
  - "frontendapt-industry-power-energy-page-en"
  - "frontendapt-industry-robotics-page-en"
  - "frontendapt-industry-security-equipment-page-en"
  - "frontendapt-industry-server-data-center-page-en"
tags: ["applications", "routing-map", "boundary-map", "coverage", "gap-map", "wiki-routing"]
---

# Definition

> The application routing and boundary map is the single prompt-entry point for selecting which wiki page to consult when writing application-layer PCB/PCBA content. Use this page first. Dedicated routing now exists for all currently indexed APT industry families. All 14 current dedicated application pages are `active`, all 14 have companion application fact cards, and all 14 now also have dedicated evidence packs. The application evidence-pack gap is closed for the current indexed set.

## Why This Topic Matters

- The application wiki layer has grown non-uniformly: some segments have dedicated boundary pages while others have only overview coverage.
- Without a routing map, agents re-open already-covered families, miss existing boundary pages, or write past the real coverage ceiling.
- This page prevents duplication and stops agents from treating the overview layer as if it provides execution-boundary routing.

---

## Primary Routing Table

Use this table as the first-pass decision gate:

| Application / Market | Dedicated Wiki Boundary Page? | Route To |
|---|---|---|
| **5G / Telecom / Base Station** | ✅ Yes | `wiki/applications/5g-telecom-pcb-execution-boundary-map.md` |
| **Compute / Server / AI Accelerator / Data Center** | ✅ Yes | `wiki/applications/compute-infrastructure-pcb-review-boundaries.md` |
| **Defense / EW / Surveillance / Targeting / Avionics-adjacent** | ✅ Yes | `wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md` |
| **Sensor / Navigation / Imaging / Radar / LIDAR** | ✅ Yes | `wiki/applications/sensor-navigation-imaging-pcb-review-boundaries.md` |
| **Power / Energy / Inverter / EV Charging / ESS** | ✅ Yes | `wiki/applications/power-energy-pcb-pcba-review-boundaries.md` |
| **Hearing Aid / Hearing Assistance** | ✅ Yes | `wiki/applications/hearing-aid-pcb-review-boundaries.md` |
| **Maker / Smart Home / IoT Platform / ESP32 / Raspberry Pi** | ✅ Yes | `wiki/applications/maker-and-smart-home-platform-boundaries.md` |
| **Automotive / EV / BMS / ECU / ADAS** | ✅ Yes | `wiki/applications/automotive-ev-pcb-pcba-boundary-map.md` |
| **Industrial Control / PLC / HMI / Servo** | ✅ Yes | `wiki/applications/industrial-control-pcb-pcba-boundary-map.md` |
| **Robotics / AGV / Cobot** | ✅ Yes | `wiki/applications/robotics-agv-cobot-pcb-pcba-boundary-map.md` |
| **Medical (broad: imaging / diagnostics / wearable)** | ✅ Yes | `wiki/applications/medical-device-pcb-pcba-boundary-map.md` |
| **Drone / UAV / Flight Controller** | ✅ Yes | `wiki/applications/drone-uav-pcb-pcba-boundary-map.md` |
| **Security Equipment / Cameras / Access Control** | ✅ Yes | `wiki/applications/security-equipment-pcb-pcba-boundary-map.md` |
| **Aerospace (civil, non-defense)** | ✅ Yes | `wiki/applications/civil-aerospace-pcb-pcba-boundary-map.md` |

---

## Coverage Tier Definitions

| Tier | Meaning | What You Can Do |
|------|---------|-----------------|
| **Wiki-Layer Complete** | Dedicated boundary page exists covering execution vocabulary, capability claims, blocked claims, and routing instructions | Use the boundary page as the primary routing frame; stay within its blocked-claims list |
| **Overview Only** | Covered only in the multi-segment overview pages; no execution-boundary routing for this segment | Use for scenario framing only; do not write execution-boundary content (materials, stackups, test flows, certification language) without opening a new boundary lane |
| **Partial** | Relevant vocabulary covered in an adjacent boundary page, but not via a dedicated page for this exact segment | Extract only the narrow overlap that the adjacent page explicitly covers; do not extrapolate to the full segment |

---

## Stable Facts

- As of 2026-05-03 after P4-202 reconciliation, 14 dedicated wiki boundary pages exist covering 5G telecom, compute, defense/EW/surveillance, sensor/navigation/imaging, power/energy, hearing aid, maker/smart-home, automotive/EV, industrial control, medical broad, robotics, security equipment, drone/UAV, and civil aerospace.
- The first-pass application routing gap is closed, and all 14 current families also have companion application fact cards.
- All 14 current dedicated application boundary pages are now `active`.
- Dedicated application evidence packs now exist for all 14 current application families.
- `wiki/applications/apt-pcb-industry-solutions-guide.md` has no YAML frontmatter; treat it as an unstructured reference document, not a wiki card.
- `facts/applications/application-coverage-gap-map.md` is the machine-readable version of this routing state.

---

## Engineering Boundaries

- Do not use the overview pages (`industry-application-scenarios-and-boundaries.md`, `apt-pcb-industry-solutions-guide.md`) to make execution-boundary claims for any specific market segment.
- Do not assume that a market page in `frontendapt-industry-*` implies a dedicated wiki boundary page; check this routing table first.
- Do not use an adjacent boundary page to extend claims across regulated vocabularies that now have their own dedicated page (e.g., do not use the defense page to write civil aerospace or drone routing).
- Certification claims (AS9100, IATF 16949, ISO 13485) require their own source-backed fact cards before appearing in application content; the overview level does not unlock them.

---

## Common Misreadings

- `industry-application-scenarios-and-boundaries.md` exists → does not mean all 10 segments have execution-boundary coverage.
- A segment appears in the APT industry matrix → does not mean a dedicated wiki boundary page exists for prompt routing.
- `defense-ew-surveillance-targeting-pcb-review-boundaries.md` covers "security" → it does not replace `security-equipment-pcb-pcba-boundary-map.md`; civilian security routing has its own dedicated page.
- `hearing-aid-pcb-review-boundaries.md` exists → it remains a narrow sub-lane and does not replace `medical-device-pcb-pcba-boundary-map.md` for broad medical routing.
- `defense-ew-surveillance-targeting-pcb-review-boundaries.md` covers avionics-adjacent vocabulary → it does not replace `civil-aerospace-pcb-pcba-boundary-map.md` for civil aviation routing.
- `methods-remote-control-and-drone-control-stack-boundary` exists → it does not replace `drone-uav-pcb-pcba-boundary-map.md` for full application routing.

---

## Must Refresh Before Publishing

- When a new dedicated application boundary wiki page is created → add row to primary routing table and update the gap map fact card
- When any draft boundary page is promoted to `active` → update the status column in the routing table
- When a new APT industry segment JSON is indexed → verify routing coverage

---

## Remaining Gaps (For Future Lanes)

| Gap | Reopen Condition |
|-----|-----------------|
| Security-equipment standards depth | Broader public metadata recovered beyond the current conservative official-depth card |
| Drone/UAV regulatory and RF depth | Broader public metadata recovered beyond the current conservative official-depth card |
| Civil aerospace assurance depth | Broader public metadata recovered beyond the current conservative official-depth card |

---

## Related Pages

- `facts/applications/application-coverage-gap-map.md` — machine-readable coverage state
- `wiki/applications/industry-application-scenarios-and-boundaries.md` — 10-segment overview (scenario framing only)
- `wiki/applications/5g-telecom-pcb-execution-boundary-map.md`
- `wiki/applications/compute-infrastructure-pcb-review-boundaries.md`
- `wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md`
- `wiki/applications/sensor-navigation-imaging-pcb-review-boundaries.md`
- `wiki/applications/power-energy-pcb-pcba-review-boundaries.md`
- `wiki/applications/hearing-aid-pcb-review-boundaries.md`
- `wiki/applications/maker-and-smart-home-platform-boundaries.md`
- `wiki/applications/automotive-ev-pcb-pcba-boundary-map.md`
- `wiki/applications/industrial-control-pcb-pcba-boundary-map.md`
- `wiki/applications/medical-device-pcb-pcba-boundary-map.md`
- `wiki/applications/robotics-agv-cobot-pcb-pcba-boundary-map.md`
- `wiki/applications/security-equipment-pcb-pcba-boundary-map.md`
- `wiki/applications/drone-uav-pcb-pcba-boundary-map.md`
- `wiki/applications/civil-aerospace-pcb-pcba-boundary-map.md`
