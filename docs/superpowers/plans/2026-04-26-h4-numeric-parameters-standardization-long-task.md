# H4 Numeric Parameters And Standardization Long-Task Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn `H4` into a durable controller-led multi-agent program that advances `more numbers` through shared `B` capability-parameter routing, advances standards-heavy control through reusable standardization cards, and keeps supplier-scoped dated numeric/parameter records bounded under a separate lane.

**Architecture:** The controller agent owns lane order, tracking docs, and final integration. Independent subagents handle disjoint lanes: shared `B` capability parameters, standards / qualification / acceptance standardization, and supplier-scoped dated records. Every lane output must distinguish routing/control improvement from readiness improvement.

**Tech Stack:** Markdown logs under `llm_wiki/logs`, plan docs under `docs/superpowers/plans`, existing `H3/H4` control notes, `apply_patch`, `rg`, `sed`, existing Codex subagents.

---

### Task 1: Lock The H4 Long-Task Control Surface

**Files:**
- Create: `docs/superpowers/plans/2026-04-26-h4-numeric-parameters-standardization-long-task.md`
- Create: `llm_wiki/logs/h4-long-task-multi-agent-plan.md`
- Modify: `llm_wiki/logs/backlog.md`
- Modify: `llm_wiki/logs/phase-status.md`
- Modify: `llm_wiki/logs/update-log.md`

- [ ] **Step 1: Confirm the current H4 baseline and lane assets**

Run: `sed -n '1,240p' llm_wiki/logs/h4-numeric-parameters-and-standardization-kickoff.md`
Expected: the file still defines three axes and keeps public reusable numeric readiness unchanged by default.

- [ ] **Step 2: Create the durable H4 multi-agent plan note**

Write `llm_wiki/logs/h4-long-task-multi-agent-plan.md` with:
- purpose and non-goals
- controller vs lane-agent ownership
- lane order
- output contract per lane
- stop conditions
- sync rules for tracking docs

- [ ] **Step 3: Record the active long-task state in tracking**

Update `backlog.md` and `phase-status.md` so they both say:
- `H4` is active as a controller-led multi-agent long task
- Lane 1 is shared `B` capability-parameter routing
- Lane 2 is standards / qualification / acceptance standardization
- Lane 3 is supplier-scoped dated numeric/parameter records

- [ ] **Step 4: Append the plan landing to the update log**

Update `update-log.md` with one concise bullet group that records:
- `H4` long-task multi-agent control is now formalized
- three lanes now have fixed ownership and order
- no readiness unlock is implied

- [ ] **Step 5: Verify the control surface is internally consistent**

Run: `rg -n "H4|Lane 1|Lane 2|Lane 3|multi-agent" llm_wiki/logs/backlog.md llm_wiki/logs/phase-status.md llm_wiki/logs/h4-long-task-multi-agent-plan.md`
Expected: lane order and status language align across all three files.

### Task 2: Advance Lane 1 Shared B Capability Parameters

**Files:**
- Create: `llm_wiki/logs/h4-trace-space-routing-note.md`
- Create: `llm_wiki/logs/h4-minimum-mechanical-drill-routing-note.md`
- Create: `llm_wiki/logs/h4-minimum-laser-via-routing-note.md`
- Modify: `llm_wiki/logs/backlog.md`
- Modify: `llm_wiki/logs/phase-status.md`
- Modify: `llm_wiki/logs/update-log.md`

- [ ] **Step 1: Use subagents to split Phase A across three disjoint classes**

Read only:
- `llm_wiki/logs/h4-shared-b-capability-parameters-first-wave-queue.md`
- `llm_wiki/logs/h4-shared-b-first-wave-parameter-routing-matrix.md`

Expected output: one memo per class with demand branches, blocker shape, acceptable authority requirement, and default refusal posture.

- [ ] **Step 2: Integrate those memos into three class routing notes**

Write:
- `h4-trace-space-routing-note.md`
- `h4-minimum-mechanical-drill-routing-note.md`
- `h4-minimum-laser-via-routing-note.md`

Each file must include:
- class purpose
- first named blocked branches
- blocker shape
- acceptable authority
- refusal posture
- readiness unchanged statement

- [ ] **Step 3: Mark Phase A as routing progress, not numeric recovery**

Tracking language must preserve:
- the lane advanced
- routing precision improved
- no shared capability numeric was unlocked

- [ ] **Step 4: Verify no note treats supplier or standards pages as shared numeric authority**

Run: `rg -n "supplier|standard|threshold|recovered|unlock" llm_wiki/logs/h4-*routing-note.md`
Expected: wording keeps authority boundaries explicit.

### Task 3: Advance Lane 2 Standardization

