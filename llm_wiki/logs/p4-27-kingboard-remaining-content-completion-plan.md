# P4-27 Kingboard Remaining Content Completion Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development for parallel source-recovery lanes, or superpowers:executing-plans if running inline. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Finish the remaining `/code/blogs/tmps/en` Kingboard material ingestion by recovering official sources where possible, adding exact-product facts only when source-backed, building a safe selector layer, and keeping unsupported commercial / capability / SI claims blocked.

**Architecture:** Treat blog drafts as claim inventories only. Official KBLaminates / Kingboard PDFs and pages create source records first; facts are created only from those sources; selector and prepreg pages consume facts without introducing new numbers. Blocked products stay explicitly blocked rather than silently inherited from adjacent suffixes.

**Tech Stack:** Markdown source registry, Markdown fact cards, `llm_wiki/logs` control documents, `rg`, `git diff --check`, source/fact ID consistency checks.

---

## Current State

Already source-backed in `P4-26`:

- `KB-6150`
- `KB-6160`
- `KB-6164`
- `KB-6165`
- `KB-6165F`
- `KB-6167F`
- `HF-140`
- `HF-170`
- `KB-3200G`
- `PI-520G`

Still not source-backed at exact-product level:

- `KB-6160A`
- `KB-6160F`
- `KB-6160LC`
- `KB-6160LC(C)`
- `KB-6165C`
- `KB-6165LE`
- `KB-6167GMD`
- `KB-6167GLD`
- `KB-6168LE`
- `KB-6169GT`
- `PI-515G`

Cross-cutting layers still missing:

- Kingboard selector / tier normalization layer.
- Prepreg construction table extraction for covered products.
- Processing-guide boundary layer beyond `KB-6160`.
- Final completion map showing which `/tmps/en` drafts are fully learned, partially learned, or blocked.

## File Structure

Create:

- `llm_wiki/logs/p4-27-kingboard-remaining-content-completion-plan.md`: this plan.
- `llm_wiki/logs/p4-28-kingboard-residual-source-recovery.md`: execution log for remaining exact-product source recovery.
- `llm_wiki/facts/materials/kingboard-material-selection-boundaries.md`: safe selector/tier normalization fact.
- `llm_wiki/facts/materials/kingboard-prepreg-construction-data-boundaries.md`: prepreg table usage guardrail.
- `llm_wiki/wiki/materials/kingboard-laminate-selection-and-boundaries.md`: topic wiki page for prompt consumption.

Create conditionally, only when official source exists:

- `llm_wiki/sources/registry/materials/kblaminates-kb-6160a-technical-information.md`
- `llm_wiki/sources/registry/materials/kblaminates-kb-6160f-kb-6060f-technical-information.md`
- `llm_wiki/sources/registry/materials/kblaminates-kb-6160lc-kb-6060lc-technical-information.md`
- `llm_wiki/sources/registry/materials/kblaminates-kb-6165c-kb-6065c-technical-information.md`
- `llm_wiki/sources/registry/materials/kblaminates-kb-6165le-kb-6065le-technical-information.md`
- `llm_wiki/sources/registry/materials/kblaminates-kb-6167gmd-technical-information.md`
- `llm_wiki/sources/registry/materials/kblaminates-kb-6167gld-technical-information.md`
- `llm_wiki/sources/registry/materials/kblaminates-kb-6168le-technical-information.md`
- `llm_wiki/sources/registry/materials/kblaminates-kb-6169gt-technical-information.md`
- `llm_wiki/sources/registry/materials/kblaminates-pi-515g-technical-information.md`

Create conditionally, only when matching source exists:

- `llm_wiki/facts/materials/kingboard-kb-6160a.md`
- `llm_wiki/facts/materials/kingboard-kb-6160f.md`
- `llm_wiki/facts/materials/kingboard-kb-6160lc.md`
- `llm_wiki/facts/materials/kingboard-kb-6165c.md`
- `llm_wiki/facts/materials/kingboard-kb-6165le.md`
- `llm_wiki/facts/materials/kingboard-kb-6167gmd.md`
- `llm_wiki/facts/materials/kingboard-kb-6167gld.md`
- `llm_wiki/facts/materials/kingboard-kb-6168le.md`
- `llm_wiki/facts/materials/kingboard-kb-6169gt.md`
- `llm_wiki/facts/materials/kingboard-pi-515g.md`

Modify:

- `llm_wiki/logs/update-log.md`
- `llm_wiki/logs/backlog.md`
- `llm_wiki/logs/phase-status.md`
- `llm_wiki/logs/p4-25-kingboard-material-blog-ingestion-map.md`
- `llm_wiki/logs/p4-26-kingboard-official-source-recovery.md`

