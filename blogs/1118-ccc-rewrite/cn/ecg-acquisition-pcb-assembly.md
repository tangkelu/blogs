---
title: "ECG 采集 PCB 组装要控制什么：低噪声装配、清洁度与可穿戴可靠性"
description: "直接回答 ECG 采集 PCB 组装中最先看的共模抑制、输入泄漏、清洁度、柔性结构应力和功能验证方法，帮助医疗与可穿戴项目把低噪声设计真正落到量产。"
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["Medical PCB assembly", "ECG acquisition PCB", "Wearable device PCB", "Low-noise PCB design", "ECG patch", "Clinical wearable"]
---

# ECG 采集 PCB 组装要控制什么：低噪声装配、清洁度与可穿戴可靠性

- **ECG 采集板的装配目标不是“能开机”，而是“低噪声信号链在量产里仍然成立”。** 对医疗与可穿戴 ECG，贴装、清洁、返修、屏蔽和测试过程都会直接改变基线稳定性与工频干扰表现。
- **共模抑制和 RLD 回路不能只在原理图里存在。** TI 的 ECG 应用资料明确指出，电极阻抗、线缆、板上保护网络和 50/60Hz 干扰都会共同决定 CMR；装配质量差会把这些理论余量吃掉。
- **高阻输入区最怕污染、湿气和人为接触。** 对干电极或可穿戴 ECG，Analog Devices 的公开资料指出电极阻抗可能比传统湿电极高 100 到 1000 倍，此时泄漏、残留和输入偏置带来的影响会被明显放大。
- **柔性与刚柔结合结构会把机械应力直接带进模拟链路。** 如果器件、补强、连接器和弯折区没有一起评审，样板能通过，也可能在佩戴和充电循环后出现波形漂移或接触不稳定。
- **功能测试必须包含真实信号链验证和可追溯记录。** IEC 60601-2-47 关注的是 ambulatory ECG system 的安全与 essential performance；对组装端来说，这意味着测试、记录、批次追溯和变更控制都属于交付的一部分。

> **Quick Answer**  
> ECG 采集 PCB 组装的核心，是让高阻、低噪声模拟前端在贴装、清洁、返修、柔性应力和系统联调后仍保持稳定。真正需要控制的不是单个焊点，而是共模抑制、输入泄漏、清洁度、结构应力和可追溯功能验证这五条链路。

## 目录

