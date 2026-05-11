# P4-353 E4 Mark Fiducial Role Route Integration

Date: 2026-05-09
Execution mode: `single_pdf_route_integration_only`
Model: `gpt-5`
Lane owner: `P4-353 E4 single-PDF route integration for PCB板的Mark点设计对SMT重要性.pdf`

## Purpose And Assigned Lane

Produce a deletion-safe lane log for one `E4` article PDF while staying at conservative route-integration level only.

This lane treats the PDF and extracted pages as `claim_inventory_only`, not authority.
It does not create or update reusable `facts/`, `wiki/`, or `sources/registry/`.

## Input Files Inspected

- `/code/blogs/tmps/PCB资料/PCB文章/PCB板的Mark点设计对SMT重要性.pdf`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB板的Mark点设计对SMT重要性/pages/page-0001.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB板的Mark点设计对SMT重要性/pages/page-0002.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB板的Mark点设计对SMT重要性/pages/page-0003.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB板的Mark点设计对SMT重要性/pages/page-0004.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB板的Mark点设计对SMT重要性/pages/page-0005.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB板的Mark点设计对SMT重要性/pages/page-0006.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB板的Mark点设计对SMT重要性/pages/page-0007.txt`

## Existing LLM Wiki Support Found

Related route / controller logs inspected:

- `/code/blogs/llm_wiki/logs/p4-283e-2026-5-7-pcb-article-e4-panelization-outline-edge-clearance-and-marking-claim-family-map.md`
- `/code/blogs/llm_wiki/logs/p4-312-2026-5-8-pcb-article-e4-usage-route-integration.md`
- `/code/blogs/llm_wiki/logs/p4-287-2026-5-7-pcb-pdf-lane-d3-e4-controller-integration.md`

Boundary-adjacent surfaces inspected:

- `/code/blogs/llm_wiki/facts/local_pdf/pin1-origin-installation-mark-visual-boundary.md`
- `/code/blogs/llm_wiki/logs/p4-332-2026-5-9-e5-polarity-reference-designator-route-integration.md`

## PDF Claim Inventory

Observed article-side claim families from the extracted pages:

1. `mark_as_optical_alignment_reference_claim`
   - the article frames `Mark` as optical or fiducial reference used by placement equipment for positional recognition

2. `mark_scope_split_claim`
   - the article splits `Mark` use across board-level, panel-level, and local-component scope

3. `mark_asymmetry_and_orientation_disambiguation_claim`
   - the article says asymmetric placement helps avoid orientation ambiguity

4. `local_component_precision_attention_claim`
   - the article links local `Mark` use to certain packages such as `QFP` and `BGA`

5. `mark_visibility_and_cleanliness_claim`
   - the article says surrounding clutter, nearby objects, or blocked space can reduce `Mark` recognition quality

6. `mark_geometry_and_keepout_numeric_claim`
   - the article provides `Mark` size, opening, edge-distance, and open-area numerics

7. `mark_count_and_arrangement_rule_claim`
   - the article provides count and corner-placement rules for board and panel contexts

8. `no_mark_workaround_and_fixture_claim`
   - the article describes pad substitution, taped stencil workaround, or fixture-added `Mark` as alternatives when `Mark` is absent

9. `machine_precision_and_business_outcome_claim`
   - the article links `Mark` design to placement precision, efficiency, schedule, and cost outcomes

10. `branded_checker_sufficiency_claim`
   - the article frames branded `DFM` checking as the route to detect missing or abnormal `Mark` design

## Per-Claim-Family Disposition

### 1. `mark_as_optical_alignment_reference_claim`

Disposition:
- `safe_route_reuse`

Admitted reuse:
- `Mark` may be written as optical alignment or fiducial reference vocabulary for SMT placement context

Primary support:
- `/code/blogs/llm_wiki/logs/p4-283e-2026-5-7-pcb-article-e4-panelization-outline-edge-clearance-and-marking-claim-family-map.md`
- `/code/blogs/llm_wiki/logs/p4-312-2026-5-8-pcb-article-e4-usage-route-integration.md`

### 2. `mark_scope_split_claim`

Disposition:
- `safe_route_reuse`

Admitted reuse:
- `Mark` discussion may be split into board-level, panel-level, and local-component scope

Primary support:
- `/code/blogs/llm_wiki/logs/p4-283e-2026-5-7-pcb-article-e4-panelization-outline-edge-clearance-and-marking-claim-family-map.md`
- `/code/blogs/llm_wiki/logs/p4-312-2026-5-8-pcb-article-e4-usage-route-integration.md`

Boundary:
- no universal count or layout-default rule may be promoted from the article

### 3. `mark_asymmetry_and_orientation_disambiguation_claim`

Disposition:
- `safe_route_reuse_with_scope_guard`

Admitted reuse:
- asymmetry may be kept as orientation-disambiguation and anti-confusion wording for `Mark` usefulness

Boundary:
- no exact placement pattern, no count rule, and no implied universal machine requirement

### 4. `local_component_precision_attention_claim`

Disposition:
- `narrow_route_reuse_only`

Admitted reuse:
- some package neighborhoods may justify local fiducial attention as a higher-precision review branch

Boundary:
- no package-specific default requirement and no universal `QFP` / `BGA` local-mark rule

### 5. `mark_visibility_and_cleanliness_claim`

Disposition:
- `safe_route_reuse`

Admitted reuse:
- `Mark` usefulness depends on visibility, uncluttered surroundings, and avoiding obvious obstruction

Primary support:
- `/code/blogs/llm_wiki/logs/p4-283e-2026-5-7-pcb-article-e4-panelization-outline-edge-clearance-and-marking-claim-family-map.md`
- `/code/blogs/llm_wiki/logs/p4-312-2026-5-8-pcb-article-e4-usage-route-integration.md`

Boundary:
- no exact keepout distance or open-area numeric rule

### 6. `mark_geometry_and_keepout_numeric_claim`

Disposition:
- `blocked`

Reason:
- all `Mark` diameters, opening values, edge distances, and nearby-clearance numerics remain blocked in this lane

### 7. `mark_count_and_arrangement_rule_claim`

Disposition:
- `blocked`

Reason:
- article-side count rules, corner rules, and arrangement defaults are not reusable authority

### 8. `no_mark_workaround_and_fixture_claim`

Disposition:
- `blocked`

Reason:
- workaround sequences, fixture substitution claims, and taped-stencil handling are process- and tool-specific fallback stories, not reusable neutral authority

### 9. `machine_precision_and_business_outcome_claim`

Disposition:
- `blocked`

Reason:
- precision, efficiency, schedule, and cost outcome claims remain article-side and unsupported as reusable authority

### 10. `branded_checker_sufficiency_claim`

Disposition:
- `blocked`

Reason:
- branded checker completeness and sufficiency claims remain marketing-side and unsupported

## Safe Reuse Classes

1. `mark_as_optical_alignment_reference`
2. `mark_scope_split_across_board_panel_and_local_component`
3. `mark_asymmetry_as_orientation_disambiguation_context`
4. `local_component_fiducial_attention_as_higher_precision_review_branch_only`
5. `mark_visibility_and_cleanliness_as_recognition_conditions`

## Blocked Claim Classes

1. `all_mark_geometry_and_keepout_numbers`
2. `all_mark_count_rules_and_corner_arrangement_defaults`
3. `all_package_specific_local_mark_defaults`
4. `all_machine_precision_or_efficiency_guarantee_claims`
5. `all_no_mark_workaround_or_fixture_substitution_claims_as_general_guidance`
6. `all_quality_cost_schedule_and_yield_outcome_claims`
7. `all_branded_checker_completeness_or_sufficiency_claims`
8. `all_universal_acceptability_judgments`

## Explicit Route Decision

This PDF is usable only for conservative fiducial-role routing:

- `Mark` as optical alignment reference
- board / panel / local-component scope split
- asymmetry as orientation-disambiguation context
- visibility and cleanliness as recognition conditions

It does not justify `Mark` geometry numerics, count defaults, package-specific mandatory local marks, no-mark workaround guidance, or branded-checker sufficiency claims.

## Completion Status

- `completed_at_single_pdf_route_level_only`
- `source_backed_route_available_without_new_fact_promotion`
- `not_completed_for_fact_promotion_or_official_source_recovery`
