# Shared Technical Blog Standard

这是跨站点统一的技术博客底线标准。

它只定义“什么样的文章算合格”，不负责决定：

- 该用 `query` 还是 `pillar`
- 关键词该归到哪个 cluster
- 数据从哪里来

这些分别由以下文件负责：

- `template-selection-and-pruning.md`
- `keyword-cluster-design-standard.md`
- `data-organization-standard.md`

## 一、技术博客的默认定位

PCB / PCBA 技术博客默认不是普通资讯文，也不是空泛 SEO 文。

默认定位应该是：

- 轻量工程指南页
- 工程问题解答页
- 设计 / 制造 / 验证 / 选型辅助页

## 二、每篇文章的最低要求

每篇都应该至少具备：

- 直接回答
- 至少一块早期结构化信息
- 至少一张早期规则 / 参数 / 对比表
- 对抽象工程主题至少 `1` 个高信息密度 failure pattern / EQ delay pattern
- FAQ
- CTA 或下一步承接
- 自然内链

如果主题确实不需要 glossary、supplier checklist、cheat sheet，就不要为了模板硬加。

### 对参数密集型主题的额外要求

以下主题默认属于参数密集型或工程控制型主题：

- DFM
- SI
- 材料
- 背钻
- 阻抗
- 板翘
- 可靠性
- 容差控制
- EMC / 安规
- 连接器 / press-fit / launch

这类文章除了第一张早期表，还应再给第二层早期结构化信息。

允许两种实现方式：

- 早期表 + 4-card UI block
- 早期表 + 额外一张或多张 markdown table

### 参数写法标准

标准写法不是只写参数，也不是只写边界话术，而是：

- 先找参数，再写进正文
- 同时写清这个参数属于什么方法、什么场景、什么边界
- 数值必须带适用条件，不能写成裸通用默认值
- 如果参数只能在特定测试方法、qualification 场景或项目条件下成立，就必须在正文里明确标注
- 如果没有足够证据支撑方法、场景和边界，宁可降级成验证动作或定性判断，也不要只留一个数字

换句话说，读者应该看到的是“这个参数在哪种方法和场景下成立”，而不是“这里只是有一个参数”。

### 图表 / 信息图使用原则

- 图表不是装饰，也不是视觉广告；它必须是正文逻辑的自然延伸
- 只有当图表能把流程变化、决策边界、结构关系、验证路径或失效模式讲得更清楚时才使用
- 图表是否需要，按以下优先级判定：
  - `must_add_figure`：正文正在解释工艺流程对比、测试 / 检验路径、结构分区或 stackup / finish zoning、失效模式与排查路径、设计决策矩阵或冻结点，且这一关系可以被一张图稳定翻译
  - `should_add_figure`：主题是 `cost`、`lead time`、`DFM`、`validation`、`routing`、`stackup`、`materials`、`reliability` 这类抽象工程流程，且图能把 2 条以上流程、阶段或控制点压缩成一个更好读的判断框架
  - `no_need`：图只会重复首图、重复表格，或只提升视觉丰富度而不能增加信息密度
- 优先用于这些主题：
  - 工艺流程对比
  - 测试 / 检验路径
  - 结构分区或 stackup / finish zoning
  - 失效模式与排查路径
  - 设计决策矩阵或冻结点
- 不要为了“看起来更丰富”而插图
- 长文默认控制正文技术图数量；通常 `1` 张高价值正文图优于 `3` 张泛化插图
- 命中 `must_add_figure` 时，正文技术图默认不可省略
- 命中 `should_add_figure` 时，优先补图而不是留白
- 如果页面已经有首图，正文图应承担解释任务，而不是重复首图的情绪或品牌功能
- 图表插入时必须同时具备：
  - 引导句：说明为什么这里值得看图
  - 高信息密度 alt：让搜索系统和 AI 能读出图表所表达的流程或比较关系
  - 专业图注：说明图的结论、适用边界、以及它不代表什么