- [ECG 采集 PCB 组装在工程上先看什么？](#ecg-采集-pcb-组装在工程上先看什么)
- [关键规则与参数总表](#关键规则与参数总表)
- [为什么 ECG 板的装配风险不只是焊接缺陷？](#为什么-ecg-板的装配风险不只是焊接缺陷)
- [清洁度、残留和高阻输入为什么必须一起管？](#清洁度残留和高阻输入为什么必须一起管)
- [柔性、无线和电源模块会怎样反向污染 ECG 通道？](#柔性无线和电源模块会怎样反向污染-ecg-通道)
- [量产前该怎么做 ECG 组装验证？](#量产前该怎么做-ecg-组装验证)
- [与 HILPCB 相关的下一步](#与-hilpcb-相关的下一步)
- [常见问题（FAQ）](#常见问题faq)
- [公开参考资料](#公开参考资料)
- [作者与审核信息](#作者与审核信息)

## ECG 采集 PCB 组装在工程上先看什么？

先看 **电极类型、共模抑制路径、高阻节点保护、结构应力、功能验证方式**。

这个问题不等于“贴片质量要好一点”，也不等于“医疗板比普通板更严格”。根据 TI 的 ECG 共模抑制应用报告，ECG 系统中的 50/60Hz 干扰不仅来自电源环境，还会通过皮肤、电极线缆、保护网络和板上 RC 失配一起耦合进前端；而 RLD、Faraday shield、隔离与后级处理都只是改善路径的一部分，不是替代装配控制的捷径。对可穿戴版本，还要额外考虑电极阻抗变化和机械应力。

工程上更稳妥的顺序是：

1. **先确认是湿电极、干电极还是贴片电极结构**  
2. **再确认 AFE/RLD/lead-off 与输入保护网络的装配敏感点**  
3. **再决定 no-clean 还是可清洗工艺，以及返修边界**  
4. **再检查柔性、蓝牙、电池和充电路径会不会把噪声注回模拟区**  
5. **最后把功能测试与可追溯记录一起定义，而不是只做 ICT 或上电测试**

如果项目已经进入样板或 NPI 阶段，建议尽早把 [SMT 组装](https://hilpcb.com/en/products/smt-assembly) 的工艺窗口与 [一站式组装](https://hilpcb.com/en/products/turnkey-assembly) 的测试边界一起拉入评审，而不是把 ECG 性能问题留到整机联调后再追。

## 关键规则与参数总表

| 规则 / 参数 | 推荐范围或判断方式 | 为什么重要 | 怎么验证 | 如果忽略会怎样 |
|---|---|---|---|---|
| 电极类型 | 先区分湿电极、干电极、贴片或多导联结构 | 电极阻抗和装配敏感点完全不同 | 需求定义、AFE 方案、样机结构评审 | 输入缓冲、清洁度和噪声预算全失真 |
| 共模抑制路径 | 把 RLD、保护电阻、RC 失配和屏蔽一起看 | ECG 工频噪声常由整条路径共同决定 | 原理图 + 装配后噪声测试 | 50/60Hz 干扰抬升，信号链余量变小 |
| 高阻节点保护 | 输入区避免残留、吸湿、手工反复返修 | 高阻输入最怕泄漏和污染 | 清洁度检查、返修限制、噪声对比 | 基线漂移、输入失衡、偶发噪声问题 |
| 柔性区与连接器 | 器件、补强、弯折区和焊点要分区评审 | 结构应力会直接影响低频稳定性 | 弯折寿命、外观与功能复测 | 佩戴后漂移、断裂或接触不稳 |
| 无线与电源模块 | 把蓝牙、充电和 PMIC 当作噪声源评审 | 数字与开关噪声可回注 AFE | 工作状态切换下做波形与噪声测试 | 实验室静态正常，实机工作时噪声升高 |
| 功能与追溯 | 测试结果要能回溯到板号和批次 | 医疗与可穿戴后期排障成本高 | MES / test log / lot record | 出问题后难以定位根因与批次边界 |

<div style="background: linear-gradient(135deg, #f3f7f6 0%, #eef2f8 100%); border: 1px solid #d6dce8; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.82); border-left: 4px solid #5a8ca8; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #41697f; font-weight: 700;">CMR Is Assembly-Sensitive</div>
      <div style="margin-top: 8px; color: #243640;">ECG 的共模抑制不只由芯片决定。电极阻抗、线缆、保护网络和板上失配一旦叠加，装配波动就会直接表现成工频噪声。</div>
    </div>
    <div style="background: rgba(255,255,255,0.82); border-left: 4px solid #4f7d6b; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #375a4d; font-weight: 700;">Cleanliness Protects Input Leakage</div>
      <div style="margin-top: 8px; color: #23352f;">高阻 ECG 输入区要把残留、湿气和返修次数一起控制。对干电极结构，这类问题会比普通消费电子更快放大成波形漂移。</div>
    </div>
    <div style="background: rgba(255,255,255,0.82); border-left: 4px solid #7d6d56; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #635543; font-weight: 700;">Wearables Add Mechanics</div>
      <div style="margin-top: 8px; color: #3a3127;">贴肤设备不是纯 PCB 问题。柔性区、补强、连接器和充电结构如果没有提前冻结，后续佩戴会把机械应力带回信号链。</div>
    </div>
    <div style="background: rgba(255,255,255,0.82); border-left: 4px solid #8c5f7c; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6d4961; font-weight: 700;">Test What Ships</div>
      <div style="margin-top: 8px; color: #3d2535;">只做上电和 AOI 不够。ECG 组装验证要在真实供电、无线和电极连接条件下检查噪声、基线和 lead-off 行为，并保留追溯记录。</div>
    </div>
  </div>
</div>

## 为什么 ECG 板的装配风险不只是焊接缺陷？

结论：**ECG 板最难的部分不是“有没有焊上”，而是“装配后整条低噪声路径是否仍然闭合”。**

TI 的 `Improving Common-Mode Rejection Using the Right-Leg Drive Amplifier` 明确指出，ECG 系统里的共模转差模问题会由电极阻抗、线缆阻抗以及前端保护网络中的电阻、电容和二极管共同决定；即使使用 1% 外部器件，系统 CMR 也可能因失配而明显下降。该报告还把 Faraday shield、隔离、电阻驱动共模电压和闭环 RLD 都列为改善手段，并提醒要同时考虑病人和操作者安全。

这对组装的直接含义是：

- **AFE 旁边的每一次返修都可能改变前端对称性**
- **输入保护、RLD 路径和 lead-off 网络不能只看原理图，必须看焊后实物状态**
- **屏蔽件、连接器和线缆接地如果装配不一致，工频噪声会在不同批次间漂移**

如果你用的是 TI AFE4960 这类可穿戴 ECG AFE，官方 datasheet 已经明确写到它支持 ECG、respiration、pace detection，并可用于 IEC 60601-2-47 与 IEC 60601-2-27 相关系统。这说明芯片级能力本身已经为医疗与可穿戴系统准备了接口，但最终能否达标，仍取决于装配是否把这些能力保留下来。

对需要批量贴装和前端噪声控制的项目，实际推进时更适合把 AFE 区和系统区分别冻结，再与 [小批量组装](https://hilpcb.com/en/products/small-batch-assembly) 或 [SMT 组装](https://hilpcb.com/en/products/smt-assembly) 工艺边界一起确认，而不是把所有问题压到试产末端。

## 清洁度、残留和高阻输入为什么必须一起管？

结论：**因为 ECG 输入区往往是高阻、低频、低幅值信号链，任何微小泄漏和污染都比普通数字板更容易变成可见问题。**

Analog Devices 关于干电极 ECG 的设计说明给出了一个很实用的公开语境：传统湿电极阻抗可在 **10kΩ** 量级，而干电极可能高出 **100 到 1000 倍**，例如 **10MΩ**。当电极阻抗升高后，AFE 前端就需要更高输入阻抗、更低偏置电流和更低噪声缓冲，否则 ECG 信号会被明显衰减，系统噪声也更容易超过标准要求。

这意味着对 ECG 装配端来说，清洁度不是“外观更漂亮”这么简单，而是直接关联：

- 输入区是否存在助焊剂或离子残留
- 清洗液是否能真正进入并排出高密度器件底部与电极接口区
- 烘干和储存是否会让湿气重新引入泄漏路径
- 返修后是否重新改变了高阻节点周边表面状态

这里不宜编造一个统一的“离子洁净度万能阈值”，因为不同产品、不同标准路线和不同 AFE 架构的边界并不一样。更稳妥的项目级做法通常是：

| 场景 | 更适合的工艺判断 | 重点确认项 |
|---|---|---|
| 湿电极、低导联、样板验证 | 可接受较简单清洗路径，但要保留噪声复测 | 输入区返修次数、清洗后基线稳定性 |
| 干电极、贴肤可穿戴 | 优先按高阻输入思路定义工艺 | 输入泄漏、湿热后噪声、佩戴后重复性 |
| 柔性或刚柔结合版本 | 清洗与干燥必须和结构一起看 | 补强边界、连接器区残留、弯折后复测 |

如果产品同时涉及柔性结构，建议把 [刚挠结合 PCB](https://hilpcb.com/en/products/rigid-flex-pcb) 的结构边界和 [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) 阶段的清洁度验证一起绑定，而不是先做结构、再补工艺。

## 柔性、无线和电源模块会怎样反向污染 ECG 通道？

结论：**在可穿戴 ECG 里，真正的噪声源往往不只在 AFE 输入端，电池、蓝牙、充电、屏蔽和柔性结构都会通过装配把问题带回来。**

TI 的 ECG 共模抑制报告已经点出，干扰既可以从皮肤、电极和线缆耦合，也可以从供电和系统地之间的耦合路径进入。对可穿戴 ECG，这条链会更长，因为设备往往还带：

- 蓝牙射频与天线
- 充电管理或无线充电
- PMIC / DCDC / LDO
- 柔性区连接器或 FPC
- 壳体、屏蔽罩与导电泡棉

与此同时，Analog Devices 关于 WCT/RLD 和 shield drive 的说明也提醒，医疗 wearable 里的 shield drive 需要额外补偿组件来稳定驱动被屏蔽电缆的电容负载。这意味着结构、线缆和 shield 本身就会改变 ECG 前端行为，不是“后加一个屏蔽件”就能解决。

对装配团队，最重要的不是记住某种固定拓扑，而是把以下几项在工艺评审里显式冻结：

1. **模拟前端、RLD 与屏蔽路径是否允许后期改位或替代料**
2. **柔性区、连接器和补强边界是否避开敏感焊点与高阻节点**
3. **无线发射、充电和显示工作状态下是否做过真实噪声复测**
4. **屏蔽件焊接、接地弹片或导电连接是否在批量里可重复**

如果项目最后要落成贴片、盒装和测试一体流程，这类设备通常更适合在 [Box Build Assembly](https://hilpcb.com/en/products/box-build-assembly) 或 [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) 维度一次性冻结结构、电源和测试路线。

## 量产前该怎么做 ECG 组装验证？

结论：**ECG 组装验证的重点不是“测试项目越多越好”，而是“测试条件要像真实出货状态”。**

IEC 60601-2-47 的公开标准目录说明，该标准面向 ambulatory electrocardiographic systems 的 safety 和 essential performance；其内容还覆盖了 marking、instructions for use、electrostatic discharge、radiated immunity 以及数据准确性相关要求。对 ECG 组装项目来说，这意味着验证不应只停留在 AOI、X-Ray 或 ICT，而要覆盖真实使用条件下的性能保持。

结合 TI 的 AFE4960、RLD/lead-off 文档和可穿戴应用语境，更实用的量产前验证路径通常是：

| 验证项 | 主要回答什么问题 | 推荐观察点 |
|---|---|---|
| 上电与基本功能 | 板子是否完成基础装配 | AFE 通讯、lead-off、参考电压、静态电流 |
| 模拟噪声与基线检查 | 装配是否破坏低噪声路径 | 空载噪声、工频干扰、基线稳定性 |
| 工作状态联测 | 系统模块是否反向污染 ECG | 蓝牙发射、充电、显示或振动开启时的波形 |
| 结构可靠性复测 | 佩戴/弯折/连接动作是否引入新问题 | 柔性区、连接器、补强边界、壳体装配后复测 |
| 追溯记录 | 后续能否定位批次问题 | 板号、元件 lot、工艺参数、测试结果绑定 |

如果你已经准备进入验证批，建议至少把以下输入整理给制造和测试团队：

1. ECG 导联结构、AFE 型号和 RLD/lead-off 方案  
2. 电极类型与目标佩戴形态  
3. 是否带蓝牙、充电、柔性区或刚柔结合结构  
4. 噪声、基线和功能判定方式  
5. 板号、批次、清洗/返修记录与功能测试结果的追溯要求  

## 与 HILPCB 相关的下一步

如果你现在要推进 ECG 采集板的装配方案，下一步最有价值的是把“模拟约束”转成“工艺输入”：

- 需要先冻结模拟前端与贴装窗口时，可先从 [SMT 组装](https://hilpcb.com/en/products/smt-assembly) 路径确认 AFE、屏蔽件和返修边界。
- 如果项目带柔性区、贴片结构或刚柔结合版本，建议同步核对 [刚挠结合 PCB](https://hilpcb.com/en/products/rigid-flex-pcb) 的补强、弯折和装配窗口。
- 进入样板或验证批前，把高阻输入区、清洁度与噪声复测策略带入 [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) 阶段会更稳妥。
- 如果希望把贴装、来料和功能测试一并闭环，直接把测试与追溯要求纳入 [一站式组装](https://hilpcb.com/en/products/turnkey-assembly) 或 [Quote / RFQ](https://hilpcb.com/en/quote/) 说明会更有效。

## 常见问题（FAQ）

<!-- faq:start -->

### ECG 采集板为什么不能只做 AOI 和上电测试？

因为很多 ECG 问题不是焊点开路短路，而是工频干扰、基线漂移、输入泄漏或结构应力。这些问题只有在真实信号链工作、无线/充电开启或佩戴状态下才会暴露。

### 干电极 ECG 为什么对装配更敏感？

公开资料显示，干电极阻抗可能比传统湿电极高 100 到 1000 倍。电极阻抗越高，输入偏置、残留、湿气和泄漏路径的影响就越容易被放大，所以装配清洁度和输入保护更关键。

### ECG 板一定要清洗吗？

不一定绝对，但不能把 no-clean 当成默认安全答案。是否清洗，要结合电极类型、高阻输入区布局、器件底部结构、可穿戴环境和返修策略一起判断，然后用噪声和漂移测试去验证，而不是只看工艺习惯。

### RLD 回路设计好了，装配问题还会影响工频噪声吗？

会。ECG 的 CMR 受电极、线缆、保护网络和板上失配共同影响。RLD 可以改善共模抑制，但装配不一致、屏蔽接触不好或高阻输入区受污染，仍然会让工频噪声升高。

### 医疗或可穿戴 ECG 的追溯记录为什么要做到板级？

因为这类产品的噪声和稳定性问题往往不是一次性失效，而是批次差异、返修差异或结构变化带来的细微偏移。没有板级测试和 lot 追溯，后续根因分析会非常慢。

<!-- faq:end -->

## 公开参考资料

1. [TI AFE4960 Datasheet](https://www.ti.com/lit/ds/symlink/afe4960.pdf)  
   支撑本文关于 AFE4960 支持 ECG、respiration、pace detection，以及可用于 IEC 60601-2-47 / 60601-2-27 相关系统的公开语境。

2. [TI Improving Common-Mode Rejection Using the Right-Leg Drive Amplifier](https://www.ti.com/lit/pdf/sbaa188)  
   支撑本文关于 ECG 中 50/60Hz 干扰来源、RLD 作用、Faraday shield、隔离以及电极/线缆/保护网络失配会降低 CMR 的工程结论。

3. [TI Understanding Lead-Off Detection in ECG](https://www.ti.com/lit/pdf/sbaa196)  
   支撑本文关于 lead-off 作为 ECG 系统验证链路一部分的语境，以及 ECG 前端验证不应只停留在上电层面的判断。

4. [Analog Devices: How to Add Wilson’s Central Terminal/Right Leg Drive Functions to the MAX30001/MAX30003 ECG AFEs in a Medical Wearable](https://www.analog.com/en/resources/design-notes/how-to-add-wilsons-central-terminalright-leg-drive-functions.html)  
   支撑本文关于 wearable ECG 中 WCT/RLD、50Hz/60Hz 干扰抑制和 shield drive 需要稳定补偿设计的说明。

5. [Analog Devices: High-Impedance and Low-Noise Op Amps Enable Dry Electrodes in Medical Systems](https://www.analog.com/en/resources/design-notes/highimpedance-and-lownoise-op-amps-enable-dry-electrodes-in-medical-systems.html)  
   支撑本文关于干电极阻抗显著高于传统湿电极，以及高阻输入、低偏置电流和低噪声缓冲对 wearable ECG 的重要性。

6. [IEC 60601-2-47 Standard Listing](https://standards.iteh.ai/catalog/standards/iec/e9f39061-7265-48e4-9bda-3b71d1af3eba/iec-60601-2-47-2001)  
   支撑本文关于 ambulatory ECG system 的 safety、essential performance、标识、EMC 和准确性语境，不把医疗合规误写成单纯的焊接要求。

## 作者与审核信息

- 作者：HILPCB 医疗电子与可穿戴内容团队
- 技术审核：PCB 装配工艺与低噪声硬件工程团队
- 最近更新：2025-11-18
