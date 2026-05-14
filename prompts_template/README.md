# PCB Blog Prompt Templates

本目录是后续博客生产的唯一执行目录，结构固定为：

- `shared/`
- `hilpcb/`
- `aptpcb/`

## 核心执行入口

后续只保留两种主模板：

- `shared/query.md`
- `shared/pillar.md`

这两个文件现在都是可直接执行的生产提示词，不再只是说明文档。

其他旧写法不再作为一级主模板：

- `playbook` 只保留为采购 / RFQ / 验收模块能力
- `story` 只保留为少量品牌叙事型专题参考
- `comparison` / `application` / `capability` 只作为按意图加载的模块

## 标准执行顺序

1. 先读 `shared/technical-blog-standard.md`
2. 再读 `shared/blog-rewrite-data-gap-contract.md`，先分析博客 / 主题关键点，判断是否需要补内部证据库
3. 先到 `../llm_wiki/` 检查现有 `sources/registry/`、`facts/`、`wiki/` 是否已覆盖当前主题；默认先消费本地知识库，不先直接查外部网络
3.1 本地检索默认使用 `rg`（ripgrep），先扫主题主词、同义词、标准号、材料名、工艺名、失败模式词，再收敛到要消费的 `fact_id`、`wiki` 页面和 gate；只有当前环境没有 `rg` 时才回退到 `grep`
4. 如果本地知识库只能支撑“安全但薄”的文章，而不能支撑顶尖稿所需的工程深度、检查表、决策矩阵、验证动作和 FAQ 含金量，也视为缺少关键事实
5. 只有当 `llm_wiki` 缺少支撑当前标题、description、H2、表格、FAQ 所需的关键事实时，才允许补外部来源；补完后必须先写回 `llm_wiki`，再继续正文
6. 再读 `shared/template-selection-and-pruning.md`，判断使用 `query` 还是 `pillar`
7. 用 `shared/evidence-pack-template.md` 准备 facts / judgments / 禁写边界
8. 选择目标站点 overlay
9. 按站点内链策略分配产品页、服务页、工具页、次级博客页
10. 如需数字型参数，先检查 `shared/fact-seed-repository-standard.md`
11. 对 `SI / DFM / assembly / validation / stackup / materials / reliability / thermal / HV isolation / connector-launch` 这类主题，先在 evidence pack 里冻结至少 `1` 条 failure pattern / EQ delay pattern，再写正文
12. 生成结尾 CTA 时，优先使用“问题场景 + 提交资料 + 工程反馈”的服务引导结构，不再默认用产品链接清单式结尾
13. 最终执行 `shared/query.md` 或 `shared/pillar.md`
14. 成稿前必须做一次“内部泄漏检查”：不得出现内部术语、内部状态词、内部工作流语言或作者思考过程

## 4 步硬流程

任何博客重写或新写，在进入正文前都必须先完成下面 4 步：

1. 先查本地 `../llm_wiki/`，优先消费已有 `sources/registry/`、`facts/`、`wiki/`、gate 和 readiness notes。
1.1 执行本地检索时，默认先用 `rg` 在 `sources/registry/`、`facts/`、`wiki/`、相关 `logs/` 中按主题词和近义词查找；`grep` 仅作 `rg` 不可用时的兼容回退。
2. 如果本地知识库不足以支撑标题、description、H2、表格、FAQ 和工程密度，再补官方公开来源；不要先跳到外部搜索。
3. 外部补到的来源、事实、主题页或 gate，必须先回写 `../llm_wiki/`；不允许“查完就直接写博客”。
4. 只有在 `llm_wiki` 已足够支撑成稿，且最小消费清单已经明确后，才允许开始正文生成。

这 4 步是硬门槛，不是建议。若本地知识库只能支撑一篇“安全但薄”的保守稿，也视为数据不足，必须先补官方来源并回写 `llm_wiki`。

## HILPCB 使用路径

