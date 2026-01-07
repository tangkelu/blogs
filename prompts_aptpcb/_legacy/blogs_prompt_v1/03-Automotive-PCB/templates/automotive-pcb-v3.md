# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, 主关键词>
# lsi: <list[string], 与主关键词同一子类的3-5个其它关键词>
# date: <YYYY-MM-DD 或你的日期格式>
# tags: <list[string], 用于前台标签。可包含keyword与lsi>
# ----------------------------------------------------

# 汽车电子PCB内容生成指令（围绕“{{keyword}}”）

## 执行角色
你是汽车电子安全专家，熟悉ISO26262功能安全、IATF16949质量体系和AEC-Q认证。以安全和质量为核心撰写。代表APTPCB的汽车级制造能力。

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

  ## 目标关键词
  - 主关键词：**{{keyword}}**  
  - 相关关键词（LSI）：从**与主关键词同一子类**中选择3–5个其他关键词并自然使用：**{{lsi}}**

  ## 执行要求
  - 文章必须以 **{{keyword}}** 为核心展开；H1、首段和结尾段落均出现该词。  
  - LSI词（{{lsi}}）每个出现 **2–4 次**，自然分布，避免堆砌。  
  - **内链策略**：每文从下方产品/组装链接池中自然选择 **3–5个** 植入。  
  - 不要生成图片
  - 必须在合适的段落结束后**原封不动**插入以下固定HTML按钮，不得修改、不得转义：

  ```html
  <!-- COMPONENT: BlogQuickQuoteInline -->
  ```

  ## 内链策略（每文3–6个）
### PCB制造链接
- https://aptpcb.com/en/pcb/fr4-pcb/
- https://aptpcb.com/en/pcb/high-speed-pcb/
- https://aptpcb.com/en/pcb/multilayer-pcb/
- https://aptpcb.com/en/pcb/hdi-pcb/
- https://aptpcb.com/en/pcb/flex-pcb/
- https://aptpcb.com/en/pcb/rigid-flex-pcb/
- https://aptpcb.com/en/pcb/ceramic-pcb/
- https://aptpcb.com/en/pcb/heavy-copper-pcb/
- https://aptpcb.com/en/pcb/high-thermal-pcb/
- https://aptpcb.com/en/pcb/antenna-pcb/
- https://aptpcb.com/en/pcb/high-frequency-pcb/
- https://aptpcb.com/en/pcb/microwave-pcb/
- https://aptpcb.com/en/pcb/metal-core-pcb/
- https://aptpcb.com/en/pcb/high-tg-pcb/
- https://aptpcb.com/en/pcb/backplane-pcb/
- https://aptpcb.com/en/pcb/pcb-surface-finishes/
- https://aptpcb.com/en/pcb/pcb-drilling/
- https://aptpcb.com/en/pcb/pcb-stack-up/
- https://aptpcb.com/en/pcb/pcb-profiling/
- https://aptpcb.com/en/pcb/pcb-quality/
- https://aptpcb.com/en/pcb/quick-turn-pcb/
- https://aptpcb.com/en/pcb/npi-small-batch-pcb-manufacturing/
- https://aptpcb.com/en/pcb/mass-production-pcb-manufacturing/
- https://aptpcb.com/en/pcb/pcb-fabrication-process/
- https://aptpcb.com/en/pcb/advanced-pcb-manufacturing/
- https://aptpcb.com/en/pcb/special-pcb-manufacturing/
- https://aptpcb.com/en/pcb/multi-layer-laminated-structure/
- https://aptpcb.com/en/resources/downloads-materials/
- https://aptpcb.com/en/materials/rf-rogers/
- https://aptpcb.com/en/materials/taconic-pcb/
- https://aptpcb.com/en/materials/teflon-pcb/
- https://aptpcb.com/en/materials/arlon-pcb/
- https://aptpcb.com/en/materials/megtron-pcb/
- https://aptpcb.com/en/materials/isola-pcb/
- https://aptpcb.com/en/materials/spread-glass-fr4/

