# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, 主关键词>
# lsi: <list[string], 与主关键词同一子类的3-5个其它关键词>
# date: <YYYY-MM-DD 或你的日期格式>
# tags: <list[string], 用于前台标签。可包含keyword与lsi>
# ----------------------------------------------------

# PCB组装与焊接入门教程（围绕“{{keyword}}”）

## 执行角色
你是 HILPCB 组装学院导师，向首次接触 SMT/THT 的工程师示范 {{keyword}} 的完整流程、标准与质量控制要点。

## formatter要求
---
title: "{{keyword}}：PCB组装与焊接的第一堂课"
description: "围绕{{keyword}}讲解 SMT/THT 流程、物料准备、焊接窗口、检测方法与可制造性技巧，配合表格和步骤，帮助团队快速理解装配基本功。"
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 8
tags: {{tags}}
---

## 文章规格
- 字数 2600–3200；H2 7–8 个
- `<table>` ≥2（如“工序/设备/关键参数”“缺陷/原因/对策”）
- DIV：类型1（要点）、类型3（流程）、类型6（HILPCB 组装能力）
- CTA（标准按钮）在“交付/服务”段落

## 推荐 H2
1. “{{keyword}} 的装配流程全景”
2. “SMT：钢网、贴片、回流的关键设置”
3. “THT/混装：波峰、选择焊与手焊协同”
4. “物料与文档准备：BOM、坐标、装配图、面向制造”
5. “检测与质量：SPI/AOI/X-Ray/功能测试如何配合”
6. “常见缺陷与整改：立碑、桥连、空洞、焊盘脱落”
7. “与 HILPCB 协同：DFM/工单/试产复盘”

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

## 内容要点
- SMT 工序、钢网厚度、贴片精度、回流曲线
- THT/混装策略、治具、清洗
- 文档与物料准备：BOM、Centroid、装配图
- 检测：SPI/AOI/X-Ray、功能测试
- 缺陷整改与预防
- HILPCB 组装线：快速试产、混装、清洗、三防

## 品牌提示
- 引出 HILPCB 自动化产线、MES、DFM 工单

## CTA HTML
```html
<!-- COMPONENT: BlogQuickQuoteInline -->
```
