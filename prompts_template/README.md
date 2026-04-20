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
2. 再读 `shared/template-selection-and-pruning.md`，判断使用 `query` 还是 `pillar`
3. 用 `shared/evidence-pack-template.md` 准备 facts / judgments / 禁写边界
4. 选择目标站点 overlay
5. 按站点内链策略分配产品页、服务页、工具页、次级博客页
6. 如需数字型参数，先检查 `shared/fact-seed-repository-standard.md`
7. 最终执行 `shared/query.md` 或 `shared/pillar.md`

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
2. `shared/template-selection-and-pruning.md`
3. `shared/keyword-cluster-design-standard.md`
4. `shared/data-organization-standard.md`
5. `shared/evidence-pack-template.md`
6. `shared/fact-seed-repository-standard.md`
7. `shared/pcb-industry-top-blog-analysis.md`
8. `shared/topic-cluster-roadmap.md`
9. `shared/blogs-directory-template-harvest.md`
10. `shared/legacy-prompt-directory-cleanup-plan.md`

## 这个目录现在负责什么

- 固定博客生产时真正使用的 prompt 入口
- 固定 Query / Pillar 两套主结构
- 固定关键词集群与数据组织方法
- 固定 evidence-first 的技术博客写法
- 固定参数事实库的使用边界与版本口径
- 固定 HILPCB 与 APTPCB 的站点承接和内链方法
- 固定 AI SEO / AI 可引用性写法，包括定义型摘要、内联来源归因、公开参考资料、FAQ query phrasing、作者与审核权威信号

## 兼容入口

顶层保留：

- `Query.md`
- `Pillar.md`

它们只作为旧路径兼容入口，不再承载新的细则。
