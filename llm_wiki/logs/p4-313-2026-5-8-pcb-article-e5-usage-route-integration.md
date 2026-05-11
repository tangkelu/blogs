# P4-313 PCB Article E5 Usage Route Integration

Date: 2026-05-08
Parent inputs:
- `/code/blogs/tmps/PCB资料/PCB文章`
- `P4-283`
- `P4-283E`
- `P4-286`
- `2026-05-08-pcb-ziliao-full-pdf-learning-and-usage-plan`
Execution mode: `controller_lane_usage_routing_only`

## Purpose

Route the `E5` article cluster into usage-safe controller classes without promoting article-PDF numerics, vendor capability claims, acceptance judgments, or assembly-yield claims into reusable facts.

This lane treats the `PCB文章` PDFs and extracted `tmps` assets as claim inventory and local evidence candidates, not authority.

## Scope

E5 input PDFs covered by this lane:

- `DFA是什么？这些组装性问题你都知道怎么解决吗？.pdf`
- `关于PCBA元器件布局的重要性.pdf`
- `组装电子元器件间距不足的严重性.pdf`
- `如何避免踩坑钢网.pdf`
- `你想知道的BGA焊接问题都在这里.pdf`
- `那些关于DIP器件不得不说的坑.pdf`
- `元器件虚焊原因之一盘中孔的可制造设计规范.pdf`
- `PCBA丝印位号与极性符号的组装性设计.pdf`
- `PCB测试四大方式你都了解吗？内含治具的DFM（可制造性）设计！.pdf`

## Controller Reading

The lane is useful for:

- subfamily naming
- defect-mechanism taxonomy
- process-step identity
- image and case-example preservation planning
- official-source gap discovery

The lane is not usable as authority for:

- threshold tables
- vendor rule defaults
- process-window numbers
- manufacturability pass/fail judgments
- capability, cost, delivery, or yield claims

## E5 Subfamily Routing

### Safe Reuse Classes

These classes are safe to reuse later as `usage routing` or `wiki planning` concepts once kept at neutral, non-numeric wording:

1. `assembly_risk_taxonomy`
   - DFA / assembly review can be framed as early detection of placement, access, repairability, and orientation risks.
   - Source PDFs: `DFA是什么？这些组装性问题你都知道怎么解决吗？.pdf`, `关于PCBA元器件布局的重要性.pdf`

2. `component_spacing_and_access_risk_taxonomy`
   - Component-to-component crowding, board-edge exposure, tall-part interference, and rework obstruction are valid risk-family labels.
   - Source PDFs: `DFA是什么？这些组装性问题你都知道怎么解决吗？.pdf`, `关于PCBA元器件布局的重要性.pdf`, `组装电子元器件间距不足的严重性.pdf`

3. `stencil_and_paste_transfer_identity`
   - Stencil purpose, paste-layer relationship, mark-point correspondence, and aperture-design-as-risk-surface are reusable concept classes.
   - Source PDF: `如何避免踩坑钢网.pdf`

4. `bga_soldering_issue_taxonomy`
   - BGA routing pressure, via treatment dependence, solderability risk, and inspection/rework difficulty are reusable topic families.
   - Source PDFs: `你想知道的BGA焊接问题都在这里.pdf`, `元器件虚焊原因之一盘中孔的可制造设计规范.pdf`

5. `dip_tht_fit_and_wave_solder_risk_taxonomy`
   - Through-hole fit mismatch, lead pitch mismatch, insertion failure, and wave-solder bridging are reusable failure-family labels.
   - Source PDF: `那些关于DIP器件不得不说的坑.pdf`

6. `polarity_pin1_and_reference_designator_clarity`
   - Reference designator visibility, polarity clarity, and pin-1 orientation are reusable assembly-communication classes.
   - Source PDF: `PCBA丝印位号与极性符号的组装性设计.pdf`

7. `test_method_identity_and_fixture_readiness`
   - AOI, flying probe, fixture test, and visual inspection are reusable test-method identity labels.
   - Locator holes and board-fixturing readiness are reusable testability-planning classes.
   - Source PDF: `PCB测试四大方式你都了解吗？内含治具的DFM（可制造性）设计！.pdf`

### Blocked Classes

Do not promote these classes from the E5 article PDFs:

1. `all_numeric_thresholds_and_ratios`
   - component spacing numbers
   - lead-to-hole numbers
   - BGA pad / ball ratio numbers
   - via, hole, locator, or stencil process values

2. `acceptance_or_capability_claims`
   - statements that a design is definitely buildable, testable, reliable, or acceptable
   - factory-readiness claims tied only to article wording

3. `yield_quality_cost_delivery_claims`
   - defect-rate reduction
   - quality-rate improvement
   - shortened cycle, lower cost, faster delivery

4. `vendor_rule_tables_and_color_grading`
   - red/yellow/green safety grading
   - packaged rule matrices
   - branded default checks and screenshot-driven rules

5. `tool_feature_and_library_claims`
   - BOM matching coverage
   - rule-count claims
   - software workflow superiority claims

6. `article_case_outcomes_as_general_authority`
   - isolated examples of shorts, open solder, burning, or failure cannot become generalized acceptance guidance without stronger authority

### Local-Evidence Candidates

