# Shared Evidence Pack Template

本模板用于所有站点的技术博客证据增强。

目标不是单纯“补几个数字”，而是先把一篇技术博客的可写信息拆清楚：

- 哪些是公开可验证事实
- 哪些是项目级工程判断
- 哪些不能写成硬事实
- 哪些段落值得放正文锚点

凡是能直接支撑正文、FAQ、表格或锚点的行，都尽量补齐 `fact_id`、`source_id` 和 `status`。

## 1. Topic Summary

- 主题：
- 主关键词：
- 次关键词：
- 页面类型：`query` / `pillar`
- 搜索意图类型：
  - 信息型 / 商业调查型 / 设计决策型 / 工艺控制型 / 风险分析型
- 目标读者：
- 站点：
  - HILPCB / APTPCB

## 2. Source Facts

先从原始博客、简稿、技术 memo 里抽出已有硬信息。

### 已有硬信息

- 协议 / 标准：
- 材料 / 家族 / 型号：
- 结构 / 工艺：
- 已有数字：
- 已有测试 / 验证方法：
- 已有应用场景：

### 原文弱点

- 哪些地方只有定性描述：
- 哪些地方明显缺证据：
- 哪些地方像工程经验但没有适用范围：
- 哪些地方疑似把经验值写成行业统一标准：

## 3. Claim Extraction

真正写作前，先把主题里的 candidate hard claims 抽出来。

典型要抽的对象：

- 协议代际、速率、Nyquist 语境
- 标准名称、class 名称、测试名称
- 材料 Dk / Df / Tg / CTI / 粗糙度语境
- 阻抗、背钻、铜厚、孔结构、公差
- 热、可靠性、环境测试方法
- 连接器 / 表面处理 / 板材家族参数

## 4. Classification

### A. Publicly Verifiable Facts

只能放“能被一级来源直接支撑”的内容。

| Claim | fact_id | source_id | Why it matters | Source type | Status |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | standard / consortium / datasheet / whitepaper / regulator | verified / must_refresh |

### B. Project-Level Judgments

这些内容可以写，但必须带适用范围，不能伪装成统一行业硬标准。

默认 `framing_only`。

| Judgment / control point | fact_id | source_id | Scope | Safe wording | Status |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | 作为项目级 DFM 目标 / 试产拦截项 / 量产评审关注点 | framing_only |

### C. Site-Specific Capability References

这些内容默认 `supplier_scoped_dated_only`。如果只是 site CTA / 承接页引用，才用 `framing_only`，且不要升格为共享能力事实。

| Capability | fact_id | source_id | Site path / source | Allowed wording | Status |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | 仅作为站点公开能力写入 | supplier_scoped_dated_only |

### D. Unsupported / Unclear

这些内容默认不能写成硬事实。请明确拆成两类：

| Claim | fact_id | source_id | Why unclear | Downgrade method | Status |
| --- | --- | --- | --- | --- | --- |
|  |  |  | 明显缺证据或无法安全降级 | 删除 / 改为定性风险 / 改成项目级判断 | blocked |
|  |  |  | 可能过期、需要刷新后才能使用 | 刷新来源后再写 | must_refresh |

## 5. Primary Sources

只收录一级来源。

### Standards / Consortia

- 名称：
- 链接：
- 可引用内容：

### Public Institutions / Regulators

- 名称：
- 链接：
- 可引用内容：

### Official Datasheets / White Papers / App Notes

- 公司 / 组织：
- 链接：
- 可引用内容：
- 是否适合在正文显式露出：

说明：

- 优先露出标准组织 / 联盟 / 监管机构锚点
- 供应商资料可作为内部核验来源
- 除非策略允许，否则不要在最终成稿中大面积露出商业供应商外链

## 6. Usable Technical Facts

这里只放已经核实、可安全进入文章的事实。

| Fact | fact_id | source_id | Source type | Status | How to write it safely |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | verified | 根据 xx 官方资料 / 从 xx 公布的语境看 / 按 xx 框架 |

## 7. Article Data Targets

用于约束本篇文章的数据密度和结构层级。

- 目标最低公开技术事实数：
- 目标最低正文官方锚点数：
- 是否必须有早期事实表：是 / 否
- 是否必须有第二层早期结构化信息块：是 / 否
- 第二层结构建议：
  - 4-card UI block / 额外 markdown tables
