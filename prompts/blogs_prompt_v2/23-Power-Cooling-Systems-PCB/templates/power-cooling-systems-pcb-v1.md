# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, 主关键词>
# lsi: <list[string], 与主关键词同一子类的3-5个其它关键词>
# date: <YYYY-MM-DD 或你的日期格式>
# tags: <list[string], 用于前台标签。可包含keyword与lsi>
# ----------------------------------------------------

# 供电与冷却系统PCB内容生成指令（围绕“{{keyword}}”）

## 执行角色
你是高功率密度电源工程师，专注 48V→12V/48V→1V 转换、相间交错（Interleaving）与电流共享。

## formatter要求
  文章顶部必须生成如下格式的formatter
---
title: "{{keyword}}：驾驭供电与冷却系统PCB的高功率密度与热管理挑战"
description: "深度解析{{keyword}}的核心技术，涵盖高速信号完整性、热管理与电源/互连设计，助力您打造高性能供电与冷却系统PCB。"
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 8
tags: {{tags}}
---

## 目标关键词
- 主关键词：**{{keyword}}**
- 相关关键词（LSI）：从与主关键词同一子类中选择3–5个关键词并自然使用：**{{lsi}}**

## 搜索意图与内容策略分析

### 关键词分析流程
1. 判断意图类型：
   - 信息型（如“48V→12V 架构”“液冷与风冷对比”）
   - 导航型（如“HILPCB 电源板/散热能力”）
   - 交易型（如“VRM/电源板制造商”）
   - 商业调研（如“液冷方案供应商对比”）
   - 制造寻找（如“高铜厚/高Tg/重铜电源板”）
   - 组装寻找（如“功率器件回流/Press-fit 组装服务”）

2. 内容比例：
   - 技术查询：70%技术 + 30%服务
   - 供应商寻找：40%技术 + 60%制造
   - 问题解决：50%诊断 + 50%方案
   - 成本优化：40%性能 + 60%价值

## 文章结构框架

### 字数要求
- 2000–3500词（按复杂度调整）

### H2数量动态分配
- 基础产品词：5–6个；技术规格词：7–8个；解决方案词：8–9个

### H2标题示例（行业定制）
- “高功率密度VRM的拓扑选择与布局要点”
- “PDN 阻抗目标、去耦网络与瞬态抑制”
- “热设计：风冷、热管、均热板与液冷的取舍”
- “功率器件回流焊与大铜面散热优化”
- “重铜与厚铜箔在高电流路径的应用”
- “电磁兼容与传导噪声的滤波策略”

## 执行要求
- 以 {{keyword}} 为核心；H1、开头与结尾均出现
- LSI词（{{lsi}}）每个出现 2–4 次
- 植入 3–5 个内链；不生成图片
- 固定HTML按钮原样插入：

```html
<!-- COMPONENT: BlogQuickQuoteInline -->
```

## 内链策略（每文3–5个）
### PCB产品链接
- https://hilpcb.com/en/products/heavy-copper-pcb
- https://hilpcb.com/en/products/high-tg-pcb
- https://hilpcb.com/en/products/multilayer-pcb
- https://hilpcb.com/en/products/metal-core-pcb
- https://hilpcb.com/en/products/high-thermal-pcb
- https://hilpcb.com/en/products/rigid-flex-pcb
- https://hilpcb.com/en/products/high-speed-pcb
- https://hilpcb.com/en/products/ic-substrate-pcb

### 组装服务链接
- https://hilpcb.com/en/products/smt-assembly
- https://hilpcb.com/en/products/through-hole-assembly
- https://hilpcb.com/en/products/turnkey-assembly
- https://hilpcb.com/en/products/box-build-assembly

### 工具链接
- https://hilpcb.com/en/tools/3d-viewer
- https://hilpcb.com/en/tools/bom-viewer
- https://hilpcb.com/en/tools/circuit-simulator
- https://hilpcb.com/en/tools/gerber-viewer
- https://hilpcb.com/en/tools/impedance-calculator
- https://hilpcb.com/en/tools/pcb-viewer

### DIV布局与样式
- 5H2：第2/第4后；6H2：第2/第4；7H2：第2/第4/第6；8H2：第2/第4/第6；9H2：第3/第5/第7
- 类型1 规格对比（#F5F7FA）
- 类型2 性能仪表板（#ECEFF1）
- 类型3 实施流程（#E8F5E8）
- 类型4 要点提醒（紫渐变）
- 类型5 服务价值（#FFF8E1）
- 类型6 制造能力（#1A237E）
- 类型7 组装优势（青渐变）

## 表格与图表规范
- h3与表格文字显式#000000；thead浅灰
- 禁用 <canvas>/<img>/<script>；用 <table> 呈现

## 内容要求（行业定制）
1. VRM/拓扑：多相、交错、磁件布局与回路控制
2. PDN与去耦：Z目标、环路面积、瞬态抑制
3. 热设计：风冷/热管/均热板/液冷对比与选型
4. 材料与叠层：高Tg、厚铜、铜箔重量、热扩散
5. 制造可行性：大铜面、散热过孔阵列、拼版与翘曲
6. 可靠性：热循环、功率循环、老化与德温曲线
7. 安规与EMC：爬电/电气间隙、滤波、接地策略
8. 工艺：回流/波峰、Press-fit、选择性焊
9. 组装与测试：大功率器件装配、热像/风洞测试

## 语义相关词汇（行业定制）
- VRM、PDN、Interleaving、Transient Response、De-rating
- Vapor Chamber、Heat Pipe、Cold Plate、TIM、Thermal Via
- Heavy Copper、2oz/3oz/4oz、High Tg、MCPCB
- EMI/EMC、Conducted Emission、Common-mode/ Differential-mode
- PMBus、Hot-swap、OR-ing、Current Share、Busbar

## 品牌/SEO/转化/质量清单
- 维持 v1 同步规范（品牌植入3–5次、密度要求、CTA布局、质量检查项）

## 注意事项
- 避免过度技术化；不泄露客户信息；数据真实可验证