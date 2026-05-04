---
fact_id: "standards-civil-aerospace-assurance-boundary"
title: "Civil aerospace assurance standards (AS9100, DO-160G, DO-254, FAA TSO, ITAR/EAR) are QMS / hardware-assurance / device-authorization / export-control boundaries — not PCB qualification proof"
topic: "Civil aerospace assurance standards identity and PCB boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-03"
source_ids:
  - "faa-ac-21-16g-do160-acceptability-page"
  - "faa-ac-20-152a-page"
  - "rtca-do-160g-product-page"
  - "rtca-do-254-product-page"
  - "rtca-do-155-product-page"
  - "as9102c-first-article-inspection-page"
notes: "AS9100 / OASIS: No official AS9100 certificate record or OASIS/IAQG registry source currently in the sources registry — AS9100 identity uses publicly known QMS standard scope. ITAR/EAR: No official ITAR/EAR source currently in sources registry — completely outside current corpus; vocabulary is blocked without exception. TSO: No official FAA TSO authorization source currently in registry. DO-160G, DO-254, DO-155 have existing source records (see source_ids above)."
tags: ["civil-aerospace", "as9100", "oasis", "do-160g", "do-254", "do-155", "faa-tso", "itar", "ear", "arinc", "qualification-boundary", "assurance-boundary", "avionics"]
---

# Canonical Summary

> Civil aerospace assurance standards operate at distinct governance layers — none create PCB-level certification, qualification, or authorization status. AS9100 is a QMS standard for aerospace organizations; DO-160G is an environmental test-procedures document family for airborne equipment; DO-254 is a design-assurance guidance document for airborne electronic hardware; FAA TSO is a device-level authorization for specific avionics articles; ITAR and EAR are US export-control regulations governing defense and dual-use articles. Mentioning these in PCB/PCBA content is safe only at document-identity and scope-framing level. All qualification pass-status, DAL assignment, authorization proof, certificate validity, and export-control compliance claims are blocked.

## Assurance Standard Families

### AS9100 — Aerospace Quality Management System

| Item | Identity (Source-Backed or Public Knowledge) |
|---|---|
| **AS9100** | SAE / IAQG AS9100 Aerospace Quality Management System standard. Current revision is AS9100D (2016). Based on ISO 9001 with aerospace-specific additions. |
| **OASIS / IAQG** | Online Aerospace Supplier Information System (OASIS) — the IAQG database of certified organizations with active AS9100/AS9110/AS9120 certificates. Certification status must be verified from OASIS, not from a supplier's marketing statement. |
| **AS9102** | Aerospace First Article Inspection Requirements standard — defines documentation and inspection requirements for first production units. Source in registry: `as9102c-first-article-inspection-page`. |
| **Scope** | AS9100 applies to the aerospace organization's quality management system — not to individual PCBs, builds, or shipments. |

**PCB boundary for AS9100:**
- AS9100 QMS vocabulary (first-article inspection, lot traceability, configuration control, non-conformance reporting, corrective action) is safe at process-description level.
- `"AS9100 Certified – Mission Assurance"` in the Tier-2 aerospace-defense source is a trust-bar marketing label — it does NOT prove current AS9100D certificate, scope, or OASIS registration status.
- Certificate validity is time-limited and scope-specific; it cannot be assumed from a product page.
- AS9102 first-article inspection identity is source-backed (`as9102c-first-article-inspection-page`) at documentation-context level only — NOT process-qualification proof.

**Blocked at PCB level:**
- `"AS9100 certified PCB"`, `"AS9100D compliant build"`, `"OASIS-listed PCB manufacturer"` (without live OASIS record) — all unsupported.
- Any AS9100 certificate number, scope, or audit date claim without verified source.

---

### DO-160G — Environmental Conditions and Test Procedures for Airborne Equipment

| Item | Identity (Source-Backed) |
|---|---|
| **DO-160G** | RTCA `DO-160G` Environmental Conditions and Test Procedures for Airborne Equipment. Source in registry: `rtca-do-160g-product-page`. |
| **FAA AC 21-16G** | FAA Advisory Circular recognizing DO-160 versions D–G as containing acceptable environmental qualifications for certain airworthiness requirements; strongly encourages DO-160G for new articles. Source in registry: `faa-ac-21-16g-do160-acceptability-page`. |
| **Scope** | DO-160G defines environmental test categories and test procedures for airborne equipment — including temperature, altitude, vibration, humidity, EMI, etc. It is a test-procedures framework, not a qualification pass-status. |
| **Sections** | DO-160G contains numbered sections (e.g., Section 4 temperature, Section 8 vibration, Section 21 magnetic effect) — section-specific test conditions and pass/fail criteria are within the standard and are NOT recoverable from the public RTCA product page. |