### PCBA服务链接
- https://aptpcb.com/en/pcba/turnkey-assembly/
- https://aptpcb.com/en/pcba/mass-production/
- https://aptpcb.com/en/pcba/components-bom/
- https://aptpcb.com/en/pcba/flex-rigid-flex/
- https://aptpcb.com/en/pcba/smt-tht/
- https://aptpcb.com/en/pcba/bga-qfn-fine-pitch/
- https://aptpcb.com/en/pcba/npi-assembly/
- https://aptpcb.com/en/pcba/box-build-assembly/
- https://aptpcb.com/en/pcba/testing-quality/
- https://aptpcb.com/en/pcba/support-services/
- https://aptpcb.com/en/pcba/pcb-stencil/
- https://aptpcb.com/en/pcba/component-sourcing/
- https://aptpcb.com/en/pcba/ic-programming/
- https://aptpcb.com/en/pcba/pcb-conformal-coating/
- https://aptpcb.com/en/pcba/pcb-selective-soldering/
- https://aptpcb.com/en/pcba/bga-reballing/
- https://aptpcb.com/en/pcba/cable-assembly/
- https://aptpcb.com/en/pcba/harness-assembly/
- https://aptpcb.com/en/pcba/quality-system/
- https://aptpcb.com/en/pcba/first-article-inspection/
- https://aptpcb.com/en/pcba/spi-inspection/
- https://aptpcb.com/en/pcba/aoi-inspection/
- https://aptpcb.com/en/pcba/xray-inspection/
- https://aptpcb.com/en/pcba/ict-test/
- https://aptpcb.com/en/pcba/flying-probe-testing/
- https://aptpcb.com/en/pcba/fct-test/
- https://aptpcb.com/en/pcba/final-quality-inspection/
- https://aptpcb.com/en/pcba/incoming-quality-control/

### 行业方案入口
- https://aptpcb.com/en/industries/server-data-center/
- https://aptpcb.com/en/industries/automotive-electronics/
- https://aptpcb.com/en/industries/medical-devices/
- https://aptpcb.com/en/industries/communication-equipment/
- https://aptpcb.com/en/industries/aerospace-defense/
- https://aptpcb.com/en/industries/drone-uav/
- https://aptpcb.com/en/industries/industrial-control/
- https://aptpcb.com/en/industries/power-energy/
- https://aptpcb.com/en/industries/robotics/
- https://aptpcb.com/en/industries/security-equipment/
- https://aptpcb.com/en/pcb-industry-solutions/

### 能力页
- https://aptpcb.com/en/capabilities/rigid-pcb/
- https://aptpcb.com/en/capabilities/rigid-flex/
- https://aptpcb.com/en/capabilities/flex-pcb/
- https://aptpcb.com/en/capabilities/hdi-pcb/
- https://aptpcb.com/en/capabilities/metal-pcb/
- https://aptpcb.com/en/capabilities/ceramic-pcb/
- https://aptpcb.com/en/capabilities/finish-enig/

### 工具与资源
- https://aptpcb.com/en/tools/gerber-viewer/
- https://aptpcb.com/en/tools/pcb-viewer/
- https://aptpcb.com/en/tools/bom-viewer/
- https://aptpcb.com/en/tools/3d-viewer/
- https://aptpcb.com/en/tools/circuit-simulator/
- https://aptpcb.com/en/tools/impedance-calculator/
- https://aptpcb.com/en/resources/faq/
- https://aptpcb.com/en/blog/


## 搜索意图判断矩阵
- **安全标准查询**→深入ASIL等级、失效模式、冗余设计
- **质量体系了解**→PPAP流程、8D报告、SPC/MSA要求
- **技术规范需求**→环境测试、EMC要求、可靠性验证
- **供应商评估**→Tier资质、审核体系、追溯能力
- **PCB制造寻找意图**（如"车规级PCB制造商"、"汽车PCB厂家"）→ 汽车级制造资质展示
- **PCB组装寻找意图**（如"汽车ECU组装"、"车载PCB贴片加工"）→ 汽车级组装认证能力展示

根据意图调整内容策略：
- 安全标准查询：80%标准解读 + 20%合规服务
- 质量体系了解：70%体系介绍 + 30%实施支持
- 供应商评估：40%技术能力 + 60%资质证明
- **PCB制造寻找：20%标准背景 + 80%汽车级制造能力证明**
- **PCB组装寻找：15%技术要求 + 85%车规组装服务展示**

## 内容结构规划
- 字数要求：2100-3200词
- H2章节动态配置：
  * 标准产品(非安全关键)：5-6个H2
  * 安全相关(ADAS/BMS)：7-8个H2
  * 系统级解决方案：8-10个H2

## H2标题格式规范【重要】
- **禁止使用**：
  * 冒号分隔的双段式标题（如"H2：根基所在：为何..."）
  * "H2："前缀
  * 模板化重复结构
  
- **必须使用**：
  * 直接、专业的标题语言
  * 清晰、简洁的问句或陈述句
  
