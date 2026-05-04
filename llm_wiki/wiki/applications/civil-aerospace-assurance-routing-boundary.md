---
topic_id: "applications-civil-aerospace-assurance-routing-boundary"
title: "Civil Aerospace Assurance Routing Boundary"
category: "applications"
status: "active"
last_reviewed_at: "2026-05-03"
fact_ids:
  - "standards-civil-aerospace-assurance-boundary"
  - "standards-civil-aerospace-official-assurance-depth"
  - "standards-aviation-altimeter-standards-metadata-boundary"
  - "standards-automotive-medical-aerospace-application-qualification-boundary"
  - "applications-civil-aerospace-coverage-gap-map"
source_ids:
  - "faa-ac-21-16g-do160-acceptability-page"
  - "faa-ac-20-152a-page"
  - "rtca-do-160g-product-page"
  - "rtca-do-254-product-page"
  - "rtca-do-155-product-page"
  - "as9102c-first-article-inspection-page"
notes: "AS9100/OASIS, TSO, ITAR/EAR, and ARINC remain conservative identity-only lanes unless stronger official sources are landed locally."
tags: ["civil-aerospace", "assurance", "routing", "as9100", "do-160g", "do-254", "tso", "arinc", "itar", "ear"]
---

# Routing Summary

> Civil aerospace assurance language is safe only when routed at the correct governance layer. This page is an active assurance router: it keeps QMS, environmental qualification, hardware design assurance, article authorization, protocol identity, and export-control vocabulary in separate lanes, and it stops PCB/PCBA content from collapsing into certification, qualification, or authorization claims.

## Governance Layer Map

| Family | Governance Layer | PCB-Safe Route |
|---|---|---|
| `AS9100D` / `OASIS` / `AS9102C` | organization QMS and FAI documentation | process-discipline and FAI identity context |
| `DO-160G` | airborne-equipment environmental test framework | airborne-equipment application context only |
| `DO-254` | airborne electronic hardware design assurance | CBA design-assurance context only |
| `DO-155` | radar-altimeter equipment performance standard | radar-altimeter application context only |
| `FAA TSO` | device-level authorization | named avionics article context only |
| `ARINC 429 / 664 / 825` | protocol / interface family | avionics-bus identity context only |
| `ITAR / EAR` | export-control law | blocked pending official-source recovery |

## Application Assurance Router

### AS9100 / OASIS / AS9102

- Route `AS9100D` into organization-level QMS vocabulary, not board-level certification.
- Route `AS9102C` into first-article inspection documentation context.
- Route `OASIS` only as the verification surface for certificate validity and scope, not as assumed proof from marketing pages.

**PCB stop line**

- Safe: first-article inspection, traceability, configuration control, non-conformance, QMS discipline.
- Blocked: `AS9100 certified PCB`, live certificate validity, scope inclusion, OASIS-listed manufacturer without local official proof.

### DO-160G

- Route `DO-160G` as the environmental conditions and test-procedures family for airborne equipment.
- Keep section identity and equipment-category framing at context level only.
- Treat qualification and pass/fail as complete-article outcomes, not PCB outcomes.

**PCB stop line**

- Safe: board for airborne equipment subject to DO-160G environmental qualification context.
- Blocked: section pass-status, exact section values, `DO-160G qualified PCB`, `DO-160G compliant PCBA`.

### DO-254

- Route `DO-254` as airborne hardware design-assurance context.
- Use FAA `AC 20-152A` only for source-backed circuit-board-assembly scope context.
- Keep DAL assignment outside PCB manufacturing language.

**PCB stop line**

- Safe: manufactured to customer DO-254 program requirements; CBA assurance context.
- Blocked: DAL-A/B/C/D/E assignment at PCB level, `DO-254 compliant PCBA`, `DO-254 certified manufacturer`.

### DO-155

- Route `DO-155` only for low-range radar-altimeter equipment context.
- Do not generalize it to other altimeter or avionics families.

**PCB stop line**

- Safe: radio-altimeter RF front-end board context.
- Blocked: `DO-155 compliant PCB`, exact performance or immunity claims.

### FAA TSO

- Route TSO numbers as named-device application context only.
- TSO authorization belongs to the complete avionics article, never to the PCB alone.

**PCB stop line**

- Safe: GNSS / TCAS / TAWS board context for a TSO-governed article family.
- Blocked: `TSO-authorized PCB`, `TSO-approved board`, `TSO-compliant PCBA`.

### ARINC

- Route ARINC only as avionics-bus identity and interface context.
- Conformance remains device/system level.

**PCB stop line**

- Safe: ARINC 429 / AFDX / ARINC 825 interface-board context.
- Blocked: ARINC conformance claims at PCB level.

### ITAR / EAR

- Keep this lane blocked.
- No PCB/PCBA export-control compliance, exemption, ECCN, or registration vocabulary is allowed from the current local corpus.

**PCB stop line**

- Safe: none beyond saying the lane is blocked.
- Blocked: all ITAR / EAR / ECCN / export-control claims.

## Safe Routes

| Draft Need | Route To |
|---|---|
| civil aerospace PCB / PCBA execution language | `wiki/applications/civil-aerospace-pcb-pcba-boundary-map.md` |
| assurance standard identity and stop lines | this page |
| narrower assurance depth | `facts/standards/civil-aerospace-assurance-boundary.md` |
| official-source depth framing | `facts/standards/civil-aerospace-official-assurance-depth.md` |
| altimeter-specific standard routing | `wiki/processes/altimeter-aviation-standards-and-assurance-boundaries.md` |
| defense / EW / military routing | `wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md` |

## Blocked Claims

- certification-validity claims
- qualification pass-status
- supplier-proof claims
- cost/lead-time/yield claims

## Non-Claims And Stop Lines

- This page does not prove certificate validity, current OASIS status, or QMS scope.
- This page does not prove qualification or authorization pass-status for any avionics article.
- This page does not prove supplier approval or supplier capability beyond conservative routing context.
- This page does not support cost, lead-time, or yield claims.
- This page does not authorize new ITAR/EAR, TSO, or ARINC assertions beyond the current local facts.

## Related Pages

- `facts/standards/civil-aerospace-assurance-boundary.md`
- `facts/standards/civil-aerospace-official-assurance-depth.md`
- `facts/standards/aviation-altimeter-standards-metadata-boundary.md`
- `wiki/applications/civil-aerospace-pcb-pcba-boundary-map.md`
- `wiki/processes/altimeter-aviation-standards-and-assurance-boundaries.md`
- `wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md`
