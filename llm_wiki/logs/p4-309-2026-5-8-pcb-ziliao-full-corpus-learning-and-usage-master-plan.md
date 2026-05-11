# P4-309 PCB资料 Full Corpus Learning And Usage Master Plan

Date: 2026-05-08
Parent state: `after P4-291, P4-308, P4-316, P4-317, and P4-318`
Execution mode: `corpus_master_resume_entry`

## Purpose

Provide one corpus-wide continuation entry for all `63` PDFs under `/code/blogs/tmps/PCB资料`.

This log does not claim that every PDF is fully learned at per-file fact level.
It fixes the current execution truth:

- handbook PDFs are already `strong_complete` at program level, but still carry narrow residual authority gaps
- article PDFs are already cluster-covered, with controller-level `usage route` coverage across `E2-E6` plus narrow single-PDF route expansions in `E1` and `E7`
- future `/goal` work should restart from this file instead of mixing handbook closeout, article cluster inventory, and package residual recovery across multiple old logs

Per-file dispatch index now also exists under:

- `logs/p4-325-2026-5-8-pcb-ziliao-per-pdf-coverage-index.md`

## Corpus Totals

- total PDFs: `63`
- handbook PDFs: `4`
- article PDFs under `PCB文章/`: `59`

## Current Corpus Status

### Handbook Batch

Status: `strong_complete_with_residual_authority_gaps`

Primary controller basis:

- `logs/p4-291-2026-5-7-pcb-pdf-strong-completion-closeout.md`
- `docs/superpowers/plans/2026-05-08-pcb-ziliao-unified-knowledge-layer-plan.md`

Residual authority gaps that remain open:

- package handbook residual `1.50 mm`
- package handbook residual `0.75 mm`
- connector-origin defaulting at universal-rule level
- board-level installation-mark geometry and stronger package-family-specific marking authority

Residual narrowing already landed:

- `0.75 mm` now has one official owner-scoped replacement route through:
- `0.75 mm` now has three official owner-scoped exact rows plus one current-public second-owner exact-data page plus one current-public third-owner exact-data page through:
  - `logs/p4-316-2026-5-8-microchip-0p75mm-tfbga-land-pattern-landing.md`
  - `logs/p4-320-2026-5-8-microchip-second-0p75mm-tfbga-row-landing.md`
  - `logs/p4-324-2026-5-8-microchip-third-0p75mm-tfbga-row-landing.md`
  - `logs/p4-389-2026-5-10-renesas-second-owner-0p75mm-package-land-pattern-boundary.md`
  - `logs/p4-466-2026-5-11-nxp-third-owner-0p75mm-reflow-footprint-landing.md`
  - `facts/methods/microchip-0p75mm-tfbga-land-pattern-4lx.md`
  - `facts/methods/microchip-0p75mm-tfbga-land-pattern-7g.md`
  - `facts/methods/microchip-0p75mm-tfbga-land-pattern-bab.md`
  - `facts/methods/renesas-0p75mm-fbga-package-land-pattern-bcg48d1.md`
  - `facts/methods/nxp-0p75mm-fbga448-reflow-footprint.md`
- `0.75 mm` now also has one current-public fourth-owner exact table through:
  - `logs/p4-481-2026-5-11-intel-fourth-owner-0p75mm-ubga-csp-guidelines-table-landing.md`
  - `facts/methods/intel-0p75mm-ubga-csp-pcb-design-guidelines-table.md`
- this does not close the broader `0.75 mm` pitch class as a universal rule, but it does raise the lane above `three Microchip rows only`
  and above `three Microchip rows plus one geometry-unverified second-owner document`
- `connector-origin` and `installation mark` now have one layered boundary route through:
- `connector-origin` and `installation mark` now have a layered boundary route through:
  - `logs/p4-317-2026-5-8-connector-origin-and-installation-mark-boundary-landing.md`
  - `logs/p4-322-2026-5-8-samtec-connector-owner-layout-route-landing.md`
  - `logs/p4-393-2026-5-10-amphenol-connector-owner-layout-route.md`
  - `facts/methods/connector-origin-and-installation-mark-boundary.md`
- this does not close them as universal cross-vendor rules, but it does add one more current-public owner route with named-side context
- the doctrine lane now also has one stronger cross-tool CAD-owner footprint-construction boundary through:
  - `logs/p4-483-2026-5-11-altium-cad-owner-footprint-reference-point-and-layer-boundary.md`
  - `facts/methods/cad-owner-footprint-reference-point-and-layer-role-boundary.md`
- this raises the CAD-owner side above `KiCad/KLC alone`, but it still does not close universal connector-origin doctrine, mandatory `pin-1` origin, or board-level installation-mark geometry
- `installation mark` now also has one narrower standards-owner zero-orientation route through:
  - `logs/p4-391-2026-5-10-iec-zero-orientation-cad-library-boundary.md`
  - `facts/methods/iec-zero-orientation-cad-library-construction-boundary.md`
- `installation mark / component marking` now also has one public IEC `pin-1` and polarity-identification route through:
  - `logs/p4-392-2026-5-10-iec-smd-component-marking-boundary.md`
  - `facts/methods/iec-smd-component-marking-boundary.md`
- this does not close board-level installation-mark geometry, universal connector-origin doctrine, or package-family-specific marking conventions
- the current `KiCad + Molex/Samtec/Amphenol + IEC + local handbook` set has now also been re-audited through:
  - `logs/p4-463-2026-5-11-package-nonbga-marking-origin-reaudit-and-no-write-closeout.md`
- this re-audit confirms that the clean `visible cue` versus `F.Fab` cue split is already absorbed in the current fact layer, and that this lane should not be reopened on the same source set unless materially stronger authority appears
- the `194页` handbook `D5` lane now also has one official-source-backed narrow route for connector-adjacent ESD placement and short entry-path interception through:
  - `logs/p4-402-2026-5-10-d5-connector-adjacent-esd-entry-path-boundary-route.md`
  - `logs/p4-403-2026-5-10-d5-esd-entry-path-boundary-owner-source-strengthening.md`
  - `facts/methods/connector-adjacent-esd-protection-and-entry-path-boundary.md`
- this does not close the whole `D5` lane, and it does not authorize board-edge distances, TVS geometry defaults, or compliance/pass claims; current best support for this narrow route is now `ST + TI` owner-layout guidance, with the earlier Nexperia source kept as reinforcing entry-point wording
- the `194页` handbook `D5` lane now also has one official-source-backed narrow route for connector-near surface-ground continuity and exposed-zone isolation through:
  - `logs/p4-404-2026-5-10-d5-surface-ground-continuity-and-exposed-zone-isolation-boundary.md`
  - `facts/methods/connector-near-surface-ground-continuity-and-exposed-zone-isolation-boundary.md`
- this still does not authorize board-edge signal distances, exposed-copper geometry defaults, or any exact return-path stitching recipe
- the `194页` handbook `D5` lane now also has one official-source-backed narrow route for clock source-end termination and crystal-routing EMC review through:
  - `logs/p4-469-2026-5-11-d5-clock-source-termination-and-crystal-routing-emc-boundary.md`
  - `facts/methods/clock-source-termination-and-crystal-routing-emc-boundary.md`
- this does not close the whole `D5` lane, and it does not authorize exact resistor values, exact clock lengths, exact spacing rules, or timing / EMC outcome claims
- the preferred current owner support for that `D5 clock` route is now further strengthened through:
  - `logs/p4-470-2026-5-11-d5-clock-routing-boundary-successor-sitime-ti-strengthening.md`
  - `sources/registry/methods/sitime-an10006-best-design-and-layout-practices.md`
- this makes the lane less dependent on a generic processor-board guide alone and more explicitly clock-owner-backed
- the `194页` handbook `D5` lane now also has one official-source-backed narrow route for switch-mode power EMC placement, compact local power-stage layout, and hot-loop minimization through:
  - `logs/p4-477-2026-5-11-d5-switch-mode-power-emc-placement-and-hot-loop-boundary.md`
  - `facts/methods/switch-mode-power-emc-placement-and-hot-loop-boundary.md`
- this does not close the whole `D5` lane, and it does not authorize exact filter values, exact analog or clock keepout distances, exact loop geometry, or EMI / EMC pass claims
- the `194页` handbook `D5` lane now also has one official-source-backed narrow route for differential-pair symmetry, localized balance-through-discontinuity, and common-mode-conversion risk through:
  - `logs/p4-501-2026-5-11-d5-differential-pair-symmetry-and-common-mode-conversion-boundary.md`
  - `facts/methods/differential-pair-symmetry-and-common-mode-conversion-boundary.md`
- this does not close the whole `D5` lane, and it does not authorize universal skew budgets, exact impedance/spacing/via recipes, or SI / jitter / EMI-pass claims
- the `194页` handbook `D3` lane now also has one official-source-backed narrow route for remote feedback and quiet sense-point routing through:
  - `logs/p4-468-2026-5-11-d3-remote-feedback-and-quiet-sense-point-boundary.md`
  - `facts/methods/remote-feedback-and-quiet-sense-point-routing-boundary.md`
- this does not close the whole `D3` lane, and it does not authorize line-width numerics, divider or compensation values, rail-specific recipes, or regulation-performance claims
- the `194页` handbook `D3` lane now also has one second official-source-backed narrow route for processor power-pin local decoupling capacitor placement through:
  - `logs/p4-494-2026-5-11-d3-processor-power-pin-local-decoupling-capacitor-placement-boundary.md`
  - `facts/methods/processor-power-pin-local-decoupling-capacitor-placement-boundary.md`
- this adds one load-side local-decoupling route above role vocabulary alone, but it still does not authorize exact capacitor counts or values, exact via recipes, universal backside doctrine, or any RK3588 rail-specific sufficiency claims
- the `194页` handbook `D3` lane now also has one third official-source-backed narrow route for exposed-pad board attach, local thermal spreading, and conditional grounded low-impedance tie through:
  - `logs/p4-495-2026-5-11-d3-exposed-pad-ground-tie-and-local-thermal-spreading-boundary.md`
  - `facts/methods/exposed-pad-ground-tie-and-local-thermal-spreading-boundary.md`
- this adds one owner-backed exposed-pad package-attach route above claim-family wording alone, but it still does not authorize universal `EPAD = GND`, exact via arrays, exact paste-window rules, or guaranteed thermal / EMI outcomes
- the `194页` handbook `D3` lane now also has one fourth official-source-backed narrow route for dedicated plane entry of power pins, ground pins, and decoupling capacitor terminals through:
  - `logs/p4-498-2026-5-11-d3-power-pin-and-decoupling-dedicated-plane-connection-boundary.md`
  - `facts/methods/power-pin-and-decoupling-dedicated-plane-connection-boundary.md`
- this adds one owner-backed local plane-entry route above placement language alone, but it still does not authorize exact via counts, exact via geometry, universal one-via-per-pin doctrine, or RK3588 rail-specific sufficiency
- the current `194页` handbook state has now also been re-audited through:
  - `logs/p4-502-2026-5-11-194-page-handbook-nine-route-successor-no-write-closeout.md`
- this successor closeout replaces the stale `P4-499` handbook residual wording and records the current safe ceiling more exactly:
  - the earlier successor closeout captured an intermediate route count before the later fifth `D5` raise
  - the current handbook ceiling is now four `D3` routes plus five `D5` routes landed
  - it should not be reopened on the same source set for `remote feedback`, current `local decoupling`, current `exposed pad`, current `dedicated plane connection`, current `D5 clock`, current `switch-mode power`, current `pair-symmetry/common-mode-conversion`, or other synonym-level rewrites of already-landed surfaces
  - future reopen should require materially stronger and non-overlapping authority beyond the current four `D3` routes and current five `D5` routes
- `1.50 mm` now has one standards-owner existence-and-scope route through:
- `1.50 mm` now also has one stronger square-BGA standards-owner package-family route through:
  - `logs/p4-487-2026-5-11-iec-square-bga-1mm-or-larger-family-boundary.md`
  - `facts/methods/iec-square-bga-1mm-or-larger-outline-and-variation-boundary.md`
