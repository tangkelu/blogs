# Lane Log: P4-167 Civil Aerospace Assurance Boundary Recovery

## Task Metadata

| Field | Value |
|-------|-------|
| `task_id` | `p4-167-civil-aerospace-assurance-boundary-recovery` |
| `lane` | `civil aerospace assurance boundary recovery` |
| `status` | `completed` |
| `completed_at` | `2026-05-03` |
| `scope` | Create a unified local assurance-boundary pack for AS9100/DO-160G/DO-254/TSO/ITAR/ARINC vocabulary so civil aerospace prompts stop relying on scattered blocked-claim notes |
| `write_scope` | `facts/standards/civil-aerospace-assurance-boundary.md`, `wiki/applications/civil-aerospace-assurance-routing-boundary.md`, `logs/p4-167-civil-aerospace-assurance-boundary-recovery.md` |

---

## Problem Being Solved

After P4-163, the civil aerospace application boundary page listed blocked claims: AS9100 certification, DO-254 DAL assignment, TSO authorization, ITAR/EAR compliance. But:

1. Blocked-claims lists have no reasoning structure — future agents cannot construct safe alternative sentences.
2. DO-160G and DO-254 already had source-backed identity in `standards-aviation-altimeter-standards-metadata-boundary` (from altimeter work), but no unified page collected all civil aerospace assurance standards into one place.
3. AS9100 had no local fact card beyond the altimeter card's reference; AS9100 trust-bar risk was called out in P4-163 but not backed by a structured boundary explanation.
4. FAA TSO, ARINC, and ITAR/EAR had no local identity framing at all.

P4-167 closes all four gaps in one unified assurance-boundary pack.

### Source Recovery Status

| Source Family | Status |
|---|---|
| DO-160G, DO-254, DO-155 | Source-backed (`rtca-do-160g-product-page`, `rtca-do-254-product-page`, `rtca-do-155-product-page`, `faa-ac-21-16g-do160-acceptability-page`, `faa-ac-20-152a-page`) — included in `source_ids` |
| AS9102 | Source-backed (`as9102c-first-article-inspection-page`) — included in `source_ids` |
| AS9100D / OASIS | Not in registry — publicly known QMS identity metadata used; noted in card `notes` field |
| FAA TSO | Not in registry — publicly known device-authorization identity used; noted |
| ITAR / EAR | Not in registry; COMPLETELY BLOCKED — noted in all three placement locations |
| ARINC 429 / 664 | Not in registry — publicly known protocol identity used; noted |

---

## Inputs Read

| File | Role |
|------|------|
| `facts/applications/civil-aerospace-coverage-gap-map.md` | Full read — confirmed 5 remaining assurance gaps (AS9100, DO-160G sections, DO-254 DAL, TSO, ITAR/EAR) |
| `facts/standards/aviation-altimeter-standards-metadata-boundary.md` | Full read — DO-160G/DO-254/DO-155 source-backed identity; this lane extends to AS9100/TSO/ARINC/ITAR layer |
| `facts/standards/automotive-medical-aerospace-application-qualification-boundary.md` | Reference — FAA AC 20-152A and AS9102 boundary patterns |
| `facts/standards/security-equipment-standards-boundary.md` | Format reference from P4-165 |

---

## Created Files

| File | Notes |
|------|-------|
| `facts/standards/civil-aerospace-assurance-boundary.md` | **Created** — 7 assurance families (AS9100/AS9102, DO-160G, DO-254, DO-155, FAA TSO, ARINC, ITAR/EAR), governance-layer identification, PCB-stop lines, blocked claims, remaining gaps. DO-160G/DO-254/DO-155 source-backed; others publicly known identity or completely blocked. |
| `wiki/applications/civil-aerospace-assurance-routing-boundary.md` | **Created**, status `draft` — document-identity sentences per family, governance-layer reach, PCB-stop lines, routing summary table, 7 common misreadings, must-refresh list |
| `logs/p4-167-civil-aerospace-assurance-boundary-recovery.md` | **Created** — this lane log |

---

## Local Knowledge Landed

### 1. Seven assurance families unified under one entry point

