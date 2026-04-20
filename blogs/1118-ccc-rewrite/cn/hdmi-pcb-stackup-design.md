---
title: "HDMI PCB 叠层怎么定：100Ω 差分、损耗预算与连接器过渡"
description: "直接回答 HDMI PCB 叠层设计中最先看的速率、100Ω 差分阻抗、参考平面、材料损耗和连接器过渡，帮助 2.0/2.1 高速视频链路在可制造堆叠中保住余量。"
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["HDMI PCB", "PCB stackup design", "Controlled impedance", "High-speed PCB", "TMDS routing", "FRL design"]
---

# HDMI PCB 叠层怎么定：100Ω 差分、损耗预算与连接器过渡

- **HDMI 叠层的核心不是“做几层板”，而是“目标速率下这条链路还有多少制造余量”。** HDMI 2.1b 官方页面明确给出系统带宽能力可到 **48Gbps**；TI 的 TMDS1204 datasheet 则说明 HDMI 2.1 FRL 支持 **3/6/8/10/12Gbps** 每 lane。速率一上去，叠层、连接器和过孔就不能再分开看。
- **HDMI 差分对的基础约束仍然是 100Ω 差分阻抗，但真正难点在于量产后还能不能守住。** TI 多份 HDMI 布局资料都把 **100Ω differential impedance** 作为明确要求，而压合厚度、蚀刻补偿和铜面粗糙度会直接决定实物偏差。
- **参考平面连续性和 launch 过渡，常常比直线段本身更先吃掉眼图余量。** 跨平面、换层、stub 和不合理 anti-pad 很容易把本来合格的差分对变成模式转换和 EMI 问题。
- **不是所有 HDMI 板都必须上高端低损耗材料，但也不是所有项目都适合普通 FR-4。** 更正确的顺序是先按速率、长度和过渡数量算链路余量，再反推 stackup 和材料，而不是先拍板层数。
- **验证一定要引入真实制板数据。** 阻抗 coupon、截面、TDR 或插损测试的价值，在于证明“制造后的几何结构仍接近模型”，而不是只证明仿真里画过 100Ω 差分线。

> **Quick Answer**  
> HDMI PCB 叠层设计的重点，是在目标版本和速率下让 100Ω 差分对、连续参考平面、低损耗几何和连接器过渡一起成立。真正好用的 stackup，不是软件里能算出阻抗，而是压合、蚀刻和装配完成后仍能稳定保住链路余量。

## 目录

