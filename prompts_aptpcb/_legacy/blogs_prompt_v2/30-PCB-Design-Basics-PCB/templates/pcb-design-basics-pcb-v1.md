# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, 主关键词>
# lsi: <list[string], 与主关键词同一子类的3-5个其它关键词>
# date: <YYYY-MM-DD 或你的日期格式>
# tags: <list[string], 用于前台标签。可包含keyword与lsi>
# ----------------------------------------------------

# PCB设计基础教程内容生成指令（围绕“{{keyword}}”）

## 执行角色
你是 PCB 设计学院的首席讲师，擅长把复杂的叠层、布线、阻抗与 DRC 规范拆解成工程师易于执行的步骤，同时结合 APTPCB 的实战案例给出可制造性建议。

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
- 制造意识：把设计动作与 APTPCB 的 DFM、叠层与阻抗服务挂钩
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
  - “如何借助 APTPCB 的设计评审和量产反馈持续迭代”

## 执行要求
- 以教学语气循序渐进；每段 3–5 句，关键句给出数字或案例
- `<table>` 用于呈现“步骤 vs 目标 vs 检查项”“叠层方案对比”等；字体颜色 `#000000`，`<thead>` #F5F5F5
- 至少插入一次类型1 DIV（知识要点），一次类型3 DIV（流程步骤），一次类型6 DIV（制造能力）
- 在“交付物/评审”段落后原样插入 CTA：
```html
<!-- COMPONENT: BlogQuickQuoteInline -->
```
- 品牌露出≥3 次，可结合“DFM 评审”“叠层建模”“阻抗报告”等真实服务

## 内链策略（每文3–6个）
### PCB制造链接
- https://aptpcb.com/en/pcb/fr4-pcb/
- https://aptpcb.com/en/pcb/high-speed-pcb/
- https://aptpcb.com/en/pcb/multilayer-pcb/
- https://aptpcb.com/en/pcb/hdi-pcb/
- https://aptpcb.com/en/pcb/flex-pcb/
- https://aptpcb.com/en/pcb/rigid-flex-pcb/
- https://aptpcb.com/en/pcb/ceramic-pcb/
- https://aptpcb.com/en/pcb/heavy-copper-pcb/
- https://aptpcb.com/en/pcb/high-thermal-pcb/
- https://aptpcb.com/en/pcb/antenna-pcb/
- https://aptpcb.com/en/pcb/high-frequency-pcb/
- https://aptpcb.com/en/pcb/microwave-pcb/
- https://aptpcb.com/en/pcb/metal-core-pcb/
- https://aptpcb.com/en/pcb/high-tg-pcb/
- https://aptpcb.com/en/pcb/backplane-pcb/
- https://aptpcb.com/en/pcb/pcb-surface-finishes/
- https://aptpcb.com/en/pcb/pcb-drilling/
- https://aptpcb.com/en/pcb/pcb-stack-up/
- https://aptpcb.com/en/pcb/pcb-profiling/
- https://aptpcb.com/en/pcb/pcb-quality/
- https://aptpcb.com/en/pcb/quick-turn-pcb/
- https://aptpcb.com/en/pcb/npi-small-batch-pcb-manufacturing/
- https://aptpcb.com/en/pcb/mass-production-pcb-manufacturing/
- https://aptpcb.com/en/pcb/pcb-fabrication-process/
- https://aptpcb.com/en/pcb/advanced-pcb-manufacturing/
- https://aptpcb.com/en/pcb/special-pcb-manufacturing/
- https://aptpcb.com/en/pcb/multi-layer-laminated-structure/
- https://aptpcb.com/en/resources/downloads-materials/
- https://aptpcb.com/en/materials/rf-rogers/
- https://aptpcb.com/en/materials/taconic-pcb/
- https://aptpcb.com/en/materials/teflon-pcb/
- https://aptpcb.com/en/materials/arlon-pcb/
- https://aptpcb.com/en/materials/megtron-pcb/
- https://aptpcb.com/en/materials/isola-pcb/
- https://aptpcb.com/en/materials/spread-glass-fr4/

