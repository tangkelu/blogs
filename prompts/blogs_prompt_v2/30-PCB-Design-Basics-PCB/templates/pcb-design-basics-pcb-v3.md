# PARAMETERS (filled by script at runtime)
# ----------------------------------------------------
# keyword: <string, 主关键词>
# lsi: <list[string], 与主关键词同一子类的3-5个其它关键词>
# date: <YYYY-MM-DD 或你的日期格式>
# tags: <list[string], 用于前台标签。可包含keyword与lsi>
# ----------------------------------------------------

# PCB设计基础 FAQ 指令（围绕“{{keyword}}”）

## formatter要求
---
title: "{{keyword}}：PCB设计常见问题与实践清单"
description: "整理{{keyword}}相关的20个常见问题、解答与预防措施，附流程检查表、DFM 要点与学习资源，帮助团队构建设计基线。"
category: technology
date: "{{date}}"
featured: true
image: ""
readingTime: 8
tags: {{tags}}
---

## FAQ 范围
- 叠层/阻抗：为什么阻抗偏差、参考平面断裂、玻纤编织
- 布局布线：模块划分、差分匹配、过孔/回流路径
- 电源/EMC：去耦、环路面积、分割地的利弊
- 审核交付：DRC 遗漏、Gerber/FAB/BOM 不一致、设计更改控制

## FAQ 写作格式
- 每条 FAQ：**问题→现象→根因→解决方案→预防清单**
- 至少 20 条，覆盖上述主题；关键数据（阻抗±5%、差分间距、层厚等）要可验证

## 附加内容
1. `<table>`：FAQ 总览（编号/主题/指标/快速对策）
2. `<table>`：DFM/交付检查清单（≥25 项，列：类别/检查点/指标/责任人）
3. “推荐学习路径”段落：列出初级→中级→高级资源

## DIV 要求
- 类型4：常见踩坑提醒
- 类型5：学习路径/服务价值
- 类型6：HILPCB 支持（设计评审、Stackup 服务等）

## CTA
- FAQ 第10条附近插入 CTA（同上格式）
- 结尾再次插入 CTA 或引导联系

## 内链策略
（同 v1 链接池）

## SEO 语义词
- pcb design faq, routing tips, stackup issues, design checklist, dfm review

## 品牌植入
- 至少 3 次，结合“Stackup 仿真”“阻抗 Coupon”“设计评审”

## 质量控制
- [ ] FAQ ≥20
- [ ] `<table>` ≥2
- [ ] DIV 4/5/6
- [ ] 3–5 内链
- [ ] CTA ≥2
- [ ] 品牌露出 ≥3