- 图注要像工程文档说明，而不是营销标语
- 如果图表无法做到“离开视觉也能被 alt 和图注准确复述”，说明图表本身信息密度不够，优先不用

### HTML 卡片作为替代展示

当主题需要在前部快速呈现 trade-off、流程分层、适用场景、主要风险或推荐动作，但图片并不合适时，可以改用 `1` 组轻量 HTML 卡片。

适用边界：

- 图会重复首图，或只增加装饰感
- 主题更适合用结构化文字表达，而不是图片表达
- 需要并列展示 `适用场景 / 主要风险 / 推荐动作 / 验证路径`
- 主题属于 `cost`、`lead time`、`routing`、`DFM`、`validation`、`stackup`、`materials`、`reliability` 这类抽象工程流程

要求：

- 卡片必须服务于正文逻辑，不得像视觉广告
- 默认控制在 `2-4` 个信息单元
- 每个卡片只回答一个核心问题，信息密度优先于装饰性
- 文风要像工程说明，不要像营销页
- 如果 HTML 卡片已经承担了核心解释任务，就不要再补一张等价图片

### 典型工程场景 / EQ 模式增强

当文章主题本身偏抽象，但又涉及 `lead time`、`cost`、`DFM`、`validation`、`release`、`test`、`stackup`、`materials` 或 `failure / troubleshooting` 时，可以补 `1` 段典型工程场景来增加信息密度。

它的作用不是讲故事，而是把前面已经成立的抽象规则，翻译成工程师熟悉的失败模式、卡点或放行延迟场景。

适用边界：

- 文章已经有规则、表格、结论，但还缺少“为什么这件事真的会卡住项目”的具体感
- 读者很可能会关心 `哪一个输入没定义会触发 EQ`、`哪一种结构会推高 review burden`、`哪一类遗漏会拖慢 release`
- 主题不适合编造客户案例，但适合写成典型工程场景

要求：

- 默认 `1` 段即可，不要把文章写成案例合集
- 优先放在相关 H2 内部，紧跟表格或结论段，而不是强制单独开一个 `Case Study` 章节
- 只能写成 `typical scenario`、`common failure pattern`、`common EQ trigger` 这类通用工程场景
- 必须写清：
  - 缺了什么输入或约束
  - 触发了哪个工程动作、暂停点或 review burden
  - 为什么它会影响 lead time、cost、risk 或 release
- 不得编造客户名、项目名、节省金额、量产结果、良率数字或工厂奇迹
- 如果写了具体数值、标准窗口或工厂能力，仍然必须满足证据边界，不能靠“案例口吻”绕过

### Physical Failure Pattern 使用要求

### Failure Mechanism Family 路由表

failure pattern 不是一个抽象占位符。不同主题族默认应该落到不同的真实失效机制族，而不是统一写成“如果处理不好会有风险”。

在进入正文前，默认先判断当前主题最接近哪一类 `failure mechanism family`：

