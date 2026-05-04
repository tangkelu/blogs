# Lane Log: P4-155 RF Material Selector v2 — Taconic / Arlon Governance-Aware Expansion

## Task Metadata

| Field | Value |
|-------|-------|
| `task_id` | `p4-155-rf-material-selector-v2-taconic-arlon` |
| `lane` | `RF material selector v2 with Taconic / Arlon governance-aware expansion` |
| `status` | `completed` |
| `completed_at` | `2026-05-03` |
| `scope` | Expand the RF material selector fact card and wiki page to include Taconic and governance-aware Arlon RF/PTFE entries, keeping official vs. Tier-2 internal vs. blocked source boundaries explicit |
| `write_scope` | `facts/materials/`, `wiki/materials/`, `logs/p4-155-rf-material-selector-v2-taconic-arlon.md` |

---

## Problem Being Solved

The existing RF material selector (`facts/materials/rf-material-selector-by-application.md` and `wiki/materials/rf-material-selector-by-application-band.md`) explicitly noted in its `Limits And Non-Claims` section:

> "This first version still does not include Taconic alternatives."

And the ASSESSMENT.md weak-areas table listed:

> `RF material selector breadth | weak-medium | current selector wiki/fact still excludes Taconic and governance-aware Arlon/Tier-2 posture even after P4-143/P4-150`

Taconic and Arlon RF/PTFE material fact cards existed in `facts/materials/` from P4-143 work, but had not been wired into the selector. This lane bridges that gap.

---

## Inputs Read

| File | Role |
|------|------|
| `facts/materials/rf-material-selector-by-application.md` | Primary target for expansion |
| `wiki/materials/rf-material-selector-by-application-band.md` | Secondary target for expansion |
| `facts/materials/taconic-ptfe-laminate-family-parameters.md` | Full Taconic family parameter table (Tier-2) |
| `facts/materials/taconic-official-source-coverage-gap.md` | Source governance state for Taconic |
| `wiki/materials/taconic-material-family-source-governance.md` | Taconic three-tier source posture |
| `facts/materials/arlon-clte-xt-microwave.md` | Arlon CLTE-XT parameters (Tier-2) |
| `facts/materials/arlon-tc350-thermal-rf.md` | Arlon TC350/TC600 parameters (Tier-2) |
| `facts/materials/arlon-ad-series-antenna.md` | Arlon AD250/AD300/AD1000 parameters (Tier-2) |
| `facts/materials/arlon-official-source-coverage.md` | Arlon source coverage state |
| `wiki/materials/arlon-material-family-source-governance.md` | Arlon three-tier source posture |

---

## Changed Files

| File | Action | Notes |
|------|--------|-------|
| `facts/materials/rf-material-selector-by-application.md` | **Updated** | See detail below |
| `wiki/materials/rf-material-selector-by-application-band.md` | **Updated** | See detail below |
| `logs/p4-155-rf-material-selector-v2-taconic-arlon.md` | **Created** | This lane log |

---

## Detail: Changes to `rf-material-selector-by-application.md`

### Frontmatter
- `reviewed_at`: `2026-04-24` → `2026-05-03`
- `source_ids`: Added `frontendapt-taconic-pcb-json`, `frontendapt-arlon-pcb-json`
- `tags`: Added `taconic`, `arlon`

### Stable Facts
Added 6 new Tier-2-tagged stable facts covering:
- Taconic TLY (ultra-low-loss), RF-35A2 (Dk 3.50, Df 0.0018, 51% lower loss than RO4350B), CER-10/20/30 (high-Dk compact)
- Arlon CLTE-XT (Df 0.0012, low-PIM), TC350 (1.0 W/m·K thermal), AD series (AD1000 Dk 10.2)

### Application Mapping
Added `Also consider [Tier-2]` sub-bullets to 8 of the 10 application buckets:
- Mixed digital + RF sub-6 → Taconic RF-35A2
- Sub-6 to tens of GHz low-loss → Taconic TLX-8, Arlon CLTE-XT
- 24–40 GHz RF front ends → Taconic TLY-5A
- 77 GHz mmWave → Taconic TLY-5A
- Compact resonators → Taconic CER-10/20/30, Arlon AD1000
- High-volume antennas / PIM-sensitive → Arlon CLTE-XT, Taconic RF-35A2
- Satellite / GPS / filters → Taconic TLY-5A, CER-10, Arlon AD250/300
- Power RF / PA / thermoset → Arlon TC350, Taconic TF-260/290
- High-power heat spreading → Arlon TC350, Taconic TF-260/290

