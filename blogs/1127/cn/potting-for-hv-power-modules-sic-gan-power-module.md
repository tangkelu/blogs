---
title: "potting for HV power modules：SiC/GaN 的FAQ与测试矩阵"
description: "以 FAQ 形式回答potting for HV power modules的20个问题，并附部分放电/Hipot/EMI测试矩阵及 ≥40 项 NPI 清单。"
category: technology
date: "2025-11-27"
featured: true
image: ""
readingTime: 8
tags: ["potting for HV power modules", "surface finish impact on power loss", "isolated power supply for gate driver", "insulation materials for HV design", "isolation testing during manufacturing", "creepage clearance for high voltage"]
---
对于高压（HV）碳化硅（SiC）和氮化镓（GaN）功率模块，灌封（Potting）不仅是简单的物理填充，更是决定其长期可靠性、电气绝缘性能和热管理能力的关键工艺。一个不完善的 **potting for HV power modules** 方案可能导致灾难性的故障，如绝缘击穿、热失控或机械应力损坏。作为您的FA/NPI顾问，本文将通过20个常见问题（FAQ）、详细的测试矩阵和一份全面的NPI清单，深入剖析高压功率模块灌封的每一个关键环节。

## 灌封材料选择的核心考量是什么？

选择正确的灌封材料是成功的第一步。材料的电气、热学和机械性能必须与SiC/GaN模块的高频、高温、高压工作环境相匹配。

**1. 如何在环氧树脂、有机硅和聚氨酯之间选择？**
*   **症状**：模块在高温或高湿环境下出现绝缘性能下降或开裂。
*   **原因**：材料选择不当。环氧树脂硬度高、粘接力强，但韧性差，易在热冲击下开裂；有机硅柔韧性好、耐温范围宽，但机械强度和粘接力较弱；聚氨酯则介于两者之间。
*   **参数**：硬度（Shore A/D）、工作温度范围、粘接强度、吸水率。
*   **解决**：对于需要高机械强度和刚性的应用，选择改性环氧树脂；对于需要承受宽温域和振动的应用，柔性有机硅是首选。
*   **预防**：在设计初期就根据模块的应力、温度和环境要求，综合评估材料数据表。

**2. 导热率 (TC) 和玻璃化转变温度 (Tg) 如何权衡？**
*   **症状**：模块结温（Tj）超出预期，导致性能下降或过早失效。
*   **原因**：灌封材料的导热率不足，或在工作温度下发生相变。
*   **参数**：导热率 (W/m·K)、玻璃化转变温度 (Tg, °C)。
*   **解决**：选择导热率 > 1.5 W/m·K 的导热灌封胶。同时，确保材料的 Tg 远高于模块的最高工作温度，以避免材料软化导致机械性能和导热性能剧烈下降。
*   **预防**：进行热仿真，评估不同导热率材料对结温的影响。选择 Tg 比最高工作温度至少高出20-30°C的材料。

**3. 灌封材料的介电强度和CTI等级有何要求？**
*   **症状**：模块在高压下发生局部放电或沿面闪络。
*   **原因**：灌封材料的绝缘性能不足。
*   **参数**：介电强度 (kV/mm)、相对漏电起痕指数 (CTI)。
*   **解决**：对于1200V及以上的系统，应选择介电强度 > 20 kV/mm 的材料。同时，CTI等级应达到PLC 0或PLC 1（≥600V），以确保在高污染环境下的绝缘可靠性。这是 **insulation materials for HV design** 的核心指标之一。
*   **预防**：严格审查材料供应商提供的VDE或UL认证报告，确保其电气性能满足设计要求。

## 灌封工艺如何避免常见缺陷？

完美的材料需要精确的工艺来执行。灌封过程中的任何疏忽都可能引入致命缺陷。

