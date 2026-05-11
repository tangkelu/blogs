# P4-334 E2 Impedance Tolerance Difficulty Route Integration

Date: 2026-05-09
Parent state: `after P4-309, P4-310, and P4-331`
Execution mode: `single_pdf_usage_route_integration_only`
Model: `gpt-5.4`
Lane ownership: `E2 single-PDF route integration for impedance-control difficulty`

## Purpose

Route `/code/blogs/tmps/PCB资料/PCB文章/PCB阻抗误差控制在5%，究竟有多难？.pdf` into already-landed repo-backed impedance, stackup, glass-effect, and measurement-boundary surfaces without promoting article-origin claims into facts.

This lane does not create or modify facts, wiki pages, trackers, or unrelated logs.
This lane treats the PDF and extracted pages as claim inventory only.

## Inputs Read

- `/code/blogs/tmps/PCB资料/PCB文章/PCB阻抗误差控制在5%，究竟有多难？.pdf`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB阻抗误差控制在5-究竟有多难/pages/page-0001.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB阻抗误差控制在5-究竟有多难/pages/page-0002.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB阻抗误差控制在5-究竟有多难/pages/page-0003.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB阻抗误差控制在5-究竟有多难/pages/page-0004.txt`
- `/code/blogs/llm_wiki/logs/p4-310-2026-5-8-pcb-article-e2-usage-route-integration.md`
- `/code/blogs/llm_wiki/logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `/code/blogs/llm_wiki/facts/methods/controlled-impedance-tdr-verification-posture.md`
- `/code/blogs/llm_wiki/facts/methods/pcb-impedance-and-rf-measurement-method-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/spread-glass-and-controlled-impedance-planning.md`
- `/code/blogs/llm_wiki/wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`
- `/code/blogs/llm_wiki/wiki/testing/rf-validation-and-test-coverage.md`

## Article Claim Inventory

The PDF mainly asserts these claim families:

- tighter impedance tolerance is hard because many fabrication variables contribute to final impedance variation
- impedance is affected by conductor geometry, dielectric properties, dielectric thickness, and solder-mask effects
- glass-fiber versus resin variation creates a fiber-weave style uncertainty class
- line-width, copper-thickness, and dielectric-thickness control are presented as major process sensitivities
- lamination consistency is presented as especially important for multilayer impedance control
- outer-layer solder-mask application is presented as a factor that shifts impedance
- the article argues that design margin is often a more realistic control strategy than pushing fabrication tolerance tighter
- the PDF also contains supplier-marketing shell and capability-style language

## Reused Repo-Backed Source / Fact / Wiki Surfaces

### 1. Spread-Glass And Controlled-Impedance Planning

Safe reuse target:

- `facts/methods/spread-glass-and-controlled-impedance-planning.md`

What this PDF can safely reinforce:

- fiber-weave or glass-versus-resin variation belongs to controlled-impedance planning
- material selection, glass style, stackup planning, and validation posture belong in one planning branch
- random placement relative to weave is a valid uncertainty class at the qualitative level

What this PDF does not newly prove:

- any exact dielectric-constant values
- any quantified skew or impedance-shift outcome
- any universal mitigation recipe

### 2. Controlled-Impedance Verification Posture

Safe reuse target:

- `facts/methods/controlled-impedance-tdr-verification-posture.md`

What this PDF can safely reinforce:

- impedance control should be treated as a fabrication-plus-verification problem, not as geometry intent alone
- when an article discusses difficult tolerance holding, later writing can route into verification posture instead of promising fabrication precision

What this PDF does not newly prove:

- any exact acceptance band
- any universal coupon coverage
- any promise that every build receives identical verification depth

### 3. Measurement-Method Boundary

Safe reuse target:

- `facts/methods/pcb-impedance-and-rf-measurement-method-boundary.md`
- `wiki/testing/rf-validation-and-test-coverage.md`

What this PDF can safely reinforce:

- impedance discussion should stay tied to method vocabulary such as characteristic-impedance verification rather than being turned into a generic capability claim
- fabrication difficulty and measurement identity are different things and should remain separated

What this PDF does not newly prove:

- any supplier-specific tolerance capability
- any RF performance claim
- any broader finished-board pass/fail outcome

### 4. Advanced Stackup And Fabrication Planning

Safe reuse target:

- `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`

What this PDF can safely reinforce:

- impedance-sensitive work belongs inside stackup architecture and fabrication-planning workflow
- conductor geometry, dielectric construction, lamination behavior, and outer-layer finishing all sit inside the same process branch
- design margin can be framed as a planning response to fabrication variation

