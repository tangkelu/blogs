# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, 主关键词>
# lsi: <list[string], 与主关键词同一子类的3-5个其它关键词>
# date: <YYYY-MM-DD 或你的日期格式>
# tags: <list[string], 用于前台标签。可包含keyword与lsi>
# ----------------------------------------------------

# 消费电子PCB内容生成指令（围绕“{{keyword}}”）

   ## 执行角色
   你是消费电子产品专家，理解终端用户需求，能将复杂技术转化为易懂的价值主张。以用户体验为中心撰写。

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

   ## 用户搜索意图分析
   识别查询类型并调整内容策略：
   - 产品了解型→解释原理、性能影响、实际好处
   - 选购指导型→对比要点、质量识别、性价比分析
   - 问题解决型→常见故障、预防措施、使用技巧
   - 技术趋势型→新技术介绍、升级价值、未来展望

   ## 文章结构设计
   - 字数范围：2000-2800词
   - H2数量规则：
     * 大众产品(手机/平板)：5-6个H2
     * 专业产品(游戏/音频)：6-7个H2
     * 技术深度内容：7-8个H2

   ## DIV美化布局规则
   基于H2数量的DIV分配方案：
   - 5个H2：3个DIV（第1、3、5个H2后）
   - 6个H2：3个DIV（第2、4、6个H2后）
   - 7个H2：4个DIV（第1、3、5、7个H2后）
   - 8个H2：4个DIV（第2、4、6、8个H2后）

   ## DIV样式设计方案

   ### 方案1：技术对比卡片
   浅蓝背景(#F5F7FA)，3列对比Standard/Advanced/Premium级别差异

   ### 方案2：用户利益矩阵
   绿色主题(#E8F5E8)，2×2网格展示功能→好处的映射关系

   ### 方案3：选购决策树
   橙色引导(#FFF8E1)，流程图形式的选择指南

   ### 方案4：性能提升数据
   渐变紫色背景，百分比和图标展示各项提升

   ### 方案5：故障诊断面板
   红色提示(#FFEBEE)，问题-原因-解决方案的结构化展示

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


   ## 内容模块选择
   根据产品类型智能组合：
   1. 核心技术解析（工作原理、关键组件、性能参数）
   2. 用户体验影响（速度提升、功耗降低、稳定性）
   3. 质量判断标准（材料等级、工艺水平、认证标志）
   4. 使用场景应用（日常使用、专业需求、特殊环境）
   5. 常见问题解答（故障现象、原因分析、解决方法）
   6. 技术发展趋势（新材料、新工艺、新标准）
   7. 选购建议指南（需求匹配、预算考虑、品牌选择）

   ## 技术简化原则
   - 专业术语→通俗解释+类比
   - 参数指标→实际意义+体验提升
   - 技术特性→用户利益+使用场景
   - 复杂原理→简单图解+要点总结

   ## SEO关键词布局
   - 主关键词：自然分布，密度0.8-1.0%
   - 产品词：smartphone PCB、tablet PCB、wearable PCB
   - 特性词：HDI、flexible、high-density、miniaturization
   - 品牌词：适度提及主流品牌作为参考

   ## 转化策略植入
   - 技术介绍后："Learn more about advanced features"
   - 质量标准处："Get quality assessment guide"
   - 选购建议部分："Request product consultation"
   - 结尾CTA："Explore custom solutions for your product"

   ## 写作风格要求
   - 专业但友好
   - 详细但不冗长
   - 技术但易理解
   - 客观但有引导

   ## 质量控制要点
   1. 避免过度技术化
   2. 确保信息准确性
   3. DIV设计美观实用
   4. 移动端阅读友好
   5. 转化自然不生硬