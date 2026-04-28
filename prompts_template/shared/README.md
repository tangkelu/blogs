# Shared Prompt Base

这里放跨站点共用的方法论、模板骨架和数据标准，不绑定 HILPCB 或 APTPCB 的具体站点路径。

## 共享层应该包含什么

- `query.md` 与 `pillar.md` 两个主骨架
- 技术博客统一标准
- 博客分析 / 重写 / 生成前的数据缺口契约
- 博客评估 rubric
- 模板保留 / 裁剪规则
- 关键词集群设计标准
- 数据组织标准
- 证据包模板
- 参数事实库标准
- 行业头部博客分析
- 旧 prompt 目录清理方案
- 竞品关键词来源标准

## 共享层不应该包含什么

- 某个站点的产品 / 服务 URL
- 某个站点的 capability 口径
- 某个站点的内链分发比例
- 某个站点特有的商业承接路径

这些内容统一放到：

- `../hilpcb/`
- `../aptpcb/`

## 建议阅读顺序

1. `technical-blog-standard.md`
2. `blog-rewrite-data-gap-contract.md`
3. `blog-evaluation-rubric.md`
4. `template-selection-and-pruning.md`
5. `keyword-cluster-design-standard.md`
6. `data-organization-standard.md`
7. `evidence-pack-template.md`
8. `evidence-pack-consumption-contract.md`
9. `query.md` 或 `pillar.md`
10. `fact-seed-repository-standard.md`
11. `legacy-prompt-directory-cleanup-plan.md`
12. `competitive-keyword-source-standard.md`

## 新增共享资产

为承接旧 prompt 目录中仍有价值的“数据标准类资产”，本目录额外保留：

- `fact-seed-repository-standard.md`
- `fact-seed-repository-template.csv`

它们用于约束参数口径、来源引用、版本控制和 `DATA_GAP` 行为，不替代 `evidence-pack-template.md`，而是作为 evidence-first 体系的参数底座。

另新增：

- `evidence-pack-consumption-contract.md`
- `blog-rewrite-data-gap-contract.md`

它用于约束模板如何消费 evidence pack，尤其是 `verified / framing_only / blocked / must_refresh / supplier_scoped_dated_only` 的处理方式，以及缺失证据时的 `DATA_GAP` 行为。

`blog-rewrite-data-gap-contract.md` 用于约束博客分析、重写、生成前的强制流程：先分析博客 / 主题关键点，再检查 `llm_wiki` 是否足够支撑顶尖稿；缺数据先补 source / fact / wiki / gate，再重写或生成博客，最后做内部泄漏、高风险 claim、组件、FAQ、审核署名和格式检查。
