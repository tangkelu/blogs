# P4-311 PCB Article E3 Usage Route Integration

Date: 2026-05-08
Parent plan: `P4-309` / `2026-05-08-pcb-ziliao-full-pdf-learning-and-usage-plan`
Input directory: `/code/blogs/tmps/PCB资料/PCB文章`
Prior map: `p4-283e3-2026-5-7-pcb-article-e3-claim-family-boundary-map.md`
Execution mode: `controller_usage_route_integration_only`

## Scope

This lane routes the `E3` fabrication-features article cluster into usage classes for later controller action.

It does not promote article-origin numerics, capability limits, certification claims, vendor rule tables, yield claims, lead-time claims, MOQ claims, pricing claims, or quality-rate claims into reusable authority.

Temporary article PDFs remain claim inventory only.

## Cluster Coverage

Primary `E3` article inputs identified from the batch:

- `PCB可制造性设计及案例分析之孔槽篇.pdf`
- `器件引脚的方槽、方孔如何避坑？.pdf`
- `器件引脚小尺寸的孔和槽如何避坑？.pdf`
- `PCB板漏孔、漏槽在设计端如何避坑.pdf`
- `一招搞定PCB阻焊过孔问题.pdf`
- `这样做，轻松拿捏阻焊桥！.pdf`
- `PCB设计如何防止阻焊漏开窗.pdf`
- `PCB焊盘设计之问题详解.pdf`
- `多层板的焊盘到底应该怎么设计？四种主要设计方式带你搞懂！.pdf`
- `千万不能小瞧的PCB半孔板.pdf`
- `PCB“金手指”从设计到生产全流程.pdf`
- `如何避免“断头线”带来的DFM（可制造性）问题？.pdf`
- `PCB设计孔间距的DFM可靠性.pdf`

## Safe Reuse Classes

These classes are safe for later reuse as vocabulary, failure-mode framing, or workflow posture only:

- `hole_and_slot_intent_taxonomy`
  - plated vs non-plated intent must be expressed explicitly in design outputs
  - hole and slot definitions carry both electrical and fabrication meaning
- `cad_export_failure_modes`
  - omitted holes, omitted slots, and malformed fabrication outputs are recurring data-handoff failure families
  - CAM / fabrication review should confirm intended holes, slots, and related feature presence before release
- `small_feature_manufacturability_risk_taxonomy`
  - very small holes and slots belong to a manufacturability-risk family
  - risk wording may be reused without article thresholds
- `via_mask_treatment_taxonomy`
  - via mask treatment is scenario-dependent rather than universal
  - the safe reusable surface is the existence of multiple treatment choices plus review need
- `solder_mask_opening_and_bridge_control_taxonomy`
  - solder-mask opening completeness and bridge preservation are defect-prevention families
  - blocked values remain blocked, but the defect-prevention taxonomy is reusable
- `pad_geometry_and_pad_mask_relationship_taxonomy`
  - pad geometry, pad symmetry, and pad-to-mask relationship affect assembly outcome and defect risk
  - safe reuse stays at mechanism and review posture level
- `edge_feature_special_handling_taxonomy`
  - castellated / half-hole and gold-finger edge features require special fabrication and handoff handling
  - edge-connector contact regions are distinct from ordinary pads
- `hole_spacing_reliability_taxonomy`
  - hole-to-hole spacing belongs to reliability and failure-risk framing
  - exact spacing rules remain blocked pending stronger authority
- `trace_stub_and_break_risk_taxonomy`
  - broken trace remnants and residual copper artifacts can be treated as DFM risk families

## Blocked Classes

The following remain blocked for direct reuse from the article batch:

- all exact drill sizes, slot widths, pad sizes, annular-ring values, mask-expansion values, bridge-width values, and hole-spacing values
- all process-window tables, vendor DFM charts, traffic-light thresholds, and pass/fail screenshots that encode hidden numeric rules
- all claims that a specific small hole, slot, via, pad, bridge, half-hole, or gold-finger structure is manufacturable by default
- all yield, first-pass rate, defect-rate, scrap-rate, cost, price, MOQ, lead-time, or turnaround statements
- all equipment-proof, capability-proof, qualification-proof, certification-proof, or supplier-readiness claims
- all statements that imply universal acceptance criteria for via tenting, via opening, mask bridge, pad design, half-hole design, gold-finger design, or hole spacing
- all article-origin remediation sequences that depend on branded tool screenshots or vendor-specific export settings

## Local Evidence Candidates

These are candidates for future `local_evidence_now` handling if clean captures can be isolated without embedded thresholds or branded contamination:

- `hole_slot_ambiguity_visuals`
  - diagrams showing plated vs non-plated hole/slot intent differences
  - diagrams showing round hole vs slot vs square-feature representation differences
- `export_failure_visuals`
  - screenshots showing missing slot, missing hole, or zero-diameter / omitted-feature failure modes
