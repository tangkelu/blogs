# Blog Rewrite Data-Gap Contract

本契约用于所有博客分析、重写、生成任务。默认适用于 `query.md`、`pillar.md`、HILPCB overlay、APTPCB overlay，以及任何基于 `prompts_template/` 执行的博客工作。

核心原则：

> 不先盲目写作。先判断现有博客或目标主题是否具备顶尖稿所需的数据支撑；缺数据先补 `llm_wiki`，再重写或生成。

## 强制执行流程

### 1. 先分析博客或主题关键点

在重写或生成正文前，必须先拆出文章要成立的关键点：

- 核心搜索意图
- 读者要做的工程决策
- 必须解释清楚的技术概念
- 必须出现的判断表、检查表或选择框架
- 需要的材料、工艺、测试、标准、参数或应用语境
- 需要承接到站点产品页、服务页、工具页或 quote 的动作
- 明确不能写入的 claim classes

如果是现有博客重写，还要先给出质量状态：

| 状态 | 含义 | 下一步 |
| --- | --- | --- |
| `ready` | 已有数据足够支撑顶尖稿 | 可以直接重写 / 生成 |
| `safe_but_generic` | 安全但泛泛，缺少工程审查价值 | 先补数据或 gate，再重写 |
| `needs_data` | 关键事实、来源、判断框架不足 | 必须先补 `llm_wiki` |
| `hold` | 缺口涉及高风险 claim，当前不能安全降级 | 暂停生成，改写范围或补强来源 |

### 2. 检查 `llm_wiki` 是否有支撑

围绕关键点检查：

- `llm_wiki/sources/registry/`
- `llm_wiki/facts/`
- `llm_wiki/wiki/`
- `llm_wiki/policies/`
- `llm_wiki/logs/` 中对应 gate / readiness / control notes

检查目标不是“能不能写一篇安全文章”，而是：

- 能不能写出具体工程判断
- 能不能写出比泛泛说明更强的检查表或选择框架
- 能不能解释边界和 non-claims
- 能不能给出可执行的 buyer / engineer action
- 能不能支撑标题、description、H2、表格、FAQ 中的每个强承诺

### 3. 缺数据时先补数据

如果关键点没有足够支撑，必须先补 `llm_wiki`，而不是用常识或旧稿硬写。

可补类型：

- source registry card
- fact card
- topic wiki page
- rewrite / generation gate
- readiness / control note

补数据时要保持来源边界：

- 官方标准、监管机构、原厂 datasheet、官方技术文档优先
- 内部站点公开页面可作为站点能力和承接语境，不自动升级成行业事实
- 第三方技术指南可以用于保守方法解释，但不能支撑供应商能力、认证、验收、性能或数字承诺

### 4. 再重写或生成博客

只有在数据缺口处理后，才能写正文。

重写或生成时必须消费新增数据：

- 新增 fact / gate 中的关键检查项要进入正文
- 新增 non-claims 要体现在边界表、FAQ 或删减动作中
- 不允许补了数据但正文仍停留在泛泛解释

目标不是“结构完整”，而是：

- 有工程审查价值
- 有具体选择逻辑
- 有读者可执行的检查表或资料清单
- 有安全的商业承接
- 不暴露内部数据层、prompt、workflow、仓库路径或 `llm_wiki`

### 5. 最后做发布前验证

公开博客输出前必须检查：

- 内部泄漏：`llm_wiki`、内部路径、prompt、template、workflow、evidence pack、`DATA_GAP`、`framing_only`、`blocked` 等不得出现
- 高风险 claim：覆盖率、良率、成本、交期、认证、qualification、IPC 阈值、标准验收值、SI pass/fail、BER、eye-mask、jitter、insertion-loss 等不得无证据出现
- 站点组件：HILPCB 博客必须包含 `<!-- COMPONENT: BlogQuickQuoteInline -->`
- FAQ markers：需要 FAQ 时使用 `<!-- faq:start -->` 与 `<!-- faq:end -->`
- 作者和审核：只能使用公开安全实体，例如 `HILPCB Engineering Team`、`HILPCB Engineering Content Review Team`
- Markdown 格式：运行 `git diff --check` 或等价检查

## 顶尖稿判断标准

一篇博客不是因为“没有错”就算顶尖。顶尖稿至少满足：

- 标题承诺和正文兑现一致
- 顶部答案能独立回答搜索意图
- 关键表格不是装饰，而能帮助工程选择
- 技术边界清楚，知道什么不能证明
- 有具体设计 / 制造 / 测试 / 采购动作
- 有公开来源和安全内链承接
- 没有内部策略、证据层、提示词或审稿流程泄漏

## 推荐执行模式

对于大批博客：

1. 先抽样分析一篇代表性博客。
2. 如果是 `safe_but_generic`，不要继续批量生成。
3. 基于缺陷补 `llm_wiki`。
4. 用补齐后的数据重写同一篇，做成质量标杆。
5. 再把这个标杆策略推广到同类博客。

