# Internal Capability Taxonomy

Last updated: 2026-04-24

## Purpose

给 `llm_wiki` 内部支持层建立稳定分类，避免 methods 卡越积越多之后出现：

- 同一能力散落在不同命名下
- topic wiki 聚合边界不清
- backlog 只能按感觉推进

本 taxonomy 主要用于 `internal` 来源衍生出的工艺 / 能力类 fact cards。

## Scope

当前内部能力层统一归入五个一级桶：

1. `stackup`
2. `fabrication`
3. `finish`
4. `validation`
5. `integration`

说明：

- `category` 字段暂时仍保留为 `methods`
- 这个 taxonomy 作为二级语义层存在，用于治理、聚合和后续 wiki 编排
- P4-02 之后新增的 PCBA 和材料覆盖仍按这五个桶治理；如果一张卡描述的是“材料官方参数”，留在 `facts/materials`，如果描述的是“材料如何被内部工艺消费”，按主要用途映射到 `stackup`、`fabrication` 或 `validation`

## Taxonomy Definitions

### `stackup`

定义：

- 涉及材料组合、层叠结构、压合窗口、RF/高速混材策略

应该放这里的内容：

- hybrid material strategy
- PTFE / FR-4 stackup framing
- lamination profile and resin-flow posture
- high-layer-count stackup review logic

当前已归类卡片：

- `hybrid-rf-stackup-capability`
- `ptfe-processing-capability`
- `hdi-microvia-and-vippo-process-posture`
- `rigid-flex-stackup-and-bend-reliability-posture`
- `spread-glass-and-controlled-impedance-planning`

Planned wiki aggregation:

- `wiki/processes/hybrid-rf-stackup-strategy.md`
- `wiki/processes/ptfe-processing-and-manufacturability.md`

### `fabrication`

定义：

- 涉及钻孔、背钻、腔体、机械特征、微孔、受控深度等制程动作

应该放这里的内容：

- backdrill
- cavity machining
- microvia / controlled-depth drilling
- shield cavity and waveguide feature planning

当前已归类卡片：

- `backdrill-control-capability`
- `cavity-machining-capability`
- `high-layer-count-backdrill-and-registration-posture`
- `thermal-pcb-platform-selection-posture`
- `ic-substrate-fine-line-build-up-posture`

Planned wiki aggregation:

- `wiki/processes/rf-drilling-and-transition-control.md`
- `wiki/processes/cavity-and-shield-feature-planning.md`

### `finish`

定义：

- 涉及表面处理选择、分区、多 finish 策略、RF / press-fit / wire-bond finish 逻辑

应该放这里的内容：

- RF finish selection
- finish zoning by area / assembly path
- selective multi-finish strategy
- press-fit-related finish choice

当前已归类卡片：

- `surface-finish-selection-for-rf`
- `selective-multi-finish-strategy`
- `finish-zoning-by-assembly-sequence-and-storage-exposure`
- `press-fit-finish-selection`

Planned wiki aggregation:

- `wiki/processes/rf-surface-finish-selection.md`
- `wiki/processes/finish-zoning-and-selective-multi-finish.md`

### `validation`

定义：

- 涉及测试层级、验证深度、TDR/VNA/coupon/metrology/traceability 的组织方式

应该放这里的内容：

- RF validation posture
- advanced validation scope layering
- coupon planning and correlation
- validation-ladder logic

当前已归类卡片：

- `rf-validation-capability`
- `advanced-validation-scope-segmentation`
- `controlled-impedance-tdr-verification-posture`
- `pcba-layered-inspection-stack`
- `pcba-ict-vs-fct-boundary`
- `pcba-fai-fqi-and-traceability-gates`
- `pcba-flying-probe-test-positioning`

Planned wiki aggregation:

- `wiki/testing/rf-validation-and-test-coverage.md`
- `wiki/testing/validation-ladder-from-e-test-to-si-verification.md`

### `integration`

定义：

