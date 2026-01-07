---
title: "esd handling guide：PCB组装与焊接的第一堂课"
description: "围绕esd handling guide讲解 SMT/THT 流程、物料准备、焊接窗口、检测方法与可制造性技巧，配合表格和步骤，帮助团队快速理解装配基本功。"
category: technology
date: "2025-12-16"
featured: true
image: ""
readingTime: 8
tags: ["esd handling guide", "smt process overview", "through hole soldering basics", "aoi basics", "assembly drawing essentials", "selective solder guideline"]
---
欢迎来到 HILPCB 组装学院。我是你们的导师。

对于许多刚刚完成 PCB 设计的工程师来说，将 Gerber 文件转化为实物电路板的过程往往充满了未知的挑战。你可能精心计算了阻抗，完美布局了高速信号，但如果组装（PCBA）环节失控，所有的设计努力都将付诸东流。

在 HILPCB 的产线上，我们常说：“焊接是技术，但静电防护（ESD）是信仰。”今天这堂课，我们将以 **esd handling guide**（静电防护操作指南）为核心基石，全面拆解从 SMT 贴片到 THT 插件的完整组装流程。无论你是制作原型（Prototype）还是准备小批量试产，掌握这些标准和流程，是确保产品“一次做对”的关键。

## esd handling guide 的装配流程全景

在深入具体的焊接技术之前，我们必须建立一个全景视角。PCB 组装不仅仅是把元件焊上去，它是一个包含环境控制、物料管理、精密加工和严格检测的闭环系统。而贯穿这个闭环的“红线”，就是 ESD 防护。

静电放电（ESD）可以产生高达数千伏的电压，瞬间击穿敏感的 IC 栅极，或者造成更可怕的“潜在失效”——即芯片在出厂时是好的，但在用户使用几周后突然损坏。因此，一份合格的 **esd handling guide** 是所有操作的前提。

<div class="hil-process">
  <h3>HILPCB 标准组装与 ESD 管控流程</h3>
  <ol>
    <li>
      <strong>入厂与静电释放</strong>
      <p>人员穿戴防静电服、手腕带（1MΩ 电阻接地），通过 ESD 门禁测试；物料在 EPA（静电保护区）拆包。</p>
    </li>
    <li>
      <strong>锡膏印刷 (Solder Paste Printing)</strong>
      <p>使用激光切割钢网，将锡膏精准漏印在焊盘上。此阶段需监控环境温湿度，防止锡膏吸潮。</p>
    </li>
    <li>
      <strong>SPI (Solder Paste Inspection)</strong>
      <p>3D 锡膏检测，确保锡膏厚度、体积符合标准，拦截 60% 的潜在焊接缺陷。</p>
    </li>
    <li>
      <strong>SMT 贴片 (Pick & Place)</strong>
      <p>高速贴片机吸取元件。注意：吸嘴与飞达（Feeder）必须具备耗散静电能力，防止摩擦生电。</p>
    </li>
    <li>
      <strong>回流焊接 (Reflow Soldering)</strong>
      <p>通过 10 温区回流炉，完成表面贴装元件的焊接。氮气保护可减少氧化。</p>
    </li>
    <li>
      <strong>AOI 与 X-Ray 检测</strong>
      <p>光学检测外观，X 光透视 BGA 底部焊点。此时需使用防静电周转架移动板卡。</p>
    </li>
    <li>
      <strong>THT 插件与波峰焊</strong>
      <p>处理通孔元件。涉及波峰焊、选择性波峰焊或手工补焊。</p>
    </li>
  </ol>
</div>

## SMT：钢网、贴片、回流的关键设置

表面贴装技术（SMT）是现代电子制造的主力。要理解 **smt process overview**，我们需要关注三个核心要素：钢网设计、贴片精度和回流曲线。

### 1. 钢网（Stencil）的艺术
钢网决定了锡膏的用量。对于细间距（Fine Pitch）元件，如 0.4mm 间距的 BGA 或 0201 阻容，钢网的厚度和开孔方式至关重要。
*   **厚度选择**：通常在 0.1mm 到 0.15mm 之间。过厚会导致连锡（短路），过薄会导致少锡（虚焊）。
*   **电抛光与纳米涂层**：HILPCB 建议对高密度板使用电抛光钢网，壁面光滑，利于脱模。

