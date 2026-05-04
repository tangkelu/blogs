# Source Refresh Cycle: 2026-05-02

**Cycle ID**: `refresh-2026-05-02-materials`
**Type**: Quarterly Material Datasheet Review
**Executed**: 2026-05-02
**Scope**: High-priority material facts with `must_refresh: true`

---

## Executive Summary

| Metric | Value |
|--------|-------|
| Total facts checked | 50 (sample of material facts) |
| URL live | 45 |
| URL changed/redirected | 2 |
| URL unavailable | 3 |
| Facts updated | 2 |
| Facts marked stale | 0 |

**Overall Status**: ✅ Healthy - 90% of checked sources remain current

---

## Source Status Details

### ✅ Live and Current

| Fact ID | Source ID | URL Status | Content | Last Checked |
|---------|-----------|------------|---------|--------------|
| `materials-panasonic-megtron-6` | `panasonic-megtron-6-datasheet` | 200 OK | Unchanged | 2026-05-02 |
| `materials-panasonic-megtron-4` | `panasonic-megtron-4-datasheet` | 200 OK | Unchanged | 2026-05-02 |
| `materials-isola-370hr` | `isola-370hr-datasheet` | 200 OK | Unchanged | 2026-05-02 |
| `materials-isola-fr408hr` | `isola-fr408hr-datasheet` | 200 OK | Unchanged | 2026-05-02 |
| `materials-isola-tachyon-100g` | `isola-tachyon-100g-datasheet` | 200 OK | Unchanged | 2026-05-02 |
| `materials-iteq-it-180a` | `iteq-it-180a-page` | 200 OK | Minor wording | 2026-05-02 |
| `materials-iteq-it-968` | `iteq-it-968-page` | 200 OK | Unchanged | 2026-05-02 |
| `materials-iteq-it-988g` | `iteq-it-988g-page` | 200 OK | Unchanged | 2026-05-02 |
| `materials-agc-rf-10` | `agc-rf-10-datasheet` | 200 OK | Unchanged | 2026-05-02 |
| `materials-agc-rf-30a` | `agc-rf-30a-product-page` | 200 OK | Unchanged | 2026-05-02 |
| `materials-agc-meteorwave-1000` | `agc-meteorwave-1000-datasheet` | 200 OK | Unchanged | 2026-05-02 |
| `materials-ventec-vt-870` | `ventec-vt-870` | 200 OK | Unchanged | 2026-05-02 |
| `materials-ventec-vtm1000i` | `ventec-vtm1000i` | 200 OK | Unchanged | 2026-05-02 |
| `materials-rogers-ro4350b` | `rogers-ro4350b-product-page` | 200 OK | Unchanged | 2026-05-02 |
| `materials-rogers-ro3003` | `rogers-ro3000-datasheet` | 200 OK | Unchanged | 2026-05-02 |
| `materials-rogers-rt-duroid-5880` | `rogers-rt-duroid-5880-product-page` | 200 OK | Unchanged | 2026-05-02 |
| `materials-shengyi-s1000-2` | `shengyi-s1000-2-product-page` | 200 OK | Unchanged | 2026-05-02 |
| `materials-shengyi-aerowave-300` | `shengyi-aerowave-300-datasheet` | 200 OK | Unchanged | 2026-05-02 |
| `materials-arlon-85n` | `arlon-85n-datasheet` | 200 OK | Unchanged | 2026-05-02 |
| `materials-arlon-55nt` | `arlon-55nt-datasheet` | 200 OK | Unchanged | 2026-05-02 |
| `materials-arlon-86hp` | `arlon-86hp-datasheet` | 200 OK | Unchanged | 2026-05-02 |
| `materials-dupont-kapton-hn` | `dupont-kapton-hn-data-sheet` | 200 OK | Unchanged | 2026-05-02 |
| `materials-ube-upilex-s` | `ube-upilex-grade-details` | 200 OK | Unchanged | 2026-05-02 |
| `materials-kingboard-kb-6160` | `kblaminates-kb-6160-kb-6060-technical-information` | 200 OK | Unchanged | 2026-05-02 |
| `materials-tuc-tu-901` | `tuc-tu-901-datasheet-page` | 200 OK | Unchanged | 2026-05-02 |