### Limits And Non-Claims
- Removed stale "This first version still does not include Taconic alternatives" note
- Added explicit Tier-2 governance boundaries for Taconic and Arlon RF/PTFE families
- Added PTFE plasma desmear fabricator-capability warning (Taconic TLY, Arlon CLTE-XT)

### Open Questions
- Updated from "add Taconic" → "confirm official Taconic/Arlon URLs" and "add dedicated antenna/PA/satcom card"

---

## Detail: Changes to `rf-material-selector-by-application-band.md`

### Frontmatter
- `status`: `draft` → `active`
- `last_reviewed_at`: `2026-04-24` → `2026-05-03`
- `fact_ids`: Added 13 Taconic and Arlon fact card IDs
- `source_ids`: Added `frontendapt-taconic-pcb-json`, `frontendapt-arlon-pcb-json`
- `tags`: Added `taconic`, `arlon`

### Stable Facts
Restructured into three sub-sections:
1. **Official-Source-Backed Entries (Tier 1)** — existing Rogers/Isola/Panasonic/Ventec/AGC content, unchanged
2. **Taconic Additions — Tier-2 Internal Only** — 8 application bullets with Tier-2 disclaimer blockquote
3. **Arlon Additions — Tier-2 Internal Only (RF/PTFE Families)** — 4 application bullets with Tier-2 disclaimer blockquote

### Source Tier Governance (new section)
Added 3-row table mapping tiers to entry sets and external publishability.

### Common Misreadings
Added 2 new entries:
- Taconic RF-35A2 and RO4350B matched Dk ≠ drop-in substitute (different fabrication chemistry)
- Tier-2 entries in selector ≠ officially validated; source-gap pairing required for external publication

### Related Fact Cards
Expanded from 11 to 21 entries, including all Taconic and Arlon RF/PTFE fact cards and governance wiki links.

---

## Local Knowledge Landed

### 1. Taconic integration into RF selector
Taconic's 8-family portfolio (TLY, TLX, TLC, RF-35, CER, TF, fastRise, TacLam) is now wired into the selector with application mappings, Tier-2 governance warnings, and explicit blocked-publication instructions.

### 2. Arlon RF/PTFE integration into RF selector
Arlon's 3 RF/PTFE families (CLTE-XT, TC350/600, AD series) are now wired into the selector. N-series and 86HP were already official-backed and are unaffected.

### 3. Taconic RF-35A2 vs RO4350B disambiguation
Critical misreading now explicitly blocked: same Dk does not mean same fabrication route. RF-35A2 = PTFE plasma; RO4350B = FR-4 chemistry.

### 4. Wiki page promoted to `active`
`rf-material-selector-by-application-band.md` was `draft`; now `active` with complete Tier-1 + Tier-2 coverage.

---

## Blocked Claims (Maintained)

All original claims preserved plus new additions:
- Official Taconic/Arlon datasheet authority where no current public product page exists
- External publication of Tier-2-only numeric claims without source-gap pairing
- Universal frequency-band-to-material prescriptions
- Availability, lead-time, and pricing claims
- PIM performance guarantees (depends on fabrication quality)
- Exact thermal performance values without specific assembly and thermal design context

---

## Residual Gaps

| Gap | Status | Reopen Condition |
|-----|--------|-----------------|
| Official Taconic RF product pages | Not recovered | Reopen if official `4taconic.com` or ADD domain RF laminate pages become accessible |
| Official Arlon CLTE-XT/TC350/AD pages | Not recovered | Reopen if `arlonemd.com` publishes live product pages for RF/PTFE families |
| Dedicated antenna-array / PA / satcom application card | Not yet created | Low priority; build after official source anchors improve |
| Rogers Ro3010 fact card | Not in fact_ids of selector | Minor; Ro3010 is used in source_ids but lacks a standalone fact card |

---

## Completion Status

**Status**: `completed`

**Completion definition met**:
- ✅ `rf-material-selector-by-application.md` expanded: Taconic + Arlon entries added with Tier-2 governance labels
- ✅ `rf-material-selector-by-application-band.md` expanded: three sub-sections, Source Tier Governance table, new misreadings, expanded related cards
- ✅ Wiki status upgraded from `draft` to `active`
- ✅ "This version still does not include Taconic" stale note removed
- ✅ All Tier-2 governance boundaries explicit and paired with source-gap warnings
- ✅ Lane log created (this file)
- ✅ Blocked claims preserved and expanded
