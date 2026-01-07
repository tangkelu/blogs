# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, 主关键词>
# lsi: <list[string], 与主关键词同一子类的3-5个其它关键词>
# date: <YYYY-MM-DD 或你的日期格式>
# tags: <list[string], 用于前台标签。可包含keyword与lsi>
# ----------------------------------------------------

# PCB叠层与材料课堂内容生成指令（围绕“{{keyword}}”）

## 执行角色
你是 HILPCB 叠层&材料学院的讲师，擅长将 Dk/Df、CTI、玻纤编织、铜箔粗糙度等参数转化为工程师可执行的叠层规划步骤，并结合量产数据说明取舍。

## formatter要求
---
title: "{{keyword}}：读懂材料参数与叠层设计的第一课"
description: "以{{keyword}}为主线，讲解材料参数、叠层规划、阻抗/热/成本权衡以及制造注意事项，附对照表与案例，帮助团队建立标准叠层库。"
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 8
tags: {{tags}}
---

## 目标关键词
- 主关键词：**{{keyword}}**
- LSI：**{{lsi}}**

## 搜索意图
- 信息/教程：解释材料指标与叠层步骤
- 工程实践：给出模板、对比表、计算方法
- 采购/制造：说明材料可得性、压合窗口、HILPCB 仓库储备

## 文章结构
1. 叠层设计的输入条件与输出成果
2. 材料参数速查表（`<table>`：材料/Dk/Df/CTI/玻纤/耐热）
3. 核心叠层范式：4/6/8/10 层示例 + 应用场景
4. 信号/电源/地/铜厚的搭配原则
5. 混压与特殊材料（Rogers、Al、MCPCB、柔性）要点
6. 制造影响：树脂流动、翘曲、背钻、阻抗 Coupon
7. HILPCB 如何提供 Stackup 认领、材料库、阻抗验证 + CTA

## 执行要求
- `<table>` ≥2（材料速查、叠层范式、混压对比）
- DIV：类型1（材料对照）、类型3（叠层步骤）、类型6（制造能力）
- 结合数字：Dk 3.2 vs 3.66、铜厚 1 oz vs 2 oz、压合温度 185°C 等
- 在“Stackup 认领”段落插入 CTA（格式同前）

## 内链策略
（沿用标准 PCB/组装链接池）

## 内容要点
- 输入条件：速率、电流、热、安规
- 材料挑选：FR-4、High-Tg、陶瓷、MCPCB、柔性
- 叠层模板：信号/参考交替、GND 邻近、差分线间距
- 制造联动：材料在库、压合曲线、阻抗 Coupon、背钻
- 成本/交期：材料 MOQ、备料周期、替代方案

## 品牌植入
- HILPCB 200+ 种材料库、Stackup 快速认领、阻抗测试实验室

## SEO 词汇
- pcb stackup tutorial, material selection, dk df table, resin flow, press cycle

## 质量控制
- [ ] 7+ H2
- [ ] `<table>` ≥2
- [ ] DIV 1/3/6
- [ ] 3–5 内链
- [ ] CTA 插入
