# P4-343 E5 Component Spacing Severity Route Integration

Date: 2026-05-09
Execution mode: `single_pdf_route_integration_only`
Model: `gpt-5.4`
Lane owner: `P4-343 E5 single-PDF route integration for 组装电子元器件间距不足的严重性.pdf`

## Purpose

Route the single article PDF `组装电子元器件间距不足的严重性.pdf` into already-landed repo-backed assembly-route and access-review surfaces where safe, while keeping the PDF as `claim_inventory_only` and blocking all article-origin spacing thresholds, solder-mask sufficiency claims, via-in-pad rules, defect-certainty claims, and tool-marketing or commercial claims.

This pass is single-PDF route integration only. It does not create or update reusable `facts/`, `wiki/`, `sources/registry/`, or trackers.

## Inputs Inspected

- `/code/blogs/tmps/PCB资料/PCB文章/组装电子元器件间距不足的严重性.pdf`
- `/code/blogs/tmps/pcb_pdf_extracted_full/组装电子元器件间距不足的严重性/pages/page-0001.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/组装电子元器件间距不足的严重性/pages/page-0002.txt`
- `/code/blogs/llm_wiki/logs/p4-313-2026-5-8-pcb-article-e5-usage-route-integration.md`
- `/code/blogs/llm_wiki/logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `/code/blogs/llm_wiki/facts/methods/selective-wave-solder-and-mixed-technology-sequencing.md`
- `/code/blogs/llm_wiki/facts/methods/selective-solder-design-access-checks.md`
- `/code/blogs/llm_wiki/facts/methods/parameter-scope-pcba-selective-solder-tht-route-context.md`
- `/code/blogs/llm_wiki/facts/methods/manual-solder-rework-boundary-for-mixed-technology.md`
- `/code/blogs/llm_wiki/facts/methods/pcba-mixed-technology-assembly-flow.md`
- `/code/blogs/llm_wiki/wiki/processes/selective-solder-fixture-and-access-planning.md`
- `/code/blogs/llm_wiki/wiki/processes/hand-solder-touchup-and-rework-control.md`
- `/code/blogs/llm_wiki/wiki/testing/pcba-quality-gates-and-test-strategy.md`

## PDF Claim Inventory

Observed article-side claim families from the extracted pages:

1. `dense_component_spacing_as_assembly_risk`
   - the article frames insufficient component-to-component spacing as an assembly-risk condition rather than only a placement-aesthetics issue
   - it links dense neighborhoods to solder shorts, weak joints, and maintenance difficulty

2. `tht_pin_via_and_pad_proximity_short_or_bridge_claim`
   - the article says connector pins, vias, installation holes, and nearby pads can be too close
   - it ties that closeness to shorting or bridging outcomes during soldering

3. `wave_route_and_parameter_language`
   - the article mentions wave-solder suitability and also blames process parameters such as speed or soldering time in one example
   - it mixes geometry-side and process-side causality in the same defect story

4. `smt_pad_via_proximity_to_insufficient_solder_claim`
   - the article says via-to-pad proximity can pull solder away, creating too little solder, cold joints, opens, or tombstoning-style outcomes
   - it treats via-in-pad and near-pad vias as one defect family

5. `missing_solder_mask_or_uncovered_copper_claim`
   - the article says uncovered conductive paths or uncovered annular rings near pads can connect to the solder joint
   - it ties this to insufficient solder, shorts, and reliability concerns

6. `manual_touchup_and_repair_obstruction_claim`
   - the article says close pad or via neighborhoods increase bridge risk during hand touch-up
   - it also says some blocked or sealed conditions can become difficult or impossible to repair

7. `reliability_and_business_outcome_language`
   - the article extends local defect anecdotes into reliability, product-quality, cost, and schedule language
   - it closes with branded checker and workflow-superiority marketing

## Existing LLM Wiki Support Found

This PDF has only limited but real overlap with current repo-backed surfaces. The overlap is posture-level, not parameter-level.

### 1. Dense neighborhoods belong in mixed-technology route planning

Safe route:
- `facts/methods/pcba-mixed-technology-assembly-flow.md`
- `facts/methods/selective-wave-solder-and-mixed-technology-sequencing.md`

Admitted reuse:
- dense SMT / THT neighborhoods can be described as part of one coordinated assembly-flow review rather than as isolated post-layout surprises
- through-hole insertion, SMT soldering, later wave or selective solder, inspection, and test belong in one route discussion
- the article can safely reinforce that close component spacing should be reviewed before committing to the downstream solder route

Boundary:
- this PDF does not add source-backed spacing limits, route-selection thresholds, or generic process settings
- it does not prove one solder route is mandatory for all dense layouts

### 2. Close spacing can be reframed as access, shielding, and thermal-review posture

Safe route:
- `facts/methods/selective-solder-design-access-checks.md`
- `wiki/processes/selective-solder-fixture-and-access-planning.md`

Admitted reuse:
- nearby parts, connector overhang, dense bottom-side neighborhoods, and obstructed joints belong in access-review language
- close THT and mixed-technology neighborhoods can be treated as reachability and nearby-hardware review inputs
- inspection handoff stays in the same route discussion when dense geometry makes soldering or rework harder

Boundary:
- this PDF only supports conservative wording that dense neighborhoods deserve access review
- it does not authorize exact keep-out rules, fixture-opening rules, nozzle assumptions, or certainty that selective solder closes the problem

### 3. Manual touch-up and rework difficulty has bounded support

Safe route:
- `facts/methods/manual-solder-rework-boundary-for-mixed-technology.md`
- `wiki/processes/hand-solder-touchup-and-rework-control.md`

Admitted reuse:
- dense neighborhoods can make manual touch-up, rework, and post-defect recovery harder
- manual intervention can be framed as controlled exception work that reconnects to inspection and revalidation
- the article can support a conservative statement that poor spacing raises serviceability and rework-control concerns

Boundary:
- this PDF does not prove any joint is unreworkable in the general case
- it does not authorize operator, temperature, dwell, or rework-count rules

### 4. Inspection and quality-gate adjacency exists, but only indirectly

Safe route:
- `wiki/testing/pcba-quality-gates-and-test-strategy.md`

Admitted reuse:
- dense-spacing defect risks should stay separate from later inspection and release-gate claims
- post-solder issues still need inspection or electrical validation in the broader quality flow

Boundary:
- this PDF does not itself add new test-method authority, coverage claims, or release criteria

### 5. Parameter scope remains blocked at article level

Safe route:
- `facts/methods/parameter-scope-pcba-selective-solder-tht-route-context.md`

Admitted reuse:
- spacing, pad, via, and route-neighborhood discussion may stay at review-context level
- any exact value later needed must come from stronger owner-scoped or primary sources

Boundary:
- this PDF cannot supply generic spacing numbers, via-to-pad numbers, solder-mask design thresholds, or acceptability defaults

## Safe Reuse Classes

1. `dense_component_spacing_requires_route_review`
   - reusable as a neutral statement that dense assembly neighborhoods should be reviewed before downstream solder-route commitment

2. `mixed_smt_tht_neighbor_access_risk_taxonomy`
   - reusable as a neutral statement that nearby pins, pads, vias, and component bodies can create access and reachability concerns

3. `manual_touchup_serviceability_risk`
   - reusable as a neutral statement that crowded neighborhoods can raise bridge risk and reduce ease of controlled rework

4. `local_pdf_scoped_mechanism_examples`
   - connector pin near via short example
   - installation hole or through-hole near pad bridge example
   - via near SMT pad solder-starvation example
   - dense-neighborhood hand-solder bridge-risk example

## Blocked Claims

The following claim families remain blocked and must not be promoted from this PDF:

1. `all_spacing_threshold_and_clearance_rules`
   - minimum component spacing values
   - pad-to-via values
   - pin-to-hole or hole-to-pad spacing values
   - any general DFM clearance default

2. `all_solder_mask_and_copper_exposure_rule_defaults`
   - universal claims that one solder-mask treatment is sufficient
   - any blanket rule for when annular rings or traces must be covered
   - any implied acceptability threshold from the article examples

3. `all_via_in_pad_and_near_pad_process_rules`
   - certainty that a near-pad via will always drain solder
   - universal via-in-pad defect outcomes
   - sealing, plugging, or covering rules from article wording alone

4. `all_defect_causality_and_certainty_claims`
   - certainty that one spacing issue alone causes shorting, cold solder, opens, tombstoning, or burning
   - certainty that parameter adjustment alone explains or fixes the outcome
   - certainty that one design-side example generalizes to all assemblies

5. `all_route_selection_superiority_claims`
   - claims that wave solder is or is not suitable based on the article alone
   - claims that selective solder or manual solder is mandatory for dense layouts
   - claims that one route universally prevents these defects

6. `all_reliability_quality_cost_and_schedule_claims`
   - reliability certainty
   - quality-improvement certainty
   - cost, cycle-time, delay, or delivery claims

7. `tool_marketing_and_checker_sufficiency_claims`
   - branded checker sufficiency
   - branded workflow superiority
   - software-check completeness or guaranteed prevention claims

## Explicit Route Decision

This article advances only to a `limited_route_support` posture above pure cluster inventory.

The narrow result is:

- it safely maps into existing repo-backed surfaces for `dense neighborhood review inside mixed-technology assembly planning`
- it safely maps into existing repo-backed surfaces for `access, shielding, and reachability review when nearby hardware crowds the solder zone`
- it safely maps into existing repo-backed surfaces for `manual touch-up and rework becoming higher-risk in crowded neighborhoods`

It does **not** justify a new fact card or wiki page from this lane.

It also does **not** justify promoting article-origin spacing values, solder-mask rules, via-in-pad rules, defect-certainty language, burned-board anecdotes, or branded checker claims into reusable facts.

If stated plainly: this PDF is useful as claim inventory and conservative route support for `crowded-neighborhood assembly-risk posture`, but strong route support remains weak because the article mixes geometry, process settings, and marketing claims without primary authority.

## Reused Repo-Backed Source / Fact / Wiki Surfaces

### Fact surfaces

- `methods-pcba-mixed-technology-assembly-flow`
  - primary safe reuse surface for keeping the article inside coordinated SMT / THT / solder / inspection route language

- `methods-selective-wave-solder-and-mixed-technology-sequencing`
  - primary safe reuse surface for keeping wave or selective mentions at route-selection posture only

- `methods-selective-solder-design-access-checks`
  - primary safe reuse surface for turning close spacing into access-review and nearby-hardware review wording

- `methods-manual-solder-rework-boundary-for-mixed-technology`
  - primary safe reuse surface for limiting hand-solder and rework claims to controlled exception-path language

- `methods-parameter-scope-pcba-selective-solder-tht-route-context`
  - primary safe reuse surface for blocking article-side geometry and route values from becoming generic rules

### Wiki surfaces

- `processes-selective-solder-fixture-and-access-planning`
  - receives the article only as support for access-planning posture, not as dimension authority

- `processes-hand-solder-touchup-and-rework-control`
  - receives the article only as support for crowded-neighborhood rework difficulty and revalidation posture

- `testing-pcba-quality-gates-and-test-strategy`
  - adjacent support only for keeping defect anecdotes separate from release-gate authority

### Existing controller log surfaces

- `p4-313`
  - this PDF remains inside the earlier `component_spacing_and_access_risk_taxonomy` safe reuse class
  - this PDF also remains inside the earlier `official_source_recovery_target` posture for assembly-oriented spacing, rework access, and pad / land-pattern intent

- `p4-309`
  - corpus status remains `usage_route_covered_at_controller_level_only`
  - this single-PDF lane does not change the broader `E5` corpus truth

## Residual Gaps

1. stronger primary or owner-scoped support for assembly-oriented component spacing and rework-access boundaries
   - needed before any spacing guidance can be stated beyond generic review posture

2. stronger source-backed treatment of via-near-pad and via-in-pad defect mechanisms
   - needed before solder-starvation or short-risk outcomes can be generalized

3. stronger source-backed treatment of solder-mask and exposed-copper boundary conditions near pads and vias
   - needed before any uncovered-copper rule can be reused

4. stronger route-selection evidence for when dense neighborhoods push wave, selective, or manual paths
   - current support is posture-level only, not threshold-level

5. no clean authority in this lane for reliability, burned-board, cost, or schedule outcomes
   - these remain blocked

## Lane Status

Status: `completed_at_single_pdf_route_level_only`

What is complete:
- the single component-spacing severity article PDF has been routed into existing mixed-technology, access-review, and rework-control posture surfaces
- safe reuse classes, blocked claims, and limited-route boundaries are explicit
- the lane now states clearly that the PDF is mostly a claim-inventory and risk-taxonomy input rather than a reusable rule source

What is not complete:
- no official-source recovery was performed
- no new `facts/`, `wiki/`, `sources/registry/`, or tracker updates were created
- no article images were preserved as local evidence
- no article-origin geometry, process, reliability, or capability claim was unlocked

## Final Lane Report

- changed file: `/code/blogs/llm_wiki/logs/p4-343-2026-5-9-e5-component-spacing-severity-route-integration.md`
- lane status: `completed_at_single_pdf_route_level_only`
- route strength: `limited_route_support`
- safe reuse classes:
  - `dense_component_spacing_requires_route_review`
  - `mixed_smt_tht_neighbor_access_risk_taxonomy`
  - `manual_touchup_serviceability_risk`
  - `local_pdf_scoped_mechanism_examples`
- blocked claims:
  - `all_spacing_threshold_and_clearance_rules`
  - `all_solder_mask_and_copper_exposure_rule_defaults`
  - `all_via_in_pad_and_near_pad_process_rules`
  - `all_defect_causality_and_certainty_claims`
  - `all_route_selection_superiority_claims`
  - `all_reliability_quality_cost_and_schedule_claims`
  - `tool_marketing_and_checker_sufficiency_claims`
- residual gaps:
  - stronger primary or owner-scoped support for assembly-oriented spacing and rework-access boundaries
  - stronger source-backed treatment of via-near-pad and via-in-pad mechanisms
  - stronger source-backed treatment of solder-mask / exposed-copper boundary conditions
  - stronger route-selection evidence for dense-neighborhood solder-path decisions
  - no clean authority for reliability, burned-board, cost, or schedule outcomes
