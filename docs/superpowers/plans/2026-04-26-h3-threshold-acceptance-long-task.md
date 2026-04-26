# H3 Threshold And Acceptance Long-Task Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn `H3` into a durable multi-agent program that keeps `22-layer`, `14-layer`, and `20-layer` under explicit threshold/acceptance governance while generating execution-ready queue notes instead of ad hoc reassessment.

**Architecture:** The controller agent owns queue order, tracking docs, and final integration. Independent subagents handle read-only queue intake on disjoint branches: `22-layer` execution controls first, then `14-layer` standards/rigid-flex intake, then `20-layer` method/qualification intake. Every queue output must distinguish `metadata_only`, `public_threshold_available`, and `controlled_exclusion`, and must route unsupported claims to a draft action rather than a generic warning.

**Tech Stack:** Markdown logs under `llm_wiki/logs`, fact-boundary cards under `llm_wiki/facts`, live draft references under `/code/hileap/frontendHIL/docs/hilpcb_blog_04.24/en`, `apply_patch`, `rg`, `sed`, existing Codex subagents.

---

### Task 1: Lock The H3 Long-Task Control Surface

**Files:**
- Create: `docs/superpowers/plans/2026-04-26-h3-threshold-acceptance-long-task.md`
- Create: `llm_wiki/logs/h3-long-task-multi-agent-plan.md`
- Modify: `llm_wiki/logs/backlog.md`
- Modify: `llm_wiki/logs/phase-status.md`
- Modify: `llm_wiki/logs/update-log.md`

- [ ] **Step 1: Confirm the current H3 baseline and open queues**

Run: `sed -n '1,220p' llm_wiki/logs/h3-threshold-and-acceptance-layer-kickoff.md`
Expected: the file still defines `22-layer` first, `14-layer` second, `20-layer` third, and keeps `public_threshold_available` narrow by default.

- [ ] **Step 2: Create the durable H3 multi-agent plan note**

Write `llm_wiki/logs/h3-long-task-multi-agent-plan.md` with:
- purpose and non-goals
- queue order
- controller vs subagent ownership
- output contract per queue
- stop conditions
- sync rules for tracking docs

- [ ] **Step 3: Record the active execution order in tracking**

Update `backlog.md` and `phase-status.md` so they both say:
- `H2` is closed as governance-complete
- `H3` is active
- `22-layer` queue execution is in progress
- `14-layer` and `20-layer` queue intake are running under multi-agent control

- [ ] **Step 4: Append the plan landing to the update log**

Update `update-log.md` with one concise bullet group that records:
- H3 long-task multi-agent control is now formalized
- `22-layer` execution control note landed
- `14-layer` and `20-layer` intake were dispatched or integrated

- [ ] **Step 5: Verify the control surface is internally consistent**

Run: `rg -n "H3|22-layer|14-layer|20-layer" llm_wiki/logs/backlog.md llm_wiki/logs/phase-status.md llm_wiki/logs/h3-long-task-multi-agent-plan.md`
Expected: queue order and status language align across all three files.

### Task 2: Finish H3 Queue 1 For 22-Layer

**Files:**
- Create: `llm_wiki/logs/h3-22-layer-evidence-pack-blacklist-and-residual-wording.md`
- Modify: `llm_wiki/logs/backlog.md`
- Modify: `llm_wiki/logs/phase-status.md`
- Modify: `llm_wiki/logs/update-log.md`

- [ ] **Step 1: Re-read the queue-1 control inputs**

Run: `sed -n '1,240p' llm_wiki/logs/h3-22-layer-threshold-and-acceptance-inventory.md`
Expected: every draft cluster already maps to a claim family and default disposition.

- [ ] **Step 2: Create the execution-grade blacklist/residual-wording note**

Write `llm_wiki/logs/h3-22-layer-evidence-pack-blacklist-and-residual-wording.md` with:
- blacklist clusters
- allowed residual wording classes
- banned wording patterns
- evidence-pack actions by draft area
- completion criteria for queue closeout

- [ ] **Step 3: Mark Queue 1 as execution-ready, not numeric-unlocked**

Update tracking docs so they say Queue 1 now has:
- inventory
- source-policy split
- blacklist/residual-wording control

But also say:
- `public_threshold_available: none`
- supplier evidence is still absent
- `22-layer` remains blocked for high-density numeric reuse

- [ ] **Step 4: Verify no file overstates the outcome**

Run: `rg -n "public_threshold_available|numeric|supplier evidence|blocked" llm_wiki/logs/h3-22-layer-*.md llm_wiki/logs/backlog.md llm_wiki/logs/phase-status.md`
Expected: wording stays at control/readiness level and does not claim recovery of thresholds or supplier proof.

### Task 3: Create H3 Queue 2 Intake For 14-Layer

**Files:**
- Create: `llm_wiki/logs/h3-14-layer-threshold-and-rigid-flex-intake.md`
- Modify: `llm_wiki/logs/backlog.md`
- Modify: `llm_wiki/logs/phase-status.md`
- Modify: `llm_wiki/logs/update-log.md`

- [ ] **Step 1: Use a read-only subagent to summarize the surviving 14-layer risk load**

