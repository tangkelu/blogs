# P4-384 E2 Safety-Distance Taxonomy And Spacing-Boundary Route Integration

Date: 2026-05-09
Execution mode: `single_pdf_route_integration_only`
Model: `gpt-5`
Lane owner: `P4-384 E2 single-PDF route integration for PCB设计必须考虑的8种安全距离，搞错1种都出大问题！.pdf`

## Purpose And Assigned Lane

Produce a deletion-safe lane log for one `E2` article PDF while staying at conservative route-integration level only.

This lane treats the PDF and extracted pages as `claim_inventory_only`, not authority.
It does not create or update reusable `facts/`, `wiki/`, or `sources/registry/`.

## Input Files Inspected

- `/code/blogs/tmps/PCB资料/PCB文章/PCB设计必须考虑的8种安全距离，搞错1种都出大问题！.pdf`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB设计必须考虑的8种安全距离-搞错1种都出大问题/pages/page-0001.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB设计必须考虑的8种安全距离-搞错1种都出大问题/pages/page-0002.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB设计必须考虑的8种安全距离-搞错1种都出大问题/pages/page-0003.txt`

## Existing LLM Wiki Support Found

Related route / controller logs inspected:

- `/code/blogs/llm_wiki/logs/p4-310-2026-5-8-pcb-article-e2-usage-route-integration.md`
- `/code/blogs/llm_wiki/logs/p4-283b-2026-5-7-pcb-article-e2-layout-routing-stackup-layers-and-impedance-claim-family-map.md`
- `/code/blogs/llm_wiki/logs/p4-382-2026-5-9-e2-layout-routing-manufacturability-route-integration.md`

Repo-backed support surfaces inspected:

- `/code/blogs/llm_wiki/facts/methods/ipc-solder-mask-layer-and-pad-definition-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/depanelization-cleanliness-and-edge-risk-boundary.md`

## PDF Claim Inventory

Observed article-side claim families from the extracted pages:

1. `electrical_vs_nonelectrical_spacing_taxonomy_claim`
   - the article explicitly splits safety distance into electrical-related and non-electrical-related families

2. `trace_pad_and_pad_pad_spacing_claim`
   - the article treats trace-to-trace, trace-to-pad, and pad-to-pad spacing as electrical spacing families

3. `pad_hole_and_via_spacing_claim`
   - the article includes pad-hole width and via-to-via spacing as layout-rule families

4. `copper_to_board_edge_spacing_claim`
   - the article frames copper-to-edge setback as a board-edge safety and manufacturing topic

5. `silkscreen_to_pad_spacing_claim`
   - the article treats silkscreen overlap with solderable pads as a manufacturing-data conflict topic

6. `mechanical_3d_clearance_claim`
   - the article frames horizontal spacing and 3D height clearance as mechanical-fit and interference checks

7. `exact_spacing_numeric_claim`
   - the article includes explicit `mm` and `mil` threshold examples for multiple spacing families

8. `design_rule_menu_and_vendor_capability_claim`
   - the article references CAD menu-path handling and ends with vendor capability / standard / promo wording

## Per-Claim-Family Disposition

### 1. `electrical_vs_nonelectrical_spacing_taxonomy_claim`

Disposition:
- `safe_route_reuse`

Admitted reuse:
- spacing checks may be written as at least two separate families: electrical-related and non-electrical-related
- the taxonomy itself is safe at category level only

Primary support:
- `/code/blogs/llm_wiki/logs/p4-310-2026-5-8-pcb-article-e2-usage-route-integration.md`

Boundary:
- no conversion of this taxonomy into exact thresholds

### 2. `trace_pad_and_pad_pad_spacing_claim`

Disposition:
- `safe_route_reuse_with_scope_guard`

Admitted reuse:
- traces, pads, and adjacent conductor features may be written as distinct spacing review surfaces
- spacing may be framed as a manufacturability, reliability, and assembly-risk topic family

Primary support:
- `/code/blogs/llm_wiki/logs/p4-283b-2026-5-7-pcb-article-e2-layout-routing-stackup-layers-and-impedance-claim-family-map.md`
- `/code/blogs/llm_wiki/logs/p4-382-2026-5-9-e2-layout-routing-manufacturability-route-integration.md`

Boundary:
- no minimum spacing number, no voltage-conditioned rule, and no universal acceptance threshold

### 3. `pad_hole_and_via_spacing_claim`

Disposition:
- `limited_route_support_only`

Admitted reuse:
- pad-hole and via adjacency may be written as geometry-sensitive review objects that need stricter authority before numeric use

Primary support:
- `/code/blogs/llm_wiki/facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`

Boundary:
- no exact hole diameter, no exact via spacing, and no manufacturing-capability implication

### 4. `copper_to_board_edge_spacing_claim`

Disposition:
- `safe_route_reuse_with_scope_guard`

Admitted reuse:
- copper-to-edge spacing may be written as an edge-risk and release-review surface
- board-edge setback belongs in profiling and edge-handling review, not only electrical design intent

Primary support:
- `/code/blogs/llm_wiki/facts/methods/depanelization-cleanliness-and-edge-risk-boundary.md`

Boundary:
- no exact copper setback numeric, no keepout recipe, and no short-circuit inevitability claim

### 5. `silkscreen_to_pad_spacing_claim`

Disposition:
- `safe_route_reuse_with_scope_guard`

Admitted reuse:
- silkscreen and solderable pad overlap may be written as a released-manufacturing-data conflict topic

Primary support:
- `/code/blogs/llm_wiki/facts/methods/ipc-solder-mask-layer-and-pad-definition-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`

Boundary:
- no exact silkscreen offset number and no factory-default auto-cleanup sufficiency claim

### 6. `mechanical_3d_clearance_claim`

Disposition:
- `safe_route_reuse`

Admitted reuse:
- horizontal spacing and 3D height clearance may be written as mechanical-interference and enclosure-fit review surfaces

Primary support:
- `/code/blogs/llm_wiki/logs/p4-382-2026-5-9-e2-layout-routing-manufacturability-route-integration.md`

Boundary:
- no exact component spacing, no enclosure-fit guarantee, and no universal assembly-clearance rule

### 7. `exact_spacing_numeric_claim`

Disposition:
- `blocked`

Reason:
- all exact spacing numbers, common values, and acceptable-value wording remain blocked in this lane

### 8. `design_rule_menu_and_vendor_capability_claim`

Disposition:
- `blocked`

Reason:
- CAD menu paths, factory capability, `IPC` standard-grade overclaims, and promo language are not reusable authority here

## Safe Reuse Classes

1. `electrical_vs_nonelectrical_spacing_taxonomy`
2. `trace_pad_via_and_component_spacing_as_distinct_review_surfaces`
3. `spacing_as_manufacturability_reliability_and_assembly_risk_topic_family`
4. `copper_to_board_edge_as_edge_risk_release_review_surface`
5. `silkscreen_to_pad_overlap_as_manufacturing_data_conflict_topic`
6. `mechanical_3d_height_and_horizontal_clearance_as_fit_review_surface`

## Blocked Claim Classes

1. `all_exact_trace_pad_pad_via_board_edge_and_component_spacing_numerics`
2. `all_exact_hole_diameter_and_hole_tolerance_claims`
3. `all_common_value_best_value_and_barely_acceptable_threshold_wording`
4. `all_voltage_conditioned_clearance_truth_or_pass_fail_threshold_claims`
5. `all_cad_menu_path_as_authority_claims`
6. `all_vendor_capability_standard_and_promo_outcome_claims`

## Explicit Route Decision

This PDF is usable only for conservative safety-distance taxonomy and spacing-boundary routing:

- electrical versus non-electrical spacing taxonomy
- traces, pads, vias, board edge, silkscreen, and components as distinct spacing review surfaces
- spacing as a manufacturability/reliability/assembly-risk topic family
- copper-to-board-edge setback as edge-risk review
- silkscreen-to-pad overlap as manufacturing-data conflict
- horizontal and 3D clearance as mechanical-fit review

It does not justify any exact spacing threshold, hole/via numeric, `best/common/acceptable` value wording, CAD-rule menu authority, or vendor capability/promo claim.

## Completion Status

- `completed_at_single_pdf_route_level_only`
- `source_backed_route_available_without_new_fact_promotion`
- `not_completed_for_fact_promotion_or_official_source_recovery`
