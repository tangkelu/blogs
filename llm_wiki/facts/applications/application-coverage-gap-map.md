---
fact_id: "applications-application-coverage-gap-map"
title: "Application coverage gap map: which application families have dedicated wiki routing and which remain at overview or claim-family level"
topic: "Application coverage and gap mapping"
category: "applications"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
last_reconciled_at: "2026-05-03"
reconciliation_notes: "P4-156 initial build plus P4-157/P4-158/P4-159/P4-160 follow-on reconciliation and P4-161/P4-162/P4-163 application expansion; P4-168/P4-169 activated 7 newer application pages; P4-170/P4-173 added 4 standards-depth routing companions; P4-174/P4-180 activated the 7 earlier legacy application pages; P4-181/P4-187 landed the 7 missing application fact cards; P4-188/P4-190 landed 3 regulated standards-depth cards; P4-191/P4-202 landed the 12 remaining application evidence packs; shared map reconciled after P4-202"
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
tags: ["applications", "coverage-map", "gap-map", "wiki-routing", "application-families"]
---

# Canonical Summary

> As of 2026-05-03 after P4-202 reconciliation, the application layer has 14 dedicated `active` wiki boundary pages, 14 companion application fact cards, and 14 application evidence packs. The first-pass routing gap, the first-pass application fact-card gap, and the application evidence-pack gap are all closed for the current indexed application set.

## Coverage State By Application Family

### Application Coverage State

| Application Family | Wiki Boundary Page | Companion Fact Card | Evidence Pack | Last Reviewed |
|---|---|---|---|---|
| **5G Telecom** | `wiki/applications/5g-telecom-pcb-execution-boundary-map.md` | `facts/applications/5g-telecom-coverage-gap-map.md` | present | 2026-05-03 |
| **Compute Infrastructure** | `wiki/applications/compute-infrastructure-pcb-review-boundaries.md` | `facts/applications/compute-infrastructure-coverage-gap-map.md` | present | 2026-05-03 |
| **Defense / EW / Surveillance / Targeting** | `wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md` | `facts/applications/defense-ew-coverage-gap-map.md` | present | 2026-05-03 |
| **Sensor / Navigation / Imaging** | `wiki/applications/sensor-navigation-imaging-pcb-review-boundaries.md` | `facts/applications/sensor-navigation-imaging-coverage-gap-map.md` | present | 2026-05-03 |
| **Power / Energy** | `wiki/applications/power-energy-pcb-pcba-review-boundaries.md` | `facts/applications/power-energy-coverage-gap-map.md` | present | 2026-05-03 |
| **Hearing Aid** | `wiki/applications/hearing-aid-pcb-review-boundaries.md` | `facts/applications/hearing-aid-coverage-gap-map.md` | present | 2026-05-03 |
| **Maker / Smart Home** | `wiki/applications/maker-and-smart-home-platform-boundaries.md` | `facts/applications/maker-smart-home-coverage-gap-map.md` | present | 2026-05-03 |
| **Automotive / EV** | `wiki/applications/automotive-ev-pcb-pcba-boundary-map.md` | `facts/applications/automotive-ev-coverage-gap-map.md` | present | 2026-05-03 |
| **Industrial Control** | `wiki/applications/industrial-control-pcb-pcba-boundary-map.md` | `facts/applications/industrial-control-coverage-gap-map.md` | present | 2026-05-03 |
| **Medical Device (broad)** | `wiki/applications/medical-device-pcb-pcba-boundary-map.md` | `facts/applications/medical-application-coverage-gap-map.md` | present | 2026-05-03 |
| **Robotics / AGV / Cobot** | `wiki/applications/robotics-agv-cobot-pcb-pcba-boundary-map.md` | `facts/applications/robotics-coverage-gap-map.md` | present | 2026-05-03 |
| **Security Equipment** | `wiki/applications/security-equipment-pcb-pcba-boundary-map.md` | `facts/applications/security-equipment-coverage-gap-map.md` | present | 2026-05-03 |
| **Drone / UAV** | `wiki/applications/drone-uav-pcb-pcba-boundary-map.md` | `facts/applications/drone-uav-coverage-gap-map.md` | present | 2026-05-03 |
| **Civil Aerospace** | `wiki/applications/civil-aerospace-pcb-pcba-boundary-map.md` | `facts/applications/civil-aerospace-coverage-gap-map.md` | present | 2026-05-03 |

