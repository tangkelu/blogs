# What To Keep From `/code/blogs/blogs`

本文件记录从 `/code/blogs/blogs` 目录中真正值得吸收进 `prompts_template` 的规则。

目标不是把旧提示词整套搬过来，而是提炼那些确实能帮助我们写出“PCB 制造与组装行业顶尖博客”的方法。

## 一、这次扫描覆盖了什么

重点审读了这些文件：

- `/code/blogs/blogs/seo_rewrite_master_prompt.md`
- `/code/blogs/blogs/llm_rewrite_existing_blog_prompt.md`
- `/code/blogs/blogs/llm_generate_full_blog_prompt.md`
- `/code/blogs/blogs/technical_blog_evidence_pack_template.md`
- `/code/blogs/blogs/1119-1-ccc/rewrite.md`
- `/code/blogs/blogs/1118-2-cccc-rewrite/rewrite.md`

并抽样检查了几类成品博客：

- 制造控制
- 高速布线
- 成本优化
- MES / traceability
- 设计 checklist / stackup checklist

## 二、确认应该保留的高价值规则

### 1. Title Type Diversification

这是旧提示词里非常值得保留的一条。

同一批博客不能全部用同一种标题骨架，尤其不能反复复用：

- `[主词]制造边界`
- `[主词]量产边界`
- `什么是[主词]，量产时最先看什么`

应按意图分流成几类标题：

- 定义 / 速览型
- 设计 / 决策型
- 制造 / 工艺控制型
- 风险 / 失效分析型
- 选型 / 对比型

这条规则已经被吸收到：

- `shared/template-selection-and-pruning.md`
- `shared/query.md`
- `shared/pillar.md`

但后续还应继续执行得更硬。

### 2. Direct Answer Block

旧提示词强调：

- frontmatter 后要尽快给出单独 answer block
- answer block 要能独立回答问题

这条规则对 SEO、AI 摘取和工程读者扫描都有效。

应该保留的不是旧文里的固定 H2 文案，而是：

- 每篇都要有明确的“直接回答”区
- 位置必须在很前面
- 不能拖到背景铺垫后面

### 3. Early Summary Table

这一条也应保留。

高质量技术博客在前部就应给出一张结构化表，帮助：

- 搜索理解
- AI 抽取
- 工程师快速扫描

值得保留的不是某个固定列名，而是表格职能：

- 参数 / 结构 / 风险 / 验证
- 公开事实 / 项目级检查项 / 工程提醒

### 4. Second Early Structured Layer

`seo_rewrite_master_prompt.md` 中最有价值的经验之一，是对参数密集型主题要求：

- 除了第一张早期表
- 还要再给第二层早期结构化信息块

这一点对以下主题尤其有效：

- SI
- 材料
- 阻抗
- 背钻
- 可靠性
- DFM
- EMC / 安规
- 连接器 / press-fit / launch

保留方式：

- 不是强制每篇都上 UI 卡片
- 而是要求参数密集型主题必须有“早期双层结构”
- 第二层可以是：
  - 4-card UI block
  - 多张补充 markdown table

### 5. Claim Extraction

这是旧体系里最应该进入标准流程的能力之一。

真正写作前，必须先抽取：

- 协议名
- 标准名
- 材料名
- 参数
- 阈值
- 测试方法
- compatibility claims

再分成：

- 公开可验证事实
- 项目级经验判断
- 不支持 / 不清楚

这一点已经被吸收到：

- `shared/data-organization-standard.md`
- `shared/evidence-pack-template.md`

### 6. Visible Citation Rule

旧提示词有一个非常正确的判断：

- 默认不要在文末堆 `公开资料参考`
- 更好的做法是把高价值一级来源嵌进正文关键论证段

这对技术博客尤其重要，因为：

- 正文引用更服务结论
- 不会把成稿做成“参考链接清单”
- 更接近真正高质量技术内容

保留方式：

- 单篇只放少量高价值锚点
- 优先标准组织、联盟、监管机构
- 商业供应商资料更多作为内部核验来源

### 7. Answer-First H2 Rule

这条也值得保留：

- 每个主要 H2 开头先给结论
- 再展开背景、原理、验证和影响

这比常见的“先铺背景再说重点”更适合搜索型技术博客。

### 8. Instruction-Leak Prevention

旧提示词明确要求：

- 不允许把提示词语言泄漏到正文
- UI 卡片、表格、FAQ、CTA 都必须是读者向内容

这条非常重要，应该保留为硬规则。

### 9. Footer Identity Block

旧提示词要求文末有：

- 作者
- reviewer
- 最后更新

这对工程博客的可信度和规范化是有帮助的。

值得保留，但应写成站点 convention，而不是所有站点都必须完全同字面。

### 10. Internal Linking As Cluster Support

旧提示词把内链定义为：

- cluster relevance 支撑
- 语义锚文本
- 不做 exact-match spam

这条应保留，而且与我们之前的“优先产品 / 服务 / 能力页”原则并不冲突。

## 三、确认不应该整套保留的内容

### 1. 过重的缺项即失败清单

旧提示词把大量结构写成“缺项即失败”。

问题是：

- 对个别主题有效
- 对整个体系会造成模板僵化

所以不应整套照搬。

应改为：

- 按主题类型定义最低要求
- 参数密集型主题执行更强结构
- 非参数密集型主题保持适度弹性

### 2. 所有参数密集型主题都默认双 quote 组件

这是站点组件 convention，不是行业博客通用原则。

可以保留在站点 overlay 或站点执行规范里，不应写成 shared 内容方法的核心。

### 3. 过强的 UI 卡片频率要求

旧提示词强调 cluster 里要经常出现 UI 卡片。

这有一定价值，但如果执行过度，会让博客显得批量模板化。

正确保留方式是：

- 参数密集型主题优先双层结构
- UI 卡片只是其中一种表达手段
- 表格更适合时就用表格

### 4. 某些成品博客里过长的 FAQ / Checklist 化写法

抽样看到一些旧成品存在问题：

- FAQ 过长
- checklist 堆叠过多
- 前部铺垫太多
- CTA 和营销块偏重

这些不应进入 shared 模板。

## 四、从成品博客里总结出的反向经验

抽样后的结论是：

- 只靠长 FAQ 和长 checklist，并不能自动写出顶级博客
- 只靠“看起来专业”的术语堆砌，也不能建立权威
- 真正有效的是：
  - 早期直接回答
  - 早期结构化信息
  - 明确 trade-off
  - 明确验证路径
  - 正文中有证据支撑的结论

## 五、已经并入 `prompts_template` 的收获

这次从 `/code/blogs/blogs` 目录提炼出的精华，已经或应当并入这些文件：

- `shared/technical-blog-standard.md`
- `shared/template-selection-and-pruning.md`
- `shared/query.md`
- `shared/pillar.md`
- `shared/evidence-pack-template.md`
- `shared/data-organization-standard.md`

## 六、以后继续保留的执行原则

以后如果再从旧目录吸收内容，筛选标准应当是：

1. 这条规则能否提升真实搜索意图匹配
2. 这条规则能否提升工程可信度
3. 这条规则能否提升 AI / 搜索抽取质量
4. 这条规则会不会让模板更僵、更像批量生成

只有前 3 条成立且第 4 条风险可控，才值得进入 `prompts_template`。
