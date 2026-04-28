# HILPCB Pillar Overlay

把本文件叠加到 `../shared/pillar.md` 上使用。

## HILPCB Pillar 内容职责

- 主题枢纽页负责建立行业权威
- 中段优先承接到 HILPCB 产品页与服务页
- FAQ 与结尾允许加入工具页和报价页

## 推荐内链分布

- 总内链 `5-8` 个
- 产品页 / 服务页 / 工具页至少 `3-4` 个
- 强相关博客最多 `2-3` 个

## 内置报价组件

HILPCB pillar 博客必须包含内置快速报价组件：

```html
<!-- COMPONENT: BlogQuickQuoteInline -->
```

放置规则：

- 每篇至少插入 `1` 个；长文、材料 / stackup / manufacturing / capability 枢纽页建议插入 `2` 个。
- 优先放在中部或中下部：总览表、决策矩阵、材料/工艺路线表之后；或放在 FAQ / 下一步之前。
- 如果旧结构已经在首段附近放了组件，正文中下部仍应至少保留一个组件，用来承接 RFQ 或工程评审动作。
- 组件必须单独成行，不能放进 frontmatter、表格、FAQ 包裹、代码块或引用块里。
- 组件前后的正文要说明读者应该准备哪些工程输入，例如 stackup、Gerber、BOM、阻抗、材料、装配或验证要求。

## 适合优先做强的枢纽主题

- High-Speed / Impedance
- HDI / Microvia
- Rigid-Flex / Flex Reliability
- PCBA / Assembly Quality
- Materials / Surface Finish / Thermal
