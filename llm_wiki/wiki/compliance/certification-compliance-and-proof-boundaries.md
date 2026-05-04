---
topic_id: "compliance-certification-compliance-and-proof-boundaries"
title: "Certification, Compliance, And Proof Boundaries"
category: "compliance"
status: "active"
last_reviewed_at: "2026-05-03"
fact_ids:
  - "compliance-boundary-and-refresh-map"
  - "apt_pcb_certifications_and_standards_overview"
  - "compliance-rohs-reach-svhc"
  - "standards-high-reliability-traceability-and-counterfeit-control-metadata"
  - "methods-pcba-release-traceability-governance-boundary"
  - "internal-frontendapt-policies-metadata-boundary"
  - "internal-frontendapt-business-metrics-boundary"
  - "standards-automotive-medical-aerospace-application-qualification-boundary"
source_ids:
  - "frontendapt-about-index-en"
  - "frontendapt-policies-index-en"
  - "apt_pcba_quality_system_page"
  - "ec-rohs-directive"
  - "echa-candidate-list"
  - "ipc-1782b-traceability-standard-page"
  - "fda-21cfr-82065-traceability-page"
  - "iso-26262-road-vehicles-functional-safety-package"
  - "iatf-16949-overview-page"
  - "fda-qmsr-page"
  - "faa-ac-20-152a-page"
tags: ["compliance", "certification", "rohs", "reach", "iso-9001", "iso-13485", "iatf-16949", "as9100", "ul", "traceability", "counterfeit", "governance", "proof-boundary"]
---

# Definition

> Certification and compliance governance for this knowledge base means separating three non-interchangeable layers: **certification inventory** (what certifications are named in APT/HIL public sources), **live-date refresh items** (any current-validity claim that requires reverification before external use), and **non-promotable proof claims** (customer-specific qualifications, device approvals, supplier proofs, and audit outcomes that cannot be established from internal framing alone). This page is the prompt-safe routing map for that separation.

## Why This Topic Matters

- The knowledge base currently has a **weak-medium compliance layer**: certifications are named in internal JSON, but their current validity, scope, and project-applicability are not established.
- Writing compliance claims without this separation creates reputational risk: overstating a certification validity or scope that has lapsed or doesn't cover the specific product is a real liability.
- Later AI agents need a clear routing frame to decide which compliance claims are safe to include in external content and which require human verification or explicit hedging.

---

## Three-Layer Separation

### Layer 1 — Certification Inventory (Safe with Hedging)

These certification names are present in APTPCB internal public JSON and can be framed in external content with standard hedging. They do not prove current validity.

**Quality Management:**
- ISO 9001:2015 (Quality Management System)
- ISO 13485 (Medical Device QMS)
- IATF 16949 (Automotive Quality Management)
- ISO 14001:2015 (Environmental Management)

**Safety and Product:**
- UL (Product safety listing — cite as "UL listed per company profile"; do not state specific file number without verification)
- CCC (China Compulsory Certification)
- CE (European conformity — cite as "CE marked per company profile"; do not state specific DoC without product-level verification)
- RoHS (Hazardous substances compliance statement)

**Industry Standards Support:**
- IPC-A-600 Class 2/3 (PCB acceptability)
- IPC-A-610 Class 2/3 (Assembly acceptability)
- IPC-6012 Class 2/3/3A (PCB qualification/performance)

**Safe hedging pattern**: "As stated in APTPCB's public company profile, [certification name] is listed as a held certification. This does not constitute current validity confirmation and should be verified before project-specific use."

### Layer 2 — Live-Date Refresh (Require Current Verification)

These items must be verified against current records before appearing in external content. They cannot be used with the point-in-time internal JSON as sole evidence.

| Item | Refresh Source |
|------|---------------|
| ISO 9001:2015 currently valid and audited | Current certificate issued by certification body |
| ISO 13485 currently valid | Same |
| IATF 16949 currently valid | Same |
| UL listing status and file number | UL certification database (UL Product iQ) |
| CE Declaration of Conformity per product | Current DoC for specific product/directive combination |
| ECHA Candidate List SVHC count | ECHA live Candidate List page (current as of query date) |
| RoHS exemption applicability | Current EC RoHS exemption status (reassessed ~18–24 month cycles) |
| Facility capacity, headcount, SMT line count | Dated internal update or recent customer audit |
| 24h DFM / 72h turnkey service levels | Current service agreement or quote confirmation |
| ISO 9001/14001 policy document currency | Existing internal policy docs carry 2010 effective dates; verify whether superseded versions exist |

