---
lane: "P4-43 official-source recovery scout"
input_dir: "/code/blogs/tmps/2026.4.24/en"
output_file: "/code/blogs/llm_wiki/logs/p4-43-2026-4-24-layer-count-pcb-manufacturing-official-source-recovery-scout.md"
status: "source_backed_fact_layer_partial"
checked_at: "2026-04-28"
model: "gpt-5.4"
scope_notes:
  - "tmps drafts treated as claim inventory, not authority"
  - "no tracker updates"
  - "no fact card, wiki, source-registry, or tmps edits in this lane"
---

# Purpose

Deletion-safe scout log for the 10 English layer-count PCB manufacturing drafts under `/code/blogs/tmps/2026.4.24/en`.

This lane only inventories file/topic intent, checks existing `llm_wiki` support for layer-count ingestion and adjacent governance, records which claim families are already covered at support or boundary level, and marks the remaining official-source or dated-capability gaps.

# Input File Inventory

- `6-layer-pcb-manufacturing.md`
- `8-layer-pcb-manufacturing.md`
- `10-layer-pcb-manufacturing.md`
- `12-layer-pcb-manufacturing.md`
- `14-layer-pcb-manufacturing.md`
- `16-layer-pcb-manufacturing.md`
- `18-layer-pcb-manufacturing.md`
- `20-layer-pcb-manufacturing.md`
- `22-layer-pcb-manufacturing.md`
- `24-layer-pcb-manufacturing.md`

# Existing `llm_wiki` Support Checked

## Batch-level layer-count coverage and generation gate

- `/code/blogs/llm_wiki/logs/p4-20-layer-count-claim-coverage-map.md`
- `/code/blogs/llm_wiki/logs/layer-count-blog-readiness.md`
- `/code/blogs/llm_wiki/logs/en-layer-count-blog-generation-gate.md`
- `/code/blogs/llm_wiki/logs/h0-numeric-claim-inventory.md`

## Governance for high-density, capability, and numeric containment

- `/code/blogs/llm_wiki/logs/p4-06-nq-1-shared-b-buckets-closeout.md`
- `/code/blogs/llm_wiki/logs/p4-06-nq-2-d-interpretation-guardrails-closeout.md`
- `/code/blogs/llm_wiki/logs/h2-backdrill-and-stub-bucket-decision.md`
- `/code/blogs/llm_wiki/logs/h2-testing-and-verification-capability-bucket-decision.md`
- `/code/blogs/llm_wiki/logs/h2-standards-minima-source-map.md`
- `/code/blogs/llm_wiki/logs/h3-20-layer-method-and-qualification-intake.md`
- `/code/blogs/llm_wiki/logs/h3-20-22-supplier-record-intake-template.md`

## Fact and wiki support for HDI, high-layer, backdrill, impedance, rigid-flex, and build-up context

- `/code/blogs/llm_wiki/facts/methods/high-layer-count-backdrill-and-registration-posture.md`
- `/code/blogs/llm_wiki/facts/methods/backdrill-control-capability.md`
- `/code/blogs/llm_wiki/facts/methods/controlled-impedance-tdr-verification-posture.md`
- `/code/blogs/llm_wiki/facts/methods/8-10-12-layer-impedance-and-geometry-implication-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/12-layer-high-speed-context-vs-board-guarantee-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/16-layer-pdn-and-thermal-heuristic-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/hdi-microvia-and-vippo-process-posture.md`
- `/code/blogs/llm_wiki/facts/methods/microvia-reliability-public-context.md`
- `/code/blogs/llm_wiki/facts/methods/14-layer-rigid-flex-reliability-numeric-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/rigid-flex-stackup-and-bend-reliability-posture.md`
- `/code/blogs/llm_wiki/facts/methods/20-layer-build-up-material-pages-do-not-authorize-feature-size-claims.md`
- `/code/blogs/llm_wiki/facts/methods/20-layer-interconnect-reliability-workflow-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/20-layer-process-window-and-recipe-boundary.md`
- `/code/blogs/llm_wiki/facts/standards/22-layer-class-3-and-addendum-threshold-boundary.md`
- `/code/blogs/llm_wiki/facts/standards/22-layer-clause-family-vs-threshold-boundary.md`
- `/code/blogs/llm_wiki/wiki/processes/apt-capability-family-map-and-boundaries.md`
- `/code/blogs/llm_wiki/wiki/processes/ptfe-processing-and-manufacturability.md`
- `/code/blogs/llm_wiki/wiki/processes/backplane-execution-and-connector-integration.md`
- `/code/blogs/llm_wiki/wiki/processes/ai-server-optical-module-pcb-pcba-review-map.md`

