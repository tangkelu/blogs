# APTPCB Site Overlay

这里放 APTPCB 专属的提示词覆盖层与站点策略。

适用站点：

- `https://aptpcb.com`

站点结构重点：

- `pcb/`
- `pcba/`
- `capabilities/`
- `materials/`
- `industries/`
- `resources/`
- `tools/`
- `quote/`

建议使用顺序：

1. 先读 `../shared/technical-blog-standard.md`
2. 再读：
   - `../shared/template-selection-and-pruning.md`
   - `../shared/keyword-cluster-design-standard.md`
   - `../shared/data-organization-standard.md`
3. 用 `../shared/query.md` 或 `../shared/pillar.md`
4. 再叠加本目录的：
   - `query-overlay.md`
   - `pillar-overlay.md`
   - `internal-link-strategy.md`
   - `internal-link-pool.md`
   - `site-content-map.md`
   - `legacy-keyword-content-map.md`（仅当你在整理历史关键词资产时）
   - `assets-image-catalog.md`（仅当你需要站内图片索引时）

## APTPCB 站点层职责

APTPCB overlay 主要负责：

- 把 shared 骨架映射到 `pcb/`、`pcba/`、`materials/`、`capabilities/`、`industries/`
- 规定内链优先级和分发比例
- 把技术内容自然导向 RFQ、DFM、材料选择、制造能力确认

它不负责：

- 决定文章是 `query` 还是 `pillar`
- 规定哪些章节必须强制出现
- 替代 evidence pack

## 从旧目录吸收的保留资产

APTPCB 旧 prompt 目录中，仍有少量资产值得保留，但不再作为执行模板：

- `legacy-keyword-content-map.md`
  用于参考历史关键词与文件名映射
- `assets-image-catalog.md`
  用于参考站内已有图片素材

旧版 `blogs_prompt_v5/v6`、`plan_templates/`、`_legacy/` 目录后续都应视为归档，而不是生产入口。
