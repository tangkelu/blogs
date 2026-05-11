# P4-344 E5 Via-In-Pad Manufacturability Route Integration

Date: 2026-05-09
Execution mode: `single_pdf_route_integration_only`
Model: `gpt-5.4`
Lane owner: `P4-344 E5 single-PDF route integration for 元器件虚焊原因之一盘中孔的可制造设计规范.pdf`

## Purpose

Route the single article PDF `元器件虚焊原因之一盘中孔的可制造设计规范.pdf` into already-landed repo-backed via-in-pad, HDI, and BGA assembly-boundary surfaces where safe, while keeping the PDF as `claim_inventory_only` and blocking all article-origin geometry numerics, universal process defaults, cost / lead-time claims, and branded DFM-checker claims.

This pass is single-PDF route integration only. It does not create or update reusable `facts/`, `wiki/`, `sources/registry/`, or trackers.

## Inputs Inspected

- `/code/blogs/tmps/PCB资料/PCB文章/元器件虚焊原因之一盘中孔的可制造设计规范.pdf`
- `/code/blogs/tmps/pcb_pdf_extracted_full/元器件虚焊原因之一盘中孔的可制造设计规范/pages/page-0001.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/元器件虚焊原因之一盘中孔的可制造设计规范/pages/page-0002.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/元器件虚焊原因之一盘中孔的可制造设计规范/pages/page-0003.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/元器件虚焊原因之一盘中孔的可制造设计规范/pages/page-0004.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/元器件虚焊原因之一盘中孔的可制造设计规范/pages/page-0005.txt`
- `/code/blogs/llm_wiki/logs/p4-313-2026-5-8-pcb-article-e5-usage-route-integration.md`
- `/code/blogs/llm_wiki/logs/p4-309-2026-5-8-pcb-ziliao-full-corpus-learning-and-usage-master-plan.md`
- `/code/blogs/llm_wiki/logs/p4-337-2026-5-9-e5-bga-soldering-route-integration.md`
- `/code/blogs/llm_wiki/facts/methods/hdi-microvia-and-vippo-process-posture.md`
- `/code/blogs/llm_wiki/facts/methods/low-void-bga-dfm-to-process-review.md`
- `/code/blogs/llm_wiki/facts/methods/low-void-bga-reflow-paste-vs-assembly-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/hidden-joint-xray-inspection-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/pcba-stencil-selective-solder-and-fine-pitch-controls.md`
- `/code/blogs/llm_wiki/facts/methods/microchip-csp-bga-solder-land-and-pitch-examples.md`
- `/code/blogs/llm_wiki/wiki/processes/low-void-bga-reflow-and-hidden-joint-inspection.md`

## PDF Claim Inventory

Observed article-side claim families from the extracted pages:

1. `via_in_pad_identity_and_scope`
   - the article defines `盘中孔` as via-in-pad on SMD or BGA pads
   - it separates via-in-pad from ordinary through-hole component pads

2. `dense_bga_escape_pressure_to_via_in_pad`
   - the article says dense BGA escape can force layer changes and pad-located vias
   - it treats small-pitch BGA fanout failure as a driver toward via-in-pad

3. `backside_filter_capacitor_via_in_pad_case`
   - the article gives a backside filter-capacitor pad case where dense BGA escape vias conflict with capacitor placement
   - it presents via-in-pad as a congestion workaround family

4. `article_numeric_fanout_geometry`
   - the article gives concrete via, trace-width, annular-ring, and BGA-pitch values for fanout
   - it claims a threshold above which normal fanout is possible and below which via-in-pad is needed

5. `resin_fill_plating_planarization_process_claim`
   - the article says BGA via-in-pad normally needs resin plugging and plated surface treatment for soldering
   - it also describes a local process sequence including drilling, copper plating, resin fill, cure, grinding, and later drilling

6. `untreated_via_in_pad_solderability_failure_claim`
   - the article says untreated via-in-pad reduces effective soldering area
   - it ties unfilled or unprocessed pad vias to solder bead, oil burst, and virtual-solder outcomes

7. `cost_cycle_and_checker_marketing_language`
   - the article claims via-in-pad is expensive and lengthens production cycle
   - it closes with branded DFM-checker sufficiency and cost-reduction messaging

## Existing LLM Wiki Support Found

This PDF has some real overlap with existing repo-backed surfaces, but the overlap is still narrow and boundary-oriented.

### 1. Via-in-pad belongs inside existing HDI / VIPPO posture

