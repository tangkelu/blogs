---
title: "ADAS 雷达 PCB 材料怎么选：77/79GHz 性能、混压叠层与车规可靠性"
description: "直接回答 ADAS 雷达 PCB 材料选型时最先看的低损耗、铜箔粗糙度、混压兼容性、表面处理与验证路径，帮助在 76-81GHz 设计中平衡毫米波性能与量产稳定性。"
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["ADAS radar PCB", "Automotive PCB", "High-frequency PCB", "PCB materials", "77GHz radar PCB", "mmWave PCB"]
---

# ADAS 雷达 PCB 材料怎么选：77/79GHz 性能、混压叠层与车规可靠性

- **先看材料稳定性，不要只看低损耗典型值。** 对 77/79GHz 雷达板，真正决定可用性的不是 datasheet 上单个 Df 数字，而是 Dk 公差、TCDk、吸湿行为和批次一致性是否能支撑相位与阻抗稳定。
- **铜箔粗糙度会直接放大毫米波插损和相位偏差。** Rogers 的毫米波资料明确指出，粗糙铜面会增加导体损耗，并让等效 Design Dk 偏高；对薄介质雷达板，这个影响更明显。
- **ADAS 雷达板常见正确路径不是“全板都上 PTFE”，而是 RF 层与 FR-4 混压。** 是否能混压、是否兼容 FR-4 类工艺、钻孔与层间配准是否可控，往往比“材料牌号是否高级”更影响量产成败。
- **材料、铜箔和表面处理必须一起评审。** 在毫米波频段，ENIG 这类含镍表面处理可能拉高插损并引入相位波动；铜厚、粗糙度、finish 和薄介质组合要一起看，而不是分开决定。
- **样板成功不等于方案成熟。** 车载雷达材料方案至少要经过代表性 coupon、插损或相位一致性、温循/湿热与混压结构检查，才能判断能否从样板走到 NPI 和量产。

> **Quick Answer**  
> ADAS 雷达 PCB 材料选型的核心，不是单纯寻找“最低损耗板材”，而是同时确认 76-81GHz 下的 Dk/Df 稳定性、铜箔粗糙度、混压叠层兼容性、表面处理影响和车规环境验证路径。能做出稳定雷达板的方案，通常是电性能、制造窗口和可靠性一起成立的方案。

## 目录

