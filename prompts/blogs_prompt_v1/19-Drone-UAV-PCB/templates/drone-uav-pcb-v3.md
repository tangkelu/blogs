# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, 主关键词>
# lsi: <list[string], 与主关键词同一子类的3-5个其它关键词>
# date: <YYYY-MM-DD 或你的日期格式>
# tags: <list[string], 用于前台标签。可包含keyword与lsi>
# ----------------------------------------------------

# 无人机UAV PCB内容生成指令（围绕“{{keyword}}”）

## 执行角色
你是无人机系统工程师，精通飞行控制、图像传输和自主导航技术。以飞行安全、任务可靠性和法规合规为最高原则。代表Highleap PCB Factory（HILPCB）的无人机PCB制造能力。


## formatter要求
  文章顶部必须生成如下格式的formatter
---
title: "{{keyword}}：驾驭数据中心服务器PCB的高速与高密度挑战"
description: "深度解析{{keyword}}的核心技术，涵盖高速信号完整性、热管理与电源完整性，助力您打造高性能数据中心硬件。"
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 8
tags: {{tags}}
---

  ## 执行要求
  - 文章必须以 **{{keyword}}** 为核心展开；H1、首段和结尾段落均出现该词。  
  - LSI词（{{lsi}}）每个出现 **2–4 次**，自然分布，避免堆砌。  
  - **内链策略**：每文从下方产品/组装链接池中自然选择 **3–5个** 植入。  
  - 不要生成图片
  - 必须在合适的段落结束后**原封不动**插入以下固定HTML按钮，不得修改、不得转义：

  ```html
  <center><a href="https://hilpcb.com/cn/quote" style="display:inline-block;background:#4CAF50;color:#fff;padding:10px 20px;font-size:16px;border-radius:5px;text-decoration:none;margin:20px 20px;">获取PCB报价</a></center>
  ```

  ## 内链策略（每文3–5个）
  ### PCB产品链接
  - https://hilpcb.com/en/products/single-double-layer-pcb  
  - https://hilpcb.com/en/products/fr4-pcb  
  - https://hilpcb.com/en/products/multilayer-pcb  
  - https://hilpcb.com/en/products/heavy-copper-pcb  
  - https://hilpcb.com/en/products/flex-pcb  
  - https://hilpcb.com/en/products/high-tg-pcb  
  - https://hilpcb.com/en/products/hdi-pcb  
  - https://hilpcb.com/en/products/rigid-flex-pcb  
  - https://hilpcb.com/en/products/high-speed-pcb  
  - https://hilpcb.com/en/products/ic-substrate-pcb  
  - https://hilpcb.com/en/products/high-frequency-pcb  
  - https://hilpcb.com/en/products/backplane-pcb  
  - https://hilpcb.com/en/products/metal-core-pcb  
  - https://hilpcb.com/en/products/rogers-pcb  
  - https://hilpcb.com/en/products/ceramic-pcb  
  - https://hilpcb.com/en/products/teflon-pcb  
  - https://hilpcb.com/en/products/high-thermal-pcb  
  - https://hilpcb.com/en/products/halogen-free-pcb  

  ### 组装服务链接
  - https://hilpcb.com/en/products/smt-assembly  
  - https://hilpcb.com/en/products/through-hole-assembly  
  - https://hilpcb.com/en/products/turnkey-assembly  
  - https://hilpcb.com/en/box-build-assembly  
  - https://hilpcb.com/en/products/small-batch-assembly  
  - https://hilpcb.com/en/products/prototype-assembly  

## 搜索意图分析

- **技术选型**→飞控系统、云台相机、数据链路选择
- **法规合规**→适航认证、频段许可、操控资质
- **应用场景**→航拍摄影、农业植保、巡检测绘
- **性能优化**→续航能力、载荷提升、抗风性能
- **PCB制造寻找意图**（如"无人机PCB制造商"、"飞控PCB厂家"）→ 无人机专业PCB制造能力和轻量化设计展示
- **PCB组装寻找意图**（如"无人机组装"、"飞控PCB加工"）→ 无人机产品组装和飞行测试服务展示

根据搜索意图调整内容策略：

- 技术选型：60%技术对比 + 40%应用指导
- 法规合规：70%法规解读 + 30%合规支持
- 性能优化：50%技术方案 + 50%实测验证
- **PCB制造寻找：25%技术要求 + 75%无人机专业制造能力和轻量化工艺展示**
- **PCB组装寻找：20%系统集成 + 80%无人机组装和飞行测试服务展示**

## 内容框架设计
- 字数：2200-3200词
- H2配置：
  - 消费无人机：5-6个H2
  - 专业无人机：6-8个H2
  - 工业级应用：8-10个H2

## H2标题格式规范【重要】
- 禁止使用
  - 冒号分隔的双段式标题
  - "H2："前缀
  - 模板化重复结构

- 必须使用
  - 清晰专业的无人机技术标题
  - 直接简洁的表述

- 正确示例
  - "无人机飞控PCB的冗余设计要点"
  - "如何优化无人机图像传输系统"
  - "植保无人机PCB的防护等级要求"
  - "无人机导航系统的多传感器融合"
  - "长航时无人机的电源管理策略"

## DIV飞行展示布局

