# P4-325 PCB资料 Per-PDF Coverage Index

Date: 2026-05-08
Parent state: `after P4-309 through P4-324`
Execution mode: `deletion_safe_per_pdf_coverage_index`

## Purpose

Provide one deletion-safe index that maps every PDF under `/code/blogs/tmps/PCB资料` to its current `llm_wiki` usage state, controlling lane, and safest in-repo resume surface.

This index is for recovery and subagent dispatch.
It does not claim that every PDF is fully absorbed into `facts/` or `wiki/`.

## Interpretation Rules

- `local_pdf_fact-backed` means the PDF already contributes at least one curated local-PDF fact or direct handbook evidence route.
- `official_fact-backed` means the PDF already has at least one official-source replacement or official-route integration in the same contribution lane.
- `blocked_evidence_only` means the PDF has deletion-safe evidence and/or boundary handling, but no body-ready fact promotion for that PDF surface.
- `claim_family_level_only_with_explicit_hold_reason` means the PDF is lane-covered only as inventory, routing, or hold logic.

For article PDFs, current per-file mapping is still mostly cluster-owned rather than file-specific fact absorption.

## Corpus Totals

- total PDFs: `63`
- handbook PDFs: `4`
- article PDFs: `59`

## Handbook PDFs

| PDF | Current usage state | Current contribution surface | Primary in-repo route |
| --- | --- | --- | --- |
| `【PCB必备】42种-常见PCB封装设计指导规范.pdf` | `official_fact-backed` + `local_pdf_fact-backed` + `blocked_evidence_only` | package / footprint governance, owner-source replacement routing, local package evidence, plus stronger exact-data replacement around residual `1.50 mm` and `0.75 mm` package lanes, one stronger standards-owner square-BGA package-family boundary and one stronger area-array land-pattern family boundary around the still-open `1.50 mm` class, one AMD-hosted third-owner `1.50 mm` exact row, one Intel-hosted fourth-owner `0.75 mm` exact table, and one stronger cross-tool CAD-owner footprint-construction boundary for reference-point and visible/documentation layer-role handling | `logs/p4-291-2026-5-7-pcb-pdf-strong-completion-closeout.md`; `logs/p4-464-2026-5-11-iec-area-array-land-pattern-family-boundary.md`; `logs/p4-487-2026-5-11-iec-square-bga-1mm-or-larger-family-boundary.md`; `logs/p4-479-2026-5-11-amd-third-owner-1p50mm-bga-footprint-row-landing.md`; `logs/p4-481-2026-5-11-intel-fourth-owner-0p75mm-ubga-csp-guidelines-table-landing.md`; `logs/p4-483-2026-5-11-altium-cad-owner-footprint-reference-point-and-layer-boundary.md`; `wiki/processes/package-library-governance-and-footprint-review-map.md`; `facts/local_pdf/pin1-origin-installation-mark-visual-boundary.md`; `pdf_evidence/pcb_ziliao/package/` |
| `【PCB必备】85页-PCB设计EMC设计指导书.pdf` | `official_fact-backed` + `blocked_evidence_only` | EMC method lanes, source-backed method cards, diagram/evidence preservation | `logs/p4-209-2026-5-6-emc-handbook-controller-note.md`; `facts/methods/`; `pdf_evidence/pcb_ziliao/`; `wiki/consumption/lock-emc-fcc-compliance-evidence-pack.md` |
| `【PCB必备】158页-PCBA检验规范汇总.pdf` | `official_fact-backed` + `blocked_evidence_only` | inspection taxonomy, ESD / workmanship method boundaries, defect-photo evidence | `logs/p4-291-2026-5-7-pcb-pdf-strong-completion-closeout.md`; `wiki/testing/pcba-visual-inspection-taxonomy.md`; `wiki/processes/inspection-governance-navigation-map.md`; `pdf_evidence/pcb_ziliao/pcba/` |
| `【PCB必备】194页-PCB设计规范经验之书.pdf` | `claim_family_level_only_with_nine_strengthened_official_routes` | RK3588-scoped bounded lane coverage, plus four owner-backed `D3` routes for remote feedback and quiet sense-point routing, processor power-pin local decoupling capacitor placement, exposed-pad board attach with local thermal spreading plus conditional grounded low-impedance tie, and dedicated plane connection for power pins and decoupling terminals, and five non-overlapping `D5` routes for connector-adjacent ESD entry-path interception, connector-near surface-ground continuity and exposed-zone isolation, clock source-end termination plus crystal-routing EMC review, switch-mode power EMC placement with compact local power-stage and hot-loop control, and differential-pair symmetry plus common-mode-conversion risk, with platform-specific numerics blocked and the current nine-route ceiling now extending beyond broad reread on the same source layer | `logs/p4-282-2026-5-7-rk3588-handbook-lane-split-plan.md`; `logs/p4-282a-2026-5-7-rk3588-handbook-lane-d1-design-flow-and-placement-governance.md`; `logs/p4-282b-2026-5-7-rk3588-handbook-lane-stackup-impedance-and-routing-governance.md`; `logs/p4-282c-2026-5-7-rk3588-handbook-lane-power-delivery-and-grounding-layout.md`; `logs/p4-282d-2026-5-7-rk3588-handbook-lane-interface-and-memory-routing.md`; `logs/p4-282e-2026-5-7-rk3588-handbook-lane-emc-esd-and-dfm-review-boundaries.md`; `logs/p4-402-2026-5-10-d5-connector-adjacent-esd-entry-path-boundary-route.md`; `logs/p4-403-2026-5-10-d5-esd-entry-path-boundary-owner-source-strengthening.md`; `logs/p4-404-2026-5-10-d5-surface-ground-continuity-and-exposed-zone-isolation-boundary.md`; `logs/p4-468-2026-5-11-d3-remote-feedback-and-quiet-sense-point-boundary.md`; `logs/p4-469-2026-5-11-d5-clock-source-termination-and-crystal-routing-emc-boundary.md`; `logs/p4-470-2026-5-11-d5-clock-routing-boundary-successor-sitime-ti-strengthening.md`; `logs/p4-477-2026-5-11-d5-switch-mode-power-emc-placement-and-hot-loop-boundary.md`; `logs/p4-494-2026-5-11-d3-processor-power-pin-local-decoupling-capacitor-placement-boundary.md`; `logs/p4-495-2026-5-11-d3-exposed-pad-ground-tie-and-local-thermal-spreading-boundary.md`; `logs/p4-498-2026-5-11-d3-power-pin-and-decoupling-dedicated-plane-connection-boundary.md`; `logs/p4-501-2026-5-11-d5-differential-pair-symmetry-and-common-mode-conversion-boundary.md`; `logs/p4-502-2026-5-11-194-page-handbook-nine-route-successor-no-write-closeout.md` |

