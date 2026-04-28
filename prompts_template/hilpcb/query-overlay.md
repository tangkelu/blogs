# HILPCB Query Overlay

把本文件叠加到 `../shared/query.md` 上使用。

## 站点承接优先级

1. `products/`
2. `services/`
3. `tools/`
4. `blog/`
5. `quote/`

## 内链策略

- 单篇建议 `4-6` 个内链
- 至少 `2` 个直达产品页或服务页
- 中段优先落：
  - `high-speed-pcb`
  - `hdi-pcb`
  - `rigid-flex-pcb`
  - `turnkey-assembly`
  - `smt-assembly`
  - `pcb-prototype`
  - `quick-turn-pcb`
  - `pcb-surface-finish`
  - `impedance-calculator`

## 口径要求

- 不要把 HILPCB 的公开产品页描述直接写成行业统一标准
- 商业承接要自然嵌入工程动作
- 比起博客互链，更优先把流量送到产品 / 服务 / 工具页

## 内置报价组件

HILPCB 博客必须包含内置快速报价组件：

```html
<!-- COMPONENT: BlogQuickQuoteInline -->
```

放置规则：

- 每篇至少插入 `1` 个；长文、参数密集型文章、材料 / stackup / capability / manufacturing 文章可插入 `2` 个。
- 优先放在中部或中下部：第一张早期规则表、关键路线表、材料/stackup 判断表之后；或放在 FAQ / 下一步之前。
- 不要只放在首段之前；如果沿用旧稿首段组件，正文中下部仍应至少有一个承接工程动作的组件。
- 组件必须单独成行，不能放进 frontmatter、表格、FAQ 包裹、代码块或引用块里。
- 组件前后的正文要自然说明读者应该准备 stackup、Gerber、BOM、阻抗、材料或验证要求，不能把组件当作纯广告横幅。