## Stable Facts

- `wiki/applications/` currently contains 24 files: 14 dedicated application boundary pages, 7 application-adjacent standards/routing pages, 1 routing spine, and 2 overview/reference docs.
- `facts/applications/` currently contains 16 files: this gap map, 14 dedicated family cards, and the overview card.
- All 14 current dedicated application boundary pages are now `active`.
- All 14 current dedicated application families now have companion `facts/applications/*` cards.
- The 10 APT industry segments from `frontendapt-industry-*` pages now produce dedicated wiki-level routing for all 10 covered industry lanes when hearing aid is treated as a narrow medical sub-lane and the new broad medical page is treated as the primary medical route.
- The overview pages (`industry-application-scenarios-and-boundaries.md`, `apt-pcb-industry-solutions-guide.md`) cover all 10 segments at scenario/matrix level but do NOT provide execution-boundary routing for any individual segment.
- `apt-pcb-industry-solutions-guide.md` has no YAML frontmatter and is effectively an unstructured reference document, not a wiki card.
- `wiki/consumption/` currently contains dedicated application evidence packs for all 14 current application families.

## Conditions And Methods

- When routing a prompt or blog draft to the application layer, first check this card to determine whether a dedicated boundary page exists.
- If a dedicated page exists, use its dedicated wiki boundary page plus its companion application fact card rather than the overview pages.
- If a dedicated evidence pack exists in `wiki/consumption/`, prefer the evidence pack for downstream prompt execution.
- If no dedicated page exists, use `industry-application-scenarios-and-boundaries.md` for scenario framing, but do not use it to make execution-boundary claims for regulated or specialized markets.
- Update `last_reconciled_at` when a new application wiki page is created.
- Check each page's YAML `status` before publishing. All 14 current dedicated pages are now `active`, but that still means routing-governance only, not capability proof.

## Limits And Non-Claims

- This card does not prove that any application family has complete coverage; even `active` pages still operate as bounded routing/governance layers rather than capability proof.
- It does not validate certifications, qualification, or deployment evidence for any industry segment.
- The first-pass application routing gap, the first-pass application fact-card gap, and the current application evidence-pack gap are now closed; remaining work is deeper regulated official-source supplementation plus non-application normalization.
- "Covered" means a wiki boundary page exists to guide prompt construction—it does not mean the corpus proves capability, certification, or shipped-volume claims for that market.

## Remaining Gaps (Explicit Reopen Conditions)

| Gap | Reopen Condition |
|-----|-----------------|
| Security-equipment official-source depth | When broader public metadata is recovered beyond the current conservative official-depth layer |
| Drone/UAV official-source depth | When broader public metadata is recovered beyond the current conservative official-depth layer |
| Civil-aerospace official-source depth | When broader public metadata is recovered beyond the current conservative official-depth layer |

## Source Links

- wiki/applications/industry-application-scenarios-and-boundaries.md
- wiki/applications/5g-telecom-pcb-execution-boundary-map.md
- wiki/applications/compute-infrastructure-pcb-review-boundaries.md
- wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md
- wiki/applications/sensor-navigation-imaging-pcb-review-boundaries.md
- wiki/applications/power-energy-pcb-pcba-review-boundaries.md
- wiki/applications/hearing-aid-pcb-review-boundaries.md
- wiki/applications/maker-and-smart-home-platform-boundaries.md
- wiki/applications/automotive-ev-pcb-pcba-boundary-map.md
- wiki/applications/industrial-control-pcb-pcba-boundary-map.md
- wiki/applications/medical-device-pcb-pcba-boundary-map.md
- wiki/applications/robotics-agv-cobot-pcb-pcba-boundary-map.md
- wiki/applications/security-equipment-pcb-pcba-boundary-map.md
- wiki/applications/drone-uav-pcb-pcba-boundary-map.md
- wiki/applications/civil-aerospace-pcb-pcba-boundary-map.md
- wiki/applications/security-equipment-standards-and-routing-boundary.md
- wiki/applications/drone-uav-regulatory-routing-boundary.md
- wiki/applications/civil-aerospace-assurance-routing-boundary.md
- facts/applications/apt-pcb-industry-applications-overview.md
