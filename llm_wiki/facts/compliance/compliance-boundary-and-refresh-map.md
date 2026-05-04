---
fact_id: "compliance-boundary-and-refresh-map"
title: "PCB/PCBA compliance boundary map: certification inventory, live-date refresh classes, and non-promotable proof claims separated"
topic: "Compliance boundary and refresh governance"
category: "compliance"
status: "active"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
source_ids:
  - "frontendapt-policies-index-en"
  - "frontendapt-about-index-en"
  - "apt_pcba_quality_system_page"
  - "ec-rohs-directive"
  - "echa-candidate-list"
  - "ipc-1782b-traceability-standard-page"
  - "fda-21cfr-82065-traceability-page"
  - "iso-26262-road-vehicles-functional-safety-package"
  - "iatf-16949-overview-page"
  - "fda-qmsr-page"
  - "faa-ac-20-152a-page"
tags: ["compliance", "certification", "refresh", "rohs", "reach", "iso-9001", "iso-13485", "iatf-16949", "as9100", "ul", "governance", "boundary-map"]
---

# Canonical Summary

> The PCB/PCBA compliance layer in this knowledge base separates into three distinct classes: (A) **Certification Inventory** — names, scope frameworks, and management system references that can be stated from internal JSON and public standards metadata; (B) **Live-Date Refresh Items** — any current-validity claim (certification active, SVHC count, exemption status, audit date) that must be re-verified before external use; (C) **Non-Promotable Proof Claims** — customer-specific qualifications, project approvals, pass-status assertions, and regulatory device-level clearances that require independent verifiable evidence and cannot be promoted from internal framing alone.

---

## Class A — Certification Inventory (Statable from Internal + Public Metadata)

These items can be stated with standard hedging as long as the source tier is respected.

### Quality Management System Certifications (Internal JSON — Tier-2)

| Certification | Framework | Source | External Use |
|--------------|-----------|--------|-------------|
| ISO 9001:2015 | Quality management system | `frontendapt-about-index-en`, `frontendapt-policies-index-en` | ✅ With "as stated in public company profile" hedge; not current validity proof |
| ISO 13485 | Medical device QMS | `frontendapt-about-index-en` | ✅ Same hedge |
| IATF 16949 | Automotive QMS | `frontendapt-about-index-en` | ✅ Same hedge |
| ISO 14001:2015 | Environmental management | `frontendapt-policies-index-en` | ✅ Same hedge |
| UL | Product safety | `frontendapt-about-index-en` | ✅ Frame as "UL listed per company profile" — do not state file number without verification |
| CCC | China compulsory certification | `frontendapt-about-index-en` | ✅ Same hedge |
| CE | European conformity declaration | `frontendapt-about-index-en` | ✅ Same hedge |
| RoHS | Hazardous substances restriction | `frontendapt-about-index-en` | ✅ Same hedge |

### Industry Standards Class Support (Internal JSON — Tier-2)

| Standard | Class/Scope | Source | External Use |
|----------|-------------|--------|-------------|
| IPC-A-600 | Class 2, Class 3 | `apt_rigid_pcb_capability_page` | ✅ Frame as "Class 2/3 per internal capability statement" |
| IPC-A-610 | Class 2, Class 3 assembly acceptability | `apt_pcba_quality_system_page` | ✅ Same hedge |
| IPC-6012 | Class 2, Class 3, 3A qualification/performance | `apt_rigid_pcb_capability_page` | ✅ Same hedge |
| MIL-PRF-31032 | Military PCB — process-capable language only | `apt_industries_aerospace_defense` | ⚠️ "Process-capable" framing only; no QPL or approval claim |

### Regulatory Substance Frameworks (Official Public Sources — Tier-1)

| Framework | Stable Fact | Source |
|-----------|-------------|--------|
| RoHS Directive | EU rules restricting hazardous substances in EEE; latest directive entered into force 21 July 2011 | `ec-rohs-directive` |
| RoHS Exemptions | Limited in time; reassessment takes ~18–24 months from application date | `ec-rohs-directive` |
| ECHA Candidate List | Authentic legal-obligation version for SVHC; 253 entries as of 2026-02-04 | `echa-candidate-list-news-2026-02-04` |

### Traceability Standards (Official Public Sources — Tier-1)

| Standard | Stable Vocabulary | Source |
|----------|------------------|--------|
| IPC-1782B | Manufacturing and supply-chain traceability; covers PCB fab + PCB/mechanical assembly | `ipc-1782b-traceability-standard-page` |
| FDA 21 CFR 820.65 | Medical device traceability, UDI linkage, recall/adverse event investigation | `fda-21cfr-82065-traceability-page` |
| AS5553E | Counterfeit-risk control for EEE procurement and integration | `as5553e-counterfeit-parts-page` |
| AS6081A | Independent distribution control: reliable sources, suspect/counterfeit parts, incident reporting | `as6081a-independent-distribution-page` |
| DFARS 252.246-7008 | Government procurement source hierarchy, risk-based traceability, contractor record obligations | `dfars-252-246-7008-sources-of-electronic-parts-page` |

