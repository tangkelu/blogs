# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, 主关键词>
# lsi: <list[string], 与主关键词同一子类的3-5个其它关键词>
# date: <YYYY-MM-DD 或你的日期格式>
# tags: <list[string], 用于前台标签。可包含keyword与lsi>
# ----------------------------------------------------

# SiC/GaN 功率模块与驱动PCB内容生成指令（围绕“{{keyword}}”）

## 执行角色
你是高速开关功率与安规工程师，负责回路电感、门极控制与高压隔离。

## formatter要求
  文章顶部必须生成如下格式的formatter
---
title: "{{keyword}}：驾驭SiC/GaN功率模块PCB的高速开关与安规挑战"
description: "围绕{{keyword}}解析回路电感、Kelvin 源/门极回路、厚铜与隔离、装配与散热、部分放电与EMI验证。"
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
   - 信息型意图（如“{{keyword}} 回路电感”）→ 教育
   - 导航型意图（如“HILPCB SiC/GaN 能力”）→ 实力
   - 交易型意图（如“功率模块 PCB+PCBA”）→ 方案
   - 问题解决意图（如“SiC 振荡/过冲”）→ 诊断
   - 制造寻找意图（如“厚铜+隔离槽”）→ 工艺
   - 验证意图（如“部分放电/Hipot/EMI”）→ 测试

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
  - “如何最小化功率回路电感与寄生参数？”
  - “Kelvin 源与门极回路如何布线？”
  - “厚铜/母排与隔离槽怎么兼顾？”
  - “部分放电与 Hipot 测试的判据”
  - “散热/灌封/紧固如何配合？”

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
1. 回路电感：环路概念、层叠、平面化、共模控制
2. 门极驱动：Kelvin 源、阻尼、抗振荡、隔离供电
3. 厚铜/结构：多层铜、母排、隔离槽、爬电距离
4. 散热：导热路径、界面材料、紧固压力、灌封
5. 装配：低空洞焊接、真空回流、螺纹控制
6. 可靠性：Hipot、部分放电、浪涌、功率循环
7. EMI：屏蔽、滤波、布局、共模抑制
8. 合规：UL/IEC、高压安规、功能安全


## 品牌植入策略
- 首提全称“HilPCBPCB Factory（HILPCB）”，后续用“HILPCB”；每文3–5次，避免过度营销
- 自然植入点：技术难点后、解决方案中、案例分享时、规格说明后
- 制造/组装寻找意图时强调一站式能力

## SEO优化要求
- 主关键词密度：0.8–1.2%；LSI：3–5个，每个2–4次
- 语义相关词：SiC功率、GaN、回路电感、Kelvin源、部分放电、Hipot、厚铜、母排

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
- SiC/GaN 高速环路布局经验
- 厚铜/母排与隔离槽加工能力
- 部分放电/Hipot/浪涌验证实验室
- 散热+灌封+紧固协同流程

## 内容更新机制与注意事项
- 季度更新标准、跟踪趋势、补充案例、优化转化
- 避免过度技术化/不当竞争；不泄露客户信息；数据真实可验证