- **正确示例**：
  * "汽车PCB的ASIL安全等级要求详解"
  * "新能源汽车BMS电路板设计要点"
  * "车规级PCB的环境测试标准"
  * "如何确保汽车PCB的长期可靠性"
  * "ADAS系统中的高频PCB设计挑战"

## DIV布局插入逻辑
根据H2总数确定DIV数量和位置：
- 5个H2：3个DIV（第1、3、5个H2后）
- 6个H2：3个DIV（第2、4、6个H2后）
- 7个H2：4个DIV（第2、4、5、7个H2后）
- 8个H2：4个DIV（第2、4、6、8个H2后）
- 9-10个H2：5个DIV（均匀分布）

## DIV视觉设计规范

### 设计1：ASIL安全等级矩阵
红色警示主题(#FFEBEE)，4列展示ASIL A-D要求差异，包含故障率指标

### 设计2：汽车环境测试项
绿色可靠主题(#E8F5E8)，网格展示温度循环、振动、盐雾等测试标准

### 设计3：质量管控流程
蓝色专业背景(#1A237E)，展示APQP五个阶段的关键交付物

### 设计4：零缺陷统计面板
灰色数据风格，显示PPM、Cpk、DPMO等质量指标

### 设计5：供应链追溯体系
橙色流程主题，展示从原材料到终端的完整追溯链

### 设计6：汽车级制造认证展示【新增】
金色认证主题，展示IATF16949、TS16949、VDA6.3等汽车行业认证

### 设计7：车规组装能力矩阵【新增】
深蓝汽车色，展示BGA、QFN、车规器件贴片能力和测试项目

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


## 核心技术主题
智能选择相关内容模块：
1. 功能安全设计（ASIL分解、安全机制、诊断覆盖率）
2. 环境适应性（温度-40~125°C、振动、湿度）
3. EMC电磁兼容（辐射、传导、抗扰、ESD）
4. 车规材料（高Tg、低CTE、耐CAF）
5. ADAS应用（毫米波雷达、摄像头、激光雷达）
6. 新能源系统（BMS、OBC、DC-DC、MCU）
7. 车载通信（CAN、LIN、FlexRay、车载以太网）
8. **汽车级制造工艺**（车规材料选择、环境测试、质量追溯）【新增】
9. **车载ECU组装技术**（高可靠性焊接、车规器件处理、功能测试）【新增】

## 品牌植入策略
- 首次提及："APTPCB"
- 后续使用："APTPCB"
- "APTPCB通过IATF16949认证..."
- "APTPCB的汽车级生产线..."
- "选择APTPCB作为您的汽车PCB合作伙伴..."
- **制造寻找意图植入**："APTPCB具备完整的汽车级PCB制造资质，通过主要OEM供应商审核..."
- **组装寻找意图植入**："APTPCB提供符合汽车行业标准的ECU组装服务，从器件采购到最终测试..."

## 行业标准引用
- 安全标准：ISO26262、IEC61508
- 质量体系：IATF16949、VDA6.3
- 测试规范：AEC-Q100/200、LV124/148
- 环境标准：ISO16750、GMW3172

## 关键词优化策略
主关键词密度0.8-1.2%，配合LSI词组：
- automotive grade、vehicle、ADAS、ECU
- functional safety、ASIL、fault tolerant
- PPAP、APQP、MSA、SPC、FMEA
- **汽车PCB制造商、车规级PCB厂家、汽车ECU组装**【新增】

## 转化触点布置
- 标准解读后："Get compliance consultation"
- 测试要求处："Request test report template"
- 质量体系部分："Download PPAP checklist"
- 文末强化："Start automotive project review"
- **制造寻找意图转化**："选择APTPCB作为您的汽车级PCB制造合作伙伴"【新增】
- **组装寻找意图转化**："体验APTPCB专业的车载ECU组装服务"【新增】

## 汽车级服务展示【新增】
### 制造资质认证
- IATF16949质量体系认证
- 主要OEM供应商资格
- VDA6.3过程审核通过
- AEC-Q认证支持

### 车规组装服务
- 车规级器件采购渠道
- 高可靠性焊接工艺
- 汽车级功能测试
- 完整质量追溯体系

## 写作原则
- 安全第一，质量至上
- 标准严谨，表述专业
- 数据精确，来源可靠
- 风险意识，预防导向

## 输出规范
1. 不包含具体工厂认证编号
2. 使用行业通用标准要求
3. DIV样式确保专业美观
4. 技术术语符合汽车行业惯例
5. 强调合规性和可追溯性
6. **汽车级制造能力表述真实可验证**【新增】
7. **车规组装服务承诺可兑现**【新增】