**PCB boundary for DO-160G:**
- DO-160G document-family identity vocabulary is source-backed and safe: named as the RTCA environmental-conditions and test-procedures document family for airborne equipment.
- FAA AC 21-16G recognition context is source-backed: DO-160 versions D–G recognized for certain airworthiness requirements.
- Section-level test conditions, temperature ranges, vibration profiles, humidity limits, altitude limits, or pass/fail criteria are inside the standard text — NOT recoverable from public RTCA product page metadata.
- A PCB or PCBA does not "pass DO-160G"; the complete airborne equipment/article is tested against selected DO-160G sections as determined by the applicant and the appropriate airworthiness authority.

**Blocked at PCB level:**
- `"DO-160G qualified PCB"`, `"DO-160G Section 4 passed"`, `"DO-160G compliant PCBA"` — all unsupported.
- Any specific temperature, vibration, altitude, or EMI DO-160G value without section-level source.

---

### DO-254 — Design Assurance Guidance for Airborne Electronic Hardware

| Item | Identity (Source-Backed) |
|---|---|
| **DO-254** | RTCA `DO-254` Design Assurance Guidance for Airborne Electronic Hardware. Source in registry: `rtca-do-254-product-page`. |
| **FAA AC 20-152A** | FAA Advisory Circular supporting airborne electronic hardware design-assurance context; explicitly covers circuit-board-assembly scope. Source in registry: `faa-ac-20-152a-page`. |
| **DAL (Design Assurance Level)** | DO-254 defines Design Assurance Levels A–E (A = most critical, E = no safety effect). DAL assignment is determined by the safety assessment of the aircraft function, not by the PCB manufacturer. |
| **Scope** | DO-254 applies to the hardware design lifecycle process — planning, requirements, design, implementation, verification, configuration management, and process assurance. FAA AC 20-152A supports circuit-board-assembly context only. |

**PCB boundary for DO-254:**
- DO-254 document-family identity vocabulary is source-backed: RTCA airborne electronic hardware design-assurance guidance document; circuit-board-assembly scope supported by FAA AC 20-152A.
- DAL assignment (DAL-A, B, C, D, E) is a safety-assessment outcome determined by the aircraft system integrator and certification authority — not by the PCB manufacturer.
- A PCB manufacturer can describe manufacturing to a customer's DO-254 program requirements; they cannot assert DAL level or DO-254 compliance independently.

**Blocked at PCB level:**
- `"DO-254 DAL-B PCB"`, `"DO-254 compliant flight controller PCB"`, `"DO-254 certified PCB manufacturer"` — all unsupported.
- Any DAL assignment without a customer-program safety-assessment source.

---

### DO-155 — Minimum Performance Standards for Airborne Low-Range Radar Altimeters

| Item | Identity (Source-Backed) |
|---|---|
| **DO-155** | RTCA `DO-155` Minimum Performance Standards – Airborne Low Range Radar Altimeters. Source in registry: `rtca-do-155-product-page`. |
| **Scope** | Applies specifically to low-range radar altimeters — NOT to barometric altimeters or laser altimeters. |

**PCB boundary for DO-155:**
- DO-155 identity is safe for radio altimeter RF front-end PCB context only.
- Do NOT apply DO-155 to barometric pressure sensor PCBs or laser time-of-flight PCBs.
- For altimeter-specific slug content, route to `wiki/processes/altimeter-aviation-standards-and-assurance-boundaries.md`.

---

### FAA TSO — Technical Standard Order

| Item | Identity (Public Knowledge) |
|---|---|
| **TSO** | FAA Technical Standard Order — a minimum performance standard for specified articles used on civil aircraft. TSO authorization is granted to a specific article design and manufacturer. |
| **TSO-C** prefix | TSO-C numbers identify specific equipment categories (e.g., TSO-C119 for TCAS, TSO-C151 for TAWS, TSO-C145/C146 for GNSS). |
| **Scope** | TSO authorization applies to a specific avionics article (device) — the complete unit including hardware, firmware, and documentation — authorized by the FAA for installation on civil aircraft. |

**PCB boundary for FAA TSO:**
- TSO is a device-level authorization — it applies to a named avionics article, not to a PCB or PCBA.
- A PCB manufacturer cannot hold TSO authorization; the TSO holder is the article designer/manufacturer.
- TSO identity context (named TSO number for an avionics category) may be used to describe the application context of a board — not as a claim that the PCB has TSO authorization.

