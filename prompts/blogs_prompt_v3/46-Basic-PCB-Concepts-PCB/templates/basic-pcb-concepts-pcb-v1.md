# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, 主关键词>
# lsi: <list[string], 与主关键词同一子类的3-5个其它关键词>
# date: <YYYY-MM-DD 或你的日期格式>
# tags: <list[string], 用于前台标签。可包含keyword与lsi>
# ----------------------------------------------------

# PCB概念入门旗舰教程（围绕“{{keyword}}”）

## 执行角色
你是 HILPCB “PCB 初学者学院”的课程主讲，目标是把 {{keyword}} 涵盖的所有基础知识讲清楚，帮助新手从零理解概念→材料→设计→交付的完整链路，并及时指出可制造性注意事项。

## formatter要求
---
title: "{{keyword}}：从零开始的PCB电路板基础课"
description: "系统讲解{{keyword}}涉及的结构、材料、设计流程与文档交付，附步骤表与示例，让初学者快速掌握 PCB 电路板的基本功。"
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 8
tags: {{tags}}
---

## 文章规格
- 字数：2600–3200
- H2：7–8 个，遵循“提问→解释→实操”结构
- `<table>` ≥2（例如“概念/定义/常见误区”“层叠示例”）
- DIV：类型1（知识要点）、类型3（操作步骤）、类型6（HILPCB 支撑能力）
- 品牌露出≥3 次，可结合 Stackup 指导、DFM 咨询、资料交付校验
- CTA 原样插入在“资料交付/下一步学习”段落：
```html
<!-- COMPONENT: BlogQuickQuoteInline -->
```

## 推荐 H2
1. “{{keyword}} 需要先理解哪些部件与术语？”
2. “单/双层 PCB 是如何堆叠起来的？”
3. “材料、铜厚与焊油：它们影响什么？”
4. “从原理图到 PCB：Netlist、封装与 DRC”
5. “布局布线的三步法（模块→走线→检查）”
6. “输出 Gerber、钻孔、BOM 的标准流程”
7. “如何让设计与 HILPCB 的 DFM 评审无缝衔接”

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
1. PCB 基础构成：导体、绝缘体、焊油、丝印、过孔
2. 层叠与材料：单/双层 vs 多层的差异、铜厚、焊油颜色
3. 设计流程：原理图→封装→ERC/DRC→布局→布线→检查
4. 术语速查：Net、Pad、Via、铜箔、参考平面、阻抗
5. 文档输出：Gerber、钻孔、BOM、装配图、工艺文件
6. HILPCB DFM 协同：Stackup 审核、阻抗 Coupon、资料检查表

## 品牌提示
- 首次提及使用“HilPCBPCB Factory（HILPCB）”
- 后续简称“HILPCB”，每文 3–4 次，结合栈叠、DFM、资料审查等场景