- this raises the standards-side wording above `IEC 60191-6-2 existence only` and above generic area-array family framing alone, but it still does not expose a public exact `1.50 mm` PCB land-pattern row
- `1.50 mm` now has one current-public named-package exact row through:
  - `logs/p4-390-2026-5-10-nxp-sot648-1-1p50mm-reflow-footprint-landing.md`
  - `facts/methods/nxp-1p50mm-bga225-reflow-footprint.md`
- `1.50 mm` now also has one current-public second-owner named-package drawing through:
  - `logs/p4-398-2026-5-10-renesas-second-owner-1p50mm-bga-package-drawing-boundary.md`
  - `facts/methods/renesas-1p50mm-bga-package-drawing-prbg0225cb-a.md`
- `1.50 mm` now also has one current-public second-owner exact row through:
  - `logs/p4-405-2026-5-10-renesas-second-owner-1p50mm-exact-row-landing.md`
  - `facts/methods/renesas-1p50mm-bga-lga-mount-pad-dimensions-row.md`
- `1.50 mm` still also has one standards-owner existence-and-scope route through:
  - `logs/p4-318-2026-5-8-iec-1p50mm-bga-standards-existence-boundary.md`
  - `facts/methods/bga-1p50mm-pitch-standards-existence-boundary.md`
- `1.50 mm` now also has one stronger standards-owner area-array land-pattern family route through:
  - `logs/p4-464-2026-5-11-iec-area-array-land-pattern-family-boundary.md`
  - `facts/methods/iec-area-array-land-pattern-geometry-family-boundary.md`
- the current `1.50 mm` exact lane has now also been re-audited after that standards-family raise through:
  - `logs/p4-465-2026-5-11-1p50mm-exact-lane-reaudit-after-iec-family-raise.md`
- `1.50 mm` now also has one current-public third-owner exact row through:
  - `logs/p4-479-2026-5-11-amd-third-owner-1p50mm-bga-footprint-row-landing.md`
  - `facts/methods/amd-bg225-bgg225-1p50mm-bga-footprint-row.md`
- this does not close the broader `1.50 mm` pitch class as a universal rule, but it does raise the lane above `one NXP exact row + one Renesas named-package drawing + one Renesas exact row`
  and above `IEC 60191-6-2 existence only`
  and above `IEC 60191-6-2 + IEC 61188-5-8 / 61188-6-2` without the tighter square-BGA package-family boundary

Handbook PDF paths:

- `/code/blogs/tmps/PCB资料/【PCB必备】194页-PCB设计规范经验之书.pdf`
- `/code/blogs/tmps/PCB资料/【PCB必备】85页-PCB设计EMC设计指导书.pdf`
- `/code/blogs/tmps/PCB资料/【PCB必备】158页-PCBA检验规范汇总.pdf`
- `/code/blogs/tmps/PCB资料/【PCB必备】42种-常见PCB封装设计指导规范.pdf`

### Article Batch

Status: `usage_route_covered_at_controller_level_only`

Primary controller basis:

- `logs/p4-283-2026-5-7-pcb-article-cluster-inventory.md`
- `logs/p4-283e3-2026-5-7-pcb-article-e3-claim-family-boundary-map.md`
- `logs/p4-290-2026-5-7-pcb-article-e1-e7-controller-integration.md`
- `logs/p4-310-2026-5-8-pcb-article-e2-usage-route-integration.md`
- `logs/p4-311-2026-5-8-pcb-article-e3-usage-route-integration.md`
- `logs/p4-312-2026-5-8-pcb-article-e4-usage-route-integration.md`
- `logs/p4-313-2026-5-8-pcb-article-e5-usage-route-integration.md`
- `logs/p4-314-2026-5-8-pcb-article-e6-usage-route-integration.md`

Interpretation:

- the article corpus already has controller-owned claim-family coverage
- the article corpus now has bounded `usage route` surfaces for `E2-E6`, plus limited single-PDF route expansion in `E1` and `E7`
- `E1` and `E7` remain non-fact-promoted lanes, but now each has limited single-PDF route expansion above pure hold-map coverage
- `E6` now also includes one narrow official-fact raise above route-only status for `BOM查错助力元器件采购.pdf`:
  - `logs/p4-407-2026-5-10-e6-bom-identity-field-separation-authority-recovery.md`
  - `facts/methods/bom-identity-field-separation-manufacturer-part-and-supplier-link-boundary.md`
  - `sources/registry/methods/altium-activebom-managing-solutions-manufacturer-supplier-identity.md`
  - `sources/registry/methods/altium-activebom-manufacturer-link-fields-dialog.md`
  - `sources/registry/methods/altium-365-bom-portal-identity-and-sourcing-columns.md`
- this raises one `E6` PDF beyond `single-PDF route only` into one narrow official boundary for manufacturer identity, manufacturer part number, and supplier-facing link separation
- `E6` now also includes one narrow official-fact raise above route-only status for `电子元器件封装(Package).pdf`:
  - `logs/p4-408-2026-5-10-e6-package-identity-grammar-authority-recovery.md`
  - `sources/registry/methods/infineon-package-family-and-package-detail-identity-grammar.md`
  - `sources/registry/methods/kicad-library-conventions-package-family-and-footprint-naming.md`
  - strengthened `facts/methods/package-family-and-footprint-governance-vocabulary-boundary.md`
- this raises one more `E6` PDF beyond `single-PDF route only` into one narrow official boundary for package family label, pin-count, variant, and owner-scoped legacy-alias identity grammar
- `E5` now also includes one narrow official-fact raise above route-only status for `PCB测试四大方式你都了解吗？内含治具的DFM（可制造性）设计！.pdf`:
  - `logs/p4-409-2026-5-10-e5-test-method-and-ict-fixture-authority-recovery.md`
  - strengthened `facts/methods/pcba-ict-fixture-introduction-gate.md`
  - strengthened `wiki/processes/ict-fixture-introduction-and-method-selection.md`
  - existing official anchors `sources/registry/standards/keysight-in-circuit-test-systems-page.md` and `sources/registry/standards/seica-flying-probe-page.md`
- this raises one `E5` PDF beyond `single-PDF route only` into one narrow official boundary for fixture-based versus fixture-free test-method identity and ICT fixture-introduction readiness
- `E5` now also includes one narrow official-fact raise above route-only status for `你想知道的BGA焊接问题都在这里.pdf`:
  - `logs/p4-410-2026-5-10-e5-bga-process-and-hidden-joint-authority-recovery.md`
  - `facts/methods/bga-staged-process-review-and-hidden-joint-inspection-boundary.md`
  - existing `facts/methods/low-void-bga-dfm-to-process-review.md`
  - existing `facts/methods/low-void-bga-reflow-paste-vs-assembly-boundary.md`
  - existing `facts/methods/hidden-joint-xray-inspection-boundary.md`
  - existing public anchors `sources/registry/methods/indium-reflow-profile-to-paste-spec.md`, `sources/registry/methods/kester-standard-reflow-profile.md`, `sources/registry/methods/nasa-pcb-inspection-and-quality-control-2022-page.md`, `sources/registry/standards/ipc-a-610h-toc.md`, and `sources/registry/standards/ipc-j-std-001j-toc.md`
- this raises one more `E5` PDF beyond `single-PDF route only` into one narrow official boundary for staged BGA process review, paste-dependent reflow framing, and hidden-joint inspection visibility
- `E5` now also includes one narrow official-fact raise above route-only status for `如何避免踩坑钢网.pdf`:
  - `logs/p4-411-2026-5-10-e5-stencil-guideline-family-authority-recovery.md`
  - `sources/registry/standards/ipc-7525c-toc.md`
  - `facts/methods/ipc-stencil-guideline-family-and-upstream-print-control-boundary.md`
  - existing `facts/methods/pcba-stencil-selective-solder-and-fine-pitch-controls.md`
  - existing `facts/methods/selective-wave-solder-and-mixed-technology-sequencing.md`
- this raises one more `E5` PDF beyond `single-PDF route only` into one narrow official boundary for stencil-guideline family scope, solder-paste layer identity, and upstream print-control framing
- `E5` now also includes one narrow official-fact raise above route-only status for `PCBA丝印位号与极性符号的组装性设计.pdf`:
  - `logs/p4-412-2026-5-10-e5-pin1-polarity-and-designator-authority-recovery.md`
  - `facts/methods/pin1-polarity-and-reference-designator-documentation-boundary.md`
  - existing `facts/methods/iec-smd-component-marking-boundary.md`
  - existing `facts/methods/iec-zero-orientation-cad-library-construction-boundary.md`
  - existing `facts/methods/component-orientation-and-polarity-inspection-vocabulary-boundary.md`
- this raises one more `E5` PDF beyond `single-PDF route only` into one narrow official boundary for `pin-1`, polarity, and reference-designator documentation governance
- `E3` now also includes one narrow official-fact raise above route-only status for `PCB设计如何防止阻焊漏开窗.pdf`:
  - `logs/p4-417-2026-5-10-e3-solder-mask-opening-authority-recovery.md`
  - existing `facts/methods/ipc-solder-mask-layer-and-pad-definition-boundary.md`
  - existing `facts/methods/cam-data-exchange-format-boundary.md`
  - existing `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`
- this raises one `E3` PDF beyond `single-PDF route only` into one narrow official boundary for solder-mask openings as released manufacturing data and missing-opening completeness review
- `E3` now also includes one narrow official-fact raise above route-only status for `PCB设计孔间距的DFM可靠性.pdf`:
  - `logs/p4-418-2026-5-10-e3-hole-spacing-authority-recovery.md`
  - existing `facts/methods/hole-spacing-reliability-boundary.md`
  - existing `facts/methods/cam-data-exchange-format-boundary.md`
- this raises one more `E3` PDF beyond `single-PDF route only` into one narrow official boundary for hole-spacing as a standards-adjacent reliability-review topic
- `E3` now also includes one narrow official-fact raise above route-only status for `PCB板漏孔、漏槽在设计端如何避坑.pdf`:
  - `logs/p4-419-2026-5-10-e3-hole-slot-output-completeness-authority-recovery.md`
  - existing `facts/methods/cam-data-exchange-format-boundary.md`
  - existing `facts/methods/padstack-origin-pin1-and-footprint-review-governance-boundary.md`
  - existing `wiki/processes/pcb-design-data-exchange-and-tool-boundaries.md`
- this raises one more `E3` PDF beyond `single-PDF route only` into one narrow official boundary for released fabrication-package completeness, omitted hole/slot review, and guarded feature-definition failure posture
- `E3` now also includes one narrow official-fact raise above route-only status for `PCB“金手指”从设计到生产全流程.pdf`:
  - `logs/p4-435-2026-5-10-e3-gold-finger-edge-contact-identity-authority-recovery.md`
  - existing `facts/standards/edge-contact-gold-finger-standards-metadata-boundary.md`
  - existing `facts/methods/finish-zoning-by-assembly-sequence-and-storage-exposure.md`
  - existing `wiki/processes/finish-zoning-and-selective-multi-finish.md`
- this raises one more `E3` PDF beyond `single-PDF route only` into one narrow official boundary for `gold finger` as edge-contact-region identity, edge-contact region as distinct from ordinary solderable pad zones, and finish zoning as guarded review posture
- `E2` now also includes one narrow official-fact raise above route-only status for `PCB阻抗误差控制在5%，究竟有多难？.pdf`:
  - `logs/p4-420-2026-5-10-e2-impedance-planning-and-measurement-boundary-authority-recovery.md`
  - existing `facts/methods/controlled-impedance-tdr-verification-posture.md`
  - existing `facts/methods/pcb-impedance-and-rf-measurement-method-boundary.md`
  - existing `facts/methods/spread-glass-and-controlled-impedance-planning.md`
  - existing `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`
  - existing `wiki/testing/rf-validation-and-test-coverage.md`
