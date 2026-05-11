# P4-339 E5 DIP/THT Route Integration

Date: 2026-05-09
Execution mode: `single_pdf_route_integration_only`
Model: `gpt-5.4`
Lane owner: `P4-339 E5 single-PDF route integration for DIP/THT pitfalls article`

## Purpose

Route the single article PDF `那些关于DIP器件不得不说的坑.pdf` into already-landed repo-backed THT / selective-solder route-boundary surfaces where safe, while keeping the PDF as `claim_inventory_only` and blocking all article-origin hole-size rules, lead-diameter rules, pitch rules, bridging-causality certainty, software-check coverage claims, and cost / yield / delivery claims.

This pass is single-PDF route integration only. It does not create or update reusable `facts/`, `wiki/`, `sources/registry/`, or trackers.

## Inputs Inspected

- `/code/blogs/tmps/PCB资料/PCB文章/那些关于DIP器件不得不说的坑.pdf`
- `/code/blogs/tmps/pcb_pdf_extracted_full/那些关于DIP器件不得不说的坑/pages/page-0001.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/那些关于DIP器件不得不说的坑/pages/page-0002.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/那些关于DIP器件不得不说的坑/pages/page-0003.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/那些关于DIP器件不得不说的坑/pages/page-0004.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/那些关于DIP器件不得不说的坑/pages/page-0005.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/那些关于DIP器件不得不说的坑/pages/page-0006.txt`
- `/code/blogs/llm_wiki/logs/p4-313-2026-5-8-pcb-article-e5-usage-route-integration.md`
- `/code/blogs/llm_wiki/logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `/code/blogs/llm_wiki/facts/methods/selective-wave-solder-and-mixed-technology-sequencing.md`
- `/code/blogs/llm_wiki/facts/methods/parameter-scope-pcba-selective-solder-tht-route-context.md`
- `/code/blogs/llm_wiki/facts/methods/selective-solder-design-access-checks.md`
- `/code/blogs/llm_wiki/wiki/processes/selective-solder-fixture-and-access-planning.md`

## PDF Claim Inventory

Observed article-side claim families from the extracted pages:

1. `dip_package_and_tht_insertion_identity`
   - the article frames DIP as a through-hole insertion package family
   - it ties DIP assembly problems to hole / lead / pitch compatibility at insertion and soldering time

2. `hole_oversize_to_looseness_and_insufficient_solder_claim`
   - the article says PCB hole size can be too large for the real component lead
   - it ties oversize holes to loose fit, insufficient solder, and empty-solder examples after wave solder

3. `hole_undersize_to_insertion_failure_and_rework_claim`
   - the article says PCB hole size can be too small for the component lead
   - it ties undersize holes to insertion failure and then to painful board-side recovery or remake outcomes

4. `lead_pitch_mismatch_to_insertion_failure_claim`
   - the article says lead pitch mismatch between footprint and component can make the part unusable
   - it presents a connector example with mismatched pin spacing

5. `close_hole_spacing_to_wave_bridge_risk_claim`
   - the article says closely spaced through-hole pins can increase bridge risk during wave solder
   - it also admits wave-solder bridging has multiple causes beyond one design-side factor

6. `case_outcome_and_reliability_language`
   - the article extends one insufficient-solder case into stability, product-performance, and safety-risk wording

7. `software_checker_scope_and_cost_time_claims`
   - the article promotes branded DFM checks for THT lead-related review
   - it claims earlier checking can avoid production delay and research cost waste

## Existing Repo-Backed Support Found

This PDF has only partial overlap with the cited repo-backed surfaces, and the overlap is conservative.

### 1. Mixed-technology route selection and wave/selective posture

Safe route:
- `facts/methods/selective-wave-solder-and-mixed-technology-sequencing.md`
- `facts/methods/parameter-scope-pcba-selective-solder-tht-route-context.md`

Admitted reuse:
- through-hole soldering belongs inside a staged mixed-technology assembly route rather than as an isolated post-layout event
- wave solder and selective solder should be framed as route choices influenced by board population and nearby constraints
- THT discussion can safely reuse route-stage vocabulary such as insertion, solder-route choice, and post-solder inspection context

Boundary:
- this PDF can reinforce that DIP / THT problems belong in route planning before solder execution
- it does not add source-backed hole-size rules, lead-diameter clearance rules, pitch limits, bridge thresholds, or generic process settings

### 2. Access, shielding, and nearby-hardware review for THT solder routes

Safe route:
- `facts/methods/selective-solder-design-access-checks.md`
- `wiki/processes/selective-solder-fixture-and-access-planning.md`

Admitted reuse:
- close THT neighborhoods can be treated as an access-planning and solder-route review issue
- nearby geometry, dense populations, and reachability concerns belong in pre-solder review
- inspection handoff after THT soldering belongs in the same route discussion

Boundary:
- this PDF can only support conservative wording that dense THT layouts deserve route and access review
- it does not prove that any one close-pitch layout will bridge, that selective solder is mandatory, or that fixture planning alone closes the risk

### 3. THT parameter scope as page-context only, not general rule authority

Safe route:
- `facts/methods/parameter-scope-pcba-selective-solder-tht-route-context.md`

Admitted reuse:
- THT geometry discussion may be kept at the review-context layer
- exact values, if later needed, must come from named owner-scoped component datasheets or stronger primary sources

Boundary:
- this PDF is useful for identifying review targets such as `lead versus hole compatibility` and `pitch compatibility`
- it does not authorize any specific dimension, tolerance, or acceptability rule from the article examples

## Safe Reuse Classes

1. `dip_tht_fit_review_identity`
   - reusable as a neutral statement that DIP / THT assembly review starts with lead, hole, and pitch compatibility before insertion and solder-route execution

2. `tht_route_context_before_wave_or_selective_solder`
   - reusable as a neutral statement that THT fit problems should be caught before downstream wave or selective solder operations

3. `dense_tht_neighborhood_requires_access_review`
   - reusable only through the existing selective-solder access-planning surfaces, not as a new direct rule from this PDF

4. `local_pdf_scoped_mechanism_examples`
   - oversize hole to loose-fit / insufficient-solder example
   - undersize hole to insertion-failure example
   - pitch mismatch to insertion-failure example
   - close-pitch wave-bridge risk example

## Explicit Route Decision

This article only partially advances above pure cluster inventory.

The important narrow result is:

- it maps into existing source-backed posture pages for `THT / DIP review as part of mixed-technology route planning`
- it maps into existing source-backed posture pages for `dense through-hole solder neighborhoods as access-review inputs`
- it maps into existing route-boundary posture for `THT geometry discussion must stay owner-scoped or primary-source-backed before dimensions are reused`

It does **not** justify a new fact card or wiki page from this lane.

It also does **not** justify promoting article-origin hole sizes, lead diameters, pitch values, bridge-risk certainty, safety-outcome claims, or branded THT checker coverage into reusable facts.

If stated plainly: this article mostly supplies claim inventory for THT fit and wave-solder-risk review, then maps that inventory into already-landed mixed-technology and selective-solder access-boundary surfaces.

## Blocked Claims

The following claim families remain blocked and must not be promoted from this PDF:

1. `all_hole_size_lead_diameter_and_tolerance_rules`
   - hole-size examples
   - lead-diameter examples
   - drilling or plating tolerance statements
   - any implied clearance default between hole and lead

2. `all_pitch_spacing_and_bridge_threshold_rules`
   - pitch values from article examples
   - minimum hole-spacing conclusions
   - any claim that one spacing value predicts bridge-free or bridge-prone assembly

3. `all_insertion_failure_or_rework_certainty_claims`
   - certainty that one mismatch always forces one recovery path
   - certainty that multilayer boards always require one universal remediation outcome

4. `all_wave_solder_causality_overclaims`
   - claims that close pitch alone explains wave bridging
   - claims that design-side geometry alone explains insufficient solder or open solder
   - claims that one route choice alone prevents those defects

5. `reliability_performance_and_safety_outcome_claims`
   - product-performance degradation certainty
   - safety-hazard certainty
   - stability or lifetime conclusions from one article case

6. `tool_marketing_and_checker_coverage_claims`
   - branded DFM sufficiency
   - completeness of THT lead-related checks
   - workflow-superiority claims from the article software section

7. `cost_time_yield_and_delivery_claims`
   - production-delay avoidance certainty
   - R&D cost savings certainty
   - yield, throughput, or delivery improvement claims

## Reused Repo-Backed Source / Fact / Wiki Surfaces

### Fact surfaces

- `methods-selective-wave-solder-and-mixed-technology-sequencing`
  - primary safe reuse surface for keeping the article inside mixed-technology SMT-first plus THT solder-route planning language

- `methods-parameter-scope-pcba-selective-solder-tht-route-context`
  - primary safe reuse surface for keeping article-side THT geometry references at route-context level only

- `methods-selective-solder-design-access-checks`
  - primary safe reuse surface for turning close THT spacing into access-review and nearby-hardware review wording instead of direct dimensional rules

### Wiki surfaces

- `processes-selective-solder-fixture-and-access-planning`
  - receives the article only as conservative support for access-planning and route-selection posture, not as parameter authority

### Existing controller log surfaces

- `p4-313`
  - this PDF remains inside the earlier `dip_tht_fit_and_wave_solder_risk_taxonomy` safe reuse class
  - this PDF also remains inside the earlier `official_source_recovery_target` posture for `tht connector and dip package datasheet guidance`

- `p4-309`
  - corpus status remains `usage_route_covered_at_controller_level_only`
  - this single-PDF lane does not change the broader `E5` corpus truth

## Residual Gaps

1. owner-scoped component and connector datasheets for lead diameter, recommended finished hole, and pitch intent
   - needed before any hole / lead / pitch relationship can be promoted

2. stronger primary-source support for THT bridge-risk design boundaries
   - needed before any close-pitch, hole-spacing, or wave-bridge design rule can be stated

3. stronger source-backed split between wave, selective, and manual THT routes for dense connector neighborhoods
   - current reuse supports route posture, not route-selection thresholds

4. stronger source-backed linkage between THT fit mismatch and downstream joint-quality failure modes
   - needed before empty-solder, insufficient-solder, or reliability outcomes can be generalized

5. no clean authority in this lane for article-side commercial or safety-impact wording
   - these remain blocked

## Lane Status

Status: `completed_at_single_pdf_route_level_only`

What is complete:
- the single DIP / THT pitfalls article PDF has been routed into existing mixed-technology and selective-solder access-boundary surfaces
- safe reuse classes and blocked claim classes are explicit
- the lane now states clearly that the PDF mainly contributes THT fit-review claim inventory rather than reusable dimensional authority

What is not complete:
- no official-source recovery was performed
- no new `facts/`, `wiki/`, `sources/registry/`, or tracker updates were created
- no article images were preserved as local evidence
- no article-origin dimensional, reliability, or capability claim was unlocked

## Final Lane Report

Changed files:
- `/code/blogs/llm_wiki/logs/p4-339-2026-5-9-e5-dip-tht-route-integration.md`

Lane status:
- `completed_at_single_pdf_route_level_only`

Safe reuse classes:
- DIP / THT fit-review identity before insertion and solder-route execution
- THT route-context review before wave or selective solder
- dense THT neighborhood as access-review input only
- local PDF-scoped mechanism examples only

Blocked claims:
- hole-size, lead-diameter, and tolerance rules
- pitch, spacing, and bridge-threshold rules
- insertion-failure and rework-certainty claims
- wave-solder causality overclaims
- reliability, performance, and safety-outcome claims
- tool-marketing and checker-coverage claims
- cost, time, yield, and delivery claims

Reused repo-backed source / fact / wiki surfaces:
- `facts/methods/selective-wave-solder-and-mixed-technology-sequencing.md`
- `facts/methods/parameter-scope-pcba-selective-solder-tht-route-context.md`
- `facts/methods/selective-solder-design-access-checks.md`
- `wiki/processes/selective-solder-fixture-and-access-planning.md`
- `logs/p4-313-2026-5-8-pcb-article-e5-usage-route-integration.md`
- `logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`

Residual gaps:
- owner-scoped DIP / connector datasheet recovery for dimensions
- stronger bridge-risk and route-selection authority
- stronger THT fit-mismatch to solder-outcome authority
- no authority here for commercial or safety-impact claims
