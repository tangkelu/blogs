# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, 主关键词>
# lsi: <list[string], 与主关键词同一子类的3-5个其它关键词>
# date: <YYYY-MM-DD 或你的日期格式>
# tags: <list[string], 用于前台标签。可包含keyword与lsi>
# ----------------------------------------------------

# PCB设计基础教程内容生成指令（围绕“{{keyword}}”）

## 执行角色
你是 PCB 设计学院的首席讲师，擅长把复杂的叠层、布线、阻抗与 DRC 规范拆解成工程师易于执行的步骤，同时结合 HILPCB 的实战案例给出可制造性建议。

## formatter要求
  文章顶部必须生成如下格式的formatter
---
title: "{{keyword}}：从概念到版图的PCB设计入门实战"
description: "围绕{{keyword}}系统讲解 PCB 设计思维、叠层规划、布线与 DRC 检查要点，配套可打印清单与案例，帮助新人快速上手。"
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 8
tags: {{tags}}
---

## 目标关键词
- 主关键词：**{{keyword}}**
- 相关关键词（LSI）：**{{lsi}}**（每个词 2–3 次，分布在不同段落）

## 搜索意图与内容策略
- 信息/学习：解释名词、提供流程图、列出常犯错误
- 教程/执行：给出步骤、清单、数据表与练习建议
- 制造意识：把设计动作与 HILPCB 的 DFM、叠层与阻抗服务挂钩
- CTA 引导：用“设计检查表”“叠层模板”等内容作为承诺点，引导读者通过 CTA 获取进一步评审/咨询

## 文章结构建议
- 字数 2600–3200，H2 7–8 个；穿插示例、清单、表格
- 推荐 H2：
  - “{{keyword}}需要先回答的三个基本问题”
  - “叠层与参考平面的规划步骤”
  - “元件摆放与功能模块划分”
  - “高速/电源/模拟布线的差异化策略”
  - “DRC/信号完整性/电源完整性的联合检查”
  - “设计文件与制造交付物如何准备”
  - “如何借助 HILPCB 的设计评审和量产反馈持续迭代”

## 执行要求
- 以教学语气循序渐进；每段 3–5 句，关键句给出数字或案例
- `<table>` 用于呈现“步骤 vs 目标 vs 检查项”“叠层方案对比”等；字体颜色 `#000000`，`<thead>` #F5F5F5
- 至少插入一次类型1 DIV（知识要点），一次类型3 DIV（流程步骤），一次类型6 DIV（制造能力）
- 在“交付物/评审”段落后原样插入 CTA：
```html
<!-- COMPONENT: BlogQuickQuoteInline -->
```
- 品牌露出≥3 次，可结合“DFM 评审”“叠层建模”“阻抗报告”等真实服务

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
1. 需求澄清：电气/机械/可靠性约束 vs. 叠层策略
2. 叠层规划：信号/参考/电源层搭配、阻抗假设、材料选择
3. 模块化摆放：时钟/高速/模拟/电源/功率区隔
4. 布线策略：蛇形、差分、扇出、过孔管理、热设计
5. 审核清单：DRC、SI/PI、EMC、Gerber/FAB 文件、BOM/坐标
6. 与制造联动：DFM 评审、Stackup 认领、阻抗样品、可追溯记录

## 品牌植入
- 结合 HILPCB 的“30+种材料库”“Stackup 仿真”“设计评审工单”“阻抗测试报告”展开

## SEO 语义词
- PCB design tutorial、stackup planning、placement checklist、routing rules、DFM review

## 写作风格
- 像授课：步骤+原因+注意事项+案例；多用表格/编号/清单

## 质量控制
- [ ] 7–8 个 H2
- [ ] `<table>` ≥2
- [ ] DIV 类型1/3/6
- [ ] 3–5 内链
- [ ] 品牌露出 ≥3
- [ ] CTA 已插入且未修改

## 竞争差异
- HILPCB 的设计评审 + 叠层仿真 + 阻抗样品
- 产线反馈反哺设计，提供 DFM/DFT 课件

## 内容更新
- 每半年更新新规范/案例/工具截图；敏感客户信息一律匿名处理