| Topic family | Default mechanism family | Draft must explain | Default retrieval terms |
| --- | --- | --- | --- |
| `test / ICT / fixture / probe / DFT / depanel support / access tooling` | `mechanical load / strain` | 工装或探针把力施加在哪里，局部板弯或应变如何产生，为什么会变成潜伏失效或 release hold | `probe load`, `board flex`, `mechanical strain`, `support pin`, `strain relief`, `micro-crack`, `latent damage`, `open solder joint`, `MLCC`, `hidden joint` |
| `stackup / SI / PI / impedance / DDR / RF / EMC / ESD` | `electrical field / return path collapse` | 返回路径、阻抗连续性、耦合关系或保护路径在哪里失控，最终表现成什么电气验证失败 | `return path`, `plane split`, `stitching via`, `crosstalk`, `overshoot`, `eye closure`, `jitter`, `ESD path`, `stub`, `field coupling` |
| `thermal / MCPCB / power / LED / heavy copper / reflow heat` | `thermal mismatch / heat path` | 热路径、热堆积或材料膨胀不匹配在哪里出现，最终导致什么焊点、材料或寿命问题 | `thermal path`, `hot spot`, `CTE mismatch`, `heat spreading`, `voiding`, `solder fatigue`, `thermal cycling`, `delamination` |
| `assembly / stencil / reflow / via-in-pad / coplanarity / warpage / solderability` | `process window interaction` | 设计为什么看似可做但会把装配窗口压窄，最终导致什么制程波动、返工或量产不稳定 | `process window`, `warpage`, `coplanarity`, `tombstone`, `voiding`, `bridging`, `insufficient wetting`, `paste release`, `rework` |
| `coating / cleanliness / surface finish / residue / corrosion / contamination` | `chemical / surface condition` | 表面状态、残留物或界面化学在哪里失控，最终为什么变成漏电、腐蚀、附着或焊接问题 | `residue`, `ionic contamination`, `electrochemical migration`, `adhesion`, `wetting`, `oxidation`, `corrosion`, `surface condition` |
| `quote package / Gerber / ODB++ / IPC-2581 / BOM / stackup note / fabrication drawing / release docs` | `data-package incompleteness / governance failure` | 缺了什么定义或资料包字段，谁会停下来，为什么会引发错误假设、EQ、返工或 release delay | `missing input`, `package completeness`, `EQ hold`, `ambiguity`, `release package`, `netlist`, `stackup note`, `fabrication drawing`, `coordinate data` |

如果主题同时命中多类，只要求主文至少落稳 `1` 条主机制族；其他机制可以作为次要风险补充，但不能反过来把主机制写空。

以下主题默认不能只停留在规则、trade-off 或 review posture，应在正文中补 `1` 条主 failure chain 或同等密度的典型工程场景：

- `SI`
- `DFM`
- `assembly`
- `test / ICT / fixture / probe / DFT`
- `validation`
- `stackup`
- `materials`
- `reliability`
- `thermal`
- `high voltage / isolation`
- `connector / launch / press-fit`

这条 failure chain 不是装饰性案例，而是正文的证明链。它应回答：

- 板上到底同时存在什么结构、材料、封装、热负载或数据包缺口
- 真正失控的物理机制、装配机制或 EQ 触发动作是什么
- 最终会怎样坏掉、暂停、返工、误测或拖慢 release
- 为什么这说明 release package、DFM gate、stackup intent、装配说明或 test intent 必须在前面冻结

failure chain 的位置可按文章结构决定：可嵌入相关 H2、side note、caution block、review checklist 或 handoff section。不要把所有文章都写成同一位置、同一长度、同一句式；全文默认只保留 `1` 条主 failure chain，其他风险用短提醒即可。

如果主题属于 `quote package / Gerber / ODB++ / IPC-2581 / BOM / stackup note / fabrication drawing / release docs / FAI / NPI launch` 这条 `data-package incompleteness / governance failure` 族，failure pattern 不能只写成 `资料不全 -> 需要 EQ`。

优先补足一条“机器放大错误”的真实工厂链路，可贴近以下要素，但不要逐篇复制同一句式：

- `mixed BOM / unapproved substitute / unclear AVL status`
- `polarity / Pin 1 / package orientation / coordinate rotation mismatch`
- `line program released and feeders loaded`
- `FAI halt-and-verify missing or reduced to a weak signoff`
- `machine repeats the same wrong assumption across the lot`
- `downstream electrical test / power-on / debug catches the issue too late`
- `mass manual rework / scrap / release delay follows`

也就是说，这类主题的 failure pattern 默认要回答：

- 资料包里到底缺了哪个字段、批准状态或坐标定义
- 谁会按这个错误假设继续放料、编程、贴装或放行
- 为什么错误不会只停在一块板，而会被自动化设备成批复制
- 为什么这说明 FAI 的本质是 `halt, verify, and lock the baseline before scale`