**4. 如何防止灌封过程中产生气泡或空洞？**
*   **症状**：部分放电测试不通过，或在热循环后出现局部过热点。
*   **原因**：灌封胶内部残留空气，形成绝缘薄弱点。空气的介电强度远低于灌封材料，在高电场下容易被击穿。
*   **参数**：真空度、搅拌速度、注胶速率、固化压力。
*   **解决**：采用真空灌封工艺。在混合和注胶前对A/B组分进行真空脱泡，并在真空环境下进行注胶，以彻底排除空气。
*   **预防**：制定严格的真空灌封SOP，包括真空度维持时间、注胶路径规划，并定期维护真空设备。

**5. 灌封前的表面清洁和预处理有多重要？**
*   **症状**：灌封胶与模块外壳或PCB表面发生分层、剥离。
*   **原因**：粘接表面存在油污、灰尘、湿气或脱模剂残留，影响了附着力。
*   **参数**：表面能、清洁度标准。
*   **解决**：使用等离子清洗或化学清洗剂（如异丙醇）彻底清洁所有待灌封表面。对于难粘接的材料（如PBT、PPS），可能需要使用底涂剂（Primer）来增强附着力。
*   **预防**：将表面清洁和预处理纳入生产流程的关键控制点（KCP），并进行附着力划格测试或拉拔测试进行验证。

**6. 固化过程中的温度和时间曲线如何优化？**
*   **症状**：灌封胶固化不完全、表面发粘，或固化后内应力过大导致元件损坏。
*   **原因**：固化曲线与材料供应商的建议不符。
*   **参数**：升温速率、恒温温度、恒温时间、降温速率。
*   **解决**：严格遵循材料数据手册（TDS）推荐的固化曲线。对于大型或复杂模块，可采用阶梯式升温，让材料有足够的时间流动和排泡，同时减小固化收缩产生的内应力。
*   **预防**：使用带有程序控温功能的烘箱，并定期对其进行温度均匀性校准。

<!-- COMPONENT: BlogQuickQuoteInline -->

## 灌封如何影响模块的电气性能？

灌封不仅是机械保护，它会直接改变模块的电磁场分布，从而影响其电气性能。

**7. 灌封如何改变爬电距离和电气间隙？**
*   **症状**：模块在安规测试中无法通过，尽管裸板设计满足要求。
*   **原因**：灌封材料填充了原有的空气间隙，其介电常数（通常为3-5）远高于空气（约为1），导致电场分布改变。
*   **参数**：爬电距离 (Creepage)、电气间隙 (Clearance)、介电常数 (εr)。
*   **解决**：在设计阶段，必须考虑灌封后的情况。使用有限元分析（FEA）软件仿真灌封后的电场分布，确保关键位置的电场强度低于材料的击穿阈值。适当增加物理距离或设计绝缘肋是常见的优化手段，以保证足够的 **creepage clearance for high voltage**。
*   **预防**：DFM（可制造性设计）阶段，与像 HilPCBPCB Factory (HILPCB) 这样的专业制造商合作，利用其仿真能力和制造经验，提前优化绝缘设计。

**8. 灌封材料的介电常数如何影响寄生电容和EMI？**
*   **症状**：模块的开关速度变慢，共模噪声增加。
*   **原因**：高介电常数的灌封材料增加了开关节点到散热器（地）之间的寄生电容（Coss, Cgd），这会减缓开关瞬变（dv/dt），并为共模电流提供新的耦合路径。
*   **参数**：介电常数 (εr)、损耗角正切 (tanδ)。
*   **解决**：选择介电常数和损耗角正切尽可能低的灌封材料。在布局布线时，最小化高dv/dt环路面积，并优化接地路径。
*   **预防**：在早期设计中就将灌封材料的电气参数纳入寄生参数提取和电路仿真模型中。