- this raises one more `E2` PDF beyond `single-PDF route only` into one narrow official boundary for controlled-impedance planning, spread-glass uncertainty, and measurement-boundary separation
- `E2` now also includes one narrow official-fact raise above route-only status for `PCB为什么常用50Ω阻抗？6大原因.pdf`:
  - `logs/p4-448-2026-5-11-e2-50ohm-impedance-boundary-authority-recovery.md`
  - existing `facts/methods/controlled-impedance-tdr-verification-posture.md`
  - existing `facts/methods/pcb-impedance-and-rf-measurement-method-boundary.md`
  - existing `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`
  - existing `wiki/processes/rf-transmission-line-structure-boundaries.md`
- this raises one more `E2` PDF beyond `single-PDF route only` into one narrow official boundary for `50 ohm` as a controlled-impedance planning label, stackup-aware context, and measurement-boundary topic
- `E7` now also includes one narrow official-fact raise above route-only status for `PCB制造文件传输数据的主要格式.pdf`:
  - `logs/p4-430-2026-5-10-e7-handoff-format-identity-authority-recovery.md`
  - existing `facts/methods/cam-data-exchange-format-boundary.md`
  - existing `facts/methods/pcba-test-method-input-package-boundary.md`
- this raises one `E7` PDF beyond `single-PDF route only` into one narrow official boundary for native PCB authoring file versus released manufacturing-handoff package identity, Gerber / `ODB++` as fabrication-handoff exchange-format identity, and the guarded boundary that fabrication-oriented outputs do not by themselves settle the full downstream assembly or test package
- direct promotion remains blocked by default for article numerics, vendor rule tables, workflow screenshots, capability claims, yield claims, and acceptance thresholds

## Article Cluster Map

### `E1` DFM Governance And Persuasion

Current status: `controller_hold_lane_with_single_pdf_route_expansion`

PDF paths:

- `/code/blogs/tmps/PCB资料/PCB文章/PCB layout有DRC检查为什么还要用DFM.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/全局DFM意识对于PCB设计的重要性.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/对PCB设计师而言，熟练运用DFM已成为必备能力.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/引领工业新思想--DFM的含义将如何演变.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/华秋DFM在硬件制造中的作用.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/大家最关心的制造成本来了！怎么使用DFM降低成本？.pdf`

Narrow follow-up already landed:

- `logs/p4-349-2026-5-9-e1-drc-vs-dfm-review-boundary-route-integration.md`
- `logs/p4-356-2026-5-9-e1-dfm-concurrent-engineering-route-integration.md`
- `logs/p4-358-2026-5-9-e1-dfm-governance-loop-route-integration.md`
- `logs/p4-359-2026-5-9-e1-global-dfm-awareness-route-integration.md`
- `logs/p4-360-2026-5-9-e1-dfm-manufacturing-stage-linking-route-integration.md`
- `logs/p4-395-2026-5-10-e1-dfm-cost-driver-route-integration.md`

Interpretation:

- this does not make the whole `E1` lane fact-promoted
- it raises six single PDFs above pure cluster inventory:
  - `PCB layout有DRC检查为什么还要用DFM.pdf` now has a bounded route into `DRC` versus `DFM` as separate review layers, `DFM` as staged manufacturability / assembly review posture, cross-functional review language, and the guarded boundary that manufacturability findings are not always identical to online-layout-rule violations
  - `PCB layout有DRC检查为什么还要用DFM.pdf` now also has one narrow official-fact boundary for `DRC` versus `DFM` stage-boundary posture:
    - `DRC` may be reused only as layout-stage rule-correctness checking against preset constraints
    - `DFM` may be reused only as a separate staged manufacturability / assembly review posture before release
    - this still does not unlock exact `DRC` numeric examples, comparison-table rows, standards lists, software sufficiency, or cost / reliability outcomes
  - `引领工业新思想--DFM的含义将如何演变.pdf` now has a bounded route into `DFM` as upstream concurrent-engineering posture, manufacturability feedback before release handoff, `DFM` inside broader `DFX` / `NPI` review vocabulary, and bare-board versus assembly-facing `DFM` branch split only
  - `引领工业新思想--DFM的含义将如何演变.pdf` now also has one narrow official-fact boundary for `DFM` upstream concurrent-engineering and pre-release feedback posture:
    - `DFM` may be reused only as an upstream concurrent-engineering review posture
    - manufacturability feedback may be reused only as being returned into design before fabrication or assembly release handoff
    - this still does not unlock outcome claims, software sufficiency, named-company adoption, or universal `DFX` taxonomy closure
  - `对PCB设计师而言，熟练运用DFM已成为必备能力.pdf` now has a bounded route into `DFM` specification maintenance, checklist-as-planning-tool, issue-report governance, sample-validation feedback loop, and summary-review posture only
  - `对PCB设计师而言，熟练运用DFM已成为必备能力.pdf` now also has one narrow official-fact boundary for `DFM` governance-artifact and feedback-loop posture:
    - `DFM specification` may be reused only as a maintained governance artifact
    - `DFM checklist` may be reused only as a design-planning and review-routing tool
    - `DFM report` may be reused only as a running issue and correction record
    - sample validation and feedback may be reused only as a before-release governance-loop posture
  - `全局DFM意识对于PCB设计的重要性.pdf` now has a bounded route into design rules and constraints aligned to selected build context, manufacturing awareness before layout freeze, constraint maintenance and design-target clarity as `DFM` posture, and cross-functional governance language only
  - `全局DFM意识对于PCB设计的重要性.pdf` now also has one narrow official-fact boundary for `DFM` early manufacturing-awareness and selected-build-context alignment posture:
    - `DFM` may be reused only as an early manufacturing-awareness review posture before layout freeze or release handoff
    - design rules, constraints, and build assumptions may be reused only as needing alignment with the selected build context
    - this still does not unlock supplier capability proof, real-time BOM or alternate claims, ecosystem workflow claims, software sufficiency, or cost / schedule / profit outcomes
  - `华秋DFM在硬件制造中的作用.pdf` now has a bounded route into `DFM` as broader than layout-only checking, fabrication readiness before release handoff, assembly readiness before downstream build, `test-point planning`, and later test-stage preparation as review-stage vocabulary only
  - `华秋DFM在硬件制造中的作用.pdf` now also has one narrow official-fact boundary for broader-than-layout stage-linking review posture:
    - `DFM` may be reused only as broader than layout-only checking
    - fabrication readiness, assembly readiness, and test-preparation planning may be reused only as pre-release review surfaces before downstream handoff
    - this still does not unlock software-capability, procurement-automation, process-recipe, test-completeness, or cost / yield / reliability outcome claims
  - `大家最关心的制造成本来了！怎么使用DFM降低成本？.pdf` now has a bounded route into cost-driver categories as quote-preparation review surfaces, `DFM` before quote handoff for cost-impacting ambiguity reduction, fabrication/assembly/test burden as engineering-input classes, and material / finish / stackup / process-family complexity as project-specific cost context only
  - `大家最关心的制造成本来了！怎么使用DFM降低成本？.pdf` now also has one narrow official-fact boundary for `DFM before quote` and cost-ambiguity review posture:
    - `DFM` before quote or release handoff may be reused as a cost-ambiguity review gate
    - fabrication complexity, assembly burden, test burden, and BOM readiness may be reused only as quote-preparation review surfaces
    - material, finish, stackup, and process-family complexity may be reused only as project-specific engineering-input context
    - this still does not unlock price tables, cost formulas, savings math, or business-outcome claims
- it still does not unlock comparison-table rows, rule-count claims, standards-list authority, exact `DRC` numeric examples, universal `DFX` taxonomy closure, exact checklist rows, `ISO` equivalence, real-time BOM and alternate claims, sourcing guarantees, branded workflow sufficiency, executable process instructions, or cost / reliability outcome claims

### `E2` Layout, Routing, Stackup, Layers, And Impedance

Current status: `usage_route_integrated_at_controller_level_only`

PDF paths:

- `/code/blogs/tmps/PCB资料/PCB文章/PCB布局布线的可制造性设计.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/印制电路板设计重点.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/一文带你读懂PCB电路板设计中各种层的定义.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/PCB叠层顺序规划配置方案.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/PCB为什么常用50Ω阻抗？6大原因.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/PCB阻抗误差控制在5%，究竟有多难？.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/PCB内层的可制造性设计.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/PCB设计必须考虑的8种安全距离，搞错1种都出大问题！.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/PCB可制造性设计及案例分析之线路篇.pdf`

Narrow follow-up already landed:

- `logs/p4-385-2026-5-9-e2-copper-balance-and-routing-expression-route-integration.md`
- `logs/p4-384-2026-5-9-e2-safety-distance-taxonomy-and-spacing-boundary-route-integration.md`
- `logs/p4-383-2026-5-9-e2-design-priority-and-layout-governance-route-integration.md`
- `logs/p4-382-2026-5-9-e2-layout-routing-manufacturability-route-integration.md`
- `logs/p4-381-2026-5-9-e2-stackup-planning-and-reference-plane-route-integration.md`
- `logs/p4-380-2026-5-9-e2-layer-definition-grammar-and-drill-annotation-route-integration.md`
- `logs/p4-331-2026-5-9-e2-50ohm-impedance-route-integration.md`
- `logs/p4-334-2026-5-9-e2-impedance-tolerance-difficulty-route-integration.md`
- `logs/p4-350-2026-5-9-e2-inner-layer-manufacturability-route-integration.md`

Interpretation:

- this does not make the whole `E2` lane fact-promoted
- it raises nine single PDFs above pure cluster inventory:
  - `PCB可制造性设计及案例分析之线路篇.pdf` now has a bounded route into fill-line versus solid-copper expression boundary, dense/sparse routing and copper-balance as manufacturability risk families, thin residual copper and isolated copper as fabrication-risk families, special pad effective area as a review surface, board-edge copper and milling-path conflict review, panel-level copper-balance difference as a review trigger, and outer-layer bare-copper band as a release-expression boundary only
  - `PCB可制造性设计及案例分析之线路篇.pdf` now also has one narrow official-fact boundary for board-edge copper and milling-path conflict review:
    - board-edge nets, copper, and milling paths may be reused as edge-conflict and release-review topics
    - edge-near conductive features may be reused as needing review against profiling intent before release
    - outer-layer decorative or exposed copper bands may be reused as release-expression objects that should stay unambiguous relative to profiling or program intent
    - this still does not unlock milling or edge-clearance numerics, profiling-program defaults, `BGA` pad-style preference claims, decorative-copper implementation recipes, or tool/capability claims
  - `PCB设计必须考虑的8种安全距离，搞错1种都出大问题！.pdf` now has a bounded route into electrical versus non-electrical spacing taxonomy, traces/pads/vias/board-edge/components as distinct spacing review surfaces, spacing as a manufacturability/reliability/assembly-risk topic family, copper-to-edge as edge-risk review, silkscreen-to-pad overlap as manufacturing-data conflict, and mechanical 3D clearance as fit-review surface only
  - `PCB设计必须考虑的8种安全距离，搞错1种都出大问题！.pdf` now also has one narrow official-fact boundary for silkscreen-pad conflict posture:
    - silkscreen and solderable pad overlap may be reused as a released-manufacturing-data conflict topic
    - this conflict may be reused as a footprint-release and fabrication-output review surface before release
    - this still does not unlock spacing numerics, voltage-conditioned clearance rules, CAD menu authority, or supplier-capability claims
  - `印制电路板设计重点.pdf` now has a bounded route into pre-layout input readiness as a DFM intake gate, library/footprint governance before layout release, layout priority and functional partitioning as qualitative posture, decoupling and power-grouping planning surfaces, routing priority with return-path continuity boundary, adjacent-layer direction control as crosstalk-risk posture, and impedance-layer/reference-layer selection with validation posture only
  - `印制电路板设计重点.pdf` now also has one narrow official-fact boundary for reference-plane continuity and return-path routing discipline:
    - routing priorities, loop-area awareness, split-plane caution, and return-path continuity may be written as execution-boundary language
    - reference-plane continuity and return-path quality may be reused as routing-planning concerns
    - high-speed signals may be reused as needing caution near split power-reference regions because return-path continuity can degrade
    - this still does not unlock spacing numerics, `3W/10W/20H` rules, exact current/via tables, exact impedance geometry/tolerance rules, or tool/capability claims
  - `PCB布局布线的可制造性设计.pdf` now has a bounded route into layout/routing DFM as an early review gate, routing path complexity as a manufacturability review surface, dense SMT neighborhoods as assembly-risk context, mixed SMT/THT population as solder-route selection context, board-edge/profile zones as release-review surfaces, and tall/short component neighborhoods as access/heating/rework risk surfaces only
  - `PCB布局布线的可制造性设计.pdf` now also has one narrow official-fact boundary for board-edge profiling and release-review:
    - board-edge components, pads, and conductive features may be reused as a profiling and release-review topic
    - edge-near conductive features may be reused as needing review against rail handling, profiling intent, and post-separation damage risk before release
    - process rails or panel-edge accommodations may be reused as routing-enablement context, not as permission to ignore edge-risk review
    - this still does not unlock board-edge spacing numerics, machine-rail compatibility certainty, profiling allowance or rail-width recipes, route-superiority claims, or cost/yield/cycle outcomes
  - `PCB叠层顺序规划配置方案.pdf` now has a bounded route into stackup planning as a multivariable tradeoff, signal / power / ground as distinct layer-role families, reference-plane continuity and return-path planning, decoupling short-path awareness as a placement-and-access posture, split-power-plane caution for nearby high-speed routing, and controlled-impedance planning/validation posture only
  - `PCB叠层顺序规划配置方案.pdf` now also has one narrow official-fact boundary for reference-plane continuity and return-path routing discipline:
    - reference-plane continuity and return-path quality may be reused as routing-planning concerns
    - high-speed signals may be reused as needing caution near split power-reference regions because return-path continuity can degrade
    - this still does not unlock exact layer-count or thickness rules, exact stackup recipes, decoupling or EMI outcomes, impedance geometry or tolerance claims, `HDI` / laser-drill capability closure, or supplier/manufacturer capability claims
  - `一文带你读懂PCB电路板设计中各种层的定义.pdf` now has a bounded route into layer-role vocabulary as design-intent grammar, top / bottom / multilayer as board-family identity wording, drillguide / drilldrawing / `Drl` / `NPTH` as output-annotation vocabulary, blind / buried layer-pair names as released-output examples only, and design-tool naming versus manufacturing-data boundary
  - `一文带你读懂PCB电路板设计中各种层的定义.pdf` now also has one narrow official-fact boundary for layer-role and released-output annotation vocabulary:
    - top / bottom / multilayer may be reused as board-family or layer-role identity wording
    - solder mask, legend, and drill may be reused as released manufacturing-data layer families
    - `Drillguide`, `Drilldrawing`, `Drl`, `NPTH`, and blind / buried layer-pair names may be reused only as output-annotation examples
    - this still does not unlock hole-size, stackup, drill-depth, keepout, capability, or manufacturability claims
  - `PCB为什么常用50Ω阻抗？6大原因.pdf` now has a bounded route into controlled-impedance planning, stackup context, RF structure naming, and measurement-method boundary surfaces
  - `PCB为什么常用50Ω阻抗？6大原因.pdf` now also has one narrow official-fact boundary for controlled-impedance planning and measurement-boundary posture:
    - `50 ohm` may be reused only as a common label inside controlled-impedance discussion
    - controlled impedance may be reused as a stackup-aware planning topic rather than a free-floating rationale
    - measurement-method identity may be reused only as a separate layer from supplier-capability, compatibility, and cost claims
    - this still does not unlock historical-origin proof, geometry recipes, manufacturability proof, compatibility doctrine, or cost claims
  - `PCB阻抗误差控制在5%，究竟有多难？.pdf` now has a bounded route into impedance-difficulty planning, spread-glass uncertainty, stackup / material / validation linkage, and RF validation boundary surfaces
  - `PCB阻抗误差控制在5%，究竟有多难？.pdf` now also has one narrow official-fact boundary for controlled-impedance planning and measurement-boundary separation:
    - controlled impedance may be reused as a multivariable stackup/material/lamination/verification planning topic
    - spread-glass or fiber-weave variation may be reused as a qualitative uncertainty class only
    - measurement-method identity may be reused only as a separate layer from tolerance promise and supplier-capability claims
    - this still does not unlock tolerance percentages, exact geometry, quantified solder-mask impact, coupon coverage, or supplier-capability claims
  - `PCB内层的可制造性设计.pdf` now has a bounded route into inner-layer power / ground / reference-plane taxonomy, return-path and split-plane continuity caution, stackup-organization framing, and multilayer-branch planning surfaces
  - `PCB内层的可制造性设计.pdf` now also has one narrow official-fact boundary for reference-plane selection and split-plane crossing caution:
    - reference-plane choice belongs to return-path and shielding-aware planning
    - ground-plane preference may be kept only as qualitative reference-plane posture
    - key-signal routing across plane splits can be kept as a return-path discontinuity caution class
    - this still does not unlock plane-size or offset numerics, exact stackup-order or coupling recipes, dense-BGA geometry claims, current-bottleneck certainty, or tool/capability claims
- it still does not unlock `50 ohm` history closure, drill or stackup numerics, exact layer-count or thickness rules, exact component-spacing or line/space/via thresholds, spacing minimum tables or voltage-conditioned clearance claims, `3W/10W/20H` formula claims, exact copper-balance/routing-expression widths or BGA pad-style preference claims, `HDI` / laser-drill capability closure, keepout-rule authority, supplier capability, manufacturability, compatibility, or cost claims

### `E3` Fabrication Features, Pads, Holes, Slots, Vias, Solder Mask, And Edge Features

Current status: `usage_route_integrated_at_controller_level_only`

PDF paths:

- `/code/blogs/tmps/PCB资料/PCB文章/PCB可制造性设计及案例分析之孔槽篇.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/器件引脚的方槽、方孔如何避坑？.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/器件引脚小尺寸的孔和槽如何避坑？.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/PCB板漏孔、漏槽在设计端如何避坑.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/一招搞定PCB阻焊过孔问题.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/这样做，轻松拿捏阻焊桥！.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/PCB设计如何防止阻焊漏开窗.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/PCB焊盘设计之问题详解.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/多层板的焊盘到底应该怎么设计？四种主要设计方式带你搞懂！.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/千万不能小瞧的PCB半孔板.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/PCB“金手指”从设计到生产全流程.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/如何避免“断头线”带来的DFM（可制造性）问题？.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/PCB设计孔间距的DFM可靠性.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/PCB邮票孔桥连设计要点，干货满满！.pdf`

Narrow follow-up already landed:

- `logs/p4-378-2026-5-9-e3-half-hole-edge-feature-and-panelization-route-integration.md`
- `logs/p4-375-2026-5-9-e3-hole-slot-fabrication-intent-and-output-completeness-route-integration.md`
- `logs/p4-376-2026-5-9-e3-square-lead-special-hole-intent-release-check-route-integration.md`
- `logs/p4-377-2026-5-9-e3-small-hole-slot-feature-typing-opening-risk-route-integration.md`
- `logs/p4-352-2026-5-9-e3-hole-slot-output-completeness-route-integration.md`
- `logs/p4-362-2026-5-9-e3-solder-mask-opening-completeness-route-integration.md`
- `logs/p4-365-2026-5-9-e3-gold-finger-edge-contact-boundary-integration.md`
- `logs/p4-367-2026-5-9-e3-via-solder-mask-treatment-route-integration.md`
- `logs/p4-369-2026-5-9-e3-pad-geometry-and-pad-mask-review-route-integration.md`
- `logs/p4-371-2026-5-9-e3-multilayer-pad-mask-relationship-route-integration.md`
- `logs/p4-372-2026-5-9-e3-broken-trace-residual-copper-route-integration.md`
- `logs/p4-373-2026-5-9-e3-solder-mask-bridge-preservation-route-integration.md`
- `logs/p4-417-2026-5-10-e3-solder-mask-opening-authority-recovery.md`
- `logs/p4-418-2026-5-10-e3-hole-spacing-authority-recovery.md`
- `logs/p4-419-2026-5-10-e3-hole-slot-output-completeness-authority-recovery.md`

Interpretation:

- this does not make the whole `E3` lane fact-promoted
- it raises fourteen single PDFs above pure cluster inventory:
  - `千万不能小瞧的PCB半孔板.pdf` now has a bounded route into half-hole as a special board-edge feature family, half-hole board as a special panelization subfamily, ordinary-board panelization assumptions as potentially unsafe around half-hole edges, and opening / bridge expression as release-check surfaces only
  - `千万不能小瞧的PCB半孔板.pdf` now also has one narrow official-fact boundary for half-hole special edge-feature review posture:
    - `half-hole` may be reused as special board-edge feature review vocabulary
    - half-hole board may be reused as a special panelization subfamily where ordinary-board assumptions should not be silently carried over
    - opening or bridge expression near half-hole edge regions may be reused only as release-check surfaces
    - panel-branch selection around half-hole edge regions may be reused only as explicit special-review context
  - `PCB邮票孔桥连设计要点，干货满满！.pdf` now has a bounded route into `stamp-hole / mouse-bite` as panel-connection branch vocabulary, `V-cut` as a separate panelization branch identity, explicit special breakaway / slot branch handling, and `castellated / half-hole` edge region as special review context only
  - `PCB可制造性设计及案例分析之孔槽篇.pdf` now has a bounded route into hole / slot features as fabrication-intent objects, omitted or misexpressed holes / slots as handoff-risk families, hole-table or slot-annotation support as release-check surfaces, conflicting hole-slot intent at one location as design-intent-loss risk, and pre-release `DFM/CAM` review as timing only
  - `PCB可制造性设计及案例分析之孔槽篇.pdf` now also has one narrow official-fact boundary for hole-slot released-output completeness review posture:
    - intended hole and slot features may be reused as released fabrication-package completeness review surfaces
    - omitted or misexpressed hole-slot intent may be reused as manufacturing-data completeness review topics before release
    - hole-table and slot-annotation support may be reused only as release-check support surfaces
    - conflicting hole-slot intent may be reused only as guarded design-intent-loss review family
  - `器件引脚的方槽、方孔如何避坑？.pdf` now has a bounded route into square or non-round lead shape as a package-to-footprint review trigger, special hole / slot request as explicit fabrication-intent expression, design-canvas appearance as separate from released-output correctness, and pre-release special-feature annotation review only
  - `器件引脚的方槽、方孔如何避坑？.pdf` now also has one narrow official-fact boundary for special hole-slot intent release-review posture:
    - square or non-round lead shape may be reused as a package-to-footprint review trigger
    - square-hole or square-slot request may be reused only as explicit special-feature intent that must be carried into the released package
    - design-canvas square-like appearance may be reused only as insufficient proof of released-output correctness
    - special hole-slot notes or annotation may be reused only as release-check support surfaces
  - `器件引脚小尺寸的孔和槽如何避坑？.pdf` now has a bounded route into small-hole / small-slot manufacturability risk framing, small lead-hole feature typing as handoff-risk family, opening or cover-oil expression as release-check surface when feature typing is confused, and pre-release `DFM/CAM` review as timing only
  - `器件引脚小尺寸的孔和槽如何避坑？.pdf` now also has one narrow official-fact boundary for small hole-slot typing release-review posture:
    - small lead-hole or small-slot feature typing may be reused as a guarded handoff-risk and release-review topic
    - mistyped small hole-slot intent may be reused only as manufacturing-data completeness review topic
    - opening or cover-oil expression may be reused only as a release-check surface when typing is confused
    - pre-release `DFM/CAM` timing may be reused only as review posture
  - `PCB板漏孔、漏槽在设计端如何避坑.pdf` now has a bounded route into omitted holes / slots as fabrication-handoff failure families, drill / route / slot output completeness as release-check topic, CAD layer-role mismatch as design-intent-loss risk, and the boundary that feature presence must be explicit in the released package rather than only visible in the design canvas
  - `PCB板漏孔、漏槽在设计端如何避坑.pdf` now also has one narrow official-fact boundary for hole-slot output-completeness review posture:
  - intended holes, slots, drill, and route features may be reused as fabrication-package completeness review surfaces
  - missing holes or slots may be reused as manufacturing-data completeness review topics before release
  - CAD layer-role mismatch and guarded feature-definition failure may be reused only as design-intent-loss or upstream review families
  - this still does not unlock CAD-specific output recipes, checker completeness, or any hole / slot / drill numerics
  - `一招搞定PCB阻焊过孔问题.pdf` now has a bounded route into via solder-mask treatment as branch taxonomy, treatment choice as context-dependent review, released solder-mask expression as the deciding output surface for cover versus open handling, and via-in-pad as one treatment-related dense-interconnect branch only
  - `一招搞定PCB阻焊过孔问题.pdf` now also has one narrow official-fact boundary for via `cover/open` release-expression and release-review posture:
    - via `cover/open` may be reused as released solder-mask output expression rather than only design-canvas intent
    - via solder-mask treatment may be reused as a fabrication-package release-review topic
    - mismatched via cover/open intent may be reused only as a guarded output-review surface before handoff
    - via-in-pad adjacency may be reused only as a branch-escalation trigger into existing HDI posture
  - `PCB设计如何防止阻焊漏开窗.pdf` now has a bounded route into solder-mask opening as explicit manufacturing-data expression, opening completeness as a release-check topic, hole-pad / SMT-pad / selected exposed-copper opening presence as review surfaces, footprint or padstack definition failure as a missing-opening family, version or object-type mismatch as design-intent-loss risk, and pre-release opening review posture only
  - `PCB设计如何防止阻焊漏开窗.pdf` now also has one narrow official-fact boundary for solder-mask opening release posture:
    - solder-mask openings may be reused as explicit released manufacturing data
    - missing openings may be reused as fabrication-package completeness review before release
    - footprint-definition failure, padstack-definition failure, and object-type or version mismatch may be reused only as guarded missing-opening families
    - this still does not unlock opening numerics, tool-recipe claims, checker sufficiency, or solderability / efficiency outcome claims
  - `PCB焊盘设计之问题详解.pdf` now has a bounded route into pad symmetry as a review dimension, pad length / width / inner spacing as non-numeric review dimensions, pad-to-mask relationship as a controlled review topic, and package-to-pad mismatch as a footprint-review trigger only
  - `PCB焊盘设计之问题详解.pdf` now also has one narrow official-fact boundary for pad review dimensions and mismatch-trigger posture:
    - pad symmetry may be reused as a footprint-review dimension
    - `pad length / width / inner spacing` may be reused as non-numeric review dimensions
    - pad-to-mask relationship may be reused as a controlled review topic
    - package-to-pad mismatch may be reused as an explicit footprint-review trigger
  - `多层板的焊盘到底应该怎么设计？四种主要设计方式带你搞懂！.pdf` now has a bounded route into pad and solder-mask opening as separate review objects, `盖PAD` / `露PAD` as pad-mask relationship branches, usable pad area as dependent on pad-to-mask relationship, `半盖半露` as a non-default pad-asymmetry risk branch, and `等大设计` as a tolerance-sensitive mask-encroachment risk family only
  - `多层板的焊盘到底应该怎么设计？四种主要设计方式带你搞懂！.pdf` now also has one narrow official-fact boundary for pad-mask relationship review posture:
    - pad and solder-mask opening may be reused as separate controlled review objects
    - `盖PAD` / `露PAD` may be reused only as guarded pad-mask relationship branches
    - `半盖半露` and `等大设计` may be reused only as pad-asymmetry or tolerance-sensitive risk branches requiring review
    - this still does not unlock pad/opening numerics, universal branch-selection doctrine, IPC terminology closure, or outcome claims
  - `这样做，轻松拿捏阻焊桥！.pdf` now has a bounded route into solder-mask bridge preservation as a defect-prevention family, dense pad spacing and pad-mask relationship as bridge-risk review topic, bridge presence or loss as a release-check surface, and no-bridge open-window treatment as a higher-risk fallback posture only
  - `这样做，轻松拿捏阻焊桥！.pdf` now also has one narrow official-fact boundary for solder-mask bridge release-review posture:
    - bridge presence or loss may be reused only as a released-output review surface in dense adjacent-opening contexts
    - adjacent pad spacing and pad-mask opening relationship may be reused only as guarded bridge-risk review context
    - no-bridge or open-window treatment may be reused only as a higher-risk fallback release posture when preserved separation is not maintained
    - this still does not unlock exact `IPC` terminology closure, bridge numerics, color/copper default rules, checker sufficiency, or outcome claims
  - `PCB“金手指”从设计到生产全流程.pdf` now has a bounded route into `gold finger` as edge-contact-region vocabulary, edge-contact region as distinct from ordinary solderable pad zones, finish planning as a zoned review topic, and IPC finish / acceptability / rigid-board standards metadata as standards-family anchors only
  - `PCB“金手指”从设计到生产全流程.pdf` now also has one narrow official-fact boundary for edge-contact identity and zoned-review posture:
    - `gold finger` may be reused as edge-connector contact-region vocabulary rather than as ordinary generic pad language
    - edge-contact region may be reused as distinct from ordinary solderable pad zones
    - finish planning may be reused as a zoned review topic when contact-duty and soldering-duty differ
    - this still does not unlock finish thickness, bevel, durability, contact resistance, acceptance, supplier capability, or qualification claims
  - `如何避免“断头线”带来的DFM（可制造性）问题？.pdf` now has a bounded route into broken traces and residual copper as DFM risk families, continuity / open-net language as release-check review surfaces, CAM confirmation as a handoff clarification boundary, and fabrication-data formats as identity rather than proof of correctness
- it also now has one narrow official-source-backed terminology boundary through:
  - `logs/p4-363-2026-5-9-e3-ipc-solder-mask-terminology-boundary-recovery.md`
  - `facts/methods/ipc-solder-mask-layer-and-pad-definition-boundary.md`
  - `sources/registry/standards/ipc-7093a-toc.md`
- it also now has one narrower vendor-scoped owner terminology boundary through:
  - `logs/p4-364-2026-5-9-e3-intel-nsmd-smd-vendor-terminology-boundary.md`
  - `facts/methods/intel-nsmd-smd-land-pad-terminology-boundary.md`
- current repo-backed wording may now name `NSMD/SMD` through Intel `AN 114` only:
  - `SMD` pads match BGA pad size in that owner-guidance context
  - `NSMD` pads are about `15%` smaller in that owner-guidance context
- it also now has one narrower standards-adjacent and CAD-owner hole-spacing boundary through:
- `logs/p4-396-2026-5-10-e3-hole-spacing-reliability-boundary-route-integration.md`
- `logs/p4-418-2026-5-10-e3-hole-spacing-authority-recovery.md`
  - `facts/methods/hole-spacing-reliability-boundary.md`
- current repo-backed wording may now name hole spacing only as:
  - reliability and failure-risk review topic
  - annular-ring weakening or breakout-like caution vocabulary
  - cracks and wicking, drill-wander, and CAF risk context
- `PCB设计孔间距的DFM可靠性.pdf` now also has one narrow official-fact boundary for hole-spacing reliability-review posture:
  - hole wall to hole wall may be reused as governed design-rule vocabulary
  - hole-to-hole clearance and hole-to-object clearance may be reused as CAD-owner manufacturing-rule vocabulary
  - this still does not unlock universal hole-spacing thresholds, acceptance criteria, or supplier-capability claims
- it also now has one narrower manufacturer-owner panelization and edge-feature boundary through:
  - `logs/p4-397-2026-5-10-e3-stamp-hole-panelization-boundary-route-integration.md`
  - `facts/methods/stamp-hole-panelization-and-castellated-edge-boundary.md`
- current repo-backed wording may now name this bridge lane only as:
  - stamp-hole or mouse-bite as panel-connection branch vocabulary
  - `V-cut` as a separate panelization branch identity
  - explicit panelization-input handling for special breakaway or slot branches
  - castellated or half-hole edge region as special review context
- `PCB邮票孔桥连设计要点，干货满满！.pdf` now also has one narrow official-fact boundary for stamp-hole branch-selection posture:
  - `logs/p4-450-2026-5-11-e3-stamp-hole-branch-selection-authority-recovery.md`
  - existing `facts/methods/stamp-hole-panelization-and-castellated-edge-boundary.md`
- this raises one more `E3` PDF beyond `single-PDF route only` into one narrow official boundary for stamp-hole or mouse-bite as branch-selection vocabulary and special-review topic
- `这样做，轻松拿捏阻焊桥！.pdf` now also has one narrow official-fact boundary for solder-mask bridge release-review posture:
  - `logs/p4-451-2026-5-11-e3-solder-mask-bridge-release-review-authority-recovery.md`
  - existing `facts/methods/ipc-solder-mask-layer-and-pad-definition-boundary.md`
  - existing `facts/methods/cam-data-exchange-format-boundary.md`
  - existing `wiki/processes/pcb-design-data-exchange-and-tool-boundaries.md`
- this raises one more `E3` PDF beyond `single-PDF route only` into one narrow official boundary for bridge presence/loss as released-output review topic
- `如何避免“断头线”带来的DFM（可制造性）问题？.pdf` now also has one narrow official-fact boundary for broken-trace release-check posture:
  - `logs/p4-449-2026-5-11-e3-broken-trace-release-check-authority-recovery.md`
  - existing `facts/methods/pcba-dfm-dft-dfa-review-gate-positioning.md`
  - existing `facts/methods/cam-data-exchange-format-boundary.md`
  - existing `wiki/processes/pcb-design-data-exchange-and-tool-boundaries.md`
- this raises one more `E3` PDF beyond `single-PDF route only` into one narrow official boundary for broken traces or residual copper as release-check and handoff-clarification topic
- it still does not unlock pad-geometry numerics or standards-grade pad-definition closure, via-treatment numerics or default rules, solder-mask opening numerics, gold-finger thickness or bevel rules, CAD-specific output recipes, tool-side detection completeness, universal solderability certainty, or any process-efficiency claims
- it also still does not unlock hole / slot numerics, plated / non-plated terminology closure, square-hole workaround defaults, half-hole geometry or process-order rules, stamp-hole bridge numerics, `V-cut` priority doctrine, small-feature compensation rules, factory-default behavior claims, or capability / cost / cycle outcomes

### `E4` Panelization, Outline, Edge Clearance, Marking, And Character

Current status: `controller_routed_at_usage_level_only`

PDF paths:

- `/code/blogs/tmps/PCB资料/PCB文章/PCB可制造性设计及案例分析之字符、外形、拼板（图文结合，推荐）.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/PCB拼板，不得不注意的10个问题！.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/PCB板各种形状的拼版实例分享.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/啥？PCB拼版对SMT组装有影响！.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/PCB板的Mark点设计对SMT重要性.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/元器件到PCB板边缘间距不足的严重性.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/PCBA板边器件布局重要性.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/PCB字符的DFM（可制造性）设计.pdf`

Narrow follow-up already landed:

- `logs/p4-443-2026-5-10-e4-legend-open-area-conflict-authority-recovery.md`
- `logs/p4-379-2026-5-9-e4-legend-outline-panel-direction-release-review-route-integration.md`
- `logs/p4-442-2026-5-10-e4-assembly-facing-panel-handling-access-risk-authority-recovery.md`
- `logs/p4-434-2026-5-10-e4-board-edge-layout-access-risk-authority-recovery.md`
- `logs/p4-421-2026-5-10-e4-board-edge-access-risk-authority-recovery.md`
- `logs/p4-347-2026-5-9-e4-board-edge-spacing-severity-route-integration.md`
- `logs/p4-348-2026-5-9-e4-board-edge-component-layout-importance-route-integration.md`
- `logs/p4-357-2026-5-9-e4-irregular-shape-panelization-examples-route-integration.md`
- `logs/p4-445-2026-5-11-e4-irregular-panel-edge-access-risk-authority-recovery.md`
- `logs/p4-444-2026-5-11-e4-panel-handling-and-edge-interference-authority-recovery.md`
- `logs/p4-353-2026-5-9-e4-mark-fiducial-role-route-integration.md`
- `logs/p4-354-2026-5-9-e4-character-legend-manufacturability-route-integration.md`
- `logs/p4-355-2026-5-9-e4-assembly-facing-panel-handling-route-integration.md`
- `logs/p4-361-2026-5-9-e4-panel-connection-and-edge-interference-route-integration.md`