执行时叠加以下文件：

- `hilpcb/query-overlay.md` 或 `hilpcb/pillar-overlay.md`
- `hilpcb/internal-link-strategy.md`
- `hilpcb/internal-link-pool.md`
- `hilpcb/site-content-map.md`

HILPCB 的内链承接优先级应持续保持：

- `products/`
- `services/`
- `tools/`
- `blog/`
- `quote/`

## APTPCB 使用路径

执行时叠加以下文件：

- `aptpcb/query-overlay.md` 或 `aptpcb/pillar-overlay.md`
- `aptpcb/internal-link-strategy.md`
- `aptpcb/internal-link-pool.md`
- `aptpcb/site-content-map.md`

APTPCB 的内链承接要优先落向：

- `pcb/`
- `pcba/`
- `capabilities/`
- `materials/`
- `industries/`
- `tools/`
- `resources/`
- `quote/`

## 推荐优先阅读

1. `shared/technical-blog-standard.md`
2. `shared/blog-rewrite-data-gap-contract.md`
3. `shared/blog-evaluation-rubric.md`
4. `shared/template-selection-and-pruning.md`
5. `shared/keyword-cluster-design-standard.md`
6. `shared/data-organization-standard.md`
7. `shared/evidence-pack-template.md`
8. `shared/fact-seed-repository-standard.md`
9. `shared/pcb-industry-top-blog-analysis.md`
10. `shared/topic-cluster-roadmap.md`
11. `shared/blogs-directory-template-harvest.md`
12. `shared/legacy-prompt-directory-cleanup-plan.md`

## 这个目录现在负责什么

- 固定博客生产时真正使用的 prompt 入口
- 固定博客分析 / 重写 / 生成前的 `分析关键点 -> 查内部证据库 -> 补数据 -> 再写作` 契约
- 固定 Query / Pillar 两套主结构
- 固定关键词集群与数据组织方法
- 固定 evidence-first 的技术博客写法
- 固定参数事实库的使用边界与版本口径
- 固定 HILPCB 与 APTPCB 的站点承接和内链方法
- 固定 failure pattern 与工程协作式 CTA 必须先在 evidence pack 中成型
- 固定“最终成稿不得暴露内部思考过程和内部术语”的红线
- 固定 AI SEO / AI 可引用性写法，包括定义型摘要、内联来源归因、公开参考资料、FAQ query phrasing、作者与审核权威信号

## 与 LLM Wiki 的边界

`prompts_template/` 是写作执行层，不是事实主库。

真实数据、来源登记、事实卡片、主题 wiki 现在统一放在：

- `../llm_wiki/`

执行博客写作时：

- 在 `prompts_template/` 里组装证据与结构
- 在内部证据库里优先读取来源、事实卡片、主题页
- 如果本地知识库只能产出保守薄稿，也算缺少关键事实；此时必须先补官方来源并回写 `../llm_wiki/`
- 只有本地知识库足够支撑顶尖稿时，才允许直接进入正文；否则必须先把新增来源 / fact / wiki 回写到 `../llm_wiki/`

对外成稿红线：

- 最终博客正文、脚注、FAQ、作者信息、review 信息、引用说明中，不得出现 `llm_wiki`、`evidence pack`、`source layer`、`local evidence layer`、`working prompt`、`prompt`、`workflow`、`internal`、`repo`、`knowledge base` 等内部执行术语
- 最终博客成稿不得使用 Markdown 脚注语法，例如 `[^1]`、`[^validation]`；如需归因，只能使用正文内联来源句柄或括号式说明
- 这些词只允许出现在内部流程文档里，不允许出现在面向站点发布的最终 Markdown 成稿里

不要把外部真实数据源登记、法规刷新记录、材料参数事实卡片继续堆回本目录。

## 兼容入口

顶层保留：

- `Query.md`
- `Pillar.md`

它们只作为旧路径兼容入口，不再承载新的细则。
