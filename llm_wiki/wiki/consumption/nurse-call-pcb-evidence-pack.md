# Nurse Call PCB Evidence Pack

**Pack ID**: `consumption-nurse-call-pcb`
**Date**: 2026-05-05
**Status**: `go_now_conservative`
**Template**: `blog-rewrite`

---

## 1. Traceability Core

```yaml
topic: "Nurse call PCB rewrite"
scope: |
  Conservative evidence pack for rewriting nurse-call, bedside-terminal,
  patient-handset, and room-signaling PCB content into a release-review article.

  Supports nurse-call system identity, bedside and room-device vocabulary,
  mixed audio plus network board context, cleaning and protection workflow,
  test-method layering, and validation handoff.

  Does not support PCB-level safety compliance, patient-protection proof,
  installation approval, uptime claims, or universal electrical-test rules.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/aptpcb/query-overlay.md"

fact_ids:
  - "methods-nurse-call-pcb-release-boundary"
  - "standards-medical-standards-depth-boundary"
  - "methods-pcba-inspection-process-governance-boundary"
  - "methods-pcba-flying-probe-vs-ict-selection-posture"
  - "methods-conformal-coating-medical-regulated-boundary"
  - "methods-pcba-medical-traceability-dhr-dmr-boundary"

source_ids:
  - "ul-nurse-call-emergency-call-systems-page"
  - "iec-60601-1-medical-electrical-equipment-page"
  - "ascom-nurse-call-solutions-page"
  - "austco-tacera-nurse-call-page"
  - "frontendapt-industry-medical-page-en"

wiki_support:
  - "wiki/consumption/medical-device-evidence-pack.md"
  - "wiki/applications/medical-device-pcb-pcba-boundary-map.md"

must_refresh:
  - claim: "Any PCB-level safety or patient-protection wording"
    value: true
  - claim: "Any exact cleaning, coating, or electrical-test threshold"
    value: true
  - claim: "Any lead-time, cost, yield, or uptime wording"
    value: true

excluded_claim_classes:
  - "UL 1069 compliance proof at PCB level"
  - "IEC 60601-1 compliance proof at PCB level"
  - "2 MOPP / 2 MOOP board qualification"
  - "patient-safe or approved PCB wording"
  - "universal ICT-mandatory claims"
  - "cost, lead-time, yield, uptime, or response-time promises"
```

## 2. Rewrite Posture

| Field | Value |
|---|---|
| **Primary keyword** | `nurse call PCB` |
| **Reader intent** | Understand what should be reviewed before releasing a nurse-call board into fabrication and assembly |
| **Safe angle** | Board role, patient-side versus infrastructure-side split, audio plus network coexistence, cleaning workflow, cable and handset handoff, layered validation |
| **Unsafe angle** | Medical compliance explainer, patient-protection proof, or generic hospital-equipment brochure |

## 3. Handoff Summary

> A safe `nurse call PCB` rewrite should behave like a bedside and room-signaling release-review article. It should explain how the board fits inside a nurse-call system, which physical and workflow burdens belong to bedside devices, how audio, network, and power paths must stay separated, how cleaning and protection decisions affect access, and how board evidence hands off into later functional and system-level validation. It must not drift into UL 1069 listing proof, IEC 60601-1 compliance proof, patient-protection classification, or universal testing claims.

**Verdict**: ✅ `go_now_conservative`
