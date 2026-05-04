# Lane Log: P4-163 Civil Aerospace Application Boundary Aggregation

## Task Metadata

| Field | Value |
|-------|-------|
| `task_id` | `p4-163-civil-aerospace-application-boundary-aggregation` |
| `lane` | `civil aerospace application boundary aggregation` |
| `status` | `completed` |
| `completed_at` | `2026-05-03` |
| `scope` | Create a dedicated civil-aerospace routing layer so non-defense avionics, civil navigation, and aircraft-system prompts stop borrowing defense-only vocabulary as if it were program approval |
| `write_scope` | `facts/applications/civil-aerospace-coverage-gap-map.md`, `wiki/applications/civil-aerospace-pcb-pcba-boundary-map.md`, `logs/p4-163-civil-aerospace-application-boundary-aggregation.md` |

---

## Problem Being Solved

The P4-156 gap map classified civil aerospace as "Partial" — covered through `defense-ew-surveillance-targeting-pcb-review-boundaries.md`. The problem is structural: the defense page covers EW, ISR, radar, and guided systems using MIL-STD vocabulary. Civil aviation (commercial aircraft avionics, civil navigation, air traffic electronics) is a different regulatory world — FAA, DO-160G, DO-254, AS9100, ARINC — and it was being served by the wrong routing page.

Two additional complications:

1. **AS9100 trust-bar in Tier-2 source**: The aerospace-defense JSON SEO metadata explicitly says `"AS9100 compliance"` and the trust bar says `"AS9100 Certified – Mission Assurance"`. This is the highest-risk trust-bar label in the entire Tier-2 corpus — it sounds like a current certificate but is marketing framing. Without a dedicated boundary page, writers would import this as a certifiable claim.

2. **DO-160G / DO-254 vocabulary**: Both standards are in the sources registry at identity-metadata level only (via `standards-aviation-altimeter-standards-metadata-boundary`). Without a dedicated routing page, writers use DO-160G and DO-254 as if they prove qualification pass-status or DAL assignment.

A dedicated civil aerospace page separates this content from defense, binds the AS9100 trust-bar risk explicitly, and routes altimeter-specific content to the existing process page.

---

## Inputs Read

| File | Role |
|------|------|
| `facts/applications/application-coverage-gap-map.md` | Confirmed civil aerospace as partial-overlap under defense page |
| `wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md` | Existing page; aerospace-defense JSON listed as source; focus is defense/EW |
| `facts/standards/aviation-altimeter-standards-metadata-boundary.md` | DO-160G, DO-254, DO-155 identity-only boundary; key input |
| `facts/standards/automotive-medical-aerospace-application-qualification-boundary.md` | FAA AC 20-152A, AS9102 boundary; key input |
| `wiki/processes/altimeter-aviation-standards-and-assurance-boundaries.md` | Altimeter process page; informed cross-routing |
| `/code/hileap/frontendAPT/public/static/industries/en/aerospace-defense-pcb.json` | Full Tier-2 source; 5 board-family sections + FAQs read |
| `sources/registry/internal/frontendapt-industry-aerospace-defense-page-en.md` | Source registry record |

---

## Created Files

| File | Notes |
|------|-------|
| `facts/applications/civil-aerospace-coverage-gap-map.md` | **Created** — 5-family coverage state, AS9100 trust-bar governance note, aviation standards layer inventory, limits and gaps |
| `wiki/applications/civil-aerospace-pcb-pcba-boundary-map.md` | **Created** — per-family safe-angle + blocked-claim routing, 4-way routing decision table, standards context table, 7 common misreadings, AS9100 trust-bar explicitly bounded |
| `logs/p4-163-civil-aerospace-application-boundary-aggregation.md` | **Created** — this lane log |

---

## Local Knowledge Landed

### 1. AS9100 trust-bar explicitly bounded — highest-risk item
`"AS9100 Certified – Mission Assurance"` trust-bar is marketing framing only. It appears in both the wiki boundary page definition section, the engineering boundaries section, and the common misreadings section. Three explicit placements to ensure agents do not import it as a certification claim.

### 2. Four-way routing established
Civil aviation → this page. Defense/military aviation (EW/ISR/radar/guided systems) → defense page. Altimeter-specific slugs (DO-155/radio/barometric/laser) → altimeter process page. Civilian UAV → drone page. The routing table is at the top of the wiki boundary page.

### 3. Aviation standards bounded at correct level
DO-160G: document-family identity + FAA AC 21-16G recognition context only — no section-level test or pass-status. DO-254: design-assurance guidance identity + circuit-board-assembly scope only — no DAL assignment. AS9102: FAI documentation context only — no process-capability proof. AS9100: identity-only — no certificate, no OASIS listing.

### 4. ITAR/EAR completely blocked
ITAR and EAR are completely outside the source corpus. Any export-control compliance language requires refresh. This is stated in three places: the standards context table, engineering boundaries, and must-refresh list.

### 5. Redundancy vocabulary bounded
"Redundant channel, voting logic" vocabulary is framed as customer-design support only — NOT safety-function certification, DO-178C software assurance, or FMEA/FMECA outcome proof.

---

## Blocked Claims (Maintained)

- AS9100 certification status, scope, or OASIS registration
- DO-160G section-level test conditions or qualification pass-status
- DO-254 DAL assignment or design-assurance compliance
- Airworthiness, TSO authorization, STC, or FAA approval
- ITAR, EAR, or export-control compliance
- MIL-STD, defense-program, or weapons-system qualification
- RF performance, data-link (ARINC 429/664) conformance
- RTCA minimum-performance-standard claims
- Mission reliability, MTBF, or program-history claims
- Yield, throughput, cost, or lead-time claims

---

## Residual Gaps

| Gap | Status | Reopen Condition |
|-----|--------|-----------------|
| AS9100 current certificate / OASIS listing vocabulary | Not yet | Official AS9100 certificate record or OASIS listing source |
| DO-160G section-level test vocabulary | Not yet | Full DO-160G standard or clause-level FAA AC source |
| DO-254 DAL / design-assurance vocabulary | Not yet | Full DO-254 standard or clause-level source |
| ITAR / EAR export-control boundary | Not yet | Official ITAR/EAR source (currently completely outside corpus) |
| TSO authorization vocabulary | Not yet | Official FAA TSO source recovery |
| Promote wiki page draft → active | Not yet | Content review pass |

---

## Completion Status

**Status**: `completed`

**Completion definition met**:
- ✅ `facts/applications/civil-aerospace-coverage-gap-map.md` created: 5-family coverage state, AS9100 trust-bar governance note, aviation standards layer inventory, limits and remaining gaps
- ✅ `wiki/applications/civil-aerospace-pcb-pcba-boundary-map.md` created: per-family safe-angle + blocked-claim routing, 4-way routing decision table, complete standards context table, 7 common misreadings
- ✅ Civil aerospace no longer routes into defense overlap; dedicated boundary page exists
- ✅ AS9100 trust-bar explicitly bounded in 3 locations (definition, engineering boundaries, common misreadings)
- ✅ DO-160G / DO-254 bounded at identity-metadata level only (no section, no DAL)
- ✅ ITAR/EAR completely blocked and stated in three places
- ✅ Four-way routing (civil aviation / defense / altimeter slugs / civilian UAV) established
- ✅ Integration with existing altimeter process page and standards fact cards via cross-routing
- ✅ Lane log created (this file)
- ✅ Blocked claims preserved