- [HDMI PCB 叠层在工程上先看什么？](#hdmi-pcb-叠层在工程上先看什么)
- [关键规则与参数总表](#关键规则与参数总表)
- [为什么 HDMI 叠层要先按速率和长度算损耗预算？](#为什么-hdmi-叠层要先按速率和长度算损耗预算)
- [100Ω 差分阻抗为什么必须和真实制程绑定？](#100ω-差分阻抗为什么必须和真实制程绑定)
- [连接器、换层和 stub 为什么比直线段更危险？](#连接器换层和-stub-为什么比直线段更危险)
- [量产前应该怎么验证 HDMI stackup？](#量产前应该怎么验证-hdmi-stackup)
- [与 HILPCB 相关的下一步](#与-hilpcb-相关的下一步)
- [常见问题（FAQ）](#常见问题faq)
- [公开参考资料](#公开参考资料)
- [作者与审核信息](#作者与审核信息)

## HDMI PCB 叠层在工程上先看什么？

先看 **目标版本、每 lane 速率、板内长度、参考平面、连接器过渡**。

这个问题不等于“按高速规则画差分线”，也不等于“找一套通用 HDMI 线宽线距直接套用”。HDMI Licensing Administrator 的官方 2.1b 页面说明，HDMI 2.1b 支持更高分辨率和刷新率，带宽能力可提升到 **48Gbps**；TI 的 TMDS1204 datasheet 则给出了 HDMI 2.1 FRL 的实际 lane rate 级别：**3/6/8/10/12Gbps**。换句话说，对 HDMI 2.0/2.1 板来说，你真正先要确认的是：

1. **当前链路到底是 HDMI 2.0 TMDS 级别，还是 HDMI 2.1 FRL 级别**  
2. **板内走线长度和连接器位置是否会逼迫换层或长 stub**  
3. **普通 FR-4 是否还有足够余量，还是应切到中低损耗体系**  
4. **参考平面和 launch 区域能不能持续保持连续**  
5. **工厂是否能按目标 stackup 稳定做出 100Ω 差分**

如果项目已经进入原理图后期或布局前期，建议尽早把 [高速 PCB](https://hilpcb.com/en/products/high-speed-pcb) 的 stackup 方向和 [阻抗计算工具](https://hilpcb.com/en/tools/impedance-calculator/) 一起拉进评审，而不是等走线完成后再反推材料与层叠。

## 关键规则与参数总表

| 规则 / 参数 | 推荐范围或判断方式 | 为什么重要 | 怎么验证 | 如果忽略会怎样 |
|---|---|---|---|---|
| HDMI 版本与速率 | 先明确是 TMDS 6Gbps 还是 FRL 最高 12Gbps/lane 语境 | 速率直接决定损耗预算和材料窗口 | 规格书、芯片 datasheet、协议配置 | 用错 stackup，后期眼图和 EMI 都会紧 |
| 差分阻抗 | HDMI 差分对按 100Ω 目标控制 | 基本传输结构约束 | 阻抗计算、coupon、TDR | 反射增加、眼图收窄 |
| 参考平面 | 差分对全路径尽量邻接连续参考平面 | 回流连续性影响 SI 和 EMI | layout review、换层检查 | 模式转换、辐射风险升高 |
| 材料与铜箔 | 按长度、速率和表面粗糙度一起判断 | 高速下损耗和制造公差都会放大 | stackup review、截面、插损测试 | 样板能亮，量产边界变差 |
| 连接器/过孔过渡 | launch、anti-pad、stub 和换层必须单独评审 | 过渡常比直线段更先出问题 | 3D 过渡建模、TDR、实测波形 | 黑屏、花屏、间歇性稳定性差 |
| 制造一致性 | 设计值必须转成工厂可实现几何 | 压合和蚀刻后实际尺寸会偏移 | 截面、coupon、批次对比 | 不同批次链路余量飘移 |

<div style="background: linear-gradient(135deg, #eef4fb 0%, #eef7f5 100%); border: 1px solid #d6e0ea; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4b7aa7; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #365b7e; font-weight: 700;">Version Sets the Stackup</div>
      <div style="margin-top: 8px; color: #223544;">HDMI 2.0 和 2.1 不能共用一套模糊 stackup 思路。先看 lane rate，再决定材料、层数和长度预算。</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4f7d6c; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #395d51; font-weight: 700;">100Ω Must Survive Fabrication</div>
      <div style="margin-top: 8px; color: #22352e;">100Ω 不是软件输入框里的目标值，而是压合、蚀刻和铜面粗糙度叠加之后，工厂还能稳定做出来的实物结果。</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #8a6a4a; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6a523a; font-weight: 700;">Launch Regions Kill Margin Fast</div>
      <div style="margin-top: 8px; color: #3a2e24;">HDMI 板最容易掉余量的常常不是长直线，而是连接器、换层和 stub 这些过渡结构。</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #8a5d78; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6b4760; font-weight: 700;">Validate the Real Geometry</div>
      <div style="margin-top: 8px; color: #3d2636;">真正成熟的 HDMI stackup，要靠 coupon、截面和 TDR/插损数据证明制造后几何仍接近模型，而不是只靠版图 review。</div>
    </div>
  </div>
</div>

## 为什么 HDMI 叠层要先按速率和长度算损耗预算？

结论：**因为 HDMI 的材料和层叠是否够用，取决于实际链路速率、长度和过渡数量，而不是“这类接口一般用什么板材”。**

官方语境已经足够说明这点。HDMI 2.1b 页面明确给出系统带宽能力提升到 **48Gbps**；TI 的 TMDS1204 datasheet 则给出 FRL 的 lane rate 最高到 **12Gbps**。而在 HDMI 2.0 路线下，TI 的 TDP158 datasheet 也明确写到它支持 HDMI 2.0b、TMDS 数据率最高 **6Gbps**，足以对应 4K60 24bpp 等场景。

把这些数字放在 stackup 决策里，真正要回答的不是“FR-4 能不能做 HDMI”，而是：

- **板内路径有多长**
- **中间有多少连接器、ESD 器件、re-driver 或换层**
- **当前 lane rate 下，普通 FR-4 还有没有余量**
- **是否已经进入需要更低损耗铜面和更稳介质厚度的区间**

如果板上只有很短的 TMDS/FRL 路径且过渡少，常规或中低损耗体系可能已经足够；但如果 HDMI 走线较长、连接器位置不理想、还叠加过孔和保护件，那么更合理的动作通常是先收敛 [高速 PCB](https://hilpcb.com/en/products/high-speed-pcb) 叠层，再去锁定布线，而不是先走完线再发现材料窗口不够。

## 100Ω 差分阻抗为什么必须和真实制程绑定？

结论：**因为 HDMI 的 100Ω 差分不是一个抽象目标，而是压合、蚀刻和铜面真实形貌共同决定的结果。**

TI 多份 HDMI 官方资料都把 100Ω 差分作为明确设计要求。例如 TI 的 HDMI layout material 中直接写出“**TRACE IMPEDANCE: 100 OHM DIFFERENTIAL IMPEDANCE**”；处理器产品文档也给出 TMDS differential signal traces 需要做到 **100Ω ±10% differential impedance** 的表述。这说明 HDMI 的基本规则并不模糊，但真正的难点在于制造后还能否保持。

量产里常见的偏差源包括：

- 压合后介质厚度与 nominal 值不完全一致
- 蚀刻后的实线宽与图纸线宽存在补偿差异
- 铜面粗糙度改变高频损耗和等效阻抗
- 阻焊、参考平面形态和邻近铜区让实物模型偏离仿真模型

所以更稳妥的 stackup 流程通常是：

1. 用目标材料体系和厂内经验参数先做阻抗反推  
2. 用 [阻抗计算工具](https://hilpcb.com/en/tools/impedance-calculator/) 或场求解做前期几何判断  
3. 在样板阶段用 coupon/TDR/截面确认实物偏差  
4. 把工厂补偿值回写到正式 stackup 里  

这一步如果省掉，最后经常出现的情况就是“仿真里 100Ω，实板里只剩接近目标但没有余量”。

## 连接器、换层和 stub 为什么比直线段更危险？

结论：**因为 HDMI 直线段通常可控，而 launch、过孔和换层更容易引入模式转换、局部阻抗突变和额外损耗。**

TI 的 TPD12S016 HDMI 保护布局指南给出了很具体的布线要求：TMDS differential pairs 要以 **100Ω differential impedance** 路由；pair 内长度匹配要控制在较小窗口内；不同 pair 之间也要保持足够间距。这类规则的价值，不只是让直线段整齐，而是提醒工程师：过渡段往往才是最需要小心的地方。

对 HDMI stackup 来说，最应单独评审的通常是：

- 连接器 launch 下方是否仍有连续参考平面
- 过孔 pad / anti-pad 是否按目标几何优化
- 换层处是否有地过孔帮助回流闭合
- 通孔 stub 是否需要缩短甚至 back-drill
- 差分对进入 breakout 后是否仍保持对称

如果项目同时还有更高密的接口或模块化连接结构，常常值得把这类 launch 问题与 [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) 的 breakout 能力一起看，而不是只把 HDMI 当成普通视频口布线。

## 量产前应该怎么验证 HDMI stackup？

结论：**真正有用的 HDMI 验证，不是证明“图纸上有 100Ω 差分”，而是证明“制造后的板子仍然守住目标”。**

更实用的验证路径通常包括：

| 验证项 | 主要回答什么问题 | 推荐观察点 |
|---|---|---|
| 阻抗 coupon | 工厂是否把目标几何稳定做出来 | 100Ω 目标值与批次离散度 |
| 截面检查 | 压合和蚀刻后结构有没有偏移 | 介质厚度、线宽、铜形貌 |
| TDR 或插损测试 | 过渡段和整体链路是否健康 | 局部不连续点、直线段与过渡段差异 |
| 多板对比 | 工艺窗口够不够宽 | 不同板间眼图/阻抗/损耗一致性 |
| 实际系统联测 | stackup 是否在真实连接器和器件条件下成立 | 分辨率、刷新率、黑屏花屏边界、EMI 表现 |

如果项目已经准备进入样板或验证批，把 stackup、coupon、launch 和测试项一起带进 [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) 阶段通常最有效，因为 HDMI 的很多问题不是最后调一下 equalizer 就能完全掩盖的。

## 与 HILPCB 相关的下一步

如果你现在要推进 HDMI 板的叠层设计，下一步更适合把“接口要求”转成“可制造输入”：

- 先用 [高速 PCB](https://hilpcb.com/en/products/high-speed-pcb) 路径收敛目标材料、铜箔和层叠方向。
- 在早期就用 [阻抗计算工具](https://hilpcb.com/en/tools/impedance-calculator/) 反推 100Ω 差分的几何范围，而不是布线后再回头猜。
- 如果板上同时有连接器 breakout、换层和更高密度局部扇出，建议同步核对 [多层 PCB](https://hilpcb.com/en/products/multilayer-pcb) 或 [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) 的可实现窗口。
- 当 stackup、coupon 和 launch 评审已经收敛时，直接把这些输入整理进 [Quote / RFQ](https://hilpcb.com/en/quote/) 或 [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) 说明会更高效。

## 常见问题（FAQ）

<!-- faq:start -->

### HDMI 2.1 板一定要用高端低损耗材料吗？

不一定。关键在于实际 lane rate、板内长度、换层和过渡数量。如果路径很短、结构紧凑，常规或中低损耗体系也可能够用；如果链路更长、过渡更多、速率更高，材料窗口就会明显收紧。

### HDMI 差分对是不是只要按 100Ω 画线就可以了？

不可以。100Ω 只是目标值，真实结果还取决于压合厚度、蚀刻补偿、铜面粗糙度、阻焊和参考平面连续性。只按名义 Dk 和线宽线距画线，量产后很容易偏离目标。

### HDMI 差分对需要连续参考平面吗？差分不是自己回流吗？

仍然需要。差分对不是天然脱离参考平面工作。launch、换层或跨分割时，如果回流路径不连续，模式转换和 EMI 风险都会明显上升。

### HDMI 板的问题更常出在线路本身还是连接器过渡？

很多时候更常出在连接器 launch、换层过孔和 stub。直线段通常更容易控制，而过渡结构更容易引入局部阻抗突变和模式转换。

### HDMI stackup 为什么一定要做 coupon 或 TDR 验证？

因为这类验证能告诉你制造后的几何结构是否仍接近模型。没有 coupon、截面或 TDR 数据，所谓“100Ω 差分”往往只是设计值，不是实物值。

<!-- faq:end -->

## 公开参考资料

1. [HDMI 2.1b Specification Overview](https://www.hdmi.org/spec/hdmi2_1/index.aspx)  
   支撑本文关于 HDMI 2.1b 带宽能力可到 48Gbps、支持更高分辨率和刷新率的官方语境。

2. [TI TMDS1204 Datasheet](https://www.ti.com/lit/ds/symlink/tmds1204.pdf)  
   支撑本文关于 HDMI 2.1 FRL 支持 3/6/8/10/12Gbps 每 lane，以及 2.1 sink redriver 应用场景的公开数据。

3. [TI TDP158 Product Page / Datasheet](https://www.ti.com/product/TDP158)  
   支撑本文关于 HDMI 2.0b / 6Gbps TMDS 级别链路语境，以及 HDMI 2.0 stackup 与 TMDS 速率判断。

4. [TI TPD12S016 PCB Layout Guidelines for HDMI ESD Protection](https://www.ti.com/lit/an/slla324/slla324.pdf)  
   支撑本文关于 HDMI 差分对 100Ω、连接器保护器件附近的布局要求以及过渡区需要重点控制的工程结论。

5. [TI HDMI Design Guide](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/138/5684.Texas-Instruments-HDMI-Design-Guide.pdf)  
   支撑本文关于 layer stack、controlled impedance、reference planes、vias 和 routing guidelines 需要联动评审的说明。

6. [TI Processor Documentation Example: TMDS Differential Signal Traces 100Ω ±10%](https://www.ti.com/lit/ds/sprs870b/sprs870b.pdf)  
   支撑本文关于 TMDS differential signal traces 需要做到 100Ω ±10% 差分阻抗的官方表述。

## 作者与审核信息

- 作者：HILPCB 高速接口与叠层内容团队
- 技术审核：PCB 工艺、SI 与高速连接器工程团队
- 最近更新：2025-11-18
