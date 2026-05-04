---
topic_id: "processes-inspection-governance-navigation-map"
title: "Inspection Governance Navigation Map"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-03"
fact_ids:
  - "processes-inspection-governance-navigation-map"
  - "methods-pcba-inspection-process-governance-boundary"
  - "methods-pcba-screening-qualification-governance-boundary"
  - "methods-pcba-release-traceability-governance-boundary"
  - "methods-hidden-joint-xray-inspection-boundary"
  - "methods-pcba-flying-probe-vs-ict-selection-posture"
  - "methods-low-void-bga-conservative-generation-gate"
  - "methods-pcba-first-article-inspection-vs-high-speed-validation-boundary"
  - "methods-pcba-dfm-dft-dfa-review-gate-positioning"
  - "pcba-electrical-testing-methods-comparison"
source_ids:
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-spi-inspection-page-en"
  - "frontendapt-pcba-aoi-inspection-page-en"
  - "frontendapt-pcba-xray-inspection-page-en"
  - "frontendapt-pcba-ict-test-page-en"
  - "frontendapt-pcba-fct-test-page-en"
  - "frontendapt-pcba-flying-probe-testing-page-en"
  - "frontendapt-pcba-first-article-inspection-page-en"
  - "frontendapt-pcba-incoming-quality-control-page-en"
tags: ["pcba", "inspection", "testing", "governance", "spi", "aoi", "x-ray", "ict", "fct", "flying-probe", "screening", "qualification", "fai", "traceability", "navigation-map"]
---

# Definition

> This page is the single prompt-entry point for all PCBA inspection, testing, screening, qualification, and traceability governance. It does not duplicate fact card content; it routes agents to the correct card for each governance question, defines the safe vocabulary layer, and blocks overclaims at every stage of the inspection and test flow.

## Why This Page Exists

Before this page, PCBA inspection governance was fragmented across six or more individual fact cards. Agents consulting `methods-pcba-inspection-process-governance-boundary` alone would miss the three-layer screening/qualification/FAI separation in `methods-pcba-screening-qualification-governance-boundary`, the IQC evidence chain in `methods-pcba-release-traceability-governance-boundary`, and the flying-probe vs. ICT selection logic in `methods-pcba-flying-probe-vs-ict-selection-posture`. This fragmentation caused:

1. Inspection gates described as universally mandatory (every project, every gate)
2. Screening vocabulary (burn-in, ESS) used as qualification or certification proof
3. Flying probe and ICT conflated without selection posture
4. FAI described as ongoing quality assurance rather than first-build documentation review
5. X-ray void language overclaimed as defect-acceptance thresholds

This navigation page closes all five patterns by providing a unified entry point with cross-routing to each specialist card.

---

## Quick Navigation: Find the Right Card

| Question | Fact Card | Depth |
|---|---|---|
| What is the full gate sequence? What does each gate own? | `methods-pcba-inspection-process-governance-boundary` | Gate table, defect-class ownership |
| When should X-ray be used? What are the package types? | `methods-hidden-joint-xray-inspection-boundary` | X-ray scope, BGA/LGA/QFN context |
| How do ICT and flying probe differ? When to use each? | `methods-pcba-flying-probe-vs-ict-selection-posture` | Selection matrix by project stage and volume |
| How do ICT, flying probe, and boundary-scan compare? | `pcba-electrical-testing-methods-comparison` | Method-comparison table |
| What are screening, qualification, and FAI? How do they differ? | `methods-pcba-screening-qualification-governance-boundary` | Three-layer separation |
| What is IQC → production traceability → final release? | `methods-pcba-release-traceability-governance-boundary` | Evidence chain stages |
| What does FAI cover and what does it NOT prove? | `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary` | FAI scope vs. production audit |
| What DFM/DFT changes improve gate coverage? | `methods-pcba-dfm-dft-dfa-review-gate-positioning` | Test-point design, DFT recommendations |
| What is the BGA void / hidden-joint boundary? | `methods-low-void-bga-conservative-generation-gate` | Void governance, reflow language |
| How does the NPI ramp relate to inspection gates? | `methods-pcba-npi-to-mass-production-gates` + `wiki/processes/pcba-npi-to-mass-production-flow.md` | Gate phase mapping |

---

## Gate Sequence Reference

```
IQC (Incoming)
  ↓
Solder Paste Print
  → SPI (Solder Paste Inspection)
  ↓
Component Placement
  → Pre-reflow AOI
  ↓
Reflow Oven
  → Post-reflow AOI
  → X-ray / AXI  (when BGA/LGA/QFN/hidden-joint packages present)
  ↓
Through-hole / Wave (if mixed technology)
  ↓
ICT (bed-of-nails)   ← requires test-point design; high-volume production
  OR
Flying Probe         ← no fixture; NPI, small volume, no ICT design-in
  ↓
FCT (Functional Test) ← powered; customer-supplied spec
  ↓
Burn-in / ESS        ← screening; high-reliability; program-triggered only
  ↓
FAI Documentation    ← first build only; design verification not ongoing audit
  ↓
Final Inspection + Traceability
  → Certificate of Conformance
  → Lot-to-board serial linkage
  → Packing + shipment release
```