## Policy support

- `/code/blogs/llm_wiki/policies/internal-capability-taxonomy.md`

# Draft Topic / Claim Family Inventory

## Family A: batch-level layer-count architecture and article structure

Observed draft intent:

- present a staircase from `6-layer` through `24-layer`
- map each layer count to a dominant engineering pressure
- tie layer count to stackup, materials, process complexity, and validation

Disposition:

- `completed_at_claim_family_level`
- Existing batch-level support already covers the topic structure and current rewrite gate.
- No draft-specific architecture ladder should be promoted as fact without separate source-backed support per claim class.

## Family B: multilayer stackup defaults and layer-assignment recipes

Representative files:

- `6-layer-pcb-manufacturing.md`
- `8-layer-pcb-manufacturing.md`
- `10-layer-pcb-manufacturing.md`
- `12-layer-pcb-manufacturing.md`
- `16-layer-pcb-manufacturing.md`
- `24-layer-pcb-manufacturing.md`

Observed draft intent:

- default stackup patterns
- named layer-function tables
- default signal/power/ground distribution
- symmetric placement rules presented as standard recipes

Disposition:

- `source_backed_fact_layer_partial`
- Existing support covers stackup-planning posture and architecture examples.
- Default stackup tables, dielectric-spacing assumptions, embedded-capacitance numerics, and “recommended default recipe” wording remain blocked unless separately sourced.

## Family C: impedance, SI, backdrill, and validation posture

Representative files:

- `6-layer-pcb-manufacturing.md`
- `8-layer-pcb-manufacturing.md`
- `12-layer-pcb-manufacturing.md`
- `18-layer-pcb-manufacturing.md`
- `24-layer-pcb-manufacturing.md`

Observed draft intent:

- controlled-impedance framing
- via-stub and backdrill rationale
- TDR / VNA / SI verification workflow
- channel-performance, skew, and loss claims

Disposition:

- `source_backed_fact_layer_partial`
- Existing support is strong for guarded method identity, planning posture, and verification-ladder framing.
- Exact impedance tolerances, frequency ceilings, skew budgets, channel-loss budgets, and validation-package promises remain blocked pending official source plus dated capability record where supplier-specific.

## Family D: HDI, microvia, BGA escape, and build-up constructions

Representative files:

- `8-layer-pcb-manufacturing.md`
- `10-layer-pcb-manufacturing.md`
- `12-layer-pcb-manufacturing.md`
- `20-layer-pcb-manufacturing.md`

Observed draft intent:

- blind/buried via and microvia framing
- BGA escape routing pressure
- `1+8+1`, `2+6+2`, any-layer, and build-up context
- sequential lamination and density-driven routing claims

Disposition:

- `source_backed_fact_layer_partial`
- Existing support covers HDI/microvia vocabulary, process posture, and `20-layer` build-up governance boundaries.
- Pitch-by-pitch BGA escape tables, layer-span defaults, capture-pad and geometry rules, microvia reliability thresholds, and shop-capability proof remain blocked.

## Family E: rigid-flex and flex-reliability branch

Representative files:

- `6-layer-pcb-manufacturing.md`
- `8-layer-pcb-manufacturing.md`
- `14-layer-pcb-manufacturing.md`

Observed draft intent:

- rigid-flex as a layer-count branch
- polyimide and flex-material framing
- bend-radius, transition-zone, and dynamic-flex reliability claims
- `IPC-6013`-adjacent marketing language

Disposition:

- `source_backed_fact_layer_partial`
- Existing support covers rigid-vs-rigid-flex framing, posture, and numeric-boundary control.
- Bend-life, bend-radius tables, dynamic-flex survivability, `IPC-6013` threshold leakage, and supplier-proof reliability claims remain blocked.

## Family F: high-layer power, thermal, and heavy-copper outcome framing

Representative files:

- `16-layer-pcb-manufacturing.md`
- `24-layer-pcb-manufacturing.md`

Observed draft intent:

- PDN planning
- thermal dissipation and current-density outcome claims
- heavy-copper and large-format process sensitivity

Disposition:

- `source_backed_fact_layer_partial`
- Existing support covers planning posture and heuristic-boundary containment.
- Thermal-outcome tables, current-density limits, copper-thickness capability defaults, and performance guarantees remain blocked pending stronger official sources and dated capability records.

