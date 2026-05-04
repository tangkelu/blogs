---
fact_id: "methods-pcba-screening-qualification-governance-boundary"
title: "PCBA screening and qualification governance should separate environmental stress screening, reliability qualification, and first-article verification into distinct program-level activities"
topic: "PCBA screening and qualification governance boundary"
category: "methods"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
source_ids:
  - "frontendapt-pcba-quality-system-page-en"
  - "frontendapt-pcba-first-article-inspection-page-en"
  - "as9102c-first-article-inspection-page"
  - "ipc-6012-addendum-taxonomy-page"
  - "ipc-6012fs-space-military-addendum-page"
tags: ["pcba", "screening", "qualification", "fai", "burn-in", "stress-test", "reliability", "governance", "as9102", "ipc-6012"]
---

# Canonical Summary

> PCBA screening and qualification governance requires clear separation between environmental stress screening (ESS), reliability qualification testing, and first-article inspection (FAI). Screening is a production-level stress activity to precipitate early failures; qualification is a program-level activity to prove design and process capability; FAI is a first-build verification against design documentation. These layers operate at different scopes and should not be conflated.

## Stable Facts

### Three Governance Layers

| Layer | Scope | Purpose | Timing |
|-------|-------|---------|--------|
| **Screening (ESS)** | Production lot | Precipitate latent defects, early-life failures | 100% or sample of production units |
| **Qualification** | Program/design | Prove design and process meet reliability requirements | Development/validation phase, design changes |
| **FAI** | First build | Verify first production units match design documentation | First production run, design changes |

### Screening (ESS) - Production Level

- **Burn-in**: Temperature and/or electrical stress to accelerate early-life failure mechanisms
- **Thermal Cycling**: Temperature shock/cycle to expose interconnect stress, solder joint fatigue
- **Environmental Stress**: Combined temperature, humidity, vibration as applicable
- **Purpose**: Remove infant-mortality failures before customer shipment
- **Scope**: Typically 100% for high-reliability; sampling for commercial

### Qualification - Program Level

- **Qualification Testing**: Formal test program to prove design meets reliability specifications
- **Test Vehicles**: Dedicated qualification vehicles or representative production samples
- **Standards Reference**: IPC-6012 addenda (EM/FA/FS), AS9102, customer-specific requirements
- **Purpose**: Provide evidence that design and qualified process can meet life/reliability targets
- **Scope**: Program-level, design-specific, process-change triggered

### First Article Inspection (FAI) - Build Level

- **AS9102C**: Aerospace standard for FAI requirements (formal FAIR documentation)
- **APTPCB Internal FAI**: Built-in FAI for new/changed projects, FAIR report generation
- **Purpose**: Verify first production units match all design documentation before volume release
- **Scope**: First build of new designs, after significant design changes

### Governance Boundaries

**FAI is NOT Qualification**:
- FAI verifies conformance to design documentation (correct build)
- Qualification verifies ability to meet reliability/performance targets (correct design)
- FAI can be part of qualification evidence, but does not replace qualification testing

**Screening is NOT Qualification**:
- Screening removes defective units from production lots
- Qualification proves the design/process can produce reliable units
- Screening happens on every (or sampled) production lot; qualification happens once per qualified configuration

**IPC-6012 Addenda Context**:
- IPC-6012EM (Medical): May require qualification and conformance documentation
- IPC-6012FA (Automotive): May require PPAP-style qualification and ongoing conformance
- IPC-6012FS (Space/Military): Requires formal qualification and lot acceptance testing

## Conditions And Methods

- Use this card when distinguishing between production-level screening, program-level qualification, and build-level FAI
- Apply governance layer appropriate to project requirements (commercial vs medical vs automotive vs aerospace)
- Pair with IPC-6012 addendum metadata for industry-specific qualification requirements
- Pair with AS9102 metadata for aerospace FAI requirements

## Limits And Non-Claims

- This card does not specify screening parameters (temperature, duration, sample size)
- It does not specify qualification test plans or acceptance criteria
- It does not provide FAI form content or re-accomplishment triggers
- It does not prove that any specific supplier performed qualification or passed FAI
- It does not make FAI universally mandatory for all PCBA builds

## Open Questions

- Document specific burn-in parameters when available
- Clarify qualification testing requirements for different industry segments
- Add DPA (Destructive Physical Analysis) boundary for high-reliability programs

## Source Links

- /code/hileap/frontendAPT/public/static/pcba/en/quality-system.json
- /code/hileap/frontendAPT/public/static/pcba/en/first-article-inspection.json
- https://saemobilus.sae.org/standards/as9102c-aerospace-series-first-article-inspection-requirements
- https://shop.electronics.org/taxonomy/term/792 (IPC-6012 addendum taxonomy)
- https://www.electronics.org/TOC/IPC-6012FS_TOC.pdf

