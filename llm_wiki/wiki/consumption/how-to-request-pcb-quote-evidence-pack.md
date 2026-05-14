---
title: "How to Request PCB Quote Evidence Pack"
category: "consumption"
status: "active"
last_reviewed_at: "2026-05-13"
tags: ["quote", "rfq", "prototype", "lead-time", "intake", "dfm", "procurement", "hilpcb"]
---

# How to Request PCB Quote Evidence Pack

**Pack ID**: `consumption-how-to-request-pcb-quote`
**Date**: `2026-05-13`
**Status**: `mostly_ready`
**Template**: `query`

---

## 1. Traceability Core

```yaml
topic: "how to request pcb quote"
scope: |
  Conservative evidence pack for a future query memo about how a reader should
  request a PCB quote from HIL without turning the page into a pricing, SLA, or
  factory-capacity claim set.

  Supports one narrow intake-and-handoff posture:
  revision identity, fab files, stackup / material / finish expectations,
  quantity, urgency, BOM identity, test intent, special requirements,
  CAM / data-exchange handoff, and controlled-source / procurement identity.

  Treats HIL /en/quote as intake authority only. It supports route identity,
  field taxonomy, upload support, and package-completeness framing. It does not
  support exact price, instant quote, lead-time promise, MOQ, yield, supplier
  ranking, capacity / factory-scale claims, quote-speed guarantee, or any
  production-readiness guarantee.

template: "prompts_template/shared/query.md"
overlay: "prompts_template/hilpcb/query-overlay.md"

fact_ids:
  - "methods-pcb-cost-driver-review-and-quote-preparation-boundary"
  - "methods-procurement-release-identity-completeness-and-controlled-source-boundary"
  - "methods-pcb-prototype-quickturn-and-volume-routing"
  - "methods-pre-fabrication-validation-workflow-boundary"

source_ids:
  - "frontendhil-quote-page-en"

wiki_framing_support:
  - "wiki/processes/pcb-design-data-exchange-and-tool-boundaries"
  - "wiki/consumption/pcb-prototype-readiness-checklist-evidence-pack.md"

must_refresh:
  - claim: "exact price, price table, savings math, or instant quote wording"
    value: true
  - claim: "lead-time promise, quote turnaround promise, or rush guarantee"
    value: true
  - claim: "MOQ, yield, live capacity, or factory-scale claim"
    value: true
  - claim: "supplier ranking, sourcing superiority, or procurement outcome claim"
    value: true
  - claim: "production-readiness or manufacturability guarantee"
    value: true

excluded_claim_classes:
  - "exact price or instant quote"
  - "lead-time promise or quote-speed guarantee"
  - "MOQ or yield claim"
  - "supplier ranking or factory-capacity ranking"
  - "capacity / factory-scale proof"
  - "uploading files guarantees production readiness"
```

---

## 2. Query Posture

| Field | Value |
|---|---|
| **Primary keyword** | `how to request pcb quote` |
| **Reader intent** | Understand which inputs should be frozen before sending an RFQ |
| **Safe angle** | Intake completeness and engineering-handoff clarity |
| **Unsafe angle** | Price-shopping, SLA, or commercial-comparison page |
| **Site** | `HILPCB` |

**Working posture**: the pack is `mostly_ready` for an internal query memo that explains RFQ input discipline for prototype and urgent-build contexts without drifting into commercial promises.

---

## 3. Safe Article Frame

| Section Type | Safe Treatment |
|--------------|----------------|
| Definition | A PCB quote request is an intake package for review, not a promise of price or schedule |
| Quote route | Position `/en/quote` as the canonical HIL intake route and field-collection authority |
| Revision identity | Ask the reader to freeze project or revision identity before upload |
| Fab files and handoff | Explain that fabrication files are part of a staged CAM/data-exchange handoff, not proof that one export is complete |
| Stackup / material / finish | Treat them as engineering inputs that shape quote-preparation review |
| Quantity and urgency | Treat them as intake fields that help routing posture, not as proof of MOQ or lead-time commitment |
| BOM identity | Keep manufacturer identity and controlled-source posture explicit; do not collapse them into casual seller strings |
| Test intent and special requirements | Treat them as review inputs for DFM / validation planning, not as guarantee triggers |
| CTA | Invite the reader to prepare the package and submit through HIL quote intake |