## Article PDFs

### E1 DFM Governance And Persuasion

Status rule for all `E1` PDFs in this index:

- current usage state: `claim_family_level_only_with_explicit_hold_reason`
- six additional `E1` PDFs now have at least one narrow `official_fact-backed` route:
  - `PCB layout有DRC检查为什么还要用DFM.pdf`
  - `全局DFM意识对于PCB设计的重要性.pdf`
  - `对PCB设计师而言，熟练运用DFM已成为必备能力.pdf`
  - `引领工业新思想--DFM的含义将如何演变.pdf`
  - `华秋DFM在硬件制造中的作用.pdf`
  - `大家最关心的制造成本来了！怎么使用DFM降低成本？.pdf`
- primary route: `logs/p4-290-2026-5-7-pcb-article-e1-e7-controller-integration.md`

| PDF | Cluster | Current usage state | Primary in-repo route |
| --- | --- | --- | --- |
| `PCB layout有DRC检查为什么还要用DFM.pdf` | `E1` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-455`; `P4-349`; `P4-290`; `wiki/consumption/pcb-design-for-manufacturing-2-evidence-pack.md`; `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md` |
| `全局DFM意识对于PCB设计的重要性.pdf` | `E1` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-454`; `P4-359`; `P4-290`; `P4-283a`; `P4-356`; `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md`; `wiki/consumption/pcb-design-for-manufacturing-2-evidence-pack.md`; `facts/methods/internal-resource-layer-prompt-support-corpus.md` |
| `对PCB设计师而言，熟练运用DFM已成为必备能力.pdf` | `E1` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-453`; `P4-358`; `P4-290`; `P4-283a`; `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md`; `facts/processes/apt-npi-process-capabilities.md`; `wiki/processes/inspection-governance-navigation-map.md` |
| `引领工业新思想--DFM的含义将如何演变.pdf` | `E1` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-456`; `P4-356`; `P4-290`; `P4-283a`; `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md`; `facts/processes/apt-npi-process-capabilities.md` |
| `华秋DFM在硬件制造中的作用.pdf` | `E1` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-457`; `P4-360`; `P4-290`; `P4-356`; `P4-358`; `P4-359`; `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md`; `facts/methods/pcba-ict-boundary-and-flying-probe-method-identity.md`; `wiki/testing/pcba-quality-gates-and-test-strategy.md` |
| `大家最关心的制造成本来了！怎么使用DFM降低成本？.pdf` | `E1` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-452`; `P4-395`; `P4-290`; `P4-283a`; `facts/methods/pcb-cost-driver-review-and-quote-preparation-boundary.md`; `wiki/processes/pcb-cost-driver-review-and-quote-preparation.md`; `wiki/consumption/pcb-cost-drivers-yield-evidence-pack.md`; `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md` |

### E2 Layout, Routing, Stackup, Layers, And Impedance

Status rule for all `E2` PDFs in this index:

- current usage state: `claim_family_level_only_with_explicit_hold_reason`, except these eight PDFs, which now each have at least one narrow `official_fact-backed` route:
  - `PCB布局布线的可制造性设计.pdf`
  - `印制电路板设计重点.pdf`
  - `一文带你读懂PCB电路板设计中各种层的定义.pdf`
  - `PCB叠层顺序规划配置方案.pdf`
  - `PCB阻抗误差控制在5%，究竟有多难？.pdf`
  - `PCB内层的可制造性设计.pdf`
  - `PCB设计必须考虑的8种安全距离，搞错1种都出大问题！.pdf`
  - `PCB可制造性设计及案例分析之线路篇.pdf`
- controller lane is already `usage_route_integrated_at_controller_level_only`
- primary route: `logs/p4-310-2026-5-8-pcb-article-e2-usage-route-integration.md`