Read only:
- `/code/hileap/frontendHIL/docs/hilpcb_blog_04.24/en/14-layer-pcb-manufacturing.md`
- `llm_wiki/facts/standards/14-layer-standards-threshold-boundary.md`
- `llm_wiki/facts/methods/14-layer-rigid-flex-reliability-numeric-boundary.md`
- `llm_wiki/facts/materials/14-layer-flex-material-exact-product-boundary.md`
- `llm_wiki/logs/p4-06-14-layer-bridge-prep.md`
- `llm_wiki/logs/p4-06-14-layer-evidence-pack.md`
- `llm_wiki/logs/p4-06-nq-3-14-layer-special-risk-closeout.md`

Expected output: a memo listing surviving risk clusters, safe residual wording, blocked numerics/assertions, and a recommended file structure.

- [ ] **Step 2: Integrate the memo into a queue-intake note**

Write `llm_wiki/logs/h3-14-layer-threshold-and-rigid-flex-intake.md` with:
- queue purpose
- current baseline
- inventory table by draft area
- `metadata_only` vs `controlled_exclusion` split
- residual wording classes that remain safe for conservative bridge use

- [ ] **Step 3: Keep the verdict conservative**

Tracking language must preserve:
- `14-layer` may already be bridgeable conservatively under `P4-06`
- this `H3` intake is about threshold/rigid-flex control hardening
- this is not a new numeric-unlock branch

- [ ] **Step 4: Verify no H3 note accidentally reopens already closed bridge work**

Run: `rg -n "14-layer" llm_wiki/logs/h3-14-layer-threshold-and-rigid-flex-intake.md llm_wiki/logs/p4-06-14-layer-evidence-pack.md llm_wiki/logs/p4-06-nq-3-14-layer-special-risk-closeout.md`
Expected: the new H3 note sharpens exclusions without contradicting the existing conservative bridge posture.

### Task 4: Create H3 Queue 3 Intake For 20-Layer

**Files:**
- Create: `llm_wiki/logs/h3-20-layer-method-and-qualification-intake.md`
- Modify: `llm_wiki/logs/backlog.md`
- Modify: `llm_wiki/logs/phase-status.md`
- Modify: `llm_wiki/logs/update-log.md`

- [ ] **Step 1: Use a read-only subagent to summarize the surviving 20-layer blocker load**

Read only:
- `/code/hileap/frontendHIL/docs/hilpcb_blog_04.24/en/20-layer-pcb-manufacturing.md`
- `llm_wiki/facts/methods/20-layer-any-layer-hdi-rewrite-guardrail.md`
- `llm_wiki/facts/materials/20-layer-build-up-material-boundary-and-non-claims.md`
- `llm_wiki/logs/p4-13-20-layer-draft-blocker-map.md`
- `llm_wiki/logs/p4-13-20-layer-bridge-exclusion-and-downgrade-map.md`
- `llm_wiki/logs/p4-13-post-assertion-containment-reassessment.md`

Expected output: a memo listing surviving risk clusters, safe residual wording, blocked numerics/assertions, and a recommended file structure.

- [ ] **Step 2: Integrate the memo into a queue-intake note**

Write `llm_wiki/logs/h3-20-layer-method-and-qualification-intake.md` with:
- queue purpose
- current baseline
- inventory table by draft area
- `metadata_only` vs `controlled_exclusion` split
- method-name vocabulary vs qualification-proof boundary

- [ ] **Step 3: Keep 20-layer explicitly blocked for high-density numeric reuse**

Tracking language must preserve:
- geometry/process-window/HIL-assertion clusters remain blocked
- `IST` and method names remain context, not pass/fail proof
- no supplier-evidence layer exists yet

- [ ] **Step 4: Verify the intake does not broaden allowed method claims**

Run: `rg -n "IST|qualification|method|threshold|supplier" llm_wiki/logs/h3-20-layer-method-and-qualification-intake.md llm_wiki/logs/p4-13-20-layer-bridge-exclusion-and-downgrade-map.md`
Expected: method names stay governance/context-only and no acceptance proof is implied.

### Task 5: Maintain The Long-Task Loop

**Files:**
- Modify: `llm_wiki/logs/backlog.md`
- Modify: `llm_wiki/logs/phase-status.md`
- Modify: `llm_wiki/logs/update-log.md`

- [ ] **Step 1: Keep queue state explicit after each landing**

After each queue note lands, update:
- queue status
- what changed
- what remains blocked

Do not wait until the end of the wave.

- [ ] **Step 2: Preserve disjoint ownership for long-running agents**

Agent ownership rule:
- controller: plan, integration, tracking, final wording
- agent A: `22-layer` residual blacklist refinement if reopened
- agent B: `14-layer` intake
- agent C: `20-layer` intake

Do not assign overlapping write scope to subagents.

- [ ] **Step 3: Stop if the evidence ceiling has not changed**

If a pass only improves boundary precision but does not recover stronger authority, record:
- retrieval safety improved
- readiness unchanged
- blocked verdict unchanged

Do not recast that as a readiness unlock.

- [ ] **Step 4: End the wave with a queue-status summary**

Run: `sed -n '1,220p' llm_wiki/logs/layer-count-blog-readiness.md`
Expected: `20-layer` and `22-layer` still read as blocked for high-density numeric reuse unless a later supplier-evidence discipline exists.
