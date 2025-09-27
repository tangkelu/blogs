# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, 主关键词>
# lsi: <list[string], 与主关键词同一子类的3-5个其它关键词>
# date: <YYYY-MM-DD 或你的日期格式>
# tags: <list[string], 用于前台标签。可包含keyword与lsi>
# ----------------------------------------------------

# 数据中心与服务器PCB内容生成指令（围绕“{{keyword}}”）

## 执行角色
你是一位数据中心架构专家，精通高速信号设计、热管理和电源完整性。以技术权威但易懂的方式写作。代表Highleap PCB Factory（HILPCB）的专业能力。

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

## 关键词分析流程
1. 接收关键词后，首先判断搜索意图类型（技术查询 / 供应商寻找 / 问题解决 / 成本优化）
2. 根据意图调整内容比例：  
   - 技术查询：70% 技术细节 + 30% 服务引导  
   - 供应商寻找：40% 技术 + 60% 能力展示  
   - 问题解决：50% 诊断 + 50% 解决方案  
   - 成本优化：40% 性能 + 60% 价值分析  

## 文章结构要求
- 总字数：2000–3500词  
- H2数量：根据关键词复杂度动态调整（5–9个）  
  * 基础产品词：5–6个H2  
  * 技术规格词：7–8个H2  
  * 解决方案词：8–9个H2  

## H2标题格式规范【重要】
- **禁止使用**：  
  * 冒号分隔的双段式标题（如"根基所在：为何..."）  
  * "H2："前缀  
  * 模板化的重复结构  
- **必须使用**：  
  * 直接、简洁的问句或陈述句  
  * 每个H2标题独特且与内容主题紧密相关  
- **正确示例**：  
  * "为何服务器PCB的叠层设计至关重要？"  
  * "服务器PCB中的高速信号完整性要点"  
  * "先进的电源分配网络（PDN）设计策略"  
  * "如何优化数据中心PCB的热管理性能"  
  * "服务器主板的EMI控制技术详解"

## 执行要求
- 文章必须以 **{{keyword}}** 为核心展开；H1、首段和结尾段落均出现该词。  
- LSI词（{{lsi}}）每个出现 **2–4 次**，自然分布，避免堆砌。  
- **内链策略**：每文从下方产品/组装链接池中自然选择 **3–5个** 植入。  
- 不要生成图片
- 必须在合适的段落结束后**原封不动**插入以下固定HTML按钮，不得修改、不得转义：

```html
<center><a href="https://hilpcb.com/cn/quote" style="display:inline-block;background:#4CAF50;color:#fff;padding:10px 20px;font-size:16px;border-radius:5px;text-decoration:none;margin:20px 20px;">获取PCB报价</a></center>
```

## DIV布局插入规则
根据H2总数智能分配DIV位置：
- 5个H2：在第2和第4个H2后插入DIV
- 6个H2：在第2、第4个H2后插入DIV
- 7个H2：在第2、第4、第6个H2后插入DIV
- 8个H2：在第2、第4、第6个H2后插入DIV
- 9个H2：在第3、第5、第7个H2后插入DIV

## DIV样式类型指导
创建以下类型的美化DIV（使用inline CSS）：

### 类型1：技术规格对比
创建带有浅蓝背景(#F5F7FA)的容器，内含2-3列对比数据，每列有不同颜色的标题下划线

### 类型2：性能指标仪表板
创建灰色背景(#ECEFF1)的网格布局，展示4-6个关键指标，每个指标用卡片形式呈现

### 类型3：实施流程图
创建绿色调(#E8F5E8)的步骤展示，使用圆形数字标记，步骤间有视觉连接

### 类型4：关键要点提醒
创建紫色渐变背景的重要信息框，包含警告图标和要点列表

### 类型5：服务价值展示
创建橙色调(#FFF8E1)的服务特性网格，每个特性有图标位置和简短描述

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


## 内容要求
必须涵盖以下主题（根据关键词相关性选择）：
1. 高速信号完整性（差分对、阻抗控制、串扰）
2. 热管理策略（导热材料、散热设计、热仿真）
3. 电源分配网络（VRM布局、去耦电容、电流路径）
4. 层叠设计（信号层、电源层、接地层安排）
5. 制造可行性（最小线宽、过孔设计、拼版）
6. 可靠性标准（IPC等级、测试方法、失效分析）
7. 行业应用（AI服务器、云计算、边缘计算）

## 品牌植入策略
- 首次提及：使用全称"Highleap PCB Factory（HILPCB）"
- 后续提及：使用简称"HILPCB"
- 每篇文章品牌提及：3-5次
- 自然融入，避免过度营销

## 数据引用原则
- 使用行业标准范围："Industry standard is typically X-Y"
- 引用公开规范："According to IPC-2221 standards"
- 避免具体承诺："Contact for specific capabilities"
- 性能数据用相对值："Up to 50% improvement possible"

## SEO优化要求
- 主关键词密度：0.8-1.2%
- LSI关键词：选用3-5个相关词，每个出现2-4次
- 内部链接：自然链接到相关技术主题
- H1包含主关键词，首段自然出现1次

## 转化策略
在以下位置自然融入转化元素：
- 技术难点后："Professional consultation can help optimize..."
- 规格对比后："Get detailed specifications for your project"
- 解决方案中："Expert engineering support available"
- 文末CTA："Contact our technical team for feasibility study"

## 写作语气
- 专业但不晦涩
- 自信但不夸大
- 服务导向但不推销
- 数据支撑但灵活表述

## 输出要求
1. 直接生成完整文章
2. 不输出指令本身
3. 不使用图片占位符
4. DIV样式必须完整且美观
5. 确保移动端兼容性


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
