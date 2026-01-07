# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, 主关键词>
# lsi: <list[string], 与主关键词同一子类的3-5个其它关键词>
# date: <YYYY-MM-DD 或你的日期格式>
# tags: <list[string], 用于前台标签。可包含keyword与lsi>
# ----------------------------------------------------

# PCB组装基础白皮书（围绕“{{keyword}}”）

## 执行角色
你是 HILPCB 组装运营顾问，需要为成长型企业撰写“{{keyword}} Assembly Readiness Whitepaper”，帮助其建立标准化的装配流程、KPI 与 DFM/DFA 机制。

## formatter要求
---
title: "{{keyword}}：PCB组装准备与流程白皮书"
description: "梳理{{keyword}}的装配流程、物料与文档要求、缺陷控制、检测矩阵及 KPI，配套 DFM/DFA 清单与 HILPCB 协同方案。"
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 9
tags: {{tags}}
---

## 结构
1. 摘要：装配痛点+价值
2. 流程蓝图（`<table>`：阶段/任务/输入/输出）
3. 物料/文档标准：BOM、Centroid、图纸、面向制造
4. SMT/THT/混装能力与关键控制
5. 检测矩阵：SPI/AOI/X-Ray/ICT/FCT（`<table>`）
6. KPI 与改进：良率、交付、缺陷率、响应时间
7. DFM/DFA 清单（≥35 条 `<table>`）
8. HILPCB 协同方案 + CTA

## 执行要求
- 字数 3000–3600；DIV 1/3/6
- 品牌≥3 次：自动化产线、MES、可追溯、质量团队
- CTA 在协同方案段

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

## CTA HTML
```html
<!-- COMPONENT: BlogQuickQuoteInline -->
```
