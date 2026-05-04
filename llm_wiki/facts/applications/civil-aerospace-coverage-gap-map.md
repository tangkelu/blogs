---
fact_id: "applications-civil-aerospace-coverage-gap-map"
title: "Civil aerospace application coverage gap map: which board families have wiki-layer routing and which remain blocked"
topic: "Civil aerospace PCB/PCBA application coverage"
category: "applications"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
last_reconciled_at: "2026-05-03"
reconciliation_notes: "P4-163 initial build; sourced from frontendapt-industry-aerospace-defense-page-en (Tier-2), aviation-altimeter-standards-metadata-boundary, automotive-medical-aerospace-application-qualification-boundary, and defense-ew-surveillance-targeting-pcb-review-boundaries. Civil aerospace content is now separated from defense/EW/military context, with the shared Tier-2 aerospace-defense source used at civil-context vocabulary level only."
source_ids:
  - "frontendapt-industry-aerospace-defense-page-en"
  - "faa-ac-20-152a-page"
  - "faa-ac-21-16g-do160-acceptability-page"
  - "rtca-do-160g-product-page"
  - "rtca-do-254-product-page"
  - "as9102c-first-article-inspection-page"
tags: ["civil-aerospace", "avionics", "flight-control", "do-160g", "do-254", "faa", "as9100", "coverage-map", "gap-map"]
---

# Canonical Summary

> As of 2026-05-03, civil aerospace has a dedicated wiki boundary page (`wiki/applications/civil-aerospace-pcb-pcba-boundary-map.md`) created by P4-163. Prior to this lane, civil aerospace content was partially covered under `defense-ew-surveillance-targeting-pcb-review-boundaries.md`. The shared Tier-2 aerospace-defense source supports 5 board families. It does NOT prove AS9100 certification, DO-160G environmental qualification, DO-254 design-assurance level (DAL), airworthiness, TSO authorization, ITAR compliance, or export-control status.

## Critical Governance Note on the Tier-2 Source

The aerospace-defense JSON SEO metadata contains `"AS9100 compliance"` and `"mission assurance"` in the page title and description. These are marketing claims, NOT:
- Proof that the PCB supplier holds a current AS9100 certificate
- Proof that any specific program, product, or build is AS9100-conforming
- Proof of OASIS registration status

Treat the Tier-2 source as application-scenario framing only. All AS9100, qualification, certification, and mission-assurance vocabulary must be refreshed before publication.

## Board Family Coverage State

### Supported at Scenario + Board-Class Level (Tier-2 Internal Source)

| Board Family | Application Context | PCB/PCBA Vocabulary Supported |
|---|---|---|
| **Avionics / Flight Control / Navigation** | Flight computers, avionics I/O boards, cockpit display PCBs, sensor interface boards, data concentrators | Multilayer processor/FPGA/memory/mixed-signal board, redundant channel + voting logic layout description (customer-design basis), air-data/IMU/GNSS/altimeter sensor interface vocabulary, cockpit display/HMI PCB |
| **Communication / RF / Data Links** | Airborne radios, satcom boards, data link PCBAs | RF/microwave layer and matching network board description, high-speed ADC/DAC/FPGA/DSP signal processing board vocabulary, thermal/conduction-cooled layout vocabulary |
| **Power / Actuation** | Power supplies, DC-DC converters, motor/actuator drivers, PDUs | High-voltage/high-current creepage/clearance description, MOSFET/IGBT/gate driver/current-sense layout, EMC-aware power layout, redundancy and monitoring vocabulary |
| **Ground Systems / Test Equipment** | Rugged computers, command-console PCBs, test racks, simulators | Rugged compute board, control console/HMI PCB, test/interface PCBA, long-lifecycle materials and process description |
| **Ruggedization / Materials / Stackup** | All aerospace board types in harsh environments | High-Tg material vocabulary (customer-specified), controlled impedance and high-speed layer, via/PTH integrity, conformal coating vocabulary |

