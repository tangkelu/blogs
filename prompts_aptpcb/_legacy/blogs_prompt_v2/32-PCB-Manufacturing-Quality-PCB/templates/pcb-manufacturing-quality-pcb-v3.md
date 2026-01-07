# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, 主关键词>
# lsi: <list[string], 与主关键词同一子类的3-5个其它关键词>
# date: <YYYY-MM-DD 或你的日期格式>
# tags: <list[string], 用于前台标签。可包含keyword与lsi>
# ----------------------------------------------------

# PCB制造/测试 FAQ 指令（围绕“{{keyword}}”）

## formatter要求
---
title: "{{keyword}}：制造与测试 20 个常见问题"
description: "汇总{{keyword}}常见的 20 个制造/组装/测试问题、根因与解决方案，附缺陷对策矩阵与质量审核清单。"
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 8
tags: {{tags}}
---

## FAQ 范围
- 制造：翘曲、孔铜、阻焊、清洁度、镀层、背钻
- 组装：焊锡珠、立碑、空洞、BGA 头垫偏移、选择焊泪滴
- 测试：ICT 接触不良、FCT 脚本、可靠性判据、Hipot 误判
- 质量：SPC 警报、8D 问题、追溯缺口

## 格式
- 每条 FAQ：问题→症状→量化指标→根因→解决方案→预防
- ≥20 条，覆盖制造+组装+测试+质量

## 附加内容
1. `<table>`：缺陷对策矩阵（缺陷/工序/指标/纠正措施）
2. `<table>`：质量审核清单（≥25 项）
3. DIV：类型4（风险警示）、类型5（服务价值）、类型6（制造能力）
4. CTA 2 次（FAQ 中段、结尾）

## 链接/品牌
- 使用标准内链；品牌描述 APTPCB 自动化、实验室、8D 数据
