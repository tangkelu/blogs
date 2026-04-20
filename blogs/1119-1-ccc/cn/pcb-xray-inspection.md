---
title: "PCB X-Ray 检测到底该看什么：不只是拍出空洞图"
description: "直接回答 PCB X-Ray 检测中最该前置定义的适用范围、缺陷判读、抽样逻辑、工艺回溯和追溯链路，帮助 BGA、BTC 与高可靠性 PCBA 项目把隐藏焊点风险更早收敛。"
category: technology
date: "2025-11-19"
featured: true
image: ""
readingTime: 10
tags: ["x-ray inspection", "pcba quality", "bga inspection", "void analysis", "traceability"]
---

# PCB X-Ray 检测到底该看什么：不只是拍出空洞图

- **PCB X-Ray 检测真正先解决的，不是“有没有拍到缺陷图”，而是隐藏焊点质量能否和装配过程、抽样规则、追溯链路真正闭环。** IPC-7095E 与 IPC-7093 的公开标题都把 design、assembly process guidance 放在核心位置，说明 X-Ray 不该只是事后图片判断。
- **X-Ray 不应该只盯“空洞”一个词。** 对 BGA、BTC、QFN、LGA 和大底部焊盘器件来说，润湿、桥连、错位、头枕、焊点一致性和空洞分布都是不同的风险维度。
- **最有价值的 X-Ray 不是找到一块坏板，而是能反推钢网、锡膏、焊盘、回流和器件受潮条件。** 如果图像不能回到工艺，质量改进会很慢。
- **抽样策略必须和封装风险、批次变化和失效成本绑定。** 新封装、新钢网、新锡膏或新回流窗口，都不适合继续沿用旧的抽样密度。
- **没有批次、设备、程序和判定记录绑定的 X-Ray 图像，很难支持后续根因分析和客诉处理。**

> **Quick Answer**  
> PCB X-Ray 检测的核心，不是把图片拍清楚，而是提前定义哪些器件必须看、看哪类隐藏焊点风险、图像如何回到工艺、以及结果如何进入追溯链路。对 BGA、BTC 和高可靠性 PCBA 来说，X-Ray 是过程控制工具，不只是验收动作。

## 目录

