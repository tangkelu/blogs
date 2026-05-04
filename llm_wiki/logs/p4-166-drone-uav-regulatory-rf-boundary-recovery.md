# Lane Log: P4-166 Drone/UAV Regulatory And RF Boundary Recovery

## Task Metadata

| Field | Value |
|-------|-------|
| `task_id` | `p4-166-drone-uav-regulatory-rf-boundary-recovery` |
| `lane` | `drone/UAV regulatory and RF boundary recovery` |
| `status` | `completed` |
| `completed_at` | `2026-05-03` |
| `scope` | Create a reusable local regulatory and RF boundary pack for drone/UAV content so FAA Part 107, EASA UAS, FCC RF, CE RED, and GNSS/RTK vocabulary is bounded at document-identity level rather than only appearing in blocked-claims lists |
| `write_scope` | `facts/standards/drone-uav-regulatory-and-rf-boundary.md`, `wiki/applications/drone-uav-regulatory-routing-boundary.md`, `logs/p4-166-drone-uav-regulatory-rf-boundary-recovery.md` |

---

## Problem Being Solved

After P4-162, the drone/UAV application boundary page correctly blocked FAA Part 107, EASA UAS, FCC authorization, GNSS accuracy, and autonomy claims. But:

1. All blocked items were in a blocked-claims list — no local reasoning available to explain *why* or construct safe alternatives.
2. No local fact card described what FAA Part 107, EASA UAS categories, FCC Part 15/97, CE RED, or GNSS/RTK accuracy standards actually mean at document-identity level.
3. The existing `methods-remote-control-and-drone-control-stack-boundary` card covered PX4/MAVLink/ExpressLRS identity but not the regulatory/authorization layer.

P4-166 converts scattered blocked claims into a structured boundary pack: regulatory-framework identity sentences, scope-reach explanation, and PCB-stop lines for each regulatory family — so future agents can route correctly without rediscovering the regulatory scope from scratch.

### Source Recovery Status

No official FAA Part 107, EASA UAS, FCC Part 15/97, CE RED, or GNSS standard source is currently in the sources registry. The fact card uses **publicly known regulatory-identity metadata** — framework names, issuing bodies, and scope descriptions common knowledge in the drone industry. The four existing source_ids (`px4-basic-concepts-guide`, `mavlink-overview-page`, `expresslrs-getting-started`, `frontendapt-industry-drone-uav-page-en`) are included as the existing corpus foundation; they do not prove regulatory compliance claims. Official regulatory sources must be added when recovered.

---

## Inputs Read

| File | Role |
|------|------|
| `facts/applications/drone-uav-coverage-gap-map.md` | Full read — confirmed 4 remaining regulatory gaps (FAA Part 107, EASA, FCC/CE, GNSS/RTK) |
| `facts/methods/remote-control-and-drone-control-stack-boundary.md` | Partial read — confirmed PX4/MAVLink/ExpressLRS identity already established; this lane extends to regulatory/RF layer |
| `facts/standards/security-equipment-standards-boundary.md` | Format reference from P4-165 |

---

## Created Files

| File | Notes |
|------|-------|
| `facts/standards/drone-uav-regulatory-and-rf-boundary.md` | **Created** — 5 regulatory families (FAA Part 107, EASA UAS, FCC RF, CE RED, GNSS/RTK), identity table per family, PCB-stop lines, blocked claims, remaining gaps |
| `wiki/applications/drone-uav-regulatory-routing-boundary.md` | **Created**, status `draft` — document-identity sentences, scope-reach, PCB-stop lines per family, RC protocol identity extension, routing table, must-refresh list, 6 common misreadings |
| `logs/p4-166-drone-uav-regulatory-rf-boundary-recovery.md` | **Created** — this lane log |

---

## Local Knowledge Landed

### 1. Five regulatory families mapped at identity level