**9. 灌封后部分放电 (PD) 性能为何会恶化？**
*   **症状**：裸模块PD测试通过，但灌封后在更低的电压下就出现放电信号。
*   **原因**：灌封过程中引入了微小气泡，或在灌封胶与元件/基板的界面处存在微小分层。这些缺陷在高电场下成为局部放电的策源地。
*   **解决**：通过优化真空灌封工艺和表面预处理来消除缺陷。进行100%的在线部分放电测试，作为 **isolation testing during manufacturing** 的关键一环，以筛选出不合格品。
*   **预防**：建立严格的工艺控制和在线监测体系，确保灌封质量的一致性。

---
<div style="background-color: #F5F7FA; padding: 20px; border-radius: 8px; margin: 30px 0;">
<h3 style="color: #000000; text-align: center; border-bottom: 2px solid #4CAF50; padding-bottom: 10px;">灌封材料性能对比</h3>
<table style="width:100%; border-collapse: collapse; text-align: center;">
<thead style="background-color: #E0E0E0;">
<tr>
<th style="padding:12px; border: 1px solid #ccc; color: #000000;">性能指标</th>
<th style="padding:12px; border: 1px solid #ccc; color: #000000;">环氧树脂 (Epoxy)</th>
<th style="padding:12px; border: 1px solid #ccc; color: #000000;">有机硅 (Silicone)</th>
<th style="padding:12px; border: 1px solid #ccc; color: #000000;">聚氨酯 (Polyurethane)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">硬度</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">高 (Shore D 70-90)</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">低 (Shore A 10-70)</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">中等 (Shore A 50 - D 60)</td>
</tr>
<tr>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">工作温度</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">-40°C to 150°C</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">-60°C to 250°C</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">-40°C to 130°C</td>
</tr>
<tr>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">导热率 (W/m·K)</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">0.5 - 2.5</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">0.3 - 4.0</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">0.3 - 1.5</td>
</tr>
<tr>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">介电强度 (kV/mm)</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">20 - 28</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">18 - 25</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">15 - 22</td>
</tr>
<tr>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">优点</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">高强度、强粘接力、耐化学性好</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">优异的柔韧性、宽温域、低应力</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">性能均衡、耐磨性好</td>
</tr>
<tr>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">缺点</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">韧性差、内应力大、返修困难</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">机械强度低、粘接力较弱</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">耐温和耐湿性相对较差</td>
</tr>
</tbody>
</table>
</div>
---

## 灌封对热管理和机械应力有何挑战？

灌封层是热量传导的必经之路，也是机械应力的主要来源。

**10. 如何验证灌封后的实际热阻？**
*   **症状**：实测结温高于仿真结果。
*   **原因**：灌封层与散热器或基板之间存在界面热阻，或灌封材料本身存在空洞，导致实际热阻增大。
*   **参数**：结-壳热阻 (Rth,j-c)。
*   **解决**：使用T3Ster等热瞬态测试设备，精确测量灌封后模块的实际热阻抗曲线，并与仿真和设计值进行对比。
*   **预防**：在灌封工艺中确保良好的界面润湿性，并使用声学显微镜（SAM）检查是否存在分层或大尺寸空洞。

**11. 温度循环如何导致灌封胶开裂或分层？**
*   **症状**：模块在进行温度循环或功率循环测试后，出现绝缘失效。
*   **原因**：灌封材料与内部元件（如陶瓷基板、铜引线框架）的热膨胀系数（CTE）不匹配，在温度变化时产生巨大的热机械应力，最终导致材料疲劳开裂或界面分层。
*   **参数**：热膨胀系数 (CTE)。
*   **解决**：选择CTE与模块内部主要材料相近的灌封胶。对于CTE差异较大的情况，应选择低模量、高韧性的柔性灌封材料（如有机硅）来吸收应力。
*   **预防**：进行有限元热力学仿真，预测应力集中区域，并优化结构设计或材料选择。

