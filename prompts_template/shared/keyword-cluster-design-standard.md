# Keyword Cluster Design Standard

本文件定义 PCB / PCBA 博客的关键词集群怎么组织，避免出现：

- 集群太散，文章之间互相抢词
- 集群只按词面分类，不按搜索意图分类
- 只堆 informational 词，没有商业承接路径
- 站点内容结构和关键词结构脱节

## 一、集群设计目标

一个健康的关键词集群必须同时满足四件事：

1. 搜索意图清晰
2. 站内承接路径清晰
3. 页面之间不互相内耗
4. 能把读者从“查概念”逐步带到“选方案 / 提交 RFQ / 下单评估”

补充原则：

- 不把竞品 keyword export 直接当集群
- 竞品 ranking 词只能作为来源池，必须先经过意图、业务域、承接路径和 evidence 的四重筛选

如需处理 `/code/blogs/top_blog_keywords` 这类原始库，先读：

- `competitive-keyword-source-standard.md`

## 二、集群设计的基本单位

不要只按“关键词列表”管理，而要按四层结构管理：

### 1. Domain

站点级业务域，例如：

- PCB fabrication
- PCBA assembly
- Materials
- Testing and inspection
- Reliability and compliance
- Industry applications

### 2. Cluster

主题集群，例如：

- High-speed / impedance
- HDI / microvia
- Rigid-flex / flex reliability
- Surface finish
- Thermal management
- Assembly defects

### 3. Pillar Topic

每个集群中的主题 hub，例如：

- `high speed pcb`
- `rigid flex pcb`
- `pcb surface finish`
- `pcb assembly defects`

### 4. Query Topic

围绕 pillar 展开的具体问题页，例如：

- `what is controlled impedance pcb`
- `ENIG vs OSP`
- `pcb warpage causes`
- `microvia aspect ratio`
- `flying probe vs ict`

## 三、先按意图分组，再按词面分组

每个关键词在进入集群前，先判定意图，再决定归属。

### 主要意图类型

- `definition_meaning`
- `how_to`
- `comparison_vs`
- `cost`
- `lead_time`
- `troubleshooting`
- `capability_transactional`
- `industry_application`
- `pillar_overview`
- `brand_or_navigational`

### 归类规则

- `what is`、`meaning`、`definition` 归入定义型 Query
- `how to`、`design rules`、`checklist` 归入操作型 Query
- `vs`、`difference`、`choose` 归入比较型 Query
- `cost`、`price`、`quote` 归入商业 Query
- `lead time`、`turnaround` 归入交付 Query
- `failure`、`defect`、`root cause` 归入排障 Query
- 宽主题主词归入 Pillar
- 竞品品牌词、导航词、明显跑偏词先剔除，不进入 cluster

## 四、推荐集群框架

### A. 制造与报价集群

目标：

- 承接采购、制造、交期、MOQ、报价、能力相关需求

Pillar 例子：

- PCB manufacturing
- PCB fabrication process
- Turnkey PCBA

Query 例子：

- pcb manufacturing cost
- pcb prototype lead time
- turnkey pcb assembly process
- how to request pcb quote

优先承接页：

- HILPCB: `products/`、`services/`、`quote/`
- APTPCB: `pcb/`、`pcba/`、`capabilities/`、`quote/`

### B. 高速 / RF / 阻抗集群

目标：

- 承接高附加值设计与制造主题

Pillar 例子：

- high speed pcb
- controlled impedance pcb
- high frequency pcb

Query 例子：

- stripline vs microstrip impedance
- impedance control tolerance
- how to design differential pairs on pcb
- rogers vs fr4 for rf pcb

优先承接页：

- HILPCB: `products/high-speed-pcb`、`products/high-frequency-pcb`、`tools/impedance-calculator`
- APTPCB: `pcb/high-speed-pcb`、`pcb/high-frequency-pcb`、`materials/rf-rogers`、`tools/impedance-calculator`

### C. HDI / Microvia / Fine Pitch 集群

Pillar 例子：

- hdi pcb
- microvia design

Query 例子：

- stacked vs staggered microvia
- microvia reliability issues
- hdi pcb cost drivers
- fine line pcb manufacturing limits

优先承接页：

- HILPCB: `products/hdi-pcb`
- APTPCB: `pcb/hdi-pcb`、`capabilities/`

### D. Flex / Rigid-Flex 集群

Pillar 例子：

- rigid flex pcb
- flex pcb design

Query 例子：

- rigid flex bending radius
- rigid flex stackup guide
- flex pcb stiffener design
- rigid flex reliability testing