**All gates are per-project-configuration, NOT universally mandatory.**

---

## Gate Safe Vocabulary

### SPI
- Safe: solder paste volume, height, area, offset, bridging, missing paste, 2D/3D measurement, trend monitoring
- Blocked: first-pass yield %, DPPM, throughput rate, universal acceptance threshold

### AOI (Pre- and Post-reflow)
- Safe: component presence/orientation/polarity/type/shift, solder joint geometry, tombstone, bridging, wetting, fillet description
- Blocked: coverage %, false-call rate, skip rate, throughput

### X-ray / AXI
- Safe: hidden joint types (BGA, LGA, QFN, CSP), void description, cold joint, head-in-pillow, 2D/2.5D/3D CT context
- Blocked: void acceptance threshold %, X-ray pass rate, universal void limit, DPPM
- Route to: `methods-hidden-joint-xray-inspection-boundary` and `methods-low-void-bga-conservative-generation-gate` for depth

### ICT (Bed-of-nails)
- Safe: fixture-based testing, net coverage context, opens/shorts/component-value/polarity detection, boundary-scan integration identity
- Blocked: net coverage %, test time per board, fixture cost, universal coverage claim
- Route to: `methods-pcba-flying-probe-vs-ict-selection-posture` for selection logic

### Flying Probe
- Safe: no-fixture electrical test, NPI/small-volume/prototype use context, programmatic coverage, no upfront fixture cost
- Blocked: coverage % vs. ICT, false-call rate, speed comparison numerics
- Route to: `methods-pcba-flying-probe-vs-ict-selection-posture` for selection logic

### FCT (Functional Test)
- Safe: powered behavior, communication protocol test, firmware load, signal integrity under load, customer spec-driven description
- Blocked: pass rate %, test coverage %, universal FCT spec claim

### Burn-in / ESS (Screening)
- Safe: infant-mortality, early-life failure, temperature stress, electrical stress, ESS concept description
- Blocked: burn-in temperature, hours, failure acceleration factor, reliability proof, qualification equivalence

### FAI (First Article Inspection)
- Safe: first-build verification, BOM/drawing match, dimensional check, workmanship review, design-change trigger
- Blocked: ongoing production audit, certification proof, process-qualification equivalence, AS9100/AS9102 compliance
- Route to: `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary`

### IQC / Traceability / Final Release
- Safe: incoming material inspection, lot assignment, production barcode/serial tracking, CoC vocabulary, evidence chain description
- Blocked: supplier qualification proof, regulatory registration, IPC-1782 compliance status, FDA UDI compliance
- Route to: `methods-pcba-release-traceability-governance-boundary`

---

## Three-Layer Governance Separation

**ALWAYS** keep these three layers separate in any written content:

| Layer | Scope | Purpose | Common Overclaim to Avoid |
|-------|-------|---------|--------------------------|
| **Screening (ESS)** | Per production lot | Precipitate infant-mortality failures | "Burn-in qualifies the design" |
| **Qualification** | Per program/design | Prove design meets reliability targets | "Qualification = production clearance" |
| **FAI** | Per first build (or design change) | Verify first units match design documentation | "FAI = ongoing QA audit" |

---

## ICT vs. Flying Probe Selection Summary

| Dimension | ICT (Bed-of-nails) | Flying Probe |
|---|---|---|
| Fixture required | Yes — custom, lead time | No fixture |
| Best project stage | Mass production, stable design | NPI, prototype, low volume |
| Coverage potential | Higher (70–90%+) | Lower; programmatic |
| Setup cost | Higher upfront | Lower upfront, higher per-board |
| DFT requirement | Test-point density needed | Less strict |

Do NOT state exact coverage % or cost numerics without project-specific source.

---

## Must Refresh Before Publishing

- Any yield, DPPM, or throughput rate claims
- Any X-ray void acceptance threshold or solder-joint acceptance criteria
- Any ICT or flying-probe coverage % claims
- Any burn-in temperature, duration, or acceleration factor claims
- Any FAI equated to ongoing production audit or certification proof
- Any IPC-1782, FDA UDI, or AS9102 compliance status claims
- Any claim that a universal gate set applies to every project

---

## Related Pages

- `wiki/processes/pcba-npi-to-mass-production-flow.md` — gate timing in NPI ramp context
- `wiki/processes/low-void-bga-reflow-and-hidden-joint-inspection.md` — X-ray and BGA void depth
- `wiki/processes/selective-solder-fixture-and-access-planning.md` — fixture planning context
- `wiki/processes/hil-assembly-capability-map.md` — HIL assembly type routing
- `facts/processes/process-governance-gap-map.md` — overall process coverage state
- `facts/processes/inspection-governance-navigation-map.md` — companion fact card

## Primary Sources

- /code/hileap/frontendAPT/public/static/pcba/en/spi-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/aoi-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/xray-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/ict-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/fct-test.json
- /code/hileap/frontendAPT/public/static/pcba/en/flying-probe-testing.json
- /code/hileap/frontendAPT/public/static/pcba/en/first-article-inspection.json
- /code/hileap/frontendAPT/public/static/pcba/en/incoming-quality-control.json
- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