**12. 灌封如何对内部元件（如键合线）施加应力？**
*   **症状**：功率循环测试中出现键合线根部断裂或剥离。
*   **原因**：灌封胶在固化收缩和后续的温度变化中，对细小的键合线施加了拉伸或剪切应力。
*   **解决**：选择固化收缩率低、模量低的灌封材料。优化键合线的弧高和形状，使其能更好地承受来自灌封胶的应力。
*   **预防**：在NPI阶段进行严格的功率循环和温度循环测试，并通过解剖分析来检查键合线的健康状况。

## 驱动与隔离电源在灌封设计中要注意什么？

门极驱动电路的性能直接关系到SiC/GaN器件的开关特性，灌封对其影响不容忽视。

**13. 灌封如何影响门极驱动回路的阻抗？**
*   **症状**：门极驱动信号出现过冲、振铃或上升沿变缓。
*   **原因**：灌封材料的介电常数改变了驱动环路的寄生电容和电感，导致其特征阻抗发生变化。
*   **解决**：在PCB设计阶段，使用阻抗控制工具（如HILPCB的在线阻抗计算器）进行精确计算，并预留一定的设计余量。
*   **预防**：将灌封影响纳入驱动回路的协同仿真中，确保在灌封后仍有足够的驱动性能裕量。

**14. 为何需要为门极驱动器设计专用的 isolated power supply for gate driver？**
*   **症状**：高侧驱动器工作异常，或在开关过程中出现共模电流干扰。
*   **原因**：高压侧的驱动器参考地电位随着开关节点剧烈波动，需要一个具有高隔离电压和低寄生电容的电源为其供电。
*   **解决**：使用专为门极驱动设计的隔离DC/DC电源模块。这种电源通常具有高CMTI（共模瞬态抗扰度）、低隔离电容（< 5pF）和强化的绝缘等级。一个可靠的 **isolated power supply for gate driver** 是保证SiC/GaN稳定工作的先决条件。
*   **预防**：在选择隔离电源时，重点关注其隔离电容、CMTI和隔离电压等级，确保其满足应用要求。

**15. 灌封材料与驱动PCB的涂层兼容性如何？**
*   **症状**：灌封胶与PCB阻焊层或三防漆之间附着力差，出现剥离。
*   **原因**：材料化学不兼容。例如，某些有机硅灌封胶可能会被含硫或胺类的三防漆抑制固化。
*   **解决**：进行兼容性测试。将灌封胶涂覆在涂有三防漆的测试板上，按标准流程固化后，进行附着力测试。
*   **预防**：要求PCB供应商和三防漆供应商提供材料成分信息，避免使用已知不兼容的材料组合。

---
<div style="background: linear-gradient(135deg, #E1BEE7 0%, #D1C4E9 100%); color: #311B92; padding: 20px; border-radius: 8px; margin: 30px 0;">
<h3 style="color: #311B92; text-align: center;">Potting for HV Power Modules 关键要点</h3>
<ul style="list-style-type: disc; margin-left: 20px; color: #311B92;">
<li style="margin-bottom: 10px;"><strong>真空灌封是必须：</strong> 消除气泡是保证绝缘性能和避免部分放电的根本。</li>
<li style="margin-bottom: 10px;"><strong>CTE匹配是关键：</strong> 优先选择与内部元件CTE相近或低模量的材料，以管理热机械应力。</li>
<li style="margin-bottom: 10px;"><strong>电气参数影响仿真：</strong> 必须将灌封材料的介电常数纳入寄生参数和EMI仿真。</li>
<li style="margin-bottom: 10px;"><strong>表面处理定成败：</strong> 清洁和预处理直接决定了灌封的粘接可靠性，防止分层。</li>
<li style="margin-bottom: 10px;"><strong>测试验证不可少：</strong> 100%的部分放电和Hipot测试是质量控制的最后防线。</li>
</ul>
</div>
---

## 灌封模块的测试与验证策略是什么？

“没有测量，就没有控制。”严格的测试是确保灌封模块质量的唯一途径。

