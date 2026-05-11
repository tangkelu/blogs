# P4-312 PCB Article E4 Usage Route Integration

Date: 2026-05-08
Parent inputs:
- `/code/blogs/tmps/PCB资料/PCB文章`
- `P4-283E`
- `P4-309`
- `2026-05-08-pcb-ziliao-full-pdf-learning-and-usage-plan`
- `/root/.codex/skills/llm-wiki-workflow/SKILL.md`
Execution mode: `controller_lane_usage_routing_only`

## Purpose

Route the `E4` article cluster into usage-safe controller classes for later reuse, evidence preservation, and authority recovery planning.

This lane does not promote article-origin edge-clearance numbers, mark sizes, character sizes, rail widths, panel defaults, capability claims, quality claims, or supplier rule tables into reusable authority.

The `PCB文章` PDFs and any `tmps` derivatives remain claim inventory only.

## Scope

E4 input PDFs covered by this lane:

- `PCB可制造性设计及案例分析之字符、外形、拼板（图文结合，推荐）.pdf`
- `PCB拼板，不得不注意的10个问题！.pdf`
- `PCB板各种形状的拼版实例分享.pdf`
- `啥？PCB拼版对SMT组装有影响！.pdf`
- `PCB板的Mark点设计对SMT重要性.pdf`
- `元器件到PCB板边缘间距不足的严重性.pdf`
- `PCBA板边器件布局重要性.pdf`
- `PCB字符的DFM（可制造性）设计.pdf`

## Controller Reading

This lane is useful for:

- panelization and outline subfamily naming
- board-edge and assembly-interface risk taxonomy
- Mark / fiducial role framing
- character / legend manufacturability-risk framing
- local-evidence selection planning
- official-source gap discovery

This lane is not usable as authority for:

- threshold tables
- panel geometry defaults
- edge-clearance defaults
- mark geometry defaults
- character stroke, height, spacing, or keep-out numbers
- manufacturability pass/fail judgments
- factory capability, quality, cost, or delivery claims

## Safe Reuse Classes

These classes are safe to reuse later as neutral controller vocabulary, usage routing, or wiki-planning concepts when kept non-numeric and non-capability-bearing:

1. `panelization_method_selection_taxonomy`
   - Panelization choice depends on board outline regularity, depanel path style, and connection strategy.
   - Irregular, circular, half-hole, or edge-protruding boards belong to special handling branches.

2. `assembly_facing_panel_handling_taxonomy`
   - A panel can be fabrication-valid yet still create assembly-handling, conveyor, clamping, or depaneling problems.
   - Rail presence, orientation clarity, and machine-facing handling posture are reusable risk-family concepts.

3. `outline_and_connection_feature_risk_taxonomy`
   - Break tabs, V-CUT-style separation intent, bridge placement, corner relief, and slot-assisted outline access are reusable outline-risk classes.
   - Safe reuse stops at mechanism and branch identity, not numeric design closure.

4. `board_edge_component_exposure_taxonomy`
   - Components near the board edge belong to interference, impact, stress, and pad-damage risk families.
   - Taller parts, overhanging parts, and fragile edge-near structures require explicit edge-awareness in review.

5. `mark_fiducial_alignment_taxonomy`
   - Mark points serve optical alignment roles at panel, board, and local-component scope.
   - Asymmetry, visibility, and visual cleanliness are reusable framing concepts for Mark usefulness.

6. `character_legend_manufacturability_taxonomy`
   - Silkscreen / character content belongs to readability, obstruction, contamination, and misidentification risk families.
   - Character manufacturability can be routed safely as a fabrication-communication topic without promoting exact sizing rules.

7. `character_vs_assembly_marking_boundary`
   - E4 covers printed-character manufacturability and obstruction risk.
   - Assembly polarity, pin-1 semantics, and placement-facing legend communication stay in `E5`, not this lane.

## Blocked Classes

Do not promote these classes from the E4 article PDFs:

1. `all_numeric_panel_and_edge_rules`
   - edge-clearance distances
   - rail widths
   - panel border dimensions
   - tab counts, bridge widths, web widths, or slot sizes
   - V-CUT distances, no-gap / gap numbers, or panel-center spacing values

2. `all_mark_geometry_and_keepout_numbers`
   - Mark diameters
   - opening sizes
   - copper-clearance numbers
   - local Mark spacing defaults

3. `all_character_geometry_rules`
   - stroke widths
   - character heights
   - line widths
   - spacing, keep-out, or offset numbers

4. `panel_default_and_factory_capability_claims`
   - statements that a panel style is standard, recommended by default, or universally acceptable
   - statements implying a factory can always build, assemble, route, or depanel a cited structure

5. `quality_cost_delivery_and_yield_claims`
   - claims about quality improvement, lower damage rate, lower cost, better yield, or faster delivery

6. `vendor_rule_tables_and_branded_workflow_claims`
   - red/yellow/green rule matrices
   - software-check screenshots
   - supplier-specific DFM defaults
   - article case conclusions that depend on branded workflow shells

7. `universal_acceptance_judgments`
   - any wording that a specific edge-near layout, Mark pattern, panel shape, or character arrangement is definitely passable or unpassable without stronger authority

## Local Evidence Candidates

These are candidates for later `local_evidence_now` handling if neutral subregions can be preserved without branded shells, CTA banners, or embedded threshold tables:

1. `irregular_panelization_examples`
   - circular, irregular, half-hole, or protruding-edge panel examples
   - bridge or breakout examples that explain why a special branch exists

2. `assembly_interference_panel_visuals`
   - no-gap vs gapped interference examples
   - rail / clamping / conveyor obstruction examples
   - orientation ambiguity examples where symmetry hides machine intent

3. `board_edge_damage_or_collision_visuals`
   - edge-near component strike, stress, or depanel-damage illustrations
   - nozzle, clamp, or fixture interference examples

4. `mark_placement_and_cleanliness_visuals`
   - global vs local Mark placement examples
   - asymmetry and visibility examples
   - blocked or contaminated Mark region examples

5. `character_obstruction_and_readability_visuals`
   - character printed on pads, holes, or copper-sensitive regions
   - clipped, mirrored, overlapped, or obscured legend examples
   - ambiguous reference text placement examples kept non-numeric

Exclude from local evidence intake:

- QR or CTA surfaces
- vendor software promo pages
- screenshots whose meaning depends on embedded pass/fail tables
- charts that visually encode hidden numeric rule classes
- full pages where branding dominates the technical signal

## Official-Source Recovery Targets

These are the preferred authority-recovery directions if the controller later promotes E4 beyond routing-only status:

1. `ipc_or_primary_panelization_handling_guidance`
   - recover primary guidance for panel handling concepts, depaneling intent vocabulary, and assembly-facing panel considerations
   - goal: terminology and workflow framing, not unsupported default dimensions

2. `pcb_fabrication_drawing_and_outline_terminology`
   - recover stronger terminology for board outline definition, routing intent, breakaway features, and drawing communication
   - goal: support neutral outline-language reuse

3. `component_vendor_or_standard_mechanical_keepout_guidance`
   - recover primary guidance for edge-sensitive parts, protrusion constraints, and package mechanical keepout interpretation
   - goal: strengthen board-edge risk framing without promoting article distances

4. `fiducial_mark_alignment_guidance`
   - recover official or primary assembly documentation for global/local fiducial purpose, recognition conditions, and alignment vocabulary
   - goal: support Mark terminology and usage boundaries

5. `ipc_library_or_legend_printing_guidance`
   - recover primary guidance for silkscreen / legend readability, obstruction avoidance, and fabrication-printing terminology
   - goal: support character manufacturability wording without importing unsupported size rules

6. `depanelization_and_assembly_interaction_guidance`
   - recover primary guidance for depanel stress, panel support, and assembly-process interaction with edge features
   - goal: upgrade mechanism wording, not claim numeric closure

## Route Decision By E4 Subfamily

| Subfamily | Primary route | Controller reason |
| --- | --- | --- |
| panelization method selection | `safe_reuse_class` + `local_evidence_candidate` | the branch taxonomy is reusable and visuals are often more valuable than article text |
| irregular outline and edge-connection design | `safe_reuse_class` + `local_evidence_candidate` + `official_source_recovery_target` | examples help locally; stronger terminology still needs primary sources |
| assembly-facing panel handling | `safe_reuse_class` + `official_source_recovery_target` | mechanism framing is reusable, but defaults and pass/fail rules are blocked |
| board-edge component exposure | `safe_reuse_class` + `local_evidence_candidate` + `official_source_recovery_target` | risk family is reusable; exact clearances remain blocked |
| Mark / fiducial strategy | `safe_reuse_class` + `local_evidence_candidate` + `official_source_recovery_target` | examples are locally useful, normative geometry needs stronger authority |
| character / legend manufacturability | `safe_reuse_class` + `local_evidence_candidate` + `official_source_recovery_target` | obstruction and readability taxonomy is reusable; exact character rules remain blocked |

## Hold Notes

- all `tmps` article numerics remain `claim_inventory_only`
- `E4` should not be used to justify edge-clearance, Mark, character, or panel-default numbers
- `E4` character coverage is limited to manufacturability and print-legibility risk, not polarity or pin-1 semantics
- repeated branded banners, CTA blocks, and software-promo pages remain excluded from reusable evidence
- future fact or wiki promotion should come from official standards, primary assembly/library guidance, or clearly labeled local evidence records

## Status

`controller_routed_at_usage_level_only`

What is complete:

- E4 subfamilies are routed into safe reuse, blocked, local-evidence, and official-source-recovery classes
- the character branch is explicitly integrated into the E4 lane
- the E4/E5 boundary for character vs assembly legend semantics is now explicit

What is not complete:

- no official-source recovery has been performed in this lane
- no `facts/`, `wiki/`, `sources/registry/`, or tracker updates were created here
- no image evidence records were preserved here

## Recommended Next Action

Recommended next action: `local_evidence_now`

Reason:

- the highest immediate value in `E4` is preserving neutral visuals for irregular panelization, board-edge interference, Mark cleanliness, and character obstruction
- many of the article pages in this cluster are example-driven, while official numeric closure for panel and edge rules is fragmented or supplier-scoped
- local evidence can improve later writing safety without overclaiming capability or default-rule authority

If a follow-on controller wants stronger normative wording after local evidence capture, the next recovery priority should be `fiducial_mark_alignment_guidance` and `ipc_library_or_legend_printing_guidance` before any attempt to recover panel-default or edge-clearance numbers.
