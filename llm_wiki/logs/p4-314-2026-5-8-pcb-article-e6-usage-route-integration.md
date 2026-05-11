# P4-314 PCB Article E6 Usage Route Integration

Date: 2026-05-08
Parent inputs:
- `/code/blogs/tmps/PCB资料/PCB文章`
- `p4-283e6-2026-5-7-pcb-article-e6-packages-bom-and-component-selection-alignment-claim-family-map.md`
- `p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `2026-05-08-pcb-ziliao-full-pdf-learning-and-usage-plan.md`
- `/root/.codex/skills/llm-wiki-workflow/SKILL.md`
Execution mode: `controller_lane_usage_routing_only`

## Purpose

Route the `E6` article cluster into usage-safe controller classes for later reuse, local evidence intake, and official-source recovery planning.

This lane does not promote article-origin package dimensions, size-code tables, BOM quantities, stock claims, lead-time claims, pricing claims, procurement promises, or vendor workflow claims into reusable authority.

The `PCB文章` PDFs and any `tmps` derivatives remain claim inventory only.

## Scope

E6 input PDFs covered by this lane:

- `电子元器件封装(Package).pdf`
- `如何解决bom物料与焊盘不匹配问题.pdf`
- `BOM查错助力元器件采购.pdf`
- `如何避免采购电子元器件入坑.pdf`
- `0Ω电阻在PCB板中的5大常见作用.pdf`
- `单层双面多层FPC有何区别？.pdf`

## Controller Reading

This lane splits into two different route families that must not be merged:

1. `technical_identity_subsets`
   - package identity and naming grammar
   - package-to-footprint / pin-count alignment framing
   - BOM identity normalization boundaries
   - 0R resistor role taxonomy
   - FPC structure and layer-family taxonomy

2. `procurement_risk_hold_subsets`
   - sourcing risk stories
   - shortage / cold-material narratives
   - stock, lead-time, and supplier-screening claims
   - vendor-tool or service-workflow promises

The first family can support bounded qualitative reuse.
The second family remains primarily hold-only unless later backed by official or dated vendor-specific authority.

## Safe Reuse Classes

These classes are safe to reuse later as neutral controller vocabulary, usage routing, or wiki-planning concepts when kept non-numeric and non-promissory.

### Technical Identity Subsets

1. `package_identity_grammar`
   - package naming must be separated from exact geometry.
   - package family labels, lead-style families, and code-system identity are reusable as taxonomy only.
   - metric / imperial code presence can be mentioned as an identity-system concept, not as a conversion table.

2. `package_to_footprint_alignment_taxonomy`
   - BOM package identity and PCB land-pattern identity must be checked for alignment before release.
   - pin-count mismatch, package-name mismatch, and library-selection mismatch are reusable failure-family labels.
   - safe reuse stops at review posture and mismatch taxonomy, not dimensional closure.

3. `bom_identity_normalization_boundary`
   - BOM rows should separate electrical identity from package, footprint, and supplier metadata.
   - normalization and reconciliation are reusable workflow concepts.
   - the safe reusable surface is identity hygiene, not article workflow screenshots.

4. `zero_ohm_resistor_role_taxonomy`
   - `0R` parts can be framed as jumper, isolation, configuration, measurement, debug, or placeholder roles.
   - safe reuse is role taxonomy only.
   - package selection, current-handling, and thermal consequences remain blocked pending stronger authority.

5. `fpc_structure_and_layer_taxonomy`
   - single-layer, double-layer, and multilayer FPC belong to distinct structure families.
   - flexibility, routing density, and manufacturing complexity can be reused as qualitative tradeoff framing.
   - safe reuse stops at structure identity and tradeoff direction, not material stacks or dimensional rules.

### Mixed Identity Plus Hold Boundary

6. `procurement_risk_as_review_trigger_not_authority`
   - package ambiguity, alternate-package confusion, and lifecycle uncertainty can be reused only as reasons to trigger stronger review.
   - the reusable part is the existence of sourcing-risk branches, not the article's advice or outcome claims.

## Blocked Classes

Do not promote these classes from the E6 article PDFs:

1. `all_package_dimensions_and_size_tables`
   - package width, length, height, pitch, body-size, land-pattern, and resistor-size values
   - EIA / metric conversion rows
   - pin-count tables used as authority

2. `all_bom_quantities_and_matching_outcomes`
   - line-item counts
   - missing-part counts
   - exact mismatch rates
   - any claim that a matching flow is complete, automatic, or universally sufficient

3. `all_procurement_market_claims`
   - stock levels
   - lead times
   - price, MOQ, or cost claims
   - shortage severity or availability judgments presented as general truth

4. `all_supplier_screening_and_service_promises`
   - claims that a procurement workflow prevents risk by default
   - claims that a vendor tool, service, or platform guarantees matching or sourcing quality
   - supplier-recommendation language presented as reusable authority

5. `all_zero_ohm_part_selection_rules`
   - exact resistance tolerance discussion used beyond identity
   - package recommendations
   - current, power, voltage, or thermal suitability claims
   - statements implying a `0R` part is always safe as jumper or fuse substitute

6. `all_fpc_material_stack_and_rule_values`
   - copper thickness
   - bend radius values
   - adhesive, stiffener, or coverlay defaults
   - layer-count feasibility claims treated as universal design closure

7. `all_quality_yield_cost_and_delivery_claims`
   - quality-rate improvement
   - reduced procurement cost
   - shortened cycle time
   - yield or reliability outcome claims

8. `all_branded_workflow_shells`
   - vendor screenshots
   - QR / CTA surfaces
   - promotional callouts
   - article case conclusions that depend on branded tool context

## Local Evidence Candidates

These are candidates for later `local_evidence_now` handling if neutral subregions can be preserved without branded shells, CTA banners, or embedded threshold tables.

### Technical Identity Candidates

1. `package_identity_visuals`
   - package-family comparison diagrams
   - component-letter or package-category taxonomy panels
   - size-code identity examples where exact rows are not needed

2. `bom_footprint_mismatch_visuals`
   - package-name mismatch examples
   - pin-count mismatch examples
   - BOM-to-footprint reconciliation examples that show the failure family without depending on rule tables

3. `bom_normalization_workflow_panels`
   - neutral diagrams showing BOM cleanup or identity-field separation
   - keep only if the workflow meaning survives removal of product-marketing shell

4. `zero_ohm_usage_visuals`
   - jumper-routing examples
   - isolation / debug branch examples
   - placeholder or configuration-use diagrams kept non-numeric

5. `fpc_layer_structure_visuals`
   - single-layer vs double-layer vs multilayer structure diagrams
   - layer-family illustrations that explain taxonomy without embedded material rules

### Hold-Subset Candidates

6. `procurement_risk_case_panels`
   - preserve only if the panel is useful as local case evidence for ambiguity or shortage narrative
   - do not treat as authority for supply-state conclusions

Exclude from local evidence intake:

- package or resistor dimension tables
- availability dashboards
- pricing, lead-time, or stock screenshots
- supplier-comparison tables
- QR / CTA surfaces
- full pages where branding or workflow promotion dominates the technical signal

## Official-Source Recovery Targets

These are the preferred authority-recovery directions if the controller later promotes E6 beyond routing-only status.

### Technical Identity Recovery Targets

1. `ipc_or_component_vendor_package_terminology`
   - recover primary terminology for package-family identity, naming grammar, and package-vs-land-pattern distinction
   - goal: support neutral vocabulary, not article size-table reuse

2. `ipc_land_pattern_and_library_governance_guidance`
   - recover primary guidance for package-to-footprint alignment, land-pattern review, and library-validation posture
   - goal: upgrade mismatch framing from article case examples to method guidance

3. `bom_data_model_and_plm_identity_guidance`
   - recover primary BOM-field and component-identity guidance from CAD / PLM primary documentation or standards-adjacent sources
   - goal: support BOM normalization language without reusing vendor-promo workflow claims

4. `zero_ohm_component_datasheet_and_application_guidance`
   - recover component-vendor datasheets or application notes for `0R` resistor identity, ratings, and intended use boundaries
   - goal: separate valid role descriptions from unsafe universalization

5. `fpc_structure_terminology_and_design_guidance`
   - recover official or primary guidance for FPC layer-family vocabulary, structure naming, and build-up concepts
   - goal: support taxonomy and qualitative tradeoff wording

### Procurement Hold Recovery Targets

6. `dated_vendor_specific_procurement_guides`
   - recover dated vendor capability or sourcing-guidance documents only if the future task explicitly needs vendor-scoped procurement posture
   - goal: keep any recovery explicitly local, dated, and non-universal

7. `manufacturer_lifecycle_and_supply_status_authority`
   - recover official manufacturer lifecycle notices or distributor primary pages only when a concrete part family is in scope
   - goal: avoid generic procurement advice masquerading as durable fact

## Route Decision By E6 Subfamily

| Subfamily | Primary route | Controller reason |
| --- | --- | --- |
| package identity and naming grammar | `safe_reuse_class` + `local_evidence_candidate` + `official_source_recovery_target` | taxonomy value is real, but dimensions and size tables stay blocked |
| package-to-footprint and pin-count alignment | `safe_reuse_class` + `local_evidence_candidate` + `official_source_recovery_target` | mismatch framing is reusable, closure rules need stronger authority |
| BOM identity normalization | `safe_reuse_class` + `local_evidence_candidate` + `official_source_recovery_target` | field-separation logic is reusable, workflow promises are blocked |
| procurement-risk narratives | `blocked_class` + `local_evidence_candidate` + `official_source_recovery_target` | risk stories are useful only as hold-map triggers, not durable fact |
| `0R` resistor usage roles | `safe_reuse_class` + `local_evidence_candidate` + `official_source_recovery_target` | role taxonomy is reusable, part-selection and ratings remain blocked |
| FPC layer-family taxonomy | `safe_reuse_class` + `local_evidence_candidate` + `official_source_recovery_target` | structure framing is reusable, stack/material rules need primary support |

## Hold Notes

- technical identity subsets and procurement-risk hold subsets must remain explicitly separated in later reuse
- `tmps` article numerics remain `claim_inventory_only`
- package identity can support library-governance and review-language planning, but not dimensional fact closure
- procurement PDFs should not be reused to justify stock, cost, lead-time, supplier-quality, or sourcing-workflow claims
- `0R` resistor articles can support role taxonomy only until vendor datasheets or application notes narrow the safe usage boundary
- FPC article content can support structure naming and qualitative complexity framing only until stronger primary guidance is recovered

## Status

`controller_routed_at_usage_level_only_with_explicit_procurement_hold_split`

What is complete:

- E6 subfamilies are split into technical identity routes and procurement-risk hold routes
- safe reuse, blocked, local-evidence, and official-source-recovery classes are explicit
- later agents can resume this lane without reopening the full article batch

What is not complete:

- no official-source recovery has been performed in this lane
- no `facts/`, `wiki/`, `sources/registry/`, or tracker updates were created here
- no image evidence records were preserved here
- no package dimensions, BOM quantities, sourcing claims, or `0R` selection rules were promoted

## Recommended Next Action

Recommended next action: `source_recovery_now_for_technical_identity_subsets`, while keeping `procurement_risk_hold_subsets` on hold.

Priority order:

1. package-to-footprint / land-pattern governance guidance
2. `0R` resistor datasheet-backed use-boundary recovery
3. FPC structure terminology recovery
4. BOM identity-field guidance

Reason:

- the highest safe value in `E6` is not procurement advice; it is identity and taxonomy recovery
- package alignment, `0R` role boundaries, and FPC structure naming can likely be improved with primary sources
- procurement-risk stories remain too time-sensitive and vendor-scoped to promote from article wording alone