Safe route:
- `facts/methods/hdi-microvia-and-vippo-process-posture.md`

Admitted reuse:
- via-in-pad can be described as part of standard dense-interconnect / HDI process posture rather than as an isolated oddity
- dense routing escalation from ordinary fanout toward HDI-style solutions is compatible with the existing `microvia / any-layer / VIPPO` posture
- guarded wording such as `belongs to dense interconnect planning`, `requires process review`, and `should stay tied to HDI context` is supported

Boundary:
- this PDF does not add universal via-in-pad drill, fill, plating, or lamination rules
- it does not prove that every via-in-pad case is `VIPPO` in the exact internal-process sense
- it does not authorize exact geometry or production-window values

### 2. Dense BGA routing pressure can reuse the existing BGA process-review posture

Safe route:
- `facts/methods/low-void-bga-dfm-to-process-review.md`
- `facts/methods/pcba-stencil-selective-solder-and-fine-pitch-controls.md`
- `wiki/processes/low-void-bga-reflow-and-hidden-joint-inspection.md`

Admitted reuse:
- dense BGA escape pressure belongs in a staged package-review and process-review chain
- fine-pitch BGA handling can stay attached to dense-package planning, not treated as ordinary generic SMT
- the article can safely reinforce that via-in-pad discussion often starts from BGA density and downstream assembly sensitivity

Boundary:
- this PDF does not add source-backed BGA pitch-to-fanout thresholds
- it does not add owner-scoped land-pattern authority
- it does not prove that via-in-pad is the only valid route for all dense BGA cases

### 3. One existing owner-scoped package example supports only a narrow existence check

Safe route:
- `facts/methods/microchip-csp-bga-solder-land-and-pitch-examples.md`

Admitted reuse:
- the repo already has one owner-scoped example where `0.4 mm` land pitch uses via in pad
- this is enough to support a limited statement that via-in-pad exists as a documented package-owner layout choice in at least one narrow CSP/BGA context

Boundary:
- this article cannot convert that owner-scoped example into a universal cross-vendor threshold rule
- this article cannot use that example to validate its own generic pitch cutoff, fanout dimensions, or mandatory-treatment language

### 4. Untreated via-in-pad solderability risk has only local mechanism support

Safe route:
- `facts/methods/low-void-bga-reflow-paste-vs-assembly-boundary.md`
- `facts/methods/hidden-joint-xray-inspection-boundary.md`
- `logs/p4-337-2026-5-9-e5-bga-soldering-route-integration.md`

Admitted reuse:
- the article can support a conservative local-mechanism statement that pad-located vias interact with solder transfer and hidden-joint risk review
- it can also reinforce that dense BGA and via-in-pad decisions belong with later reflow and inspection planning, not only layout convenience

Boundary:
- current repo-backed surfaces do not close the article's defect-causality claims for untreated via-in-pad
- this lane does not have primary authority for `resin fill always required`, `plated flat surface always required`, or `untreated pad vias always cause virtual solder`

## Safe Reuse Classes

1. `via_in_pad_as_dense_interconnect_posture`
   - reusable as a neutral statement that via-in-pad belongs in dense interconnect / HDI process posture, not as a casual default

2. `dense_bga_escape_pressure_review_trigger`
   - reusable as a neutral statement that dense BGA escape pressure can trigger review of via strategy, layer-change strategy, and package-specific routing approach

3. `package_owner_scoped_via_in_pad_existence_example`
   - reusable only through existing owner-scoped examples that keep package name, pitch, and source framing attached

4. `local_pdf_scoped_mechanism_examples`
   - untreated via-in-pad can reduce solderable area in the article's mechanism framing
   - backside decoupling or filter-capacitor pad congestion can push layout toward via-in-pad in the article's examples
   - via-in-pad discussion belongs downstream with assembly and inspection review, not only routing convenience

## Blocked Claims

The following claim families remain blocked and must not be promoted from this PDF:

1. `all_article_numeric_fanout_geometry`
   - via diameter values
   - trace-width or spacing values
   - annular-ring values
   - generic BGA pitch cutoffs for normal fanout versus via-in-pad

2. `all_universal_via_in_pad_design_defaults`
   - claims that via-in-pad is the only solution below one pitch threshold
   - claims that every BGA via-in-pad must use the same treatment stack
   - claims that backside capacitor pads should generally accept vias without owner-scoped authority

