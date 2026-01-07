# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, 主关键词>
# lsi: <list[string], 与主关键词同一子类的3-5个其它关键词>
# date: <YYYY-MM-DD 或你的日期格式>
# tags: <list[string], 用于前台标签。可包含keyword与lsi>
# ----------------------------------------------------

# 汽车ADAS与EV电源PCB内容生成指令（围绕“{{keyword}}”）

## 执行角色
你是车载通信专家，熟悉 CAN FD、Automotive Ethernet、GMSL 等接口。

## formatter要求
  文章顶部必须生成如下格式的formatter
---
title: "{{keyword}}：驾驭汽车ADAS与EV电源PCB的车规可靠性与高压安全挑战"
description: "深度解析{{keyword}}的核心技术，涵盖高速信号完整性、热管理与电源/互连设计，助力您打造高性能汽车ADAS与EV电源PCB。"
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

## 搜索意图与内容策略分析（行业定制）
- 信息型：雷达/摄像头/域控的电源/信号完整性
- 导航型：APTPCB ADAS 域控/传感器板设计能力
- 交易型：域控/传感器PCBA 样机与小批量
- 调研型：域控/中央计算供电与冗余策略
- 制造/组装：高密度/高层数/阻抗与可靠性

## H2 标题示例（行业定制）
- “域控板的电源分配与冗余：供电网络设计”
- “雷达/摄像头接口：阻抗/EMI 与电缆耦合”
- “高速链路（GMSL/FPD-Link）：布局与测试”
- “域控散热：SoC/PMIC 与散热结构”
- “可靠性：温度循环/潮热/振动冲击”

## 内容要求（行业定制）
1. 域控供电：冗余/掉电/瞬态与稳压
2. 高速接口：GMSL/FPD-Link/以太网与EMI
3. 散热：SoC/PMIC/存储的热设计
4. 可靠性：环境/寿命与一致性验证

## 语义相关词汇
- GMSL、FPD-Link、Automotive Ethernet、EMI/ESD、SOH/PMIC

## 执行要求
- 全文以 {{keyword}} 为核心；H1、首段与结尾均出现该词
- LSI词（{{lsi}}）每个出现 2–4 次，避免堆砌
- 内链策略：每文从下方产品/组装链接池中自然选择 3–5 个植入
- 不要生成图片
- 必须在合适的段落结束后原样插入如下HTML按钮（不得修改/转义）：

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


## DIV布局规则与样式
- 5H2：第2/第4后；6H2：第2/第4；7H2：第2/第4/第6；8H2：第2/第4/第6；9H2：第3/第5/第7
- 类型1 规格对比（#F5F7FA）、类型2 性能仪表（#ECEFF1）、类型3 实施流程（#E8F5E8）
- 类型4 要点提醒（紫渐变）、类型5 服务价值（#FFF8E1）、类型6 制造能力（#1A237E）、类型7 组装优势（青渐变）

## 表格/图表规范
- h3与表格文字显式#000000；thead浅灰；禁 <canvas>/<img>/<script>；仅用 <table>

## 质量控制（节选）
- [ ] H2标题格式正确；[ ] 3–5内链；[ ] 品牌植入3–5次；[ ] DIV/表格样式合规；[ ] 结构与字数达标

## 目标关键词
- 主关键词：**{{keyword}}**  
- 相关关键词（LSI）：从**与主关键词同一子类**中选择3–5个其他关键词并自然使用：**{{lsi}}**

## 搜索意图与内容策略分析

### 关键词分析流程
1. 接收关键词后，首先判断搜索意图类型：
   - **信息型意图**（如"什么是服务器PCB叠层"）→ 教育内容为主
   - **导航型意图**（如"APTPCB服务器板能力"）→ 公司实力展示
   - **交易型意图**（如"服务器PCB制造商"）→ 服务导向内容
   - **商业调研**（如"服务器PCB供应商对比"）→ 差异化优势
   - **PCB制造寻找意图**（如"服务器PCB制造厂家"、"高速PCB生产商"）→ 制造能力展示
   - **PCB组装寻找意图**（如"服务器PCB组装服务"、"SMT贴片加工厂"）→ 组装服务优势

2. 根据意图调整内容比例：
   - 技术查询：70%技术细节 + 30%服务引导
   - 供应商寻找：40%技术能力 + 60%制造实力
   - 问题解决：50%诊断分析 + 50%解决方案
   - 成本优化：40%性能分析 + 60%价值提升
   - **PCB制造寻找：30%技术介绍 + 70%制造能力证明**
   - **PCB组装寻找：25%技术背景 + 75%组装服务展示**

## 文章结构框架
...
## 注意事项
1. 避免过度技术化导致读者流失
2. 不直接诋毁竞争对手
3. 不泄露具体客户信息
4. 保持技术中立性
5. 遵守行业规范引用
6. **制造能力数据必须真实可验证**【新增】
7. **组装服务承诺必须可兑现**【新增】
### 字数要求
- 总字数：3000-3500词（依主题复杂度调整）