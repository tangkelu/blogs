# PCB / PCBA LLM Wiki

本目录承载博客生产上游的 `真实数据知识库`，不直接承载博客成稿。

最终目标：让写作 AI 能优先基于 `llm_wiki` 写出真实、专业、可追溯的 PCB / PCBA 博客。`llm_wiki` 应尽可能直接提供材料参数、工艺能力、制造流程、测试与检验、质量控制、标准 / 合规边界、应用场景和工程判断依据。只有当 `llm_wiki` 找不到所需数据时，才去网络上的官方网站、标准组织、监管机构或原厂资料补源，并把补到的数据沉淀回 `llm_wiki`。

它与 `prompts_template/` 的关系是：

- `llm_wiki/` 负责真实数据、来源治理、事实卡片、主题 wiki
- `prompts_template/` 负责博客写作执行、证据包组装、结构化产出

换句话说：

- 先把真实数据建设进 `llm_wiki/`
- 再由 `prompts_template/` 和写作 AI 消费这些数据
- 如果写作 AI 发现 `llm_wiki` 缺数据，应先触发官方补源和入库，而不是直接把未入库的网页内容当成长期事实层

## 目标与边界

`llm_wiki` 的目标不是只记录“能不能写”，而是沉淀可复用的真实 PCB / PCBA 知识。

应进入 `llm_wiki` 的内容包括：

- 材料真实数据：材料家族、具体牌号、Dk / Df / Tg / Td / CTE / thermal conductivity / moisture absorption 等参数，并保留测试条件、频率、方法和来源
- 工艺真实数据：HDI、microvia、VIPPO、backdrill、controlled impedance、rigid-flex、MCPCB、ceramic、PTFE、surface finish、SMT / THT / selective solder、box build 等工艺流程和边界
- 测试与质量真实数据：SPI、AOI、X-ray、ICT、FCT、FAI / FQI、NPI gates、traceability、DFM / DFT / DFA、inspection vs reliability 的边界
- 标准与合规数据：IPC、ISO、FDA、RoHS、REACH、USB-IF、MIL / aerospace / medical 等可公开引用的元数据、适用边界和 refresh 规则
- 能力边界：APT / HIL 内部公开页面或 dated capability record 能支持的能力描述，以及明确不能支持的数值、承诺和认证证明
- 写作可消费的主题聚合：把原子事实组织成可供 evidence pack 和博客 prompt 调用的 topic wiki

不应进入 `llm_wiki` 作为事实的内容包括：

- 临时草稿里的未验证数值、公式、价格、交期、良率、能力承诺、认证承诺、供应商审计结论
- 没有来源、没有日期、没有测试条件的行业传闻或泛化经验
- 把某个产品 datasheet 的数值泛化成整个材料家族的通用数值
- 把官网 marketing language 直接升级成可验证的工艺能力、质量结果或客户承诺
- 把 standards metadata 当成付费标准正文、阈值表或验收准则

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

`logs/` 可以记录临时草稿批次的 claim inventory、source gaps 和 deletion-safe snapshot，但日志本身不等于真实 fact layer。只有当数据进入 `sources/`、`facts/`、`wiki/` 并通过引用校验后，才算进入可复用知识层。

## 工作原则

1. 优先官方、标准、原厂、监管源，不优先博客。
2. 每条事实都要能追溯到来源。
3. 数值必须带测试方法、条件或频率。
4. 动态信息必须标记 `must_refresh: true`。
5. 主题 wiki 只能汇总事实，不能替代来源。
6. 博客写作时若 `llm_wiki` 缺乏稳定主源，应先补官方来源并入库；无法及时补源时，必须明确该 claim 不可写或只能写成待确认边界。
7. `tmps/` 草稿只能作为需求输入和 claim inventory，不能作为真实参数、能力、价格、认证或质量数据的来源。

## 临时草稿与完整学习

`/code/blogs/tmps/...` 下的源 md 可能最终被移除，因此每个草稿批次至少要在 `llm_wiki` 留下 deletion-safe 学习记录。

最低要求：

- 文件清单、标题、H2 / H3 结构或主题摘要
- 每篇草稿的主题意图和可复用 outline
- 草稿暴露出的 claim families
- 已有 `llm_wiki` 可支撑的数据层
- 仍缺的官方来源、产品 datasheet、标准 metadata 或 dated capability record
- 必须阻断的 claim：数值、价格、交期、良率、认证、能力、供应商证明、性能承诺等

“完整学习”不能只停留在 ingestion map。完整学习应按这个链路完成：

