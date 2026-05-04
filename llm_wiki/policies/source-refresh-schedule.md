# Source Refresh Schedule Policy

**Policy ID**: `policy-source-refresh-schedule`
**Version**: 1.0
**Date**: 2026-05-02
**Status**: Active

---

## Purpose

Define refresh rules for `must_refresh: true` sources and facts to maintain data quality and prevent stale information from entering prompt consumption.

---

## Refresh Categories

### 1. Material Datasheets

| Source Type | Max Age | Refresh Trigger | Action |
|-------------|---------|-----------------|--------|
| Official manufacturer datasheet | 2 years | Annual review | Re-verify URL + values |
| Product page (web) | 1 year | Semi-annual check | Check page status |
| Obsolete product notice | Immediate | Alert on discovery | Update gap notes |

**Affected Fact Cards** (~200+ material facts):
- `materials-panasonic-megtron-*`
- `materials-isola-*`
- `materials-iteq-*`
- `materials-agc-*`
- `materials-ventec-*`
- All other `must_refresh: true` material facts

### 2. Commercial/Dynamic Claims

| Claim Type | Max Age | Refresh Trigger | Action |
|------------|---------|-----------------|--------|
| Lead time | 1 month | Monthly check | Exclude if stale |
| Cost/price | 1 month | Quote-stage only | Never promote as fact |
| MOQ | 1 month | Monthly check | Mark for refresh |
| Service status | 1 month | On-demand only | `must_refresh: true` |

**Blocked from Fact Cards**:
- Cost adders
- Turnaround promises
- Quote-stage specifics

### 3. Capability/Process Claims

| Claim Type | Max Age | Refresh Trigger | Action |
|------------|---------|-----------------|--------|
| HIL capability numbers | 6 months | Quarterly review | Exclude pending refresh |
| Registration tolerance | 6 months | Quarterly check | Exclude from evidence pack |
| Impedance tolerance | 6 months | Quarterly check | Exclude from evidence pack |

**Status**: B-class blocked - never enter facts without dated supplier record

### 4. Gap/Hold Tracking

| Gap Type | Check Frequency | Action |
|----------|-----------------|--------|
| Taconic RF | Monthly | Check 4taconic.com for RF laminate pages |
| Arlon RF/PTFE | Quarterly | Check arlonemd.com sitemap for CLTE/TC/AD series |
| Standards metadata | Quarterly | Check IPC/SAE for revision updates |

---

## Refresh Workflow

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Schedule       │────→│  Check Source   │────→│  Update Status  │
│  Trigger        │     │  URL + Content  │     │  (live/stale)   │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                        │
        ┌───────────────────────────────────────────────┘
        ▼
┌─────────────────┐     ┌─────────────────┐
│  Update Fact    │←────│  Source Changed?│
│  (if needed)    │ Yes └─────────────────┘
└─────────────────┘               │ No
        │                         ▼
        │                 ┌─────────────────┐
        │                 │  Extend Date    │
        │                 │  (last_checked) │
        │                 └─────────────────┘
        ▼
┌─────────────────┐
│  Log Update     │
│  (update-log.md)│
└─────────────────┘
```

---

## Fact Card Refresh Metadata

### Required Fields

```yaml
---
fact_id: "materials-example"
must_refresh: true

# Refresh metadata
refresh_schedule: "annual"           # annual | semi-annual | quarterly | monthly
last_checked: "2026-05-02"           # Last verification date
next_check_due: "2026-11-02"         # Next scheduled check
source_stability: "high"              # high | medium | low (URL stability)

# Source tracking
source_ids:
  - "example-datasheet"
  
source_verification:
  url_status: "live"                  # live | redirected | 404 | changed
  content_hash: "sha256:abc123"       # Optional: content fingerprint
  last_content_change: "2026-01-15"   # When source content last changed
---
```

### Refresh Status Values

| Status | Meaning | Action |
|--------|---------|--------|
| `current` | Source live, content unchanged | Continue use |
| `verified` | Re-checked, content confirmed | Update `last_checked` |
| `changed` | Source changed, needs review | Re-verify fact accuracy |
| `stale` | Past max age, not checked | Exclude from evidence packs |
| `unavailable` | Source 404/redirected | Mark gap, update notes |
| `deprecated` | Product discontinued | Update gap notes |

---

## Automated Refresh Triggers

### Time-Based Triggers

| Schedule | Target Facts | Action |
|----------|--------------|--------|
| Monthly | Material gaps (Taconic, Arlon) | URL status check |
| Quarterly | High-speed material datasheets | Re-verify + update dates |
| Semi-annual | All `must_refresh: true` facts | Full refresh cycle |
| Annual | Complete source registry audit | Comprehensive review |

### Event-Based Triggers

| Event | Action |
|-------|--------|
| New evidence pack request | Check all referenced facts are current |
| Source URL reported broken | Immediate verification + update |
| Manufacturer revision notice | Update affected facts |
| Product discontinuation notice | Update gap notes |

---

## Refresh Log Format

```markdown
## 2026-05-02 (Source Refresh Cycle)

### Material Datasheets Checked
- ✅ `panasonic-megtron-6-datasheet` - URL live, content unchanged
- ✅ `isola-370hr-datasheet` - URL live, content unchanged
- ⚠️ `iteq-it-180a-page` - Minor wording change, values confirmed
- ❌ `taconic-rf-35-product-page` - Still unavailable

### Gap Tracking Updated
- Taconic RF: No change (4taconic.com still industrial-only)
- Arlon CLTE-XT: Not in current sitemap

### Facts Updated
- Updated: `facts/materials/iteq-it-180a.md` (content_change noted)
- Extended: 45 material facts with new `last_checked` date
- Excluded: 0 facts (no stale data this cycle)
```

---

## Integration with Evidence Packs

### Pre-Flight Check

Before using a fact in evidence pack:

```yaml
# In evidence pack YAML
pre_flight_check:
  - fact_id: "materials-panasonic-megtron-6"
    last_checked: "2026-05-02"
    status: "current"              # Must be current or verified
    
  - fact_id: "materials-taconic-rf-35"
    status: "stale"                # ❌ Will not be included
    exclusion_reason: "Source unavailable, marked in gap notes"
```

### Evidence Pack Quality Gate

| Gate | Check |
|------|-------|
| All facts `last_checked` within max age | Block stale facts |
| No `unavailable` sources | Re-verify before use |
| No `changed` without review | Confirm accuracy first |

---

## File Locations

| Type | Path |
|------|------|
| This policy | `policies/source-refresh-schedule.md` |
| Refresh logs | `logs/refresh-cycles/` |
| Gap tracking | `facts/materials/*-gap.md` |
| Fact metadata | `facts/*/*.md` frontmatter |

---

## Related Documents

| Document | Relation |
|----------|----------|
| `policies/prompt-consumption-specification.md` | Evidence pack quality gates |
| `workflows/claim-inventory-to-consumption.md` | Stage 3 (Recovery) refresh handling |
| `logs/update-log.md` | Refresh cycle logging |

---

## Revision History

| Date | Version | Changes |
|------|---------|---------|
| 2026-05-02 | 1.0 | Initial refresh schedule policy (T24) |

---

*This policy ensures must_refresh data is proactively managed, not passively stale.*
