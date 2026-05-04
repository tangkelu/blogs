---
task_id: "p4-146-arlon-rf-ptfe-official-datasheet-monitor"
status: "completed"
owner: "cascade-subagent"
lane: "Arlon RF/PTFE official datasheet monitor"
input_paths:
  - /code/blogs/llm_wiki/facts/materials/arlon-rf-ptfe-current-site-gap.md
  - /code/blogs/llm_wiki/logs/p4-126-2026-5-2-taconic-arlon-rf-ptfe-current-site-recheck.md
  - /code/blogs/llm_wiki/logs/p4-116-2026-5-2-arlon-product-grade-source-recovery.md
  - /code/blogs/llm_wiki/logs/p4-143-taconic-arlon-rf-ptfe-detailed-recovery.md
  - /code/blogs/llm_wiki/facts/materials/arlon-detailed-material-specs-recovery.md
  - /code/blogs/llm_wiki/facts/materials/arlon-official-source-coverage.md
  - /code/blogs/llm_wiki/wiki/materials/arlon-material-family-source-governance.md
  - /code/blogs/llm_wiki/sources/registry/materials/arlon-*.md
  - /code/blogs/llm_wiki/sources/registry/internal/frontendapt-materials-arlon-pcb-page-en.md
output_paths:
  - /code/blogs/llm_wiki/facts/materials/arlon-official-source-coverage.md (UPDATED)
  - /code/blogs/llm_wiki/wiki/materials/arlon-material-family-source-governance.md (UPDATED)
  - /code/blogs/llm_wiki/logs/p4-146-arlon-rf-ptfe-monitor.md
write_scope:
  - /code/blogs/llm_wiki/sources/registry/materials/
  - /code/blogs/llm_wiki/facts/materials/
  - /code/blogs/llm_wiki/wiki/materials/
  - /code/blogs/llm_wiki/logs/p4-146-arlon-rf-ptfe-monitor.md
blocked_claims:
  - exact RF/PTFE product datasheet authority for CLTE-XT, TC350, AD250/300/1000, CuClad, DiClad, IsoClad
  - current Arlon/AGC product availability or lead times for RF/PTFE families
  - supplier capability proof for RF/PTFE families
  - numeric claims without current official source for RF/PTFE families
completed_at: "2026-05-03"
---

# P4-146 Arlon RF/PTFE Official Datasheet Monitor

## Scope

Monitor and consolidate the Arlon RF/PTFE official datasheet recovery state across prior lanes (P4-116, P4-126, P4-143), then land reusable local knowledge by updating the `arlon-official-source-coverage` fact card and the `arlon-material-family-source-governance` wiki page to reflect the full post-P4-143 state.

## Pre-Execution Collision Check

- Checked all `logs/p4-14*` files: no existing `p4-146-*` log found. Lane is clear.
- No collision detected.

## What Was Found (Prior-Lane Baseline)

### Official Source Status (2026-05-02, confirmed across P4-116 + P4-126)

| Family | Official Status |
|--------|----------------|
| 33N, 35N, 37N, 45N, 47N, 84N, 85N | ✅ Live official product pages at `arlonemd.com` |
| 55NT, 85NT | ✅ Live official product pages + datasheets |
| 86HP | ✅ Live official product page (2022-11-10) + datasheet (`86HP-v-1.6.pdf`, 2024/02 path) — recovered in P4-116 |
| CLTE-XT / CLTE-AT | ❌ Not in current official sitemap (2026-05-02) |
| TC350 / TC600 | ❌ Not in current official sitemap (2026-05-02) |
| AD250 / AD300 / AD1000 | ❌ Not in current official sitemap (2026-05-02) |
| CuClad / DiClad / IsoClad | ❌ Not in current official sitemap (2026-05-02) |

### Internal Recovery State (P4-143)

APTPCB internal JSON recovered exact Dk/Df/CTE/thermal specs for all RF/PTFE families:
- CLTE-XT: Dk 2.94, Df 0.0012 @ 10 GHz, Z-CTE 20 ppm/°C (copper-matched), thermal 0.45 W/m·K
- TC350: Dk 3.50, Df 0.0020, thermal 1.00 W/m·K (thermally enhanced)
- AD250: Dk 2.50, Df 0.0014, peel 12.0 lb/in
- AD1000: Dk 10.2, Df 0.0014
- CuClad/DiClad: Dk 2.17–2.60, Df 0.0009