- `via_mask_treatment_visuals`
  - neutral diagrams comparing common via mask treatment options if no rule table is embedded
- `mask_bridge_failure_visuals`
  - examples of bridge loss, opening omission, or bridging-risk visual categories without numeric overlays
- `pad_mismatch_visuals`
  - illustrations of pad asymmetry, package-to-pad mismatch, or equal-size pad-pattern risk examples
- `half_hole_and_edge_feature_visuals`
  - neutral visuals for half-hole / castellated edge construction and gold-finger region identity
- `hole_spacing_failure_visuals`
  - crack, breakout, or structural-risk style images if captions can be kept non-numeric

Exclude from local evidence intake:

- vendor CTA banners
- branded workflow posters
- QR / community join pages
- screenshots whose explanatory value depends on embedded threshold tables
- charts that visually encode exact capability classes even when text is cropped

## Official-Source Recovery Targets

These are the best next authority-recovery targets if the controller selects `source_recovery_now`:

- `ipc_hole_slot_fabrication_drawing_terminology`
  - recover official or standards-adjacent terminology for plated / non-plated holes and slots
  - goal: support vocabulary and drawing-intent framing, not numeric capability closure
- `ipc_land_pattern_and_pad_design_methodology`
  - recover official pad / land-pattern method sources for pad geometry, symmetry, and assembly-risk framing
  - goal: support method identity and review posture
- `ipc_solder_mask_design_terminology`
  - recover official terminology for mask opening, mask-defined vs non-mask-defined context, and bridge concept vocabulary
  - goal: improve neutral process wording without importing unsupported clearances
- `ipc_or_standards_edge_connector_gold_finger_vocabulary`
  - recover terminology for edge-connector contact regions, finish-region identity, and handling distinctions
  - goal: separate generic gold-finger vocabulary from unsupported process promises
- `ipc_or_industry_guidance_castellated_half_hole_vocabulary`
  - recover neutral terminology for castellated / half-hole structures and board-edge feature identity
  - goal: support taxonomy only unless stronger authority is found
- `official_dfm_data_handoff_guidance`
  - recover official or CAD-vendor primary documentation for fabrication-output checking of holes, slots, and related feature layers
  - goal: support release-check workflow framing without promoting tool-specific claims
- `reliability_or_standard_context_for_feature_spacing`
  - recover official reliability framing for structural weakness, breakout, or spacing-sensitive failure risk
  - goal: upgrade failure-mode wording only; do not assume public exact thresholds will be recoverable

## Route By E3 Subfamily

| E3 subfamily | Route class | Controller posture |
| --- | --- | --- |
| `E3-A` hole and slot taxonomy | `safe_reuse_plus_official_recovery_target` | Reuse vocabulary now; recover stronger terminology source later. |
| `E3-B` hole and slot omission / export failure | `safe_reuse_plus_local_evidence_candidate` | Reuse workflow posture now; preserve neutral failure screenshots if clean. |
| `E3-C` small-hole and small-slot manufacturability risk | `safe_reuse_only_with_blocked_numeric_boundary` | Keep risk framing only; all thresholds blocked. |
| `E3-D` via solder-mask treatment | `safe_reuse_plus_official_recovery_target` | Reuse taxonomy now; recover standards-side terminology for treatment classes. |
| `E3-E` solder-mask opening and bridge control | `safe_reuse_plus_official_recovery_target` | Reuse defect-prevention framing now; recover mask terminology later. |
| `E3-F` pad geometry and pad-mask relationship | `safe_reuse_plus_official_recovery_target` | Reuse mechanism framing now; recover pad / land-pattern method sources later. |
| `E3-G` half-hole and gold-finger edge features | `safe_reuse_plus_local_evidence_candidate_plus_official_recovery_target` | Reuse edge-feature taxonomy now; consider both neutral visuals and terminology recovery. |
| `E3-H` hole-spacing reliability | `safe_reuse_only_with_reliability_recovery_target` | Reuse reliability framing only; exact thresholds remain blocked until official support exists. |
| `E3-I` broken trace / residual-copper feature risk | `safe_reuse_plus_local_evidence_candidate` | Reuse risk family wording now; preserve only neutral failure examples if useful. |

## Status

`hold_map_ready_for_next_controller_decision`

This lane is usage-integrated at controller level only. It is not source-backed and does not unlock reusable numeric or supplier-capability authority.

## Recommended Next Action

Recommended next action: `source_recovery_now`

Reason:

- `E3` exposes several strong terminology targets that are likely recoverable from official or primary-method sources
- the safest immediate value is standards-side vocabulary for holes, slots, pads, solder mask, and edge-connector feature identity
- local evidence remains useful, but should be secondary to terminology recovery because many article visuals are contaminated by branded or threshold-bearing context

If the controller cannot recover acceptable official terminology quickly, downgrade the lane to `local_evidence_now` for neutral diagrams only and keep the rest as blocked hold-map coverage.