What this PDF does not newly prove:

- any default stackup recipe
- any exact dielectric or copper-thickness rule
- any multilayer capability guarantee

## Route Decision

Controller outcome for this PDF:

- this article supports only existing repo-backed surfaces and does not unlock any new reusable fact layer by itself
- route the PDF into the existing `E2` impedance-difficulty and process-variation bucket only
- keep reuse at qualitative planning, uncertainty, and boundary level
- do not elevate any article tolerance, process window, equipment, capability, or marketing-shell claim

## Safe Reuse Classes

- `impedance_control_as_multivariable_fabrication_problem`
- `fiber_weave_effect_as_uncertainty_class_in_impedance_planning`
- `geometry_dielectric_lamination_and_mask_all_affect_impedance`
- `stackup_and_material_choices_must_be_planned_with_validation_posture`
- `design_margin_is_a_safe_system_level_response_to_process_variation`
- `measurement_identity_must_stay_separate_from_supplier_capability_claim`

## Blocked Claims

The following claim classes remain blocked for reuse from this PDF:

- all article-origin tolerance percentages and comparisons among common, tighter, or aspirational impedance windows
- all exact dielectric-constant numbers for glass cloth, resin, or other material constituents
- all exact line-width, copper-thickness, dielectric-thickness, or solder-mask-effect numbers
- all exact impedance-drop examples attributed to one or more solder-mask passes
- all claims that specific exposure, etching, compensation, or lamination controls are sufficient to guarantee a target tolerance
- all supplier capability claims, including layer-count, minimum line-width / spacing, or stated impedance-control quality
- all equipment-quality claims inferred from the article alone
- all branded CTA, download, QR, and promotional shell content

## Per-Claim Routing Map

| Article claim family | Route status | Reuse path | Notes |
| --- | --- | --- | --- |
| many process variables affect final impedance | `safe_reuse` | `p4-310` plus `advanced-pcb-fabrication-and-stackup-planning` | matches existing process-planning posture |
| fiber-weave variation creates randomness in impedance outcome | `safe_reuse_with_boundary` | `spread-glass-and-controlled-impedance-planning` | qualitative uncertainty only |
| impedance should be treated as a fabrication-control problem | `safe_reuse_with_boundary` | `controlled-impedance-tdr-verification-posture` | planning and verification posture only |
| tight tolerance targets are difficult in practice | `safe_reuse_with_boundary` | `p4-310` plus `pcb-impedance-and-rf-measurement-method-boundary` | difficulty framing only, not capability proof |
| line-width / copper / dielectric / mask changes shift impedance | `safe_reuse` | `advanced-pcb-fabrication-and-stackup-planning` | no article numerics reused |
| design for more system margin instead of assuming perfect fab control | `safe_reuse` | `advanced-pcb-fabrication-and-stackup-planning` | safe as qualitative engineering posture |
| common fab tolerance window is a settled industry norm | `blocked_pending_source_recovery` | none | needs official or dated capability evidence |
| exact solder-mask pass impact on impedance | `blocked` | none | article-origin numeric claim |
| exact line-width tolerance needed to hold impedance | `blocked` | none | article-origin numeric claim |
| named supplier capability and promotional manufacturing claims | `blocked` | none | supplier-specific and marketing-shell content |

## Residual Gaps

This lane does not close:

- official-source support for generic industry impedance-tolerance norms
- official-source support for fiber-weave effect and mitigation outside existing internal planning posture
- quantified solder-mask impact boundaries under defined structures and conditions
- public, dated fabricator capability evidence for any supplier-specific tolerance or geometry claim
- exact acceptance, coupon, or verification-coverage policy for current production programs

## Status

This single PDF is now:

- `usage_route_integrated_at_single_pdf_level_only`

What is true now:

- later agents do not need to reread the article to know what is safe to reuse
- the PDF is attached to existing repo-backed impedance-planning, spread-glass, measurement-boundary, and testing surfaces
- the blocked numeric and supplier-capability claim classes are explicit

What is not true now:

- this PDF is not fact-promoted
- this PDF does not establish new tolerances, recipes, or capability facts
- this PDF does not close the official-source gap for tight impedance-control claims

## Recommended Next Action

Recommended next action: `none_inside_this_lane`

If a future lane wants to narrow blockers, the highest-value recovery targets would be:

- official sources on fiber-weave effect, impedance planning, and test-method scope
- dated supplier capability records for any customer-facing tolerance commitment
- stronger source-backed boundaries for solder-mask impact and lamination-sensitive impedance variation