---

## 4. Safe Intake Scope

### 4.1 Supported Input Classes

| Input Class | Safe Use |
|-------------|----------|
| Revision identity | ✅ Project name, version, or release identity can be requested for quote clarity |
| Fab files | ✅ Gerber or comparable fabrication-package inputs can be requested as handoff artifacts |
| Stackup / material / finish | ✅ Safe as quote-preparation and complexity-review inputs |
| Quantity | ✅ Safe as RFQ intake context |
| Urgency | ✅ Safe as routing context only |
| BOM identity | ✅ Safe when framed as manufacturer / MPN / controlled-source review input |
| Test intent | ✅ Safe as validation and review-planning context |
| Special requirements | ✅ Safe as explicit constraints or notes for review |
| CAM / data-exchange handoff | ✅ Safe as package-completeness and staged handoff language |
| Controlled-source / procurement identity | ✅ Safe as governance and completeness posture |

### 4.2 Explicitly Blocked

| Blocked Claim | Reason |
|---------------|--------|
| `the quote can be given instantly` | Form presence does not authorize instant-quote claims |
| `the price will be X` | Local evidence supports intake and review posture, not exact commercial output |
| `urgent means delivery in X days` | Urgency fields are intake only, not SLA authority |
| `MOQ starts at N` | MOQ is outside the local stable evidence layer |
| `this package will yield Y%` | Yield claims are unsupported |
| `HIL is the best supplier or fastest factory` | Ranking and capacity claims are out of scope |
| `the factory can always absorb the job immediately` | Capacity / scale proof is not supported here |
| `a clean RFQ package guarantees production readiness` | Intake completeness is not the same as release success |

---

## 5. Recommended Memo Spine

1. What should a reader prepare before requesting a PCB quote?
2. Why is `/en/quote` an intake route instead of a pricing or SLA page?
3. Which revision, fabrication-file, and stackup details should travel together?
4. How should quantity and urgency be described without overpromising schedule?
5. What should the BOM prove before procurement review starts?
6. Why should test intent and special requirements be explicit in the RFQ?
7. Why does file upload not by itself prove package completeness?

---

## 6. Reusable Evidence Notes

> The safest public role for `/en/quote` is intake authority: it collects the package that quote and engineering review need. It is not stable authority for exact price, instant quoting, or lead-time promises.

> A strong RFQ starts with identity clarity: project or revision identity, fabrication files, stackup intent, material and finish expectations, quantity, urgency, BOM identity, test intent, and special requirements.

> Quantity and urgency are useful intake fields, but they do not by themselves authorize MOQ language, queue guarantees, or shipping-date commitments.

> File upload is a handoff step, not proof that the package is complete. Fabrication review, procurement review, and validation planning still depend on different evidence objects.

> Procurement-safe wording should preserve manufacturer identity, manufacturer part number, and controlled-source review as separate governance surfaces instead of turning them into live supply or ranking claims.

> Prototype and quick-turn language can explain routing posture, but not a universal promise that every urgent quote becomes an accelerated production slot.

---

## 7. Pre-flight

- [x] `/en/quote` is pinned as intake authority only
- [x] Safe scope is limited to intake, handoff, and procurement-identity fields
- [x] Price, SLA, MOQ, yield, ranking, capacity, and readiness guarantees are explicitly blocked
- [x] Prototype / urgency context is framed as routing posture rather than promise language
- [x] Pack remains usable for a future query memo without writing a public draft

**Verdict**: ✅ `mostly_ready` for `how-to-request-pcb-quote` query-memo support inside `llm_wiki`.
