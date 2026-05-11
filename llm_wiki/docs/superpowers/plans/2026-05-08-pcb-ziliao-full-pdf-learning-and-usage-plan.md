# PCB资料 Full PDF Learning And Usage Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert all `63` PDFs under `/code/blogs/tmps/PCB资料` into a usage-ready `llm_wiki` surface where every PDF is covered by deletion-safe learning artifacts and every reusable claim family is routed into `official_fact`, `local_pdf_fact`, `blocked_evidence`, or explicit hold/boundary status.

**Architecture:** Treat the corpus as two different systems that must not be mixed. The `4` handbook PDFs are already near the unified knowledge-layer target and should continue through narrow authority-recovery, `pdf_evidence`, `facts/local_pdf`, and route integration. The `59` `PCB文章` PDFs are not “fully learned” per file yet; they should be promoted from cluster-level claim inventory into bounded, usage-oriented lanes that extract reusable wiki/fact surfaces only where source-backed or tightly local-scoped wording is safe.

**Tech Stack:** `/code/blogs/llm_wiki` markdown corpus, `/code/blogs/tmps/PCB资料`, `/code/blogs/tmps/pcb_pdf_extracted_full`, `llm-wiki-workflow`, `rg`, `git diff --check`, and `gpt-5.4` subagents for bounded independent lanes.

---

## Current Authoritative Resume State

This plan was created before `P4-314`, `P4-316`, `P4-317`, `P4-318`, `P4-319`, `P4-320`, `P4-321`, `P4-322`, and `P4-323`.
For current execution and future `/goal` recovery, treat `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md` as the authoritative resume entry.

Current real state:

- handbook side is `strong_complete_with_residual_authority_gaps`
- article side is `usage_route_covered_at_controller_level_only` across `E2-E6`
- `E1` and `E7` remain `claim_family_level_only_with_hold`
- package residual narrowing already landed:
  - `P4-316` for one owner-scoped `0.75 mm` exact-data replacement row
  - `P4-320` for one additional owner-scoped `0.75 mm` exact-data replacement row
  - `P4-317` for one layered `connector-origin / installation mark` boundary route
  - `P4-322` for one additional Samtec connector-owner named-series layout route
  - `P4-318` for one `1.50 mm` standards-owner existence-and-scope boundary
  - `P4-319` for one controller-level public recheck confirming that `1.50 mm` still has no landed public exact-geometry row above the current `P4-318` ceiling
  - `P4-321` for one Amphenol connector-owner access-blocker note
  - `P4-323` for one `1.50 mm` search-filter note that excludes body-size and contact-pad-spacing false positives
- corpus dispatch surface already landed:
  - `P4-325` for one deletion-safe per-PDF coverage index across all `63` PDFs

Current next sequence:

1. continue `package residual authority recovery`, with public `1.50 mm exact geometry` still the highest-value open gap
2. if no clean `1.50 mm` geometry row is found, preserve the current `P4-318` ceiling, treat `P4-319` as the latest negative-result controller note, and apply `P4-323` to filter out body-size and contact-pad-spacing false positives before reopening owner-drawing candidates
3. after that, consider narrower follow-up recovery only for:
   - additional owner-scoped `0.75 mm` rows beyond the current multiple Microchip routes
   - additional owner-specific or standards-adjacent `connector-origin / installation mark` layers beyond the current `Molex + Samtec` public route set
   - article-side narrow official-source recovery for `E2 / E4 / E5 / E6`

Interpretation rule:

- the historical task checklist below remains useful as execution history and lane design reference
- it is not the current truth about what is still unfinished
- do not reopen `E2-E6` article usage-route integration as if it were still the primary undone batch
- do not say all `63` PDFs are already fully learned at fact/wiki level

---

## Scope And Success Criteria

### Corpus In Scope