**16. 生产中如何进行有效的 isolation testing during manufacturing？**
*   **症状**：产品在客户端发生绝缘故障，导致批量召回。
*   **原因**：生产线上的绝缘测试覆盖不全或标准过低。
*   **解决**：实施多阶段测试策略。在灌封前对模块进行初步Hipot测试，灌封固化后再进行100%的Hipot测试和部分放电测试。这套完整的 **isolation testing during manufacturing** 流程能有效筛出潜在缺陷。
*   **预防**：将测试数据与产品序列号绑定，建立可追溯的质量数据库，用于持续的工艺改进。

**17. 除了Hipot测试，为何部分放电测试至关重要？**
*   **症状**：模块通过了Hipot测试，但在长期运行后仍发生绝缘击穿。
*   **原因**：Hipot测试只能检测出已经形成的贯穿性绝缘缺陷，而无法发现微小的、尚未发展的缺陷（如内部气泡）。部分放电（PD）测试通过检测绝缘体内部微小放电产生的脉冲信号，能灵敏地发现这些早期隐患。
*   **解决**：将PD测试作为出厂必检项。设定严格的PDIV（部分放电起始电压）和在额定工作电压下的放电量（pC）标准。
*   **预防**：对PD测试不合格品进行详细的失效分析（FA），找出根本原因（如灌封空洞、界面分层），并反馈到前端工艺进行改进。

**18. 如何通过声学显微镜 (SAM) 检测内部空洞或分层？**
*   **症状**：对PD测试失效的模块进行分析，需要无损检测手段。
*   **原因**：SAM利用超声波在不同介质界面反射的原理，可以清晰地成像出模块内部的空洞、分层、裂纹等缺陷。
*   **解决**：在NPI阶段和批量生产抽检中，使用C-SAM对模块进行扫描，验证灌封工艺的稳定性和一致性。
*   **预防**：建立SAM图像的“黄金标准”，任何偏离标准的图像都应触发工艺审查。

## 表面处理与功率损耗有何关联？

在高频应用中，导体表面的细节会直接影响性能。

