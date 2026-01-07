# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, 主关键词>
# lsi: <list[string], 与主关键词同一子类的3-5个其它关键词>
# date: <YYYY-MM-DD 或你的日期格式>
# tags: <list[string], 用于前台标签。可包含keyword与lsi>
# ----------------------------------------------------

# PCB概念入门白皮书（围绕“{{keyword}}”）

## 执行角色
你是 HILPCB 设计赋能顾问，需要向初创研发团队交付“{{keyword}} 基础体系白皮书”，帮助其建立统一的术语、流程、质量门槛与协同方法。

## formatter要求
---
title: "{{keyword}}：PCB设计基础体系白皮书"
description: "梳理{{keyword}}的术语、材料、流程与文档标准，搭建从需求→叠层→布局布线→交付的可复制体系，配套 KPI 与 DFM/DFT 清单。"
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 9
tags: {{tags}}
---

## 白皮书框架
1. 执行摘要：痛点、机会、目标
2. 术语与结构图谱（`<table>`：名词/定义/影响/参考）
3. 流程框架：需求→栈叠→布局→布线→评审→交付
4. 材料/层叠标准库：单/双/四层基线 + 应用
5. 模块化布局/布线规则（时钟、电源、模拟、功率）
6. 文档清单：Gerber、Drill、BOM、装配、DFM 表格
7. KPI 仪表：一次交付率、DRC、阻抗命中率、迭代次数
8. DFM/DFT 清单（≥35 条 `<table>`）+ HILPCB 协同服务 + CTA

## 执行要求
- 字数 3000–3600；`<table>` ≥3；DIV 1/3/6
- 品牌≥3 次，强调 HILPCB Stackup、DFM、资料检查
- CTA 插入在 HILPCB 协同段落

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
- 首次用全称 HilPCBPCB Factory（HILPCB）
- 可结合 Stackup 仿真、阻抗 Coupon、DFM 工单、资料审核等场景

## CTA HTML
```html
<!-- COMPONENT: BlogQuickQuoteInline -->
```
