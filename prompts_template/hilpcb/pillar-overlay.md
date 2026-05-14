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

## HILPCB CTA 规则

- HILPCB 的 Pillar 页面结尾 CTA，优先写成“专题进入执行阶段时的关键卡点 + 应提交的工程资料 + 工程团队返回的 review 输出 + 公开响应时效”
- 当前可公开复用的联系邮箱是 `sales@hilpcb.com`
- 当前可公开复用的承接页是 `https://hilpcb.com/en/quote/`
- 当前可公开复用的响应表述，应以 HIL 现有公开 quote 文案为边界：
  - `Our team will contact you within 24 hours with detailed pricing and technical recommendations.`
- 对 stackup、materials、assembly、thermal、test strategy、HV isolation、高速互连、BGA / HDI 这类专题，可把 CTA 收敛成 `engineering review feedback within 24 hours`，但不要把它扩写成 fabrication completion、delivery, yield, or approval promises
- CTA 应总结该专题最常见的执行卡点
  - 例如 stackup 冻结、压合对称性、连接器过渡区几何控制、BGA 动态翘曲、测试覆盖率、隔离边界、装配热容量冲突
- 允许补充 `3-4` 个一级承接页链接，但它们应作为后续阅读路径，不应替代主 CTA
- 不要把专题页结尾写成产品目录或品牌宣传段

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

- Single / Double Layer PCB
- Low-layer FR-4 / Prototype Baseline
- High-Speed / Impedance
- HDI / Microvia
- Rigid-Flex / Flex Reliability
- PCBA / Assembly Quality
- Turnkey BOM Sourcing / PCBA Traceability
- Through-Hole / Mixed-Technology Assembly
- Volume PCBA Ramp / SPC Production
- Materials / Surface Finish / Thermal
