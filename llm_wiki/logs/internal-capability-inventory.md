# Internal Capability Inventory

Last updated: 2026-04-24

## Purpose

盘点 `frontendHIL` 与 `frontendAPT` 非博客公开内容中，已经可以沉淀为 `llm_wiki` 内部支持层的能力主题。

这份清单的作用不是替代 facts，而是：

- 让后续批次按固定主题推进
- 避免重复从多语言页面里反复找点
- 明确哪些能力已经落卡，哪些还只是候选

本清单现已受 `policies/internal-capability-taxonomy.md` 约束。

## Inventory Rules

- 这里只收录英文非博客公开页面作为主扫描入口
- 内部页面只能作为 `internal support`
- 含明显营销数字的内容，只有在多页重复、且用于“能力存在性”时才可沉淀
- 涉及标准、法规、官方材料参数时，仍以外部主源为准

## Current Internal Source Spine

Already registered:

- `frontendhil-rogers-product-page-en`
- `frontendhil-high-frequency-product-page-en`
- `frontendapt-high-frequency-pcb-page-en`
- `frontendapt-microwave-pcb-page-en`
- `frontendapt-pcb-surface-finishes-page-en`
- `frontendhil-pcb-surface-finish-landing-en`
- APT PCBA pages for SMT/THT, SPI, AOI, X-ray, ICT, FCT, FPT, IQC, FAI/FQI, NPI, small-batch, mass production, stencil, selective soldering, BGA/QFN, cable, harness, IC programming, support, and BOM/component sourcing
- APT PCB pages for advanced fabrication, HDI, high-layer-count, impedance control, fabrication process, high-thermal, metal-core, ceramic, rigid-flex, flex, multilayer, and high-speed
- HIL product pages for HDI, heavy copper, high thermal, IC substrate, metal core, rigid-flex, ceramic, flex, Teflon/PTFE, large-volume assembly, and small-batch assembly
- APT material pages for Arlon, Isola, Megtron, Taconic, Teflon/PTFE, spread-glass FR-4, and controlled-impedance stackups

Newly identified as high-value:

- `frontendapt-pcb-drilling-page-en`
- `frontendapt-antenna-pcb-page-en`
- `frontendapt-backplane-pcb-page-en`
- `frontendhil-backplane-product-page-en`
- `frontendhil-high-speed-product-page-en`

## Capability Map

以下能力域已统一映射到 taxonomy buckets：

- `stackup`
- `fabrication`
- `finish`
- `validation`
- `integration`

### Stackup

Status:

- `covered`

Existing fact cards:

- `hybrid-rf-stackup-capability`
- `ptfe-processing-capability`
- `hdi-microvia-and-vippo-process-posture`
- `rigid-flex-stackup-and-bend-reliability-posture`
- `spread-glass-and-controlled-impedance-planning`

Main supporting pages:

- HIL `rogers-pcb.json`
- HIL `high-frequency-pcb.json`
- APT `high-frequency-pcb.json`
- APT `microwave-pcb.json`
- APT `pcb-stack-up.json`
- APT `multi-layer-laminated-structure.json`

Next likely cards:

- `lamination-profile-and-resin-flow-control`
- `high-layer-count-stackup-review-posture`

### Validation

Status:

- `covered`

Existing fact cards:

- `rf-validation-capability`
- `advanced-validation-scope-segmentation`
- `pcba-layered-inspection-stack`
- `pcba-ict-vs-fct-boundary`
- `pcba-fai-fqi-and-traceability-gates`
- `pcba-flying-probe-test-positioning`
- `controlled-impedance-tdr-verification-posture`

Main supporting pages:

- HIL `rogers-pcb.json`
- HIL `high-frequency-pcb.json`
- HIL `high-speed-pcb.json`
- APT `high-frequency-pcb.json`
- APT `microwave-pcb.json`
- APT `pcb-quality.json`

Next likely cards:

- `advanced-validation-scope-segmentation`
- `coupon-planning-and-correlation-posture`

### Finish

Status:

- `partially_covered`

Existing fact cards:

- `surface-finish-selection-for-rf`
- `selective-multi-finish-strategy`
- `finish-zoning-by-assembly-sequence-and-storage-exposure`
- `press-fit-finish-selection`

Main supporting pages:

- APT `pcb-surface-finishes.json`
- HIL `pcb-surface-finish` landing
- HIL `rogers-pcb.json`
- HIL `high-frequency-pcb.json`
- APT `antenna-pcb.json`

Next likely cards:

- `finish-zoning-by-assembly-sequence-and-storage-exposure`
- `press-fit-finish-selection`

### Fabrication

Status:

- `now`

Strong supporting pages:

- APT `pcb-drilling.json`
- APT `backplane-pcb.json`
- HIL `backplane-pcb.json`
- HIL `high-speed-pcb.json`
- HIL `rogers-pcb.json`
- HIL `multilayer-pcb.json`

Immediate target cards:

- `backdrill-control-capability`

Later target cards:

- `press-fit-hole-control-posture`
- `microvia-and-controlled-depth-drilling-posture`

Fabrication subclusters:

- drilling and stub control
- cavity, shield, and antenna mechanical features

Strong supporting pages:

- APT `pcb-drilling.json`
- APT `backplane-pcb.json`
- APT `antenna-pcb.json`
- APT `high-frequency-pcb.json`
- APT `microwave-pcb.json`
- HIL `backplane-pcb.json`
- HIL `high-frequency-pcb.json`
- HIL `high-speed-pcb.json`
- HIL `rogers-pcb.json`
- HIL `multilayer-pcb.json`

Existing fact cards:

- `backdrill-control-capability`
- `cavity-machining-capability`
- `high-layer-count-backdrill-and-registration-posture`
- `thermal-pcb-platform-selection-posture`
- `ic-substrate-fine-line-build-up-posture`

Later target cards:

- `press-fit-hole-control-posture`
- `microvia-and-controlled-depth-drilling-posture`
- `shield-cavity-and-waveguide-feature-planning`
- `phase-match-and-launch-review-posture`

### Integration

Status:

- `partially_covered`

Strong supporting pages:

- APT `backplane-pcb.json`
- HIL `backplane-pcb.json`
- HIL `high-speed-pcb.json`
- APT `pcb-drilling.json`
- APT `pcb-impedance-control.json`

Existing fact cards:

- `press-fit-and-backplane-integration-posture`
- `pcba-mixed-technology-assembly-flow`
- `pcba-bom-sourcing-and-traceability-posture`
- `pcba-box-build-system-integration-posture`
- `pcba-npi-to-mass-production-gates`
- `pcba-stencil-selective-solder-and-fine-pitch-controls`
- `pcba-cable-harness-and-ic-programming-integration`

Likely cards:

- `large-format-backplane-handling-posture`
- `connector-zone hole-control and plating review`

## Prioritized Candidate Queue

### Batch A

- `backdrill-control-capability`
- `cavity-machining-capability`

### Batch B

- `finish-zoning-by-assembly-sequence-and-storage-exposure`
- `press-fit-finish-selection`

### Batch C

- `press-fit-and-backplane-integration-posture`
- `advanced-validation-scope-segmentation`

### Batch D

- `large-format-backplane-handling-posture`
- `coupon-planning-and-correlation-posture`

### Batch E

- `pcba-quality-gates-and-test-strategy` wiki aggregation
- `pcba-npi-to-mass-production-flow` wiki aggregation
- `advanced-pcb-fabrication-and-stackup-planning` wiki aggregation
- `internal-material-family-coverage-and-refresh-rules` wiki aggregation

## Notes

- `APT antenna-pcb` 是新增的高价值内部源，尤其适合支撑 cavity / selective finish / launch planning。
- `APT pcb-drilling` 与 `APT/HIL backplane` 组合后，已经足够支撑一个内部 `backdrill control` 能力卡。
- 多语言镜像页面暂不重复登记，除非英文页缺失关键信息。
- P4-02 后，英文非博客 JSON 的主干数据已经足够进入新一轮 wiki 聚合；下一步不应继续无限补 source，而应先把 PCBA / advanced fabrication / material coverage 上卷成可消费主题页。