| PDF | Cluster | Current usage state | Primary in-repo route |
| --- | --- | --- | --- |
| `PCB布局布线的可制造性设计.pdf` | `E2` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-429`; `P4-382`; `P4-310`; `P4-283b`; `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md`; `facts/methods/selective-solder-design-access-checks.md`; `facts/methods/depanelization-cleanliness-and-edge-risk-boundary.md`; `facts/methods/ipc-solder-mask-layer-and-pad-definition-boundary.md`; `wiki/processes/mixed-technology-solder-route-selection.md` |
| `印制电路板设计重点.pdf` | `E2` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-427`; `P4-383`; `P4-310`; `P4-283b`; `P4-336`; `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md`; `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`; `facts/methods/ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity.md`; `facts/methods/controlled-impedance-tdr-verification-posture.md`; `facts/methods/current-carrying-trace-width-and-copper-boundary.md`; `wiki/processes/package-library-governance-and-footprint-review-map.md`; `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md` |
| `一文带你读懂PCB电路板设计中各种层的定义.pdf` | `E2` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-414`; `P4-380`; `P4-310`; `facts/methods/layer-role-and-drill-output-annotation-vocabulary-boundary.md`; `facts/local_pdf/padstack-layer-role-visual-boundary.md`; `facts/methods/ipc-solder-mask-layer-and-pad-definition-boundary.md`; `facts/methods/cam-data-exchange-format-boundary.md`; `facts/methods/pcb-design-tool-official-feature-identity-boundary.md`; `wiki/processes/pcb-design-data-exchange-and-tool-boundaries.md`; `wiki/processes/rigid-board-family-and-layer-boundaries.md` |
| `PCB叠层顺序规划配置方案.pdf` | `E2` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-425`; `P4-381`; `P4-350`; `P4-310`; `facts/methods/ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity.md`; `facts/methods/controlled-impedance-tdr-verification-posture.md`; `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`; `wiki/processes/rigid-board-family-and-layer-boundaries.md` |
| `PCB为什么常用50Ω阻抗？6大原因.pdf` | `E2` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-448`; `P4-331`; `P4-310`; `facts/methods/controlled-impedance-tdr-verification-posture.md`; `facts/methods/pcb-impedance-and-rf-measurement-method-boundary.md`; `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`; `wiki/processes/rf-transmission-line-structure-boundaries.md` |
| `PCB阻抗误差控制在5%，究竟有多难？.pdf` | `E2` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-420`; `P4-334`; `P4-310`; `facts/methods/controlled-impedance-tdr-verification-posture.md`; `facts/methods/pcb-impedance-and-rf-measurement-method-boundary.md`; `facts/methods/spread-glass-and-controlled-impedance-planning.md`; `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`; `wiki/testing/rf-validation-and-test-coverage.md` |
| `PCB内层的可制造性设计.pdf` | `E2` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-426`; `P4-350`; `P4-310`; `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`; `facts/methods/ground-and-return-path-boundary-stays-at-reference-plane-and-routing-continuity.md`; `wiki/processes/rigid-board-family-and-layer-boundaries.md` |
| `PCB设计必须考虑的8种安全距离，搞错1种都出大问题！.pdf` | `E2` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-424`; `P4-384`; `P4-310`; `P4-283b`; `P4-382`; `facts/methods/ipc-solder-mask-layer-and-pad-definition-boundary.md`; `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`; `facts/methods/depanelization-cleanliness-and-edge-risk-boundary.md` |
| `PCB可制造性设计及案例分析之线路篇.pdf` | `E2` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-428`; `P4-385`; `P4-310`; `P4-283b`; `P4-382`; `P4-384`; `facts/methods/depanelization-cleanliness-and-edge-risk-boundary.md`; `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`; `facts/methods/ipc-solder-mask-layer-and-pad-definition-boundary.md` |

### E3 Fabrication Features, Pads, Holes, Slots, Vias, Solder Mask, And Edge Features

Status rule for all `E3` PDFs in this index:

- all fourteen `E3` PDFs in this batch now each have at least one narrow `official_fact-backed` route:
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
  - `如何避免“断头线”带来的DFM（可制造性）问题？.pdf`
  - `PCB“金手指”从设计到生产全流程.pdf`
  - `PCB设计孔间距的DFM可靠性.pdf`
  - `PCB邮票孔桥连设计要点，干货满满！.pdf`
- the broader blocked claim classes for each PDF still remain `claim_family_level_only_with_explicit_hold_reason` outside those narrow routes
- controller lane is already `hold_map_ready_for_next_controller_decision`
- one narrow official-source-backed terminology boundary also now exists for the solder-mask subfamily through `P4-363`
- one narrower vendor-scoped owner terminology boundary also now exists for `NSMD/SMD` through `P4-364`, but it does not promote any individual article PDF above its current state
- primary route: `logs/p4-311-2026-5-8-pcb-article-e3-usage-route-integration.md`

| PDF | Cluster | Current usage state | Primary in-repo route |
| --- | --- | --- | --- |
| `PCB可制造性设计及案例分析之孔槽篇.pdf` | `E3` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-437`; `P4-375`; `P4-352`; `P4-419`; `P4-311`; `P4-368`; `facts/methods/cam-data-exchange-format-boundary.md`; `wiki/processes/pcb-design-data-exchange-and-tool-boundaries.md` |
| `器件引脚的方槽、方孔如何避坑？.pdf` | `E3` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-438`; `P4-376`; `P4-437`; `P4-311`; `P4-352`; `P4-368`; `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`; `facts/methods/package-to-footprint-and-pin-count-alignment-review-boundary.md`; `facts/methods/tht-pressfit-terminal-route-boundary.md` |
| `器件引脚小尺寸的孔和槽如何避坑？.pdf` | `E3` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-439`; `P4-377`; `P4-437`; `P4-311`; `P4-352`; `P4-362`; `P4-368`; `facts/methods/cam-data-exchange-format-boundary.md`; `wiki/processes/pcb-design-data-exchange-and-tool-boundaries.md` |
| `PCB板漏孔、漏槽在设计端如何避坑.pdf` | `E3` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-419`; `P4-352`; `P4-311`; `P4-283e3`; `facts/methods/cam-data-exchange-format-boundary.md`; `wiki/processes/pcb-design-data-exchange-and-tool-boundaries.md`; `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`; `pdf_evidence/pcb_ziliao/package/padstack-layer-role-diagram.md`; `pdf_evidence/pcb_ziliao/package/via-padstack-naming-grammar.md` |
| `一招搞定PCB阻焊过孔问题.pdf` | `E3` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-436`; `P4-367`; `P4-311`; `facts/methods/ipc-solder-mask-layer-and-pad-definition-boundary.md`; `facts/methods/cam-data-exchange-format-boundary.md`; `facts/methods/hdi-microvia-and-vippo-process-posture.md`; `P4-344`; `P4-423` |
| `这样做，轻松拿捏阻焊桥！.pdf` | `E3` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-451`; `P4-373`; `P4-311`; `P4-362`; `P4-371`; `facts/methods/ipc-solder-mask-layer-and-pad-definition-boundary.md`; `facts/methods/cam-data-exchange-format-boundary.md`; `wiki/processes/pcb-design-data-exchange-and-tool-boundaries.md` |
| `PCB设计如何防止阻焊漏开窗.pdf` | `E3` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-417`; `P4-362`; `P4-363`; `P4-311`; `P4-352`; `facts/methods/ipc-solder-mask-layer-and-pad-definition-boundary.md`; `facts/methods/cam-data-exchange-format-boundary.md`; `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`; `facts/local_pdf/padstack-layer-role-visual-boundary.md`; `wiki/processes/pcb-design-data-exchange-and-tool-boundaries.md` |
| `PCB焊盘设计之问题详解.pdf` | `E3` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-441`; `P4-369`; `P4-311`; `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`; `facts/methods/package-to-footprint-and-pin-count-alignment-review-boundary.md`; `facts/methods/intel-nsmd-smd-land-pad-terminology-boundary.md` |
| `多层板的焊盘到底应该怎么设计？四种主要设计方式带你搞懂！.pdf` | `E3` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-447`; `P4-371`; `P4-369`; `P4-311`; `facts/methods/ipc-solder-mask-layer-and-pad-definition-boundary.md`; `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`; `facts/methods/intel-nsmd-smd-land-pad-terminology-boundary.md` |
| `千万不能小瞧的PCB半孔板.pdf` | `E3` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-440`; `P4-378`; `P4-366`; `P4-311`; `P4-357`; `P4-361`; `P4-362`; `P4-373`; `facts/methods/stamp-hole-panelization-and-castellated-edge-boundary.md` |
| `如何避免“断头线”带来的DFM（可制造性）问题？.pdf` | `E3` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-449`; `P4-372`; `P4-311`; `facts/methods/cam-data-exchange-format-boundary.md`; `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md`; `wiki/processes/pcb-design-data-exchange-and-tool-boundaries.md`; `wiki/consumption/pcb-design-for-manufacturing-2-evidence-pack.md` |
| `PCB“金手指”从设计到生产全流程.pdf` | `E3` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-435`; `P4-365`; `P4-311`; `facts/standards/edge-contact-gold-finger-standards-metadata-boundary.md`; `facts/methods/finish-zoning-by-assembly-sequence-and-storage-exposure.md`; `wiki/processes/finish-zoning-and-selective-multi-finish.md` |
| `PCB设计孔间距的DFM可靠性.pdf` | `E3` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-418`; `P4-396`; `P4-370`; `P4-311`; `facts/methods/hole-spacing-reliability-boundary.md`; `facts/methods/cam-data-exchange-format-boundary.md`; `wiki/processes/pcb-design-data-exchange-and-tool-boundaries.md` |
| `PCB邮票孔桥连设计要点，干货满满！.pdf` | `E3` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-450`; `P4-397`; `P4-374`; `P4-311`; `P4-361`; `P4-357`; `P4-366`; `facts/methods/stamp-hole-panelization-and-castellated-edge-boundary.md` |

### E4 Panelization, Outline, Edge Clearance, Marking, And Character

Status rule for all `E4` PDFs in this index:

- current usage state: `claim_family_level_only_with_explicit_hold_reason`, except these seven PDFs, which now each have at least one narrow `official_fact-backed` route:
  - `PCB可制造性设计及案例分析之字符、外形、拼板（图文结合，推荐）.pdf`
  - `PCB拼板，不得不注意的10个问题！.pdf`
  - `PCB板各种形状的拼版实例分享.pdf`
  - `PCB字符的DFM（可制造性）设计.pdf`
  - `啥？PCB拼版对SMT组装有影响！.pdf`
  - `元器件到PCB板边缘间距不足的严重性.pdf`
  - `PCBA板边器件布局重要性.pdf`
- one additional single-PDF route is now recorded as `source_backed_route_available_without_new_fact_promotion` and has been re-audited against current stencil/data-vocabulary anchors without gaining clean official promotion:
  - `PCB板的Mark点设计对SMT重要性.pdf`
- controller lane is already `controller_routed_at_usage_level_only`
- primary route: `logs/p4-312-2026-5-8-pcb-article-e4-usage-route-integration.md`

| PDF | Cluster | Current usage state | Primary in-repo route |
| --- | --- | --- | --- |
| `PCB可制造性设计及案例分析之字符、外形、拼板（图文结合，推荐）.pdf` | `E4` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-443`; `P4-379`; `P4-312`; `P4-424`; `P4-354`; `P4-355`; `P4-357`; `P4-361`; `facts/methods/ipc-solder-mask-layer-and-pad-definition-boundary.md`; `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`; `facts/methods/depanelization-cleanliness-and-edge-risk-boundary.md`; `facts/methods/selective-solder-design-access-checks.md` |
| `PCB拼板，不得不注意的10个问题！.pdf` | `E4` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-444`; `P4-361`; `P4-312`; `P4-442`; `facts/methods/depanelization-cleanliness-and-edge-risk-boundary.md`; `facts/methods/selective-solder-design-access-checks.md`; `wiki/processes/compact-closure-and-rework.md`; `logs/p4-421-2026-5-10-e4-board-edge-access-risk-authority-recovery.md`; `logs/p4-434-2026-5-10-e4-board-edge-layout-access-risk-authority-recovery.md` |
| `PCB板各种形状的拼版实例分享.pdf` | `E4` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-445`; `P4-357`; `P4-312`; `P4-440`; `facts/methods/depanelization-cleanliness-and-edge-risk-boundary.md`; `facts/methods/selective-solder-design-access-checks.md`; `wiki/processes/compact-closure-and-rework.md`; `logs/p4-421-2026-5-10-e4-board-edge-access-risk-authority-recovery.md`; `logs/p4-434-2026-5-10-e4-board-edge-layout-access-risk-authority-recovery.md`; `logs/p4-442-2026-5-10-e4-assembly-facing-panel-handling-access-risk-authority-recovery.md`; `logs/p4-444-2026-5-11-e4-panel-handling-and-edge-interference-authority-recovery.md` |
| `啥？PCB拼版对SMT组装有影响！.pdf` | `E4` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-442`; `P4-355`; `P4-312`; `facts/methods/selective-solder-design-access-checks.md`; `facts/methods/depanelization-cleanliness-and-edge-risk-boundary.md`; `wiki/processes/compact-closure-and-rework.md`; `wiki/processes/mixed-technology-solder-route-selection.md`; `logs/p4-421-2026-5-10-e4-board-edge-access-risk-authority-recovery.md`; `logs/p4-434-2026-5-10-e4-board-edge-layout-access-risk-authority-recovery.md` |
| `PCB板的Mark点设计对SMT重要性.pdf` | `E4` | `source_backed_route_available_without_new_fact_promotion` | `P4-460`; `P4-353`; `P4-312`; `P4-283e`; `facts/methods/ipc-stencil-guideline-family-and-upstream-print-control-boundary.md`; `facts/methods/cam-data-exchange-format-boundary.md`; `facts/local_pdf/pin1-origin-installation-mark-visual-boundary.md`; `logs/p4-332-2026-5-9-e5-polarity-reference-designator-route-integration.md` |
| `元器件到PCB板边缘间距不足的严重性.pdf` | `E4` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-421`; `P4-347`; `P4-312`; `facts/methods/selective-solder-design-access-checks.md`; `wiki/processes/compact-closure-and-rework.md`; `wiki/processes/mixed-technology-solder-route-selection.md` |
| `PCBA板边器件布局重要性.pdf` | `E4` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-434`; `P4-348`; `P4-312`; `facts/methods/selective-solder-design-access-checks.md`; `wiki/processes/compact-closure-and-rework.md`; `wiki/processes/mixed-technology-solder-route-selection.md`; `logs/p4-421-2026-5-10-e4-board-edge-access-risk-authority-recovery.md` |
| `PCB字符的DFM（可制造性）设计.pdf` | `E4` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-446`; `P4-354`; `P4-312`; `P4-424`; `P4-443`; `facts/methods/ipc-solder-mask-layer-and-pad-definition-boundary.md`; `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md` |

