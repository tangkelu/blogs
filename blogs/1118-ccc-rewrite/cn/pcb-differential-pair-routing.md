---
title: "PCB 差分对布线怎么做：阻抗、参考平面、skew 与过孔结构的实用规则"
description: "直接回答 PCB 差分对布线中最先看的目标阻抗、参考平面连续性、对称性、长度补偿、via stub 与制造验证，帮助 USB、PCIe、LVDS、以太网和显示接口在真实叠层中保住信号完整性。"
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["Differential pair routing", "High-speed PCB", "PCB layout", "Signal integrity", "Controlled impedance", "PCB stackup"]
---

# PCB 差分对布线怎么做：阻抗、参考平面、skew 与过孔结构的实用规则

- **差分对布线最先要锁定的不是“是否等长”，而是这对线到底按哪个标准或 datasheet 目标设计。** 不同接口的目标并不一样。NXP 的 PTN3222 eUSB2 指南要求 **85Ω differential impedance**；NXP 的汽车以太网 AN13335 则明确 MDI 要按 **100Ω** edge-coupled microstrip 或 stripline 路由。
- **对称性比“看起来靠得很近”更重要。** Intel 在 AN528 里明确指出，理想差分对需要满足两条线从电气上“看起来一样”，否则会出现 differential-to-common mode conversion。也就是说，差分对的核心不是排版美观，而是结构对称。
- **参考平面连续性和层变换处理，往往比直线段本身更容易把链路做坏。** NXP AN13462 明确要求高速差分线不要跨 plane split，且尽量在同一层、少打 via；Intel 的 via discontinuity 指南则强调 layer change 时要给回流路径配置足够且对称的 GND vias。
- **蛇形补偿、反焊盘和 via stub 都不能机械套模板。** Intel 的 P/N de-skew 指南指出，trace 上做 de-skew trombone 可能造成阻抗波动和 mode conversion；这意味着长度补偿需要放在失配点附近，并且要考虑耦合状态变化。
- **差分对是否可量产，取决于叠层、公差、breakout 和验证是否一起定义。** Intel 82566 布局检查表、NXP 高速接口布局指南都在重复同一件事：目标阻抗、同层路由、via 数量、对称性和回流路径必须作为一组条件交付给工厂，而不是只给一份“100Ω 差分”备注。

> **Quick Answer**  
> PCB 差分对布线的核心，是让两条线在真实叠层、真实铜厚和真实过渡结构下保持对称的传播环境。先确定接口目标阻抗和 skew 预算，再控制同层路由、连续参考平面、对称 via 和适度长度补偿，最后用 coupon、TDR 或系统测试验证制造后的结果。

## 目录