### Layer 3 — Non-Promotable Proof Claims (Blocked)

These cannot be stated from any source currently in the knowledge base. They require independent verifiable evidence obtained outside this repo.

| Blocked Claim | Why Non-Promotable |
|--------------|-------------------|
| Customer-specific compliance status | Depends on customer flowdown, program scope, and acceptance testing |
| Project-specific certification validity | Certification scope is site/process/product-specific; cannot generalize |
| FDA 510(k) / PMA device clearance | Requires device-specific regulatory filing and FDA decision |
| CE Medical Device Regulation (MDR) conformity | Requires notified body involvement for higher-risk classes |
| AS9100 qualification proof | Not stated in any internal source |
| MIL-PRF-31032 QPL or qualification record | Not stated in any internal source; requires government program evidence |
| Supplier qualification proof (AVL, QPL, ASL) | Customer/program-specific approved vendor record required |
| Audit outcome or pass/fail for specific lot | Requires actual audit or inspection record |
| Counterfeit-part authentication for specific lot | AS6171A: testing alone cannot confirm authenticity without original-manufacturer traceability |
| UL specific file number | Not confirmed in current internal sources |
| ISO 26262 / IATF 16949 project compliance | Vocabulary can be used; actual E/E system safety compliance is project-specific |

---

## Regulatory Substance Governance

### RoHS / REACH / SVHC

**Safe to state (Tier-1 official):**
- EU RoHS rules restrict hazardous substances in electrical and electronic equipment; latest directive entered into force 21 July 2011.
- RoHS exemptions are time-limited and reassessed (typically ~18–24 months from application date).
- ECHA maintains the authentic Candidate List for SVHC legal-obligation purposes.
- As of 2026-02-04, the Candidate List had 253 entries.

**Always required:**
- Tie any SVHC count to its verification date — the Candidate List is updated multiple times per year.
- Do not present an old count as current without date attribution.
- Do not collapse REACH article obligations with RoHS substance restrictions into the same rule set.

---

## Traceability and Counterfeit-Control Governance

### What Can Be Stated

- IPC-1782B is the current IPC traceability standard covering PCB fabrication and PCB/mechanical assembly; it defines traceability levels and data elements.
- APTPCB uses a cumulative evidence chain: IQC → production lot tracking → inspection/test gates → final release authorization (Certificate of Conformance).
- Four traceability levels exist in the APTPCB framing: PCB lot only → PCB + major component lots → full BOM lot → serialized unit.
- AS5553E, AS6081A, and DFARS 252.246-7008 provide standards vocabulary for counterfeit-risk control, independent distribution control, and government procurement source hierarchy.

### What Must Not Be Claimed

- That any specific lot, component, or board has been authenticated per AS6171A requirements.
- That testing alone proved counterfeit-free status (AS6171A: testing without known chain of custody cannot confirm authenticity).
- That APTPCB satisfies DFARS 252.246-7008 for any specific government contract.
- That specific IPC-1782B traceability levels have been achieved for a particular project.

---

## Industry-Sector Compliance Routing

| Sector | Vocabulary Available | Proof Not Available |
|--------|---------------------|---------------------|
| **Automotive** | ISO 26262 (functional-safety context), IATF 16949 QMS framing, AEC-Q component-document context, PPAP/APQP/FMEA/SPC vocabulary | Specific project ISO 26262 ASIL compliance, current IATF 16949 certificate, component qualification results |
| **Medical** | ISO 13485 QMS framing, FDA QMSR (21 CFR Part 820) design-control vocabulary, IQC/traceability/COC chain, UDI context | FDA 510(k)/PMA clearance, CE MDR conformity, device-level approval, clinical performance claims |
| **Aerospace/Defense** | AS9100 framing (named in profile), FAA AC 20-152A design-assurance context, AS9102 FAI vocabulary, traceability/counterfeit-control vocabulary (AS5553E, AS6081A, IPC-1782B) | AS9100 current certification, MIL-PRF-31032 QPL, program-specific qualification record, DO-254 assurance level |
| **General/Commercial** | ISO 9001:2015 QMS framing, RoHS compliance statement, IPC-A-610 Class 2 acceptability framing | Specific customer audit outcome, lot-specific compliance record |