### Industry Application-Qualification Standards (Official Public Sources — Tier-1, Vocabulary Only)

| Standard | Vocabulary Scope | Not Established |
|----------|-----------------|----------------|
| ISO 26262 | Road-vehicle E/E functional-safety context | No proof of specific project or system compliance |
| IATF 16949 | Automotive QMS context and customer-specific requirements framing | No proof of current certification validity per project |
| AEC-Q | Component qualification document context | No proof of any component qualification outcome |
| FDA QMSR (21 CFR Part 820) | Medical device QMS and design control vocabulary | No device-level clearance or 510(k)/PMA proof |
| FAA AC 20-152A | Airborne electronic hardware design-assurance context | No program approval or DO-254 assurance-level proof |

---

## Class B — Live-Date Refresh Items (Must Reverify Before External Use)

Any claim in this class requires current verification before it can appear in external content.

| Claim Type | Why Refresh-Required | Refresh Source |
|-----------|---------------------|----------------|
| ISO 9001:2015 currently valid | Requires periodic surveillance audits; internal JSON is point-in-time | Current certificate or audit record |
| ISO 13485 currently valid | Same | Same |
| IATF 16949 currently valid | Same | Same |
| UL file number or listing status | File numbers can change; listing scope can be modified | Current UL certification database |
| CE declaration current and applicable | Declaration of Conformity is product-specific; scope must match | Current DoC per product |
| ECHA Candidate List count | List is updated multiple times per year | ECHA live Candidate List page |
| RoHS exemption current applicability | Exemptions reassessed on 18–24 month cycles | Current EC RoHS exemption status page |
| AS9100 / MIL qualification or QPL listing | Not stated in internal JSON; would require separate evidence | Customer-provided or government QPL record |
| Facility capacity and headcount | Internal JSON is point-in-time; actual figures may change | Dated internal update or customer audit |
| Service commitments (24h DFM, 72h turnkey) | Operational figures, not contractual guarantees | Current service agreement or quote confirmation |
| ISO 9001:2015 policy documents effective date | Existing policy documents carry 2010 effective dates; may be superseded | Current published version from APTPCB |

---

## Class C — Non-Promotable Proof Claims (Blocked)

These cannot be stated from internal framing, policy documents, or metadata alone. They require independent verifiable evidence.

| Blocked Claim Class | Why Blocked |
|--------------------|-------------|
| Customer-specific compliance status | Depends on customer flowdown, audit, and acceptance — not generalizable |
| Project-specific certification validity | Certification scope is product/process/site-specific |
| Regulatory device-level approval (FDA 510(k)/PMA, CE MDR) | Requires device-specific regulatory filing and clearance |
| Supplier qualification proof (AVL, QPL, ASL) | Requires customer-specific or program-specific approved vendor record |
| AS9100 / MIL-PRF-31032 qualification proof | Not stated in any current internal source; would require separate program evidence |
| Counterfeit avoidance proof for specific lots | AS6171A: testing alone cannot confirm authenticity without traceability to original manufacturer |
| IPC-A-610 / IPC-A-600 acceptance at specific class for delivered lot | Class support ≠ inspection pass for any specific project |
| Audit outcome or pass/fail status | Requires actual audit record |
| UL file number (specific) | Not confirmed in internal sources; requires direct lookup |

---

## Conditions And Methods

- Use Class A items to establish framing, vocabulary, and policy-existence language.
- Always hedge Class A internal-JSON items with "as stated in APTPCB public profile" or equivalent disclosure.
- Always tie any SVHC/exemption count to the date it was verified.
- Use Class B items only after confirming currency with the appropriate refresh source.
- Do not promote Class C items regardless of how they appear in internal framing.

## Limits And Non-Claims

- This fact card does not prove any certification is currently valid.
- It does not establish any customer-specific, project-specific, or device-specific compliance.
- It does not replace customer due diligence, supplier audits, or regulatory filings.
- It does not provide certification text, scope statements, or audit criteria.

## Related Fact Cards

- `apt_pcb_certifications_and_standards_overview` — certification inventory (Class A expansion)
- `compliance-rohs-reach-svhc` — RoHS/REACH/SVHC live-date handling
- `standards-high-reliability-traceability-and-counterfeit-control-metadata` — traceability and counterfeit vocabulary
- `methods-pcba-release-traceability-governance-boundary` — cumulative evidence chain for PCBA release
- `internal-frontendapt-policies-metadata-boundary` — policy documents (ISO 9001/14001 framework references)
- `internal-frontendapt-business-metrics-boundary` — company profile and certification inventory source
