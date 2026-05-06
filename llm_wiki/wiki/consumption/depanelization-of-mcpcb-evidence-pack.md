# Depanelization of MCPCB Evidence Pack

**Pack ID**: `consumption-depanelization-of-mcpcb`
**Date**: 2026-05-05
**Status**: `go_now_conservative`
**Template**: `blog-rewrite`

---

## 1. Traceability Core

```yaml
topic: "Depanelization of MCPCB rewrite"
scope: |
  Conservative evidence pack for rewriting a depanelization-of-MCPCB article.

  Supports the article at MCPCB / IMS singulation-method selection, edge-risk
  review, component-to-edge stress sensitivity, profile-shape branch choice,
  cleanliness follow-up, and NPI validation posture level.

  Does not support universal strain limits, burr-height tables, blade settings,
  die-clearance numbers, throughput claims, cost claims, or one-method-fits-all
  guidance.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  - "processes-apt-metal-core-capability-specs"
  - "methods-mcpcb-ims-and-reflow-source-coverage"
  - "methods-pcb-stackup-special-process-and-baseline-families"
  - "methods-mcpcb-depanelization-method-selection-boundary"
  - "methods-depanelization-cleanliness-and-edge-risk-boundary"

wiki_support:
  - "wiki/processes/pcb-service-routing-from-prototype-to-special-process.md"
  - "wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md"
  - "wiki/consumption/power-energy-evidence-pack.md"

source_ids:
  - "frontendapt-pcb-pcb-profiling-page-en"
  - "frontendapt-metal-pcb-capability-en"
  - "lpkf-insulated-metal-substrates-page"
  - "lpkf-technical-cleanliness-page"

must_refresh:
  - claim: "Any exact strain, burr-height, blade-gap, web-thickness, or cut-speed number"
    value: true
  - claim: "Any statement that one singulation method is universally best for all MCPCB panels"
    value: true
  - claim: "Any exact cleanliness threshold or isolation test criterion"
    value: true

excluded_claim_classes:
  - "Universal depanelization settings table"
  - "Guaranteed crack-free or burr-free outcome"
  - "Machine-vendor throughput or cost comparison"
  - "Electrical-safety proof from edge appearance alone"
  - "Lead-time, yield, or production-volume promises"
```

---

## 2. Rewrite Posture

| Field | Value |
|---|---|
| **Primary keyword** | `depanelization of mcpcb` |
| **Reader intent** | Understand how to review MCPCB singulation before release |
| **Safe angle** | Method-selection and edge-risk review for metal-core panel separation |
| **Unsafe angle** | Universal tooling-parameter guide or generic FR-4 snap-apart tutorial |

**Working posture**: treat depanelization as a release-review problem. Explain how MCPCB / IMS singulation changes when geometry, edge cleanliness, mechanical load, and downstream mounting or isolation risk matter.

---

## 3. Supported Content Shapes

### 3.1 Method Selection

- It is safe to separate straight-line scoring, routed profiles, and low-mechanical-stress singulation into different method branches.
- The rewrite may explain that metal-substrate panels deserve a more deliberate singulation choice than routine FR-4 breakaway language suggests.

### 3.2 Edge Risk

- The article may explain why conductive fragments, rough edges, and exposed edge conditions deserve explicit inspection.
- It is safe to connect edge condition to later mounting, cleanliness, and isolation review without inventing thresholds.

### 3.3 Component Sensitivity

- It is safe to explain that edge-adjacent LEDs, MLCCs, connectors, or solder joints raise the review burden.
- Avoid universal setback numbers unless separately source-backed.

### 3.4 NPI Validation

- The rewrite may recommend sample cuts, first-build review, and method confirmation before broad release.
- It may emphasize that depanelization settings and fixtures should be validated on the real panel design rather than copied from a generic rule set.

### 3.5 MCPCB Context

- MCPCB / IMS can be discussed as a thermal-platform context that changes the singulation review burden.
- Avoid converting that context into thermal-performance or safety proof.

---

## 4. Recommended Article Spine

1. What changes when MCPCB panels are separated?
2. How should singulation method be chosen?
3. Why edge cleanliness and debris control matter more on metal-substrate boards
4. Which layout and assembly conditions usually trigger a process hold?
5. What should be confirmed in NPI before release?
6. How should the final release package describe the cut route?

---

## 5. Handoff Summary

> A safe depanelization-of-MCPCB rewrite should read like an engineering singulation review. It should explain method selection, edge-risk review, cleanliness follow-up, component sensitivity near the cut line, and first-build validation. It must not drift into fake process numerics, snap-apart simplifications, or universal machine settings.

**Verdict**: ✅ `go_now_conservative`
