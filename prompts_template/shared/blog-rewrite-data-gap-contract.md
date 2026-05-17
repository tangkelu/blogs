# Blog Rewrite Data-Gap Contract

本契约用于所有博客分析、重写、生成任务。默认适用于 `query.md`、`pillar.md`、HILPCB overlay、APTPCB overlay，以及任何基于 `prompts_template/` 执行的博客工作。

核心原则：

> 不先盲目写作。先判断现有博客或目标主题是否具备顶尖稿所需的数据支撑；缺数据先补内部证据库，再重写或生成。

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
| `needs_data` | 关键事实、来源、判断框架不足 | 必须先补内部证据库 |
| `hold` | 缺口涉及高风险 claim，当前不能安全降级 | 暂停生成，改写范围或补强来源 |

补充硬判定：

- 如果现有证据只能支撑“方法边界、流程位置、泛化选型姿态”，但不足以支撑更厚的工程检查表、选择框架、参数语境、验证动作或 buyer / engineer checklist，不得把该主题判成 `ready`。
- 如果成稿预期会明显偏薄，或只能靠大量定性句子维持结构完整，应直接判为 `safe_but_generic` 或 `needs_data`，不得先写一个“安全版”再算完成。
- `safe_but_generic` 不是可发布状态，只是缺口已识别但尚未补齐的中间状态。

### 2. 检查内部证据库是否有支撑

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

硬规则：

- 默认先用 `llm_wiki`，不先直接查外部网络或临时搜索结果。
- 默认先用 `rg` 对 `llm_wiki/sources/registry/`、`llm_wiki/facts/`、`llm_wiki/wiki/`、相关 `llm_wiki/logs/` 做本地关键词检索；主题主词、同义词、标准号、材料名、工艺名、失败模式词都应纳入检索式。只有当前环境没有 `rg` 时才回退到 `grep`。
- 默认先把主题归到一个主 `failure mechanism family`，并优先打开 `llm_wiki/wiki/processes/blog-failure-pattern-mechanism-family-map.md`；如果没有完成这一步，就不应开始判断 `ready`。
- 如果主题涉及 `test / ICT / fixture / probe / DFT / assembly stress`，失败模式词默认还要包含 `probe load`、`board flex`、`mechanical strain`、`strain relief`、`micro-crack`、`latent damage`、`open solder joint`、`MLCC`、`hidden joint` 等物理机制词；如果这些词本地无命中，通常不能判成 `ready`。
- 如果本地知识库已经有足够支撑，必须直接消费本地卡片和主题页，不要跳过。
- 只有当 `llm_wiki` 明确缺少当前文章关键事实时，才进入外部来源补充。
- “当前文章关键事实”不只指有没有基础定义，也包括能否支撑顶尖稿所需的厚度：工程审查表、决策矩阵、参数边界、验证步骤、检查项、常见误判与 non-claims。
- 如果 `llm_wiki` 只能支撑一篇保守薄稿，而不能支撑顶尖稿，应视为“明确缺少关键事实”，必须进入外部来源补充。
- 在真正写正文前，必须先明确列出本次要消费的 `fact_id`、`wiki` 页面、对应本地 `rg` 命中路径或等价检索结果，以及仍然缺失、需要去官方补源的点；如果这份消费清单为空，或只有泛泛的 source record 名称，没有对应 fact/wiki 消费路径，视为流程未执行到位。
- 这份消费清单默认还必须写出：当前主题的主 `failure mechanism family` 是什么，为什么是它，以及为它准备了哪些本地机制词命中。
- 如果执行中只是“看过一些本地卡片”，但正文没有明显消费这些卡片的检查项、边界、失效模式或工程动作，也视为没有真正使用 `llm_wiki`。
- 如果文章讨论的是 `test / ICT / fixture / probe / DFT`，但消费清单里只有 `method identity`、`stage boundary`、`release posture`，没有 `physical failure pattern` 或 `mechanical strain` 类消费路径，也应视为未执行到位。
- 如果文章属于 `SI / stackup / thermal / assembly / coating / quote-package` 这类主题，但消费清单没有落到对应机制族，例如 `return path collapse`、`heat path`、`process window`、`surface condition`、`data-package incompleteness`，也应视为未执行到位。