## Family G: standards, hi-rel, qualification, and acceptance authority

Representative files:

- `14-layer-pcb-manufacturing.md`
- `20-layer-pcb-manufacturing.md`
- `22-layer-pcb-manufacturing.md`

Observed draft intent:

- `IPC Class 3`, `IPC-6013`, `IPC-6012` and addendum framing
- qualification, lot-conformance, and release-authority implications
- supplier-status and compliance-style marketing

Disposition:

- `source_backed_fact_layer_partial`
- Existing support is usable for metadata-level hierarchy and guardrail control.
- Threshold tables, acceptance criteria, supplier approval, compliance proof, qualification success, and accepted-lot claims remain blocked.

## Family H: commercial and supplier-specific capability claims

Observed draft intent:

- lead time, quick-turn, prototype-to-production, and cost uplift claims
- shop-specific tolerance, yield, inspection-coverage, and engineering-support claims
- region/customer references used as proof signals

Disposition:

- `blocked_pending_dated_capability_record`
- Current corpus governance already treats these as non-reusable without dated scoped records.
- No draft-originated commercial or supplier-proof claim is safe to promote from this batch.

# Per-Draft Disposition

| Draft | Current batch posture | Safe reuse from existing support | Main blocked classes |
| --- | --- | --- | --- |
| `6-layer-pcb-manufacturing.md` | `source_backed_fact_layer_partial` | multilayer entry-point framing, material-category branching, validation posture | generic FR-4 numeric ladders, stackup defaults, impedance geometry, cost uplift, supplier capability |
| `8-layer-pcb-manufacturing.md` | `source_backed_fact_layer_partial` | mixed-signal / EMC planning context, architecture framing, HDI adjacency | EMC dB claims, embedded-capacitance numerics, rigid-flex numerics, capability tables |
| `10-layer-pcb-manufacturing.md` | `source_backed_fact_layer_partial` | HDI vocabulary, BGA-density pressure, architecture examples | pitch tables, blind/buried-via capability, `1+8+1` / `2+6+2` defaults, registration and cost claims |
| `12-layer-pcb-manufacturing.md` | `source_backed_fact_layer_partial` | high-speed system context, backdrill rationale, validation workflow | `GHz`, `ps`, exact impedance / skew / depth claims, VNA commitments, turnaround claims |
| `14-layer-pcb-manufacturing.md` | `source_backed_fact_layer_partial` | rigid-vs-rigid-flex branch framing, transition-zone review, material-class context | `IPC-6013` threshold leakage, bend-life tables, dynamic-flex proof, compliance-style claims |
| `16-layer-pcb-manufacturing.md` | `source_backed_fact_layer_partial` | power-dense planning posture, heavy-copper workflow context | PDN heuristics as hard rules, thermal outcomes, process-window numerics, lead-time claims |
| `18-layer-pcb-manufacturing.md` | `source_backed_fact_layer_partial` | hybrid RF/digital material framing, PTFE and backdrill posture, validation workflow | RF geometry, impedance tolerance, insertion-loss or frequency promises, cost multipliers |
| `20-layer-pcb-manufacturing.md` | `blocked_pending_dated_capability_record` | guarded build-up / any-layer vocabulary, reliability-workflow context | stacked-microvia proof, process-control numerics, geometry tables, HIL capability, yield/cost/lead-time |
| `22-layer-pcb-manufacturing.md` | `blocked_pending_dated_capability_record` | hi-rel workflow vocabulary, addendum hierarchy, traceability and lot-conformance context | class thresholds, supplier approval, compliance proof, acceptance authority, commercial claims |
| `24-layer-pcb-manufacturing.md` | `source_backed_fact_layer_partial` | high-speed system context, material ladder, large-panel sensitivity, workflow validation posture | `112G` budgets, insertion-loss tables, exact VNA scope, production proof, scrap/cycle/lead-time numerics |

# Safe Reuse Classes

These can be reused conservatively from current `llm_wiki` support without treating the tmps drafts as authority.

- batch-level generation gate and coverage-map conclusions for the 10 layer-count topics
- architecture-pressure wording:
  `6-layer` as multilayer entry point, `10-layer` as HDI/BGA density pressure, `12-layer` and `24-layer` as high-speed planning context, `14-layer` as rigid-vs-rigid-flex branch, `20/22-layer` as guarded governance branches
- workflow posture:
  high-layer registration sensitivity, sequential-lamination planning, backdrill rationale, TDR/VNA as validation-ladder components