Interpretation:

- this does not make the whole `E4` lane fact-promoted
- it raises eight single PDFs above pure cluster inventory:
  - `PCB可制造性设计及案例分析之字符、外形、拼板（图文结合，推荐）.pdf` now has a bounded route into legend on opened or solderable areas as a release-review surface, special inner-slot or concave outline as branch-review trigger, board-edge connection detail as post-separation review trigger, and symmetric panel direction as released-package clarity topic only
  - `PCB可制造性设计及案例分析之字符、外形、拼板（图文结合，推荐）.pdf` now also has one narrow official-fact boundary for legend on opened or solderable areas as released-manufacturing-data conflict:
    - legend on opened or solderable areas may be reused as released-manufacturing-data conflict
    - legend overlap with solderable surfaces may be reused only as footprint-release and fabrication-output review surface
    - this still does not unlock legend numerics, cleanup recipes, panel-direction doctrine, route-default rules, checker sufficiency, or quality/efficiency outcomes
  - `PCB拼板，不得不注意的10个问题！.pdf` now has a bounded route into panelization as a release-review topic for small or special boards, `V-CUT` / stamp-hole / hollow connection strip as connection-branch vocabulary, straight-line versus irregular-outline branch-selection context, board-edge or protruding-part interference review, and outer frame / holding edge / rails as planning objects only
  - `PCB拼板，不得不注意的10个问题！.pdf` now also has one narrow official-fact boundary for panelization as assembly-facing handling and edge-interference review posture:
    - panelization may be reused as assembly-facing handling and release-review decision
    - board-edge or protruding-part interference may be reused only as assembly-access and adjacency-risk review context
    - outer frame, holding edge, and panel rails may be reused only as planning and keep-access objects
    - singulation-stage accessibility loss or damage may be reused only as guarded downstream risk
    - this still does not unlock connection-branch numerics, `Mark` / tooling-hole rules, route-default doctrine, checker sufficiency, or quality/efficiency/cost outcomes
  - `PCB板各种形状的拼版实例分享.pdf` now also has one narrow official-fact boundary for protruding-edge and half-hole special regions as assembly-access and keep-access review posture:
    - protruding-edge or edge-near hardware may be reused only as panel-adjacency and assembly-access risk context
    - half-hole board may be reused only as special panelization subfamily requiring explicit special-review context
    - inward-facing special edge regions may be reused only as keep-access and adjacency-risk review surfaces
    - singulation-stage accessibility loss or damage may be reused only as guarded downstream risk
    - this still does not unlock gap/hole/bridge numerics, breakage certainty, route-default doctrine, checker sufficiency, or cost/yield/schedule outcomes
  - `元器件到PCB板边缘间距不足的严重性.pdf` now has a bounded route into board-edge component exposure as an assembly-risk family, tall-part edge exposure as a priority-review signal, depanel / transport / machine-path interference risk framing, serviceability / rework / compact-closure impact context, and mechanism-level edge-stress caution without numeric closure
  - `元器件到PCB板边缘间距不足的严重性.pdf` now also has one narrow official-fact boundary for board-edge access-risk and re-entry review posture:
    - board-edge-near parts may be reused as access-risk review surfaces
    - depanel / transport / rail / clamp / tooling / machine-path exposure may be reused only as guarded assembly-path interference review
    - serviceability, rework, and compact-closure impact may be reused only as keep-access and re-entry review layers
    - this still does not unlock edge-clearance numerics, depanel-method spacing defaults, machine-compatibility guarantees, or cost/quality/cycle claims
  - `PCBA板边器件布局重要性.pdf` now has a bounded route into board-edge component exposure as an assembly and depanel risk family, tall or fragile edge-part priority review, equipment-path / rail / fixture interference review posture, compact-closure / re-entry / serviceability impact context, and layout-fairness / edge-stress caution without numeric closure
  - `PCBA板边器件布局重要性.pdf` now also has one narrow official-fact boundary for board-edge layout access-risk and re-entry review posture:
    - board-edge-near parts may be reused as access-risk review surfaces
    - tall or fragile edge-near parts may be reused as priority-review objects for reachability, handling exposure, and later re-entry posture
    - equipment-path, rail, fixture, carrier, and adjacent handling exposure may be reused only as guarded assembly-path interference review
    - compact-closure, keep-access, serviceability, and rework impact may be reused only as re-entry review layers
    - this still does not unlock board-edge numerics, depanel spacing defaults, machine-compatibility guarantees, reliability certainty, or cost/quality/cycle claims
  - `PCB板各种形状的拼版实例分享.pdf` now has a bounded route into irregular outline as panelization branch-selection context, shape-constrained route choice for nonflush / grooved / rounded edges, half-hole boards as special panelization subfamily, protruding-edge component interference context, and inverted arrangement / stamp-hole bridge as example branch choices only
  - `PCB板的Mark点设计对SMT重要性.pdf` now has a bounded route into `Mark` as optical alignment reference, board / panel / local-component scope split, asymmetry as orientation-disambiguation context, and visibility / cleanliness as recognition conditions
  - `PCB板的Mark点设计对SMT重要性.pdf` has now also been re-audited against the current `IPC-7525C` stencil-metadata lane, internal stencil-support lane, and `Ucamco` Gerber fiducial-attribute lane, but those anchors still stop below a clean single-PDF official raise, so this surface remains route-only unless a materially stronger assembly-owner, CAD-library-owner, or standards-adjacent fiducial source appears
  - `PCB字符的DFM（可制造性）设计.pdf` now has a bounded route into character / legend as fabrication-communication and identification context, obstruction risk on solderable areas, readability risk from small/dense/overlapping/clipped legend, mirroring as legibility coordination, and logo / code placement as release-coordination topic
  - `PCB字符的DFM（可制造性）设计.pdf` now also has one narrow official-fact boundary for character or legend on opened / solderable areas as released-manufacturing-data conflict:
    - character or legend on opened or solderable areas may be reused as released-manufacturing-data conflict topic
    - character overlap with solderable surfaces may be reused only as footprint-release and fabrication-output review surface
    - this still does not unlock legend numerics, QR / barcode geometry, color/process-capability claims, mirroring doctrine, or checker sufficiency
  - `啥？PCB拼版对SMT组装有影响！.pdf` now has a bounded route into panelization as assembly-facing handling decision, no-gap / tight adjacency as inter-board component-interference risk, rails and kept separation as assembly-clearance posture, and depanel damage / scrap as guarded downstream risk
  - `啥？PCB拼版对SMT组装有影响！.pdf` now also has one narrow official-fact boundary for assembly-facing panel handling as board-edge access-risk and keep-access review posture:
    - panelization may be reused as assembly-facing handling decision
    - no-gap or tight adjacency may be reused only as inter-board component-interference risk
    - rails and kept separation may be reused only as assembly-clearance and keep-access posture
    - depanel-stage damage plus later re-entry or serviceability impact may be reused only as guarded downstream-risk and re-entry review layers
    - this still does not unlock panelization numerics, route-default rules, machine-compatibility guarantees, checker sufficiency, or yield/cost/cycle/schedule outcomes
- it still does not unlock edge-clearance numerics, `V-CUT` or tab-route spacing defaults, stamp-hole or connection-strip numerics, `Mark` geometry/count defaults, legend geometry numerics, panelization numerics, breakage-certainty claims, machine-compatibility guarantees, reliability / quality / cycle claims, or branded checker authority

### `E5` Assembly, DFA, Stencil, Soldering, Polarity, And Test

Current status: `controller_routed_at_usage_level_only`

PDF paths:

- `/code/blogs/tmps/PCB资料/PCB文章/DFA是什么？这些组装性问题你都知道怎么解决吗？.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/关于PCBA元器件布局的重要性.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/组装电子元器件间距不足的严重性.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/如何避免踩坑钢网.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/你想知道的BGA焊接问题都在这里.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/那些关于DIP器件不得不说的坑.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/元器件虚焊原因之一盘中孔的可制造设计规范.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/PCBA丝印位号与极性符号的组装性设计.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/PCB测试四大方式你都了解吗？内含治具的DFM（可制造性）设计！.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/如何保证电子产品可靠性设计？三方面为您解读，值得收藏！.pdf`

Narrow follow-up already landed:

- `logs/p4-330-2026-5-9-e5-test-method-and-ict-fixture-route-integration.md`
- `logs/p4-332-2026-5-9-e5-polarity-reference-designator-route-integration.md`
- `logs/p4-335-2026-5-9-e5-stencil-and-paste-route-integration.md`
- `logs/p4-337-2026-5-9-e5-bga-soldering-route-integration.md`
- `logs/p4-422-2026-5-10-e5-dip-fit-review-trigger-authority-recovery.md`
- `logs/p4-339-2026-5-9-e5-dip-tht-route-integration.md`
- `logs/p4-342-2026-5-9-e5-component-layout-importance-route-integration.md`
- `logs/p4-343-2026-5-9-e5-component-spacing-severity-route-integration.md`
- `logs/p4-344-2026-5-9-e5-via-in-pad-manufacturability-route-integration.md`
- `logs/p4-345-2026-5-9-e5-dfa-assembly-risk-route-integration.md`
- `logs/p4-346-2026-5-9-e5-reliability-design-dfm-route-integration.md`
- `logs/p4-416-2026-5-10-e5-reliability-review-trigger-authority-recovery.md`
- `logs/p4-432-2026-5-10-e5-component-spacing-access-and-rework-authority-recovery.md`
- `logs/p4-433-2026-5-10-e5-crowded-neighborhood-access-and-rework-authority-recovery.md`

Interpretation:

- this does not make the whole `E5` lane fact-promoted
- it raises only ten single PDFs above pure cluster inventory:
  - `DFA是什么？这些组装性问题你都知道怎么解决吗？.pdf` now has a bounded route into DFA as assembly-risk taxonomy, package-to-footprint and pin-count mismatch review triggers, component-spacing as access / rework risk, board-edge and transport exposure as a guarded assembly-risk family, silkscreen reference visibility as an assembly-communication issue, and mark-point identity context only
  - `DFA是什么？这些组装性问题你都知道怎么解决吗？.pdf` now also has one narrow official-fact boundary for early assembly-review posture:
    - `DFA` may be reused as an upstream assembly-review gate
    - package-name mismatch, pin-count mismatch, and footprint-library selection mismatch may be reused as explicit release triggers
    - this still does not unlock spacing numerics, pad geometry, fiducial rules, hole-fit ratios, or workflow-sufficiency claims
  - `PCB测试四大方式你都了解吗？内含治具的DFM（可制造性）设计！.pdf` now has a bounded route into flying-probe versus `ICT` identity, fixture-introduction readiness, and inspection-governance surfaces
  - `PCBA丝印位号与极性符号的组装性设计.pdf` now has a bounded route into polarity / orientation inspection vocabulary and package-library governance surfaces
  - `如何避免踩坑钢网.pdf` now has a narrow official boundary into stencil-guideline family scope, solder-paste layer identity, and upstream print-control framing, plus the earlier bounded route into stencil / paste upstream control and mixed-technology sequencing surfaces
  - `你想知道的BGA焊接问题都在这里.pdf` now has a bounded route into BGA process-review, reflow boundary, and hidden-joint X-ray visibility surfaces
  - `PCBA丝印位号与极性符号的组装性设计.pdf` now has a narrow official boundary into `pin-1`, polarity, and reference-designator documentation governance, plus the earlier bounded route into inspection vocabulary and package-library governance surfaces
  - `那些关于DIP器件不得不说的坑.pdf` now has a bounded route into DIP / THT fit-review identity, mixed-technology route planning before wave or selective solder, and dense through-hole neighborhood access-review surfaces
  - `那些关于DIP器件不得不说的坑.pdf` now also has one narrow official-fact boundary for DIP/THT fit-review trigger posture:
    - DIP / THT package discussion may be reused as a fit-review trigger before insertion and solder-route execution
    - package identity versus footprint-library object alignment may be reused as a review surface before THT insertion
    - owner-scoped lead / finished-hole / pitch compatibility may be reused only as a must-check-against-the-component-datasheet review posture
    - this still does not unlock hole/lead/pitch numerics, bridge-threshold rules, route-superiority claims, or reliability/cost/schedule outcomes
  - `元器件虚焊原因之一盘中孔的可制造设计规范.pdf` now has a bounded route into via-in-pad as dense-interconnect / HDI posture, dense BGA escape-pressure review triggers, one owner-scoped via-in-pad existence example, and local mechanism examples that keep via-in-pad discussion tied to later assembly and inspection review
  - `元器件虚焊原因之一盘中孔的可制造设计规范.pdf` now also has one narrow official-fact boundary for via-in-pad review-trigger posture:
    - via-in-pad discussion may be reused as a dense-BGA escape-pressure review trigger
    - one named owner example may be reused to show that via in pad exists in real CSP/BGA layout guidance
    - via strategy escalation may stay tied to HDI posture plus later reflow and hidden-joint inspection review
    - this still does not unlock fanout numerics, pitch-threshold rules, universal resin-fill or planarization defaults, defect-certainty claims, or cost/lead-time/capability outcomes
  - `如何保证电子产品可靠性设计？三方面为您解读，值得收藏！.pdf` now has a bounded route into early DFM review-gate posture, fabrication and assembly review-surface inventory, package-to-footprint and pin-count review triggers, spacing / interference / rework-access risk language, and article-side fabrication / assembly / cost tri-split inventory only
  - `如何保证电子产品可靠性设计？三方面为您解读，值得收藏！.pdf` now also has one narrow official-fact boundary for early review posture:
    - `DFM/DFA` may be reused only as an early fabrication-and-assembly review posture
    - package-name mismatch, pin-count mismatch, and footprint-library selection mismatch may be reused as explicit stop-and-review triggers before release
    - this still does not unlock reliability outcomes, geometry numerics, pricing logic, thermal/performance assurance, or tool-sufficiency claims
  - `如何保证电子产品可靠性设计？三方面为您解读，值得收藏！.pdf` now also has one additional narrow official-fact boundary for spacing / spatial-interference / rework-access assembly-review posture:
    - spacing and spatial interference may be reused only as assembly-access review surfaces
    - dense or tall component neighborhoods may be reused only as mixed-technology assembly-review inputs because they change solder, inspection, test, and later repair access
    - package-neighborhood interference and crowded re-entry paths may be reused only as keep-access and rework-access review surfaces
    - this still does not unlock spacing numerics, geometry thresholds, reliability outcomes, thermal/performance assurance, or cost/quality/tool claims
  - `关于PCBA元器件布局的重要性.pdf` now has a bounded route into component-spacing as access / rework boundary, dense mixed-technology neighborhood review, tall-part interference review, and stencil-spacing interaction context
  - `关于PCBA元器件布局的重要性.pdf` now also has one narrow official-fact boundary for component-spacing access and rework posture:
    - component spacing may be reused as an access and rework boundary
    - dense or tall component neighborhoods may be reused as mixed-technology assembly-review inputs because they change solder access, inspection reach, test reach, and later repair access
    - connector overhang, tall-part adjacency, and large-part-over-small-part obstruction may be reused as explicit interference and re-entry review surfaces
    - this still does not unlock spacing numerics, safety grading, stencil-threshold rules, warpage-causality certainty, checker sufficiency, or cost/cycle/reliability outcomes
  - `组装电子元器件间距不足的严重性.pdf` now has a bounded route into dense-neighborhood route review, mixed SMT/THT neighbor access-risk taxonomy, manual touch-up serviceability risk, and local mechanism examples around pads, vias, and close solder neighborhoods
  - `组装电子元器件间距不足的严重性.pdf` now also has one narrow official-fact boundary for crowded-neighborhood access and rework review posture:
    - crowded mixed-technology neighborhoods may be reused as route-review triggers
    - nearby pins, pads, vias, holes, and component bodies may be reused as access and nearby-hardware interference review surfaces
    - dense neighborhoods may be reused as manual touch-up and serviceability risk context, with post-rework revalidation kept as a neighboring governance layer
    - this still does not unlock spacing thresholds, solder-mask defaults, via-in-pad rules, defect certainty, process-parameter causality, or reliability/cost/schedule outcomes
- it also now has one narrow official-source-backed test-method boundary through:
  - `logs/p4-409-2026-5-10-e5-test-method-and-ict-fixture-authority-recovery.md`
  - `facts/methods/pcba-ict-fixture-introduction-gate.md`
  - `sources/registry/standards/keysight-in-circuit-test-systems-page.md`
  - `sources/registry/standards/seica-flying-probe-page.md`
- current repo-backed wording may now name this bridge lane only as:
  - `ICT` as fixture-based and flying probe as fixture-free manufacturing-test identity
  - `ICT fixture introduction` as a DFM/DFT and release-readiness gate
  - `AOI` and manual visual inspection as neighboring governance layers rather than part of one universal doctrine
- it also now has one narrow official-source-backed BGA process boundary through:
  - `logs/p4-410-2026-5-10-e5-bga-process-and-hidden-joint-authority-recovery.md`
  - `facts/methods/bga-staged-process-review-and-hidden-joint-inspection-boundary.md`
  - `facts/methods/low-void-bga-dfm-to-process-review.md`
  - `facts/methods/low-void-bga-reflow-paste-vs-assembly-boundary.md`
  - `facts/methods/hidden-joint-xray-inspection-boundary.md`
  - `wiki/processes/low-void-bga-reflow-and-hidden-joint-inspection.md`
- current repo-backed wording may now name this bridge lane only as:
  - BGA assembly as a staged DFM-to-process-review chain
  - reflow as paste-dependent and assembly-dependent rather than a universal recipe
  - X-ray or AXI as the hidden-joint visibility layer for dense-package inspection
- it still does not unlock locator-hole geometry, universal silkscreen rules, acceptability thresholds, tool-marketing authority, pricing / quote logic, or cost / throughput / yield claims

### `E6` Packages, BOM, Procurement-Risk, And Flexible-Circuit Subset

Current status: `controller_routed_at_usage_level_only_with_explicit_procurement_hold_split`

PDF paths:

- `/code/blogs/tmps/PCB资料/PCB文章/电子元器件封装(Package).pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/如何解决bom物料与焊盘不匹配问题.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/BOM查错助力元器件采购.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/如何避免采购电子元器件入坑.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/0Ω电阻在PCB板中的5大常见作用.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/单层双面多层FPC有何区别？.pdf`

Narrow follow-up already landed:

- `logs/p4-329-2026-5-9-1p50mm-nxp-legacy-pbga-route.md`
- `logs/p4-326-2026-5-9-e6-fpc-type-taxonomy-official-source-recovery.md`
- `logs/p4-327-2026-5-9-e6-zero-ohm-jumper-identity-source-recovery.md`
- `logs/p4-328-2026-5-9-e6-package-to-footprint-alignment-source-integration.md`
- `logs/p4-333-2026-5-9-e6-package-family-and-footprint-route-integration.md`
- `logs/p4-336-2026-5-9-e6-bom-sourcing-and-alternate-control-route-integration.md`
- `logs/p4-338-2026-5-9-e6-procurement-risk-route-integration.md`
- `facts/standards/ipc-flex-printed-board-type-taxonomy-boundary.md`
- `facts/methods/zero-ohm-jumper-resistor-identity-boundary.md`
- `facts/methods/package-to-footprint-and-pin-count-alignment-review-boundary.md`
- `wiki/processes/flex-printed-board-type-taxonomy-and-structure-map.md`

Interpretation:

- this now raises five `E6` subtopics above pure article inventory:
- `1.50 mm` package residual now also has one current-public owner-scoped near-hit above the pure `P4-318` standards-owner existence boundary, but it remains below exact-geometry closure
  - `FPC` structure-taxonomy
  - `0R` jumper-class identity
  - `package-to-footprint / pin-count alignment` review posture
  - `BOM identity-field separation` review posture
  - `package identity grammar` review posture
- `BOM查错助力元器件采购.pdf` now also has a bounded single-PDF route into BOM sourcing / traceability, alternate-control, and BOM-governance surfaces without new fact promotion
- `BOM查错助力元器件采购.pdf` now also has one narrow official-fact boundary for BOM identity-field separation:
  - manufacturer identity should stay explicit
  - `Manufacturer Part Number` should remain a distinct mapped field
  - supplier-facing sourcing identity should remain a separate downstream review surface
  - this still does not unlock automatic matching sufficiency, availability, quote, or delivery claims
- `如何避免采购电子元器件入坑.pdf` now also has a bounded single-PDF route into procurement-risk, BOM identity completeness, alternate-control, and traceability vocabulary without new fact promotion
- `如何避免采购电子元器件入坑.pdf` now also has one narrow official-fact boundary for procurement-ready BOM release posture:
  - manufacturer identity should stay explicit
  - `Manufacturer Part Number` should remain distinct from supplier-facing sourcing or order-link fields
  - alternates, traceability, and authenticity review should remain controlled governance layers rather than supply-outcome proof
  - this still does not unlock stock, shortage, lead-time, MOQ, authenticity outcomes, seller approval, or delivery claims
- `电子元器件封装(Package).pdf` now also has a bounded single-PDF route into package-family vocabulary, package-to-footprint review triggers, and package-library governance surfaces without new fact promotion
- `电子元器件封装(Package).pdf` now also has one narrow official-fact boundary for package identity grammar:
  - package-family label may be reused as identity grammar
  - pin count and variant may stay as separate identifier fields
  - owner-scoped legacy aliases may be reused conservatively in package context
  - this still does not unlock size-code conversion truth, exact geometry, or universal cross-vendor package grammar
- it does not make the whole `E6` lane fact-promoted
- package dimensions, BOM quantities, procurement-risk claims, and broader `0R` role taxonomy remain on their existing routed or hold-only boundaries

### `E7` Manufacturing Data Exchange And Vendor-Tool Workflow

Current status: `controller_hold_lane_with_single_pdf_route_expansion`

PDF paths:

- `/code/blogs/tmps/PCB资料/PCB文章/PCB制造文件传输数据的主要格式.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/华秋DFM组装分析前需准备的数据文件.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/简单好用！再也不用担心PCB图形对齐问题.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/华秋DFM可视化BOM交互焊接工具，SMT工厂、PCB工程师的福音来了！.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/华秋DFM携带DFA全网重磅上线！新功能极速体验，一睹为快.pdf`
- `/code/blogs/tmps/PCB资料/PCB文章/华秋干货铺：PCB设计避坑指南（图文结合、视频演示，荐读！）.pdf`

Narrow follow-up already landed:

- `logs/p4-340-2026-5-9-e7-data-exchange-format-route-integration.md`
- `logs/p4-341-2026-5-9-e7-assembly-analysis-input-package-route-integration.md`
- `logs/p4-351-2026-5-9-e7-graphic-alignment-workflow-route-integration.md`

Interpretation:

- this does not make the whole `E7` lane fact-promoted
- it raises only three single PDFs above pure cluster inventory:
  - `PCB制造文件传输数据的主要格式.pdf` now has a bounded route into authoring-file versus manufacturing-handoff-package identity, Gerber / ODB++ / IPC-DPMX identity-level exchange vocabulary, and the boundary that fabrication outputs do not by themselves equal full assembly or test review completeness
  - `PCB制造文件传输数据的主要格式.pdf` now also has one narrow official-fact boundary for native PCB authoring file versus released manufacturing-handoff package identity:
    - native PCB authoring files and released manufacturing-transfer outputs may be reused as different data layers
    - Gerber and `ODB++` may be reused as manufacturing-data exchange format identities in fabrication handoff context
    - a released fabrication-oriented format package may be reused as not being the full downstream assembly or test package by itself
    - this still does not unlock `Excellon` authority closure, universal release-package doctrine, format-superiority claims, vendor support-matrix claims, one-format production-readiness, or cost/yield/quote-speed outcomes
  - `华秋DFM组装分析前需准备的数据文件.pdf` now has a bounded route into assembly-input-package boundary, different file families carrying different downstream review context, and the caution that Gerber / drill handoff may still require separate BOM and placement-related companion artifacts
  - `华秋DFM组装分析前需准备的数据文件.pdf` now also has one narrow official-fact boundary for assembly-analysis input package boundary:
    - fabrication-oriented handoff files and assembly-supporting companion artifacts may be reused as different data layers
    - Gerber and drill outputs may be reused as fabrication-oriented handoff files, not as the full assembly-analysis input package by themselves
    - `BOM` and placement-related data may be reused as remaining separate companion artifacts when the chosen handoff family does not already expose enough assembly context
    - this still does not unlock universal `PCB/ODB` embedded-content sufficiency, universal minimum assembly-analysis package doctrine, tool-capability claims, file-prep-readiness claims, or automatic matching / outcome claims
  - `简单好用！再也不用担心PCB图形对齐问题.pdf` now has a bounded route into graphic alignment as a shared-reference-frame correction workflow, single-layer and local-subregion alignment by common reference point, multi-layer alignment as revision-comparison registration, and coordinate-to-graphic alignment as a local pre-analysis correction posture