| Family | Frameworks Covered |
|--------|-------------------|
| FAA (US) | Part 107 (small UAS rules), Remote ID (14 CFR Part 89), operator registration |
| EASA (EU) | EU 2019/947 Open/Specific/Certified categories, EU 2019/945 CE class C0–C6 |
| FCC RF (US) | Part 15 (2.4/5.8/900 MHz unlicensed), Part 97 (amateur radio), FCC ID |
| CE RED (EU) | 2014/53/EU, EN 300 328, EN 301 893 harmonized standards |
| GNSS/RTK | GPS L1/L2/L5, GLONASS, BeiDou, Galileo, RTK, NTRIP |

### 2. PCB-stop lines explicit per family
Each regulatory family has a named "PCB-stop line" paragraph: safe board vocabulary is stated, then the authorization/certification/accuracy claim that belongs to the complete aircraft/device/operator level is named separately.

### 3. RC protocol identity extended from existing fact card
The `methods-remote-control-and-drone-control-stack-boundary` card's PX4/MAVLink/ExpressLRS identity table is reproduced in summary form in the wiki page, with an explicit pointer to the source fact card — no duplication, just cross-referencing.

### 4. Six common misreadings blocked with explanations
- `"FAA Part 107 compliant PCB"` → operational authorization, not PCB attribute
- `"EASA C2 class drone PCB"` → CE class marks the complete UAS product
- `"FCC certified RC receiver PCB"` → FCC ID authorizes the complete RF device
- `"RTK precision GNSS PCB"` → firmware + correction-service outcome, not PCB
- `"anti-jamming GNSS board"` → chipset/firmware feature, not PCB manufacturing
- `"2.4 GHz long-range PCB"` → system-level EIRP/link budget outcome, not PCB

### 5. Defense/civil-aerospace lateral routing confirmed
The routing table and related pages section explicitly routes defense UAV (MIL-STD, airworthiness) to the defense page and civil avionics DO-254 content to the civil aerospace page, preventing cross-contamination.

---

## Blocked Claims (Maintained)

- FAA Part 107 waiver, airspace authorization, registration claims
- EASA Open/Specific/Certified category authorization, CE class C0–C6
- FCC ID, Part 15/97 authorization for any RF device
- CE RED conformity or ETSI harmonized standard compliance
- GNSS accuracy (CEP, RMS, horizontal/vertical), RTK precision, fix rate, TTFF
- Anti-jamming, anti-spoofing performance
- RF range, EIRP, link budget, conducted power, spectral mask
- Autonomy, BVLOS, swarm-control performance

---

## Residual Gaps

| Gap | Status | Reopen Condition |
|-----|--------|-----------------|
| Official FAA Part 107 / Remote ID source | Not recovered | FAA regulatory page added to registry |
| Official EASA UAS regulation source | Not recovered | EASA regulation page added to registry |
| Official FCC Part 15 / FCC ID lookup source | Not recovered | FCC page added to registry |
| Official CE RED / ETSI harmonized standard source | Not recovered | EU RED or ETSI page added to registry |
| Official GPS.gov / ESA Galileo GNSS source | Not recovered | GPS.gov or ESA page added to registry |
| Promote wiki page draft → active | Not yet | Content review pass |

---

## Completion Status

**Status**: `completed`

**Completion definition met**:
- ✅ `facts/standards/drone-uav-regulatory-and-rf-boundary.md` created: 5 regulatory families, identity tables, PCB-stop lines, blocked claims, remaining gaps
- ✅ `wiki/applications/drone-uav-regulatory-routing-boundary.md` created (status `draft`): document-identity sentences, scope-reach per family, PCB-stop lines, RC protocol extension table, routing table, must-refresh, 6 common misreadings
- ✅ FAA Part 107, EASA UAS, FCC Part 15/97, CE RED, GNSS/RTK all have local identity-level framing
- ✅ Source registry gap acknowledged; existing source_ids from drone corpus included; notes explain missing official sources
- ✅ RC protocol identity linked to existing `methods-remote-control-and-drone-control-stack-boundary` (no duplication)
- ✅ Defense/civil-aerospace lateral routing explicit
- ✅ Lane log created (this file)
- ✅ Blocked claims preserved
