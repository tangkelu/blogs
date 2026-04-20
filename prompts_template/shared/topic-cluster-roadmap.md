# Shared Topic Cluster Roadmap

这是跨站点通用的高优先级主题路线图，用来回答“先做哪些 cluster”。

更完整的集群组织方法见：

- `keyword-cluster-design-standard.md`
- `competitive-keyword-source-standard.md`

## 高优先级主集群

### 1. High-Speed / Impedance / SI

适合先做的原因：

- 技术门槛高
- 高商业价值
- 易承接到高附加值产品、材料、工具页

### 2. HDI / Microvia / Fine Pitch

适合先做的原因：

- 工艺与可靠性问题密集
- 查询意图和报价意图都强
- 适合做高技术壁垒内容

### 3. Rigid-Flex / Flex Reliability

适合先做的原因：

- 设计与制造 trade-off 明显
- 容易形成 pillar + 多 query 的结构

### 4. PCBA / Assembly / Yield

适合先做的原因：

- 缺陷、测试、BOM、工艺、装配问题丰富
- 易形成商业承接

### 5. Materials / Surface Finish / Thermal

适合先做的原因：

- 选材类与比较类关键词多
- 很适合 comparison 与 application 模块

### 6. Reliability / Validation / Compliance

适合先做的原因：

- 能提升站点权威性
- 适合补标准、验证、失效模式、验收框架

### 7. Manufacturing / Cost / Lead Time

适合先做的原因：

- 直接连接 RFQ、打样、交付和采购决策
- 对转化帮助最直接

### 8. Industry Applications

适合先做的原因：

- 能把技术能力与终端场景连接起来
- 对 APTPCB 的 `industries/` 结构尤其重要

## 路线图使用方式

建议顺序：

1. 每个 cluster 先确定 pillar
2. 再补最强商业 query
3. 再补高频 how-to / troubleshooting / comparison
4. 再扩展长尾 FAQ 和应用型内容

如果 topic 来源于竞品 organic keyword 导出表，还要增加一步：

0. 先按 `competitive-keyword-source-standard.md` 做剔除、意图重分组、业务域重分组和 evidence gate

## 不建议的做法

- 先批量生成大量散 query，再回头补 hub
- 用同一标题骨架覆盖所有 cluster
- 只做 informational，不做承接路径设计