- 是否适合 glossary：是 / 否
- 是否适合 supplier checklist：是 / 否

建议：

- SI / 材料 / 阻抗 / 背钻 / EMC / 安规 / 可靠性 / 测试主题，默认应有更高数据密度
- 如果公开硬数据少，也至少补足标准语境、验证方法、项目级检查项

## 8. In-Body Citation Plan

提前规划哪些段落值得放正文锚点。

| Article section | Claim to support | Planned source |
| --- | --- | --- |
|  |  |  |

原则：

- 锚点要放在最关键的判断句里
- 不要堆链接
- 同一来源不要正文引用后又在文末重复堆一遍

## 9. AI-SEO Evidence Primitives

这一部分不是可选项。它的目标是让后续写作阶段直接拿到“可被 AI 抽取、可被作者自然写进正文、可被引用”的证据原料。

### A. Quick Answer / Definition Material

先准备一段适合放在文章前部的定义型摘要素材。

| Field | Requirement |
| --- | --- |
| Core definition | 用一句话定义“它是什么” |
| When it matters | 用一句话定义“什么时候需要重点关注” |
| Deciding factor | 用一句话定义“最关键判断依据是什么” |
| Safe short version | 整合成 40-60 词左右、可独立成立的 quick answer 草稿 |

要求：

- 必须能脱离全文独立成立
- 不要带品牌话术
- 不要写没有来源支撑的硬数字

### B. Inline Citation Handles

先把正文可能出现的关键结论，转换成可直接写进句子的来源句柄。

| Claim cluster | Inline citation handle | Source URL | Safe sentence pattern |
| --- | --- | --- | --- |
|  |  |  |  |
|  | 例如：根据 USB-IF 规范 / NXP layout guide 指出 / Rogers datasheet 给出 |  | 例如：根据 xx 规范，… |

要求：

- 至少准备 3 组 inline citation handles
- 优先覆盖数字、标准目标、材料参数、测试方法、典型设计约束
- 句柄必须自然，能直接嵌入正文，不要只保留裸链接

### C. Authority / Reviewer Inputs

先准备作者与审核信息所需的权威素材。

| Field | fact_id | source_id | Content | Status |
| --- | --- | --- | --- | --- |
| Author entity |  |  | 真实作者 / 技术团队 / 内容团队实体 | framing_only |
| Reviewer entity |  |  | 审核人 / 工程评审团队 / SI 或制造审核团队 | framing_only |
| Credentials or scope |  |  | 职能边界、审核责任、专题覆盖范围 | framing_only |
| Public profile / entity URL |  |  | 如有可公开实体页则填入 | verified / framing_only |
| Safe fallback wording |  |  | 如果没有真实姓名，最终如何安全表述 | framing_only |

要求：

- 优先准备真实可识别实体
- 如果没有真实姓名，也要写清团队边界和审核责任
- 不允许最终页面只剩空泛“编辑部”式弱权威表述

### D. FAQ Query Phrasing Seeds

先把 FAQ 的高频问法按真实搜索语言写出来。

| User query style | fact_id | source_id | Mapped FAQ question | Source / evidence basis | Status |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  | framing_only |

要求：

- FAQ 问法优先接近自然语言搜索问句
- 不要只写目录式标题改写
- 至少准备 4 个 query phrasing seeds

## 10. Handoff To Template

- 建议模板：`query` / `pillar`
- 建议模块：
  - comparison / application / capability / none
- 建议标题类型：
  - 定义 / 设计决策 / 制造控制 / 风险失效 / 选型对比
- 推荐早期表格类型：
- 推荐第二层结构块类型：
- 推荐站点承接页：
- 推荐正文锚点：
- 推荐 FAQ 补点：

## 11. Final Preflight

交给模型前先检查：

- 是否已经抽出硬信息
- 是否已经分出 `公开事实 / 项目判断 / 站点能力 / 不清楚`
- 是否已经准备好一级来源
- 是否已经明确哪些数字不能写成硬事实
- 是否已经为正文锚点做了最小规划
- 是否已经准备 quick answer 素材
- 是否已经准备 inline citation handles
- 是否已经准备作者 / 审核权威素材
- 是否已经准备 FAQ query phrasing seeds
- 是否已经决定本篇应该用 `query` 还是 `pillar`

如果以上任一项为空，这篇技术博客通常还不适合直接进入“高质量证据增强型写作”。
