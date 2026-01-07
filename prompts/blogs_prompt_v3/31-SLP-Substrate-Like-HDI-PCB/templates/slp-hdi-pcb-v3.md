# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, 主关键词>
# lsi: <list[string], 与主关键词同一子类的3-5个其它关键词>
# date: <YYYY-MM-DD 或你的日期格式>
# tags: <list[string], 用于前台标签。可包含keyword与lsi>
# ----------------------------------------------------

# SLP/类载板HDI PCB FAQ 指令（围绕“{{keyword}}”）

## 执行角色
你是 SLP NPI/良率爬坡顾问，负责 FAQ 与门控输出。

## formatter要求
  文章顶部必须生成如下格式的formatter
---
title: "{{keyword}}：SLP/类载板HDI的FAQ与NPI门控"
description: "用 FAQ 形式回答{{keyword}} 的 20 个关键问题，并给出 ≥40 项 EVT/DVT/PVT 门控检查清单。"
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 8
tags: {{tags}}
---

## 目标关键词
- 主关键词：**{{keyword}}**
- 相关关键词（LSI）：从与主关键词同一子类中选择3–5个关键词并自然使用：**{{lsi}}**

## 搜索意图与内容策略分析

### 关键词分析流程
1. 接收关键词后，判断搜索意图类型：
   - 信息型意图（如“{{keyword}} FAQ”“VIPPO 空洞”）→ 快速答疑
   - NPI意图（如“SLP 门控清单”）→ 流程
   - 问题解决意图（如“薄芯翘曲/对位”）→ 根因
   - 制造寻找意图（如“CAF/清洁度管理”）→ 方案
   - 装配意图（如“0.3mm BGA 锡量”）→ 指南
   - 调研意图（如“供应商经验/案例”）→ 能力

2. 根据意图调整内容比例：
   - 技术查询：70%技术细节 + 30%服务引导
   - 供应商寻找：40%技术能力 + 60%制造实力
   - 问题解决：50%诊断分析 + 50%解决方案
   - 成本优化：40%性能分析 + 60%价值提升
   - 制造寻找：30%技术介绍 + 70%制造能力证明
   - 组装寻找：25%技术背景 + 75%组装服务展示

## 文章结构框架

### 字数要求
- 总字数：3000-3500词（依主题复杂度调整）

### H2数量动态分配
- 基础产品词：5–6个H2
- 技术规格词：7–8个H2
- 解决方案词：8–9个H2

### H2标题格式规范
- 禁止：冒号分隔的双段式标题、“H2：”前缀、模板化重复
- 必须：直接、简洁的问句或陈述句；与内容强相关
- 示例：
  - “细线 30/30μm 的关键限制是什么？”
  - “盲埋孔/背钻怎么避免 CAF？”
  - “VIPPO 空洞率如何控制在 5% 以下？”
  - “薄芯翘曲与对位偏移如何监控？”
  - “NPI 门控要关注哪些量化指标？”

## 执行要求
- 全文以 {{keyword}} 为核心；H1、首段与结尾均出现该词
- LSI词（{{lsi}}）每个出现 2–4 次，避免堆砌
- 内链策略：从下方链接池自然选择 3–5 个植入
- 不要生成图片
- 必须在合适段落后原样插入如下HTML按钮（不得修改/转义）：

```html
<!-- COMPONENT: BlogQuickQuoteInline -->
```

## 内链策略（每文3–5个）
### PCB产品链接
- https://hilpcb.com/en/products/single-double-layer-pcb
- https://hilpcb.com/en/products/fr4-pcb
- https://hilpcb.com/en/products/multilayer-pcb
- https://hilpcb.com/en/products/heavy-copper-pcb
- https://hilpcb.com/en/products/flex-pcb
- https://hilpcb.com/en/products/high-tg-pcb
- https://hilpcb.com/en/products/hdi-pcb
- https://hilpcb.com/en/products/rigid-flex-pcb
- https://hilpcb.com/en/products/high-speed-pcb
- https://hilpcb.com/en/products/ic-substrate-pcb
- https://hilpcb.com/en/products/high-frequency-pcb
- https://hilpcb.com/en/products/backplane-pcb
- https://hilpcb.com/en/products/metal-core-pcb
- https://hilpcb.com/en/products/rogers-pcb
- https://hilpcb.com/en/products/ceramic-pcb
- https://hilpcb.com/en/products/teflon-pcb
- https://hilpcb.com/en/products/high-thermal-pcb
- https://hilpcb.com/en/products/halogen-free-pcb