### E5 Assembly, DFA, Stencil, Soldering, Polarity, And Test

Status rule for all `E5` PDFs in this index:

- current usage state: `claim_family_level_only_with_explicit_hold_reason`, except these ten PDFs, which now each have at least one narrow `official_fact-backed` route:
  - `DFA是什么？这些组装性问题你都知道怎么解决吗？.pdf`
  - `关于PCBA元器件布局的重要性.pdf`
  - `组装电子元器件间距不足的严重性.pdf`
  - `如何避免踩坑钢网.pdf`
  - `你想知道的BGA焊接问题都在这里.pdf`
  - `那些关于DIP器件不得不说的坑.pdf`
  - `元器件虚焊原因之一盘中孔的可制造设计规范.pdf`
  - `PCBA丝印位号与极性符号的组装性设计.pdf`
  - `PCB测试四大方式你都了解吗？内含治具的DFM（可制造性）设计！.pdf`
  - `如何保证电子产品可靠性设计？三方面为您解读，值得收藏！.pdf`
- controller lane is already `controller_routed_at_usage_level_only`
- primary route: `logs/p4-313-2026-5-8-pcb-article-e5-usage-route-integration.md`

| PDF | Cluster | Current usage state | Primary in-repo route |
| --- | --- | --- | --- |
| `DFA是什么？这些组装性问题你都知道怎么解决吗？.pdf` | `E5` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-415`; `P4-345`; `P4-313`; `facts/methods/dfa-assembly-review-and-package-footprint-mismatch-trigger-boundary.md`; `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md`; `facts/methods/package-to-footprint-and-pin-count-alignment-review-boundary.md`; `facts/methods/selective-solder-design-access-checks.md`; `facts/methods/pcba-stencil-selective-solder-and-fine-pitch-controls.md`; `facts/methods/pcba-ict-boundary-and-flying-probe-method-identity.md`; `wiki/processes/package-library-governance-and-footprint-review-map.md`; `wiki/processes/mixed-technology-solder-route-selection.md`; `wiki/processes/compact-closure-and-rework.md`; `wiki/testing/pcba-quality-gates-and-test-strategy.md` |
| `关于PCBA元器件布局的重要性.pdf` | `E5` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-432`; `P4-342`; `P4-313`; `facts/methods/selective-solder-design-access-checks.md`; `facts/methods/pcba-stencil-selective-solder-and-fine-pitch-controls.md`; `wiki/processes/mixed-technology-solder-route-selection.md`; `wiki/processes/compact-closure-and-rework.md`; `wiki/testing/pcba-quality-gates-and-test-strategy.md` |
| `组装电子元器件间距不足的严重性.pdf` | `E5` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-433`; `P4-343`; `P4-313`; `facts/methods/selective-wave-solder-and-mixed-technology-sequencing.md`; `facts/methods/selective-solder-design-access-checks.md`; `facts/methods/parameter-scope-pcba-selective-solder-tht-route-context.md`; `facts/methods/manual-solder-rework-boundary-for-mixed-technology.md`; `facts/methods/pcba-mixed-technology-assembly-flow.md`; `wiki/processes/selective-solder-fixture-and-access-planning.md`; `wiki/processes/hand-solder-touchup-and-rework-control.md`; `wiki/testing/pcba-quality-gates-and-test-strategy.md` |
| `如何避免踩坑钢网.pdf` | `E5` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-411`; `P4-335`; `P4-313`; `facts/methods/ipc-stencil-guideline-family-and-upstream-print-control-boundary.md`; `facts/methods/pcba-stencil-selective-solder-and-fine-pitch-controls.md`; `facts/methods/selective-wave-solder-and-mixed-technology-sequencing.md`; `wiki/processes/mixed-technology-solder-route-selection.md`; `wiki/testing/pcba-quality-gates-and-test-strategy.md` |
| `你想知道的BGA焊接问题都在这里.pdf` | `E5` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-410`; `P4-337`; `P4-313`; `facts/methods/bga-staged-process-review-and-hidden-joint-inspection-boundary.md`; `facts/methods/low-void-bga-dfm-to-process-review.md`; `facts/methods/low-void-bga-reflow-paste-vs-assembly-boundary.md`; `facts/methods/hidden-joint-xray-inspection-boundary.md`; `wiki/processes/low-void-bga-reflow-and-hidden-joint-inspection.md` |
| `那些关于DIP器件不得不说的坑.pdf` | `E5` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-422`; `P4-339`; `P4-313`; `facts/methods/package-to-footprint-and-pin-count-alignment-review-boundary.md`; `facts/methods/selective-wave-solder-and-mixed-technology-sequencing.md`; `facts/methods/parameter-scope-pcba-selective-solder-tht-route-context.md`; `facts/methods/selective-solder-design-access-checks.md`; `wiki/processes/selective-solder-fixture-and-access-planning.md` |
| `元器件虚焊原因之一盘中孔的可制造设计规范.pdf` | `E5` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-423`; `P4-344`; `P4-313`; `facts/methods/hdi-microvia-and-vippo-process-posture.md`; `facts/methods/low-void-bga-dfm-to-process-review.md`; `facts/methods/pcba-stencil-selective-solder-and-fine-pitch-controls.md`; `facts/methods/microchip-csp-bga-solder-land-and-pitch-examples.md`; `facts/methods/low-void-bga-reflow-paste-vs-assembly-boundary.md`; `facts/methods/hidden-joint-xray-inspection-boundary.md`; `wiki/processes/low-void-bga-reflow-and-hidden-joint-inspection.md` |
| `PCBA丝印位号与极性符号的组装性设计.pdf` | `E5` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-412`; `P4-332`; `P4-313`; `facts/methods/pin1-polarity-and-reference-designator-documentation-boundary.md`; `facts/methods/iec-smd-component-marking-boundary.md`; `facts/methods/iec-zero-orientation-cad-library-construction-boundary.md`; `facts/methods/component-orientation-and-polarity-inspection-vocabulary-boundary.md`; `wiki/testing/pcba-visual-inspection-taxonomy.md`; `wiki/processes/package-library-governance-and-footprint-review-map.md` |
| `PCB测试四大方式你都了解吗？内含治具的DFM（可制造性）设计！.pdf` | `E5` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-409`; `P4-330`; `P4-313`; `facts/methods/pcba-ict-boundary-and-flying-probe-method-identity.md`; `facts/methods/pcba-flying-probe-vs-ict-selection-posture.md`; `facts/methods/pcba-ict-fixture-introduction-gate.md`; `wiki/processes/ict-fixture-introduction-and-method-selection.md`; `wiki/processes/inspection-governance-navigation-map.md` |
| `如何保证电子产品可靠性设计？三方面为您解读，值得收藏！.pdf` | `E5` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-462`; `P4-416`; `P4-346`; `P4-313`; `facts/methods/dfa-assembly-review-and-package-footprint-mismatch-trigger-boundary.md`; `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md`; `facts/methods/package-to-footprint-and-pin-count-alignment-review-boundary.md`; `facts/methods/selective-solder-design-access-checks.md`; `wiki/processes/pcba-npi-to-mass-production-flow.md`; `wiki/processes/compact-closure-and-rework.md`; `wiki/processes/mixed-technology-solder-route-selection.md`; `wiki/testing/pcba-quality-gates-and-test-strategy.md`; `logs/p4-345-2026-5-9-e5-dfa-assembly-risk-route-integration.md` |

