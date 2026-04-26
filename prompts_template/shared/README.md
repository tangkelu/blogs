# Shared Prompt Base

这里放跨站点共用的方法论、模板骨架和数据标准，不绑定 HILPCB 或 APTPCB 的具体站点路径。

## 共享层应该包含什么

- `query.md` 与 `pillar.md` 两个主骨架
- 技术博客统一标准
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
2. `blog-evaluation-rubric.md`
3. `template-selection-and-pruning.md`
4. `keyword-cluster-design-standard.md`
5. `data-organization-standard.md`
6. `evidence-pack-template.md`
7. `query.md` 或 `pillar.md`
8. `fact-seed-repository-standard.md`
9. `legacy-prompt-directory-cleanup-plan.md`
10. `competitive-keyword-source-standard.md`

## 新增共享资产

为承接旧 prompt 目录中仍有价值的“数据标准类资产”，本目录额外保留：

- `fact-seed-repository-standard.md`
- `fact-seed-repository-template.csv`

它们用于约束参数口径、来源引用、版本控制和 `DATA_GAP` 行为，不替代 `evidence-pack-template.md`，而是作为 evidence-first 体系的参数底座。
