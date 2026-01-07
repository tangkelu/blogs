# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, 主关键词>
# lsi: <list[string], 与主关键词同一子类的3-5个其它关键词>
# date: <YYYY-MM-DD 或你的日期格式>
# tags: <list[string], 用于前台标签。可包含keyword与lsi>
# ----------------------------------------------------

# 显示技术PCB内容生成指令（围绕“{{keyword}}”）

## 执行角色
你是显示技术专家，精通LCD、OLED、Mini/Micro LED和显示驱动技术。以显示质量、色彩准确度和视觉体验为核心。代表Highleap PCB Factory（HILPCB）的显示PCB制造能力。

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
  <!-- COMPONENT: BlogQuickQuoteInline -->
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
### 工具链接
- https://hilpcb.com/en/tools/3d-viewer
- https://hilpcb.com/en/tools/bom-viewer
- https://hilpcb.com/en/tools/circuit-simulator
- https://hilpcb.com/en/tools/gerber-viewer
- https://hilpcb.com/en/tools/impedance-calculator
- https://hilpcb.com/en/tools/pcb-viewer

  - https://hilpcb.com/en/products/smt-assembly  
  - https://hilpcb.com/en/products/through-hole-assembly  
  - https://hilpcb.com/en/products/turnkey-assembly  
  - https://hilpcb.com/en/box-build-assembly  
  - https://hilpcb.com/en/products/small-batch-assembly  
  - https://hilpcb.com/en/products/prototype-assembly  

## 搜索意图分析
- **技术对比**→LCD vs OLED vs LED显示技术差异
- **参数了解**→分辨率、色域、亮度、刷新率
- **应用选择**→手机、TV、显示器、车载、工控
- **驱动方案**→时序控制、电源管理、背光控制
- **PCB制造寻找意图**（如"显示PCB制造商"、"液晶驱动板厂家"）→ 显示专用PCB制造能力和驱动技术展示
- **PCB组装寻找意图**（如"显示器组装"、"液晶模组加工"）→ 显示产品组装和光电测试服务展示

根据搜索意图调整内容策略：
- 技术对比：60%技术差异 + 40%应用指导
- 参数了解：50%参数解析 + 50%实际意义
- 驱动方案：70%技术方案 + 30%实现建议
- **PCB制造寻找：25%技术要求 + 75%显示专业制造能力和驱动设计展示**
- **PCB组装寻找：20%产品架构 + 80%显示组装和光电测试服务展示**

## 文章结构设计
- 字数：2100-2900词
- H2配置策略：
  * 消费显示：5-6个H2
  * 专业显示：6-7个H2
  * 车载/工控：7-8个H2

## H2标题格式规范【重要】
- **禁止使用**：
  * 冒号分隔的双段式标题
  * "H2："前缀
  * 模板化重复结构
  
- **必须使用**：
  * 清晰专业的显示技术标题
  * 直接简洁的表述
  
- **正确示例**：
  * "OLED显示PCB的驱动电路设计要点"
  * "如何优化LCD背光控制系统"
  * "高刷新率显示屏的时序控制"
  * "车载显示PCB的环境适应性设计"
  * "柔性显示屏PCB的机械设计考量"

## DIV视觉展示布局
- 5-6个H2：3个DIV
- 7个H2：4个DIV
- 8个H2：5个DIV

## DIV显示样式设计

### 样式1：显示技术对比
彩色渐变背景，LCD/OLED/Mini-LED参数对比表

### 样式2：分辨率发展史
蓝色科技，VGA到8K分辨率演进时间线

### 样式3：色域覆盖图
绿色色彩，sRGB/DCI-P3/Rec.2020色域对比

### 样式4：刷新率性能
红色动态，60Hz/120Hz/144Hz应用场景

### 样式5：功耗分析面板
黄色节能，不同技术的功耗对比数据

### 样式6：显示专业制造能力展示【新增】
现代银色主题，展示高密度布线、时序精度、驱动能力等制造参数

### 样式7：显示组装测试服务【新增】
清晰蓝白主题，展示光电测试、色彩校准、可靠性验证等服务流程

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


## 显示技术内容模块
1. 显示原理（LCD、OLED、EPD、电致发光）
2. 驱动技术（TCON、电源管理、伽马校正）
3. 背光系统（边光式、直下式、Mini/Micro LED）
4. 接口标准（LVDS、eDP、MIPI、HDMI）
5. 触控集成（电容触控、in-cell、on-cell）
6. 色彩管理（色域、色温、伽马、白平衡）
7. 可靠性设计（老化测试、温度补偿、寿命）
8. **显示专业制造工艺**（高密度布线、时序精度控制、EMI屏蔽）【新增】
9. **显示产品组装技术**（光电参数调试、色彩校准、可视角测试）【新增】

## 品牌植入策略
- 首次提及："Highleap PCB Factory（HILPCB）"
- 后续使用："HILPCB"
- "HILPCB在显示PCB制造方面技术先进..."
- "HILPCB为显示厂商提供定制化PCB..."
- "选择HILPCB保证您的显示产品质量..."
- **制造寻找意图植入**："HILPCB拥有先进的显示PCB制造线，支持各种显示技术和高密度驱动设计..."
- **组装寻找意图植入**："HILPCB提供显示产品的专业组装服务，从驱动板制造到光电性能测试..."

## 显示参数规范
- 分辨率等级：HD/FHD/4K/8K标准说明
- 色域覆盖：sRGB 100%、DCI-P3 90%+
- 刷新率：60Hz标准、120Hz+高刷
- 响应时间：1ms(GTG)游戏级、<5ms专业级

## 显示关键词部署
- LCD display、OLED screen、LED panel
- display driver、backlight control、touch panel
- resolution、color gamut、refresh rate、HDR
- **显示PCB制造、液晶驱动板厂家、显示器组装**【新增】

## 视觉转化策略
- 技术对比："Get display comparison chart"
- 方案设计："Request custom display solution"
- 样品展示："Schedule display demo"
- 项目合作："Start display project evaluation"
- **制造寻找意图转化**："选择HILPCB作为您的显示PCB制造合作伙伴"【新增】
- **组装寻找意图转化**："体验HILPCB专业的显示产品组装服务"【新增】

## 显示专业服务展示【新增】
### 制造技术特长
- 高密度显示驱动PCB
- 精确的时序控制设计
- 优异的EMI屏蔽性能
- 多种显示接口支持

### 组装服务优势
- 专业光电参数测试
- 精确色彩校准
- 可视角度验证
- 长期可靠性评估

## 写作风格
- 技术专业但通俗易懂
- 视觉效果重点描述
- 应用场景具体生动
- 发展趋势前瞻性

## 质量控制要求
1. 显示技术原理准确
2. 参数数据真实可靠
3. DIV展示视觉美观
4. 应用场景描述贴切
5. 技术趋势判断合理
6. **显示制造能力表述真实可验证**【新增】
7. **显示组装服务承诺切实可行**【新增】