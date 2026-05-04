# Lane Log: P4-151 Compliance Boundary And Refresh Map

## Task Metadata

| Field | Value |
|-------|-------|
| `task_id` | `p4-151-compliance-boundary-and-refresh-map` |
| `lane` | `compliance boundary and refresh map` |
| `status` | `completed` |
| `completed_at` | `2026-05-03` |
| `scope` | Turn the current weak-medium compliance layer into a prompt-safe local map that separates certification inventory, live-date refresh items, and non-promotable proof claims |
| `write_scope` | `facts/compliance/`, `wiki/compliance/`, `logs/p4-151-compliance-boundary-and-refresh-map.md` |

---

## Inputs Read

| File | Role |
|------|------|
| `facts/compliance/apt-pcb-certifications-and-standards-overview.md` | Certification inventory baseline (ISO 9001, IATF 16949, AS9100, IPC class support) |
| `facts/compliance/rohs-reach-svhc.md` | RoHS/REACH/SVHC live-date handling baseline |
| `facts/internal/frontendapt-policies-metadata-boundary.md` | Policy document existence, ISO 9001/14001 framework, 2010 dates caveat |
| `facts/internal/frontendapt-business-metrics-boundary.md` | Company profile, facility scale, certification inventory, service commitments |
| `facts/standards/high-reliability-traceability-and-counterfeit-control-metadata.md` | IPC-1782B, AS5553E, AS6081A, AS6171A, DFARS 252.246-7008 vocabulary boundary |
| `facts/methods/pcba-release-traceability-governance-boundary.md` | IQC → production → test → release cumulative evidence chain |
| `wiki/applications/industry-application-scenarios-and-boundaries.md` | Industry sector compliance framing, qualification vocabulary boundaries |

---

## Changed Files

| File | Action | Notes |
|------|--------|-------|
| `facts/compliance/compliance-boundary-and-refresh-map.md` | **Created** | New fact card: three-class compliance map (Class A inventory / Class B live-date / Class C blocked) |
| `wiki/compliance/certification-compliance-and-proof-boundaries.md` | **Created** | New wiki governance page; `wiki/compliance/` directory created as side effect |
| `logs/p4-151-compliance-boundary-and-refresh-map.md` | **Created** | This lane log |

**Existing fact cards in `facts/compliance/`**: Not modified. Both `apt-pcb-certifications-and-standards-overview.md` and `rohs-reach-svhc.md` are already sound and are referenced as inputs by the new boundary map.

**Source records**: Not modified. All existing source records are sufficient to support this aggregation.

---

## Local Knowledge Landed in This Pass

### 1. Three-Class Compliance Separation (new)

The new `compliance-boundary-and-refresh-map.md` fact card establishes for the first time:
- **Class A (Certification Inventory)**: what can be stated with standard hedging from internal JSON + public metadata
- **Class B (Live-Date Refresh)**: what requires current reverification before external use (includes ISO validity, UL file numbers, SVHC counts, service levels, policy document currency)
- **Class C (Non-Promotable Proof)**: what cannot be established from any current internal source (customer-specific compliance, device approvals, supplier qualification, audit outcomes, counterfeit authentication)

### 2. Industry-Sector Compliance Routing Table (new)

First explicit sector-by-sector routing for automotive / medical / aerospace / general-commercial: what vocabulary is available vs. what proof is not available. This prevents later AI from treating ISO 26262 framing as ISO 26262 project compliance.

### 3. Regulatory Substance Governance Summary (new)

First aggregated governance section for RoHS/REACH/SVHC: combined with the existing `compliance-rohs-reach-svhc` fact card into a routing frame, including the "always tie SVHC count to date" rule.

### 4. Traceability + Counterfeit Control Routing (new)

First explicit routing boundary for IPC-1782B / AS5553E / AS6081A / AS6171A in the compliance wiki: what vocabulary can be stated vs. what cannot be claimed (especially the AS6171A "testing alone ≠ authenticity" boundary).

### 5. Common Misreadings Prevention Layer (new)

Six explicit misreadings documented: "listed certification = currently valid", "ISO 13485 = medical device compliant", "CE marking = any product", "SVHC 253 = current", "RoHS compliant = always", "traceability system = specific lot traceable".

### 6. `wiki/compliance/` Directory Created (structural)

First wiki page under the new `wiki/compliance/` path. The compliance topic now has a dedicated wiki governance layer separate from `wiki/applications/`.

---

## Source Records: Updated or Unchanged?

**Intentionally preserved unchanged**: All existing source records. This is an aggregation/governance pass, not a source recovery or refresh pass. Existing records are sufficient to support the three-class separation.

---

## Blocked Claims (Explicitly Preserved)

1. **Current certification validity** — ISO 9001, ISO 13485, IATF 16949, UL, CE, CCC all require live verification; internal JSON is point-in-time
2. **Customer-specific compliance status** — blocked; depends on customer flowdown and acceptance
3. **Project-specific certification validity** — blocked; site/process/product-specific
4. **FDA device-level clearance** (510(k)/PMA) — blocked; requires device-specific regulatory filing
5. **CE Medical Device Regulation conformity** — blocked; requires notified body involvement
6. **AS9100 / MIL-PRF-31032 qualification proof** — not in any internal source; blocked
7. **Supplier qualification proof (AVL, QPL, ASL)** — blocked; program-specific
8. **Audit outcome / pass-fail for specific lot** — blocked; requires actual record
9. **Counterfeit authentication for specific lot** — blocked per AS6171A principle
10. **UL specific file number** — not confirmed in internal sources; blocked without verification
11. **ISO 26262 / IATF 16949 project compliance** — vocabulary available; project proof blocked

---

## Residual Gaps

| Gap | Status | Reopen Condition |
|-----|--------|-----------------|
| Current ISO 9001:2015 certificate text or validity date | Not in repo | Obtain from APTPCB current certificate |
| UL file number and current listing scope | Not in repo | Lookup in UL Product iQ |
| CE Declaration of Conformity per product | Not in repo | Product-specific; obtain from APTPCB |
| AS9100 status | Not confirmed in any internal source | Reopen only if external evidence is provided |
| MIL-PRF-31032 QPL status | Not confirmed | Same |
| ISO 9001/14001 policy document currency (2010 dates) | Unknown if superseded | Verify whether newer policy versions have been published |
| SCIP notification logic | Not yet covered | Add separate fact card if content covers EU article disclosure workflows |

---

## Completion Status

**Status**: `completed`

**Completion definition met**:
- ✅ New fact card created: `facts/compliance/compliance-boundary-and-refresh-map.md`
- ✅ New wiki page created: `wiki/compliance/certification-compliance-and-proof-boundaries.md`
- ✅ Lane log created (this file)
- ✅ Blocked claims explicitly preserved and listed
- ✅ Residual gaps explicitly listed
- ✅ Changed files explicitly listed
- ✅ Local knowledge landed: three-class separation, sector routing, RoHS/traceability governance, misreadings prevention

**Knowledge layer change**: `wiki/compliance/` created (new subdirectory); compliance coverage upgraded from "certification names in two fact cards" to "prompt-safe three-class separation with routing rules, sector-specific boundaries, and explicit blocked-claim list".

**Not a source refresh**: No `checked_at`, `URL`, or timestamp was mechanically updated to simulate completion.