**19. PCB的 surface finish impact on power loss 在高频下有多显著？**
*   **症状**：模块的实际工作效率低于设计值，尤其是在高频开关时。
*   **原因**：高频电流存在趋肤效应，主要集中在导体表面。粗糙的表面处理（如HASL）会增加电流路径的长度，从而增大交流电阻和功率损耗。
*   **解决**：对于高频功率模块，推荐使用表面平整的化学镀镍浸金（ENIG）或化学沉银（Immersion Silver）。ENIG提供了良好的可焊性和平整度，对减小高频损耗有明显帮助。理解 **surface finish impact on power loss** 对于优化[重铜PCB](https://hilpcb.com/en/products/heavy-copper-pcb)等功率电子产品的效率至关重要。
*   **预防**：在设计规范中明确指定PCB的表面处理类型和厚度要求。

**20. 灌封前，模块基板的表面处理有何要求？**
*   **症状**：灌封胶与DBC/AMB陶瓷基板的金属化层结合不良。
*   **原因**：基板表面的氧化或污染影响了附着力。
*   **解决**：确保基板在灌封前经过严格的清洁处理，如等离子清洗。对于镀镍层，需要控制其磷含量和氧化程度，以保证最佳的粘接效果。
*   **预防**：与基板供应商和灌封材料供应商三方合作，共同制定和验证表面处理与灌封的工艺窗口。

---
<div style="background-color: #1A237E; color: #FFFFFF; padding: 20px; border-radius: 8px; margin: 30px 0;">
<h3 style="color: #FFFFFF; text-align: center;">HILPCB 高压模块制造能力</h3>
<table style="width:100%; border-collapse: collapse; color: #FFFFFF;">
<tbody>
<tr>
<td style="padding:10px; border: 1px solid #424242; text-align: center;"><strong>最大层数</strong><br>64L</td>
<td style="padding:10px; border: 1px solid #424242; text-align: center;"><strong>最大铜厚</strong><br>20 oz</td>
<td style="padding:10px; border: 1px solid #424242; text-align: center;"><strong>高CTI材料</strong><br>CTI ≥ 600V</td>
</tr>
<tr>
<td style="padding:10px; border: 1px solid #424242; text-align: center;"><strong>绝缘设计</strong><br>增强/加强绝缘</td>
<td style="padding:10px; border: 1px solid #424242; text-align: center;"><strong>组装能力</strong><br>真空回流焊/选择性波峰焊</td>
<td style="padding:10px; border: 1px solid #424242; text-align: center;"><strong>在线测试</strong><br>AOI, X-Ray, ICT, Hipot, PD</td>
</tr>
</tbody>
</table>
<p style="text-align: center; margin-top: 15px;">HILPCB 提供从[高导热PCB](https://hilpcb.com/en/products/high-thermal-pcb)制造到复杂[交钥匙组装](https://hilpcb.com/en/products/turnkey-assembly)的一站式服务，确保您的HV功率模块在设计和制造的每个环节都得到专业支持。</p>
</div>
---

## 关键安规与EMI测试矩阵

一份清晰的测试矩阵是保证产品质量和合规性的蓝图。

<h3 style="color: #000000;">绝缘与安规测试矩阵</h3>
<table style="width:100%; border-collapse: collapse;">
<thead style="background-color: #F5F5F5;">
<tr>
<th style="padding:12px; border: 1px solid #ccc; color: #000000;">测试项</th>
<th style="padding:12px; border: 1px solid #ccc; color: #000000;">测试条件</th>
<th style="padding:12px; border: 1px solid #ccc; color: #000000;">允收标准</th>
<th style="padding:12px; border: 1px solid #ccc; color: #000000;">目的与备注</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">Hipot (耐压测试)</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">2 x U_rated + 1000V (AC, 60s)</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">漏电流 &lt; 5mA, 无击穿或闪络</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">验证绝缘系统的宏观强度。生产100%执行。</td>
</tr>
<tr>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">部分放电 (PD)</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">PDIV &gt; 1.25 x U_rated; 在U_rated下测量</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">PDIV达标, 且在U_rated下放电量 &lt; 10pC</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">检测绝缘系统内部微小缺陷，预测长期可靠性。</td>
</tr>
<tr>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">绝缘电阻</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">500V/1000V DC, 60s</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">&gt; 1 GΩ</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">评估绝缘材料的静态绝缘能力。</td>
</tr>
<tr>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">浪涌 (Surge)</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">1.2/50μs 脉冲, 依据IEC 61000-4-5</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">测试后功能正常, 绝缘性能无下降</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">模拟雷击等瞬态过压，考验模块的鲁棒性。</td>
</tr>
</tbody>
</table>

<h3 style="color: #000000;">EMI 测试矩阵 (参考 CISPR 11/22)</h3>
<table style="width:100%; border-collapse: collapse;">
<thead style="background-color: #F5F5F5;">
<tr>
<th style="padding:12px; border: 1px solid #ccc; color: #000000;">测试项</th>
<th style="padding:12px; border: 1px solid #ccc; color: #000000;">频率范围</th>
<th style="padding:12px; border: 1px solid #ccc; color: #000000;">限值等级</th>
<th style="padding:12px; border: 1px solid #ccc; color: #000000;">目的与备注</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">传导发射 (CE)</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">150kHz - 30MHz</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">Class A / Class B (QP & AV)</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">评估通过电源线传导的噪声。灌封会影响共模路径。</td>
</tr>
<tr>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">辐射发射 (RE)</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">30MHz - 1GHz (或更高)</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">Class A / Class B (QP)</td>
<td style="padding:12px; border: 1px solid #ccc; color: #000000;">评估通过空间辐射的噪声。灌封材料的介电特性有影响。</td>
</tr>
</tbody>
</table>

## SiC/GaN功率模块NPI门控清单 (≥40项)

一份全面的NPI（新产品导入）清单是确保从设计到量产顺利过渡的保障。

<h3 style="color: #000000;">设计与仿真阶段 (DFM/DFR)</h3>
1.  [ ] 灌封材料选型报告（电气、热学、机械性能）
2.  [ ] CTE 匹配性分析与热机械应力仿真
3.  [ ] 电场仿真，验证 **creepage clearance for high voltage**
4.  [ ] 寄生参数提取（考虑灌封材料εr）
5.  [ ] 热仿真，预测结温与热阻
6.  [ ] 灌封工艺流程图（DFM审查）
7.  [ ] 模具设计与注胶口/排气口位置审查
8.  [ ] 表面清洁与预处理方案定义
9.  [ ] 驱动 **isolated power supply for gate driver** 选型与评估
10. [ ] PCB表面处理对高频损耗的影响评估 (**surface finish impact on power loss**)

<h3 style="color: #000000;">物料与供应商认证</h3>
11. [ ] 灌封材料供应商资质审核与批次一致性证明
12. [ ] 陶瓷基板供应商认证与来料检验标准
13. [ ] 关键半导体器件（SiC/GaN）来料检验
14. [ ] 磁性元件（变压器/电感）绝缘等级验证
15. [ ] PCB供应商制造能力审核（如HILPCB）

<h3 style="color: #000000;">工艺验证 (PVT)</h3>
16. [ ] 灌封设备（真空系统、点胶机）能力验证 (Cpk)
17. [ ] 固化炉温度均匀性验证
18. [ ] 表面清洁效果验证（水滴角测试）
19. [ ] 灌封胶混合比例与脱泡效果验证
20. [ ] 首件样品切片分析，检查填充效果
21. [ ] 首件样品SAM扫描，建立“黄金标准”
22. [ ] 附着力测试（划格或拉拔）
23. [ ] 固化后硬度与重量一致性检查
24. [ ] 焊接工艺验证（X-Ray检查空洞率）
25. [ ] 螺栓紧固扭矩与压力均匀性验证

<h3 style="color: #000000;">测试与验证</h3>
26. [ ] 制定完整的 **isolation testing during manufacturing** 计划
27. [ ] Hipot 测试程序验证
28. [ ] 部分放电测试设备校准与测试程序验证
29. [ ] 功能测试（FCT）平台搭建与验证
30. [ ] EMI 预测试与整改方案
31. [ ] 温度循环测试 (-40°C to 125°C, 1000 cycles)
32. [ ] 功率循环测试 (ΔTj > 80°C, >50k cycles)
33. [ ] 高温高湿反偏测试 (H3TRB)
34. [ ] 振动与冲击测试
35. [ ] 可焊性与端子强度测试

<h3 style="color: #000000;">量产准备</h3>
36. [ ] 制定生产控制计划（CP）
37. [ ] 制定标准作业程序（SOP）
38. [ ] 建立产品追溯系统（序列号绑定关键物料与测试数据）
39. [ ] 失效模式与影响分析（FMEA）
40. [ ] 员工培训与上岗认证
41. [ ] 包装、运输与仓储规范定义

## 结论

**Potting for HV power modules** 是一项复杂的系统工程，它横跨材料科学、化学、电气工程、热力学和制造工艺等多个领域。对于追求极致性能和可靠性的SiC/GaN应用而言，任何一个环节的疏忽都可能前功尽弃。通过本文的FAQ、测试矩阵和NPI清单，我们希望为您提供一个清晰、可执行的框架，帮助您驾驭这一挑战。

选择一个经验丰富、技术全面的制造伙伴至关重要。HILPCB不仅能提供符合严苛标准的高性能PCB，更能以一站式组装服务，将您的设计理念转化为可靠的高压功率模块产品。如果您正在为您的下一个高压项目寻找解决方案，请立即联系我们。

<center>获取高压模块PCB/PCBA报价</center>