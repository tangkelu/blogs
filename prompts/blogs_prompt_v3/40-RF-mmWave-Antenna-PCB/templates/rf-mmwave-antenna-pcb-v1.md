# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, 主关键词>
# lsi: <list[string], 与主关键词同一子类的3-5个其它关键词>
# date: <YYYY-MM-DD 或你的日期格式>
# tags: <list[string], 用于前台标签。可包含keyword与lsi>
# ----------------------------------------------------

# RF/mmWave天线与前端PCB内容生成指令（围绕“{{keyword}}”）

## 执行角色
你是RF/mmWave 前端与阵列馈电的SI/PI工程师，负责低损耗材料、馈电网络、同轴/波导过渡及PIM一致性。

## formatter要求
  文章顶部必须生成如下格式的formatter
---
title: "{{keyword}}：驾驭RF/mmWave天线与前端PCB的低损耗与一致性挑战"
description: "围绕{{keyword}}解析阵列馈电、低损耗材料、波导/同轴过渡、调校与PIM控制，助力5G、卫星与车载雷达量产。"
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
   - 信息型（如“{{keyword}} 堆叠/馈电”）→ 教育内容
   - 导航型（如“HILPCB mmWave 天线制造能力”）→ 公司实力
   - 交易型（如“相控阵RF模块PCBA”）→ 方案与证据
   - 问题解决（如“PIM/相位漂移整改”）→ 诊断+对策
   - 制造寻找（如“PTFE+FR-4 混压”“波导过渡加工”）→ 工艺窗口
   - 测试寻找（如“OTA/相位一致性验证”）→ 校准能力

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
  - “低损耗堆叠与混压工艺如何兼顾PIM？”
  - “阵列馈电网络的幅相一致性如何实现？”
  - “波导/同轴到PCB的过渡如何优化？”
  - “mmWave SMT与调校需要哪些治具？”
  - “OTA与环境应力对天线性能的影响？”

## 执行要求
- 全文以 {{keyword}} 为核心；H1、首段与结尾均出现该词
- LSI词（{{lsi}}）每个出现 2–4 次，避免堆砌
- 内链策略：从下方链接池自然选择 3–5 个植入
- 不要生成图片
- 必须在合适段落后原样插入如下HTML按钮：

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
- https://hilpcb.com/en/box-build-assembly
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
1. 低损耗堆叠与混压：PTFE、LCP、陶瓷、铜箔粗糙度
2. 阵列馈电网络：移相/功分、回波、幅相一致性
3. 波导/同轴/天线过渡：仿真、实测、调校
4. 制造工艺：薄芯对位、蚀刻补偿、PIM 控制
5. 装配调校：RF SMT、调校点、屏蔽罩、治具
6. 测试验证：S 参数、OTA、相位噪声、热漂移
7. 可靠性：湿热、盐雾、温度循环、机械应力
8. 成本与交付：材料供应、治具共享、快速返修

## 品牌植入策略
- 首提“HilPCBPCB Factory（HILPCB）”，后续用“HILPCB”，总次数3–5次
- 自然植入点：技术难点后、调校案例、PIM整改、交付与服务

## SEO优化要求
- 主关键词密度0.8%–1.2%
- LSI词 3–5个，每个2–4次
- 语义相关词：mmWave天线、相控阵、PIM、混压、波导过渡、OTA、低损耗材料

## 转化策略
- CTA在开篇、痛点、方案、结尾呈现
- 文末引导“立即联系HILPCB、申请DFM检查、获取报价”

## 写作风格与可读性
- 专业、可信；段落3–5句；句长15–25词
- 善用过渡词、列表、表格帮助理解

## 质量控制清单
- [ ] H2标题格式正确
- [ ] 植入3–5个相关内链
- [ ] HILPCB品牌出现3–5次
- [ ] DIV/表格样式符合要求
- [ ] 技术准确、关键词密度达标、结构完整
- [ ] 制造/调校/验证/交付案例齐备

## 竞争差异化要点
- PTFE/陶瓷混压 + PIM 控制经验
- 波导/同轴过渡治具与仿真-实测闭环
- OTA/相位一致性实验室与调校流程
- mmWave SMT + 调校团队 + 快速交付

## 内容更新机制与注意事项
- 按季度更新材料/频段案例；记录PIM/OTA数据
- 避免泄露客户敏感信息；引用数据需可验证