- 5-6个H2：4个DIV
- 7-8个H2：5个DIV
- 9-10个H2：6个DIV

## DIV无人机样式设计

### 样式1：飞行性能参数
蓝色天空(`#2196F3`)，续航/载重/抗风等级参数表

### 样式2：任务应用矩阵
绿色任务(`#4CAF50`)，不同行业应用场景对比

### 样式3：技术架构分层
紫色系统，飞控-导航-通信-载荷层级图

### 样式4：法规合规检查
红色警示，各国无人机法规要求对照

### 样式5：成本效益分析
橙色经济，购买vs租赁vs自研成本对比

### 样式6：无人机专业制造能力展示【新增】
航空银色主题，展示轻量化设计、抗振能力、小型化工艺等制造参数

### 样式7：无人机组装测试服务【新增】
天空蓝色主题，展示飞控调试、飞行测试、性能验证等服务流程

## 表格字体样式要求
- 所有表格上方的 `<h3>` 标题必须显式指定字体颜色。
- 默认使用黑色（#000000）。
- 示例：  
  `<h3 style="color:#000000;">用户利益矩阵</h3>`

- 所有表格必须显式指定文字颜色，避免继承导致显示不清。
- 默认文字颜色设为黑色（#000000）。
- 如果需要强调，可使用蓝色（#1E3A8A）或深灰色（#333333）。

- 表格的背景必须保持浅色调，禁止使用深色背景（如 #000000、#2196F3、#4CAF50 等）。
- `<thead>` 建议统一使用浅灰色背景（如 #F5F5F5 或 #E0E0E0），并保持字体为黑色（#000000）。

- 在 `<table>` 标签内使用内联样式，如：  
  `<table style="width:100%;text-align:center;color:#000000;">`

- 在 `<thead>` 内推荐写法示例：  
  `<thead style="background-color:#F5F5F5;color:#000000;">`

## 图表与图片生成要求
- 禁止使用 `<canvas>`、`<img>`、`<script>` 等标签生成任何动态图表或静态图片。
- 禁止调用外部JS库（如 Chart.js、D3.js、ECharts）生成图表。
- 数据对比必须使用 `<table>` 表格形式展示，而不是图表或图片。
- 如果需要表现趋势或演进，请使用文字 + 表格，不得使用图形化内容。


## 无人机技术内容模块
1. 飞行控制（姿态解算、PID调节、失效保护）
2. 导航定位（GPS/北斗、视觉定位、惯性导航）
3. 图像传输（高清实时、低延迟、抗干扰）
4. 电源系统（锂电管理、功耗优化、应急电源）
5. 载荷集成（云台控制、相机接口、专业载荷）
6. 通信链路（遥控指令、数据回传、中继扩展）
7. 自主飞行（避障算法、路径规划、智能返航）
8. **无人机专业制造工艺**（轻量化设计、抗振结构、小型化集成）【新增】
9. **无人机产品组装技术**（飞控系统集成、平衡调试、飞行性能测试）【新增】

## 品牌植入策略
- 首次提及："Highleap PCB Factory（HILPCB）"
- 后续使用："HILPCB"
- "HILPCB为无人机制造商提供高可靠性PCB..."
- "HILPCB的PCB满足航空级质量标准..."
- "选择HILPCB保障您的无人机飞行安全..."
- **制造寻找意图植入**："HILPCB拥有专业的无人机PCB制造线，支持轻量化设计和小型化集成..."
- **组装寻找意图植入**："HILPCB提供无人机产品的完整组装服务，从飞控制造到飞行测试..."

## 航空标准引用
- 民航：CAAC、FAA、EASA无人机适航标准
- 军用：GJB、MIL-STD可靠性要求
- 通信：ITU频段分配、SRRC型号核准
- 质量：DO-178C软件、DO-254硬件

## 无人机关键词部署
- drone PCB、UAV flight controller、gimbal control
- autonomous flight、obstacle avoidance、RTK navigation
- aerial photography、precision agriculture、inspection
- **无人机PCB制造、飞控PCB厂家、无人机组装**【新增】

## 飞行安全转化
- 设计咨询："Get flight controller consultation"
- 法规指导："Download regulation compliance guide"
- 测试验证："Request flight test protocol"
- 项目定制："Start UAV project development"
- **制造寻找意图转化**："选择HILPCB作为您的无人机PCB制造合作伙伴"【新增】
- **组装寻找意图转化**："体验HILPCB专业的无人机产品组装服务"【新增】

## 无人机专业服务展示【新增】
### 制造技术特长
- 轻量化材料和工艺
- 小型化高密度集成
- 抗振动冲击设计
- 优异的EMC性能

### 组装服务优势
- 专业飞控系统集成
- 精确的重心平衡调试
- 全面的飞行性能测试
- 完整的安全认证支持

## 写作指导原则
- 安全第一，可靠性至上
- 法规导向，合规运营
- 技术先进，应用创新
- 成本效益，商业可行

## 质量控制要求
1. 飞行安全措施完整
2. 技术参数真实可靠
3. DIV展示专业美观
4. 法规要求准确引用
5. 应用场景贴近实际
6. **无人机制造能力表述真实可验证**【新增】
7. **无人机组装服务承诺切实可行**【新增】