### E6 Packages, BOM, Procurement-Risk, And Flexible-Circuit Subset

Status rule for all `E6` PDFs in this index:

- current usage state: `claim_family_level_only_with_explicit_hold_reason`, except these six PDFs, which now each have at least one narrow `official_fact-backed` route:
  - `电子元器件封装(Package).pdf`
  - `如何解决bom物料与焊盘不匹配问题.pdf`
  - `BOM查错助力元器件采购.pdf`
  - `如何避免采购电子元器件入坑.pdf`
  - `0Ω电阻在PCB板中的5大常见作用.pdf`
  - `单层双面多层FPC有何区别？.pdf`
- controller lane is already `controller_routed_at_usage_level_only_with_explicit_procurement_hold_split`
- primary route: `logs/p4-314-2026-5-8-pcb-article-e6-usage-route-integration.md`

| PDF | Cluster | Current usage state | Primary in-repo route |
| --- | --- | --- | --- |
| `电子元器件封装(Package).pdf` | `E6` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-408`; `P4-333`; `P4-314`; `facts/methods/package-family-and-footprint-governance-vocabulary-boundary.md`; `facts/methods/package-to-footprint-and-pin-count-alignment-review-boundary.md`; `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`; `wiki/processes/package-library-governance-and-footprint-review-map.md` |
| `如何解决bom物料与焊盘不匹配问题.pdf` | `E6` | `official_fact-backed` | `P4-328`; `facts/methods/package-to-footprint-and-pin-count-alignment-review-boundary.md` |
| `BOM查错助力元器件采购.pdf` | `E6` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-407`; `P4-336`; `P4-314`; `facts/methods/bom-identity-field-separation-manufacturer-part-and-supplier-link-boundary.md`; `facts/methods/pcba-bom-sourcing-and-traceability-posture.md`; `facts/methods/avl-and-alternate-control-posture.md`; `facts/methods/bom-and-hdi-complexity-boundary.md`; `wiki/processes/bom-and-hdi-complexity-boundaries.md`; `wiki/processes/international-pcb-procurement-shipping-boundaries.md` |
| `如何避免采购电子元器件入坑.pdf` | `E6` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-413`; `P4-338`; `P4-314`; `facts/methods/procurement-release-identity-completeness-and-controlled-source-boundary.md`; `facts/methods/bom-identity-field-separation-manufacturer-part-and-supplier-link-boundary.md`; `facts/methods/pcba-bom-sourcing-and-traceability-posture.md`; `facts/methods/avl-and-alternate-control-posture.md`; `facts/standards/high-reliability-traceability-and-counterfeit-control-metadata.md`; `wiki/processes/international-pcb-procurement-shipping-boundaries.md`; `wiki/processes/bom-and-hdi-complexity-boundaries.md` |
| `0Ω电阻在PCB板中的5大常见作用.pdf` | `E6` | `official_fact-backed` | `P4-327`; `facts/methods/zero-ohm-jumper-resistor-identity-boundary.md` |
| `单层双面多层FPC有何区别？.pdf` | `E6` | `official_fact-backed` | `P4-326`; `facts/standards/ipc-flex-printed-board-type-taxonomy-boundary.md`; `wiki/processes/flex-printed-board-type-taxonomy-and-structure-map.md` |

### E7 Manufacturing Data Exchange And Vendor-Tool Workflow

Status rule for all `E7` PDFs in this index:

- current usage state: `claim_family_level_only_with_explicit_hold_reason`, except these two PDFs, which now each have at least one narrow `official_fact-backed` route:
  - `PCB制造文件传输数据的主要格式.pdf`
  - `华秋DFM组装分析前需准备的数据文件.pdf`
- one additional single-PDF route is now recorded as `source_backed_route_available_without_new_fact_promotion`:
  - `简单好用！再也不用担心PCB图形对齐问题.pdf`
- primary route: `logs/p4-290-2026-5-7-pcb-article-e1-e7-controller-integration.md`

| PDF | Cluster | Current usage state | Primary in-repo route |
| --- | --- | --- | --- |
| `PCB制造文件传输数据的主要格式.pdf` | `E7` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-430`; `P4-340`; `P4-290`; `wiki/processes/pcb-design-data-exchange-and-tool-boundaries.md`; `facts/methods/cam-data-exchange-format-boundary.md`; `facts/methods/pcba-test-method-input-package-boundary.md`; `sources/registry/standards/ucamco-gerber-format-page.md`; `sources/registry/standards/siemens-odb-plus-plus-page.md`; `sources/registry/standards/ipc-dpmx-ipc-2581-consortium-home-page.md` |
| `华秋DFM组装分析前需准备的数据文件.pdf` | `E7` | `official_fact-backed` + `source_backed_route_available_without_new_fact_promotion` | `P4-431`; `P4-341`; `P4-290`; `wiki/processes/pcb-design-data-exchange-and-tool-boundaries.md`; `facts/methods/pcba-test-method-input-package-boundary.md`; `facts/methods/package-to-footprint-and-pin-count-alignment-review-boundary.md`; `facts/methods/pcba-bom-sourcing-and-traceability-posture.md`; `facts/methods/cam-data-exchange-format-boundary.md`; `wiki/consumption/assembly-solutions-evidence-pack.md` |
| `简单好用！再也不用担心PCB图形对齐问题.pdf` | `E7` | `source_backed_route_available_without_new_fact_promotion` | `P4-351`; `P4-290`; `logs/p4-283c-2026-5-7-pcb-article-manufacturing-data-exchange-and-vendor-tool-hold-map.md`; `wiki/processes/pcb-design-data-exchange-and-tool-boundaries.md`; `facts/methods/pcba-test-method-input-package-boundary.md`; `facts/methods/cam-data-exchange-format-boundary.md` |
| `华秋DFM可视化BOM交互焊接工具，SMT工厂、PCB工程师的福音来了！.pdf` | `E7` | `claim_family_level_only_with_explicit_hold_reason` | `P4-290` |
| `华秋DFM携带DFA全网重磅上线！新功能极速体验，一睹为快.pdf` | `E7` | `claim_family_level_only_with_explicit_hold_reason` | `P4-290` |
| `华秋干货铺：PCB设计避坑指南（图文结合、视频演示，荐读！）.pdf` | `E7` | `claim_family_level_only_with_explicit_hold_reason` | `P4-290` |

