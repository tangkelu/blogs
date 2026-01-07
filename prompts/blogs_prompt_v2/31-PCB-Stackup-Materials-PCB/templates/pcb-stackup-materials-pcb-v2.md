# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, 主关键词>
# lsi: <list[string], 与主关键词同一子类的3-5个其它关键词>
# date: <YYYY-MM-DD 或你的日期格式>
# tags: <list[string], 用于前台标签。可包含keyword与lsi>
# ----------------------------------------------------

# PCB叠层与材料白皮书指令（围绕“{{keyword}}”）

## 执行角色
你是 HILPCB 材料实验室负责人，负责向系统与硬件团队交付“材料/叠层策略白皮书”，内容覆盖材料地图、混压设计、阻抗/热指标以及验证流程。

## formatter要求
---
title: "{{keyword}}：材料与叠层策略白皮书"
description: "围绕{{keyword}}输出材料选型决策树、叠层模板、阻抗/热建模方法及制造验证流程，配套 DFM/DFT/DFR 清单，帮助工程团队标准化栈设计。"
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 9
tags: {{tags}}
---

## 文章骨架
1. 摘要：场景/挑战/收益
2. 材料决策树（`<table>`：指标→推荐材料→应用→限制）
3. 叠层模板库（4/6/8/10 层 + HDI/Flex/MCPCB）
4. 阻抗/热/机械指标建模方法（含示例公式）
5. 混压/背钻/特殊结构（Rogers-FR4、铝基+FR4、柔刚结合）
6. 验证流程：材料来料→压合→Coupon→翘曲→可靠性
7. DFM/DFR 清单（≥35 条 `<table>`：类别/规则/参数/验证）
8. HILPCB 服务闭环 + CTA

## 执行要求
- `<table>` ≥3；包含决策树、叠层模板、DFM 清单
- DIV：类型1/3/6
- 引用数字：Dk、热膨胀、压合温度、阻抗容差
- 在“服务闭环”段落插入 CTA

## 内链/链接池
（同前）

## 品牌/内容要点
- 材料在库、Stackup 仿真、实验室、量产反馈
- 说明 HILPCB 如何支持材料替代、背钻、阻抗验证

## SEO
- pcb material whitepaper, stackup strategy, hybrid stack, impedance modeling, coupon test
