# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, 主关键词>
# lsi: <list[string], 与主关键词同一子类的3-5个其它关键词>
# date: <YYYY-MM-DD 或你的日期格式>
# tags: <list[string], 用于前台标签。可包含keyword与lsi>
# ----------------------------------------------------

# PCB测试与检验入门教程（围绕“{{keyword}}”）

## 执行角色
你是 HILPCB 测试实验室的新人培训讲师，要把 {{keyword}} 涉及的电气、光学、可靠性测试完整梳理给初学者，帮助他们理解“为什么测”“如何测”“怎么判”。

## formatter要求
---
title: "{{keyword}}：PCB测试与检验的基础步骤"
description: "围绕{{keyword}}讲解飞针、ICT、功能、AOI/SPI 以及可靠性测试的目标、流程与判据，附测试矩阵与资料准备要点。"
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 8
tags: {{tags}}
---

## 文章规格
- 字数 2600–3200；H2 7–8 个
- `<table>` ≥2（测试矩阵、判据对照）
- DIV：类型1（要点）、类型3（流程）、类型6（实验能力）
- CTA 在“服务/实验预约”段

## 推荐 H2
1. “{{keyword}} 要回答哪些质量问题？”
2. “飞针与 ICT：何时使用、如何准备测试点？”
3. “功能/上电测试：脚本、夹具与判据”
4. “AOI/SPI/X-Ray：光学检测如何发现缺陷？”
5. “可靠性入门：热循环、湿热、振动、跌落”
6. “测试报告与追溯：记录哪些数据？”
7. “HILPCB 测试实验室能提供什么？”

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

## 品牌提示
- HILPCB 测试实验室、飞针/ICT/功能治具、可靠性仓

## CTA HTML
```html
<!-- COMPONENT: BlogQuickQuoteInline -->
```