### 3. 缺数据时先补数据

如果关键点没有足够支撑，必须先补内部证据库，而不是用常识或旧稿硬写。

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

外部补充触发条件：

- 文章核心 H2 只能写成泛化定义，无法展开成有信息密度的工程章节
- 关键表格只能写成空泛判断，无法形成真正可执行的 review / selection / validation 结构
- FAQ 只能重复常识，无法回答读者真正的项目决策问题
- 标题、description、目录或早期摘要的 promise 无法靠现有 `llm_wiki` 兑现到足够深度
- 文章主题天然依赖标准、方法、设备、测试、材料或工艺的公开官方解释，而本地知识库只有片段化 framing

补完后必须回写：

- 外部补到的 source registry card、fact card、topic wiki page、gate 或 readiness note，必须先落回 `llm_wiki`
- 不允许“外部查到了，但没回写知识库，就直接写博客”
- 不允许“先用外部搜索把博客写厚，回头再考虑要不要补知识库”

### 4. 再重写或生成博客

只有在数据缺口处理后，才能写正文。

重写或生成时必须消费新增数据：

- 新增 fact / gate 中的关键检查项要进入正文
- 新增 non-claims 要体现在边界表、FAQ 或删减动作中
- 不允许补了数据但正文仍停留在泛泛解释
- 如果新增数据没有明显提升标题兑现度、表格密度、章节判断力和 FAQ 含金量，说明补数没有真正被消费，不能算完成
- 去空泛不等于去结构；如果 source-backed 内容已经足够支撑决策表、检查表、门控表、边界表或 FAQ，就不能只因为压缩篇幅而把这些高价值结构块删掉
- 如果文章比前稿明显变短，必须额外检查：删掉的是重复空话，还是删掉了真正帮助工程决策的结构化信息；后者不允许直接通过
- 如果文章被收敛到更保守的 claim 边界，仍然必须保留足够的信息密度，不能退化成只有抽象判断的大纲式骨架
- 对 `SI`、`DFM`、`validation`、`stackup`、`materials`、`cost`、`lead time`、`reliability`、`connector / launch` 这类主题，若正文缺少具体工程卡点、典型失效模式、常见 EQ 触发点、评审暂停点或 release burden 说明，应判为未完成
- 安全降级后的正文，至少还应保留以下内容中的 `2` 类：典型工程场景、失败模式与排查链路、结构化 trade-off、评审冻结点、供应商沟通动作、验证分层动作；否则默认属于 `safe_but_generic`
- 如果主体段落大多可以通过替换主题词继续适用于多个相邻主题，说明正文仍停留在通用词替换层，应继续补特异性机制、典型失效模式或工程暂停点
- 如果 FAQ 主要由防御性免责声明组成，而没有解决实际工程追问，也应判为未完成

目标不是“结构完整”，而是：

- 有工程审查价值
- 有具体选择逻辑
- 有读者可执行的检查表或资料清单
- 有安全的商业承接
- 不暴露内部数据层、prompt、workflow、仓库路径或内部证据库名称
- 不暴露内部思考过程、作者推理痕迹或“为什么这样写”的元叙述
- 即使删除了高风险数值，也仍然有足够“工程血肉”，能让读者理解为什么这个主题会卡住设计、报价、试产或放行

### 5. 最后做发布前验证

公开博客输出前必须检查：

- 内部泄漏：`llm_wiki`、`evidence pack`、`source layer`、`local evidence layer`、`working prompt`、`prompt`、`workflow`、`internal`、`repo`、`knowledge base`、内部路径、template、`DATA_GAP`、`framing_only`、`blocked` 等不得出现
- 思考过程泄漏：`analysis`、`reasoning`、`chain-of-thought`、`my logic`、`I chose this because`、`based on the prompt`、`according to the template` 等作者侧元叙述不得出现
- 引用格式：最终博客不得使用 Markdown 脚注语法，例如 `[^1]`、`[^validation]`；如需归因，只能使用正文内联来源句柄或括号式说明
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
3. 先去官方来源补齐缺口，并把 source / fact / wiki / gate 回写到 `llm_wiki`。
4. 用补齐后的数据重写同一篇，做成质量标杆。
5. 再把这个标杆策略推广到同类博客。
