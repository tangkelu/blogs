# P4-335 E5 Stencil And Paste Route Integration

Date: 2026-05-09
Execution mode: `single_pdf_route_integration_only`
Model: `gpt-5.4`
Lane owner: `P4-335 E5 single-PDF route integration for stencil and paste-transfer article`

## Purpose

Route the single article PDF `如何避免踩坑钢网.pdf` into already-landed repo-backed surfaces where safe, while keeping the PDF as `claim_inventory_only` and blocking all article-origin numeric rules, process-capability claims, tool-marketing claims, and delivery claims.

This pass is single-PDF route integration only. It does not create or update reusable `facts/`, `wiki/`, `sources/registry/`, or trackers.

## Inputs Inspected

- `/code/blogs/tmps/PCB资料/PCB文章/如何避免踩坑钢网.pdf`
- `/code/blogs/tmps/pcb_pdf_extracted_full/如何避免踩坑钢网/pages/page-0001.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/如何避免踩坑钢网/pages/page-0002.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/如何避免踩坑钢网/pages/page-0003.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/如何避免踩坑钢网/pages/page-0004.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/如何避免踩坑钢网/pages/page-0005.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/如何避免踩坑钢网/pages/page-0006.txt`
- `/code/blogs/llm_wiki/logs/p4-313-2026-5-8-pcb-article-e5-usage-route-integration.md`
- `/code/blogs/llm_wiki/logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `/code/blogs/llm_wiki/facts/methods/pcba-stencil-selective-solder-and-fine-pitch-controls.md`
- `/code/blogs/llm_wiki/facts/methods/selective-wave-solder-and-mixed-technology-sequencing.md`
- `/code/blogs/llm_wiki/wiki/processes/mixed-technology-solder-route-selection.md`
- `/code/blogs/llm_wiki/wiki/testing/pcba-quality-gates-and-test-strategy.md`

## PDF Claim Inventory

Observed article-side claim families from the extracted pages:

1. `stencil_purpose_and_paste_layer_identity`
   - stencil is framed as the transfer tool for putting solder paste onto PCB pads
   - paste layer / steel stencil layer is framed as distinct from the PCB itself

2. `aperture_to_pad_relationship`
   - article states stencil openings correspond to SMD pads
   - article also states dense-pad situations may use slightly smaller openings

3. `mark_point_correspondence`
   - article distinguishes two mark-point styles on the stencil
   - article ties stencil mark usability to whether PCB-side mark points exist

4. `notched_pad_or_opening_example`
   - article says certain chip-style pad designs should include a notch / opening feature to avoid assembly issues
   - article ties the absence of that feature to defect anecdotes

5. `stencil_manufacturing_method_menu`
   - article names etch, laser, and electroform as stencil-making methods
   - article attaches precision, range, cost, and surface-finish claims to those methods

6. `paste_stencil_vs_red_glue_vs_dual_process`
   - article distinguishes solder-paste stencil use for reflow from red-glue stencil use for wave-solder-oriented mixed assemblies
   - article describes a two-stencil dual-process setup when paste and red glue both appear

7. `tool_and_delivery_marketing`
   - article promotes a branded checker workflow
   - article includes fast-delivery, low-price, and ordering convenience claims

## Existing Repo-Backed Support Found

This PDF does have overlap with existing repo-backed surfaces, but only at conservative process-identity level.

### 1. Stencil and upstream print-control identity

Safe route:
- `facts/methods/pcba-stencil-selective-solder-and-fine-pitch-controls.md`

Admitted reuse:
- stencil belongs to the upstream solder-paste printing stage
- stencil / paste handling is part of one broader process-control chain
- dense-package and print-control discussion belongs upstream of later soldering and inspection steps

Boundary:
- this PDF can reinforce that stencil and paste-transfer language belongs in upstream process framing
- it does not add source-backed aperture geometry, paste-transfer ratios, stencil thickness defaults, or defect-rate claims

### 2. Mixed-technology sequencing posture

Safe route:
- `facts/methods/selective-wave-solder-and-mixed-technology-sequencing.md`
- `wiki/processes/mixed-technology-solder-route-selection.md`

Admitted reuse:
- solder-paste stencil use belongs to the SMT reflow side of the flow
- red-glue and later through-hole / wave-style discussion belongs to mixed-technology route selection language
- paste, SMT placement, and later through-hole solder-route choice can be explained as one coordinated assembly sequence rather than isolated techniques

Boundary:
- this PDF can only map into the already-landed mixed-technology route posture
- it does not prove when red glue should be chosen, when wave is mandatory, or that one route is universally better

### 3. Quality-gate adjacency only

Safe route:
- `wiki/testing/pcba-quality-gates-and-test-strategy.md`

Admitted reuse:
- stencil print quality belongs earlier than inspection and downstream release gates
- print-stage control and later quality gates should not be collapsed into one generic `quality` claim

Boundary:
- this page is only adjacent support here
- the stencil PDF does not itself add new source-backed test strategy, inspection coverage, or release-gate authority

## Safe Reuse Classes

1. `stencil_purpose_and_paste_transfer_identity`
   - reusable as a neutral statement that the stencil is the upstream transfer tool for solder paste deposition onto target pad locations

2. `paste_layer_is_separate_from_finished_pcb`
   - reusable as a neutral CAD / manufacturing-file identity concept

3. `mixed_technology_route_split_between_paste_reflow_and_later_tht_soldering`
   - reusable only at high level through existing mixed-technology route pages

4. `local_pdf_scoped_example_families`
   - aperture / notch example
   - mark-point dependency example
   - paste-versus-red-glue opening-location example

## Explicit Route Decision

This article only partially advances above pure cluster inventory.

The important narrow result is:

- it maps into existing source-backed posture pages for `stencil as upstream paste-print control`
- it maps into existing source-backed posture pages for `mixed-technology sequencing between solder-paste reflow and later through-hole solder-route choice`

It does **not** justify a new fact card or wiki page from this lane.

It also does **not** justify promoting article-origin mark-point rules, notch rules, aperture rules, stencil-fabrication precision numbers, or red-glue process defaults into reusable facts.

If stated plainly: this article mostly maps into existing source-backed posture pages rather than adding new source-backed knowledge.

## Blocked Claims

The following claim families remain blocked and must not be promoted from this PDF:

1. `all_aperture_geometry_rules`
   - slightly-smaller-than-pad guidance
   - any unstated aperture reduction norm
   - any implied area-ratio or release-ratio rule

2. `all_notch_rule_defaults`
   - universal claims that chip pads must include a specific notch style
   - certainty that one notch treatment prevents listed defects across all parts

3. `mark_point_type_and_shape_rules`
   - half-etch versus through-hole mark-point defaults
   - standard mark-point size, location, or equipment-fit conclusions

4. `stencil_fabrication_precision_thickness_and_capability_claims`
   - etch / laser / electroform precision numbers
   - thickness freedom claims
   - wear, strength, or release-performance superiority claims

5. `process_selection_superiority_claims`
   - red glue is better for a given board class
   - one process ordering is universally preferred
   - one stencil route guarantees fewer defects

6. `defect_prevention_certainty_claims`
   - guaranteed avoidance of tombstoning, solder beads, floating, sliding, or similar outcomes

7. `tool_marketing_claims`
   - branded checker sufficiency
   - branded workflow superiority
   - branded ordering convenience as engineering authority

8. `commercial_and_delivery_claims`
   - fastest delivery
   - cheaper price
   - schedule protection
   - production-loss certainty

## Reused Repo-Backed Source / Fact / Wiki Surfaces

### Fact surfaces

- `methods-pcba-stencil-selective-solder-and-fine-pitch-controls`
  - primary safe reuse surface for stencil and paste-print process identity

- `methods-selective-wave-solder-and-mixed-technology-sequencing`
  - primary safe reuse surface for turning paste / red-glue / later solder-route language into conservative mixed-technology sequencing wording

### Wiki surfaces

- `processes-mixed-technology-solder-route-selection`
  - receives the article only as route-selection support, not as parameter authority

- `testing-pcba-quality-gates-and-test-strategy`
  - adjacent support only for keeping print-stage control separate from later inspection and release-gate language

### Existing controller log surfaces

- `p4-313`
  - this PDF remains inside the earlier `stencil_and_paste_transfer_identity` safe reuse class
  - this PDF also remains inside the earlier `official_source_recovery_target` posture for stencil / solder-paste guidance

- `p4-309`
  - corpus status remains `usage_route_covered_at_controller_level_only`
  - this single-PDF lane does not change the broader `E5` corpus truth

## Residual Gaps

1. official-source support for stencil aperture-design boundaries
   - needed before any aperture reduction, notch-treatment, or print-defect mitigation rule can be promoted

2. official or owner-scoped support for mark-point geometry and equipment-compatibility framing
   - needed before any mark-point type or size guidance can be reused

3. stronger source-backed treatment for red-glue process positioning
   - current reuse is only mixed-technology sequencing posture, not full process guidance

4. official-source support for stencil fabrication method comparison
   - needed before method-precision, release-performance, or durability differences can be stated

5. no clean authority in this lane for article-side cost, lead-time, or delivery outcomes
   - these remain blocked

## Lane Status

Status: `completed_at_single_pdf_route_level_only`

What is complete:
- the single stencil article PDF has been routed into existing repo-backed stencil and mixed-technology posture surfaces
- safe reuse classes and blocked claim classes are explicit
- the lane now states clearly that the PDF mostly maps into existing source-backed posture pages

What is not complete:
- no official-source recovery was performed
- no new `facts/`, `wiki/`, `sources/registry/`, or tracker updates were created
- no article images or diagrams were preserved as local evidence
- no article-origin numeric or capability rule was unlocked

## Final Lane Report

Changed files:
- `/code/blogs/llm_wiki/logs/p4-335-2026-5-9-e5-stencil-and-paste-route-integration.md`

Lane status:
- `completed_at_single_pdf_route_level_only`

Safe reuse classes:
- stencil purpose and paste-transfer identity
- paste-layer / stencil-layer identity as separate from the finished PCB
- mixed-technology sequencing split between solder-paste reflow and later through-hole solder-route choice
- local PDF-scoped example families only

Blocked claims:
- aperture rules
- notch defaults
- mark-point geometry and type rules
- stencil fabrication precision / thickness / superiority claims
- process-window and defect-prevention certainty claims
- tool-marketing claims
- cost, lead-time, and delivery claims

Reused repo-backed source / fact / wiki surfaces:
- `methods-pcba-stencil-selective-solder-and-fine-pitch-controls`
- `methods-selective-wave-solder-and-mixed-technology-sequencing`
- `processes-mixed-technology-solder-route-selection`
- `testing-pcba-quality-gates-and-test-strategy`
- `p4-313`
- `p4-309`

Residual gaps:
- official stencil aperture-design authority
- official mark-point guidance
- stronger source-backed red-glue positioning
- official stencil-fabrication method comparison authority
- no authority for article commercial outcomes
