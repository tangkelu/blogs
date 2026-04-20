# Template Selection And Pruning Standard

本文件用于回答四个问题：

1. 现在还保留哪些主模板
2. 哪些旧模板要降级或淘汰
3. 不同关键词意图该怎么选模板
4. 顶级 PCB / PCBA 博客的结构经验，哪些应该进入模板

## 一、结论先行

基于现有旧模板、关键词脚本和头部行业博客模式，后续模板体系应当收敛为：

- 主模板只保留 `Query` 与 `Pillar`
- `Playbook` 不再作为一级主模板，只保留为可选模块风格
- `Story` 不再作为常规模板，只作为极少数品牌叙事型专题的写法参考
- `Comparison`、`Application`、`Capability` 改为按意图加载的模块，而不是独立模板

换句话说，今后的结构应该是：

`共享骨架（Query / Pillar） + 意图模块 + 站点 overlay + 证据包`

## 二、为什么要这样裁剪

### 顶级博客真正稳定出现的，不是“模板种类很多”

头部 PCB / PCBA 内容的共同点更接近：

- 开头直接回答问题
- 很快给出表格、规则、决策框架
- 中段用设计 / 制造 / 验证 / 风险结构展开
- 自然放入采购、DFM、打样、能力承接
- FAQ 与术语表只在主题确实需要时补充

它们并没有稳定证明“每个主题都需要独立的 playbook / story / cheat sheet / glossary / supplier checklist 大全套”。

### 旧模板的问题

旧 APTPCB v5/v6 模板的主要问题是：

- 主模板数量过多，使用者很难判断何时选用
- 把很多高负担结构写成强制项
- 大量 HTML 卡片、清单、cheat sheet、glossary 被固定写死
- 页面经常先满足模板，再满足搜索意图
- 同一篇文章容易出现信息重复

结果是：

- 生成成本高
- 维护难
- 结构僵硬
- 对技术博客最重要的“证据、参数、验证方法”反而不够突出

## 三、保留 / 合并 / 淘汰清单

### 保留为一级主模板

#### 1. Query

适用于：

- `what is`
- `how to`
- `cost`
- `lead time`
- `troubleshooting`
- `X vs Y`
- 某个具体规则、参数、失效模式、工艺问题

保留原因：

- 头部技术博客大量页面本质上都是“工程问题解答页”
- 易于承载直接回答、规则表、步骤、排查、FAQ、商业承接

#### 2. Pillar

适用于：

- 主题型指南
- 行业型大主题
- 工艺 / 材料 / 板型 / 验证体系的专题枢纽页

保留原因：

- 适合做主题中心页和站内集群 hub
- 能承接定义、设计、制造、验证、选型、误区、相关子话题

### 降级为可选模块或风格

#### 3. Playbook

处理方式：

- 不再作为一级模板
- 只保留“采购 / 供应商评估 / RFQ / 验收 / 风险控制”模块能力

保留内容：

- 供应商资格清单
- RFQ 资料清单
- 验收与验证路径
- 采购决策规则

丢弃内容：

- 把整篇文章都写成采购剧本
- 强制所有文章进入 buyer playbook 结构

#### 4. Story

处理方式：

- 不再作为常规生产模板
- 只作为品牌专题、案例式深读、复杂 trade-off 叙事的特殊写法参考

保留内容：

- 用具体场景解释复杂技术冲突
- 用“实验室表现 vs 量产现实”的叙事方法解释 trade-off

丢弃内容：

- 每篇技术博客都必须有故事化开头
- 为了“可读性”牺牲直接回答和工程结构

### 保留为按意图加载的模块

#### 5. Comparison 模块

适用：

- `X vs Y`
- `difference between`
- `how to choose A or B`

必须补充：

- 比较表
- 决策规则
- 例外边界

#### 6. Application 模块

适用：

- `applications`
- `used in`
- 行业应用型关键词

必须补充：

- 行业 / 场景表
- 不同行业约束
- 场景下的验证动作

