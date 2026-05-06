# Extended Reality PCB Evidence Pack

**Pack ID**: `consumption-extended-reality-pcb`
**Date**: 2026-05-05
**Status**: `go_now_conservative`
**Template**: `blog-rewrite`

---

## 1. Traceability Core

```yaml
topic: "Extended reality PCB rewrite"
scope: |
  Conservative evidence pack for rewriting an extended-reality PCB article.

  Supports XR only as a wearable compact-hardware context, then routes the
  article into board-role definition, compact-access planning, display and
  sensor interface-family identity, rigid-flex handling context, inspection
  planning, and validation handoff.

  Does not support claims that HDI is mandatory, that rigid-flex is standard,
  exact layer-count norms, thermal-safety thresholds, wireless performance,
  or consumer-device feature proof.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  - "methods-wearable-compact-access-and-closure-boundary"
  - "methods-rigid-flex-stackup-and-bend-reliability-posture"
  - "standards-embedded-imaging-serial-interface-boundary"
  - "methods-inspection-planning-around-connector-and-shield-obstructions"
  - "methods-conformal-coating-masking-test-access-and-protection-workflow"
  - "methods-pcba-validation-handoff-package"

wiki_support:
  - "wiki/processes/wearable-compact-access-and-closure-boundaries.md"
  - "wiki/processes/rigid-flex-handling-lane.md"
  - "wiki/processes/sensor-and-display-serial-interface-review-boundaries.md"
  - "wiki/processes/compact-imaging-assembly-inspection-planning.md"

source_ids:
  - "frontendapt-pcb-rigid-flex-pcb-page-en"
  - "frontendapt-pcba-flex-rigid-flex-page-en"
  - "frontendapt-pcba-first-article-inspection-page-en"
  - "mipi-csi-2-spec-page"
  - "mipi-dsi-2-spec-page"
  - "ti-lvds-overview-page"

must_refresh:
  - claim: "Any exact layer count, HDI geometry, bend ratio, or wearable thermal limit"
    value: true
  - claim: "Any exact interface throughput, lane count, or display/video performance number"
    value: true
  - claim: "Any battery-life, wireless, latency, or user-comfort performance claim"
    value: true

excluded_claim_classes:
  - "XR feature or product-performance proof"
  - "Mandatory HDI or rigid-flex doctrine"
  - "Wearable safety or skin-temperature thresholds"
  - "5G, RF, wireless, or sensor-fusion performance claims"
  - "Cost, lead-time, and yield promises"
```

---

## 2. Rewrite Posture

| Field | Value |
|---|---|
| **Primary keyword** | `extended reality pcb` |
| **Safe reader intent** | Understand how to review a compact wearable XR board before release |
| **Safe angle** | Access-planned wearable compute board with display, sensor, and closure constraints |
| **Unsafe angle** | XR feature guide, thermal-safety guide, or HDI-specification list |

**Working posture**: treat XR as application context only, then move immediately into board-role, compact-access, interface planning, rigid-flex-as-conditional-route, and layered validation.

---

## 3. Supported Content Shapes

### 3.1 Board Role And Compactness

- XR is safe only as a compact wearable hardware context.
- The rewrite may talk about compute board, display-side interconnect, sensor-side interconnect, and closure pressure.
- The rewrite should explain why access and serviceability shrink before validation is finished.

### 3.2 Display And Sensor Interfaces

- `MIPI DSI-2` is safe as display-side interface-family identity.
- `MIPI CSI-2`, `D-PHY`, and `LVDS` are safe as sensor-side or imaging-side interface-family identity.
- Interface names must remain identity-level only and not drift into bitrate, compliance, or latency proof.

### 3.3 Rigid-Flex And Bend Context

- Rigid-flex is safe as one possible compact-routing strategy when enclosure pressure is high.
- The rewrite may explain bend-zone review, carrier support, stiffeners, and transition handling.
- The rewrite must not imply that every XR board requires rigid-flex or that bend guidance proves reliability.

### 3.4 Access, Closure, And Protection

- Compact boards are safe to describe as access-planned builds.
- The rewrite may discuss inspection reach, programming reach, connector mating, shielding, coating keep-access, and closure timing.
- The rewrite should keep closure and protection separate from readiness proof.

### 3.5 Validation Handoff

- The article may explain layered inspection, first-build control, electrical confirmation, and later system validation handoff.
- It may emphasize that compact wearable closure can remove access before validation is complete.
- It may not turn inspection or handoff into performance proof.

---

## 4. Recommended Article Spine

1. What should engineers review first on a wearable XR board?
2. Why XR should be translated into board role instead of feature promises
3. How display, sensor, and support interfaces should stay separated
4. When rigid-flex helps and when it simply adds release burden
5. Which closure and access items usually trigger EQ holds?
6. How should inspection and validation stay layered before final closure?

---

## 5. Handoff Summary

> A safe extended-reality PCB rewrite should stop being an XR marketing article almost immediately. The durable rewrite angle is a compact wearable board review: board role, display and sensor interface-family identity, optional rigid-flex routing, access-before-closure planning, and layered validation. The current evidence does not support default HDI rules, thermal limits, feature performance, or wireless promises.

**Verdict**: ✅ `go_now_conservative`