These are candidates for later `local_pdf_evidence` handling if the main agent chooses to preserve clean subregions without branded banners, CTA shells, or threshold tables:

1. `dfa_case_illustrations`
   - placement conflict examples
   - board-edge interference examples
   - oversized or asymmetric pad examples

2. `spacing_and_rework_obstruction_examples`
   - connector crowding
   - large-part adjacency
   - large-part-over-small-part repair blockage

3. `stencil_structure_and_mark_examples`
   - paste-layer identity diagrams
   - stencil mark-point correspondence illustrations
   - aperture-shape or notch examples that explain defect mechanism without relying on article thresholds

4. `bga_and_via_in_pad_process_examples`
   - BGA solderability problem illustrations
   - via-in-pad process-sequence images
   - filtered images showing why untreated via-in-pad can starve solder

5. `dip_fit_mismatch_examples`
   - lead-to-hole mismatch examples
   - pitch mismatch examples
   - wave-solder bridging examples

6. `polarity_and_pin1_marking_examples`
   - covered reference designator cases
   - ambiguous polarity marking cases
   - incorrect or missing pin-1 orientation examples

7. `test_fixture_and_locator_examples`
   - fixture-contact concept figures
   - locator-hole readiness illustrations
   - no-locator testing obstruction examples

### Official-Source Recovery Targets

These are the preferred authority-recovery directions if the main agent later promotes E5 beyond controller routing:

1. `ipc_assembly_design_and_land_pattern_guidance`
   - recover official guidance for assembly-oriented spacing, rework access, and pad/land-pattern intent
   - likely source families: IPC assembly design and land-pattern standards

2. `ipc_stencil_and_solder_paste_guidance`
   - recover official guidance for stencil aperture design, paste-transfer principles, and print-related defect mechanisms
   - likely source families: IPC stencil / solder-paste design references

3. `ipc_jstd_soldering_acceptability_and_process_guidance`
   - recover official guidance for soldering defect terminology, through-hole / SMT workmanship framing, and process interpretation boundaries
   - likely source families: J-STD / IPC soldering documents

4. `bga_package_and_board_assembly_guidance`
   - recover official or package-vendor guidance for BGA land pattern, via-in-pad treatment expectations, and assembly considerations
   - likely source families: semiconductor package application notes, IPC package guidance

5. `tht_connector_and_dip_package_datasheet_guidance`
   - recover component-vendor datasheets for lead diameter, pitch, recommended hole size, and mounting pattern intent
   - likely source families: connector / DIP component datasheets

6. `silkscreen_polarity_and_pin1_marking_guidance`
   - recover official package-marking and library-guideline sources for polarity, orientation, and reference-mark visibility
   - likely source families: IPC library / land-pattern guidance, package datasheets

7. `testability_and_fixture_design_guidance`
   - recover official testability guidance for test access, fixture strategy, and locator-hole planning
   - likely source families: IPC testability standards and fixture-design guidance

## Route Decision By E5 Subfamily

| Subfamily | Primary route | Controller reason |
| --- | --- | --- |
| DFA / assembly review | `safe_reuse_class` | useful as neutral risk taxonomy only |
| component spacing / repair access | `safe_reuse_class` + `official_source_recovery_target` | concept is reusable, thresholds are blocked |
| stencil / paste / mark | `safe_reuse_class` + `local_evidence_candidate` + `official_source_recovery_target` | diagrams may be worth keeping, design rules need authority |
| BGA soldering / via-in-pad | `safe_reuse_class` + `local_evidence_candidate` + `official_source_recovery_target` | strong mechanism value, numeric and capability claims blocked |
| DIP / THT fit | `safe_reuse_class` + `official_source_recovery_target` | datasheet-backed recovery is better than article reuse |
| polarity / pin-1 / designators | `safe_reuse_class` + `local_evidence_candidate` + `official_source_recovery_target` | examples are locally useful, normative rules need authority |
| test methods / fixture readiness | `safe_reuse_class` + `official_source_recovery_target` | method names are reusable, locator-hole rules need authority |

## Hold Notes

- `tmps` article numerics remain `claim_inventory_only`
- repeated `华秋DFM` banners, CTA blocks, and software-promo pages remain excluded from reusable evidence
- article case anecdotes can guide search and local evidence selection, but not acceptance judgment
- any future E5 fact or wiki promotion should be sourced from official standards, package-vendor documents, or clearly labeled local-PDF evidence records

## Status

`controller_routed_at_usage_level_only`

What is complete:

- E5 subfamilies are now routed into safe reuse, blocked, local-evidence, and official-source-recovery classes
- later agents can resume without reopening the whole article batch

What is not complete:

- no official-source recovery has been performed in this lane
- no `facts/`, `wiki/`, `sources/registry/`, or tracker updates were created here
- no image evidence records were preserved here

## Recommended Next Action

Recommended next action: `source_recovery_now` on the highest-value E5 authority gaps, starting with:

1. BGA / via-in-pad assembly guidance
2. stencil / solder-paste aperture guidance
3. testability / fixture / locator-hole guidance

If immediate authority recovery is out of scope, the fallback next action is `local_evidence_now` for clean E5 diagrams that explain mechanism without carrying branded tables or vendor thresholds.
