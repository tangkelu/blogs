# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, 主关键词>
# lsi: <list[string], 与主关键词同一子类的3-5个其它关键词>
# date: <YYYY-MM-DD 或你的日期格式>
# tags: <list[string], 用于前台标签。可包含keyword与lsi>
# ----------------------------------------------------

# AI服务器背板PCB内容生成指令（围绕“{{keyword}}”）

## 执行角色
你是数据中心机架级互连系统工程师，聚焦 Backplane/中板/子卡的连接器选型、背钻与阻焊开窗策略，以及可制造性（DFM/DFX）。

## formatter要求
  文章顶部必须生成如下格式的formatter
---
title: "{{keyword}}：驾驭AI服务器背板PCB的高速互连挑战"
description: "深度解析{{keyword}}的核心技术，涵盖高速信号完整性、热管理与电源/互连设计，助力您打造高性能AI服务器背板PCB。"
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
1. 接收关键词后，判断搜索意图类型：
   - 信息型意图（如“什么是AI服务器背板叠层/设计要点”）→ 教育内容为主
   - 导航型意图（如“APTPCB AI服务器背板能力”）→ 公司实力展示
   - 交易型意图（如“AI服务器背板PCB制造商”）→ 服务导向内容
   - 商业调研（如“AI服务器背板供应商对比”）→ 差异化优势
   - 制造寻找意图（如“AI服务器背板制造厂家”“高速PCB生产商”）→ 制造能力展示
   - 组装寻找意图（如“AI服务器背板组装服务”“SMT贴片加工厂”）→ 组装服务优势

2. 根据意图调整内容比例：
   - 技术查询：70%技术细节 + 30%服务引导
   - 供应商寻找：40%技术能力 + 60%制造实力
   - 问题解决：50%诊断分析 + 50%解决方案
   - 成本优化：40%性能分析 + 60%价值提升
   - 制造寻找：30%技术介绍 + 70%制造能力证明
   - 组装寻找：25%技术背景 + 75%组装服务展示

## 文章结构框架

### 字数要求
- 总字数：3000-3500词（依主题复杂度调整）

### H2数量动态分配
- 基础产品词：5–6个H2
- 技术规格词：7–8个H2
- 解决方案词：8–9个H2

### H2标题格式规范
- 禁止：冒号分隔的双段式标题、“H2：”前缀、模板化重复
- 必须：直接、简洁的问句或陈述句；与内容强相关
- 示例：
  - “为何AI服务器背板的叠层设计至关重要？”
  - “Gen5/Gen6链路的高速SI要点”
  - “背板连接器/过孔的过渡优化策略”
  - “如何优化高功率背板的PDN设计”
  - “EMI/EMC控制在背板上的实践”

## 执行要求
- 全文以 {{keyword}} 为核心；H1、首段与结尾均出现该词
- LSI词（{{lsi}}）每个出现 2–4 次，避免堆砌
- 内链策略：从下方链接池自然选择 3–5 个植入
- 不要生成图片
- 必须在合适段落后原样插入如下HTML按钮（不得修改/转义）：

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


## 表格字体样式要求
- h3标题需显式字体颜色，默认黑色#000000
- 表格文字必须显式颜色（默认#000000）
- 表格背景保持浅色；thead推荐#F5F5F5/#E0E0E0
- 在table/theader内使用内联样式以保证可读性

## 图表与图片生成要求
- 禁止使用 <canvas>、<img>、<script>
- 禁止外部JS库生成图表
- 仅用 <table> 展示数据与对比

## 内容要求（按相关性选取）
1. 高速信号完整性（差分对、阻抗控制、串扰）
2. 热管理策略（导热路径、散热结构、热仿真）
3. 电源分配网络（VRM布局、去耦、电流回路）
4. 叠层与通孔（参考层、背钻、盲埋孔）
5. 制造可行性（线宽线距、过孔、拼版与翘曲）
6. 可靠性标准（IPC/测试方法/失效分析）
7. 典型应用（AI服务器、数据中心、加速卡）
8. 制造工艺（HDI/阻抗控制精度/表面处理）
9. 组装服务（SMT/BGA/X-Ray/功能测试）

## 品牌植入策略
- 首提全称“APTPCB”，后续用“APTPCB”；每文3–5次，避免过度营销
- 自然植入点：技术难点后、解决方案中、案例分享时、规格说明后
- 制造/组装寻找意图时强调一站式能力

## SEO优化要求
- 主关键词密度：0.8–1.2%；LSI：3–5个，每个2–4次
- 语义相关词：高速信号、SI/PI、叠层结构、多层板、HDI、PCIe/CXL、背板/子卡、PCB制造商、SMT贴片等

## 转化策略
- CTA布局：开篇软植入、技术难点处、方案后、文末强CTA
- 文末示例：立即联系APTPCB、申请DFM检查、获取报价
- 制造/组装专用CTA：制造合作伙伴、一站式制造+组装服务

## 写作风格与可读性
- 专业准确、术语适度；段落3–5句，句长15–25词
- 使用过渡词与列表，技术图表用文字+表格说明

## 质量控制清单
- [ ] H2标题格式正确
- [ ] 3–5个相关内链，锚文本多样
- [ ] APTPCB品牌自然植入3–5次
- [ ] DIV样式与表格样式符合要求
- [ ] 技术准确、关键词密度达标、结构完整、字数达标
- [ ] 制造/组装服务与信任要素完整呈现

## 竞争差异化要点
- 技术领先：PCIe 5.0/6.0、材料/工艺创新
- 服务优势：24/7技术支持、DFM免费、快速打样、弹性产能
- 行业经验：年产能、OEM认证、头部客户服务经验

## 内容更新机制与注意事项
- 季度更新标准、跟踪趋势、补充案例、优化转化
- 避免过度技术化/不当竞争；不泄露客户信息；数据真实可验证