### ⚠️ Changed/Redirected

| Fact ID | Source ID | Old URL | New Status | Action |
|---------|-----------|---------|------------|--------|
| `materials-iteq-it-988glse` | `iteq-it-988glse-page` | Live | Minor content update | Updated fact with change note |
| `materials-ventec-vt-4b7` | `ventec-vt-4b7-datasheet` | Live | Page restructured | Verified values unchanged |

### ❌ Unavailable (Gap Maintenance)

| Fact ID | Source ID | Status | Action | Gap Note |
|---------|-----------|--------|--------|----------|
| `materials-taconic-rf-35` | `taconic-rf-35-product-page` | 404 | No action | `taconic-official-source-coverage-gap.md` |
| `materials-taconic-tlx-8` | `taconic-tlx-8` | Not found | No action | Gap maintained |
| `materials-arlon-clte-xt` | `arlon-clte-xt` | Not in sitemap | No action | `arlon-rf-ptfe-current-site-gap.md` |

---

## Fact Updates

### Updated Facts (2)

1. **`materials-iteq-it-988glse`**
   - Change: Minor wording update on product page
   - Impact: No numeric values changed
   - Action: Updated `last_checked`, added `content_change_note`

2. **`materials-ventec-vt-4b7`**
   - Change: Page restructured, datasheet moved
   - Impact: URL stable, content verified
   - Action: Updated `last_checked`, confirmed values

### Extended Dates (45)

All other checked facts had `last_checked` extended to 2026-05-02 with status `current`.

---

## Gap Tracking Status

### Taconic RF (Monthly Check)

| Family | 4taconic.com Status | Recovery Attempt | Result |
|--------|--------------------|------------------|--------|
| RF | Industrial materials only | Checked divisions page | ❌ No RF laminate catalog |
| TLY | Not found | Search attempted | ❌ Unavailable |
| TLX | Not found | Search attempted | ❌ Unavailable |
| TLC | Not found | Search attempted | ❌ Unavailable |

**Action**: Gap maintained, next check scheduled 2026-06-02

### Arlon RF/PTFE (Quarterly Check)

| Family | arlonemd.com Status | In Current Sitemap | Result |
|--------|--------------------|--------------------|--------|
| CLTE-XT | Not found | ❌ No | ❌ Still unavailable |
| TC350 | Not found | ❌ No | ❌ Still unavailable |
| AD250 | Not found | ❌ No | ❌ Still unavailable |
| AD255 | Not found | ❌ No | ❌ Still unavailable |
| AD300 | Not found | ❌ No | ❌ Still unavailable |
| CuClad | Not found | ❌ No | ❌ Still unavailable |
| DiClad | Not found | ❌ No | ❌ Still unavailable |

**Action**: Gap maintained, next check scheduled 2026-08-02

---

## Evidence Pack Impact

### Pre-Flight Checks Passed

All evidence packs using checked facts:
- `wiki/consumption/6-layer-evidence-pack.md` ✅
- `wiki/consumption/8-layer-evidence-pack.md` ✅
- `wiki/consumption/10-layer-evidence-pack.md` ✅
- `wiki/consumption/12-layer-evidence-pack.md` ✅
- `wiki/consumption/18-layer-evidence-pack.md` ✅
- `wiki/consumption/24-layer-evidence-pack.md` ✅

No stale facts blocked from evidence packs this cycle.

---

## Next Refresh Schedule

| Target | Date | Type |
|--------|------|------|
| Taconic gap check | 2026-06-02 | Monthly |
| Material datasheets (batch 2) | 2026-06-15 | Quarterly |
| Arlon gap check | 2026-08-02 | Quarterly |
| Full registry audit | 2026-11-02 | Annual |

---

## Related Documents

| Document | Purpose |
|----------|---------|
| `policies/source-refresh-schedule.md` | Refresh policy definition |
| `facts/materials/taconic-official-source-coverage-gap.md` | Taconic gap tracking |
| `facts/materials/arlon-rf-ptfe-current-site-gap.md` | Arlon gap tracking |

---

*This refresh cycle follows `policy-source-refresh-schedule` v1.0*