### Aviation Standards Coverage Already Landed (Standards Fact Card Layer)

| Standard | Fact Card | Coverage Level |
|---|---|---|
| `DO-160G` | `standards-aviation-altimeter-standards-metadata-boundary` | Document-family identity only — NOT qualification pass-status |
| `DO-254` | `standards-aviation-altimeter-standards-metadata-boundary` | Design-assurance guidance identity + circuit-board-assembly scope only |
| `DO-155` | `standards-aviation-altimeter-standards-metadata-boundary` | Low-range radar altimeter MPS identity only |
| `FAA AC 20-152A` | `standards-automotive-medical-aerospace-application-qualification-boundary` | Airborne electronic hardware / circuit-board-assembly assurance context only |
| `FAA AC 21-16G` | `standards-aviation-altimeter-standards-metadata-boundary` | DO-160 versions D–G recognition for certain airworthiness requirements |
| `AS9102 FAI` | `standards-automotive-medical-aerospace-application-qualification-boundary` | First-article inspection identity and documentation context only |
| `AS9100` | **NOT in sources registry at certification level** | Identity-only; current certificate status and OASIS listing are refresh-required |

### Process / Test Coverage Already Applicable

- SPI → AOI → X-ray (BGA/LGA/QFN on avionics and radar boards) → ICT/flying-probe → FCT → burn-in/environmental screening preparation (description level) → final inspection + traceability

## Stable Facts

- The Tier-2 source covers civil and defense aerospace together; this card and its corresponding wiki page focus on civil aerospace (commercial aviation, civil avionics, non-defense electronics).
- `"AS9100 Certified – Mission Assurance"` is a trust-bar label in the Tier-2 source; it does NOT prove current AS9100 certificate or OASIS registration.
- DO-160G, DO-254, and AS9100 are supported at standards-identity level only; qualification pass-status, DAL assignment, and certification are blocked.
- FAA `AC 20-152A` supports circuit-board-assembly design-assurance context only — NOT airworthiness approval, TSO authorization, or installation approval.
- AS9102 supports first-article-inspection documentation context only — NOT process-capability proof or AS9100 audit readiness.
- ITAR, EAR, and export-control compliance are completely outside the scope of any current source in the registry.

## Conditions And Methods

- Use this card for civil commercial aviation content (commercial aircraft avionics, civil navigation, civil communication, civil ground systems).
- For defense/military aviation contexts (EW, radar, ISR, MIL-STD), route to `wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md`.
- For altimeter-specific slug content, also use `wiki/processes/altimeter-aviation-standards-and-assurance-boundaries.md`.

## Limits And Non-Claims

- AS9100 certificate, OASIS registration, or QMS audit status NOT supported.
- DO-160G section-level test, test condition, or pass-status NOT supported.
- DO-254 DAL assignment, design-assurance level, or compliance proof NOT supported.
- Airworthiness, TSO, STC, FAA approval, or installation authorization NOT supported.
- ITAR, EAR, export-control, or classified-program compliance NOT supported.
- Mission reliability, MTBF, field-deployment statistics, or customer-program history NOT supported.
- Yield, throughput, cost, or lead-time claims NOT supported.

## Remaining Gaps

| Gap | Reopen Condition |
|-----|-----------------|
| AS9100 certification status vocabulary depth | Official AS9100 certificate record or OASIS listing recovery |
| DO-160G section-level test vocabulary | Full DO-160G standard access or clause-level FAA AC source |
| DO-254 DAL/design-assurance vocabulary | Full DO-254 standard access or clause-level source |
| ITAR / EAR export-control boundary | Official ITAR/EAR source (currently completely outside corpus) |
| TSO authorization vocabulary | Official FAA TSO source recovery |
| Dedicated civil-aerospace wiki page status | Reopen only if the page later regresses and requires demotion from `active` |
