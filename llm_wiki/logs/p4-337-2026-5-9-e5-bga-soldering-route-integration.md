# P4-337 E5 BGA Soldering Route Integration

Date: 2026-05-09
Execution mode: `single_pdf_route_integration_only`
Model: `gpt-5.4`
Lane owner: `P4-337 E5 single-PDF route integration for BGA soldering issues article`

## Purpose

Route the single article PDF `你想知道的BGA焊接问题都在这里.pdf` into already-landed repo-backed BGA process and hidden-joint inspection surfaces where safe, while keeping the PDF as `claim_inventory_only` and blocking all article-origin numeric design rules, vendor-tool checks, process-capability claims, quality-yield claims, and assembly-acceptance claims.

This pass is single-PDF route integration only. It does not create or update reusable `facts/`, `wiki/`, `sources/registry/`, or trackers.

## Inputs Inspected

- `/code/blogs/tmps/PCB资料/PCB文章/你想知道的BGA焊接问题都在这里.pdf`
- `/code/blogs/tmps/pcb_pdf_extracted_full/你想知道的BGA焊接问题都在这里/pages/page-0001.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/你想知道的BGA焊接问题都在这里/pages/page-0002.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/你想知道的BGA焊接问题都在这里/pages/page-0003.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/你想知道的BGA焊接问题都在这里/pages/page-0004.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/你想知道的BGA焊接问题都在这里/pages/page-0005.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/你想知道的BGA焊接问题都在这里/pages/page-0006.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/你想知道的BGA焊接问题都在这里/pages/page-0007.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/你想知道的BGA焊接问题都在这里/pages/page-0008.txt`
- `/code/blogs/llm_wiki/logs/p4-313-2026-5-8-pcb-article-e5-usage-route-integration.md`
- `/code/blogs/llm_wiki/logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `/code/blogs/llm_wiki/facts/methods/low-void-bga-reflow-paste-vs-assembly-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/low-void-bga-dfm-to-process-review.md`
- `/code/blogs/llm_wiki/facts/methods/hidden-joint-xray-inspection-boundary.md`
- `/code/blogs/llm_wiki/wiki/processes/low-void-bga-reflow-and-hidden-joint-inspection.md`

## PDF Claim Inventory

Observed article-side claim families from the extracted pages:

1. `bga_package_identity_and_dense_escape_pressure`
   - BGA is described as a ball-grid package with bottom-side solder balls
   - the article frames BGA as a dense package whose escape routing can become constrained

2. `between_pad_escape_and_via_in_pad_escalation`
   - the article says some BGA pitch situations do not permit between-pad escape routing
   - it then escalates to via-in-pad and HDI-style routing as a solution family

3. `via_in_pad_fill_and_planarization_need`
   - the article says via-in-pad requires resin fill and plated planarization treatment
   - it ties untreated pad holes to solder loss and later soldering problems

4. `bga_area_via_blocking_and_reflow_side_effects`
   - the article says vias in the BGA area should be blocked / filled
   - it ties that treatment to solder migration and opposite-side defects during reflow

5. `assembly_sequence_identity`
   - the article names stencil printing, placement, reflow, and X-ray inspection as stages in the BGA assembly flow

6. `reflow_profile_as_quality_sensitive_step`
   - the article says reflow profile setup affects soldering outcomes
   - it lists defect examples when the profile is inappropriate

7. `xray_for_hidden_joint_visibility`
   - the article says X-ray is especially important for BGA and similar hidden-joint packages
   - it frames X-ray as a visibility step after reflow

8. `pad_uniformity_and_mask_opening_claims`
   - the article makes pad-size consistency, routing takeoff, and solder-mask opening claims
   - it presents these as direct BGA solderability and yield drivers

9. `tool_marketing_and_ratio_rule_checks`
   - the article promotes branded DFM checks
   - it makes cost, quality, and pad-to-ball ratio claims through those tool checks

## Existing Repo-Backed Support Found

This PDF does have overlap with existing repo-backed surfaces, but only at conservative process-boundary level.

### 1. BGA as staged DFM-to-process review

Safe route:
- `facts/methods/low-void-bga-dfm-to-process-review.md`
- `wiki/processes/low-void-bga-reflow-and-hidden-joint-inspection.md`

Admitted reuse:
- dense BGA handling belongs in a staged review chain rather than one isolated design or oven choice
- print planning, placement, reflow, hidden-joint inspection, and first-build confirmation belong to one linked process posture
- BGA density and hidden-joint structure justify conservative process-review language

Boundary:
- this PDF can reinforce that BGA soldering should be routed through a multi-step review chain
- it does not add source-backed BGA land-pattern geometry, pad sizing, escape-count rules, via treatment defaults, or release criteria

### 2. Reflow as paste-and-assembly-dependent profiling context

Safe route:
- `facts/methods/low-void-bga-reflow-paste-vs-assembly-boundary.md`
- `wiki/processes/low-void-bga-reflow-and-hidden-joint-inspection.md`

Admitted reuse:
- reflow belongs to measured process profiling rather than generic recipe reuse
- paste transfer, board context, package density, and profiling should stay linked
- guarded wording such as `requires process review`, `must be profiled on the real board`, and `assembly-dependent` is supported

Boundary:
- this PDF can only map into the existing reflow-boundary posture
- it does not prove profile windows, void percentages, peak temperatures, TAL, ramp rates, or defect-prevention certainty

### 3. X-ray as hidden-joint visibility boundary

Safe route:
- `facts/methods/hidden-joint-xray-inspection-boundary.md`
- `wiki/processes/low-void-bga-reflow-and-hidden-joint-inspection.md`

Admitted reuse:
- BGA belongs to the hidden-joint inspection lane where visual access is limited
- X-ray can be described as the visibility layer for concealed solder joints and internal solder features
- X-ray belongs in a layered inspection flow rather than as a standalone acceptance proof

Boundary:
- this PDF can reinforce the use of X-ray / AXI language for hidden-joint visibility
- it does not add universal acceptance thresholds, mandatory coverage rules, CT requirements, or proof that X-ray alone closes assembly risk

## Safe Reuse Classes

1. `bga_dense_package_and_hidden_joint_identity`
   - reusable as a neutral statement that BGA is a dense bottom-terminated package family with concealed solder-joint inspection pressure

2. `bga_process_chain_identity`
   - reusable as a neutral sequence that stencil print, placement, reflow, and hidden-joint inspection belong to one staged assembly flow

3. `reflow_requires_board_specific_process_review`
   - reusable only through the existing BGA reflow boundary surfaces, not as a new direct fact from this PDF

4. `xray_as_visibility_layer_for_bga_joints`
   - reusable only as hidden-joint inspection language through the existing X-ray boundary surfaces

5. `local_pdf_scoped_mechanism_examples`
   - untreated via-in-pad causing solder-loss risk
   - dense BGA escape pressure leading to via-in-pad / HDI escalation
   - hidden-joint inspection visibility need after reflow

## Explicit Route Decision

This article partially advances above pure cluster inventory, but only by mapping into already-landed BGA process-boundary pages.

The important narrow result is:

- it maps into existing source-backed posture pages for `BGA as a staged DFM-to-process-review lane`
- it maps into existing source-backed posture pages for `reflow as paste-and-assembly-dependent profiling context`
- it maps into existing source-backed posture pages for `X-ray as hidden-joint visibility rather than universal acceptance proof`

It does **not** justify a new fact card or wiki page from this lane.

It also does **not** justify promoting article-origin pad geometry, pitch thresholds, ratio rules, via-fill defaults, solder-mask opening numbers, quality-yield claims, or branded DFM checker outputs into reusable facts.

If stated plainly: this article mostly maps into existing source-backed BGA process and inspection posture rather than adding new source-backed knowledge.

## Blocked Claims

The following claim families remain blocked and must not be promoted from this PDF:

1. `all_pitch_escape_geometry_and_line_space_rules`
   - any specific pitch threshold for between-pad routing
   - any statement that two traces can or cannot route between pads by one universal number
   - any line-width, spacing, or manufacturability default inferred from the article

2. `all_via_in_pad_treatment_defaults`
   - universal resin-fill or planarization requirements stated without primary package or fabrication authority
   - claims that one via treatment always solves BGA solderability
   - HDI necessity claims stated as universal rules rather than case-dependent escalation

3. `all_pad_ball_ratio_and_takeoff_rules`
   - pad-to-ball ratio percentages
   - routing takeoff percentage or diameter rules
   - any claim that crossing a stated ratio directly predicts soldering success or failure

4. `all_mask_opening_and_pad_uniformity_numerics`
   - solder-mask opening numbers
   - copper opening equality rules
   - universal pad-uniformity rules stated from article text alone

5. `quality_yield_reliability_and_acceptance_claims`
   - statements that certain article-side treatments guarantee quality, yield, reliability, or acceptability
   - claims that a listed defect mechanism always causes a specific assembly outcome

6. `xray_coverage_and_acceptance_overclaims`
   - X-ray can inspect almost everything
   - X-ray alone can judge solder quality by comparison to one standard shape
   - mandatory coverage or universal acceptance conclusions for BGA

7. `tool_marketing_and_factory_capability_claims`
   - branded DFM sufficiency
   - branded checker superiority
   - cost-reduction, manufacturability, or review-completeness claims tied only to the article tool workflow

8. `commercial_cost_and_delivery_claims`
   - via-in-pad cost certainty
   - production-loss prevention certainty
   - any factory capability or economics claim not backed by dated capability records or primary sources

## Reused Repo-Backed Source / Fact / Wiki Surfaces

### Fact surfaces

- `methods-low-void-bga-dfm-to-process-review`
  - primary safe reuse surface for turning the article into staged BGA process-review language

- `methods-low-void-bga-reflow-paste-vs-assembly-boundary`
  - primary safe reuse surface for keeping reflow discussion in board-specific profiling posture

- `methods-hidden-joint-xray-inspection-boundary`
  - primary safe reuse surface for converting article-side X-ray language into hidden-joint visibility boundary wording

### Wiki surfaces

- `processes-low-void-bga-reflow-and-hidden-joint-inspection`
  - receives the article only as route support for staged BGA process and inspection posture, not as parameter authority

### Existing controller log surfaces

- `p4-313`
  - this PDF remains inside the earlier `bga_soldering_issue_taxonomy` safe reuse class
  - this PDF also remains inside the earlier `official_source_recovery_target` posture for BGA package and board-assembly guidance

- `p4-309`
  - corpus status remains `usage_route_covered_at_controller_level_only`
  - this single-PDF lane does not change the broader `E5` corpus truth

## Residual Gaps

1. primary-source support for BGA land-pattern and escape-routing boundaries
   - needed before any pad geometry, pitch, trace-count, or routing takeoff rule can be promoted

2. primary-source support for via-in-pad treatment boundaries
   - needed before resin fill, plated overfill, planarization, or HDI-escalation language can move above conservative mechanism examples

3. stronger source-backed treatment for hidden-joint inspection coverage and acceptance
   - current reuse only supports visibility-boundary wording, not acceptance thresholds or coverage percentages

4. primary-source support for BGA defect-mechanism-to-inspection linkage
   - needed before specific article defect examples can be converted into reusable diagnostic guidance

## Status

`source_backed_route_available_for_bga_process_and_hidden_joint_inspection_only`