### 2. 贴片机与 ESD 风险
在高速贴片过程中，吸嘴与元件的高频接触极易产生静电。
*   **esd handling guide 要点**：贴片机的吸嘴必须使用导电或静电耗散材料。所有 Feeder（供料器）必须良好接地。如果你的 BOM 中包含高灵敏度的射频芯片或 MOSFET，请务必在 [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) 需求中备注特殊的 ESD 等级要求。

### 3. 回流焊曲线（Reflow Profile）
回流焊不是简单的加热。它分为四个阶段，每个阶段都有严格的时间和温度窗口：
*   **预热区（Preheat）**：升温斜率控制在 1-3°C/sec，激活助焊剂，去除挥发物。
*   **恒温区（Soak）**：让 PCB 整体温度均匀，防止“立碑”效应。
*   **回流区（Reflow）**：温度达到峰值（无铅工艺通常为 245°C 左右），焊锡熔化润湿。
*   **冷却区（Cooling）**：快速冷却以细化晶粒，增强焊点强度。

## THT/混装：波峰、选择焊与手焊协同

尽管 SMT 占据主导，但连接器、大电容和功率器件仍需通孔插装（THT）。**through hole soldering basics** 的核心在于热量的传递。

### 波峰焊（Wave Soldering）
适用于大批量、纯 THT 或底面已点红胶的混装板。
*   **治具（Pallet）**：对于双面混装板，我们需要制作合成石治具，遮蔽底部的 SMT 元件，只露出 THT 焊盘过波峰。

### 选择性波峰焊（Selective Soldering）
这是 **selective solder guideline** 中推崇的高端工艺。它像一个自动化的“机器手”，喷射微型锡波，逐个焊接焊点。
*   **优势**：无需专用治具，热冲击小，适合高密度双面混装板。
*   **应用**：当通孔元件周围 3mm 内有 SMT 器件时，传统波峰焊无法操作，选择焊是最佳方案。

### 手工焊接与 ESD
在样品阶段或特殊器件处理时，手工焊接不可避免。
*   **esd handling guide 警示**：
    *   必须使用恒温且接地良好的焊台。
    *   操作员必须佩戴有线防静电手环（无线手环在工业级 ESD 防护中通常被视为无效）。
    *   烙铁头应定期测量对地电阻（<2Ω）和漏电压（<2mV）。

## 物料与文档准备：BOM、坐标、装配图、面向制造

优秀的输入决定优秀的输出。为了让 HILPCB 的自动化产线高效运转，你需要准备标准化的工程资料。