默认逻辑应覆盖以下链路，但可调整顺序和表达：

- `setup`
- `missing definition or uncontrolled geometry`
- `physical mechanism or review trigger`
- `manufacturing / test / field consequence`
- `why the package must define this boundary before release`

如果主题属于 `test / ICT / fixture / probe / DFT`，failure pattern 不能只写成 `access 不够 -> review burden 增加`。优先补足一条实体物理链：

- `probe / clamp / support tooling load`
- `board flex / local strain / poor backside support`
- `MLCC crack / open solder joint / hidden-joint stress / latent damage`
- `initial screening may pass, but later open / short / intermittent or release hold appears`

也就是说，这类主题的 failure pattern 默认要回答：

- 夹具或探针到底把力施加在了哪里
- 哪些脆弱器件或隐藏焊点区域会承受局部应力
- 为什么这会变成潜伏失效，而不只是当场测不过
- 为什么 test-point 规划因此也是机械安全间距与支撑设计问题

禁止写成：

- 空泛提醒，例如 “if not handled properly, problems may occur”
- 只说“会影响性能”而不解释具体怎么失控
- 只说“工厂需要注意”而不解释缺了什么输入
- 用泛化营销口吻把 failure pattern 写成品牌背书

### CTA / Next Steps 使用要求

技术博客结尾的 `CTA / Next steps` 不能退化成“欢迎联系我们获取报价”。

CTA 必须按 `page_intent_mode` 选择，不得把所有技术博客默认写成 quote、SLA 或 24h DFM 反馈：

| `page_intent_mode` | CTA mode | 结尾必须覆盖 | SLA / quote 使用边界 |
| --- | --- | --- | --- |
| `knowledge` | `reference CTA` | 下一步阅读路径、概念边界、相关深文章或 support page | 不写 SLA，不把主 CTA 指向 quote |
| `review` | `review CTA` | review package、review owner、会返回的 DFM / stackup / assembly / test-access 输出 | 不默认写 SLA，除非站点 overlay 和页面意图都允许 |
| `handoff` | `handoff CTA` | handoff package、缺项字段、交接 owner、release / FAI / test 的下一步动作 | 不默认写报价，不把 handoff 缺项强行改成价格问题 |
| `commercial` | `quote CTA` | quote path、公开邮箱、报价资料包、成本 / 交期 / quick-turn 判断输入 | 只有该模式可使用 SLA、quote page 或 24h 反馈作为主收口 |

对 `assembly / BOM / drawing / quote package / release docs / FAI / NPI / test planning / stackup review / DFM review` 这类主题，如果 `page_intent_mode` 是 `review` 或 `handoff`，CTA 应写成工程协作式承接，并回答与该模式相关的问题：

- 读者现在最可能担心什么工程翻车点
- 应该提交哪一套资料包
- 哪个工程团队会接手 review
- 会返回哪些审查输出或冻结建议
- 是否需要联系、review、handoff 或 quote；只有 `commercial` 模式才写 SLA

如果主题属于 `FAI / BOM / release package / assembly launch / NPI`，CTA 默认优先覆盖以下输入：

- `AVL`
- `approved substitute status`
- `assembly drawing`
- `Gerber`
- `placement / coordinate data`
- `polarity / Pin 1 / rotation concerns`
- `expected FAI / inspection / test ownership`

CTA 逻辑链按模式选择，不要求每篇固定同一顺序：

- `knowledge`：`knowledge gap -> next reading -> decision point`
- `review`：`reader pain or launch risk -> review package -> review owner -> review output`
- `handoff`：`handoff gap -> missing input -> owner -> release / FAI / test action`
- `commercial`：`commercial need -> quote package -> quote path or email -> allowed SLA`

禁止写成：

- 只有品牌口号，没有工程输入
- 只有产品页链接，没有 review scope
- 只有“联系我们”而没有资料包定义
- 只有抽象承诺，而没有读者能立即执行的下一步

