# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, 主关键词>
# lsi: <list[string], 与主关键词同一子类的3-5个其它关键词>
# date: <YYYY-MM-DD 或你的日期格式>
# tags: <list[string], 用于前台标签。可包含keyword与lsi>
# ----------------------------------------------------

# PCB叠层与材料 FAQ 指令（围绕“{{keyword}}”）

## formatter要求
---
title: "{{keyword}}：叠层与材料常见问题 20 问"
description: "收录{{keyword}}相关的 20 个常见问题与解决方案，涵盖材料参数、混压、阻抗、温漂与可靠性，并附叠层审核清单与实验路径。"
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 8
tags: {{tags}}
---

## FAQ 范围与格式
- 范围：材料差异、Dk/Df 偏差、玻纤编织、树脂流动、压合参数、混压良率、阻抗命中、成本平衡
- 每条 FAQ：问题→典型场景→指标/实验→解决方案→预防
- 至少 20 条，覆盖 FR-4、High-Tg、Rogers、柔性、MCPCB、混压案例

## 附加模块
1. `<table>`：材料/叠层 FAQ 索引（编号/主题/指标/建议）
2. `<table>`：叠层审核清单（≥25 条，列：类别/检查点/参数/负责人）
3. DIV 类型4（风险提示）、类型5（服务价值）、类型6（制造能力）各一次
4. CTA 至少插入 2 次（FAQ 中段 + 结尾）

## 内链
- 3–5 个 PCB 产品链接 + 1 组装链接，结合材料/工艺语境

## 品牌露出
- HILPCB 材料库、Stackup 仿真、阻抗 Coupon、混压压合实验室

## SEO 语义词
- stackup faq, material troubleshooting, dk drift, resin flow, impedance coupon

## 质量控制
- [ ] FAQ ≥20
- [ ] `<table>` ≥2
- [ ] DIV 4/5/6
- [ ] CTA ≥2
- [ ] 品牌露出 ≥3