- HDI/build-up vocabulary:
  microvia, blind/buried via, build-up, any-layer, VIPPO, and density-first framing only where existing boundary cards already support guarded usage
- rigid-flex posture:
  rigid/flex transition planning, bend-zone sensitivity, polyimide/flex-material context without numeric reliability promises
- standards metadata:
  hierarchy and identity framing for `IPC-6012` / addendum and `IPC-6013`-adjacent vocabulary, not thresholds
- material-context reuse:
  exact-product material cards or guarded family-level context where `llm_wiki` already limits scope

# Blocked Claim Classes

These classes should remain blocked for this batch unless later recovery lands official primary sources or dated supplier records.

- draft-originated layer-count capability maxima, stackup defaults, and process-limit tables
- exact impedance tolerances, skew budgets, insertion-loss budgets, channel-performance outcomes, and frequency ceilings
- via, trace, spacing, aspect-ratio, registration, residual-stub, lamination-count, and thickness capability numerics
- BGA escape tables by pitch, fanout-channel counts, and HDI geometry defaults
- bend-radius, dynamic-flex cycle-life, rigid-flex transition tolerance, and generic `IPC-6013` threshold claims
- supplier-specific build quality, certification, qualification, acceptance, or compliance claims
- lead time, prototype-turn, price, MOQ, yield, quality rate, and defect-rate claims
- HIL-specific “we fabricate” or “our capability” assertions without dated capability record support
- legal or IP conclusions, trademark-equivalence claims, or substitution conclusions

# Official-Source Gaps

## Gap 1: dated capability records for reusable fabrication numbers

Status:

- `blocked_pending_dated_capability_record`

Needed for:

- reusable `trace/space`, drill/microvia, registration, backdrill depth/stub, thickness, impedance-tolerance, and verification-scope claims

Current support ceiling:

- public-site scoped parameters and internal posture cards exist, but they do not become normalized factory capability facts

## Gap 2: official support for layer-count-specific stackup or routing defaults

Status:

- `blocked_pending_official_source`

Needed for:

- any future attempt to publish default `6/8/10/12/16/24-layer` stackup tables or BGA escape rules as authoritative rather than illustrative

Current support ceiling:

- existing corpus supports planning posture and examples, not universal default recipes

## Gap 3: rigid-flex reliability and standards-threshold source layer

Status:

- `blocked_pending_official_source`

Needed for:

- any future `14-layer` rewrite that wants numeric bend guidance, threshold-level `IPC-6013` language, or stronger released-lot/reliability wording

Current support ceiling:

- posture and boundary control only

## Gap 4: high-speed validation-package authority

Status:

- `blocked_pending_official_source`

Needed for:

- exact TDR / VNA / insertion-loss / skew / frequency package claims in `12-layer`, `18-layer`, and `24-layer`

Current support ceiling:

- workflow-level validation framing only, not universal package promises

## Gap 5: supplier-evidence layer for `20-layer` and `22-layer`

Status:

- `blocked_pending_dated_capability_record`

Needed for:

- any reopening of `20-layer` or `22-layer` capability, qualification, acceptance, or commercial proof claims

Current support ceiling:

- governance and containment are already strong, but the missing evidence is now mainly supplier-record authority rather than public-metadata discovery

# Recommended Next Recovery Lanes

1. `Tier 1 dated capability record lane` for reusable fabrication numbers across `trace/space`, drill/microvia, registration, impedance tolerance, backdrill/stub, and validation scope.
2. `High-speed validation boundary lane` for exact method/package separation around TDR, VNA, coupon, channel, and pass/fail wording used by `12-layer`, `18-layer`, and `24-layer`.
3. `Rigid-flex reliability source lane` for official bend, transition, and `IPC-6013`-adjacent metadata that can narrow the `14-layer` branch without importing thresholds from drafts.
4. `20-layer supplier-record lane` using the existing intake template, limited to dated scoped evidence for capability/process-control/commercial claims if the business truly needs those claims.
5. `22-layer supplier-record lane` using the same governed intake path for qualification, compliance, lot-conformance, or acceptance assertions.

# Lane Status

- Batch support is already broad at governance and claim-family level.
- Existing `llm_wiki` coverage is sufficient for deletion-safe intake and conservative rewrite containment across the batch.
- The main unresolved ceiling is not topic discovery; it is missing official or dated supplier authority for numeric capability, qualification, and commercial claim classes.
- Overall lane status: `source_backed_fact_layer_partial`.