| Family | Governance Layer | Source Status |
|--------|----------------|--------------|
| AS9100D / OASIS | QMS — aerospace organization level | Publicly known identity; OASIS not in registry |
| AS9102 | FAI — first-build documentation | Source-backed |
| DO-160G | Environmental test-procedures — complete airborne article | Source-backed |
| DO-254 | Design-assurance process guidance — hardware lifecycle | Source-backed |
| DO-155 | MPS — low-range radar altimeter only | Source-backed |
| FAA TSO | Device-level authorization — named avionics article | Publicly known identity; not in registry |
| ARINC 429/664/825 | Protocol identity — device/system conformance level | Publicly known identity; not in registry |
| ITAR / EAR | Export-control law — complete block | NOT in registry; completely blocked |

### 2. "Governance layer" concept introduced
Each standard family now has an explicit "Governance layer" label — this is new vocabulary added to this card vs. previous cards. It tells agents immediately at which layer (QMS / test-procedures / design-assurance / device-authorization / export-law) the standard operates, so the PCB-stop line follows naturally.

### 3. ITAR/EAR complete block stated in three locations
ITAR/EAR complete block is stated in:
- The fact card (standalone section with "Full block" header)
- The wiki routing table ("Complete block — no routing")
- The must-refresh list ("complete block until official source")
- The common misreadings section (two misreadings: `"ITAR-free PCB"` and `"EAR99 PCB"`)

### 4. AS9100 trust-bar risk resolved with structured explanation
The `"AS9100 Certified – Mission Assurance"` trust-bar from the Tier-2 source now has a structured PCB-stop explanation: certificate validity is time-limited and scope-specific; it cannot be assumed from a product page. This is more actionable than the previous blocked-claims list.

### 5. DO-254 DAL framing clarified
DAL assignment is now explicitly described as a safety-assessment outcome determined by the aircraft system integrator — PCB manufacturer can support a customer's DO-254 program requirements but cannot independently assert DAL level. This is a nuanced boundary not previously stated.

### 6. Seven common misreadings blocked with explanation
All seven misreadings have explanation sentences, including the two ITAR/EAR cases that were not previously covered in this depth.

---

## Blocked Claims (Maintained)

- AS9100 certificate status, scope, or OASIS registration
- DO-160G section-level test conditions or pass-status
- DO-254 DAL assignment or design-assurance compliance
- FAA TSO authorization for any device or PCB
- ARINC conformance proof
- ITAR/EAR compliance, license, exemption, ECCN, or export-control classification — COMPLETELY BLOCKED

---

## Residual Gaps

| Gap | Status | Reopen Condition |
|-----|--------|-----------------|
| Official AS9100D / OASIS registry source | Not recovered | SAE/IAQG OASIS page added to registry |
| Official FAA TSO index source | Not recovered | FAA TSO page added to registry |
| ITAR/EAR official source | Not recovered | DDTC/BIS source added (currently completely blocked) |
| Official ARINC 429/664 public metadata | Not recovered | ARINC standards page added to registry |
| DO-160G section-level vocabulary depth | Not recovered | Full DO-160G standard or clause-level FAA AC source |
| DO-254 DAL vocabulary depth | Not recovered | Full DO-254 standard or clause-level source |
| Promote wiki page draft → active | Not yet | Content review pass |

---

## Completion Status

**Status**: `completed`

**Completion definition met**:
- ✅ `facts/standards/civil-aerospace-assurance-boundary.md` created: 7 assurance families, governance-layer identification, PCB-stop lines, source coverage notes, blocked claims, remaining gaps
- ✅ `wiki/applications/civil-aerospace-assurance-routing-boundary.md` created (status `draft`): document-identity sentences per family, governance-layer reach, PCB-stop lines, routing table, must-refresh, 7 common misreadings
- ✅ DO-160G/DO-254/DO-155 source-backed identity correctly forwarded from existing altimeter standards card
- ✅ AS9100 trust-bar risk resolved with structured PCB-stop explanation
- ✅ DO-254 DAL framing nuance added (cannot independently assert DAL)
- ✅ ITAR/EAR complete block stated in 4 locations
- ✅ FAA TSO and ARINC identity vocabulary added (previously absent from corpus)
- ✅ Source registry gap acknowledged for all non-registry families
- ✅ Lane log created (this file)
- ✅ Blocked claims preserved