**Blocked at PCB level:**
- `"TSO-authorized PCB"`, `"TSO-C119 compliant PCBA"`, `"TSO-approved board"` — all unsupported without the complete device holding TSO authorization.

---

### ARINC Standards — Avionics Data Buses

| Item | Identity (Public Knowledge) |
|---|---|
| **ARINC 429** | Aeronautical Radio Inc. specification for the dominant avionics data bus used in civil transport aircraft — defines unidirectional serial communication. |
| **ARINC 664 / AFDX** | ARINC specification for Avionics Full-Duplex Switched Ethernet (AFDX) — used in modern commercial aircraft for high-bandwidth data transfer. |
| **ARINC 825** | Controller Area Network (CAN) application layer for avionics. |

**PCB boundary for ARINC:**
- ARINC bus identity (named bus standard, board interface vocabulary) is safe as application-context framing.
- ARINC conformance testing is device/system-level — not PCB manufacturing proof.

**Blocked at PCB level:**
- `"ARINC 429 conformant PCB"`, `"AFDX certified board"` — unsupported.

---

### ITAR / EAR — US Export-Control Regulations

| Item | Identity |
|---|---|
| **ITAR** | International Traffic in Arms Regulations (22 CFR Parts 120–130); controls export and import of defense-related articles and services listed on the US Munitions List (USML). |
| **EAR** | Export Administration Regulations (15 CFR Parts 730–774); controls export of dual-use items on the Commerce Control List (CCL). |
| **ECCN** | Export Control Classification Number — assigned to items on the CCL. |

**Full block — no PCB vocabulary:**
- ITAR and EAR are completely outside the current sources registry.
- Any ITAR or EAR compliance, authorization, license, exemption, or ECCN classification claim requires official source recovery before any content can be written.
- "ITAR-compliant PCB", "EAR99 PCB", "ITAR-free PCB", "ITAR-registered supplier" — all completely unsupported without official source.
- This applies equally to civil aerospace and defense contexts.

---

## Stable Facts

- AS9100D is the current revision; AS9100 certificate validity and OASIS registration must be verified from OASIS — not from marketing pages or Tier-2 sources.
- DO-160G, DO-254, DO-155 have source-backed identity cards in the registry; they are supported at document-family and scope-identity level only.
- FAA AC 20-152A supports circuit-board-assembly design-assurance context — this is the closest existing source to PCB-level assurance; it is still NOT PCB qualification proof.
- FAA TSO is a device-level authorization; no PCB-level TSO claim is supportable.
- ARINC bus standards are protocol-identity vocabulary only; conformance is device/system level.
- ITAR and EAR are completely blocked — no content permitted without official source recovery.

## Conditions And Methods

- Use this card for any civil aerospace draft mentioning AS9100, DO-160G, DO-254, DO-155, TSO, ARINC, ITAR, or EAR.
- Pair with `wiki/applications/civil-aerospace-pcb-pcba-boundary-map.md` for full application routing.
- Pair with `wiki/applications/civil-aerospace-assurance-routing-boundary.md` for the prompt-consumable companion.
- For altimeter-specific slugs, also use `wiki/processes/altimeter-aviation-standards-and-assurance-boundaries.md`.
- For defense-specific vocabulary (MIL-STD, weapons systems, EW), route to `wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md`.

## Limits And Non-Claims

- AS9100 certificate status, scope, or OASIS registration NOT supported.
- DO-160G section-level test conditions or pass-status NOT supported.
- DO-254 DAL assignment or design-assurance compliance NOT supported.
- FAA TSO authorization for any device or PCB NOT supported.
- ARINC conformance proof NOT supported.
- ITAR/EAR compliance, license, exemption, or ECCN classification COMPLETELY BLOCKED.

## Remaining Gaps

| Gap | Reopen Condition |
|-----|-----------------|
| Official AS9100D / OASIS registry source | SAE/IAQG OASIS page added to sources registry |
| Official FAA TSO index source | FAA TSO page added to sources registry |
| Official ITAR USML source | DDTC/State Dept ITAR source added to registry (currently completely blocked) |
| Official EAR CCL source | BIS/Commerce Dept EAR source added to registry (currently completely blocked) |
| Official ARINC 429 / ARINC 664 public metadata | ARINC standards page added to registry |
| DO-160G section-level vocabulary | Full DO-160G standard access or clause-level FAA AC source |
| DO-254 DAL vocabulary depth | Full DO-254 standard or clause-level source |
| Promote wiki page draft → active | Content review pass |