#### 7. Capability 模块

适用：

- `manufacturer`
- `service`
- `quote`
- `MOQ`
- `lead time`
- `cost`

必须补充：

- 能力快照
- lead time / MOQ / RFQ 清单

限制：

- 只能使用站点已公开能力
- 不能让 capability 内容压倒技术主体

## 四、模板选择规则

### Query 触发条件

满足以下任一情况，优先用 `Query`：

- 关键词是单个问题或单个决策
- 用户想知道“是什么 / 怎么做 / 为什么失败 / 怎么选 / 多少钱 / 多久”
- 文章主目标是解决一个工程问题
- 文章预计不会成为某个主题集群的 hub 页

典型关键词：

- `pcb impedance control`
- `microvia reliability`
- `ENIG vs OSP`
- `pcb assembly cost`
- `how to prevent pcb warpage`

### Pillar 触发条件

满足以下任一情况，优先用 `Pillar`：

- 关键词本身是一个大主题
- 后续会围绕它持续扩展子文章
- 页面要承担专题 hub 或内容中心的职责
- 需要系统覆盖定义、设计、制造、验证、误区和下一步

典型关键词：

- `high speed pcb`
- `rigid flex pcb`
- `pcb stackup`
- `pcb surface finish`
- `pcb testing and inspection`

### 模块叠加规则

- `X vs Y`：`Query + Comparison`
- 应用行业：`Query/Pillar + Application`
- 报价、MOQ、交期、制造商能力：`Query/Pillar + Capability`
- 采购导向强但仍是技术问题：优先 `Query + Capability`，不要直接切成 Playbook

## 五、哪些结构必须保留，哪些不要强制

### 必须保留的结构原语

这些是头部技术博客反复证明有效的结构：

- 开头直接回答
- 关键规则或关键参数表
- 设计 / 制造 / 验证 / 风险其中至少两个视角
- 明确的 decision framing
- FAQ
- 自然商业承接
- 指向产品 / 服务 / 工具 / 资源页的内链

### 条件性保留的结构

这些结构只在主题确实需要时才启用：

- TOC
- Glossary
- Supplier qualification checklist
- Cheat sheet
- 行业应用表
- 详细 capability 表
- 大段采购流程

启用条件是“有助于该关键词的真实意图”，而不是“旧模板里有”。

### 不应再强制的内容

- 每篇都必须有大块 HTML 卡片
- 每篇都必须有 glossary
- 每篇都必须有 supplier checklist
- 每篇都必须有 cheat sheet
- 每篇都必须做成 buyer playbook
- 每篇都必须讲故事

## 六、推荐的最小模板体系

### Query 最小骨架

- frontmatter
- 直接回答
- 关键规则 / 参数表
- 设计 / 制造 / 排查 / 选型中的 2-4 个主题块
- FAQ
- 下一步 / CTA
- 作者与审核信息

### Pillar 最小骨架

- frontmatter
- 核心结论
- 定义与边界
- 总览表
- 设计 / 制造 / 验证 / 选型 / 误区
- 相关子话题入口
- FAQ
- 结语 / CTA
- 作者与审核信息

## 七、以后写模板时的原则

- 模板负责结构，不负责替代证据
- 模板负责回答意图，不负责堆砌栏目
- 模板要先服务工程读者，再服务 SEO
- 模板要适配不同站点的承接页，不直接写死商业路径
- 模板只保留高频有效原语，低频结构改为可选模块

## 八、对旧体系的处理建议

- 继续保留 `Query.md` 与 `Pillar.md` 作为兼容入口
- `Playbook` 与 `Story` 不再新增为 shared 主模板
- 旧 v5/v6 中有价值的模块逻辑，迁移到 shared 标准文档中
- 以后新增模板前，先回答：
  - 它是新意图，还是旧意图的模块？
  - 头部博客里是否真的存在稳定对应形态？
  - 不新增这个模板，是否也能用 Query / Pillar + 模块解决？
