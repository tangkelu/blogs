# P4-385 E2 Copper-Balance And Routing-Expression Route Integration

Date: 2026-05-09
Execution mode: `single_pdf_route_integration_only`
Model: `gpt-5`
Lane owner: `P4-385 E2 single-PDF route integration for PCB可制造性设计及案例分析之线路篇.pdf`

## Purpose And Assigned Lane

Produce a deletion-safe lane log for one `E2` article PDF while staying at conservative route-integration level only.

This lane treats the PDF and extracted pages as `claim_inventory_only`, not authority.
It does not create or update reusable `facts/`, `wiki/`, or `sources/registry/`.

## Input Files Inspected

- `/code/blogs/tmps/PCB资料/PCB文章/PCB可制造性设计及案例分析之线路篇.pdf`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB可制造性设计及案例分析之线路篇/pages/page-0001.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB可制造性设计及案例分析之线路篇/pages/page-0002.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB可制造性设计及案例分析之线路篇/pages/page-0003.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB可制造性设计及案例分析之线路篇/pages/page-0004.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB可制造性设计及案例分析之线路篇/pages/page-0005.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB可制造性设计及案例分析之线路篇/pages/page-0006.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB可制造性设计及案例分析之线路篇/pages/page-0007.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB可制造性设计及案例分析之线路篇/pages/page-0008.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB可制造性设计及案例分析之线路篇/pages/page-0009.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB可制造性设计及案例分析之线路篇/pages/page-0010.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB可制造性设计及案例分析之线路篇/pages/page-0011.txt`

## Existing LLM Wiki Support Found

Related route / controller logs inspected:

- `/code/blogs/llm_wiki/logs/p4-310-2026-5-8-pcb-article-e2-usage-route-integration.md`
- `/code/blogs/llm_wiki/logs/p4-283b-2026-5-7-pcb-article-e2-layout-routing-stackup-layers-and-impedance-claim-family-map.md`
- `/code/blogs/llm_wiki/logs/p4-382-2026-5-9-e2-layout-routing-manufacturability-route-integration.md`
- `/code/blogs/llm_wiki/logs/p4-384-2026-5-9-e2-safety-distance-taxonomy-and-spacing-boundary-route-integration.md`

Repo-backed support surfaces inspected:

- `/code/blogs/llm_wiki/facts/methods/depanelization-cleanliness-and-edge-risk-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/ipc-solder-mask-layer-and-pad-definition-boundary.md`

## PDF Claim Inventory

Observed article-side claim families from the extracted pages:

1. `layout_before_routing_and_partitioning_claim`
   - the article again frames placement and routing as interactive and says analog/digital separation and topology awareness matter before routing closes

2. `fill_line_vs_solid_copper_expression_claim`
   - the article distinguishes fill-line style copper expression from solid copper-region expression and warns that they are not equivalent in downstream handling

3. `dense_sparse_routing_and_copper_balance_claim`
   - the article treats routing density imbalance and copper-balance imbalance as manufacturability risk families

4. `thin_residual_copper_and_island_claim`
   - the article warns about very thin residual copper or small attached copper strips as detachment/short-risk families

5. `special_pad_effective_area_claim`
   - the article uses unusual pad shapes to argue that nominal outline and effective solderable area may differ

6. `board_edge_trace_copper_and_milling_path_claim`
   - the article treats board-edge copper or nets near routing/milling paths as release-review and edge-conflict topics

7. `mixed_panel_residual_copper_ratio_claim`
   - the article discusses very different residual-copper ratios across boards in one panel as a production-balance concern

8. `tight_lead_spacing_bridge_numeric_claim`
   - the article includes exact bridge, annular, hole, and lead-spacing numerics

9. `mask_defined_bga_preference_claim`
   - the article claims a pad-definition preference for BGA based on appearance and mask-offset handling

10. `outer_layer_bare_copper_band_claim`
   - the article treats decorative or edge-exposed copper bands as objects that can be confused with routing/program intent unless expressed clearly

11. `tool_and_vendor_capability_claim`
   - the article includes software pain points, program defaults, capability advice, and promo language

## Per-Claim-Family Disposition

### 1. `layout_before_routing_and_partitioning_claim`

Disposition:
- `safe_route_reuse`

Admitted reuse:
- placement and routing may be written as interactive rather than fully separable stages
- analog/digital separation and topology-aware placement may be written as qualitative layout-governance posture only

Primary support:
- `/code/blogs/llm_wiki/logs/p4-382-2026-5-9-e2-layout-routing-manufacturability-route-integration.md`

Boundary:
- no performance guarantee or universal placement doctrine

### 2. `fill_line_vs_solid_copper_expression_claim`

Disposition:
- `safe_route_reuse_with_scope_guard`

Admitted reuse:
- fill-line expression and solid copper-region expression may be written as different release-data objects
- copper expression should be explicit enough that downstream manufacturing-data interpretation is not ambiguous

Primary support:
- `/code/blogs/llm_wiki/logs/p4-310-2026-5-8-pcb-article-e2-usage-route-integration.md`

Boundary:
- no tool-specific workflow, no exact line-width setting, and no software-behavior certainty claim

### 3. `dense_sparse_routing_and_copper_balance_claim`

Disposition:
- `safe_route_reuse_with_scope_guard`

Admitted reuse:
- routing density imbalance and copper-balance imbalance may be written as manufacturability risk families

Primary support:
- `/code/blogs/llm_wiki/logs/p4-283b-2026-5-7-pcb-article-e2-layout-routing-stackup-layers-and-impedance-claim-family-map.md`

Boundary:
- no exact etch-compensation, width-adjustment, plating-balance, or process-yield rule

### 4. `thin_residual_copper_and_island_claim`

Disposition:
- `narrow_route_reuse_only`

Admitted reuse:
- thin residual copper, isolated copper, and weakly attached copper features may be written as fabrication-risk families

Primary support:
- `/code/blogs/llm_wiki/logs/p4-382-2026-5-9-e2-layout-routing-manufacturability-route-integration.md`

Boundary:
- no exact minimum width and no universal short-circuit certainty claim

### 5. `special_pad_effective_area_claim`

Disposition:
- `limited_route_support_only`

Admitted reuse:
- nominal pad outline and effective solderable area may diverge for unusual pad shapes, so pad geometry should be reviewed for effective usable area rather than only outline appearance

Primary support:
- `/code/blogs/llm_wiki/facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`

Boundary:
- no exact pad-shape recommendation and no direct geometry promotion

### 6. `board_edge_trace_copper_and_milling_path_claim`

Disposition:
- `safe_route_reuse`

Admitted reuse:
- board-edge nets, copper, and milling paths may be written as edge-conflict and release-review topics
- edge-near conductive features should be checked against profiling intent before release

Primary support:
- `/code/blogs/llm_wiki/facts/methods/depanelization-cleanliness-and-edge-risk-boundary.md`
- `/code/blogs/llm_wiki/logs/p4-384-2026-5-9-e2-safety-distance-taxonomy-and-spacing-boundary-route-integration.md`

Boundary:
- no exact milling offset numeric and no universal redesign prescription

### 7. `mixed_panel_residual_copper_ratio_claim`

Disposition:
- `limited_route_support_only`

Admitted reuse:
- strongly different copper-balance states across boards in one panel may be written as a panel-balance review trigger family

Boundary:
- no plating-current rule, no lamination/fill certainty, and no supplier-process conclusion

### 8. `tight_lead_spacing_bridge_numeric_claim`

Disposition:
- `blocked`

Reason:
- exact bridge, hole, annular, tolerance, and lead-spacing numerics remain blocked

### 9. `mask_defined_bga_preference_claim`

Disposition:
- `blocked`

Reason:
- pad-definition preference and BGA pad-style advice need stronger owner or standards authority than this article

### 10. `outer_layer_bare_copper_band_claim`

Disposition:
- `safe_route_reuse_with_scope_guard`

Admitted reuse:
- decorative or exposed outer-layer copper bands may be written as release-expression objects that must be made unambiguous relative to profiling/program intent

Primary support:
- `/code/blogs/llm_wiki/facts/methods/depanelization-cleanliness-and-edge-risk-boundary.md`

Boundary:
- no exact stackup/opening/thermal-via recipe and no appearance-quality guarantee

### 11. `tool_and_vendor_capability_claim`

Disposition:
- `blocked`

Reason:
- tool pain-point claims, capability claims, and promo language are not reusable authority

## Safe Reuse Classes

1. `placement_and_routing_as_interactive_governance_stages`
2. `fill_line_vs_solid_copper_as_distinct_release_expression_objects`
3. `dense_sparse_routing_and_copper_balance_as_manufacturability_risk_families`
4. `thin_residual_copper_and_island_as_fabrication_risk_families_only`
5. `special_pad_effective_area_as_review_surface_only`
6. `board_edge_copper_and_milling_path_conflict_review`
7. `panel_level_copper_balance_difference_as_review_trigger_only`
8. `outer_layer_bare_copper_band_as_release_expression_boundary`

## Blocked Claim Classes

1. `all_exact_fill_line_width_balance_width_and_residual_copper_numerics`
2. `all_exact_bridge_hole_annular_tolerance_and_lead_spacing_rules`
3. `all_bga_mask_defined_preference_or_pad_definition_closure_claims`
4. `all_exact_milling_offset_opening_and_thermal_via_recipes`
5. `all_tool_behavior_program_default_and_vendor_capability_claims`
6. `all_quality_cost_yield_and_cycle_outcome_claims`

## Explicit Route Decision

This PDF is usable only for conservative copper-balance and routing-expression routing:

- placement and routing as interactive governance stages
- fill-line versus solid-copper expression as distinct release-data objects
- dense/sparse routing and copper-balance as manufacturability risk families
- thin residual copper and isolated copper as fabrication-risk families only
- special pad effective area as a review surface only
- board-edge copper and milling-path conflict review
- panel-level copper-balance difference as a review trigger only
- outer-layer bare-copper band as a release-expression boundary

It does not justify any exact line width, spacing, bridge, hole, annular, tolerance, BGA pad-style preference, milling/opening recipe, tool behavior claim, or vendor capability/cost/yield outcome.

## Completion Status

- `completed_at_single_pdf_route_level_only`
- `source_backed_route_available_without_new_fact_promotion`
- `not_completed_for_fact_promotion_or_official_source_recovery`