- it still does not unlock Excellon authority closure, universal format-superiority claims, vendor support-matrix claims, one-package manufacturing-readiness guarantees, or branded UI-step / convenience claims

## Historical Article Execution Order

Historical execution sequence under this master entry:

1. `E3`
2. `E5`
3. `E2`
4. `E4`
5. `E6`
6. package residual authority recovery

Hold-only by default:

- `E1`
- `E7`

## Current Next Sequence

Current next sequence from this master entry is:

1. use this master entry as a current-state surface, not as a blind `1.50 mm first` search instruction
2. treat the current package residual block as materially stronger but still open:
  - `1.50 mm = IEC 60191-6-2 existence + IEC 61188-5-8/6-2 land-pattern family boundary + NXP exact row + Renesas named-package drawing + Renesas exact row + AMD-hosted BG225/BGG225 third-owner exact row`
  - `0.75 mm = three Microchip exact rows + one Renesas second-owner exact-data page + one NXP third-owner exact-data page + one Intel-hosted .75mm µBGA CSP fourth-owner exact table`
   - `connector-origin = KiCad + Molex + Samtec + Amphenol layered support`
   - `installation mark / component marking = layered support + IEC zero-orientation + IEC pin-1 / polarity-identification route`
3. reopen those package residuals only if a materially stronger owner or standards-adjacent source appears
4. otherwise keep the current restart pressure on candidate-gated package and doctrine residuals from `P4-325`, while treating article-side narrow recovery as effectively exhausted at the current authority layer unless genuinely new authority appears

## Batch-1 Deliverables

The first execution batch under this master entry is:

1. create this `P4-309` corpus master log
2. create `logs/p4-311-2026-5-8-pcb-article-e3-usage-route-integration.md`
3. create `logs/p4-313-2026-5-8-pcb-article-e5-usage-route-integration.md`
4. update trackers so future `/goal` work resumes from `P4-309`

Batch-1 status:

- `completed`
- landed outputs:
  - `logs/p4-311-2026-5-8-pcb-article-e3-usage-route-integration.md`
  - `logs/p4-313-2026-5-8-pcb-article-e5-usage-route-integration.md`

## Batch-2 Deliverables

The second execution batch under this master entry is:

1. create `logs/p4-310-2026-5-8-pcb-article-e2-usage-route-integration.md`
2. create `logs/p4-312-2026-5-8-pcb-article-e4-usage-route-integration.md`
3. update trackers so future `/goal` work resumes from `P4-309` with `E2/E3/E4/E5` article usage integration already landed and `E6` as the final article usage lane still open at that batch boundary

Batch-2 status:

- `completed`
- landed outputs:
  - `logs/p4-310-2026-5-8-pcb-article-e2-usage-route-integration.md`
  - `logs/p4-312-2026-5-8-pcb-article-e4-usage-route-integration.md`

## Batch-3 Deliverables

The third execution batch under this master entry is:

1. create `logs/p4-314-2026-5-8-pcb-article-e6-usage-route-integration.md`
2. update trackers so future `/goal` work resumes from `P4-309` with article-side usage routing complete through `E2-E6`

Batch-3 status:

- `completed`
- landed outputs:
  - `logs/p4-314-2026-5-8-pcb-article-e6-usage-route-integration.md`

## Batch-4 Deliverables

The fourth execution batch under this master entry is:

1. land one owner-scoped `0.75 mm` exact-data replacement row
2. land one layered boundary route for `connector-origin` and `installation mark`
3. land one standards-owner existence boundary for `1.50 mm`
4. update master and trackers so future `/goal` work resumes from `P4-309` with package residuals narrowed rather than fully open

Batch-4 status:

- `completed_as_partial_residual_narrowing`
- landed outputs:
  - `logs/p4-316-2026-5-8-microchip-0p75mm-tfbga-land-pattern-landing.md`
  - `logs/p4-317-2026-5-8-connector-origin-and-installation-mark-boundary-landing.md`
  - `logs/p4-318-2026-5-8-iec-1p50mm-bga-standards-existence-boundary.md`

## Batch-5 Deliverables

The fifth execution batch under this master entry is:

1. recheck whether the public package-owner surface can advance `1.50 mm` beyond the current `P4-318` standards-existence boundary
2. if no real public exact-geometry row appears, land a controller note so future `/goal` work does not reopen the same uncertainty as if it were unscouted

Batch-5 status:

- `completed_as_no_upgrade_recheck`
- landed outputs:
  - `logs/p4-319-2026-5-8-1p50mm-public-exact-geometry-recheck.md`

## Batch-6 Deliverables

The sixth execution batch under this master entry is:

1. strengthen the `0.75 mm` residual lane by landing one more owner-scoped named-package exact-data row
2. update route maps and trackers so future `/goal` work sees `0.75 mm` as `multiple owner-scoped rows landed`, not just one

Batch-6 status:

- `completed_as_partial_residual_narrowing`
- landed outputs:
  - `logs/p4-320-2026-5-8-microchip-second-0p75mm-tfbga-row-landing.md`

## Batch-7 Deliverables

The seventh execution batch under this master entry is:

1. recheck whether one additional connector-owner public drawing can safely strengthen the current `connector-origin / installation mark` lane
2. if the candidate remains public-access blocked, land a controller note so future `/goal` work does not misread it as already-promotable authority

Batch-7 status:

- `completed_as_access_blocker_note`
- landed outputs:
  - `logs/p4-321-2026-5-8-connector-owner-amphenol-public-access-blocker-note.md`

## Batch-8 Deliverables

The eighth execution batch under this master entry is:

1. land one more publicly retrievable connector-owner named-series drawing route
2. update the current boundary card so connector-owner support is not limited to `Molex 105133` alone

Batch-8 status:

- `completed_as_partial_residual_narrowing`
- landed outputs:
  - `logs/p4-322-2026-5-8-samtec-connector-owner-layout-route-landing.md`

## Batch-9 Deliverables

The ninth execution batch under this master entry is:

1. preserve one reusable search filter for the still-open `1.50 mm` exact-geometry lane
2. record that some `1.50` hits in package drawings are false positives tied to body size or contact-pad spacing rather than package pitch

Batch-9 status:

- `completed_as_search_filter_note`
- landed outputs:
  - `logs/p4-323-2026-5-8-1p50mm-search-filter-note.md`

## Batch-10 Deliverables

The tenth execution batch under this master entry is:

1. land one more owner-scoped `0.75 mm` named-package exact-data row
2. update route maps and trackers so future `/goal` work sees `0.75 mm` as three landed owner-scoped Microchip rows

Batch-10 status:

- `completed_as_partial_residual_narrowing`
- landed outputs:
  - `logs/p4-324-2026-5-8-microchip-third-0p75mm-tfbga-row-landing.md`

## Resume Rule

When future agents are asked whether `/code/blogs/tmps/PCB资料` is fully learned, the correct answer is:

- handbook side: program-level `strong_complete`, with explicit residual authority gaps
- article side: controller-level usage routing is covered across `E2-E6`, while `E1/E7` remain hold-heavy with only narrow single-PDF route expansions and article-side fact/wiki promotion is still far from complete

Do not collapse these two statements into a false single claim such as `all PDFs fully learned`.

## Next Resume Point

Resume from this file and execute:

- do not treat current package residuals as blind-search-first continuation
- treat `0.75 mm` as `three owner-scoped Microchip exact rows plus one Renesas second-owner exact-data page plus one NXP third-owner exact-data page`, not as fully closed
- treat `connector-origin` as `KiCad convention plus Molex, Samtec, and Amphenol named-series routes`, not as a universal doctrine
- treat `installation mark / component marking` as `layered boundary support plus one IEC zero-orientation anchor plus one IEC public pin-1 / polarity-identification route`, while board-level geometry and package-family-specific marking closeout remain open
- treat the current non-BGA `connector-origin / installation-mark / visible-vs-fab cue` lane as already re-audited at this safe ceiling; do not reopen it on the current `KiCad + Molex/Samtec/Amphenol + IEC + local handbook` set alone
- treat connector-owner support as `KiCad convention plus Molex, Samtec, and Amphenol named-series routes`, not as a universal connector doctrine
- treat `P4-321` as the current blocker note for one additional Amphenol connector-owner candidate; do not promote it until the public endpoint is retrievable as a real owner document
- treat `1.50 mm` as `IEC 60191-6-2 existence plus IEC 61188-5-8/6-2 land-pattern family boundary plus one NXP exact row plus one Renesas drawing plus one Renesas exact row plus one AMD-hosted BG225/BGG225 third-owner exact row`, while universal closeout still remains open
- treat `P4-319` as the current negative-result controller note for public `1.50 mm` recheck; do not pretend this gap is unscouted
- treat `P4-323` as the current search-filter note for `1.50 mm`; filter out body-size and contact-pad-spacing false positives before reopening owner-drawing candidates
- treat `P4-473` as a still-useful reject-filter note for the old weak `1.50 mm` candidate classes:
  - current IEC pages still stay at metadata or standards-family framing only
  - current Infineon near-hit still lacks a same-document public exact land-pattern row
  - current ADI candidate class still contains false positives where `1.50` is not the real package pitch
- treat `P4-479` as the current third-owner exact-row landing for `1.50 mm`
- do not reopen `1.50 mm` again on the old weak candidate classes alone; only reopen it next for a legitimately public official geometry surface or another materially stronger owner-scoped surface above the current stack
- treat `0.75 mm` as second priority behind `1.50 mm`, but no longer as a lane still waiting on a fourth owner row
- treat `P4-474` as a still-useful reject-filter note for the old weak `0.75 mm` candidate classes:
  - current NXP general-BGA guidance still does not expose a `0.75 mm` row
  - current IEC surface still remains family-boundary metadata rather than public exact geometry
  - current Renesas common-pitch material still does not rise above the already-landed multi-owner ceiling
- treat `P4-481` as the current fourth-owner exact-table landing for `0.75 mm`
- do not reopen `0.75 mm` again on the old weak candidate classes alone; only reopen it next for a legitimately public official geometry surface or another materially stronger owner-scoped surface above the current stack
- treat `P4-475` as the latest negative-result successor for the remaining doctrine residuals:
  - current IEC support still stays at orientation or marking framing rather than doctrine closeout
  - current `KiCad/KLC` support still stays at CAD-owner convention level
  - current connector-owner material still stays at named-series context rather than cross-family doctrine
- treat the `194页 handbook` as currently strengthened to `four D3 + four D5 routes`; do not keep it in the main watch-only residual list unless another genuinely independent handbook residual later clears a new authority bar
- treat `P4-482` as the current completion-wording successor after `P4-481`; do not keep using `P4-480` as the freshest completion snapshot
- treat article-side narrow recovery as effectively exhausted at the current authority layer except for already re-audited `E4 Mark` and `E7` residuals; reopen those only if genuinely new authority appears, otherwise shift restart pressure back to non-article residual authority gaps
- preserve the article-side result as:
  - `E2-E6` usage-route covered at controller level
  - `E1/E7` hold-heavy lanes with bounded single-PDF route expansions
- keep `E1` and `E7` hold-heavy unless a bounded neutral subset can change the fact layer
