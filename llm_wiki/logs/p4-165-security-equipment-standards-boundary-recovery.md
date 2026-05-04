# Lane Log: P4-165 Security Equipment Standards Boundary Recovery

## Task Metadata

| Field | Value |
|-------|-------|
| `task_id` | `p4-165-security-equipment-standards-boundary-recovery` |
| `lane` | `security equipment standards boundary recovery` |
| `status` | `completed` |
| `completed_at` | `2026-05-03` |
| `scope` | Create a reusable local standards-boundary pack that explains what fire alarm, intrusion alarm, access control, and IP video standard names mean and where PCB/PCBA content must stop |
| `write_scope` | `facts/standards/security-equipment-standards-boundary.md`, `wiki/applications/security-equipment-standards-and-routing-boundary.md`, `logs/p4-165-security-equipment-standards-boundary-recovery.md` |

---

## Problem Being Solved

After P4-161, the security equipment application boundary page blocked all standard-listing claims (UL 864, EN 54, EN 50131, ONVIF, etc.) correctly, but only as items in a blocked-claims list. This meant that:

1. Future agents encountering drafts with "EN 54" or "UL 864" had no local reasoning — they could block the claim but could not explain *why* or construct a safe alternative.
2. No local fact card described what these standards actually are at document-identity level.
3. Writers needed to rediscover the standard scope each time from scratch.

P4-165 converts the scattered blocked-claim notes into a reusable structured boundary pack: document-identity sentences, scope-reach explanation, and explicit PCB-stop lines for each of the four security-equipment standards families.

### Source Recovery Status

No official UL, CENELEC, IEC, or ONVIF source page is currently in the sources registry. The fact card and wiki page use **publicly known standards-identity metadata only** — document names, issuing bodies, and scope descriptions that are common knowledge in the security industry. This is the same pattern used for other identity-level boundary cards in the knowledge base. Sources must be added when official URLs are recovered and added to `sources/registry/standards/`.

---

## Inputs Read

| File | Role |
|------|------|
| `facts/applications/security-equipment-coverage-gap-map.md` | Full read — confirmed 4 remaining standards gaps (UL 864, EN 54, EN 50131/UL 2050, UL 294/EN 60839, ONVIF) |
| `wiki/applications/security-equipment-pcb-pcba-boundary-map.md` | Context — confirmed existing blocked-claims list structure |
| `facts/standards/automotive-medical-aerospace-application-qualification-boundary.md` | Format reference — identity-only boundary card pattern |

---

## Created Files

| File | Notes |
|------|-------|
| `facts/standards/security-equipment-standards-boundary.md` | **Created** — 4 standard families, identity table, PCB boundary for each, blocked claims, remaining gaps, no source_ids (sources not yet in registry) |
| `wiki/applications/security-equipment-standards-and-routing-boundary.md` | **Created**, status `draft` — detailed document-identity sentences, scope-reach, PCB-stop lines, routing table, must-refresh list, common misreadings |
| `logs/p4-165-security-equipment-standards-boundary-recovery.md` | **Created** — this lane log |

---

## Local Knowledge Landed

### 1. Four security standards families mapped at identity level

| Family | Standards Covered |
|--------|-----------------|
| Fire alarm | UL 864, EN 54 series, NFPA 72, BS 5839 |
| Intrusion alarm | EN 50131 (Grade 1–4), UL 2050, EN 50130-4 |
| Access control | UL 294, EN 60839-11, ANSI/SIA AC-01 |
| IP video / surveillance | ONVIF profiles (S/G/C/A/M/T), H.265/HEVC, H.264/AVC, RTSP |

### 2. PCB-stop lines explicit for each family
Each family has an explicit "where PCB vocabulary must stop" paragraph — safe board vocabulary is named, and then the listing/grading/conformance claim that belongs to the device/system level is named separately. This structure can be consumed directly by agent rewrites without re-reasoning.

### 3. Five common misreadings blocked with explanation
- `"EN 54 compliant"` → notified body testing of complete fire alarm system, not PCB.
- `"UL 864 listed"` → UL 864 listing belongs to the control unit as a complete product.
- `"ONVIF compatible PCB"` → device-firmware interoperability; PCB alone cannot hold ONVIF conformance.
- `"Grade 2 alarm PCB"` → EN 50131 grade is for the installed system.
- `"H.265 4K video PCB"` → SoC/firmware implementation, not PCB manufacturing.

### 4. Routing table covers all four segments plus lateral routes
Each of the four sub-segments now has a routing row pointing to both the application boundary page and this standards page, plus lateral routing to defense/EW and maker/smart-home pages.

---

## Blocked Claims (Maintained)

- UL listing number, UL file number, or UL category code claims
- EN 54, EN 50131, EN 60839, or other CENELEC certification mark claims
- ONVIF conformant device listing or ONVIF profile test result claims
- H.265/H.264 encoding performance, resolution, bitrate, or latency claims
- EN 50131 Grade assignment
- GDPR, CCPA, biometric/privacy-regulation compliance

---

## Residual Gaps

| Gap | Status | Reopen Condition |
|-----|--------|-----------------|
| Official UL 864 public source | Not recovered | UL standard page added to registry |
| Official EN 54 series public source | Not recovered | CENELEC/BSI page added to registry |
| Official ONVIF conformance profile docs | Not recovered | ONVIF public registry page added to registry |
| Official EN 50131 / UL 2050 source | Not recovered | Added to registry |
| Official UL 294 / EN 60839 source | Not recovered | Added to registry |
| Promote wiki page draft → active | Not yet | Content review pass |

---

## Completion Status

**Status**: `completed`

**Completion definition met**:
- ✅ `facts/standards/security-equipment-standards-boundary.md` created: 4 standards families, identity table per family, PCB-stop lines, blocked claims, remaining gaps
- ✅ `wiki/applications/security-equipment-standards-and-routing-boundary.md` created (status `draft`): document-identity sentences, scope-reach explanation, PCB-stop lines, routing table, must-refresh, 5 common misreadings
- ✅ UL 864 / EN 54 / EN 50131 / UL 2050 / UL 294 / EN 60839 / ONVIF all now have local identity-level framing
- ✅ PCB-stop boundary stated for all four security standard families
- ✅ Source registry gap acknowledged; card marked `source_ids: []` with explicit notes explaining why
- ✅ Routing table covers all four sub-segments plus lateral defense/EW and smart-home routes
- ✅ Lane log created (this file)
- ✅ Blocked claims preserved