### 1. BOM (Bill of Materials)
BOM 是组装的圣经。
*   **关键字段**：位号（Designator）、数量、MPN（制造商零件编号）、描述、封装。
*   **工具推荐**：使用 HILPCB 的 [BOM Viewer](https://hilpcb.com/en/tools/bom-viewer) 检查物料的可采购性和生命周期。

### 2. 坐标文件 (Centroid/Pick & Place File)
机器需要知道每个元件的 X、Y 坐标和旋转角度。请确保坐标原点与 PCB Gerber 中的原点一致。

### 3. 装配图 (Assembly Drawing)
这是 **assembly drawing essentials** 的核心。Gerber 中的丝印层有时会被过孔切断或被元件覆盖。一份清晰的 PDF 装配图应包含：
*   极性元件（二极管、电解电容、IC）的清晰方向标记。
*   特殊组装要求（如：底部填充 Underfill、散热器安装、三防漆涂覆区域）。

<div class="hil-point">
  <h3>DFM 检查清单</h3>
  <p>在提交文件前，请自查：</p>
  <ul>
    <li><strong>器件间距：</strong>0201 元件之间是否保留了至少 0.15mm 的间距？</li>
    <li><strong>传送边：</strong>PCB 是否留有 3-5mm 的无元件工艺边（Break-away rails）？</li>
    <li><strong>Mark 点：</strong>板角和细间距 IC 附近是否有光学定位点？</li>
  </ul>
</div>

## 检测与质量：SPI/AOI/X-Ray/功能测试如何配合

质量不是检测出来的，是制造出来的，但检测是防止不良品流出的最后防线。了解 **aoi basics** 和其他检测手段，能帮你制定合理的测试策略。

| 检测方式 | 适用阶段 | 主要检测缺陷 | 局限性 |
| :--- | :--- | :--- | :--- |
| **SPI (锡膏检测)** | 印刷后 | 少锡、多锡、拉尖、偏移 | 无法检测元件贴装错误 |
| **AOI (自动光学检测)** | 炉前/炉后 | 缺件、错件、极性反、立碑、侧立 | 无法检测 BGA 底部、被遮挡的焊点 |
| **X-Ray** | 炉后 | BGA/QFN 短路、空洞、虚焊 | 检测速度较慢，成本较高 |
| **FCT (功能测试)** | 组装后 | 电压异常、通信失败、逻辑错误 | 需要定制治具和测试程序 |

对于高可靠性产品，HILPCB 建议采用 **SPI + 炉后 AOI + 关键器件 X-Ray** 的组合策略。

## 常见缺陷与整改：立碑、桥连、空洞、焊盘脱落

即使有完美的 **esd handling guide** 和流程，缺陷仍可能发生。学会分析缺陷是工程师进阶的必修课。

### 1. 立碑 (Tombstoning)
元件一端翘起，像墓碑一样。
*   **原因**：焊盘两端热容量不平衡（一端接大铜箔，一端接细线），导致锡膏熔化时间不同步，拉力不均。
*   **对策**：设计时使用热风焊盘（Thermal Relief），保证两端散热对称。

### 2. 桥连 (Bridging)
相邻引脚之间短路。
*   **原因**：钢网开孔过大、锡膏塌陷、贴片压力过大。
*   **对策**：缩小钢网开孔（如内缩 10%），检查刮刀压力。

### 3. 气泡/空洞 (Voiding)
X-Ray 下看到焊点内部有空腔。
*   **原因**：助焊剂挥发排气不畅，或回流区时间不足。
*   **对策**：优化回流曲线，增加恒温区时间；选用低空洞率锡膏。

### 4. ESD 损伤 (ESD Damage)
这是最隐蔽的缺陷。
*   **现象**：功能测试通过，但数周后失效。
*   **对策**：严格执行全程 ESD 防护。在 HILPCB，我们使用实时静电监控系统，确保每一块 [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb) 都在安全电压下生产。

## 与 HILPCB 协同：DFM/工单/试产复盘

从设计图纸到完美交付，需要设计端与制造端的紧密协同。HILPCB 不仅仅是代工厂，更是你的工程合作伙伴。

<div class="hil-capability">
  <h3>HILPCB 的组装能力矩阵</h3>
  <ul>
    <li><strong>全自动化产线：</strong>配备 Yamaha 高速贴片机与 10 温区氮气回流炉，支持 01005 封装及 0.3mm Pitch BGA。</li>
    <li><strong>智能 MES 系统：</strong>物料追溯精确到每一个 Reel，生产过程全透明。</li>
    <li><strong>灵活交付：</strong>支持 <a href="https://hilpcb.com/en/products/prototype-assembly">Prototype Assembly</a>（快至 24 小时）与 <a href="https://hilpcb.com/en/products/box-build-assembly">Box Build Assembly</a>（整机组装）。</li>
    <li><strong>严格的 ESD 管控：</strong>全厂区 ANSI/ESD S20.20 标准认证，离子风机全覆盖。</li>
  </ul>
</div>

### 试产复盘的重要性
在第一次试产（NPI）结束后，不要急着量产。HILPCB 的工程师会为你提供一份 DFM 反馈报告，指出哪些焊盘设计导致了良率下降，哪些元件布局影响了自动焊接。利用这些数据优化你的下一个版本，是降低成本、提升质量的最快路径。

PCB 组装是一门融合了物理、化学、材料学与管理学的综合艺术。从严格遵守 **esd handling guide** 开始，到精通 SMT/THT 的每一个工艺细节，你正在一步步将设计蓝图转化为改变世界的硬件产品。

准备好开始你的下一次组装任务了吗？

<!-- COMPONENT: BlogQuickQuoteInline -->