- `/code/blogs/tmps/PCB资料/【PCB必备】194页-PCB设计规范经验之书.pdf`
- `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- `/code/blogs/tmps/PCB资料/【PCB必备】158页-PCBA检验规范汇总.pdf`
- `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/*.pdf` (`59` files)

### True Completion For This Goal

This goal is complete only when all of the following are true:

1. every PDF in `/code/blogs/tmps/PCB资料` is covered by `llm_wiki` artifacts that survive `tmps/` deletion
2. every PDF is mapped to one of these usage states:
   - `official_fact-backed`
   - `local_pdf_fact-backed`
   - `blocked_evidence_only`
   - `claim_family_level_only_with_explicit_hold_reason`
3. handbook-origin reusable content is discoverable from `pdf_evidence/pcb_ziliao/`, `facts/local_pdf/`, `facts/`, and `wiki/` without reopening `tmps`
4. the `59` article PDFs are no longer only “clustered inventory”; each bounded cluster has either:
   - a source-backed wiki/fact route
   - a local-evidence route
   - or an explicit hold map stating why direct promotion is blocked
5. future writing agents can use `llm_wiki` alone to decide what each PDF contributes safely
6. trackers state what is directly usable, what remains blocked, and what authority gaps remain

### Non-Goals

- no fake claim that every residual numeric is replaced by an official source
- no broad reread of already neutralized branded PDFs unless a bounded lane can change the fact layer
- no promotion of article numerics, vendor rule tables, or branded workflow screens directly into reusable facts
- no expansion into `/code/blogs/tmps/materias_pdf`

## Current Baseline

### What Is Already Done

- handbook batch is already `strong_complete` at program level under:
  - `logs/p4-291-2026-5-7-pcb-pdf-strong-completion-closeout.md`
- unified local-PDF model is already cut in under:
  - `docs/superpowers/plans/2026-05-08-pcb-ziliao-unified-knowledge-layer-plan.md`
- handbook evidence and local fact layers already exist:
  - `pdf_evidence/pcb_ziliao/`
  - `facts/local_pdf/`
- article corpus already has controller-owned cluster coverage:
  - `P4-283`
  - `P4-285` through `P4-290`
- article corpus now also has bounded controller-level usage-route coverage across:
  - `P4-310`
  - `P4-311`
  - `P4-312`
  - `P4-313`
  - `P4-314`
- package residual lane has already narrowed through:
  - `P4-316`
  - `P4-320`
  - `P4-317`
  - `P4-321`
  - `P4-322`
  - `P4-318`
  - `P4-319`
  - `P4-323`

### What Is Not Done Yet

- the `59` article PDFs are still mostly below per-file or per-subtopic usage-ready absorption
- `package` residual authority gaps remain, especially:
  - public `1.50 mm` exact-geometry replacement row
  - broader `0.75 mm` coverage beyond the current multiple owner-scoped Microchip rows
  - stronger connector-owner or standards-adjacent support for `connector-origin` beyond the current `Molex + Samtec` set
  - stronger cross-vendor support for `installation mark`
- article side still lacks the narrower follow-up recoveries that could turn parts of `E2 / E4 / E5 / E6` into stronger `sources/registry`, `facts/`, or `wiki/` surfaces
- corpus-wide coverage is now resumable from `P4-309`, but true completion still requires deletion-safe per-PDF usage coverage beyond controller-level routing
- corpus-wide per-PDF indexing is now landed through `P4-325`, but most article PDFs still remain cluster-routed rather than fact-promoted per file

## File Structure

### Existing Files To Reuse

- `llm_wiki/logs/p4-283-2026-5-7-pcb-article-cluster-inventory.md`
- `llm_wiki/logs/p4-283b-2026-5-7-pcb-article-e2-layout-routing-stackup-layers-and-impedance-claim-family-map.md`
- `llm_wiki/logs/p4-283e3-2026-5-7-pcb-article-e3-claim-family-boundary-map.md`
- `llm_wiki/logs/p4-290-2026-5-7-pcb-article-e1-e7-controller-integration.md`
- `llm_wiki/logs/p4-291-2026-5-7-pcb-pdf-strong-completion-closeout.md`
- `llm_wiki/wiki/processes/package-library-governance-and-footprint-review-map.md`

### New Files To Create

- one or more new package-residual continuation logs after `P4-323`
- one or more narrow `sources/registry/methods/*.md` or `sources/registry/standards/*.md` files only if stronger primary authority is actually recovered
- one or more narrow `facts/methods/*.md` files only if the new authority supports a bounded reusable statement
- one or more new `wiki/processes/*.md` pages for article-cluster aggregation where source-backed reuse is possible
- selective `pdf_evidence/pcb_ziliao/articles/...` records if clean diagram/table subregions are worth preserving
- selective `facts/local_pdf/*.md` cards only when wording can remain explicitly local-PDF-scoped

### Existing Files Expected To Change

- `llm_wiki/logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `llm_wiki/logs/update-log.md`
- `llm_wiki/logs/backlog.md`
- `llm_wiki/logs/phase-status.md`
- `llm_wiki/wiki/processes/package-library-governance-and-footprint-review-map.md` if package residual routes improve
- existing or new `wiki/processes/*.md` aggregation pages for article-cluster usage

## Lane Strategy For `/goal` + Subagents

### Lane Ownership Rules

- every subagent owns exactly one log path under `llm_wiki/logs/`
- subagents do not update global trackers
- subagents do not create reusable `facts/` or `wiki/` unless the main agent explicitly assigns that lane
- subagents treat all `tmps/PCB资料` files as claim inventory, not authority
- main agent owns:
  - final source/fact/wiki merge
  - tracker updates
  - conflict resolution
  - verification

### Recommended Parallel Lanes

1. `package residual exact-authority lane`
   - public `1.50 mm` exact-geometry recovery first
2. `package residual support lane`
   - additional owner-scoped `0.75 mm` rows beyond the current two Microchip routes
3. `connector-origin / installation-mark support lane`
   - more owner-specific or standards-adjacent layers without universalization, using `P4-321` to avoid blocked public candidates
4. `E2 narrow official-source recovery lane`
   - layer vocabulary, stackup/governance, impedance identity, safety-distance taxonomy
5. `E4 or E5 narrow follow-up lane`
   - panelization / mark / board-edge vocabulary or assembly / test / polarity documentation vocabulary
6. `E6 narrow technical-identity lane`
   - package-to-footprint alignment, FPC identity, or `0R` identity subset without procurement-risk promotion

### Recommended Hold-Only Lanes

- `E1` DFM persuasion
- `E7` vendor-tool workflow and branded prep flows

These should only be reopened if a bounded neutral subset can change the fact layer.

## Task Plan

### Task 1: Create The Master Execution Surface

**Files:**
- Create: `llm_wiki/logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- Modify: `llm_wiki/logs/update-log.md`
- Modify: `llm_wiki/logs/backlog.md`
- Modify: `llm_wiki/logs/phase-status.md`

- [ ] **Step 1: Build the corpus master log**

Create a master log that lists:

- `63` PDF paths
- corpus split:
  - `4` handbook PDFs
  - `59` article PDFs
- current status per batch:
  - handbook: `strong_complete_with_residual_authority_gaps`
  - articles: `cluster_covered_but_not_usage_integrated`
- intended execution order:
  - `E3`
  - `E5`
  - `E2`
  - `E4`
  - `E6`
  - package residual authority

- [ ] **Step 2: Record the new continuation entry in trackers**

Update:

- `logs/update-log.md`
- `logs/backlog.md`
- `logs/phase-status.md`

State that future `/goal` work should use `P4-309` as the corpus-wide entry point rather than mixing:

- handbook `strong_complete`
- article cluster inventory
- package residual recovery

- [ ] **Step 3: Verify the master entry**

Run:

```bash
rg -n "P4-309|full-corpus-learning-and-usage" /code/blogs/llm_wiki
git -C /code/blogs diff --check -- \
  llm_wiki/logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md \
  llm_wiki/logs/update-log.md \
  llm_wiki/logs/backlog.md \
  llm_wiki/logs/phase-status.md
```

Expected:

- `P4-309` is discoverable
- `diff --check` is clean

### Task 2: Execute The `E3` Article Usage Lane First

**Files:**
- Create: `llm_wiki/logs/p4-311-2026-5-8-pcb-article-e3-usage-route-integration.md`
- Modify or Create: selective `llm_wiki/pdf_evidence/pcb_ziliao/articles/e3-*.md`
- Modify or Create: one `llm_wiki/wiki/processes/*.md` page if multiple source-backed facts must be consumed together

- [ ] **Step 1: Dispatch one subagent for `E3`**

Subagent prompt:

```text
Use model gpt-5.4. You own only this lane: PCB文章 E3 fabrication-features usage integration.
Input:
- /code/blogs/tmps/PCB资料/PCB文章
- /code/blogs/llm_wiki/logs/p4-283e3-2026-5-7-pcb-article-e3-claim-family-boundary-map.md
Output:
- /code/blogs/llm_wiki/logs/p4-311-2026-5-8-pcb-article-e3-usage-route-integration.md
Allowed edits:
- that output log only
Banned edits:
- global trackers
- facts/
- wiki/
- sources/registry/
Treat drafts as claim inventory, not facts. Do not promote unsupported numeric, capability, certification, price, lead-time, MOQ, yield, or quality claims.
Return changed files, safe reuse classes, blocked classes, local-evidence candidates, and official-source recovery targets.
```

- [ ] **Step 2: Main agent reads the lane log and chooses one of three outcomes**

Allowed outcomes:

- `source_recovery_now`
- `local_evidence_now`
- `hold_map_only`

Decision rule:

- if the lane exposes strong official-source targets for hole/slot/via/mask/pad concepts, recover them
- if clean diagrams can be cropped without rule-table contamination, preserve them as `pdf_evidence`
- if neither is true, keep the lane as usage hold map only

- [ ] **Step 3: Land the integration artifacts**

Possible outputs:

- one or more `sources/registry/methods/*.md`
- one or more `facts/methods/*.md`
- one bounded `wiki/processes/*.md`
- or explicit `blocked_evidence` records only

Do not claim exact numeric closure unless official source rows exist.

- [ ] **Step 4: Verify the lane**

Run:

```bash
rg -n "P4-311|e3|hole|slot|via|solder-mask|gold finger|half-hole" /code/blogs/llm_wiki
git -C /code/blogs diff --check -- <touched files>
```

Expected:

- lane log is discoverable
- any new source/fact/wiki links resolve
- no formatting errors

### Task 3: Execute The `E5` Article Usage Lane Second

**Files:**
- Create: `llm_wiki/logs/p4-313-2026-5-8-pcb-article-e5-usage-route-integration.md`
- Modify or Create: selective `llm_wiki/pdf_evidence/pcb_ziliao/articles/e5-*.md`
- Modify or Create: one or more `llm_wiki/wiki/processes/*.md`

- [ ] **Step 1: Dispatch one subagent for `E5`**

Subagent prompt:

```text
Use model gpt-5.4. You own only this lane: PCB文章 E5 assembly, DFA, stencil, soldering, and test usage integration.
Input:
- /code/blogs/tmps/PCB资料/PCB文章
- /code/blogs/llm_wiki/logs/p4-283-2026-5-7-pcb-article-cluster-inventory.md
Output:
- /code/blogs/llm_wiki/logs/p4-313-2026-5-8-pcb-article-e5-usage-route-integration.md
Allowed edits:
- that output log only
Banned edits:
- global trackers
- facts/
- wiki/
- sources/registry/
Treat drafts as claim inventory, not facts. Do not promote thresholds, capability claims, acceptance judgments, or assembly-yield claims.
Return changed files, safe reuse classes, blocked classes, local-evidence candidates, and official-source recovery targets.
```

- [ ] **Step 2: Main agent integrate only the safe subset**

High-probability safe outputs:

- assembly-orientation vocabulary
- pin-1 / silkscreen / polarity documentation posture
- stencil / BGA defect identity taxonomy
- generic test-method identity routing

Blocked outputs:

- acceptance thresholds
- process capability claims
- any “best/acceptable/unacceptable” article labels

- [ ] **Step 3: Verify the lane**

Run:

```bash
rg -n "P4-313|assembly|stencil|BGA|polarity|test" /code/blogs/llm_wiki
git -C /code/blogs diff --check -- <touched files>
```

Expected:

- lane is integrated or explicitly held
- blocked claims are still explicit

### Task 4: Execute The `E2` Article Usage Lane Third

**Files:**
- Create: `llm_wiki/logs/p4-310-2026-5-8-pcb-article-e2-usage-route-integration.md`
- Modify or Create: one or more `llm_wiki/wiki/processes/*.md`
- Modify or Create: selective `pdf_evidence/pcb_ziliao/articles/e2-*.md`

- [ ] **Step 1: Dispatch one subagent for `E2`**

Subagent prompt:

```text
Use model gpt-5.4. You own only this lane: PCB文章 E2 layout, routing, stackup, layers, impedance, and safety-distance usage integration.
Input:
- /code/blogs/tmps/PCB资料/PCB文章
- /code/blogs/llm_wiki/logs/p4-283b-2026-5-7-pcb-article-e2-layout-routing-stackup-layers-and-impedance-claim-family-map.md
Output:
- /code/blogs/llm_wiki/logs/p4-310-2026-5-8-pcb-article-e2-usage-route-integration.md
Allowed edits:
- that output log only
Banned edits:
- global trackers
- facts/
- wiki/
- sources/registry/
Treat drafts as claim inventory, not facts. Do not promote exact spacing, impedance, stackup, or safety-distance numerics.
Return changed files, safe reuse classes, blocked classes, local-evidence candidates, and official-source recovery targets.
```

- [ ] **Step 2: Promote only reusable boundary knowledge**

Likely safe outputs:

- layer-definition vocabulary
- reference-plane and return-path boundary routing
- characteristic-impedance identity wording
- safety-distance family taxonomy without numbers

- [ ] **Step 3: Verify the lane**

Run:

```bash
rg -n "P4-310|impedance|stackup|layer|safety-distance|reference-plane" /code/blogs/llm_wiki
git -C /code/blogs diff --check -- <touched files>
```

Expected:

- no exact numeric leakage
- wiki/fact routing remains conservative

### Task 5: Execute The `E4` And `E6` Article Lanes

**Files:**
- Create: `llm_wiki/logs/p4-312-2026-5-8-pcb-article-e4-usage-route-integration.md`
- Create: `llm_wiki/logs/p4-314-2026-5-8-pcb-article-e6-usage-route-integration.md`

- [ ] **Step 1: Dispatch `E4` subagent**

Focus:

- panelization
- board edge
- component-to-edge
- mark point
- outline families

Main-agent acceptance rule:

- only promote neutral process routing and documentation vocabulary
- keep exact edge distances and factory-specific panel rules blocked

- [ ] **Step 2: Dispatch `E6` subagent**

Focus:

- package and package-to-footprint alignment
- BOM mismatch taxonomy
- procurement-risk taxonomy
- selective 0R resistor and FPC identity subsets

Main-agent acceptance rule:

- split `E6` into safe technical identity versus procurement/purchasing hold content

- [ ] **Step 3: Verify both lanes**

Run:

```bash
rg -n "P4-312|P4-314|panel|mark point|BOM|package|0R|FPC" /code/blogs/llm_wiki
git -C /code/blogs diff --check -- <touched files>
```

Expected:

- both lanes are either usage-integrated or explicitly held
- procurement advice is not promoted as engineering fact

### Task 6: Run The Package Residual Authority Lane Last

**Files:**
- Modify: `llm_wiki/wiki/processes/package-library-governance-and-footprint-review-map.md`
- Modify: `llm_wiki/facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`
- Create: one or more narrow `sources/registry/methods/*.md`
- Create: one or more narrow `facts/methods/*.md`
- Create: `llm_wiki/logs/p4-315-2026-5-8-package-residual-authority-recovery.md`

- [ ] **Step 1: Dispatch one subagent for source scouting only**

Subagent prompt:

```text
Use model gpt-5.4. You own only this lane: package residual authority scouting.
Input:
- /code/blogs/llm_wiki/facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md
- /code/blogs/llm_wiki/wiki/processes/package-library-governance-and-footprint-review-map.md
Output:
- /code/blogs/llm_wiki/logs/p4-315-2026-5-8-package-residual-authority-recovery.md
Allowed edits:
- that output log only
Banned edits:
- global trackers
- facts/
- wiki/
- sources/registry/
Find only official package-owner, connector-owner, CAD-owner, or standards-adjacent public sources for:
- 0.75 mm pitch replacement
- 1.50 mm pitch replacement
- connector-origin defaulting
- installation-mark conventions
Do not overclaim universal rules. Return source candidates, exact scope, and what remains unresolved.
```

- [ ] **Step 2: Main agent lands only narrow recoveries**

Allowed landings:

- one official source record
- one narrow fact card
- one route-map update

Not allowed:

- universalized table rewrite
- connector-origin default by inference

- [ ] **Step 3: Verify the residual lane**

Run:

```bash
rg -n "P4-315|0.75 mm|1.50 mm|connector-origin|installation mark" /code/blogs/llm_wiki
git -C /code/blogs diff --check -- <touched files>
```

Expected:

- any new authority is narrow and explicit
- unresolved residuals remain visible if not actually closed

### Task 7: Final Corpus Integration And Completion Gate

**Files:**
- Modify: `llm_wiki/logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- Modify: `llm_wiki/logs/update-log.md`
- Modify: `llm_wiki/logs/backlog.md`
- Modify: `llm_wiki/logs/phase-status.md`
- Optional Create: `llm_wiki/logs/p4-316-2026-5-8-pcb-ziliao-full-corpus-usage-completion-gate.md`

- [ ] **Step 1: Build a per-batch completion table**

The final integration file should list:

- `4` handbook PDFs:
  - current usage state
  - residual blockers
- `59` article PDFs:
  - cluster membership
  - usage state
  - whether they now route to `wiki`, `facts`, `local_pdf_fact`, `blocked_evidence`, or hold map only

- [ ] **Step 2: Update trackers with corpus-wide wording**

Trackers must answer these questions clearly:

- are all `63` PDFs covered?
- which lanes are directly reusable for writing?
- which ones are still blocked but understood?
- which residual gaps are optional rather than blocking?

- [ ] **Step 3: Run the final completion audit**

Run:

```bash
find /code/blogs/tmps/PCB资料 -maxdepth 2 -type f | rg '\.pdf$' | wc -l
rg -n "pcb_ziliao|P4-309|P4-310|P4-311|P4-312|P4-313|P4-314|P4-315|blocked_evidence|local_pdf_fact" /code/blogs/llm_wiki
git -C /code/blogs diff --check -- /code/blogs/llm_wiki
```

Expected:

- total count remains `63`
- every planned lane is discoverable
- no formatting errors across touched `llm_wiki` files

## Execution Notes For `/goal`

### Recommended `/goal` Objective Text

Use this as the next `/goal` objective:

```text
按 llm_wiki/logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md 和 llm_wiki/docs/superpowers/plans/2026-05-08-pcb-ziliao-full-pdf-learning-and-usage-plan.md 推进 /code/blogs/tmps/PCB资料 的所有 63 个 PDF 学习与使用落地：以 package residual authority recovery 为当前主线，优先尝试 public 1.50 mm exact-geometry route，在不破坏治理边界的前提下再补 0.75 mm、connector-origin、installation mark 的窄增量，并仅把 E2/E4/E5/E6 作为后续 narrow official-source recovery lanes。
```

### Recommended First `/goal` Execution Batch

First batch only:

- one bounded `1.50 mm` public exact-geometry scouting lane
- one bounded backup lane for either:
  - additional owner-scoped `0.75 mm` package rows
  - or additional `connector-origin / installation mark` owner-specific support
- main agent integrates only if the result lands above the current `P4-323` / `P4-322` / `P4-321` / `P4-320` / `P4-319` / `P4-318` / `P4-317` / `P4-316` ceiling

Reason:

- this attacks the highest-value remaining package gap first
- it keeps subagent write scopes narrow and verifiable
- it avoids reopening already completed `E2-E6` controller-level usage integration as duplicated work

### Recommended Parallelism

- Run one `1.50 mm` exact-geometry scout and one non-overlapping backup scout in parallel.
- Keep final source/fact/wiki landing, tracker updates, and `P4-309` synchronization under the main agent.
- Do not reopen `E2-E6` usage-route integration as a first-batch parallel swarm.

## Risks And Guardrails

- article PDFs are branding-heavy; clean crop discipline is mandatory
- `claim_family_level_only` must not be misreported as fully learned
- local article figures may be useful as `blocked_evidence` or `local_pdf_fact`, but only when wording scope stays explicit
- package residual source scouting is easy to overclaim; keep package-owner scope attached to every numeric row
- tracker language must distinguish:
  - corpus covered
  - usage integrated
  - source-backed
  - still blocked

## Self-Review

### Spec Coverage

- user goal `PCB资料 目录下所有 pdf 的学习与使用`: covered by corpus-wide completion gate and all `63` PDF coverage rule
- later `/goal` with subagents: covered by lane strategy, prompts, sequencing, and recommended first batch
- distinction between handbook and article corpus: explicitly covered in architecture, current baseline, and lane split

### Placeholder Scan

- no `TBD`
- no `TODO`
- no “similar to above” execution dependency
- every `/goal` lane has explicit input, output, allowed edits, and banned edits

### Consistency Check

- `P4-309` is master entry
- `P4-310` through `P4-314` are article usage lanes
- `P4-315` is package residual authority recovery
- `P4-316` / `P4-320` are already-landed `0.75 mm` package residual narrowing passes
- `P4-317` / `P4-322` are the current public connector-owner support set for the connector lane
- `P4-318` is still the strongest landed standards-owner existence boundary for `1.50 mm`
- `P4-319` is the latest negative-result controller note for the still-open `1.50 mm` public exact-geometry gap
- `P4-321` is the current access blocker note for one Amphenol connector-owner candidate
- `P4-323` is the current search-filter note for `1.50 mm` false positives
- current `/goal` recovery should start from `P4-309`, not from the older task ordering below

## Completion Output

When this plan is executed successfully, the final response should state:

- how many of the `63` PDFs are now usage-covered directly from `llm_wiki`
- which clusters now route to reusable `facts/` or `wiki/`
- which residual authority gaps remain optional
- whether future writing agents can proceed from `llm_wiki` alone