---

## Engineering Boundaries

- Use Layer 1 (certification inventory) for establishing that certifications have been held; always hedge with "per company profile" or equivalent.
- Use Layer 2 (live-date refresh) items only after current verification — treat internal JSON values as point-in-time historical snapshots.
- Keep Layer 3 (proof claims) blocked regardless of how they appear in internal framing or marketing language.
- Do not conflate standards vocabulary with compliance proof: knowing what ISO 26262 requires is not the same as claiming a product is ISO 26262 compliant.
- Do not conflate service scope with regulatory compliance: performing SMT assembly for medical customers does not prove medical device regulatory status.

## Common Misreadings to Avoid

- **"Listed certification = currently valid"** — Certifications require periodic surveillance audits; internal JSON is point-in-time.
- **"ISO 13485 listed = medical device compliant"** — QMS certification for a manufacturer does not prove any specific device meets regulatory requirements.
- **"CE marking = EU conformity for any product"** — CE conformity is product-specific and directive-specific; a general CE statement does not cover all products.
- **"ECHA 253 entries is current"** — The Candidate List is updated multiple times per year; always cite date.
- **"RoHS compliant = no restricted substances at any time"** — Exemptions exist and are time-limited; SVHC status changes with Candidate List updates.
- **"Traceability system exists = specific lot is traceable"** — System capability does not prove specific lot traceability without the actual records.

## Must Refresh Before Publishing

- Any statement about current certification validity (ISO 9001, ISO 13485, IATF 16949, UL, CE, CCC)
- Any SVHC count or RoHS exemption status claim — always include verification date
- Any capacity, headcount, or facility-scale figure
- Any service-level commitment (24h DFM, 72h turnkey) used as a guaranteed SLA
- Any claim about medical, automotive, or aerospace compliance for a specific product or project
- Any statement about counterfeit controls for a specific lot or delivery

## Related Fact Cards

- `compliance-boundary-and-refresh-map` — primary three-class map (Class A/B/C separation)
- `apt_pcb_certifications_and_standards_overview` — full certification and standards inventory
- `compliance-rohs-reach-svhc` — RoHS/REACH/SVHC live-date handling
- `standards-high-reliability-traceability-and-counterfeit-control-metadata` — IPC-1782B, AS5553E, AS6081A, DFARS vocabulary
- `methods-pcba-release-traceability-governance-boundary` — cumulative evidence chain (IQC → production → test → release)
- `internal-frontendapt-policies-metadata-boundary` — policy documents (ISO 9001/14001 framework)
- `internal-frontendapt-business-metrics-boundary` — company profile and certification inventory

## Related Wiki Pages

- `wiki/applications/industry-application-scenarios-and-boundaries.md` — application-scenario framing; compliance boundaries per industry sector
- `wiki/processes/pcba-npi-to-mass-production-flow.md` — PCBA quality gates and process flow context

## Primary Sources

- `/code/hileap/frontendAPT/public/static/about/en/index.json`
- `/code/hileap/frontendAPT/public/static/policies/en/quality-policy.md`
- `https://environment.ec.europa.eu/topics/waste-and-recycling/rohs-directive_en`
- `https://www.echa.europa.eu/candidate-list-table`
- `https://shop.electronics.org/ipc-1782/ipc-1782-standard-only/Revision-b/english`
- `https://www.iso.org/publication/PUB200262.html`
- `https://www.iatfglobaloversight.org/iatf-16949/`
- `https://www.fda.gov/medical-devices/postmarket-requirements-devices/quality-system-qs-regulationmedical-device-current-good-manufacturing-practices-cgmp`
- `https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/1041323`