## Current Resume Meaning

This index now makes all `63` PDFs individually discoverable from `llm_wiki` alone.

What it fixes:

- future `/goal` work can assign subagents by exact PDF or exact cluster without rebuilding the inventory
- handbook versus article coverage is now separated at per-file level
- the `194页` handbook is no longer easy to misread as already fact-promoted

What it does not fix:

- it does not broadly convert the article corpus into universal per-file fact closure; many article PDFs now have at least one narrow official-backed or source-backed route, but reusable authority still stays intentionally bounded and sub-surface specific
- it does not close the current non-article residual authority gaps such as public package exact-data generalization or handbook-specific blocked lanes
- it does not promote the current re-audited article residual set beyond its present state: `PCB板的Mark点设计对SMT重要性.pdf` remains route-only, `简单好用！再也不用担心PCB图形对齐问题.pdf` remains route-only, and the three remaining branded-tool `E7` PDFs remain hold-only unless new authority appears

## Recommended Next Action

Use this file as the dispatch index for later `/goal` work.

Priority order after this index:

1. treat `1.50 mm` as materially strengthened to `IEC 60191-6-2 existence + IEC 61188-5-8/6-2 family boundary + NXP exact row + Renesas named-package drawing + Renesas exact row + AMD-hosted BG225/BGG225 third-owner exact row`, not as fully closed; do not reopen it again on the old `IEC metadata`, `Infineon near-hit`, or `ADI false-positive` candidate classes alone, and only reopen it next if a legitimately public official geometry surface or another materially stronger owner-scoped surface clearly exceeds the current ceiling
2. treat `0.75 mm` as materially strengthened to `three Microchip exact rows + one Renesas second-owner exact-data page + one NXP third-owner exact-data page + one Intel-hosted .75mm µBGA CSP fourth-owner exact table`, not as fully closed; do not reopen it again on the old `NXP general guidance`, `IEC metadata`, or same-owner `Renesas` common-pitch candidate classes alone, and only reopen it next if a legitimately public official geometry surface or another materially stronger owner-scoped surface clearly exceeds the current ceiling
3. treat the current doctrine residuals as watch-only rather than active reopen lanes; `P4-475` is the latest negative-result successor showing that current IEC, `KiCad/KLC`, TE, and named-series connector-owner candidate classes still do not clear the doctrine bar
4. treat the current article-side residual set as already re-audited rather than broadly open for more narrow recovery; reopen only if new authority appears for the current `E4 Mark` or `E7` residuals
5. use the exact per-PDF map in this file to avoid re-scanning already closed article residuals
