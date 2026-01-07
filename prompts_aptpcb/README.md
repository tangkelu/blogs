# prompts_aptpcb

- 目标：针对 aptpcb.com 的批量博客提示词库，基于现有 prompts 迁移品牌/内链，同时加入 aptpcb_urls.md 提供的路由。
- 品牌：文案中统一使用 “APTPCB”，CTA 按下方片段，旧的 APTPCB/域名已替换为 aptpcb.com。
- 历史版本：`_legacy/blogs_prompt_v1` ~ `_legacy/blogs_prompt_v4` 为归档模板，默认不再用于新站批量生成。
- Query/Pillar 导向：`blogs_prompt_v5` 将模板收敛为 Query（查询意图页）与 Pillar（体系化指南页）两类，用于降低重复率与提升 SERP 结构一致性。
- Query/Pillar 导向：`blogs_prompt_v5` 将模板收敛为 Query（查询意图页）与 Pillar（体系化指南页）两类，用于降低重复率与提升 SERP 结构一致性。
- 内链池：统一参考 `prompts_aptpcb/internal_link_pool.md`，所有模板的“内链策略”区块应使用该链接池，可按主题挑选 3–6 个。
- 路由来源：以 `aptpcb_sitemap.xml` 为主（当前站点可索引 URL 清单）；用 `scripts/sync_aptpcb_from_sitemap.py` 同步生成 `aptpcb_urls.md` 与 `prompts_aptpcb/internal_link_pool.md`。

## CTA（固定按钮）

```html
<!-- COMPONENT: BlogQuickQuoteInline -->
```

## 使用建议
- 选择合适版本：v1/v2/v3 保持行业/方案导向；v4 为教育科普向，可优先用于新站冷启动的长尾覆盖。
- 运行脚本时将 prompt 目录指向 `prompts_aptpcb/<version>`，避免与原 APTPCB prompts 混用。
- 生成后复核内链是否命中当前站点路由（参考 `prompts_aptpcb/internal_link_pool.md`），必要时按专题精简到 3–6 个链接。
- 若需要新增专题，优先在 `blogs_prompt_v5` 中新增关键词（Query/Pillar 两类模板共用），避免大量复制模板造成维护成本与重复率上升。
