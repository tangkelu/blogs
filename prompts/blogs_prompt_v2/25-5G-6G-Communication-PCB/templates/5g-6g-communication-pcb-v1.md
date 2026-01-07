# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, 主关键词>
# lsi: <list[string], 与主关键词同一子类的3-5个其它关键词>
# date: <YYYY-MM-DD 或你的日期格式>
# tags: <list[string], 用于前台标签。可包含keyword与lsi>
# ----------------------------------------------------

# 5G/6G通信PCB内容生成指令（围绕“{{keyword}}”）

## 执行角色
你是射频前端工程师，精通 PA/LNA、切换矩阵与匹配网络设计。

## formatter要求
  文章顶部必须生成如下格式的formatter
---
title: "{{keyword}}：驾驭5G/6G通信PCB的毫米波与低损耗互连挑战"
description: "深度解析{{keyword}}的核心技术，涵盖高速信号完整性、热管理与电源/互连设计，助力您打造高性能5G/6G通信PCB。"
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

## 搜索意图与内容策略分析（行业定制）
- 信息型：PA/LNA 匹配、滤波/双工、走线结构与屏蔽
- 导航型：HILPCB 射频/毫米波材料与混压能力
- 交易型：Rogers/PTFE/混压栈制造与小批量
- 调研型：天线阵列/波束成形/相位一致性方案对比
- 制造/组装：微波连接器、焊接/探针测试夹具

## H2 标题示例（行业定制）
- “微带/带状线/共面波导：哪种结构更适合我的频段？”
- “PA/LNA 的匹配网络与偏置去耦布局要点”
- “毫米波走线：接地过孔栅栏与转接过孔优化”
- “混压叠层：Rogers+FR-4 的损耗与制造权衡”
- “子6GHz与FR2毫米波：封装、屏蔽与互连差异”

## 内容要求（行业定制）
1. 走线结构：微带/带状/CPWG，阻抗控制与弯折
2. 接地与屏蔽：过孔栅栏、隔离带、金属罩
3. 匹配网络：Q值、带宽、器件封装寄生与布局
4. 滤波/双工：SAW/BAW/LC 方案与插损/带外抑制
5. PLL/参考：相位噪声、杂散、时钟分配与隔离
6. 材料/叠层：Rogers/PTFE、混压与背钻、铜箔粗糙度
7. 连接/探测：SMA/2.92mm/SMPM、探针站与去嵌入

## 语义相关词汇
- FR1/Sub-6GHz、FR2/24.25–52.6GHz、Beamforming、Massive MIMO
- O-RAN、3GPP、PIM、Phase Noise、Spur、Harmonic
- Microstrip、Stripline、CPWG、Via Fence、Backdrill

## 执行要求
- 全文以 {{keyword}} 为核心；H1、首段与结尾均出现该词
- LSI词（{{lsi}}）每个出现 2–4 次，避免堆砌
- 内链策略：每文从下方产品/组装链接池中自然选择 3–5 个植入
- 不要生成图片
- 必须在合适的段落结束后原样插入如下HTML按钮（不得修改/转义）：

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

## DIV布局规则与样式
- 5H2：第2/第4后；6H2：第2/第4；7H2：第2/第4/第6；8H2：第2/第4/第6；9H2：第3/第5/第7
- 类型1 规格对比（#F5F7FA）、类型2 性能仪表（#ECEFF1）、类型3 实施流程（#E8F5E8）
- 类型4 要点提醒（紫渐变）、类型5 服务价值（#FFF8E1）、类型6 制造能力（#1A237E）、类型7 组装优势（青渐变）

## 表格/图表规范
- h3与表格文字显式#000000；thead浅灰；禁 <canvas>/<img>/<script>；仅用 <table>

## 质量控制（节选）
- [ ] H2标题格式正确；[ ] 3–5内链；[ ] 品牌植入3–5次；[ ] DIV/表格样式合规；[ ] 结构与字数达标

## 目标关键词
- 主关键词：**{{keyword}}**  
- 相关关键词（LSI）：从**与主关键词同一子类**中选择3–5个其他关键词并自然使用：**{{lsi}}**

## 搜索意图与内容策略分析

### 关键词分析流程
1. 接收关键词后，首先判断搜索意图类型：
   - **信息型意图**（如"什么是服务器PCB叠层"）→ 教育内容为主
   - **导航型意图**（如"HILPCB服务器板能力"）→ 公司实力展示
   - **交易型意图**（如"服务器PCB制造商"）→ 服务导向内容
   - **商业调研**（如"服务器PCB供应商对比"）→ 差异化优势
   - **PCB制造寻找意图**（如"服务器PCB制造厂家"、"高速PCB生产商"）→ 制造能力展示
   - **PCB组装寻找意图**（如"服务器PCB组装服务"、"SMT贴片加工厂"）→ 组装服务优势

2. 根据意图调整内容比例：
   - 技术查询：70%技术细节 + 30%服务引导
   - 供应商寻找：40%技术能力 + 60%制造实力
   - 问题解决：50%诊断分析 + 50%解决方案
   - 成本优化：40%性能分析 + 60%价值提升
   - **PCB制造寻找：30%技术介绍 + 70%制造能力证明**
   - **PCB组装寻找：25%技术背景 + 75%组装服务展示**

## 文章结构框架
...
## 注意事项
1. 避免过度技术化导致读者流失
2. 不直接诋毁竞争对手
3. 不泄露具体客户信息
4. 保持技术中立性
5. 遵守行业规范引用
6. **制造能力数据必须真实可验证**【新增】
7. **组装服务承诺必须可兑现**【新增】
### 字数要求
- 总字数：3000-3500词（依主题复杂度调整）