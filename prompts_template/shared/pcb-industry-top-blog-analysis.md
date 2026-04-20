# Shared PCB Industry Top Blog Analysis

这份文档不是流量榜单，而是“头部 PCB / PCBA 技术博客为什么有效”的结构分析摘要。

目标是回答：

- 哪些经验应进入模板
- 哪些旧要求应当删除
- 技术博客应该怎样组织信息、数据和内链

## 一、共性结论

高表现 PCB / PCBA 内容更像工程知识页，不像普通资讯博客。

反复出现的有效组合是：

- 开头直接回答
- 很快出现表格或规则框架
- 用设计 / 制造 / 验证 / 风险结构展开
- 明确告诉读者“什么时候该选 A，不该选 B”
- 在正文中自然接入 DFM、材料、制造、测试、打样、报价路径

## 二、对标对象

对标时可优先参考这些类型的站点：

- Sierra Circuits / ProtoExpress
- Altium Resources
- MacroFab
- Eurocircuits
- Epec

注意：

- 借鉴的是结构、信息密度、问题 framing、表格 schema
- 不是照抄内容、数字或话术

## 三、这些站点通常做对了什么

### 1. 先回答问题，再讲背景

好的页面通常在很前面就完成：

- 定义
- 边界
- 为什么重要
- 先看哪些参数

而不是用很长的行业背景铺垫。

### 2. 表格不是装饰，而是决策工具

高质量页面常见的表格类型包括：

- 规则 / 参数 / 验证表
- 材料或工艺比较表
- 风险 / 失效 / 预防表
- 场景 / 约束 / 检验表

值得保留到模板里的不是“必须有很多表”，而是：

- 当读者需要比较、验证、筛选时，就应优先表格化

### 3. 主体结构接近工程流程

常见高效结构：

- 定义 / scope
- rules / specs
- process / implementation
- failure modes / troubleshooting
- validation / acceptance
- decision rules

这也和现有 `deep_read_top_rank_blogs.py` 的意图归类相吻合：

- `comparison_vs` 更适合 `query + comparison`
- `how_to` 更适合 `query`
- `definition_meaning` 更适合 `query`
- `cost` / `lead_time` 更适合 `query + 更强表格`
- `troubleshooting` 更适合 `query + failure-mode`
- 宽主题更适合 `pillar`

### 4. 商业承接是“工程下一步”，不是硬插 CTA

头部行业页面更自然的做法是：

- 当讲到 stackup、材料、DFM、测试、交期、RFQ 时，顺势引到对应解决页
- 承接动作与内容逻辑一致

这正是我们现在要采用的原则：

- 产品 / 服务 / 能力 / 工具页优先
- 博客互链次之

## 四、从这些站点得到的模板启发

### 应该进入模板的

- 直接回答
- 规则 / 参数 / 对比表
- 设计 / 制造 / 验证 / 风险中的核心视角
- decision framing
- FAQ
- 自然商业承接

### 应该从强制项中删除的

- 每篇都必须 glossary
- 每篇都必须 supplier checklist
- 每篇都必须 cheat sheet
- 每篇都必须大量 HTML 卡片
- 每篇都必须 narrative story
- 每篇都必须 buyer playbook 化

## 五、关键词与章节形态的映射

### 比较型关键词

常见优胜结构：

- 先下结论
- 再做 factor-by-factor comparison
- 最后写 how to choose

### how-to / 定义型关键词

常见优胜结构：

- definition / scope
- rules / specs
- implementation / checks
- common mistakes / troubleshooting

### 成本 / 交期型关键词

常见优胜结构：

- 先给影响因素
- 用表格拆因素
- 再解释不同窗口如何变化

### 排障型关键词

常见优胜结构：

- symptom
- likely causes
- what to check
- fix
- prevention

## 六、对我们当前模板系统的直接影响

基于以上观察，模板系统应当变成：

- `Query` 与 `Pillar` 两个主骨架
- `Comparison`、`Application`、`Capability` 三个模块
- `Playbook` 与 `Story` 从一级模板降级

这比旧体系更接近头部行业内容的真实结构。

## 七、对写作和数据组织的影响

头部页面之所以更强，不只是因为结构，而是因为它们通常能做到：

- 结论后面跟参数或依据
- 建议后面跟验证动作
- trade-off 不是空话，而是有边界条件

所以我们自己的体系必须把：

- 模板选择
- 关键词集群
- 数据组织

拆成独立标准，而不是全部塞进一个大 prompt。
