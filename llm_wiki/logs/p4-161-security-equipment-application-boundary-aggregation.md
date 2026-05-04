# Lane Log: P4-161 Security Equipment Application Boundary Aggregation

## Task Metadata

| Field | Value |
|-------|-------|
| `task_id` | `p4-161-security-equipment-application-boundary-aggregation` |
| `lane` | `security equipment application boundary aggregation` |
| `status` | `completed` |
| `completed_at` | `2026-05-03` |
| `scope` | Create a dedicated civilian security-equipment routing lane so camera, access-control, alarm, and fire-system prompts stop collapsing into defense/EW or maker/smart-home overlap |
| `write_scope` | `facts/applications/security-equipment-coverage-gap-map.md`, `wiki/applications/security-equipment-pcb-pcba-boundary-map.md`, `logs/p4-161-security-equipment-application-boundary-aggregation.md` |

---

## Problem Being Solved

The P4-156 gap map classified security equipment as "Partial" — incidentally covered under `defense-ew-surveillance-targeting-pcb-review-boundaries.md`. This was correct at the time: civilian commercial security (IP cameras, access-control panels, alarm/fire systems, intercoms) is structurally different from military/defense ISR and EW but was sharing the same routing page.

The civilian security segment has a rich Tier-2 source with 6 distinct board families and clear commercial application context. Without a dedicated page, writers make three common mistakes:
1. Import MIL-STD vocabulary (from defense page) into civilian camera/alarm articles
2. Import consumer IoT framing (from maker/smart-home page) into commercial security panels
3. Treat security certification listings (UL 864, EN 50131, UL 294) as if they are supported by the Tier-2 source

The security segment also has the highest density of regulated certification vocabulary in routine commercial language — fire alarm panels (UL 864/EN 54), access control (UL 294/EN 60839), and intrusion alarms (EN 50131) are frequently cited but are system-level certifications that the PCB manufacturer cannot certify.

---

## Inputs Read

| File | Role |
|------|------|
| `facts/applications/application-coverage-gap-map.md` | Confirmed security as partial-overlap under defense page |
| `wiki/applications/defense-ew-surveillance-targeting-pcb-review-boundaries.md` | Existing page; confirmed security-equipment JSON is listed as a source but civilian security content is not the focus |
| `wiki/applications/maker-and-smart-home-platform-boundaries.md` | Secondary overlap boundary; consumer smart-home security vs commercial security |
| `/code/hileap/frontendAPT/public/static/industries/en/security-equipment-pcb.json` | Full Tier-2 source; 6 board families + FAQs read |
| `sources/registry/internal/frontendapt-industry-security-equipment-page-en.md` | Source registry record |

---

## Created Files

| File | Notes |
|------|-------|
| `facts/applications/security-equipment-coverage-gap-map.md` | **Created** — 6-family coverage state, defense vs civilian separation, certification gaps |
| `wiki/applications/security-equipment-pcb-pcba-boundary-map.md` | **Created** — per-family safe-angle + blocked-claim routing, 3-way routing decision table (civilian / defense / smart-home), 7 common misreadings |
| `logs/p4-161-security-equipment-application-boundary-aggregation.md` | **Created** — this lane log |

---

## Local Knowledge Landed

### 1. Three-way routing clarified
Civilian commercial security → this page. Military/defense ISR/EW → `defense-ew-surveillance-targeting-pcb-review-boundaries.md`. Consumer smart-home security → `maker-and-smart-home-platform-boundaries.md`. The routing decision table at the top of the wiki boundary page makes this explicit.

### 2. 6-family board taxonomy with civilian-security-specific framing
Control panel/central controller, video surveillance (camera/NVR/DVR), access control/smart lock, intrusion/perimeter sensors, fire alarm/gas/safety, and security power/backup/PoE. Each family has safe-angle + blocked-claim split with certification vocabulary explicitly bounded.

### 3. Fire alarm certification vocabulary bounded (highest risk)
UL 864, EN 54, NFPA 72 fire-alarm listing are system-level certifications; the PCB manufacturer does not hold these and cannot claim them. Fire PCB content must stay at "manufacturing support for customer-designed fire-alarm boards" framing.

### 4. Biometric / privacy vocabulary bounded
Biometric sensor module integration is safe board-class vocabulary. Recognition accuracy (FAR/FRR), liveness detection, and GDPR/CCPA compliance are blocked — they belong to the device maker and system integrator.

### 5. Trust-bar marketing labels bounded
`"24/7 Operation – Reliable"`, `"Long Service Life – Proven"`, `"Harsh Environments – Robust"` explicitly marked as marketing framing.

### 6. PoE vocabulary bounded
PoE front-end circuit design is safe board-class vocabulary. IEEE 802.3af/at/bt compliance is a system/chipset certification, not a PCB manufacturer claim.

---

## Blocked Claims (Maintained)

- EN 50131 grading, UL 2050/681 monitoring-station approval, or intrusion alarm certification
- UL 864, EN 54, NFPA 72 fire-alarm panel listing or life-safety approval
- UL 294, EN 60839 access-control compliance
- ONVIF conformance, H.265/H.264 encoding standard, or video analytics performance
- GDPR, CCPA, biometric data-privacy, or surveillance data-retention compliance
- 24/7 uptime, MTBF, DPPM, or field-failure rate claims
- Yield, throughput, cost, or lead-time claims

---

## Residual Gaps

| Gap | Status | Reopen Condition |
|-----|--------|-----------------|
| UL 864 / EN 54 fire-panel standard vocabulary depth | Not yet | Official UL/CENELEC source recovery |
| EN 50131 / UL 2050 intrusion-alarm standard vocabulary | Not yet | Official EN/UL source recovery |
| ONVIF video standard vocabulary | Not yet | Official ONVIF source recovery |
| EN 60839 / UL 294 access-control standard vocabulary | Not yet | Official EN/UL source recovery |
| Promote wiki page draft → active | Not yet | Content review pass |

---

## Completion Status

**Status**: `completed`

**Completion definition met**:
- ✅ `facts/applications/security-equipment-coverage-gap-map.md` created: 6-family coverage state, civilian vs defense separation, certification gap inventory
- ✅ `wiki/applications/security-equipment-pcb-pcba-boundary-map.md` created: per-family safe-angle + blocked-claim routing, 3-way routing decision table, standards context table, 7 common misreadings
- ✅ Civilian security no longer routes into defense/EW overlap; dedicated boundary page exists
- ✅ Fire alarm, access-control, and intrusion certification vocabulary explicitly blocked at listing/approval level
- ✅ Biometric and video analytics blocked at accuracy/privacy level
- ✅ Trust-bar marketing labels bounded as non-specification framing
- ✅ Three-way routing (civilian / defense / smart-home) clearly established
- ✅ Lane log created (this file)
- ✅ Blocked claims preserved