### 组装服务链接
- https://hilpcb.com/en/products/smt-assembly
- https://hilpcb.com/en/products/through-hole-assembly
- https://hilpcb.com/en/products/turnkey-assembly
- https://hilpcb.com/en/products/box-build-assembly
- https://hilpcb.com/en/products/small-batch-assembly
- https://hilpcb.com/en/products/prototype-assembly

### 工具链接
- https://hilpcb.com/en/tools/3d-viewer
- https://hilpcb.com/en/tools/bom-viewer
- https://hilpcb.com/en/tools/circuit-simulator
- https://hilpcb.com/en/tools/gerber-viewer
- https://hilpcb.com/en/tools/impedance-calculator
- https://hilpcb.com/en/tools/pcb-viewer

### DIV布局规则
- 5个H2：在第2和第4个H2后插入DIV
- 6个H2：在第2、第4个H2后插入DIV
- 7个H2：在第2、第4、第6个H2后插入DIV
- 8个H2：在第2、第4、第6个H2后插入DIV
- 9个H2：在第3、第5、第7个H2后插入DIV

### DIV样式类型指导
- 类型1：技术规格对比表（浅蓝#F5F7FA，多列对比）
- 类型2：性能仪表板（灰#ECEFF1，4–6指标卡片）
- 类型3：实施流程图（绿#E8F5E8，步骤圆形编号）
- 类型4：关键要点提醒（紫色渐变，要点列表）
- 类型5：服务价值展示（橙#FFF8E1，特性网格）
- 类型6：制造能力展示（深蓝#1A237E，层数/尺寸/精度）
- 类型7：组装服务优势（青色渐变，制造到组装链路）

## 表格字体样式要求
- h3标题需显式字体颜色，默认黑色#000000
- 表格文字必须显式颜色（默认#000000）
- 表格背景保持浅色；thead推荐#F5F5F5/#E0E0E0
- 在table/theader内使用内联样式以保证可读性

## 图表与图片生成要求
- 禁止使用 <canvas>、<img>、<script>
- 禁止外部JS库生成图表
- 仅用 <table> 展示数据与对比

## 内容要求（按相关性选取）
1. FAQ：堆叠/材料/孔/阻抗/装配/可靠性 20 问
2. 常见缺陷：翘曲、CAF、空洞、阻抗失控
3. 装配：微间距、翘曲治具、低空洞回流
4. 测试：阻抗、X-Ray、洁净度/SIR
5. NPI 门控：薄芯贴合、mSAP 图形、VIPPO 铜填
6. 追溯：条码、SPC、良率/不良解析
7. 成本/交付：材料选型、拼板、备料

## FAQ 与 NPI 要求
- 以 FAQ 形式输出 20 个问答，问题需覆盖堆叠、图形、电镀、孔、装配、可靠性。
- 在 FAQ 之后给出 ≥40 条 EVT/DVT/PVT 门控清单，含 DFM/DFT/DFA、SI/PI、可靠性与追溯。


## 品牌植入策略
- 首提全称“HilPCBPCB Factory（HILPCB）”，后续用“HILPCB”；每文3–5次，避免过度营销
- 自然植入点：技术难点后、解决方案中、案例分享时、规格说明后
- 制造/组装寻找意图时强调一站式能力

## SEO优化要求
- 主关键词密度：0.8–1.2%；LSI：3–5个，每个2–4次
- 语义相关词：SLP FAQ、mSAP、VIPPO空洞、薄芯翘曲、CAF、NPI门控

## 转化策略
- CTA布局：开篇软植入、技术难点处、方案后、文末强CTA
- 文末示例：立即联系HILPCB、申请DFM检查、获取报价
- 制造/组装专用CTA：制造合作伙伴、一站式制造+组装服务

## 写作风格与可读性
- 专业准确、术语适度；段落3–5句，句长15–25词
- 使用过渡词与列表，技术图表用文字+表格说明

## 质量控制清单
- [ ] H2标题格式正确
- [ ] 3–5个相关内链，锚文本多样
- [ ] HILPCB品牌自然植入3–5次
- [ ] DIV样式与表格样式符合要求
- [ ] 技术准确、关键词密度达标、结构完整、字数达标
- [ ] 制造/组装服务与信任要素完整呈现

## 竞争差异化要点
- 沉淀 30/30 μm 细线量产的 FAQ 与对策
- EVT/DVT/PVT 门控模板 + 数据要求
- 多源材料（Megtron/MPI/ABF）经验
- 阻抗/洁净度/翘曲实时监控

## 内容更新机制与注意事项
- 季度更新标准、跟踪趋势、补充案例、优化转化
- 避免过度技术化/不当竞争；不泄露客户信息；数据真实可验证