- [ADAS 雷达 PCB 材料在工程上先看什么？](#adas-雷达-pcb-材料在工程上先看什么)
- [关键规则与参数总表](#关键规则与参数总表)
- [为什么低损耗不是唯一标准？](#为什么低损耗不是唯一标准)
- [铜箔粗糙度、finish 和薄介质为什么会一起放大损耗？](#铜箔粗糙度finish-和薄介质为什么会一起放大损耗)
- [混压叠层怎么判断能不能量产？](#混压叠层怎么判断能不能量产)
- [量产前应该怎么验证材料方案？](#量产前应该怎么验证材料方案)
- [与 HILPCB 相关的下一步](#与-hilpcb-相关的下一步)
- [常见问题（FAQ）](#常见问题faq)
- [公开参考资料](#公开参考资料)
- [作者与审核信息](#作者与审核信息)

## ADAS 雷达 PCB 材料在工程上先看什么？

先看 **工作频段、Dk/Df 稳定性、铜箔粗糙度、混压兼容性、验证方法**。

这个问题不等于“哪种高频材料最好”，也不等于“77GHz 一律上 PTFE”。根据 Rogers 的汽车雷达技术资料，车载雷达正从 24GHz 向 77GHz/79GHz 甚至 76-81GHz 宽带应用推进，毫米波 PCB 的关键不只是低损耗，还包括相位一致性、材料均匀性和制造可重复性。工程上更稳妥的做法，是先区分：

1. **哪些层是真正的 RF/天线层，哪些层是数字、控制或电源层**  
2. **材料需要满足的是最低插损、最低相位漂移，还是更平衡的成本与制造窗口**  
3. **是否要做 RF 层 + FR-4 的混压叠层**  
4. **铜箔粗糙度、表面处理和微孔工艺是否会反过来破坏毫米波收益**  
5. **供应商能否提供材料批次追溯、混压评审和代表性验证数据**

如果项目已经进入天线、馈线和多芯片雷达模组设计阶段，建议尽早把 [高频 PCB](https://hilpcb.com/en/products/high-frequency-pcb) 的材料窗口和叠层评审一起拉进前期设计冻结，而不是等 layout 完成后再把材料当成采购项处理。

## 关键规则与参数总表

| 规则 / 参数 | 推荐范围或判断方式 | 为什么重要 | 怎么验证 | 如果忽略会怎样 |
|---|---|---|---|---|
| 工作频段 | 明确是 24GHz、77GHz、79GHz 还是 76-81GHz | 频段越高，损耗、相位和制造波动越敏感 | 需求书、RF 预算、天线模型 | 用错材料窗口，样板和量产结果脱节 |
| Dk 稳定性 | 不只看典型 Dk，还要看公差、温漂和板内一致性 | 决定阻抗、相位和阵列一致性 | 材料 datasheet、TCDk、lot review | 通道间偏差增大，校准压力上升 |
| Df / 插损 | 结合介质厚度、铜箔类型和线路结构一起看 | 同一 Df 在不同铜箔和薄介质结构上表现不同 | 差分长度法 / S 参数 / coupon | 只看材料名义低损耗，实板损耗仍超标 |
| 铜箔粗糙度 | RF 层优先评估 rolled copper 或 VLP/LoPro 铜 | 毫米波下导体损耗和相位偏差会被放大 | 材料说明、铜箔规格、插损样条 | 插损抬升、相位响应批次波动 |
| 混压兼容性 | 确认是否支持 RF cap layer + FR-4 multilayer | 多数 ADAS 雷达板不会全板使用同种材料 | stackup review、压合与钻孔评审 | 板翘、配准、孔壁或层间可靠性问题 |
| 表面处理 | RF 区域避免把 finish 选择当作后置工艺 | 镍层和厚度波动会影响 mmWave loss/phase | finish 选型评审、coupon 对比 | 雷达链路额外损耗，量产一致性差 |
| 车规可靠性 | 关注吸湿、热循环、lead-free 兼容性 | 车载环境与装配热应力都更严苛 | IPC 方法、温循/湿热、装配验证 | 实验样能跑，验证批和量产批不稳定 |

<div style="background: linear-gradient(135deg, #f7f2ea 0%, #eef4ef 100%); border: 1px solid #d9cbb8; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.78); border-left: 4px solid #b87333; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #8b5e34; font-weight: 700;">Low-Loss Is Not Enough</div>
      <div style="margin-top: 8px; color: #3f3124;">毫米波材料先看 Dk/Df 的稳定性，再看名义最低损耗。对阵列与相位敏感设计，TCDk 和吸湿行为同样关键。</div>
    </div>
    <div style="background: rgba(255,255,255,0.78); border-left: 4px solid #4d7c63; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #3f6651; font-weight: 700;">Copper Matters</div>
      <div style="margin-top: 8px; color: #253a30;">RF 层不要把铜箔当背景变量。粗糙铜、镍层 finish 和薄介质组合，会直接改变插损和相位响应。</div>
    </div>
    <div style="background: rgba(255,255,255,0.78); border-left: 4px solid #8c6d1f; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #715715; font-weight: 700;">Hybrid Build First</div>
      <div style="margin-top: 8px; color: #3f3620;">多数 ADAS 雷达板最终都回到 RF 材料 + FR-4 混压。能否兼容压合、钻孔和配准，决定样板能否走向量产。</div>
    </div>
    <div style="background: rgba(255,255,255,0.78); border-left: 4px solid #8a4b4b; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6f3a3a; font-weight: 700;">Validate Like Production</div>
      <div style="margin-top: 8px; color: #412626;">只做实验室样板不够。材料方案必须通过代表性 coupon、温循/湿热和结构检查，才能说明量产风险可控。</div>
    </div>
  </div>
</div>

## 为什么低损耗不是唯一标准？

结论很直接：**对 ADAS 雷达板，材料选型应该先追求“稳定可预测”，再追求“最低典型损耗”。**

根据 Rogers 的汽车雷达设计资料，77GHz/79GHz 车载雷达用板要同时面对高频电性能、温度变化和车载环境波动。Rogers RO3003 的官方页面给出的典型数据是 Dk 3.00±0.04、Df 0.0010@10GHz、TCDk 约 -3 ppm/°C，且 water absorption 典型值为 0.04%；Rogers 同时把这类材料明确归入 77GHz 级 active safety / antenna 应用。这类信息的重要性在于：材料不仅要“损耗低”，还要在温度和湿度变化下尽量保持稳定。

对比另一类官方可选材料，Isola Astra MT77 的 datasheet 也把它定位到汽车雷达和长天线应用，典型 Df 为 0.0017，并把它描述为成本上可替代部分 PTFE 微波材料的方案。这里能看出的不是“谁绝对更好”，而是：

- **PTFE 类和超低损耗体系** 更适合把 RF 层损耗压到更低
- **热固性低损耗体系** 往往更容易和 FR-4 类多层制造流程兼容
- **真正的工程判断** 取决于天线长度、馈线损耗预算、层数、数字层复杂度和制造路线

如果你的雷达板同时带有数字控制层、IF 层或多芯片互连层，材料方案通常不能只围绕“天线层最低损耗”来定。这个阶段更适合把 RF 层和混压结构一起与 [Rogers PCB](https://hilpcb.com/en/products/rogers-pcb) 或类似高频层压板工艺能力做前置评审，而不是先把 RF 材料拍板、再让制造端被动适配。

## 铜箔粗糙度、finish 和薄介质为什么会一起放大损耗？

结论：**在毫米波频段，铜箔和表面处理不是后道细节，而是材料方案本身的一部分。**

Rogers 的毫米波 PCB 文章明确指出，较粗糙的铜面会增加导体损耗，还会让高频电磁波表现得像在更高等效 Dk 的介质上传播，因此同时影响插损和相位。文中还强调，这个问题在薄介质结构上更明显；对于高频薄板，选 smoother copper 往往比单纯更换介质材料更快见效。

在 77GHz 车载雷达语境下，Rogers 给出的对比更具体：

- RO3003 标准 ED 铜的平均表面粗糙度约为 **2.0 µm RMS**
- rolled copper 可低到 **0.35 µm RMS**
- 面向汽车毫米波雷达优化的 RO3003G2 使用 **VLP ED copper**，平均粗糙度约 **0.7 µm RMS**

Rogers 的说明同时指出，RO3003G2 在 77GHz 下的设计 Dk 约为 **3.07**，5mil 板厚时插损可到 **1.3 dB/in**。这说明对雷达板来说，材料升级很多时候并不是单看树脂体系，而是“树脂 + 填料 + 铜箔粗糙度”一起升级。

表面处理也不能单独放在 CAM 最后一步决定。Rogers 的毫米波工艺文章指出，含镍 ENIG finish 在毫米波下可能增加插损并引入相位偏差；很多 mmWave 电路更常见的低损耗选择是 ImSn、ImAg 或低损耗 OSP。对 ADAS 雷达来说，含镍 finish 是否可接受，必须结合：

- RF 线宽和线边电流分布
- 是否为 microstrip / GCPW
- 是否要求阵列通道间相位一致性
- 是否存在后续组装和可靠性约束

如果板上同时存在高密互连、BGA 和 RF 馈线，材料和 finish 的评审最好与 [多层 PCB](https://hilpcb.com/en/products/multilayer-pcb) 结构一起做，而不是把 RF 区域和装配区域拆开独立决策。

## 混压叠层怎么判断能不能量产？

结论：**ADAS 雷达材料方案能不能落地，关键通常不在“能不能做一块样板”，而在“RF 层和 FR-4 层能不能长期稳定混压”。**

Rogers RO4830 与 RO4830 Plus 的官方资料都在强化同一件事：这类材料并不是要求整板都换成高频体系，而是可以作为 **FR-4 多层板的 cap layer** 用于 76-81GHz 车载雷达。RO4830 Plus datasheet 明确写到，它面向 76-81GHz automotive radar sensor PCB，支持 FR-4 multi-layer board design 的 cap layer 场景；同时具备无玻纤、VLP copper、良好的 laser drilling、CAF resistance 和 lead-free solder process compatibility。

这类材料路线的意义在于：

- **RF 层** 用低损耗、低粗糙度体系控制天线和馈线损耗
- **数字/控制/电源层** 继续使用更可控、成本更合适的 FR-4 类材料
- **整板制造** 仍然尽量沿用 FR-4 类多层工艺窗口，而不是让整个工厂切换到 PTFE 主导流程

但这并不等于混压天然没有风险。Rogers 的 RO4830 工艺指南还特别提醒，低玻纤含量虽然有助于 electrical uniformity，但在 hybrid multilayer build 里，如果铜分布不平衡，会增加内层 bow and twist 风险；RO4830 Plus 的加工指南则强调，未增强的软材料更适合化学方式处理铜面，且要尽量保留铜面来降低变形。

工程上真正要问供应商的是：

- 这套 RF 材料是否已经验证过与 FR-4 core/prepreg 的压合兼容性
- 你们是否有针对 hybrid multilayer 的 drilling、desmear、microvia 和 finish 经验
- 量产时是使用标准 FR-4 类参数，还是要为 RF cap layer 重新收窄压合和钻孔窗口
- 是否能追溯到具体材料 lot，并在样板与 NPI 阶段保持一致

如果项目同时有微孔、盲埋孔和射频馈线，建议在工艺冻结前把 [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) 阶段的 stackup、材料牌号、铜箔等级和 finish 一并写进评审清单，而不是只把 Gerber 发出去再等问题暴露。

## 量产前应该怎么验证材料方案？

结论：**验证的目标不是证明“这套材料理论上好”，而是证明“这套材料在批量制造后仍然保持毫米波性能和结构稳定”。**

IPC TM-650 的官方目录已经给出了常用方法框架，例如：

- **2.5.5.2A / 2.5.5.5C / 2.5.5.13**：用于 Dk、Df 的不同测试方法
- **2.5.5.7A / 2.5.5.11**：TDR 与传播延迟相关测试
- **2.5.5.12A / 2.5.5.14**：板级高频信号损耗测试
- **2.6.6B / 2.6.7A**：温度循环与热冲击

对 ADAS 雷达材料选型，更有价值的验证通常不是单项数据，而是“一组能反映量产现实的组合验证”：

| 验证项 | 更适合验证什么 | 推荐观察点 |
|---|---|---|
| 材料 Dk/Df 与插损样条 | 材料是否达到 RF 预算 | 同一结构、同一 finish、同一铜箔条件下做对比 |
| RF coupon / 传输线样板 | 实际馈线损耗与相位稳定性 | 薄介质、不同 copper roughness、不同 finish |
| 混压结构检查 | 压合与钻孔窗口是否健康 | 板翘、层间配准、孔壁质量、microvia 成形 |
| 环境与装配验证 | 车载温湿与 lead-free 装配适配性 | 温循、湿热、回流后外观与电性能漂移 |
| 批次一致性复验 | 是否适合 NPI 与 SOP | lot-to-lot 的 loss / phase / yield 变化 |

如果项目准备进入报价或 NPI，最有效的动作通常不是再追加一轮抽象材料讨论，而是把以下资料直接整理给制造端：

1. RF 层目标频段与关键 loss budget  
2. 计划使用的材料牌号、板厚、铜箔类型和 finish  
3. 是否为 FR-4 混压、多层还是带微孔结构  
4. 需要重点关注的相位一致性、阵列一致性或温漂约束  
5. 样板和验证批是否要求保持同一材料 lot 或相同 stackup 逻辑  

## 与 HILPCB 相关的下一步

如果你现在要推进 ADAS 雷达板的材料评审，下一步更适合做的是“把材料方案转成可制造输入”，而不是继续停留在材料名词比较：

- 需要毫米波 RF 层与天线馈线评审时，可先走 [高频 PCB](https://hilpcb.com/en/products/high-frequency-pcb) 路径确认材料窗口与叠层方向。
- 如果已经明确采用 Rogers 或同类高频层压板，建议同步核对 [Rogers PCB](https://hilpcb.com/en/products/rogers-pcb) 的混压、钻孔和表面处理可行性。
- 如果项目处于样板到验证批切换阶段，可把 stackup、材料牌号、铜箔类型和 finish 一并带入 [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) 评审。
- 当材料、结构和验证项已经收敛时，直接整理 RF 层说明、层叠和验证重点进入 [Quote / RFQ](https://hilpcb.com/en/quote/) 会比反复口头沟通更高效。

## 常见问题（FAQ）

<!-- faq:start -->

### ADAS 雷达 PCB 一定要全板都用 PTFE 吗？

不一定。很多 76-81GHz 雷达板会把低损耗材料集中在 RF cap layer 或关键馈线层，其他数字、电源和控制层仍使用 FR-4 类材料。是否全板使用 PTFE，取决于损耗预算、层数、成本和制造窗口，而不是只看频段。

### 77GHz 雷达板为什么不能只按 Df 选材料？

因为毫米波性能不仅受 Df 影响，还受 Dk 公差、TCDk、铜箔粗糙度、finish、板厚和工艺波动影响。对阵列和相位敏感设计，很多时候“更稳定的材料体系”比“名义更低的 Df”更重要。

### 铜箔粗糙度对汽车雷达板真的有那么大影响吗？

有。官方毫米波资料已经明确指出，粗糙铜会提高导体损耗，还会改变等效 Design Dk 和相位响应。尤其在薄介质 77GHz 结构里，铜箔粗糙度和其批次波动都不能被忽略。

### ADAS 雷达板适合用 ENIG 吗？

要谨慎。对于毫米波 RF 区域，含镍 ENIG 可能增加插损并带来相位波动。是否能用，要结合 RF 线结构、finish 厚度控制、装配要求和实际验证结果一起判断，不能简单照搬普通数字板经验。

### 怎么判断混压雷达板已经具备量产条件？

至少要看到三类证据：代表性 RF coupon 或 loss/phase 验证、混压结构的压合与钻孔质量、温循/湿热或 lead-free 装配后的稳定性。如果只有单次样板成功，通常还不能说明量产风险已经关闭。

<!-- faq:end -->

## 公开参考资料

1. [Rogers Automotive Radar Design Considerations for Autonomous and Safety Systems](https://rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/technical-articles/automotive-radar-design-considerations-for-autonomous-and-safety-systems.pdf)  
   支撑本文关于 77GHz/79GHz 车载雷达应用场景、RO3003 在毫米波下的 Dk/TCDk/吸湿特点，以及材料稳定性不应只看单个低损耗指标的判断。

2. [Rogers RO3003 Laminates](https://www.rogerscorp.com/advanced-electronics-solutions/ro3000-series-laminates/ro3003-laminates)  
   支撑本文关于 RO3003 典型 Dk、Df、TCDk、CTE、吸湿和 lead-free compatible 的公开数据引用。

3. [Rogers RO3003G2 Data Sheet](https://www.rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/data-sheets/ro3003g2--data-sheet.pdf)  
   支撑本文关于 77GHz 汽车雷达优化材料、VLP ED copper、77GHz 设计 Dk 和 5mil 插损数据的引用。

4. [Rogers RO4830 Plus Laminates Data Sheet](https://rogerscorp.com/-/media/project/rogerscorp/documents/advanced-electronics-solutions/english/data-sheets/ro4830-plus-laminates-data-sheet.pdf)  
   支撑本文关于 76-81GHz cap layer、FR-4 混压、laser drilling、CAF resistance 与 lead-free solder compatibility 的判断。

5. [Rogers PCB Design and Fabrication Concerns for Millimeter-Wave Circuits](https://www.rogerscorp.com/-/media/project/rogerscorp/documents/articles/english/advanced-connectivity-solutions/pcb-design-and-fabrication-concerns-for-millimeter-wave-circuits.pdf)  
   支撑本文关于铜箔粗糙度、finish、铜厚变化和毫米波相位/插损一致性的工程结论。

6. [Rogers Steering Circuit Materials for 77 GHz Automotive Radar](https://rogerscorp.com/en/-/media/project/rogerscorp/documents/articles/english/advanced-connectivity-solutions/steering-circuit-materials-for-77-ghz-automotive-radar.pdf)  
   支撑本文关于 ED copper、rolled copper、VLP ED copper 粗糙度差异，以及这些差异如何影响 77GHz 损耗和 phase consistency 的判断。

7. [Isola Astra MT77 Laminate and Prepreg Data Sheet](https://www.isola-group.com/wp-content/uploads/data-sheets/astra-mt77-laminate-and-prepreg.pdf)  
   支撑本文关于另一类官方汽车雷达材料选择路径，以及低损耗热固性材料在成本与性能之间的平衡示例。

8. [IPC TM-650 Test Methods Manual](https://www.electronics.org/test-methods)  
   支撑本文关于 Dk/Df、TDR、signal loss、temperature cycling 与 thermal shock 验证路径的测试方法框架。

## 作者与审核信息

- 作者：HILPCB 高频与车载电子内容团队
- 技术审核：PCB 工艺与射频叠层工程团队
- 最近更新：2025-11-18
