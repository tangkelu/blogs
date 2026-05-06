# PCB Price Breakdown Material Process Testing Evidence Pack

**Pack ID**: `consumption-pcb-price-breakdown-material-vs-process-vs-testing`
**Date**: 2026-05-05
**Status**: `go_now_conservative`
**Template**: `blog-rewrite`

---

## 1. Traceability Core

```yaml
topic: "PCB price breakdown rewrite"
scope: |
  Conservative evidence pack for rewriting a PCB price-breakdown article.

  Supports the article at complexity-review and quote-preparation level:
  BOM readiness, stackup family, HDI or special-process escalation, finish
  scope, tooling, validation, and quote-handoff posture.

  Does not support universal price tables, fixed cost percentages, savings
  promises, yield claims, lead-time claims, or supplier-optimization claims.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  - "methods-pcb-cost-driver-review-and-quote-preparation-boundary"
  - "methods-pcba-bom-sourcing-and-traceability-posture"
  - "methods-bom-and-hdi-complexity-boundary"
  - "methods-pcb-stackup-special-process-and-baseline-families"
  - "standards-ipc-surface-finish-taxonomy-osp-hasl-extension"
  - "methods-pcba-fai-fqi-and-traceability-gates"

wiki_support:
  - "wiki/processes/pcb-cost-driver-review-and-quote-preparation.md"
  - "wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md"
  - "wiki/processes/pcb-service-routing-from-prototype-to-special-process.md"

source_ids:
  - "frontendapt-quote-index-en"
  - "frontendapt-pcba-component-sourcing-page-en"
  - "frontendapt-pcba-turnkey-assembly-page-en"
  - "frontendapt-pcb-hdi-pcb-page-en"
  - "frontendapt-pcb-advanced-pcb-manufacturing-page-en"
  - "frontendapt-pcb-pcb-stack-up-page-en"
  - "frontendapt-pcb-multi-layer-laminated-structure-page-en"
  - "apt_pcb_surface_finishes_guide"
  - "apt_pcb_impedance_stackup_design"

must_refresh:
  - claim: "Any universal price table, savings percentage, or uplift percentage"
    value: true
  - claim: "Any current lead-time, MOQ, stock, expedite, or market-price statement"
    value: true
  - claim: "Any yield, scrap, FPY, or supplier-optimization claim"
    value: true

excluded_claim_classes:
  - "Live economics table"
  - "Universal lowest-cost recipe"
  - "Savings or ROI proof"
  - "Supplier ranking"
  - "Cost, lead-time, or yield promises"
```

---

## 2. Rewrite Posture

| Field | Value |
|---|---|
| **Primary keyword** | `pcb price breakdown` |
| **Reader intent** | Understand what actually changes quote complexity |
| **Safe angle** | Quote-preparation and engineering-complexity review |
| **Unsafe angle** | Public pricing table or universal cost-ranking page |

**Working posture**: treat `price breakdown` as a review of BOM readiness, stackup family, HDI/special-process escalation, finish scope, tooling, validation, and quote handoff. Do not publish fake cost formulas.

---

## 3. Supported Content Shapes

### 3.1 BOM and sourcing

- BOM identity, alternates, lifecycle posture, and sourcing clarity are safe as quote inputs.
- The rewrite may explain that sourcing ambiguity often creates quote churn before fabrication starts.

### 3.2 Stackup and process family

- Baseline multilayer, hybrid, heavy-copper, and HDI routes are safe as distinct complexity families.
- The rewrite may explain that stackup and lamination route change the build path early.

### 3.3 Finish scope

- ENIG, ENEPIG, OSP, immersion silver, immersion tin, HASL, and hard gold are safe as finish-family identity.
- The rewrite may explain that finish choice should be tied to duty zone or application need, not universal cheapness.

### 3.4 Tooling and validation

- Coupons, fixtures, controlled structures, and test intent are safe as quote inputs.
- The rewrite may explain that validation scope belongs in the package before RFQ.

### 3.5 Quote handoff

- The article may end at DFM and quote review, not at a savings promise.
- It is safe to ask for Gerbers, BOM, stackup, finish notes, and validation expectations as part of a quote-ready package.

---

## 4. Recommended Article Spine

1. What does price breakdown mean in engineering terms?
2. Which inputs usually change the quote first?
3. Why stackup and board family matter early
4. When HDI and build-up change the route
5. How finish, tooling, and validation affect the package
6. What should be frozen before RFQ?

---

## 5. Handoff Summary

> A safe PCB price-breakdown rewrite should stop behaving like a price table and start behaving like a quote-preparation guide. It should explain which design and package choices increase complexity, how to freeze inputs before RFQ, and why finish, tooling, and validation scope matter. It must not drift into universal savings claims or live economics.

**Verdict**: ✅ `go_now_conservative`