### 主题特异性要求

技术博客不能只写“放到任何相邻主题都成立”的抽象句子。

如果一段话把标题中的具体主题词替换成相邻技术词后仍然几乎完全成立，例如把 `PCIe Gen6` 换成 `PCIe Gen5`、`112G Ethernet`、`USB4` 甚至更泛的 `high-speed design` 后依旧通顺，那么这段话默认过泛，必须继续下钻。

应优先补足以下层级中的至少一层：

- 该主题独有或高度相关的物理机制
- 该主题特有的失效模式或 review burden
- 该主题比相邻主题更敏感的结构、材料、测试或 release 条件
- 该主题下真正会触发工程暂停、EQ、返工或验证分层的卡点

例如：

- `high-speed` 不是终点；应继续区分 `PAM4`、`connector launch`、`backdrill`, `return path`, `material class` 等真正造成差异的因素
- `cost` 不是终点；应继续区分 `stackup route`、`HDI family`、`finish zoning`, `tooling`, `validation burden`
- `lead time` 不是终点；应继续区分 `quote clock`, `factory routing clock`, `shipping/customs clock`

### 列表使用原则

- 项目符号和短列表只能用于快速给答案、列检查项、列冻结点、列输入资料
- 不能让整篇文章退化成“标题 + bullets + FAQ”的字典式结构
- 如果某个 H2 的核心段落只有 bullets，没有因果解释、失效链路、trade-off 或工程动作，这一节通常还没写够
- 对 `SI`、`DFM`、`validation`、`stackup`、`materials`、`reliability`、`connector / launch` 这类主题，至少有一半主体 H2 应包含连贯段落，用来解释为什么、怎么卡住、如何验证

### FAQ 写法原则

- FAQ 不是免责声明区，也不是内部风控话术区
- 不要把 FAQ 写成一串 `Does this article prove X? No.` 这样的防御性问答，除非该误解本身就是高频工程误读，且回答能继续提供判断边界
- FAQ 应优先解决：
  - 常见认知误区
  - 供应商沟通中的模糊点
  - 设计、制造、验证之间最容易被混淆的边界
  - 读者在做项目决策时真正会追加追问的问题
- 如果一个 FAQ 只是在重复“本文不证明什么”，但没有进一步解释“那应该看什么、怎么确认、谁来确认”，应重写或删除

### 内部思考过程与内部术语泄漏禁令

最终成稿只能呈现对读者有用的工程内容，不得暴露作者在背后的思考过程、审稿动作或提示词执行痕迹。

禁止出现：

- 分析过程、推理过程、思考步骤、心路、判断过程说明
- “我先分析”“我判断”“这里我选择”“基于上面的推理”“下面解释我的逻辑” 这类作者自述
- “根据提示词”“按模板要求”“按本工作流”“根据 evidence pack / llm_wiki / gate / overlay” 这类内部执行语句
- `llm_wiki`、`evidence pack`、`prompt`、`template`、`workflow`、`internal`、`repo`、`knowledge base`、`working prompt`、`reasoning`、`analysis`、`chain-of-thought` 等内部术语
- 内部状态词，例如 `verified`、`framing_only`、`blocked`、`must_refresh`、`supplier_scoped_dated_only`、`DATA_GAP`
- 任何把正文写成“作者如何得出结论”的元叙述

必须改写成：

- 直接面向读者的工程结论
- 可执行的检查项、边界、验证动作或风险解释
- 对外可理解的角色称谓，例如“工程评审团队”“制造工程团队”“材料与工艺审核团队”

## 三、写作优先级

优先级从高到低：

1. 回答真实工程问题
2. 给出可验证的规则、参数、边界和检查方法
3. 帮助读者做设计 / 制造 / 采购决策
4. 自然承接到产品 / 服务 / 工具 / 资源页
5. 再考虑 SEO 扩写

## 四、证据边界

### 允许作为公开事实写入

