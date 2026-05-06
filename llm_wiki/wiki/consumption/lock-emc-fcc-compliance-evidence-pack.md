---
title: "Lock EMC FCC Compliance Evidence Pack"
category: "consumption"
status: "active"
last_reviewed_at: "2026-05-05"
tags: ["smart-lock", "emc", "fcc", "rf-module", "esd", "return-path", "review-boundary"]
---

# Lock EMC FCC Compliance Evidence Pack

**Pack ID**: `consumption-lock-emc-fcc-compliance`
**Date**: 2026-05-05
**Status**: `go_now_conservative`
**Template**: `query`

---

## 1. Traceability Core

```yaml
topic: "Lock EMC FCC compliance PCB"
scope: |
  Conservative evidence pack for smart-lock and access-control board content
  written at pre-compliance and board-review boundary.

  Supports actuator-noise partitioning, return-path continuity, user-touch and
  cable-entry ESD review, antenna/enclosure coexistence, RF-module integration
  boundary, and staged validation or release-package language.

  Does not support FCC pass-status claims, UL 294 / EN 60839 compliance proof,
  exact EMC or ESD thresholds, first-pass certification promises, or wireless
  range and ecosystem-compatibility guarantees.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/aptpcb/query-overlay.md"

fact_ids:
  - "applications-security-equipment-coverage-gap-map"
  - "methods-ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity"
  - "methods-shield-aware-test-access-and-service-access"
  - "methods-inspection-planning-around-connector-and-shield-obstructions"
  - "methods-pcba-validation-handoff-package"

source_ids:
  - "fcc-equipment-authorization-page"
  - "ecfr-47-cfr-15-212-modular-transmitters-page"
  - "ti-high-speed-layout-guidelines"
  - "silabs-an1088-designing-with-pcb-antenna"
  - "frontendapt-antenna-pcb-page-en"
  - "frontendapt-industry-security-equipment-page-en"
  - "frontendapt-pcba-testing-quality-page-en"

wiki_framing_support:
  - "wiki/consumption/security-equipment-evidence-pack"
  - "wiki/consumption/maker-smart-home-evidence-pack"
  - "wiki/consumption/industrial-control-evidence-pack"
  - "wiki/applications/security-equipment-pcb-pcba-boundary-map"
  - "wiki/applications/security-equipment-standards-and-routing-boundary"
  - "wiki/processes/cavity-and-shield-feature-planning"

must_refresh:
  - claim: "FCC process-page or modular-transmitter requirement updates"
    value: true
  - claim: "Antenna-module keep-out or enclosure guidance tied to a named module"
    value: true
  - claim: "Any exact EMC, ESD, RF, or wireless-range numeric threshold"
    value: true

excluded_claim_classes:
  - "FCC pass, first-pass, or authorized-product proof"
  - "UL 294 / EN 60839 / CE / RED compliance proof"
  - "exact EMC, ESD, or antenna-clearance numeric rules"
  - "wireless-range, RF-output, or coexistence performance guarantees"
  - "ecosystem compatibility or smart-home certification claims"
  - "cost, lead-time, yield, or field-failure claims"
```

---

## 2. Topic Summary

| Field | Value |
|-------|-------|
| **Primary Keywords** | `lock emc fcc compliance pcb`, `smart lock pcb emc`, `smart lock fcc review` |
| **Page Type** | `query` |
| **Search Intent** | Smart-lock board review, EMC preparation, FCC preparation, RF-module integration, access-control hardware |
| **Target Reader** | Smart-lock hardware engineers, access-control designers, NPI and layout teams |
| **Site** | `APTPCB` |

**Working Posture**: `go_now_conservative` at board-review and pre-compliance boundary only.

---

## 3. Safe Article Frame

| Section Type | Safe Treatment |
|--------------|----------------|
| Definition | Treat the topic as a smart-lock board review before EMC and FCC testing, not as certification proof |
| EMC priorities | Separate actuator or relay noise, preserve return paths, control external-entry ESD routes, and keep antenna regions stable |
| RF module boundary | A pre-approved module can reduce radio burden, but host integration still needs review for labeling, antenna use, and final configuration |
| Validation | Separate pre-compliance scans, board debug, and system or lab authorization outcomes |
| Standards | `FCC Part 15` and `UL 294 / EN 60839` only as standards-context vocabulary, not as board-level status |

---

## 4. Covered vs Blocked

### 4.1 Covered

| Area | Coverage |
|------|----------|
| Actuator-noise vs control/RF partitioning | ✅ Supported |
| Return-path continuity and plane discipline | ✅ Supported |
| User-touch and cable-entry ESD review wording | ✅ Supported at non-numeric level |
| Antenna-region and enclosure interaction wording | ✅ Supported |
| Modular-transmitter integration boundary | ✅ Supported |
| Staged validation and release-package language | ✅ Supported |

### 4.2 Blocked

| Blocked Claim | Reason |
|---------------|--------|
| "Pass FCC on the first run" | No reusable authority for outcome promises |
| "UL 294 compliant smart-lock PCB" | Standard applies to system or unit context, not bare PCB proof |
| "Use spacing X around every antenna" | Module and antenna guidance is design-specific |
| "This layout guarantees wireless range" | Range depends on full radio, enclosure, and system conditions |

---

## 5. Core Answer

> A smart-lock PCB can be written safely as a pre-compliance review problem: partition the noisy actuator path away from logic and RF regions, preserve return-path continuity, review every user-touch or cable entry as a possible ESD route, keep the antenna region stable against nearby metal and enclosure changes, and separate module authorization context from the final host-device test path.

---

## 6. Writing Notes

- Prefer `before EMC and FCC testing` over `FCC compliant` or `FCC certified`.
- Use `smart lock` or `access-control board` framing, then keep `UL 294` and `EN 60839` at standards-identity level only.
- If the article mentions a radio module, state that module authorization changes the integration path but does not remove host-device review duties.
- If the article needs antenna language, say `follow the module or antenna vendor's layout guidance` instead of inventing a universal keep-out number.
- Use EQ-style examples when the release burden comes from enclosure, wiring, antenna location, or unresolved interface ownership.

---

## 7. Pre-flight

- [x] Local security-equipment boundary page identified
- [x] Local smart-home and industrial-control packs checked for overlap
- [x] FCC authorization entry source identified
- [x] FCC modular-transmitter regulation source added
- [x] Official antenna-layout source added
- [x] Blocked claim classes documented

**Verdict**: ✅ `go_now_conservative` for smart-lock EMC/FCC-preparation content.