**Files:**
- Create: `llm_wiki/logs/h4-standards-family-vs-threshold-note.md`
- Create: `llm_wiki/logs/h4-qualification-vs-listing-vs-release-authority-note.md`
- Create: `llm_wiki/logs/h4-acceptance-workflow-vs-acceptance-threshold-note.md`
- Create: `llm_wiki/logs/h4-supplier-conformance-assertion-boundary-note.md`
- Modify: `llm_wiki/logs/backlog.md`
- Modify: `llm_wiki/logs/phase-status.md`
- Modify: `llm_wiki/logs/update-log.md`

- [ ] **Step 1: Split the first four standardization cards into two parallel groups**

Read only:
- `llm_wiki/logs/h4-standards-standardization-first-card-queue.md`
- `llm_wiki/logs/h4-class3-addendum-qualification-acceptance-routing-matrix.md`

Expected grouping:
- Group A: `standards-family vs threshold`, `qualification vs listing vs release-authority`
- Group B: `acceptance-workflow vs acceptance-threshold`, `supplier-conformance assertion boundary`

- [ ] **Step 2: Integrate the memos into four reusable separation cards**

Each card must include:
- claim family handled
- identity split
- default policy posture
- allowed output shape
- blocked output shape
- `22-layer` as primary protected branch
- readiness unchanged statement

- [ ] **Step 3: Keep 20-layer explicitly secondary**

Tracking language must preserve:
- `22-layer` remains the first named blocked branch for the lane
- `20-layer` only inherits secondary protection where method/workflow wording drifts toward proof

- [ ] **Step 4: Verify no standardization card behaves like threshold recovery**

Run: `rg -n "threshold recovery|numeric unlock|accepted result|approved status" llm_wiki/logs/h4-*note.md`
Expected: wording stays at standardization/routing level only.

### Task 4: Advance Lane 3 Supplier-Scoped Dated Records

**Files:**
- Create: `llm_wiki/logs/h4-20-layer-supplier-capability-fact-lane-note.md`
- Create: `llm_wiki/logs/h4-20-layer-supplier-process-control-fact-lane-note.md`
- Modify: `llm_wiki/logs/backlog.md`
- Modify: `llm_wiki/logs/phase-status.md`
- Modify: `llm_wiki/logs/update-log.md`

- [ ] **Step 1: Reuse the H3 workflow substrate without reopening H3 scaffolding**

Read only:
- `llm_wiki/logs/h3-supplier-lane-hardening-closeout.md`
- `llm_wiki/logs/h3-20-22-dated-supplier-record-admissibility.md`
- `llm_wiki/logs/h4-numeric-parameters-and-standardization-kickoff.md`

Expected: the lane uses existing trigger/admissibility/handoff controls and does not create new supplier-lane workflow scaffolding.

- [ ] **Step 2: Open the H4 supplier lane with 20-layer first**

Write:
- `h4-20-layer-supplier-capability-fact-lane-note.md`
- `h4-20-layer-supplier-process-control-fact-lane-note.md`

Each file must include:
- one branch only
- one record family only
- one bounded context only
- narrowest downstream use
- `reject_at_intake` vs `hold_for_governed_review`
- explicit readiness unchanged statement

- [ ] **Step 3: Keep supplier-scoped support non-transferable**

Tracking language must preserve:
- no supplier-scoped fact becomes shared reusable numeric authority
- no branch unlock is implied

- [ ] **Step 4: Verify no lane note promotes supplier facts into public reusable numerics**

Run: `rg -n "public reusable|unlock|generic|shared authority" llm_wiki/logs/h4-20-layer-supplier-*-note.md`
Expected: wording keeps supplier scope, date scope, and non-transferability explicit.

### Task 5: Maintain The H4 Long-Task Loop

**Files:**
- Modify: `llm_wiki/logs/backlog.md`
- Modify: `llm_wiki/logs/phase-status.md`
- Modify: `llm_wiki/logs/update-log.md`

- [ ] **Step 1: Keep lane state explicit after each landing**

After each lane landing, update:
- lane status
- what execution layer landed
- what remains blocked

- [ ] **Step 2: Preserve disjoint ownership for long-running agents**

Ownership rule:
- controller: plan, integration, tracking, final wording
- lane A agents: shared `B` class notes
- lane B agents: standards separation cards
- lane C agents: supplier-scoped branch notes

Do not assign overlapping write scope to subagents.

- [ ] **Step 3: Stop if the evidence ceiling has not changed**

If a pass only improves routing precision or refusal posture, record:
- routing/control improved
- readiness unchanged
- blocked verdict unchanged

- [ ] **Step 4: End each phase with a queue-status summary**

Run: `sed -n '1,260p' llm_wiki/logs/layer-count-blog-readiness.md`
Expected: `20-layer` and `22-layer` still read as blocked for public reusable high-density numeric claims unless a later acceptable evidence layer exists.
