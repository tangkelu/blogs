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
  - `single-double-layer-pcb`
  - `fr4-pcb`
  - `pcb-prototype`
  - `quick-turn-pcb`
  - `high-speed-pcb`
  - `hdi-pcb`
  - `rigid-flex-pcb`
  - `turnkey-assembly`
  - `smt-assembly`
  - `through-hole-assembly`
  - `large-volume-assembly`
  - `pcb-surface-finish`
  - `impedance-calculator`

## 低层数命中规则

- 当查询主题是 `single layer PCB`、`double layer PCB`、`2 layer PCB`、`single sided PCB`、`double sided PCB`、`simple FR-4`、`baseline prototype`、`cost-sensitive board` 时，优先落到 `products/single-double-layer-pcb`
- 当主题仍在“简单、低密度、快转样板”阶段，但强调材料而不是层数时，再考虑 `products/fr4-pcb`
- 当查询已经明显转向密度、阻抗、微孔或多层结构时，才升级到 `products/multilayer-pcb` 或 `products/hdi-pcb`
- 不要把低层数意图直接承接到博客页，除非博客页是在做问题解释或对比说明

## 高价值产品页命中规则

- `HDI / microvia / VIPPO / via-in-pad / fine-pitch BGA`：优先 `products/hdi-pcb`
- `BOM sourcing / component alternates / EOL / AVL / turnkey PCBA`：优先 `products/turnkey-assembly`
- `wave solder / selective solder / press-fit / connector / transformer / terminal / mixed THT`：优先 `products/through-hole-assembly`
- `mass production / repeat PCBA / SPC / MES traceability / volume ramp / forecast`：优先 `products/large-volume-assembly`

## 口径要求

- 不要把 HILPCB 的公开产品页描述直接写成行业统一标准
- 商业承接要自然嵌入工程动作
- 比起博客互链，更优先把流量送到产品 / 服务 / 工具页

## HILPCB CTA 规则

- HILPCB 的 Query 文章结尾 CTA，优先写成“工程痛点 + 应提交资料 + 工程团队反馈 + 公开响应时效”
- 当前可公开复用的联系邮箱是 `sales@hilpcb.com`
- 当前可公开复用的承接页是 `https://hilpcb.com/en/quote/`
- 当前可公开复用的响应表述，应以 HIL 现有公开 quote 文案为边界：
  - `Our team will contact you within 24 hours with detailed pricing and technical recommendations.`
- 当文章主题明显落在 DFM、stackup、assembly、materials、test access、thermal、high-speed、HV isolation 这类工程审查问题时，CTA 可以安全收敛成 `engineering review feedback within 24 hours`，但不要扩写成交付、产能或量产承诺
- 可以自然写入的资料类型包括：`Gerber`、`ODB++`、`stackup draft`、`BOM`、坐标文件、阻抗要求、背钻说明、材料 / finish 意图、测试要求、机械约束、应用场景
- 不要每篇都复制同一句 CTA；必须根据正文的 failure pattern 或 review burden 改写工程痛点
- 允许在主 CTA 后补 `2-4` 个相关链接，但这些链接只能作为辅助，不应盖过主 CTA

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
