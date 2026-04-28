# HILPCB Site Overlay

这里放 HILPCB 专属的提示词覆盖层与站点策略。

适用站点：

- `https://hilpcb.com`

站点结构重点：

- `products/`
- `services/`
- `tools/`
- `blog/`
- `quote/`

建议使用顺序：

1. 先读 `../shared/technical-blog-standard.md`
2. 再读 `../shared/blog-rewrite-data-gap-contract.md`，先判断现有博客 / 目标主题是否需要补 `llm_wiki`
3. 再读：
   - `../shared/template-selection-and-pruning.md`
   - `../shared/keyword-cluster-design-standard.md`
   - `../shared/data-organization-standard.md`
4. 用 `../shared/query.md` 或 `../shared/pillar.md`
5. 再叠加本目录的：
   - `query-overlay.md`
   - `pillar-overlay.md`
   - `layer-count-conservative-generation-gate.md`
   - `internal-link-strategy.md`
   - `internal-link-pool.md`
   - `site-content-map.md`

## HILPCB 站点层职责

HILPCB overlay 主要负责：

- 把 shared 骨架映射到 `products/`、`services/`、`tools/`、`blog/`
- 把技术内容优先导向产品页与服务页
- 控制内链分布，避免只在结尾堆博客互链
- 执行 HILPCB 专属组件与公开承接口径，但不跳过 shared 的数据缺口检查

它不负责：

- 决定文章是 `query` 还是 `pillar`
- 替代 evidence pack
- 把站点公开产品描述写成行业统一事实