1. `claim inventory`：从草稿或需求中提取要写的数据类型和 claim 家族
2. `source gap`：判断 `llm_wiki` 已有数据是否足够
3. `official source recovery`：缺数据时补官方网站、标准组织、监管机构、原厂 datasheet 或 dated capability record
4. `source records`：把来源登记到 `sources/registry/`
5. `fact cards`：把可复用真实数据沉淀到 `facts/`
6. `topic wiki`：把跨卡片知识聚合到 `wiki/`
7. `prompt consumption gate`：明确写作 AI 可用、必须降级、必须排除、必须刷新或必须继续补源的内容

如果只完成第 1-2 步，该批次只能标记为 `completed_at_claim_family_level`，不能标记为真实数据完整学习。

## 官方补源规则

当写作 AI 或学习流程发现 `llm_wiki` 缺少数据时，应优先按以下顺序补源：

1. 标准组织、监管机构、认证项目的官方页面或公开 metadata
2. 材料 / 元件 / 工艺原厂 datasheet、product page、processing guide
3. APT / HIL 非博客公开页面或 dated internal capability record
4. 只有在明确标记为 secondary support 时，才使用行业文章、博客或第三方资料

## 推荐工作流

补源后必须回写到 `llm_wiki`，不能只在单次博客写作上下文里临时使用。

1. 从草稿、关键词或写作需求提取 claim inventory
2. 检查 `llm_wiki` 是否已有足够真实数据
3. 缺数据时补官方来源或 dated capability record
4. 在 `sources/registry/` 新增来源记录
5. 在 `facts/` 提取原子事实卡片
6. 在 `wiki/` 建立主题聚合页
7. 在 `logs/` 记录新增、变更、缺口和阻断项
8. 在博客写作时由 `prompts_template/` 调用这些事实

## 规划与推进

- `ROADMAP.md` 定义长期阶段和执行顺序
- `logs/phase-status.md` 记录当前阶段状态
- `logs/backlog.md` 记录当前批次、下一批和排队项
- `policies/internal-capability-taxonomy.md` 定义内部能力类 facts 的归类与聚合边界

## 当前进度

- 当前阶段：`Phase 4`
- 当前主线：`/code/blogs/tmps/*/en` 博客数据学习与官方补源
- 当前焦点：全部当前英文 `tmps/*/en` 批次已经 deletion-safe 到 claim-family / routing level；下一步不是继续证明“有没有学过”，而是把高价值 claim 通过官方来源或 dated capability record 升格为 `sources/`、`facts/`、`wiki/` 中可复用真实数据
- 下次续接入口：`logs/p4-44-blog-learning-continuation-handoff.md`

当前 tmps 博客学习结论：

- `/code/blogs/tmps` 当前有 `29` 个 dated English `*/en` 博客目录
- 这些英文博客目录都已有 deletion-safe 学习记录或 P4-33 全局 lane 覆盖，源 md 删除后不会丢失文件清单、主题意图、claim family、阻断项和下一步补源方向
- 但这不等于所有数据都已经完整升格为事实层；完整学习仍要求官方来源 / dated record、source record、fact card、topic wiki 和 prompt consumption gate
- `/code/blogs/tmps/materias_pdf` 继续暂停，除非后续明确重启
- 立即下一步是 `P4-44 November 2025 Controller Integration`：从 P4-40 已完成的四个 November 2025 scout log 中挑选可由官方来源或 dated record 支撑的内容，升格为真实数据层

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
- `H4 Current Tranche` 已完成当前控制层 closeout：
  - 当前 tranche 已 control-complete enough to pause expansion
  - 下一实际动作改为 direct conservative generation gate / prompt-consumption handoff
- 英文 layer-count generation gate 当前结论已固定：
  - `6 / 8 / 10 / 12 / 14 / 16 / 18 / 24-layer` 为 `go_now_conservative`
  - `20 / 22-layer` 仍为 `still_hold`
- `P4-06` 相关输入并非空白：
  - first-wave / second-wave evidence-pack inputs 已存在
  - 但 high-density numeric readiness 仍被 blocked，不构成 numeric unlock 或 standards-threshold unlock

当前要特别注意：

- 上述 `H2` 进展大多仍是 governance-only 或 containment-only，不代表数字已经解锁
- `copper_plating_process_windows` child split 完成，只代表 taxonomy 和边界补齐，不代表可直接写 capability tables
- `P4-06 Evidence-Pack Bridge To Prompt Templates` 不应再表述为“未开启”；当前更准确的状态是：evidence-pack 输入面已形成，但仍未跨过高数字密度 numeric readiness gate
- `20-layer` 与 `22-layer` 相关 blocker 仍未解除前，不应把高数字密度博客写作视为 ready
- 当前 closeout 不是 numeric unlock、standards-threshold unlock、supplier-proof unlock

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