These values are stored in `arlon-detailed-material-specs-recovery.md` as Tier-2 (internal-only) authority.

### Gap Identified

Both `arlon-official-source-coverage.md` (fact card) and `arlon-material-family-source-governance.md` (wiki page) were **stale** — written before P4-116 and P4-143. They:
- Did not reference the 86HP exact-product fact card
- Did not reference `arlon-detailed-material-specs-recovery` (CLTE-XT/TC350/AD/CuClad internal recovery)
- Did not establish a tier-based governance frame (official / internal / blocked)
- Did not incorporate the full source ID list from post-P4-116 source records (55NT/85NT datasheets, 86HP product page + datasheet, current product sitemap)

## Changes Made

### Updated: `facts/materials/arlon-official-source-coverage.md`

- New title reflecting three-tier coverage state
- `reviewed_at` updated to 2026-05-03, `confidence` raised to high
- Added 8 new `source_ids`: `arlon-current-product-sitemap`, `arlon-85n-datasheet`, `arlon-55nt-product-page`, `arlon-55nt-datasheet`, `arlon-85nt-product-page`, `arlon-85nt-datasheet`, `arlon-86hp-product-page`, `arlon-86hp-datasheet`
- New **Coverage State By Family** table: 9 rows mapping each family to official source status, fact card, and use tier
- Stable Facts updated to reflect 86HP, 55NT/85NT, and current RF/PTFE blocker
- Added **Related Fact Cards** section listing all 10 Arlon fact cards

### Updated: `wiki/materials/arlon-material-family-source-governance.md`

- `last_reviewed_at` updated to 2026-05-03
- `fact_ids` expanded from 2 to 12 (added: `hi-rel-branch-normalization`, `86hp-exact-product`, `85n-exact-product`, `85nt-exact-product`, `55nt`, `detailed-material-specs-recovery`, `rf-ptfe-current-site-gap`, `clte-xt-microwave`, `tc350-thermal-rf`, `ad-series-antenna`)
- `source_ids` expanded from 12 to 20 (added: `arlon-current-product-sitemap`, `arlon-85n-datasheet`, `arlon-55nt-product-page`, `arlon-55nt-datasheet`, `arlon-85nt-product-page`, `arlon-85nt-datasheet`, `arlon-86hp-product-page`, `arlon-86hp-datasheet`)
- Definition rewritten to express three-tier posture
- New **Source Tier Map** table: Tier 1 (official), Tier 2 (internal), Tier 3 (blocked)
- Stable Facts updated for 86HP, 55NT/85NT, and internal RF/PTFE recovery
- Engineering Boundaries, Common Misreadings, Must Refresh sections all updated
- Related Fact Cards section expanded to 11 entries

### No New Source Records Created

No new `sources/registry/materials/` records were warranted:
- The current official Arlon sitemap (2026-05-02) did not expose any new RF/PTFE product pages or datasheets for CLTE-XT, TC350, AD, or CuClad families.
- All new knowledge landed in this task is structural / aggregation rather than new raw source discovery.
- The prior lanes (P4-116, P4-126, P4-143) already created all justified source records.

## Blocked Claims (Maintained)

- ❌ Official Arlon/AGC datasheet authority for CLTE-XT, TC350, AD250/300/1000, CuClad, DiClad, IsoClad
- ❌ Current Arlon/AGC product-line continuity for RF/PTFE families
- ❌ Product availability, pricing, or lead times for RF/PTFE families
- ❌ External publication of CLTE-XT/TC350/AD/CuClad specs without source-gap pairing

## Residual Gaps

- Official Arlon/AGC RF/PTFE datasheets remain the primary open recovery target; monitor `arlonemd.com` sitemap for changes
- Whether AGC Inc. continues to produce these families under the Arlon brand is unconfirmed
- AGC / Arlon domain authority disambiguation (both `arlonemd.com` and `agcinc.com` branding) not yet resolved

## Task Status

**completed** — reusable local knowledge written to disk:
1. `facts/materials/arlon-official-source-coverage.md` (UPDATED — full three-tier coverage map, 86HP + 55NT/85NT + RF/PTFE blocker, 20 source IDs)
2. `wiki/materials/arlon-material-family-source-governance.md` (UPDATED — 12 fact IDs, 20 source IDs, three-tier governance frame, 11 related fact cards)
3. This lane log

All outputs within declared write scope. No shared trackers modified. No new source records created (none justified). Blocked claims maintained.
