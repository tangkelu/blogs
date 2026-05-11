# P4-367 E3 Via Solder-Mask Treatment Route Integration

Date: 2026-05-09
Execution mode: `single_pdf_route_integration_only`
Model: `gpt-5`
Lane owner: `P4-367 E3 single-PDF route integration for 一招搞定PCB阻焊过孔问题.pdf`

## Purpose And Assigned Lane

Produce a deletion-safe lane log for one `E3` article PDF while staying at conservative route-integration level only.

This lane treats the PDF and extracted pages as `claim_inventory_only`, not authority.
It does not create or update reusable `facts/`, `wiki/`, or `sources/registry/`.

## Input Files Inspected

- `/code/blogs/tmps/PCB资料/PCB文章/一招搞定PCB阻焊过孔问题.pdf`
- `/code/blogs/tmps/pcb_pdf_extracted_full/一招搞定PCB阻焊过孔问题/pages/page-0001.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/一招搞定PCB阻焊过孔问题/pages/page-0002.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/一招搞定PCB阻焊过孔问题/pages/page-0003.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/一招搞定PCB阻焊过孔问题/pages/page-0004.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/一招搞定PCB阻焊过孔问题/pages/page-0005.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/一招搞定PCB阻焊过孔问题/pages/page-0006.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/一招搞定PCB阻焊过孔问题/pages/page-0007.txt`

## Existing LLM Wiki Support Found

Related route / controller logs inspected:

- `/code/blogs/llm_wiki/logs/p4-311-2026-5-8-pcb-article-e3-usage-route-integration.md`
- `/code/blogs/llm_wiki/logs/p4-344-2026-5-9-e5-via-in-pad-manufacturability-route-integration.md`

Repo-backed support surfaces inspected:

- `/code/blogs/llm_wiki/facts/methods/ipc-solder-mask-layer-and-pad-definition-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/cam-data-exchange-format-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/hdi-microvia-and-vippo-process-posture.md`

## PDF Claim Inventory

Observed article-side claim families from the extracted pages:

1. `via_solder_mask_treatment_option_taxonomy_claim`
   - the article groups via treatment into cover-mask, open-mask, ink-plug, resin-fill, and copper-fill branches

2. `treatment_choice_depends_on_application_context_claim`
   - the article repeatedly frames the branches as different treatments with different application scenarios rather than one universal default

3. `gerber_opening_expression_controls_cover_vs_open_claim`
   - the article says Gerber opening expression controls whether a via becomes masked or open in the released output package

4. `via_in_pad_process_branch_claim`
   - the article ties resin-filled or copper-filled branches to via-in-pad and pad-surface continuity scenarios

5. `numeric_hole_size_and_current_capacity_claim`
   - the article gives hole-size and current-carrying numeric conditions for some branch choices

6. `software_specific_ui_and_export_recipe_claim`
   - the article gives Altium, PADS, and Allegro UI and export-step instructions

7. `checker_sufficiency_and_ordering_workflow_claim`
   - the article extends into branded DFM-checker behavior and ordering-workflow claims

## Per-Claim-Family Disposition

### 1. `via_solder_mask_treatment_option_taxonomy_claim`

Disposition:
- `safe_route_reuse_with_scope_guard`

Admitted reuse:
- via solder-mask treatment can be written as a branch taxonomy rather than one universal default
- different treatments may be reviewed as distinct manufacturing-data expressions

Primary support:
- `/code/blogs/llm_wiki/logs/p4-311-2026-5-8-pcb-article-e3-usage-route-integration.md`
- `/code/blogs/llm_wiki/facts/methods/ipc-solder-mask-layer-and-pad-definition-boundary.md`

Boundary:
- no claim that the article's five-way split is an official IPC terminology closure

### 2. `treatment_choice_depends_on_application_context_claim`

Disposition:
- `safe_route_reuse`

Admitted reuse:
- via mask treatment is scenario-dependent rather than universal
- treatment choice belongs to fabrication and release review, not casual defaulting

Primary support:
- `/code/blogs/llm_wiki/logs/p4-311-2026-5-8-pcb-article-e3-usage-route-integration.md`

### 3. `gerber_opening_expression_controls_cover_vs_open_claim`

Disposition:
- `safe_route_reuse`

Admitted reuse:
- released solder-mask expression controls whether intended openings appear in the fabrication package
- cover versus open treatment belongs to released-output review, not only canvas intent

Primary support:
- `/code/blogs/llm_wiki/facts/methods/cam-data-exchange-format-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/ipc-solder-mask-layer-and-pad-definition-boundary.md`

Boundary:
- no universal file recipe or CAD-layer doctrine

### 4. `via_in_pad_process_branch_claim`

Disposition:
- `limited_route_support_only`

Admitted reuse:
- via-in-pad may be named as one treatment-related branch where pad-surface continuity and dense-interconnect review matter
- this branch should stay tied to existing HDI and via-in-pad posture rather than article process certainty

Primary support:
- `/code/blogs/llm_wiki/facts/methods/hdi-microvia-and-vippo-process-posture.md`
- `/code/blogs/llm_wiki/logs/p4-344-2026-5-9-e5-via-in-pad-manufacturability-route-integration.md`

Boundary:
- no universal resin-fill, copper-fill, planarization, or plating default

### 5. `numeric_hole_size_and_current_capacity_claim`

Disposition:
- `blocked`

Reason:
- hole-size, current-carrying, and process-threshold numerics remain article-side and are not reusable authority

### 6. `software_specific_ui_and_export_recipe_claim`

Disposition:
- `blocked`

Reason:
- Altium, PADS, Allegro, and Gerber-step instructions are tool-shell operations rather than reusable authority

### 7. `checker_sufficiency_and_ordering_workflow_claim`

Disposition:
- `blocked`

Reason:
- branded DFM-checker behavior, parameter-page workflow, and down-order flow are unsupported for general reuse

## Safe Reuse Classes

1. `via_solder_mask_treatment_as_branch_taxonomy`
2. `via_treatment_choice_as_context_dependent_review_topic`
3. `released_solder_mask_expression_controls_cover_vs_open_output`
4. `via_in_pad_as_treatment_related_dense_interconnect_branch_only`

## Blocked Claim Classes

1. `all_hole_size_current_capacity_and_process_threshold_numerics`
2. `all_universal_cover_oil_open_window_plug_fill_default_rules`
3. `all_resin_fill_copper_fill_planarization_and_plating_defaults_as_general_truth`
4. `all_tool_specific_ui_menu_export_and_object_setting_claims`
5. `all_checker_sufficiency_and_ordering_workflow_claims`
6. `all_defect_certainty_reliability_yield_or_cost_outcome_claims`
7. `all_acceptance_criteria_and_supplier_process_proof_claims`

## Explicit Route Decision

This PDF is usable only for conservative via solder-mask treatment routing:

- via solder-mask treatment as a branch taxonomy
- treatment choice as context-dependent review
- released solder-mask expression as the deciding output surface for cover versus open handling
- via-in-pad as one treatment-related dense-interconnect branch only

It does not justify treatment numerics, universal process defaults, software-operation guidance, checker sufficiency claims, or any new fact-layer promotion.

## Completion Status

- `completed_at_single_pdf_route_level_only`
- `source_backed_route_available_without_new_fact_promotion`
- `not_completed_for_fact_promotion_or_official_definition_closure`