- [PCB X-Ray 检测在工程上先看什么？](#overview)
- [关键规则与参数总表](#rules)
- [哪些产品和封装应把 X-Ray 纳入常规控制？](#scope)
- [X-Ray 真正该看什么缺陷与信号？](#defects)
- [为什么 X-Ray 的最大价值是反推工艺？](#process)
- [为什么抽样策略和追溯链路必须一起设计？](#sampling)
- [与 HILPCB 相关的下一步](#next-steps)
- [常见问题（FAQ）](#faq)
- [公开参考资料](#references)
- [作者与审核信息](#author)

<a id="overview"></a>
## PCB X-Ray 检测在工程上先看什么？

先看 **封装类型、隐藏焊点风险、缺陷判读逻辑、抽样策略和追溯方式**。

这个问题不等于“设备能不能拍出图”，也不等于“空洞率有没有超线”。IPC-7095E 针对 BGA，IPC-7093 针对 Bottom Termination Components，两个标准标题都明确把 design 与 assembly process guidance 放进讨论范围；IPC 在发布 J-STD-001J 更新时也专门提到新增了面向 X-Ray 图像中 bubbles 的图示说明。这些公开信息放在一起，已经足以说明：X-Ray 应该服务于设计、装配、检验和可靠性，而不是只服务于单张图片判定。

更值得在试产前先冻结的，通常是这五类输入：

- **哪些封装和哪些批次必须纳入常规 X-Ray**
- **每类器件最关键的隐藏焊点风险是什么**
- **图像判读是看空洞、润湿、桥连、错位还是一致性**
- **抽样密度如何随新器件、新工艺和风险等级调整**
- **图像、判定结果和工艺数据如何进入追溯链路**

对于隐藏焊点密集项目，前段通常就应同步把 [SMT 组装](https://hilpcb.com/en/products/smt-assembly) 与 [一站式组装](https://hilpcb.com/en/products/turnkey-assembly) 的过程窗口一起带入评审，而不是让检测策略和装配策略彼此脱节。

<a id="rules"></a>
## 关键规则与参数总表

| 规则 / 参数 | 推荐范围或判断方式 | 为什么重要 | 怎么验证 | 如果忽略会怎样 |
| --- | --- | --- | --- | --- |
| 适用范围 | 先按封装与失效成本定义必须 X-Ray 的对象 | 高风险器件不能等失效后补检 | NPI 评审、封装清单、质量计划 | 关键焊点风险会被漏看 |
| 判读重点 | 不同封装看不同缺陷，不只看空洞 | BGA、BTC、QFN 风险点不同 | 首件图像 review、器件分类 | 图像拍了，但结论无效 |
| 工艺回溯 | 图像要能回到钢网、锡膏、焊盘和回流 | 检测的价值在于改善过程 | 图像与制程参数绑定 | 只能发现问题，难以改进 |
| 抽样策略 | 按风险等级、工艺变更和批次动态调整 | 固定模板抽样容易失真 | 首件与量产抽样分级 | 高风险变更未被及时发现 |
| 追溯链路 | 图像、板号、程序、班次和判定一起存档 | 支撑失效分析和客诉回溯 | MES/记录表、批次绑定 | 后续只能靠猜测追根因 |
| 设计协同 | 焊盘、via in pad、底部焊盘开窗提前评审 | 很多 X-Ray 风险源于设计阶段 | DFM review、封装检查 | 贴片后才发现焊接窗口不足 |

<div style="background: linear-gradient(135deg, #eef2f7 0%, #eef6f2 100%); border: 1px solid #dbe2e9; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.86); border-left: 4px solid #64748b; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #4e5e73; font-weight: 700;">Scope</div>
      <div style="margin-top: 8px; color: #27313a;">先定义哪些封装和哪些批次必须常规 X-Ray。没有范围，后面就只会在问题出现后被动补检。</div>
    </div>
    <div style="background: rgba(255,255,255,0.86); border-left: 4px solid #517a8d; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #40616f; font-weight: 700;">Defect</div>
      <div style="margin-top: 8px; color: #25333d;">不同封装最怕的不是同一种缺陷。空洞、桥连、错位和头枕不能套一个判断模板。</div>
    </div>
    <div style="background: rgba(255,255,255,0.86); border-left: 4px solid #5e7b65; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #4a6251; font-weight: 700;">Feedback</div>
      <div style="margin-top: 8px; color: #28322b;">图像如果不能回到钢网、锡膏、焊盘和回流曲线，就很难真正改善良率。</div>
    </div>
    <div style="background: rgba(255,255,255,0.86); border-left: 4px solid #8a7650; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6c5d40; font-weight: 700;">Traceability</div>
      <div style="margin-top: 8px; color: #382f24;">没有板号、批次、程序和判定结果绑定的 X-Ray 图像，后续对客诉和失效分析帮助有限。</div>
    </div>
  </div>
</div>

<a id="scope"></a>
## 哪些产品和封装应把 X-Ray 纳入常规控制？

结论：**凡是焊点隐藏、返修代价高、导热依赖底部焊盘或现场失效成本高的器件，都更适合把 X-Ray 纳入常规过程。**

IPC-7095E 面向 BGA，IPC-7093 面向 BTC / Bottom Termination Components，这本身就说明这些封装不适合仅靠 AOI 或目视放行。对工程团队来说，更实用的判断不是“有没有 X-Ray 设备”，而是“这类器件如果焊点异常，能否接受等到功能测试或现场失效后才发现”。

常见应重点纳入的对象包括：

- **BGA、CSP 等隐藏球焊点封装**
- **QFN、LGA 和大面积底部散热焊盘器件**
- **对导热路径和焊点一致性敏感的功率器件**
- **返修代价高的高层数、细间距或高密 PCBA**
- **汽车、医疗、工业控制、通信等高可靠性板卡**

如果项目本身已经确认要走批量装配，建议尽早把这些关键器件整理进 [SMT 组装](https://hilpcb.com/en/products/smt-assembly) 或 [一站式组装](https://hilpcb.com/en/products/turnkey-assembly) 的前置控制清单，而不是等到首件后再决定“哪些要拍”。

<a id="defects"></a>
## X-Ray 真正该看什么缺陷与信号？

结论：**X-Ray 真正要看的不是“有没有空洞”，而是这类封装最关键的隐藏焊点失效模式。**

BTC 与 BGA 面对的风险不同，IPC 分别用不同标准处理，本身就说明判读逻辑不能一刀切。对 BGA，更该关注球焊点润湿、塌陷、错位、桥连和 head-in-pillow 类风险；对 BTC、QFN 和大底部焊盘器件，更应关注底部焊点分布、空洞位置、焊点覆盖与一致性。

更有价值的观察重点通常包括：

- **焊点是否形成了合理、连续的润湿形态**
- **隐藏焊点之间是否存在桥连或局部异常聚集**
- **底部焊盘上的空洞是否集中在关键导热或应力区域**
- **同器件、同批次焊点几何是否明显离散**
- **局部异常是否指向设计、印刷或回流问题**

如果板上同时存在大底部散热器件、复杂电源区或高热密度区域，也应同步把 [高导热 PCB](https://hilpcb.com/en/products/high-thermal-pcb) 的热路径和焊盘区结构一起带入判读，而不是把 X-Ray 当成纯装配后动作。

<a id="process"></a>
## 为什么 X-Ray 的最大价值是反推工艺？

结论：**因为真正值得关注的不是某块板坏了，而是同类异常为什么会重复出现。**

IPC-7093 与 IPC-7095 都属于 design and assembly process guidance，而不是单纯的验收图片集。这意味着图像必须和钢网开口、锡膏状态、焊盘设计、via in pad 处理、器件受潮情况以及回流曲线一起看。否则 X-Ray 只能告诉你“这里有问题”，却很难告诉你“问题为什么会反复发生”。

更值得回看的工艺因素通常包括：

- **钢网厚度与开口策略是否适合当前封装**
- **锡膏类型、批次、存储和使用状态是否稳定**
- **焊盘设计、阻焊定义和 via in pad 方案是否合理**
- **回流曲线是否与器件和板厚条件匹配**
- **器件和 PCB 的受潮、翘曲或板形变化是否被忽略**

如果项目仍在首板或试产阶段，通常更适合把这些工艺输入和 [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) 的验证动作一起规划，让检测结果能直接回到 DFM 和制程优化，而不是只形成一份判退报告。

<a id="sampling"></a>
## 为什么抽样策略和追溯链路必须一起设计？

结论：**因为 X-Ray 的控制价值取决于“何时看、看多少、看完能不能追到过程”。**

J-STD-001J 的更新语境已经表明，X-Ray 图像判读正被更正式地纳入装配验收体系。对工程实践来说，这意味着抽样策略不能再是固定模板，而应根据封装风险、制程成熟度、工艺变更和失效代价动态调整。

更合理的做法通常包括：

1. **新封装、新钢网、新锡膏或新回流程序首批提高检查密度。**
2. **对细间距 BGA、大底部焊盘和关键导热器件提高关注等级。**
3. **把抽样结果与板号、班次、程序、锡膏批次和设备参数绑定。**
4. **对重复异常建立升级抽样或全检触发条件。**
5. **把图像判读结果与后续纠正动作一起留档。**

没有追溯链路的 X-Ray 图像，最多只能支持当下的判定；而有追溯链路的 X-Ray 结果，才能真正支持后续失效分析、客诉回溯和工艺改进。接近量产的项目，通常更适合把抽样与追溯要求一起整理进 [Quote / RFQ](https://hilpcb.com/en/quote/) 或前置质量说明。

<a id="next-steps"></a>
## 与 HILPCB 相关的下一步

如果你现在在导入 BGA、QFN、大底部焊盘器件或其他隐藏焊点密集项目，下一步更适合把“检测动作”转成“过程控制输入”：

- 当项目重点在隐藏焊点装配质量时，先把关键器件与控制节点纳入 [SMT 组装](https://hilpcb.com/en/products/smt-assembly) 预审。
- 当需要把 PCB 制造、来料、贴片和测试整合在一起时，可同步用 [一站式组装](https://hilpcb.com/en/products/turnkey-assembly) 路径收敛流程边界。
- 当板上存在高热密度器件或底部散热焊盘时，结合 [高导热 PCB](https://hilpcb.com/en/products/high-thermal-pcb) 复核焊盘与热路径设计。
- 当需要先验证器件封装、焊盘与工艺窗口是否成立时，把关键检查项前置到 [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) 更利于尽早发现问题。
- 当适用范围、抽样逻辑、判读方式和追溯要求已经明确，再整理进 [Quote / RFQ](https://hilpcb.com/en/quote/) 会更容易一次讲清楚。

<a id="faq"></a>
## 常见问题（FAQ）

<!-- faq:start -->

### X-Ray 检测是不是主要看空洞率？

A：不是。空洞只是其中一类风险，很多项目更关键的是润湿、桥连、错位、头枕、焊点覆盖和同批一致性问题。

### 哪些产品最应该把 X-Ray 纳入常规流程？

A：隐藏焊点多、返修代价高、导热依赖底部焊盘或可靠性要求高的产品，都更适合纳入常规 X-Ray 控制。

### 为什么有了 AOI 还不够？

A：因为很多关键焊点在器件底部，AOI 看不到，而这些位置往往正好决定导热路径和长期可靠性。

### 为什么有些 X-Ray 图像看了很多，工艺却改善不明显？

A：常见原因是图像没有和钢网、锡膏、回流、焊盘和批次数据建立关联，导致只能发现异常，不能定位根因。

### 投产前最值得先冻结什么？

A：优先冻结适用范围、缺陷判读逻辑、抽样策略、升级触发条件和追溯链路。这些比单次检测结果更决定长期质量控制效果。

<!-- faq:end -->

<a id="references"></a>
## 公开参考资料

1. [IPC-7095E Table of Contents](https://www.ipc.org/TOC/IPC-7095E_toc.pdf)  
   支撑本文关于 IPC-7095E 面向 BGA 设计与装配过程指导语境的说明。

2. [IPC-7093 Table of Contents](https://www.ipc.org/TOC/IPC-7093.pdf)  
   支撑本文关于 IPC-7093 面向 Bottom Termination Components，且覆盖 X-Ray usage、repair 与 reliability 等章节的说明。

3. [IPC Releases J Revisions to Two Leading Standards for Electronics Assembly](https://www.electronics.org/news-release/ipc-releases-j-revisions-two-leading-standards-electronics-assembly)  
   支撑本文关于 J-STD-001J 更新中新增面向 X-Ray 图像 bubbles 图示语境的说明。

<a id="author"></a>
## 作者与审核信息

- 作者：HILPCB PCBA 质量内容团队
- 技术审核：装配工艺、检测与可靠性工程团队
- 最近更新：2025-11-19