- [PCB 差分对布线在工程上先看什么？](#pcb-差分对布线在工程上先看什么)
- [关键规则与参数总表](#关键规则与参数总表)
- [为什么差分对必须先从标准和叠层开始定义？](#为什么差分对必须先从标准和叠层开始定义)
- [对称性、skew 和蛇形补偿为什么经常被误用？](#对称性skew-和蛇形补偿为什么经常被误用)
- [参考平面、换层和 via stub 为什么是高风险区？](#参考平面换层和-via-stub-为什么是高风险区)
- [量产前应该怎么验证差分对布线？](#量产前应该怎么验证差分对布线)
- [与 HILPCB 相关的下一步](#与-hilpcb-相关的下一步)
- [常见问题（FAQ）](#常见问题faq)
- [公开参考资料](#公开参考资料)
- [作者与审核信息](#作者与审核信息)

## PCB 差分对布线在工程上先看什么？

先看 **接口目标阻抗、叠层、参考平面、对称性、换层策略**。

这个问题不等于“把两根线拉平行”，也不等于“先走完线再让板厂帮忙算阻抗”。不同协议、不同 PHY、不同连接器对差分对的要求并不通用。根据 NXP AN13462，eUSB2 的布局目标是 **85Ω differential impedance**，并要求高速差分线不要跨 plane split；根据 NXP AN13335，汽车以太网 MDI 则要按 **100Ω** 差分对来做，并且连接器与 choke 间的对内长度匹配要控制在 **1 mm** 内。Intel 82566 的布局清单又给出另一套语境，要求千兆以太网 MDI 按 **100Ω differential impedance (±20%)** 设计，且 pair 内长度差保持在 **50 mil** 以内。

这说明差分对布线最先要确认的是：

1. **目标接口到底要求 85Ω、90Ω、95Ω 还是 100Ω 差分**
2. **该接口的 pair 内 skew 预算来自哪里**
3. **走线所在层是 microstrip 还是 stripline，参考平面是否连续**
4. **是否允许换层，换层后如何处理回流和 stub**
5. **板厂是否能按目标叠层稳定做出对应几何**

如果板上高速接口较多，通常应在布局前就同步收敛 [高速 PCB](https://hilpcb.com/en/products/high-speed-pcb) 的 stackup 方向、[多层 PCB](https://hilpcb.com/en/products/multilayer-pcb) 的层别分配，以及 [阻抗计算工具](https://hilpcb.com/en/tools/impedance-calculator/) 的几何窗口，而不是等 DRC 通过后才回头修规则。

## 关键规则与参数总表

| 规则 / 参数 | 推荐范围或判断方式 | 为什么重要 | 怎么验证 | 如果忽略会怎样 |
|---|---|---|---|---|
| 目标阻抗 | 先按接口标准或芯片资料确认，不要套通用值 | 差分对不是统一 100Ω | 标准、datasheet、stackup review | 线宽线距一开始就错 |
| 对称性 | 两条线的截面、参考环境、过渡要尽量一致 | Intel AN528 指出不对称会引发 mode conversion | layout review、3D 过渡对比 | 共模噪声上升、眼图变差 |
| 同层路由 | 高速差分对优先在同一层走完整路径 | 层变换会引入额外不连续 | post-route review、via count | skew、反射和调试难度上升 |
| 参考平面 | 全路径尽量保持连续、单一且靠近 | plane split 会破坏回流路径 | plane review、layer review | EMI 与模式转换恶化 |
| 长度补偿 | 只按接口预算做，尽量靠近失配点补偿 | 错误 serpentine 会造成阻抗波动 | skew review、TDR、仿真 | “补长度”反而制造新问题 |
| via / stub | 减少 via；必须换层时做对称 signal via + GND via | via discontinuity 是高速常见风险 | TDR、截面、backdrill review | 局部反射、ISI、回流绕行 |

| 接口示例 | 官方来源中的典型要求 | 设计提示 |
|---|---|---|
| eUSB2 | NXP AN13462：85Ω，pair 同层对称，长度差 <20 mil，不跨 plane split | 低压高速接口也不能用“差不多就行”的通用规则 |
| 汽车以太网 MDI | NXP AN13335：100Ω，connector 到 choke 之间对内匹配 1 mm，ground via 对称 | 参考地和共模噪声控制与阻抗同样关键 |
| 千兆以太网 MDI | Intel 82566 checklist：100Ω ±20%，pair 内长度差 <50 mil，layer transition 旁 GND via 距离 40 mil 内 | 量产型板卡更强调工艺交付细节 |
| FPGA 真差分 I/O | Intel Agilex guide：100Ω，必要时考虑 backdrill 以减小 stub 影响 | 越高速越应把 via 结构纳入主设计对象 |

<div style="background: linear-gradient(135deg, #eef4fb 0%, #eef6f2 100%); border: 1px solid #d5e0ea; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4a79a2; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #365c7c; font-weight: 700;">Protocol Before Geometry</div>
      <div style="margin-top: 8px; color: #233546;">差分对不是默认 100Ω。先确认接口目标和 skew 预算，再决定线宽线距和层别。</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4b7b72; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #3a6159; font-weight: 700;">Symmetry Beats Cosmetics</div>
      <div style="margin-top: 8px; color: #223630;">真正有效的差分对不是“靠得近”，而是两条线在截面、参考和过渡上保持对称。</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #886847; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6a5138; font-weight: 700;">Return Path Is Part of the Pair</div>
      <div style="margin-top: 8px; color: #3a2f25;">差分对不是脱离参考平面工作的。plane split、地开窗和不对称 stitching 会把回流问题变成 SI 和 EMI 问题。</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #8a5f7d; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6c4960; font-weight: 700;">De-skew Needs Discipline</div>
      <div style="margin-top: 8px; color: #392733;">长度补偿不是越多越好。蛇形位置、耦合变化和 via 反焊盘处理不当，都会把补偿变成新的不连续点。</div>
    </div>
  </div>
</div>

## 为什么差分对必须先从标准和叠层开始定义？

结论：**因为差分对的目标阻抗和几何不是通用模板，而是接口要求与生产叠层共同决定的结果。**

NXP 和 Intel 的公开资料已经把这个问题说明得很清楚。NXP AN13462 对 eUSB2 给出的是 **85Ω** 目标；NXP AN13335 对汽车以太网 MDI 明确要求 **100Ω** edge-coupled microstrip 或 stripline；Intel 的 True Differential I/O 指南则给出 **100Ω** 差分目标，并建议在需要时通过 backdrill 降低 stub 影响。这意味着差分对布线的正确顺序通常是：

1. **先从接口标准、芯片手册或参考设计确定阻抗目标**  
2. **再结合连接器、损耗和 EMI 要求选择 microstrip 或 stripline**  
3. **与板厂确认真实材料、介质厚度、铜厚和工艺补偿**  
4. **最后把线宽线距和容差回写到 layout 规则里**

Intel 的 82566 布局清单还特别提醒，成对的 50Ω 单端线并不天然等于 100Ω 差分，必须结合阻抗计算器和实际叠层来判断。对工程团队来说，这一步最重要的价值是把“理论规则”转成“可制造几何”。如果项目已经开始收敛接口栈，通常应先把 [阻抗计算工具](https://hilpcb.com/en/tools/impedance-calculator/) 与 [高速 PCB](https://hilpcb.com/en/products/high-speed-pcb) 的叠层评审一起完成，而不是先按经验值拉线。

## 对称性、skew 和蛇形补偿为什么经常被误用？

结论：**因为很多团队把“长度相等”误当成“差分对正确”，却忽略了结构对称和局部耦合状态。**

Intel AN528 对理想差分对给出两个核心条件：一是两条线从电气上看必须一样，二是两条线之间的 skew 应尽量接近零。资料还明确指出，不对称会导致阻抗不连续和 differential-to-common mode conversion。这意味着：

- **对称性不仅是线长，还包括截面、介质、邻近铜区和过渡结构**
- **skew 不是独立指标，它和参考环境变化绑在一起**
- **蛇形补偿如果放错位置，可能让补偿段的阻抗比主线更差**

Intel 的 P/N de-skew 指南进一步指出，在 trace 上做 de-skew trombone 会带来两类问题：一类是 loosely coupled 区段导致阻抗波动，另一类是 delay per unit length 不再与直线段一致，进而产生 mode conversion。NXP AN13462 也给出更直接的布局动作：当需要长度补偿时，应尽量在 **mismatch 发生的位置附近** 做补偿，而不是在远处集中堆蛇形。

对差分对来说，更稳妥的做法通常是：

- 先消除器件摆位和 breakout 本身造成的非对称
- 只对真正需要控制的 pair 内 skew 做补偿
- 让补偿段保持平缓、松耦合，不要为“绝对等长”堆密蛇形
- 对玻纤效应敏感的长距离 FR-4 通道，结合 Intel AN528 的建议，考虑对角走线或其它 fiber weave 风险缓解方法

如果板上同时存在 BGA breakout 和高速边缘连接器，通常值得同步检查 [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) 的扇出能力和 [多层 PCB](https://hilpcb.com/en/products/multilayer-pcb) 的层切换策略，避免后期为了补长度被迫制造更多不连续点。

## 参考平面、换层和 via stub 为什么是高风险区？

结论：**因为差分对一旦跨层、跨分割或留下 stub，问题往往先出在回流路径和局部不连续，而不是主走线本身。**

NXP AN13462 明确要求高速差分线不要跨 plane split，并建议差分对尽量在同一层路由、尽量减少 via、不要引入 stub。NXP AN13335 也强调，ground connections next to the MDI pair 必须对称，ground via 的位置要均匀，否则 rise time skew 会转成 common-mode noise。Intel 的 via discontinuity 指南给出了更具体的制造视角：

- 如果信号只在中间层停止，留下的 via 残段会表现成 capacitive stub
- layer change 时必须给 return current 提供足够且靠近的 GND vias
- 差分对两条线的 via 配置必须对称，否则会形成 differential-mode discontinuity

Intel 82566 的布局清单甚至把这个动作写得更明确：当差分信号换层时，GND vias 应放在距信号 via **40 mil** 以内；如果从 ground-referenced 层切到 power-referenced 层，还要在附近通过 decoupling capacitor 把回流桥起来。

这说明高速差分对的高风险区通常是：

1. **BGA breakout 根部**
2. **连接器 launch**
3. **AC 耦合电容和共模器件附近**
4. **层切换 via 和 anti-pad 区**
5. **长板厚里未处理的 through via stub**

如果项目速率更高或板厚更大，通常要尽早把 backdrill、blind/buried via 或更紧凑的 transition 设计纳入 [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) 评审，而不是等首板眼图变差后再补救。

## 量产前应该怎么验证差分对布线？

结论：**真正有价值的验证，不是证明 CAD 里“成对布线”完成了，而是证明制造后的几何和系统行为仍然成立。**

更实用的验证路径通常包括：

| 验证项 | 主要回答什么问题 | 推荐观察点 |
|---|---|---|
| Stackup / 阻抗评审 | 目标几何是否与工厂可制造能力一致 | 线宽线距、铜厚、介质厚度、公差 |
| Coupon / TDR | 实物阻抗和 transition 是否接近设计值 | 阻抗平台、局部不连续点、via 影响 |
| 截面检查 | 压合与蚀刻后结构是否偏移 | 实线宽、铜厚、介质厚度、反焊盘 |
| 系统联测 | 差分对在真实器件与连接器条件下是否健康 | 眼图、链路训练、误码、EMI |
| 多板对比 | 风险来自设计还是 build 波动 | 板间离散、批次一致性、返修难度 |

Intel 82566 清单、NXP AN13462 与 NXP AN13335 的共同点都很明显：目标阻抗、长度差、plane continuity、对称 ground via、stubs 和 test points 这些信息，必须在交付工厂前就写清楚，而不是只靠 layout 工程师脑内默认。

如果项目已经接近打样，通常更稳妥的动作是把 stackup、受控阻抗表、关键 pair 的层别、via/backdrill 要求和验证方式一起带进 [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) 或 [Quote / RFQ](https://hilpcb.com/en/quote/) 输入，而不是只发 Gerber。

## 与 HILPCB 相关的下一步

如果你现在要推进高速差分对板卡，下一步更适合把“布线规则”转成“可制造输入”：

- 先用 [高速 PCB](https://hilpcb.com/en/products/high-speed-pcb) 和 [多层 PCB](https://hilpcb.com/en/products/multilayer-pcb) 路径收敛叠层、层别和参考平面策略。
- 在布局前就用 [阻抗计算工具](https://hilpcb.com/en/tools/impedance-calculator/) 反推不同接口的线宽线距，而不是等走线完成后再改 DRC。
- 如果板上 breakout 密度高、换层频繁，可同步检查 [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) 的扇出与 via 结构窗口。
- 当 stackup、受控阻抗表、关键 diff pair 和验证方式已经确定时，直接把这些输入整理进 [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) 或 [Quote / RFQ](https://hilpcb.com/en/quote/) 会更利于一次评审清楚。

## 常见问题（FAQ）

<!-- faq:start -->

### 差分对是不是默认都按 100Ω 做？

不是。不同接口的目标不同。比如 NXP 的 eUSB2 指南给的是 85Ω，而汽车以太网 MDI 和许多通用高速 I/O 则常见 100Ω。先看标准或芯片资料，不要套通用值。

### 差分对只要两根线等长就够了吗？

不够。Intel AN528 明确指出，理想差分对还必须在电气环境上保持对称。层别、参考平面、邻近铜区、过孔和反焊盘不一致时，等长也可能出现 mode conversion。

### 差分对一定不能换层吗？

不一定，但要尽量少换，而且每次换层都应把 signal via、GND via、anti-pad 和回流路径作为一个结构一起设计。越高速、越厚板，via discontinuity 的影响越明显。

### 蛇形补偿是不是越靠后集中做越方便？

通常不是。NXP 和 Intel 的公开资料都提示，长度补偿应尽量靠近失配发生处，且要避免把补偿段做成新的阻抗不连续区域。为追求报表上的绝对等长而集中堆蛇形，往往得不偿失。

### 差分对为什么也怕参考平面分割？差分不是自己回流吗？

仍然怕。差分对并不是完全脱离参考平面工作的。plane split、地开窗、不对称地 via 或 power reference 切换都会改变回流路径，进而增加共模噪声和辐射风险。

<!-- faq:end -->

## 公开参考资料

1. [Intel AN 528: PCB Dielectric Material Selection and Fiber Weave Effect on High-Speed Channel Routing](https://cdrdv2-public.intel.com/654621/an528.pdf)  
   支撑本文关于理想差分对应满足电气对称与零 skew 目标，以及 fiber weave 会影响长距离高速差分通道一致性的说明。

2. [Intel AN 875: P/N De-skew Strategy on Differential Pairs](https://www.intel.com/content/www/us/en/docs/programmable/683262/current/p-n-de-skew-strategy-on-differential-pairs.html)  
   支撑本文关于 trace trombone 补偿会造成阻抗波动和 mode conversion 风险的工程结论。

3. [Intel AN 958: Via Discontinuity](https://www.intel.com/content/www/us/en/docs/programmable/683073/current/via-discontinuity.html)  
   支撑本文关于 via stub、对称 signal via 配置、layer change 时增加 GND vias 与回流路径管理的说明。

4. [Intel 82566 Layout Checklist](https://www.intel.com/content/dam/doc/design-guide/82566-gbe-layout-checklist-ver-1-0.pdf)  
   支撑本文关于 100Ω differential impedance、pair 内长度差、换层附近 GND via 距离、避免 unused pads/stubs 等量产型差分对布局检查项。

5. [NXP AN13462 PTN3222 Layout Guidelines](https://www.nxp.com/docs/en/application-note/AN13462.pdf)  
   支撑本文关于 eUSB2 的 85Ω 目标、长度匹配、同层对称、避免 plane split、减少 vias 与避免 stubs 的接口级要求。

6. [NXP AN13335 PCB Design Guidelines for Automotive Ethernet](https://www.nxp.com/docs/en/application-note/AN13335.pdf)  
   支撑本文关于 100Ω MDI、ground symmetry、connector-to-choke 长度匹配、同层路由与 common-mode noise 风险的说明。

7. [Intel Agilex 5 True Differential I/O Interface PCB Routing Guidelines](https://www.intel.com/content/www/us/en/docs/programmable/821801/current/true-differential-i-o-interface-pcb.html)  
   支撑本文关于真差分 I/O 100Ω 目标与在需要时考虑 backdrill 以减小 stub 影响的语境。

## 作者与审核信息

- 作者：HILPCB 高速互连与 SI 内容团队
- 技术审核：PCB 工艺、信号完整性与连接器工程团队
- 最近更新：2025-11-18
