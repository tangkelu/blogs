# Thermal Imaging PCB Evidence Pack

**Pack ID**: `consumption-thermal-imaging-pcb`
**Date**: 2026-05-05
**Status**: `go_now_conservative`
**Template**: `blog-rewrite`

---

## 1. Traceability Core

```yaml
topic: "Thermal imaging PCB rewrite"
scope: |
  Conservative evidence pack for rewriting a thermal imaging PCB article.

  Supports thermal-imaging-board discussion at board-role, detector-interface,
  power/thermal segregation, serial-interface identity, environmental-review,
  and staged validation level.

  Does not support detector sensitivity numerics, NETD, optics authority,
  military qualification proof, medical-diagnostic proof, or supplier-readiness claims.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  - "applications-sensor-navigation-imaging-coverage-gap-map"
  - "methods-eo-ir-detector-owner-identity-and-interface-boundary"
  - "standards-embedded-imaging-serial-interface-boundary"
  - "standards-output-video-and-machine-vision-interface-boundary"
  - "standards-military-environmental-and-emi-qualification-boundary"
  - "methods-pcba-dfm-dft-dfa-review-gate-positioning"
  - "methods-pcba-first-article-inspection-vs-high-speed-validation-boundary"

wiki_support:
  - "wiki/consumption/sensor-navigation-imaging-evidence-pack.md"
  - "wiki/applications/sensor-navigation-imaging-pcb-review-boundaries.md"
  - "wiki/processes/eo-ir-detector-owner-identity-review-boundaries.md"
  - "wiki/processes/sensor-and-display-serial-interface-review-boundaries.md"
  - "wiki/processes/military-environmental-and-emi-standards-boundaries.md"

source_ids:
  - "lynred-about-our-technologies-page"
  - "mipi-csi-2-spec-page"
  - "ti-lvds-overview-page"
  - "mil-std-461-emi-control-standard-page"
  - "mil-std-810-environmental-engineering-tests-page"

must_refresh:
  - claim: "Any exact detector performance number, including NETD, sensitivity, or range"
    value: true
  - claim: "Any exact serial-interface throughput, lane count, or compliance statement"
    value: true
  - claim: "Any MIL-STD pass-status or qualification wording"
    value: true

excluded_claim_classes:
  - "Detector material or microbolometer architecture proof"
  - "Optics, lens, or image-registration authority"
  - "Medical-diagnostic performance or defense deployment proof"
  - "Compliance, qualification, or supplier-readiness proof"
  - "Cost, yield, lead-time, or production-volume promises"
```

---

## 2. Rewrite Posture

| Field | Value |
|---|---|
| **Primary keyword** | `thermal imaging pcb` |
| **Reader intent** | Understand what must be reviewed before releasing a thermal-imaging board |
| **Safe angle** | Board-role and release-boundary review for detector, interface, thermal partition, and validation |
| **Unsafe angle** | Sensor-performance guide, optics guide, or defense/medical qualification page |

**Working posture**: keep the article focused on detector-readout context, interface-family identity, power and thermal segregation, assembly and inspection planning, and staged validation.

---

## 3. Supported Content Shapes

### 3.1 Board Role

- Thermal imaging boards are safe to describe as detector-readout, conditioning, processing, or interface boards.
- A rewrite may distinguish detector zone, processing zone, and output or system-interface zone.
- A rewrite may explain that the PCB is only one layer in a larger optical and system chain.

### 3.2 Detector Identity

- `cooled infrared detector`, `uncooled infrared detector`, and `microbolometer` are safe only as owner-backed detector-family nouns.
- Detector naming must stay attached to board review: power segregation, packaging pressure, interface routing, and validation staging.
- Do not convert detector-family naming into thermal sensitivity or camera-performance proof.

### 3.3 Interface Identity

- `MIPI CSI-2`, `D-PHY`, and `LVDS` are safe as interface-family identity for sensor-side links.
- `HDMI`, `SDI`, `GigE Vision`, and `USB3 Vision` are safe only as output- or machine-vision-interface identity, not as proof of runtime behavior.
- The article may explain that sensor-side and output-side links are different review surfaces and should not be collapsed into one claim.

### 3.4 Environmental And EMI Context

- `MIL-STD-461` and `MIL-STD-810` are safe only as standards-context vocabulary for programs that require EMI and environmental review.
- A rewrite may explain why those standards change review burden and validation planning.
- A rewrite may not claim compliance, pass-status, or supplier qualification.

### 3.5 Validation Ladder

- DFM / DFT / DFA, first-build control, inspection, electrical confirmation, and later system validation are all separate layers.
- The rewrite may emphasize that first-article or fabrication confirmation is not the same as detector-performance proof.
- The rewrite may frame the board as a staged engineering-release problem rather than a finished-camera claim.

---

## 4. Recommended Article Spine

1. What should engineers review first on a thermal imaging PCB?
2. Where does the detector boundary stop and the board boundary begin?
3. Why power, thermal, and interface partitioning should be reviewed together
4. Which package items usually trigger clarification loops before release?
5. How should validation stay layered from intake to system bring-up?
6. What should be frozen before pilot build or low-volume release?

---

## 5. Handoff Summary

> A safe thermal imaging PCB rewrite should read like an engineering release review, not like a sensor-performance brochure. The board can be described through detector-family identity, sensor-side serial-interface vocabulary, power and thermal segregation, compact packaging, environmental-review context, and staged validation. It must not drift into NETD, optics, compliance, or deployment proof.

**Verdict**: ✅ `go_now_conservative`
