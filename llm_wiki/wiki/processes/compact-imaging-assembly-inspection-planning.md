---
wiki_id: "wiki-processes-compact-imaging-assembly-inspection-planning"
title: "Compact imaging assembly inspection planning"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-04"
fact_ids:
  - "methods-hidden-joint-xray-inspection-boundary"
  - "methods-pcba-layered-inspection-stack"
  - "methods-pcba-fai-fqi-and-traceability-gates"
  - "methods-inspection-planning-around-connector-and-shield-obstructions"
  - "methods-pcba-first-article-inspection-vs-high-speed-validation-boundary"
  - "methods-pcba-dfm-dft-dfa-review-gate-positioning"
tags: ["imaging", "compact", "inspection", "x-ray", "fai", "traceability", "processes", "hidden-joint"]
---

# Use This Page For

- Planning inspection for compact or dense assemblies where visible access, hidden-joint visibility, first-build confirmation, and later validation must be separated.
- Routing compact imaging drafts into a layered inspection plan instead of a performance-proof narrative.
- Keeping obstruction-aware inspection choice tied to connectors, shields, and dense-package visibility limits.

# Core Process Rule

- Start with inspection visibility and access, not with release proof.
- A compact assembly may require different methods for different defect classes.
- The safe local claim is that inspection planning is layered: visible inspection, hidden-joint inspection, electrical test, and quality gates each answer different questions.

# Layered Inspection Routing

## Visible Inspection

- Use AOI and visual review for visible geometry, placement, solder, and polarity questions.
- Visible inspection is not hidden-joint coverage.

## Hidden-Joint Inspection

- Use X-ray or AXI language when the draft needs concealed solder joint visibility.
- Hidden-joint inspection is appropriate for dense packages and concealed solder features such as BGA, QFN, and CSP-like contexts.
- Do not turn hidden-joint visibility into universal acceptability or mandatory coverage proof.

## Electrical Verification

- Use ICT and flying probe as separate electrical verification methods with different access models.
- Keep electrical verification distinct from optical or X-ray inspection.

## First-Build And Release Gates

- Use incoming quality, FAI, FQI, traceability, and final inspection as separate quality gates.
- FAI confirms the first build and setup, but it does not replace later validation or release review.
- Final inspection is a release gate, not a product-performance proof.

# Obstruction-Aware Planning

- Route dense or compact assemblies through visibility and obstruction review before choosing a method.
- Connectors, shields, brackets, and other overhangs change what inspection can see.
- The safe choice is method selection around visibility and access, not universal coverage assumptions.

| Draft signal | Safe route | Block if draft asks for |
| --- | --- | --- |
| `compact imaging board inspection` | layered inspection planning | universal X-ray coverage, acceptance thresholds |
| `hidden solder joints` | hidden-joint X-ray boundary | proof that X-ray alone guarantees acceptance |
| `connector overhang` or `shield can obstruction` | obstruction-aware visibility planning | fixed layout rules or coverage percentages |
| `first article inspection` | FAI gate plus traceability review | final validation or release guarantees |
| `FQI` or `final inspection` | end-of-line quality gate | product-performance proof or zero-defect claims |

# Safe Selection Language

- Write `layered inspection planning` instead of implying one inspection method covers all defects.
- Write `hidden-joint visibility` instead of `universal X-ray coverage`.
- Write `FAI, FQI, traceability, and release gates` as distinct steps.
- Write `visibility and access selection` instead of fixed inspection-layout rules.

# Unsafe Selection Language

- Do not claim universal X-ray coverage.
- Do not claim final validation or release is guaranteed by inspection alone.
- Do not claim product-performance proof from inspection planning.
- Do not publish cost, lead-time, or yield claims from this boundary page.
- Do not publish exact inspection coverage, sample-plan, or acceptance-threshold numbers from this layer.

# Blocked Claims

- universal xray-coverage claims
- final validation and release guarantees
- product-performance proof
- cost, lead-time, and yield claims

# Must Refresh Before Publishing

- Any exact coverage rule, inspection percentage, sample plan, or acceptance threshold
- Any product-specific imaging criterion or interface threshold
- Any statement that inspection planning alone proves release readiness
- Any current throughput, quote, supplier-capability, cost, lead-time, or yield claim

# Related Fact Cards

- `methods-hidden-joint-xray-inspection-boundary`
- `methods-pcba-layered-inspection-stack`
- `methods-pcba-fai-fqi-and-traceability-gates`
- `methods-inspection-planning-around-connector-and-shield-obstructions`
- `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary`
- `methods-pcba-dfm-dft-dfa-review-gate-positioning`

# Local Source Records

- `frontendapt-pcba-xray-inspection-page-en`
- `frontendapt-pcba-x-ray-inspection-page-en`
- `frontendapt-pcba-bga-qfn-fine-pitch-page-en`
- `frontendapt-pcba-aoi-inspection-page-en`
- `frontendapt-pcba-quality-system-page-en`
- `frontendapt-pcba-ict-test-page-en`
- `frontendapt-pcba-flying-probe-testing-page-en`
- `frontendapt-pcba-first-article-inspection-page-en`
- `frontendapt-pcba-pcb-selective-soldering-page-en`
- `frontendapt-pcba-testing-quality-page-en`
- `frontendapt-pcba-final-quality-inspection-page-en`
