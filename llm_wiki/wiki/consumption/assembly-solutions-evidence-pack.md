# Assembly Solutions Evidence Pack

**Pack ID**: `consumption-assembly-solutions`
**Date**: 2026-05-05
**Status**: `go_now_conservative`
**Template**: `blog-rewrite`

---

## 1. Traceability Core

```yaml
topic: "Assembly solutions rewrite"
scope: |
  Conservative evidence pack for rewriting a broad assembly-solutions article
  into a PCB assembly package-review article.

  Supports assembly-readiness discussion at package-completeness, BOM and
  placement consistency, mixed-technology flow, layered inspection, electrical
  test selection, release traceability, and validation-handoff level.

  Does not support universal process windows, fixture payback math, yield
  promises, coverage percentages, lead-time promises, or product-compliance
  proof.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  - "methods-pcba-dfm-dft-dfa-review-gate-positioning"
  - "methods-pcba-layered-inspection-stack"
  - "methods-pcba-flying-probe-vs-ict-selection-posture"
  - "methods-pcba-validation-handoff-package"
  - "methods-pcba-bom-sourcing-and-traceability-posture"
  - "methods-pcba-fai-fqi-and-traceability-gates"
  - "methods-pcba-test-method-input-package-boundary"
  - "methods-pcba-inspection-process-governance-boundary"
  - "methods-pcba-release-traceability-governance-boundary"
  - "methods-pcba-mixed-technology-assembly-flow"
  - "methods-pcba-stencil-selective-solder-and-fine-pitch-controls"
  - "methods-pcba-box-build-system-integration-posture"

wiki_support:
  - "wiki/processes/pcba-npi-to-mass-production-flow.md"
  - "wiki/processes/validation-handoff-npi-governance.md"
  - "wiki/processes/inspection-governance-navigation-map.md"
  - "wiki/processes/pcb-design-data-exchange-and-tool-boundaries.md"

source_ids:
  - "frontendapt-pcba-turnkey-assembly-page-en"
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-first-article-inspection-page-en"
  - "frontendapt-pcba-final-quality-inspection-page-en"
  - "frontendapt-pcba-flying-probe-testing-page-en"
  - "siemens-odb-plus-plus-page"
  - "as9102c-first-article-inspection-page"

must_refresh:
  - claim: "Any exact stencil, reflow, voiding, or inspection-threshold number"
    value: true
  - claim: "Any ICT or flying-probe coverage percentage, cost, or cycle-time number"
    value: true
  - claim: "Any universal lead-time, yield, or zero-defect promise"
    value: true

excluded_claim_classes:
  - "Universal SMT/THT capability table"
  - "Guaranteed quote or shipment timing"
  - "Fixture ROI, coverage, or payback math"
  - "Compliance, certification, or customer-release authority proof"
  - "Every-project-uses-every-gate claims"
```

---

## 2. Rewrite Posture

| Field | Value |
|---|---|
| **Primary keyword** | `pcb assembly solutions` |
| **Reader intent** | Understand what should be reviewed before releasing a board into assembly |
| **Safe angle** | Assembly package completeness, inspection layering, test selection, and validation handoff |
| **Unsafe angle** | Generic turnkey service brochure or universal process-parameter guide |

**Working posture**: rewrite the page as an engineering release-review article, not a broad service summary. Keep the center of gravity on what the package must expose before pilot build or turnkey intake can stay clean.

---

## 3. Supported Content Shapes

### 3.1 Package Completeness

- A rewrite may explain that fabrication files alone do not finish the assembly review package.
- It is safe to require BOM identity, placement data, revision clarity, and explicit test intent.
- ODB++, IPC-2581 / IPC-DPMX, and Gerber may be named as handoff-format context, but not as universal completeness proof.

### 3.2 Layered Inspection

- SPI, AOI, X-ray, ICT, FCT, FAI, and final inspection are safe only as distinct gates with different ownership.
- The article may explain defect-class separation and evidence accumulation.
- The article may not imply every program receives every gate.

### 3.3 Electrical-Test Selection

- Flying probe is safe as the fixture-free posture for design-changing or lower-volume work.
- ICT is safe as the fixture-based posture for more stable production programs.
- The article may not publish universal coverage or throughput comparisons.

### 3.4 Mixed-Technology Flow

- SMT, THT, selective solder, fine-pitch handling, and hidden-joint inspection are safe as one coordinated process chain.
- It is safe to explain that assembly planning changes when the board mixes dense SMT and through-hole content.
- Avoid numeric process tables unless separately refreshed.

### 3.5 Validation Handoff

- Revision identity, traceability, inspection records, test notes, and unresolved issues are safe as handoff artifacts.
- First-article and final inspection are safe as release gates, not as system-proof language.
- Box build may be presented as a later branch when the program widens into harness, firmware, or system integration.

---

## 4. Recommended Article Spine

1. What should engineers review first before assembly release?
2. Which package items usually create the first hold?
3. How should inspection stay layered instead of generic?
4. When does flying probe fit better than ICT?
5. What changes when SMT, THT, and selective solder coexist?
6. What should travel into validation handoff?

---

## 5. Handoff Summary

> A safe assembly-solutions rewrite should behave like a release-readiness article. It should explain how a board enters assembly with a complete package, how inspection and electrical test stay layered, how mixed-technology flow changes planning, and how revision plus traceability evidence moves into later validation. It must not drift into universal process numbers, blanket service promises, or certification-style claims.

**Verdict**: ✅ `go_now_conservative`
