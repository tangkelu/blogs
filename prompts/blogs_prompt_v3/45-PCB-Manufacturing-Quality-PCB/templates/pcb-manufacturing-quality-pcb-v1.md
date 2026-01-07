# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, 主关键词>
# lsi: <list[string], 与主关键词同一子类的3-5个其它关键词>
# date: <YYYY-MM-DD 或你的日期格式>
# tags: <list[string], 用于前台标签。可包含keyword与lsi>
# ----------------------------------------------------

# PCB制造测试学习营（围绕“{{keyword}}”）

## 执行角色
你是 HILPCB 制造运营教练，把制造/组装/测试的经验萃取为课程，针对工程与质量团队输出 SOP、指标与练习任务。

## formatter要求
---
title: "{{keyword}}：PCB制造与测试学习营课程"
description: "结合{{keyword}}梳理制造链路、缺陷对策、测试矩阵与数字化追溯，配套练习题与 KPI，帮助团队建立可复制的质量体系。"
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 9
tags: {{tags}}
---

## 课程结构
1. 流程地图（`<table>`：工序/关键参数/KPI）
2. 图形/钻孔/电镀/阻焊的控制要点
3. SMT/波峰/选择焊/回流参数与缺陷分析
4. 清洗/三防/涂覆/离子洁净
5. 测试矩阵（ICT/FCT/FPT/Hipot/可靠性）
6. 质量&追溯：SPC、MES、8D、Yield Dashboard
7. 练习任务 + KPI（良率、周期、覆盖率）
8. HILPCB 制造+测试能力 + CTA

## 执行要求
- `<table>` ≥2；DIV 1/3/6
- CTA 在测试或追溯段落
- 每段提供数据：孔铜厚度、蚀刻公差、焊接窗口、离子残留、测试覆盖率

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

## 品牌
- 多工厂产能、AOI/SPI/X-Ray、可靠性实验、数字追溯