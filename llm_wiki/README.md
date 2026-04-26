# PCB / PCBA LLM Wiki

本目录承载博客生产上游的 `真实数据层`，不直接承载博客成稿。

它与 `prompts_template/` 的关系是：

- `llm_wiki/` 负责真实数据、来源治理、事实卡片、主题 wiki
- `prompts_template/` 负责博客写作执行、证据包组装、结构化产出

换句话说：

- 先建设 `llm_wiki/`
- 再由 `prompts_template/` 消费这些数据

## 目录结构

- `sources/`
- `facts/`
- `wiki/`
- `policies/`
- `logs/`
- `ROADMAP.md`

## 每层的职责

### `sources/`

存放外部真实数据源登记，不直接写博客结论。

这里记录：

- 来源标题
- 组织
- 官网 URL
- 来源类型
- 发布时间
- 最近核查时间
- 稳定性
- 是否必须实时刷新

### `facts/`

存放原子事实卡片。

每张卡片只表达一个清晰主题，例如：

- 某个材料家族的关键参数
- 某个测试方法的适用边界
- 某项法规的合规逻辑

### `wiki/`

存放主题聚合页。

主题页不是营销成稿，而是把同一主题下的：

- 定义
- 稳定事实
- 工程判断边界
- 常见误区
- 仍需实时查询的点

组织成可维护的知识页。

### `policies/`

存放写库规则。

例如：

- 来源分级
- 更新时间策略
- 冲突处理规则
- 动态数据禁写规则
- internal capability taxonomy

### `logs/`

记录 ingest / update / lint / review 行为。

## 工作原则

1. 优先官方、标准、原厂、监管源，不优先博客。
2. 每条事实都要能追溯到来源。
3. 数值必须带测试方法、条件或频率。
4. 动态信息必须标记 `must_refresh: true`。
5. 主题 wiki 只能汇总事实，不能替代来源。
6. 博客写作时若缺乏稳定主源，应明确提示以官网实时查询为准。

## 推荐工作流

1. 在 `sources/registry/` 新增来源记录
2. 在 `facts/` 提取原子事实卡片
3. 在 `wiki/` 建立主题聚合页
4. 在 `logs/` 记录新增或变更
5. 在博客写作时由 `prompts_template/` 调用这些事实

## 规划与推进

- `ROADMAP.md` 定义长期阶段和执行顺序
- `logs/phase-status.md` 记录当前阶段状态
- `logs/backlog.md` 记录当前批次、下一批和排队项
- `policies/internal-capability-taxonomy.md` 定义内部能力类 facts 的归类与聚合边界

## 当前进度

- 当前阶段：`Phase 4`
- 当前主线：`P4-13 High Numeric Density Readiness Program`
- 当前焦点：`H2` 治理收口后的 `20-layer / 22-layer` blocker reduction，先继续压缩 blocked drafts 的 overclaim surface，再考虑任何 `P4-06` bridge

当前已完成的阶段性结果：

- `H1 Material Numeric Coverage` 已完成
- `H2` kickoff governance 已完成：
  - `logs/h2-capability-number-policy.md`
  - `logs/h2-capability-number-inventory.md`
  - `logs/h2-dated-capability-source-schema.md`
- `H2` 已完成第一波和第二波 capability bucket intake：
  - `impedance_tolerance`
  - `trace_space`
  - `drill_and_via_geometry`
  - `aspect_ratio`
  - `backdrill_and_stub`
  - `registration`
  - `board_thickness`
- held buckets 已进入显式治理：
  - `annular_ring`
  - `copper_plating_process_windows`
  - `stackup_recipe_and_process_count_numbers`
- `copper_plating_process_windows` 这一簇当前 child split 已补齐：
  - `copper_weight_capability`
  - `plating_thickness_build_allowance`
  - `etch_compensation`
  - `resin_fill_balance_heavy_copper_process_claims`
  - `standards_minima`
  - `recipe_process_window_leakage`
- `P4-13` blocker reduction 已完成两轮细分：
  - `22-layer` acceptance / listing / lot-conformance split
  - `20-layer` reliability / recipe / method-vs-qualification split
- `P4-13` post-split reassessment 已固定下一顺位：
  - `22-layer` threshold-boundary control
  - `20-layer` geometry / capability containment

当前要特别注意：

- 上述 `H2` 进展大多仍是 governance-only 或 containment-only，不代表数字已经解锁
- `copper_plating_process_windows` child split 完成，只代表 taxonomy 和边界补齐，不代表可直接写 capability tables
- `P4-06 Evidence-Pack Bridge To Prompt Templates` 仍未开启
- `20-layer` 与 `22-layer` 相关 blocker 仍未解除前，不应把高数字密度博客写作视为 ready

建议把以下文件当作当前总入口：

- `logs/phase-status.md`
- `logs/backlog.md`
- `logs/update-log.md`

## 初始范围

先覆盖以下主题：

- 材料
- 工艺能力
- 测试与检验
- 标准与规范
- 合规与法规
- 高频 / 高速 / RF 相关基础事实

暂不在这里存放：

- 竞品博客全文
- 成稿博客正文
- 无法追溯出处的行业传闻
- 未标日期的动态市场数字
