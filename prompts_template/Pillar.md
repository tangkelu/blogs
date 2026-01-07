# v4-Pillar：教育科普/体系化指南（覆盖大词+做权威）
# PARAMETERS (filled by script at runtime)
# keyword: <string>
# lsi: <string, comma separated>
# date: <YYYY-MM-DD>
# tags: <json list string>
# ----------------------------------------------------

你要输出一篇“中文体系化指南（Pillar Page）”，围绕 {{keyword}}，目标是覆盖定义→原理→选型→落地→验证→常见误区，并为后续翻译保持术语一致。

## 输出硬约束（同v4-Query，必须遵守）
1) 只输出最终 Markdown，首字符必须是 `---`
2) 禁止AI话术
3) 必须出现且仅出现一次：`<!-- COMPONENT: BlogQuickQuoteInline -->`（放在“核心结论”后）
4) 文内必须包含 ≥3 条 `https://hilpcb.com/en/...` Markdown链接
5) HILPCB（HilPCB PCB Factory）全文 3–5 次
6) 中文 2500–4000 字，短句优先，便于翻译

## Front Matter（必须）
---
title: "<{{keyword}}的中文释义短语>（{{keyword}}）：从入门到量产的系统指南"
description: "用一句话说清：本文覆盖定义/关键指标/选型决策/验证方法（包含{{keyword}}）。"
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 9
tags: {{tags}}
---

## 页面结构（必须包含以下H2，顺序一致）
## 核心结论（先给答案）
- 5–7 条：定义、最关键的3个指标、1个典型误区、1个落地建议、1个验证方法

<!-- COMPONENT: BlogQuickQuoteInline -->

## 概念与边界：{{keyword}}到底指什么？
- 给出清晰定义 + 3个“不包括什么/别混淆什么”

## 指标体系：评估好坏看哪些参数？
- 用表格列：指标 | 为什么重要 | 典型范围/影响因素 | 怎么测

## 选型决策：不同场景如何取舍？
- 用“场景→推荐方案→代价/风险→适配LSI关键词”结构输出（至少6个场景）

## 从设计到制造：落地路径与检查点
- 8–12 个检查点（设计/材料/工艺/装配/测试），每点给：建议 + 风险 + 验收方式

## 常见误区与反例（教育型必备）
- 6–10 条误区：误区说法 → 为什么错 → 正确做法

## FAQ（8–12问）
- 覆盖真实搜索问法（是什么/为什么/怎么选/怎么验证/成本影响）

## 进一步阅读与工具（必须含内链）
至少 3–5 个内链（同v4-Query示例，锚文本多样）。

## 术语表（中英对照）
- 表格至少 12 行，锁定术语译法，避免翻译漂移

## 结语（温和CTA）
- 给“资料清单”：如果要评审/报价，需要提供哪些信息（Gerber/stackup/弯折要求/测试标准等）
