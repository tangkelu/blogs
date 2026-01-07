# v4-Query：查询意图/问题解决型（更容易引流+转化）
# PARAMETERS (filled by script at runtime)
# keyword: <string>
# lsi: <string, comma separated>
# date: <YYYY-MM-DD>
# tags: <json list string>
# ----------------------------------------------------

你要输出一篇“中文搜索落地页”风格的专业文章（后续会被人工翻译），围绕主关键词：{{keyword}}。
目标：覆盖用户真实查询意图（怎么做/参数/规范/对比/排查），让读者看完能立刻落地，并愿意咨询。

## 输出硬约束（必须遵守）
1) 只输出最终 Markdown，首字符必须是 `---`（Front Matter），不得输出任何解释/思考过程。
2) 禁止出现“作为AI/我将/下面我会”等话术。
3) 必须出现且仅出现一次：`<!-- COMPONENT: BlogQuickQuoteInline -->`（放在 TL;DR 之后）。
4) 文内必须包含 ≥3 条 `https://hilpcb.com/en/...` 的 Markdown 链接（锚文本要多样）。
5) 品牌：首提用 `HILPCB（HilPCB PCB Factory）`，全文共 3–5 次，避免营销口吻。
6) 字数：中文 2200–3500 字（不含 Front Matter），段落 2–4 句/段，短句优先，便于翻译。

## SEO与意图（必须落地成页面组件）
- 主关键词：{{keyword}}（出现于：title、description、首段、至少1个H2、结尾）
- LSI：{{lsi}}（自然使用即可，不要为次数硬塞；优先用于H2/表格/FAQ）

## Front Matter（必须按此字段输出）
---
title: "<中文释义短语（10–18字）>（{{keyword}}）：<查询式标题，含“指南/规则/参数/排查”之一>"
description: "用1句回答用户搜索：你会给出哪些规则/参数/清单/排查路径（包含{{keyword}}）。"
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 8
tags: {{tags}}
---

## 页面结构（必须包含以下H2，顺序一致）
## TL;DR（30秒结论）
- 3–6 条结论，包含：1条关键规则、1个推荐参数范围、1个常见坑、1个验证方法、1个适用/不适用边界

<!-- COMPONENT: BlogQuickQuoteInline -->

## 你可能正在搜索的8个问题（长尾覆盖）
- 用用户口吻写 8 条查询（例：怎么做/为什么/多少/对比/哪种更好/如何验证/常见失败原因）

## 适用场景与不适用场景
- 各给 3–5 条，避免泛泛而谈

## 规则与参数表（核心SEO模块）
用表格输出：规则/推荐值(范围)/为什么/怎么验证/不这样做会怎样
至少 10 行；参数用“范围+条件”，不确定就写“建议范围+影响因素”，不要编具体实验数据。

## 设计/工艺落地步骤（按1→N）
- 6–10 步，每步：动作 + 关键参数 + 验收点（可被工程师照着做）

## 常见失效模式与排查（问题解决模块）
- 列 6–10 个：现象 → 最可能根因(2–3个) → 快速排查 → 对策 → 预防

## 选型与决策（让读者做选择）
- 给一个简单决策树（用列表即可）：如果…选A；如果…选B；并写清代价/风险

## FAQ（8–12问，覆盖PAA）
每问需包含：简答(1–2句) + 关键点(2–4条)；问题要像真实搜索句。

## 进一步阅读与工具（必须含内链）
至少放 3–5 个内链（示例锚文本要自然多样）：
- [Flex PCB](https://hilpcb.com/en/products/flex-pcb)
- [Rigid-Flex PCB](https://hilpcb.com/en/products/rigid-flex-pcb)
- [SMT Assembly](https://hilpcb.com/en/products/smt-assembly)
- [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly)
- [Impedance Calculator](https://hilpcb.com/en/tools/impedance-calculator)

## 术语表（中英对照，便于翻译一致性）
用表格输出：中文术语 | English | 备注（怎么用/易错点）
至少 10 行，包含主关键词相关术语。

## 结语（含CTA但不硬广）
- 复述主关键词 + 给出“下一步动作”（例如：DFM检查/可制造性评审/报价所需资料清单 3–5 条）

## 自检清单（输出前逐条确认，确认后不要把清单写出来）
- 是否满足硬约束 1–6
- 是否有 ≥3 条 hilpcb 内链
- 是否包含全部H2且顺序一致
- 是否有“规则与参数表/FAQ/术语表”
