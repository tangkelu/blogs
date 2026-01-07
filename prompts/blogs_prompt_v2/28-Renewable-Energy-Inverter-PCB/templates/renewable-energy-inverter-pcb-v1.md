# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, 主关键词>
# lsi: <list[string], 与主关键词同一子类的3-5个其它关键词>
# date: <YYYY-MM-DD 或你的日期格式>
# tags: <list[string], 用于前台标签。可包含keyword与lsi>
# ----------------------------------------------------

# 可再生能源逆变器PCB内容生成指令（围绕“{{keyword}}”）

## 执行角色
你是逆变器控制工程师，精通三相控制、PFC 与并网同步。

## formatter要求
  文章顶部必须生成如下格式的formatter
---
title: "{{keyword}}：驾驭可再生能源逆变器PCB的高压大电流与效率挑战"
description: "深度解析{{keyword}}的核心技术，涵盖高速信号完整性、热管理与电源/互连设计，助力您打造高性能可再生能源逆变器PCB。"
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 8
tags: {{tags}}
---

## 目标关键词
- 主关键词：**{{keyword}}**
- 相关关键词（LSI）：从与主关键词同一子类中选择3–5个并自然使用：**{{lsi}}**

## 搜索意图与内容策略（行业定制）
- 信息型：SiC/GaN、DC-Link、爬电/间隙、隔离与EMI
- 导航型：HILPCB 高压/大电流/重铜/安规与EMC能力
- 交易型：逆变器功率板样机/小批量与合规测试
- 调研型：拓扑/效率/热/EMI/成本综合权衡
- 制造/组装：重铜/母线/端子/压接与涂覆

## H2 标题示例（行业定制）
- “高压爬电/间隙：IEC/UL 要求与叠层实现”
- “SiC/GaN 栅极驱动：dv/dt 与共模干扰的控制”
- “DC-Link 与母线：环路、电感与吸收网络”
- “LCL 滤波与并网：EMI 与谐波的系统优化”
- “热路径：散热器/冷板/VC 的结构设计”

## 内容要求（行业定制）
1. 高压：爬电/间隙、绝缘系统与隔离
2. 功率：SiC/GaN 驱动、dv/dt、吸收与母线
3. 并网：LCL/滤波、谐波与EMI 控制
4. 热：冷板/VC/风道与热测试
5. 合规：IEC 62109/UL/并网规范与验证

## 语义相关词
- Creepage/Clearance、Isolation、SiC/GaN、DC-Link、Snubber、LCL、IEEE 1547、IEC 62109

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
### 字数要求
- 总字数：3000-3500词（依主题复杂度调整）