- 标准组织公开内容
- 官方 datasheet / 白皮书
- 官方材料参数
- 监管或联盟公开说明

### 只能写成项目级判断

- DFM 优先级
- 风险排序
- 试产 / 量产控制建议
- 什么时候选 A，什么时候选 B

### 不允许直接写

- 无来源数字
- 编造 capability
- 编造客户结果
- 把某工厂窗口值写成行业统一标准

## 五、结构原则

优秀的技术博客通常符合这些特征：

- 开头先给答案，不先铺背景
- 很快进入表格、规则、步骤或决策框架
- 主要 H2 开头先给结论，再展开解释
- 至少覆盖两个工程视角
  - 例如设计 + 制造
  - 或材料 + 验证
  - 或缺陷 + 排查
- 中段自然承接站点解决路径
- FAQ 补长尾问题，不重复正文

### 直接回答块

每篇都应在前部提供一个明确的 direct answer / quick answer 区域：

- 应当足够短，能独立回答问题
- 应当放在很靠前的位置
- H2 文案可以变化，但职能不能缺失

## 六、商业承接原则

- 先服务读者问题，再服务站点转化
- 优先承接到产品 / 服务 / 能力 / 工具页
- 博客互链是辅助，不是主承接
- 商业承接必须嵌入工程动作
  - 例如 DFM、stackup review、材料确认、测试要求确认

### CTA / Next Steps 写法

- 结尾 CTA 不能只是“按产品线罗列 4-5 个链接”的清单
- CTA 结构必须跟随前文定义的 `page_intent_mode`，不能所有文章默认使用同一种服务引导结构
- CTA 必须贴合正文主题，不得用一段通用销售话术套所有文章
- 推荐把 CTA 写成读者正在面对的具体问题
  - 例如阻抗、stackup、finish zoning、DFT、test access、热路径、材料选择、验证路径
- `review`、`handoff`、`commercial` 模式可以自然引导读者提交 Gerber、stackup、BOM、测试要求、应用约束或 enclosure 条件；`knowledge` 模式优先给下一步阅读路径
- 如果站点 overlay 已给出公开可用邮箱、quote 页面、DFM 响应承诺或工程团队称谓，只能在对应 `page_intent_mode` 允许时复用这些站点级信息
- 如果没有站点级公开信息，不要编造邮箱、响应时效、免费承诺、认证背书或工程服务范围
- CTA 里的链接仍然应该保留，但应作为“如果某一块仍未定义，可先看这些页面”的辅助动作，而不是整段 CTA 的主体
- CTA 必须听起来像当前页面意图的自然下一步，不像硬切换到销售页
- 对 HILPCB / APTPCB 这类带 quote intake 的站点，只有 `commercial` 模式才默认包含 quote path、邮箱或公开 SLA；`review` 和 `handoff` 模式只在需要时写 review / handoff 输入与输出；`knowledge` 模式不得强行询盘

## 七、内链原则

- 内链要均衡分布，不要堆在结尾
- 开头、中段、FAQ / 结尾都可以出现
- 优先强承接页，次优相关博客页
- 单篇文章的链接目的地不要过度集中到单一路径
- 优先使用语义化锚文本，不做 exact-match spam

## 八、语言原则

- 先写工程事实，再写营销修饰
- 句子尽量短
- 不使用空泛优势词堆砌
- 结论要带条件、边界或验证方法
- 不允许泄漏提示词 / 编辑说明 / 指令语言到正文

## 九、可信度锚点

高质量技术博客应尽量做到：

- 文末有作者 / reviewer / update 信息
- 正文关键结论可用少量一级来源锚点支撑
- 默认把锚点放在正文关键段落，而不是文末堆参考链接

## 十、模板原则

- 模板是骨架，不是内容本身
- 数据不足时，宁可减结构，不要补幻想信息
- 模板里只有高频有效原语应该被强制保留
- 低频结构一律改为模块，而不是所有文章通用