优先承接页：

- HILPCB: `products/rigid-flex-pcb`、`products/flex-pcb`
- APTPCB: `pcb/rigid-flex-pcb`

### E. 材料 / 表面处理 / 热管理集群

Pillar 例子：

- pcb materials
- pcb surface finish
- thermal management pcb

Query 例子：

- enig vs immersion silver
- osp shelf life
- high tg fr4 vs standard fr4
- metal core pcb thermal path design

优先承接页：

- HILPCB: 材料或表面处理相关产品 / 服务页
- APTPCB: `materials/`、`pcb/pcb-surface-finishes`

### F. 组装 / 缺陷 / 测试 / 质量集群

Pillar 例子：

- pcb assembly
- pcb inspection and testing

Query 例子：

- tombstoning causes
- solder void inspection
- flying probe vs ict
- spi vs aoi
- bga xray criteria

优先承接页：

- HILPCB: `products/turnkey-assembly`、`products/smt-assembly`
- APTPCB: `pcba/`、测试与检验类页面

### G. 可靠性 / 标准 / 合规集群

Pillar 例子：

- pcb reliability testing
- ipc standards for pcb

Query 例子：

- thermal cycling test for pcb
- caf failure causes
- ipc class 2 vs class 3
- ul pcb requirements

优先承接页：

- APTPCB 更适合承接到 `resources/`、`capabilities/`、`industries/`
- HILPCB 更适合承接到相关产品 / 服务页和辅助博客页

### H. 行业应用集群

Pillar 例子：

- automotive pcb
- medical pcb
- server backplane pcb

Query 例子：

- pcb requirements for adas
- medical pcb material selection
- data center pcb stackup design

优先承接页：

- APTPCB: `industries/`
- HILPCB: 相关产品页 + 行业博客页

## 五、Pillar 与 Query 的映射关系

每个 cluster 建议采用：

- `1-3` 篇 pillar
- 每个 pillar 下 `6-20` 篇 query

不要出现：

- 只有 query，没有 hub
- 一个 hub 下挂过多弱相关 query
- 多个 pillar 争夺同一核心词

### 例子

`High-Speed / Impedance`

- Pillar:
  - `high speed pcb`
  - `controlled impedance pcb`

- Query:
  - `what is controlled impedance pcb`
  - `impedance control tolerance`
  - `stripline vs microstrip`
  - `differential pair spacing guide`
  - `rogers vs fr4 for high frequency pcb`
  - `backdrilling in high speed pcb`

## 六、避免关键词内耗的规则

### 一词一主页

每个主词只能有一个主目标页：

- 一个主关键词只能有一个 pillar 或一个 query 作为 canonical 主攻页

### 相近词要有角色区分

例如：

- `high speed pcb` 是 pillar
- `controlled impedance pcb` 可以是 pillar 或 query，但不能与前者重复承担同一范围
- `impedance control tolerance` 应是 query，不应再写成宽泛 pillar

### 标题与结构要体现页面角色

- Pillar 讲范围和框架
- Query 讲答案、规则、步骤、边界
- Comparison 讲 trade-off
- Capability 讲可交付与验证

## 七、关键词集群必须绑定站点路径

不要只做关键词表，还要给每个 cluster 配站点承接主路径。

### HILPCB

优先路径：

- `products/`
- `services/`
- `tools/`
- `blog/`
- `quote/`

### APTPCB

优先路径：

- `pcb/`
- `pcba/`
- `capabilities/`
- `materials/`
- `industries/`
- `resources/`
- `tools/`
- `quote/`

## 八、关键词数据字段建议

每个关键词至少维护以下字段：

| Field | Purpose |
| --- | --- |
| keyword | 主关键词 |
| normalized_keyword | 去重后的标准词形 |
| cluster | 所属主题集群 |
| pillar_parent | 所属 hub |
| intent | 搜索意图 |
| page_type | `query` / `pillar` |
| modules | `comparison` / `application` / `capability` |
| funnel_stage | awareness / consideration / decision / implementation |
| primary_site_path | 优先承接栏目 |
| secondary_site_path | 次承接栏目 |
| priority | 内容优先级 |
| status | backlog / writing / published / refresh |

## 九、排期建议

如果要做一批新内容，优先顺序建议为：

1. 先建 cluster map
2. 每个 cluster 先定 pillar
3. 再补最强商业 Query
4. 再补高频 informational Query
5. 最后补应用、比较、长尾 FAQ 型 Query

这样能避免先写了很多散乱文章，后面又回头补 hub。