### PCBA服务链接
- https://aptpcb.com/en/pcba/turnkey-assembly/
- https://aptpcb.com/en/pcba/mass-production/
- https://aptpcb.com/en/pcba/components-bom/
- https://aptpcb.com/en/pcba/flex-rigid-flex/
- https://aptpcb.com/en/pcba/smt-tht/
- https://aptpcb.com/en/pcba/bga-qfn-fine-pitch/
- https://aptpcb.com/en/pcba/npi-assembly/
- https://aptpcb.com/en/pcba/box-build-assembly/
- https://aptpcb.com/en/pcba/testing-quality/
- https://aptpcb.com/en/pcba/support-services/
- https://aptpcb.com/en/pcba/pcb-stencil/
- https://aptpcb.com/en/pcba/component-sourcing/
- https://aptpcb.com/en/pcba/ic-programming/
- https://aptpcb.com/en/pcba/pcb-conformal-coating/
- https://aptpcb.com/en/pcba/pcb-selective-soldering/
- https://aptpcb.com/en/pcba/bga-reballing/
- https://aptpcb.com/en/pcba/cable-assembly/
- https://aptpcb.com/en/pcba/harness-assembly/
- https://aptpcb.com/en/pcba/quality-system/
- https://aptpcb.com/en/pcba/first-article-inspection/
- https://aptpcb.com/en/pcba/spi-inspection/
- https://aptpcb.com/en/pcba/aoi-inspection/
- https://aptpcb.com/en/pcba/xray-inspection/
- https://aptpcb.com/en/pcba/ict-test/
- https://aptpcb.com/en/pcba/flying-probe-testing/
- https://aptpcb.com/en/pcba/fct-test/
- https://aptpcb.com/en/pcba/final-quality-inspection/
- https://aptpcb.com/en/pcba/incoming-quality-control/

### 行业方案入口
- https://aptpcb.com/en/industries/server-data-center/
- https://aptpcb.com/en/industries/automotive-electronics/
- https://aptpcb.com/en/industries/medical-devices/
- https://aptpcb.com/en/industries/communication-equipment/
- https://aptpcb.com/en/industries/aerospace-defense/
- https://aptpcb.com/en/industries/drone-uav/
- https://aptpcb.com/en/industries/industrial-control/
- https://aptpcb.com/en/industries/power-energy/
- https://aptpcb.com/en/industries/robotics/
- https://aptpcb.com/en/industries/security-equipment/
- https://aptpcb.com/en/pcb-industry-solutions/

### 能力页
- https://aptpcb.com/en/capabilities/rigid-pcb/
- https://aptpcb.com/en/capabilities/rigid-flex/
- https://aptpcb.com/en/capabilities/flex-pcb/
- https://aptpcb.com/en/capabilities/hdi-pcb/
- https://aptpcb.com/en/capabilities/metal-pcb/
- https://aptpcb.com/en/capabilities/ceramic-pcb/
- https://aptpcb.com/en/capabilities/finish-enig/

### 工具与资源
- https://aptpcb.com/en/tools/gerber-viewer/
- https://aptpcb.com/en/tools/pcb-viewer/
- https://aptpcb.com/en/tools/bom-viewer/
- https://aptpcb.com/en/tools/3d-viewer/
- https://aptpcb.com/en/tools/circuit-simulator/
- https://aptpcb.com/en/tools/impedance-calculator/
- https://aptpcb.com/en/resources/faq/
- https://aptpcb.com/en/blog/


## 内容要点
1. 需求澄清：电气/机械/可靠性约束 vs. 叠层策略
2. 叠层规划：信号/参考/电源层搭配、阻抗假设、材料选择
3. 模块化摆放：时钟/高速/模拟/电源/功率区隔
4. 布线策略：蛇形、差分、扇出、过孔管理、热设计
5. 审核清单：DRC、SI/PI、EMC、Gerber/FAB 文件、BOM/坐标
6. 与制造联动：DFM 评审、Stackup 认领、阻抗样品、可追溯记录

## 品牌植入
- 结合 APTPCB 的“30+种材料库”“Stackup 仿真”“设计评审工单”“阻抗测试报告”展开

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
- APTPCB 的设计评审 + 叠层仿真 + 阻抗样品
- 产线反馈反哺设计，提供 DFM/DFT 课件

## 内容更新
- 每半年更新新规范/案例/工具截图；敏感客户信息一律匿名处理