3. `all_resin_fill_plating_planarization_requirements_as_general_rules`
   - universal resin-plugging defaults
   - universal copper-cap or plated-planarization defaults
   - universal process-sequence requirements from article wording alone

4. `all_defect_certainty_and_virtual_solder_outcome_claims`
   - certainty that untreated via-in-pad always causes virtual solder
   - certainty that solder beads, oil burst, or weak soldering follow from one local geometry alone
   - certainty that one described process treatment always prevents soldering defects

5. `all_cost_lead_time_and_factory_capability_claims`
   - fixed cost penalties
   - long-cycle certainty
   - factory capability assumptions
   - any statement that a board shop will or will not support one via-in-pad route by default

6. `tool_marketing_and_checker_sufficiency_claims`
   - branded DFM-checker completeness
   - claims that software detection alone is enough to resolve manufacturability
   - workflow-superiority claims tied only to the article tool

## Explicit Route Decision

This article advances only to a `limited_route_support` posture above pure cluster inventory.

The narrow result is:

- it safely maps into existing repo-backed surfaces for `via-in-pad as part of HDI / dense interconnect posture`
- it safely maps into existing repo-backed surfaces for `dense BGA escape pressure as a package-review trigger`
- it safely maps into one existing owner-scoped example showing that `via in pad` exists in a real `0.4 mm` package-layout context

It does **not** justify a new fact card or wiki page from this lane.

It also does **not** justify promoting article-origin fanout numerics, resin-fill defaults, plating / planarization defaults, defect-certainty language, cost or cycle claims, or branded checker claims into reusable facts.

If stated plainly: this PDF is useful as claim inventory and limited route support for `via-in-pad as dense-interconnect review posture`, but strong route support remains weak because the article mixes narrow mechanism examples with generic geometry rules, manufacturing defaults, and marketing claims without primary authority.

## Reused Repo-Backed Source / Fact / Wiki Surfaces

### Fact surfaces

- `methods-hdi-microvia-and-vippo-process-posture`
  - primary safe reuse surface for keeping via-in-pad inside dense-interconnect and HDI posture language

- `methods-low-void-bga-dfm-to-process-review`
  - safe reuse surface for tying via-in-pad discussion to staged BGA package and process review

- `methods-pcba-stencil-selective-solder-and-fine-pitch-controls`
  - adjacent safe reuse surface for keeping fine-pitch BGA handling inside one broader process-control chain

- `methods-microchip-csp-bga-solder-land-and-pitch-examples`
  - narrow owner-scoped existence surface for `0.4 mm` pitch using via in pad

- `methods-low-void-bga-reflow-paste-vs-assembly-boundary`
  - adjacent boundary surface for keeping solderability language attached to real assembly context instead of universal article claims

- `methods-hidden-joint-xray-inspection-boundary`
  - adjacent boundary surface for keeping hidden-joint risk language separate from acceptance or defect-certainty overclaims

### Wiki surfaces

- `processes-low-void-bga-reflow-and-hidden-joint-inspection`
  - receives the article only as route support for dense-package review posture, not as parameter authority

### Existing controller log surfaces

- `p4-313`
  - this PDF remains inside the earlier `bga_soldering_issue_taxonomy` safe reuse class
  - this PDF also remains inside the earlier `official_source_recovery_target` posture for BGA package and board-assembly guidance

- `p4-337`
  - this PDF overlaps the earlier BGA route note on `via-in-pad fill / planarization need`, but this lane does not strengthen that earlier note into fact promotion
  - this lane narrows the best safe reading to `HDI / VIPPO posture plus BGA process-review adjacency`

- `p4-309`
  - corpus status remains `usage_route_covered_at_controller_level_only`
  - this single-PDF lane does not change the broader `E5` corpus truth

## Residual Gaps

1. primary or owner-scoped support for via-in-pad treatment boundaries
   - needed before resin fill, plated-overfill, planarization, or process-sequence language can move above limited-route posture

2. stronger package-owner support for dense-BGA fanout decision boundaries
   - needed before any pitch, escape, or routing-threshold claim can be reused

3. stronger primary support for untreated via-in-pad defect mechanisms
   - needed before solder-starvation or virtual-solder outcomes can be generalized

4. stronger authority for backside decoupling-pad via-in-pad tradeoffs
   - needed before the capacitor-pad example can become reusable design guidance

5. stronger authority for commercial and schedule implications
   - needed before any cost, lead-time, or manufacturability-superiority claim can be stated

## Status

`limited_route_support_for_via_in_pad_hdi_posture_only`