## Execution Contract

- Never use `/code/blogs/tmps/en/*.md` as a source for numeric facts.
- Every numeric product fact must cite an official KBLaminates / Kingboard source record.
- If official source is not found, add the product to the blocked table with the exact failed search pattern.
- Do not infer suffix values from adjacent products.
- Do not turn product material data into finished-board compliance, channel compliance, cost, lead-time, yield, inventory, supplier relationship, or HIL/APT capability claims.
- Do not convert processing-guide examples into universal recipes.

---

### Task 1: Residual Official-Source Search Matrix

**Files:**

- Create: `llm_wiki/logs/p4-28-kingboard-residual-source-recovery.md`
- Modify: `llm_wiki/logs/update-log.md`
- Modify: `llm_wiki/logs/backlog.md`
- Modify: `llm_wiki/logs/phase-status.md`

- [ ] **Step 1: Build the search matrix**

Use independent lanes for:

- Lane A: `KB-6160A`, `KB-6160F`, `KB-6160LC`, `KB-6160LC(C)`
- Lane B: `KB-6165C`, `KB-6165LE`
- Lane C: `KB-6167GMD`, `KB-6167GLD`, `KB-6168LE`, `KB-6169GT`
- Lane D: `PI-515G`

Search patterns:

```text
site:kblaminates.com "KB-6160A"
site:kblaminates.com "KB-6160F"
site:kblaminates.com "KB-6160LC"
site:kblaminates.com "KB-6165C"
site:kblaminates.com "KB-6165LE"
site:kblaminates.com "KB-6167GMD"
site:kblaminates.com "KB-6167GLD"
site:kblaminates.com "KB-6168LE"
site:kblaminates.com "KB-6169GT"
site:kblaminates.com "PI-515G"
site:kblaminates.com/upload/ueditor/20250313 "KB-6167GLD"
site:kblaminates.com/upload/ueditor/20250313 "KB-6169GT"
```

- [ ] **Step 2: Classify every product**

Use this table shape in `p4-28`:

```markdown
| Product | Official source found | Source URL | Disposition | Notes |
| --- | --- | --- | --- | --- |
| KB-6160A | yes/no | URL or blank | source_recovered / still_blocked | exact reason |
```

- [ ] **Step 3: Stop condition**

Only products with a reachable official URL move to Task 2. Products without official URLs remain blocked.

### Task 2: Conditional Source Records For Recovered Products

**Files:**

- Create conditionally under `llm_wiki/sources/registry/materials/`

- [ ] **Step 1: Create one source record per recovered official document**

Use this exact source record shape:

```markdown
---
source_id: "kblaminates-product-slug-technical-information"
title: "PRODUCT Technical Information"
organization: "Kingboard Laminates / KBLaminates"
source_type: "datasheet"
url: "OFFICIAL_URL"
jurisdiction: "global"
published_at: ""
checked_at: "2026-04-27"
trust_tier: "t1"
stability: "semi_stable"
must_refresh: false
topic_tags: ["kingboard", "kblaminates", "product-slug", "datasheet"]
status: "active"
notes: "Official KBLaminates technical-information source. Values must remain exact-product scoped."
---

# Source Summary

## What It Covers

- Exact product identity
- Thermal, electrical, and mechanical material values where listed
- IPC / UL / specimen notes where listed

## Why It Matters

- Allows this product to move from draft-only claim inventory into source-scoped fact coverage.

## Extraction Notes

- Keep product suffix attached.
- Keep method, condition, frequency, and specimen scope attached.
- Do not infer values for adjacent suffixes.

## Refresh Notes

- Re-check if KBLaminates republishes the PDF or changes the upload path.
```

- [ ] **Step 2: Verify source IDs exist**

Run:

```bash
rg -n 'source_id: "kblaminates-' llm_wiki/sources/registry/materials
```

Expected: each recovered product has exactly one source record unless an official product page and official PDF both exist.

### Task 3: Conditional Exact-Product Fact Cards

**Files:**

- Create conditionally under `llm_wiki/facts/materials/`

- [ ] **Step 1: Create one fact card per recovered source-backed product**

Use this exact fact shape:

```markdown
---
fact_id: "materials-kingboard-product-slug"
title: "Kingboard PRODUCT baseline material card"
topic: "PRODUCT"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-27"
source_ids: ["kblaminates-product-slug-technical-information"]
tags: ["kingboard", "kblaminates", "product-slug", "materials"]
---

# Canonical Summary

> `PRODUCT` is an exact-product KBLaminates material card. It can only be used for source-scoped material-property claims and cannot be generalized to adjacent suffixes, finished-board qualification, or fabricator capability.

## Stable Facts

- KBLaminates identifies `PRODUCT` in the official source.
- Add only values directly visible in the official source.
- For dielectric values, keep frequency and method attached.
- For CTE / T-260 / T-288 / thermal stress / CTI / resistivity / peel / moisture values, keep condition and method attached.
- For IPC / UL references, quote only the product-level reference, not finished-board compliance.

## Conditions And Methods

- Keep specimen construction and thickness attached where listed.
- Treat values as typical unless the source states a minimum, maximum, or specification bound.

## Limits And Non-Claims

- This card does not prove board-level reliability, application qualification, channel compliance, cost, lead time, availability, or HIL/APT capability.
- It does not authorize suffix inheritance from adjacent Kingboard products.

## Source Links

- OFFICIAL_URL
```

- [ ] **Step 2: Preserve blocked products**

If no official source exists, do not create a fact card. Add the product to the `Still Blocked` section in `p4-28`.

### Task 4: Prepreg Construction Boundary Layer

**Files:**

- Create: `llm_wiki/facts/materials/kingboard-prepreg-construction-data-boundaries.md`

- [ ] **Step 1: Add the boundary fact**

Content requirements:

- List covered prepreg families from recovered sources:
  - `KB-6060`
  - `KB-6064`
  - `KB-6065`
  - `KB-6065F`
  - `KB-6067F`
  - `PP-HF140`
  - `PP-HF170`
  - `PP-KB3200G`
  - `PP-PI520G`
- State that prepreg Dk/Df, resin content, and pressed thickness are construction-sensitive.
- State that values must not be averaged into one Kingboard Dk/Df number.
- State that a blog may cite prepreg construction only when exact product, glass style, resin content, frequency, and source are present.

- [ ] **Step 2: Source IDs**

Use only the already recovered P4-26 source IDs and any Task 2 newly recovered source IDs.

### Task 5: Kingboard Selector / Tier Normalization Layer

**Files:**

- Create: `llm_wiki/facts/materials/kingboard-material-selection-boundaries.md`

- [ ] **Step 1: Add selector-safe groupings**

Allowed groupings:

- Conventional normal-Tg FR-4: `KB-6150`, `KB-6160`
- Low-CTE / lead-free FR-4: `KB-6164`, `KB-6165`, `KB-6165F`
- High-Tg low-CTE FR-4: `KB-6167F`
- Halogen-free normal/high-Tg: `HF-140`, `HF-170`
- Halogen-free low-loss: `KB-3200G`
- Ultra-high-Tg halogen-free / low-CTE: `PI-520G`

Blocked groupings:

- Cost ladder
- Portfolio ranking
- Speed-to-material mapping
- PAM4 / PCIe / USB / DDR / Ethernet support
- Application qualification
- Finished-board compliance proof
- HIL/APT stocking or capability proof

- [ ] **Step 2: Include exact correction notes**

Must include:

- `KB-6160` current official source values supersede draft stale values.
- `KB-6165` current official `Td` is `348 C`.
- `PI-520G` does not validate `PI-515G`.
- `KB-3200G` does not validate `KB-6169GT` or channel-speed claims.

### Task 6: Topic Wiki For Prompt Consumption

**Files:**

- Create: `llm_wiki/wiki/materials/kingboard-laminate-selection-and-boundaries.md`

- [ ] **Step 1: Build a public-writing consumption page**

Sections:

- `Use This Page For`
- `Covered Exact Products`
- `Safe Selection Language`
- `Unsafe Selection Language`
- `Prepreg And Construction Data`
- `Remaining Blocked Products`
- `Blog Rewrite Implications`

- [ ] **Step 2: Link facts and sources**

The page must reference:

- All P4-26 Kingboard fact IDs.
- `materials-kingboard-material-selection-boundaries`.
- `materials-kingboard-prepreg-construction-data-boundaries`.
- Any new exact-product facts created in Task 3.

### Task 7: Completion Map For `/tmps/en`

**Files:**

- Modify: `llm_wiki/logs/p4-25-kingboard-material-blog-ingestion-map.md`
- Modify: `llm_wiki/logs/p4-26-kingboard-official-source-recovery.md`
- Modify: `llm_wiki/logs/p4-28-kingboard-residual-source-recovery.md`

- [ ] **Step 1: Add draft-level final status**

Use these statuses:

- `fully_learned_at_exact_product_level`
- `partially_learned_with_blocked_suffixes`
- `selector_only_not_aggregate_fact`
- `blocked_pending_official_source`

- [ ] **Step 2: Classify all 17 drafts**

Expected starting classification:

- `kb-6150-pcb.md`: `fully_learned_at_exact_product_level`
- `kb-6160-pcb.md`: `fully_learned_at_exact_product_level_with_value_correction`
- `kb-6164-pcb.md`: `fully_learned_at_exact_product_level`
- `kb-6165-pcb.md`: `fully_learned_at_exact_product_level_with_td_conflict_resolved`
- `kb-6165f-pcb.md`: `fully_learned_at_exact_product_level`
- `kb-6167f-pcb.md`: `fully_learned_at_exact_product_level`
- `hf-140-hf-170-pcb.md`: `fully_learned_at_exact_product_level`
- `kb-3200g-pcb.md`: `fully_learned_at_material_property_level_but_channel_claims_blocked`
- `pi-515g-pi-520g-pcb.md`: `partially_learned_with_pi-515g_blocked`
- `kingboard-pcb-laminate.md`: `selector_only_not_aggregate_fact`
- all remaining suffix drafts: status depends on Tasks 1-3.

### Task 8: Tracking Updates

**Files:**

- Modify: `llm_wiki/logs/update-log.md`
- Modify: `llm_wiki/logs/backlog.md`
- Modify: `llm_wiki/logs/phase-status.md`

- [ ] **Step 1: Update update-log**

Add entries describing:

- Which residual sources were recovered.
- Which residual products stayed blocked.
- Which selector / prepreg / topic wiki layers were added.
- Which claim families remain non-unlocked.

- [ ] **Step 2: Update backlog**

Move the Kingboard remaining-content batch to completed only when Tasks 1-7 are finished.

- [ ] **Step 3: Update phase-status counts**

Run:

```bash
rg --files llm_wiki/sources | wc -l
rg --files llm_wiki/facts | wc -l
rg --files llm_wiki/wiki | wc -l
rg --files llm_wiki/logs | wc -l
```

Update the corpus snapshot with the new counts.

### Task 9: Verification

**Files:**

- Read-only verification across `llm_wiki`

- [ ] **Step 1: Diff hygiene**

Run:

```bash
git diff --check
```

Expected: no output.

- [ ] **Step 2: Source ID resolution**

For every new fact card, verify each `source_id` exists under `llm_wiki/sources/registry`.

Command pattern:

```bash
rg -n 'source_ids:' llm_wiki/facts/materials/kingboard-*.md
rg -n 'source_id: "kblaminates-' llm_wiki/sources/registry/materials
```

Expected: no fact references an absent source.

- [ ] **Step 3: No draft-as-source leakage**

Run:

```bash
rg -n 'tmps/en|draft|blog-only|estimated' llm_wiki/facts/materials/kingboard-*.md llm_wiki/wiki/materials/kingboard-laminate-selection-and-boundaries.md
```

Expected:

- Allowed only in limits / blocked sections.
- No fact should cite `/code/blogs/tmps/en` as evidence.

- [ ] **Step 4: Public-claim block check**

Run:

```bash
rg -n 'cost|lead time|inventory|stock|PCIe|PAM4|DDR|USB|Ethernet|AEC|PPAP|qualification|yield|HIL|APT' llm_wiki/facts/materials/kingboard-*.md llm_wiki/wiki/materials/kingboard-laminate-selection-and-boundaries.md
```

Expected:

- These terms appear only in `Limits And Non-Claims`, `Blocked`, or equivalent safety sections.

## Completion Definition

The task is complete only when:

- Every remaining product has either an official source-backed fact or an explicit blocked disposition.
- Selector and prepreg boundary layers exist.
- The topic wiki page gives prompts_template a safe Kingboard consumption layer.
- All 17 `/tmps/en` drafts have final learned / partial / blocked status.
- `git diff --check` passes.
- Source/fact references are consistent.

## Recommended Execution

Use 4 parallel `gpt-5.4` subagents for Task 1 source recovery:

- Agent A: `KB-6160A / KB-6160F / KB-6160LC / KB-6160LC(C)`
- Agent B: `KB-6165C / KB-6165LE`
- Agent C: `KB-6167GMD / KB-6167GLD / KB-6168LE / KB-6169GT`
- Agent D: `PI-515G`

Main agent should own:

- Source-record and fact-card write integration.
- Selector and prepreg boundary layers.
- Final wiki page.
- Tracking updates and verification.
