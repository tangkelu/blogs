# LLM Wiki Roadmap

Last updated: 2026-04-24

## Objective

把 `/code/blogs/llm_wiki/` 建成博客生产上游的 `真实数据层`，让后续写作优先消费：

- 可追溯的官方来源
- 条件明确的工程事实
- 与你们自身公开能力相匹配的内部支持层

不把它做成“素材堆”，而是做成可持续扩展、可复核、可被 prompt 消费的知识底座。

## Operating Rules

1. 先做结构化真实数据，再做博客消费层扩展。
2. 先补官方主源空白，再补内部能力映射，不以博客为主源。
3. 每一批新增都要同时更新：
   - `sources/registry/`
   - `facts/`
   - `logs/update-log.md`
4. 新主题进入 wiki 前，至少先有主源记录和原子事实卡片。
5. 动态内容只记录“查询规则”和“刷新要求”，不固化为长期静态事实。

## Phase Plan

## Phase 1: Foundation And Inventory

Goal:
把当前已建设内容盘点清楚，建立长期推进机制，而不是继续零散累加。

Scope:

- 固化 roadmap / phase status / backlog
- 盘点已覆盖主题、来源层级、明显缺口
- 明确下一阶段优先队列

Done when:

- 有明确阶段状态文件
- 有可执行 backlog
- 每个后续批次都能按优先级推进

## Phase 2: Internal Capability Layer Completion

Goal:
把 `frontendHIL` 和 `frontendAPT` 非博客内容中可复用的 PCB / PCBA 能力陈述系统化沉淀下来。

Scope:

- 高频 / 混压混材 / 表面处理 / 验证能力
- 制程限制、设计配合点、典型应用边界
- 内部公开能力与官方材料事实的映射关系

Priority themes:

- stackup strategy
- RF / microwave fabrication support
- finish zoning and mixed-finish strategy
- cavity / backdrill / controlled-depth process support
- validation and inspection framing

Done when:

- 核心内部能力都有独立 fact cards
- 内部 source registry 覆盖主要非博客产品/能力页
- 主题 wiki 可以清楚区分“官方材料事实”和“内部制造支持”

## Phase 3: Official Source Expansion

Goal:
把当前材料与工艺知识从 Rogers/MEGTRON/Ventec/AGC 扩展到更完整的高频高速主源集合。

Scope:

- 高频 / 高速 laminate family 扩展
- 表面处理与工艺标准元数据补强
- 合规与标准 revision refresh 机制

Priority themes:

- Taconic official-source coverage
- more Isola / Panasonic / Ventec family depth where needed
- IPC finish-standard metadata where public revision anchors are available
- additional regulatory / standards metadata that affects blog truthfulness

Done when:

- 材料选型类 wiki 不再只依赖少数家族
- 高频材料主源覆盖形成可比较矩阵
- 标准/法规类事实具备稳定刷新机制

## Phase 4: Topic Wiki Expansion

Goal:
从原子事实上卷成真正可消费的主题知识页。

Scope:

- material family wiki
- process decision wiki
- compliance decision wiki
- RF / high-speed selection wiki

Done when:

- 重要主题都有聚合页
- 每页都明确 stable facts / limits / must-refresh points
- prompt 层可以直接按 topic 调用证据包

## Phase 5: Prompt Consumption And Evidence Packs

Goal:
让 `prompts_template/` 稳定消费 `llm_wiki/`，用于博客写作、重写、对比和事实核对。

Scope:

- topic-level evidence-pack conventions
- blog drafting guardrails
- pre-publish refresh checklist for dynamic claims

Done when:

- 写博客不再靠人工临时找数据
- prompt 模板可直接引用 wiki facts / wiki pages / must-refresh instructions

## Execution Order

当前执行顺序固定为：

1. Phase 1 收口
2. Phase 2 内部能力层补齐
3. Phase 3 官方主源扩展
4. Phase 4 主题 wiki 扩展
5. Phase 5 prompt 消费接线

除非你重新改优先级，否则后续按这个顺序推进。

## Batch Size

每一批建议控制在一个可审查单元内：

- `2-5` 个 source records
- `2-6` 个 fact cards
- `0-2` 个 topic wiki pages

这样便于核查来源、控制命名一致性、减少一次性堆太多半成品。

Exception:

- 对 `frontendAPT` / `frontendHIL` 这类已确认范围的内部 JSON densification 批次，可以一次性登记较多 source records
- 但仍必须把事实层压缩成少量聚合 fact cards，避免把 wiki 变成页面摘要堆
- 完成后必须跑 source-id 引用检查，并在 backlog 中明确下一步上卷 wiki，而不是继续无限补卡

## Parallel Delivery Pattern

当一个批次可以拆成互不冲突的主题时，优先使用多 sub-agent 并行推进：

- 主 agent 负责规划、分工、最终审查、logs / backlog / phase-status 更新
- sub-agent 只负责一个明确文件或一个明确来源家族
- sub-agent 不修改全局追踪文件，避免多个 worker 同时改 `logs/`
- 每个 sub-agent 输出必须说明 changed files 和 residual risks
- 主 agent 最终统一核对来源边界、计数和下一步计划

## Quality Gates

每批完成前检查：

1. 来源是否为官方主源或明确标成 internal support
2. 数值是否保留方法/频率/条件
3. 是否错误把动态信息写成静态事实
4. 是否在 `limits` 中说明不能直接断言的部分
5. 是否更新 `update-log` 和 `phase-status`

## Current Focus

当前 focus 固定为：

- Phase 2 内部能力层已完成收口
- Phase 3 官方主源扩展已完成第一轮
- Phase 4 topic wiki expansion 已启动
- 当前第一批 `P4-01 Topic Wiki Expansion` 已完成三张聚合页：`high-speed-material-family-selection`、`rf-material-selector-by-application-band`、`finish-zoning-and-selective-multi-finish`
- `P4-02 Internal JSON Densification` 已补齐 APT/HIL 英文非博客 JSON 的 PCBA、PCB 制造能力、材料页主干来源和聚合 facts
- `P4-03 Topic Wiki Aggregation For PCBA And Advanced Fabrication` 已把 PCBA、advanced fabrication、internal material coverage 上卷成可消费主题页
- `P4-04 Prompt Consumption Bridge Planning` 已完成博客 readiness 抽样
- `P4-05 External Source Gap Fill From Blog Readiness` 已补第一批博客抽样暴露的外部主源缺口
- 下一批进入 `P4-06 Evidence-Pack Bridge To Prompt Templates`，为 Phase 5 evidence-pack 接线做准备
- 后续批次继续使用主 agent 规划和审核、sub-agent 分主题页或分来源家族并行交付
- 暂不把“行业博客采集”作为主任务
