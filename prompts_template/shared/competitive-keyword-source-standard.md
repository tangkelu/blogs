# Competitive Keyword Source Standard

本文件定义如何使用 `/code/blogs/top_blog_keywords` 这类竞品 organic keyword 导出表。

目标不是把原始 xlsx 直接拿来当内容计划，而是把它们转成：

- 可执行的 topic cluster
- 可执行的 pillar / query 候选池
- 可执行的商业承接路径设计

## 一、先给结论

`top_blog_keywords` 里的数据有价值，但它不是“现成可执行的关键词集群”。

它的正确定位是：

- 竞品关键词来源池
- 搜索需求信号池
- query 发现池
- cluster 补充池

它不应直接作为：

- 最终选题清单
- 直接批量生成输入
- 不经筛选的 query 列表

## 二、这类原始表通常包含什么

竞品 organic keyword 导出表通常包含：

- `Keyword`
- `Position`
- `Search Volume`
- `Keyword Difficulty`
- `URL`
- `Traffic`
- `Keyword Intents`
- `SERP Features`

这些字段能回答的是：

- 哪些主题正在被搜索
- 哪些 query 为竞品带来可见流量
- 哪些 URL 在承接某类意图
- 哪些 SERP 形态更适合结构化内容

但它不能直接回答：

- 这些词是否适合 HILPCB / APTPCB 商业承接
- 这些词是否应该做成 pillar 还是 query
- 这些词是否会与现有页面 cannibalize
- 这些词是否有足够 evidence 可写

## 三、为什么不能直接拿来当关键词集群

如果把竞品导出表直接当 cluster，会立刻出现四类问题：

### 1. 品牌词与导航词混入

典型问题：

- 竞品品牌词
- 首页导航词
- 与竞品强绑定的产品名

这些词对我们没有 cluster 价值。

### 2. 泛电子词混入

有些词搜索量高，但并不服务 PCB / PCBA 的专业承接，例如：

- 过泛的电子基础词
- 偏教学百科词
- 与站点承接页距离太远的概念词

### 3. 意图混乱

原始导出表会把这些混在一起：

- informational
- commercial
- navigational
- comparison
- capability
- brand

如果不先按意图拆分，后续模板选择会失真。

### 4. URL 归因来自竞品，不来自我们

竞品某个 URL 能吃到一个词，不代表我们也该用同样结构承接。

我们必须重新判断：

- 这个词是否与我们的业务域匹配
- 应该承接到产品 / 服务 / 能力 / 工具 / 博客中的哪一层

## 四、正确使用流程

### 第一步：只把它当来源池，不当结论

先承认：

- 竞品 rank 了，不代表我们必须写
- 竞品有流量，不代表适合我们
- volume 高，不代表转化高

### 第二步：先做剔除

先删除以下类型：

- 竞品品牌词
- 导航词
- 明显跑偏的泛电子词
- 与 PCB / PCBA 商业承接弱相关的词
- 没有明确内容边界的超级宽泛词

### 第三步：按意图重分组

所有候选词先映射到：

- `definition_meaning`
- `how_to`
- `comparison_vs`
- `cost`
- `lead_time`
- `troubleshooting`
- `capability_transactional`
- `industry_application`
- `pillar_overview`

不要先按词面分组，再补意图。  
必须先按意图分流。

### 第四步：按业务域重分组

再把词放入业务域：

- PCB fabrication
- PCBA assembly
- Materials
- High-speed / RF / impedance
- HDI / microvia
- Flex / rigid-flex
- Testing / inspection
- Reliability / compliance
- Industry applications
- Manufacturing / cost / lead time

### 第五步：决定是 Pillar 还是 Query

判断原则：

- 大主题、可持续扩展、多 query 可围绕它展开的，归 `pillar`
- 单个问题、单个比较、单个排障、单个决策的，归 `query`

### 第六步：补承接路径

每个候选词都必须回答：

- 最终承接到哪个站点路径
- 优先是产品页、服务页、能力页、工具页，还是次级博客页
- 站内谁是 hub，谁是 spoke

### 第七步：过 evidence gate

在进入生产前，再判断：

- 是否能准备 evidence pack
- 是否有足够公开事实或可安全表达的工程判断
- 是否会逼模型编数字

过不了 evidence gate 的词，不进入近期执行集群。

## 五、评估优先级时要看什么

### 可以提高优先级的信号

- 搜索量不错
- keyword intent 清晰
- 明显属于工程问题或采购问题
- 能承接到高价值产品 / 服务 / 工具页
- 适合做表格、比较、验证、DFM、FAQ
- 与我们既有 cluster 结构高度一致

### 应该降级或淘汰的信号

- 品牌 / 导航意图过强
- 纯百科流量，商业承接极弱
- 内容边界太宽，短期做不成高质量页面
- 需要大量不可验证数字
- 与现有页面高度重叠

## 六、推荐字段

如果后续要把原始表提炼成可执行 cluster 表，建议至少保留这些字段：

| 字段 | 作用 |
| --- | --- |
| `source_domain` | 来自哪个竞品域名 |
| `keyword` | 原始关键词 |
| `search_volume` | 搜索量 |
| `keyword_difficulty` | 竞争难度 |
| `traffic_signal` | 流量信号 |
| `intent_bucket` | 意图分类 |
| `domain_bucket` | 业务域分类 |
| `cluster` | 主题集群 |
| `topic_type` | pillar / query |
| `business_fit` | 对 HILPCB / APTPCB 的适配度 |
| `evidence_readiness` | evidence 可准备度 |
| `primary_destination` | 产品 / 服务 / 工具 / 博客承接页 |
| `status` | keep / watch / drop |
| `notes` | 备注 |

## 七、与 `prompts_template` 的关系

竞品关键词原始表本身不应进入生产 prompt。

真正应该沉淀进 `prompts_template` 的，是它提炼出的结果：

- `shared/topic-cluster-roadmap.md`
- `shared/keyword-cluster-design-standard.md`
- 站点 content map
- 站点 internal link map

换句话说：

- 原始 xlsx 是 research layer
- `prompts_template` 才是 execution layer

## 八、对 `/code/blogs/top_blog_keywords` 的建议

建议定位：

- 保留为研究原始库或归档库
- 不作为生产目录
- 不直接参与批量生成

如果后续已经把里面的高价值模式提炼完成，就可以：

- 归档
- 或删除原始表

前提是：

- 集群标准
- cluster roadmap
- 站点 content map

已经足够承接它的精华。
