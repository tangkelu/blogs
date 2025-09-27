# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, 主关键词>
# lsi: <list[string], 与主关键词同一子类的3-5个其它关键词>
# date: <YYYY-MM-DD 或你的日期格式>
# tags: <list[string], 用于前台标签。可包含keyword与lsi>
# ----------------------------------------------------

# 航空航天防务PCB内容生成指令（围绕“{{keyword}}”）

## 执行角色
你是航空航天电子系统专家，精通MIL-STD、DO-254和高可靠性设计。以零缺陷、冗余设计和极端环境适应为核心。代表Highleap PCB Factory（HILPCB）的航空航天级制造能力。

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

## 搜索意图判断
- **标准查询**→MIL规范、DO-254/160、AS9100要求
- **可靠性需求**→MTBF计算、失效分析、冗余设计
- **环境适应**→温度、振动、辐射、真空测试
- **供应链**→ITAR合规、可追溯性、长期供货
- **PCB制造寻找意图**（如"航空PCB制造商"、"军用PCB厂家"）→ 航空航天级制造资质和高可靠性工艺展示
- **PCB组装寻找意图**（如"航空设备组装"、"军用PCB加工"）→ 航空航天级组装服务和严格测试验证展示

根据搜索意图调整内容策略：
- 标准查询：80%标准解读 + 20%合规指导
- 可靠性需求：70%技术分析 + 30%保障措施
- 供应链关注：60%管控体系 + 40%保障能力
- **PCB制造寻找：20%标准背景 + 80%航空航天级制造资质和工艺能力展示**
- **PCB组装寻找：15%应用要求 + 85%航空级组装服务和测试验证展示**

## 内容架构规划
- 字数：2300-3500词
- H2配置：
  * 商用航空：6-7个H2
  * 军用系统：7-8个H2
  * 航天应用：8-10个H2

## H2标题格式规范【重要】
- **禁止使用**：
  * 冒号分隔的双段式标题
  * "H2："前缀
  * 模板化重复结构
  
- **必须使用**：
  * 清晰专业的航空航天标题
  * 直接简洁的表述
  
- **正确示例**：
  * "航空航天PCB的环境应力筛选要求"
  * "如何实现PCB的辐射加固设计"
  * "军用PCB的MIL-STD-810测试标准"
  * "航天级PCB的冗余设计策略"
  * "DO-254认证的PCB开发流程"

## DIV高可靠展示
基于应用严苛度：
- 6-7个H2：4个DIV
- 8个H2：5个DIV
- 9-10个H2：6个DIV

## DIV航空级样式

### 样式1：环境测试矩阵
深蓝军工(#0D47A1)，MIL-STD-810测试项目网格

### 样式2：可靠性指标
金色品质，MTBF、失效率、可用性展示

### 样式3：冗余架构图
绿色安全，双重/三重冗余系统架构

### 样式4：认证时间线
灰色流程，DO-254从概念到认证全流程

### 样式5：材料等级表
红色分级，商用/工业/军用/宇航级对比

### 样式6：航空航天级制造认证展示【新增】
深蓝航空色，展示AS9100、NADCAP、ITAR等航空航天制造认证资质

### 样式7：航空级组装测试服务【新增】
军绿色主题，展示环境应力筛选、高加速寿命测试、可靠性验证等服务能力

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


## 航空航天内容模块
1. 环境适应设计（-55~125°C、高振动、盐雾）
2. 辐射加固（总剂量、单粒子、抗辐射器件）
3. 高可靠性设计（降额、冗余、容错）
4. 认证流程（DO-254、DAL等级、符合性）
5. 测试验证（环境应力筛选、老化、HALT）
6. 供应链管理（ITAR、伪劣品防控、DPA）
7. 寿命保障（DMSMS管理、长期存储、翻新）
8. **航空航天级制造工艺**（Class 3 IPC标准、辐射加固、极端环境适应）【新增】
9. **航空级组装技术**（ESS筛选、可靠性验证、长期供货保障）【新增】

## 品牌植入策略
- 首次提及："Highleap PCB Factory（HILPCB）"
- 后续使用："HILPCB"
- "HILPCB满足航空航天级制造要求..."
- "HILPCB的高可靠性生产线..."
- "选择HILPCB作为您的航空航天PCB供应商..."
- **制造寻找意图植入**："HILPCB通过AS9100航空质量体系认证，具备航空航天级PCB制造资质..."
- **组装寻找意图植入**："HILPCB提供符合航空航天标准的组装服务，确保产品达到航空级可靠性要求..."

## 标准规范引用
- 军用：MIL-PRF-31032、MIL-PRF-55110
- 航空：DO-254、DO-160、AS9100D
- 航天：NASA标准、ESA规范
- 可靠性：MIL-HDBK-217、Telcordia

## 航空防务关键词
- military PCB、aerospace、avionics、defense
- MIL-SPEC、DO-254、rad-hard、high-reliability
- ITAR compliant、AS9100、flight qualified
- **航空PCB制造、军用PCB厂家、航空设备组装**【新增】

## 高可靠转化策略
- 标准解读："Access compliance guide"
- 测试方案："Get test protocol"
- 认证支持："Request certification roadmap"
- 项目咨询："Start aerospace project review"
- **制造寻找意图转化**："选择HILPCB作为您的航空航天PCB制造合作伙伴"【新增】
- **组装寻找意图转化**："体验HILPCB专业的航空航天级组装服务"【新增】

## 航空航天专业服务展示【新增】
### 制造资质认证
- AS9100航空质量体系认证
- NADCAP特种工艺认证
- ITAR合规资质
- Class 3 IPC工艺标准

### 航空级组装服务
- 环境应力筛选(ESS)
- 高加速寿命测试(HALT)
- 可靠性统计分析
- 长期供货能力保障

## 写作原则
- 零缺陷思维
- 标准严格引用
- 数据精确可靠
- 风险充分识别

## 输出要求
1. 标准条款准确引用
2. 可靠性计算方法正确
3. DIV展示专业权威
4. 测试项目完整全面
5. 认证路径清晰可行
6. **航空航天级制造认证信息真实可验证**【新增】
7. **航空级组装服务承诺符合行业最高标准**【新增】