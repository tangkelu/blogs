# Source Governance

Last updated: 2026-04-24

## 来源优先级

冲突时按以下优先级处理：

1. 标准组织 / 监管机构
2. 原始制造商 / 原厂 datasheet / 原厂工艺指南
3. 官方财报 / 投资者披露
4. 官方公共数据库
5. 内部工程审核记录
6. 行业媒体与博客

低优先级来源不得覆盖高优先级来源。

## 来源类型

允许的高优先级来源类型：

- `standard`
- `regulation`
- `datasheet`
- `processing_guide`
- `technical_note`
- `dataset`
- `annual_report`
- `investor_filing`
- `official_product_page`

不作为事实主源的类型：

- `blog`
- `seo_article`
- `reseller_copy`
- `forum_post`

可作为二级支持层的类型：

- `internal_blog`
- `internal_note`
- `internal_product_page`
- `internal_capability_claim`

这些来源可以用于：

- 帮助组织主题页结构
- 提供内部术语和工程表达
- 标记你们已经覆盖过的应用方向
- 沉淀你们自己站内已经公开承诺的工艺与验证能力

这些来源不可以用于：

- 覆盖官方 datasheet 数值
- 覆盖标准或法规结论
- 单独支撑高风险参数断言
- 在未复核前当作最终认证、交期、量产能力上限或测试频段上限的确定事实

## 动态数据规则

以下内容默认视为动态数据：

- 价格
- 交期
- 产能
- 最新认证状态
- 市场规模
- 市场份额
- 豁免状态
- SVHC 数量
- 最新法规截止日期

这类数据必须：

- 标注日期
- 记录核查时间
- 设置 `must_refresh: true`

## 数值规则

任何数值型事实都应尽量附带：

- 测试方法
- 频率
- 温度
- 厚度或铜厚
- 条件说明

禁止把不同测试方法下的值合并成一个“标准值”。

## 冲突规则

当来源冲突时：

1. 保留冲突，不强行抹平
2. 记录各自来源和日期
3. 标记为 `needs_review`
4. 不在博客中当成确定事实直接断言

## 发布时间与核查时间

每条来源都必须尽量记录：

- `published_at`
- `checked_at`

如果缺少发布时间，必须在 notes 中说明。

## 刷新周期

- `standard`: 90 天检查一次 revision metadata
- `datasheet`: 180 天检查一次
- `processing_guide`: 180 天检查一次
- `regulation`: 30 天检查一次
- `dataset`: 30 天检查一次
- `annual_report`: 每个报告周期检查一次

## 发布前硬规则

如果博客中使用了以下内容，必须临发布前再查官方：

- RoHS / REACH / SVHC 状态
- 最新标准版本
- 当前企业能力与认证
- 市场类数字
- 时间敏感新闻
