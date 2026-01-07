# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, 主关键词>
# lsi: <list[string], 与主关键词同一子类的3-5个其它关键词>
# date: <YYYY-MM-DD 或你的日期格式>
# tags: <list[string], 用于前台标签。可包含keyword与lsi>
# ----------------------------------------------------

# PCB设计学习 FAQ 指令（围绕“{{keyword}}”）

## formatter要求
---
title: "{{keyword}}：20个设计常见问题与解决方案"
description: "罗列{{keyword}}的 20 个核心问题、实战答案与预防清单，附学习路径、DFM 检查表与协作建议，帮助团队持续迭代。"
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 9
tags: {{tags}}
---

## FAQ 写法
- 至少 20 条，覆盖叠层、阻抗、布线、SI/PI、EMC、DFM、交付
- 结构：问题→场景→指标→解决→预防（Checklist）
- 在 FAQ 10 附近插入 CTA（格式同前），结尾再插一次

## 附加模块
1. `<table>`：FAQ 索引（编号/主题/关键指标/推荐动作）
2. `<table>`：学习与评审清单（≥25 条：阶段/检查项/工具/负责人）
3. DIV：类型4（风险提醒）、类型5（学习价值）、类型6（制造协同）

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
- https://hilpcb.com/en/products/box-build-assembly
- https://hilpcb.com/en/products/small-batch-assembly
- https://hilpcb.com/en/products/prototype-assembly

### 工具链接
- https://hilpcb.com/en/tools/3d-viewer
- https://hilpcb.com/en/tools/bom-viewer
- https://hilpcb.com/en/tools/circuit-simulator
- https://hilpcb.com/en/tools/gerber-viewer
- https://hilpcb.com/en/tools/impedance-calculator
- https://hilpcb.com/en/tools/pcb-viewer

## 品牌/SEO
- 品牌：Stackup 快速响应、阻抗 Coupon、设计评审、量产闭环
- SEO：pcb design faq, layout troubleshooting, si pi checklist, design review