- 涉及跨域耦合问题，特别是连接器、backplane、assembly path、mechanical + SI 联动

应该放这里的内容：

- press-fit + backplane integration
- connector-zone review logic
- large-format handling tied to electrical outcome

当前已归类卡片：

- `press-fit-and-backplane-integration-posture`
- `pcba-mixed-technology-assembly-flow`
- `pcba-bom-sourcing-and-traceability-posture`
- `pcba-box-build-system-integration-posture`
- `pcba-npi-to-mass-production-gates`
- `pcba-stencil-selective-solder-and-fine-pitch-controls`
- `pcba-cable-harness-and-ic-programming-integration`

Planned wiki aggregation:

- `wiki/processes/backplane-execution-and-connector-integration.md`

## Cards Outside This Taxonomy

以下卡片目前不进入 internal capability taxonomy：

- `spi-aoi-ict-boundaries`

原因：

- 这张卡主要是外部主源支撑的 `inspection method boundary` 卡，不属于你们内部 capability layer
- 它后续应归到更通用的 `testing / inspection` wiki 聚合，而不是 internal support taxonomy

## Normalization Rules

新写内部 methods 卡时：

1. 先判断是否属于五个一级桶之一
2. 在卡片正文里明确它是 `internal posture`、`internal support`，还是 `integration posture`
3. 在 backlog 和 inventory 中按 taxonomy 归位
4. 如果一张卡跨两个桶，按“主要决策用途”归一个主桶，不做双归类

优先级判断：

- 如果核心在材料与层叠，归 `stackup`
- 如果核心在具体制造动作，归 `fabrication`
- 如果核心在 finish 选择，归 `finish`
- 如果核心在验证层级与证据链，归 `validation`
- 如果核心在连接器 / 系统 / 结构联动，归 `integration`

## Current Mapping Table

| Fact card | Taxonomy bucket |
| --- | --- |
| `hybrid-rf-stackup-capability` | `stackup` |
| `ptfe-processing-capability` | `stackup` |
| `backdrill-control-capability` | `fabrication` |
| `cavity-machining-capability` | `fabrication` |
| `surface-finish-selection-for-rf` | `finish` |
| `selective-multi-finish-strategy` | `finish` |
| `finish-zoning-by-assembly-sequence-and-storage-exposure` | `finish` |
| `press-fit-finish-selection` | `finish` |
| `rf-validation-capability` | `validation` |
| `advanced-validation-scope-segmentation` | `validation` |
| `press-fit-and-backplane-integration-posture` | `integration` |
| `hdi-microvia-and-vippo-process-posture` | `stackup` |
| `rigid-flex-stackup-and-bend-reliability-posture` | `stackup` |
| `spread-glass-and-controlled-impedance-planning` | `stackup` |
| `high-layer-count-backdrill-and-registration-posture` | `fabrication` |
| `thermal-pcb-platform-selection-posture` | `fabrication` |
| `ic-substrate-fine-line-build-up-posture` | `fabrication` |
| `controlled-impedance-tdr-verification-posture` | `validation` |
| `pcba-layered-inspection-stack` | `validation` |
| `pcba-ict-vs-fct-boundary` | `validation` |
| `pcba-fai-fqi-and-traceability-gates` | `validation` |
| `pcba-flying-probe-test-positioning` | `validation` |
| `pcba-mixed-technology-assembly-flow` | `integration` |
| `pcba-bom-sourcing-and-traceability-posture` | `integration` |
| `pcba-box-build-system-integration-posture` | `integration` |
| `pcba-npi-to-mass-production-gates` | `integration` |
| `pcba-stencil-selective-solder-and-fine-pitch-controls` | `integration` |
| `pcba-cable-harness-and-ic-programming-integration` | `integration` |

## Immediate Follow-On Work

After taxonomy normalization, the next work should be:

1. write topic wiki pages by bucket
2. keep adding facts only where a bucket still has structural gaps
3. avoid adding more isolated cards that have no planned aggregation target
