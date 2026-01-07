---
title: "cleaning after soldering"
description: "好的，HILPCB 组装学院导师，我们开始为新工程师准备这堂关于“cleaning after soldering”的入门教程。"
category: "pcb"
date: "2025-12-02"
featured: false
image: ""
readingTime: 3
tags: ["cleaning after soldering", "bom cleanup tutorial", "ipc class 2 vs class 3 assembly", "aoi basics", "smt process overview", "panelization for assembly"]
---好的，HILPCB 组装学院导师，我们开始为新工程师准备这堂关于“cleaning after soldering”的入门教程。

---
title: "cleaning after soldering：PCB组装与焊接的第一堂课"
description: "围绕cleaning after soldering讲解 SMT/THT 流程、物料准备、焊接窗口、检测方法与可制造性技巧，配合表格和步骤，帮助团队快速理解装配基本功。"
category: technology
date: "2025-12-02"
featured: true
image: ""
readingTime: 8
tags: ["cleaning after soldering", "bom cleanup tutorial", "ipc class 2 vs class 3 assembly", "aoi basics", "smt process overview", "panelization for assembly"]
---

大家好，欢迎来到 HILPCB 组装学院。我是你们的导师，今天我们将开启 PCB 组装与焊接的第一堂课。许多新工程师认为，“cleaning after soldering”（焊接后清洗）只是 PCBA 流程的最后一个简单步骤，但实际上，它是一面镜子，反映了从设计、物料准备到焊接工艺控制的每一个环节的质量。

一个完美的焊接过程，配合恰当的助焊剂，可能只需要极简的清洗；而一个充满隐患的流程，则会让清洗变得异常困难，甚至无法挽回。因此，我们将围绕“cleaning after soldering”这个最终结果，反向追溯整个 SMT (表面贴装技术) 和 THT (通孔插装技术) 的核心要点。这堂课不仅教你如何“擦干净”，更教你如何从源头实现“无需费力去擦”的高质量装配。

让我们从全局视角开始，一步步拆解 PCBA 的每一个关键节点。

## 1. “cleaning after soldering”的装配流程全景

要理解清洗的重要性，首先必须了解它在整个 PCBA（Printed Circuit Board Assembly）生产流程中的位置。它不是一个孤立的工序，而是承上启下的关键一环。一个典型的混合组装（SMT+THT）流程如下：

<div class="type-3">
    <div class="list-box">
        <div class="list-item">
            <div class="list-item-title">Step 1: DFM & 物料准备</div>
            <p>接收客户的BOM、Gerber、坐标文件，进行可制造性设计（DFM）分析，同步进行元器件采购与IQC（来料质量控制）。</p>
        </div>
        <div class="list-item">
            <div class="list-item-title">Step 2: SMT 表面贴装</div>
            <p>锡膏印刷 → SPI（锡膏检测）→ 高速贴片 → 回流焊接 → AOI（自动光学检测）。这是组装的核心环节。</p>
        </div>
        <div class="list-item">
            <div class="list-item-title">Step 3: THT 通孔插装</div>
            <p>插件（手动/自动）→ 波峰焊或选择性焊接 → 剪脚 → 补焊。</p>
        </div>
        <div class="list-item">
            <div class="list-item-title">Step 4: 清洗与检测</div>
            <p><b>Cleaning After Soldering</b>：使用特定溶剂和设备清除焊接后残留的助焊剂、锡珠等污染物。随后进行 X-Ray 检测（针对BGA等）、ICT（在线测试）和 FCT（功能测试）。</p>
        </div>
        <div class="list-item">
            <div class="list-item-title">Step 5: 后续工序</div>
            <p>三防漆涂覆（Conformal Coating）、程序烧录、整机组装（Box Build）与最终检验（FQC）。</p>
        </div>
    </div>
</div>

从流程中可以看出，清洗发生在所有焊接工序之后、关键功能测试和防护涂覆之前。为什么这一步至关重要？

*   **可靠性**：残留的助焊剂（特别是活性较高的）在潮湿环境下可能呈酸性，腐蚀焊盘和元器件引脚，长期导致电气失效。
*   **电气性能**：离子残留物会降低板卡的表面绝缘电阻，在高频或高压电路中引发信号串扰或漏电，影响产品性能。
*   **三防漆附着力**：洁净的板面是三防漆（防潮、防盐雾、防霉菌）能够均匀、牢固附着的前提。残留物会导致涂层下产生气泡、分层或剥落。
*   **外观与检测**：干净的板面便于进行 AOI 复判和外观检查，避免污染物被误判为焊接缺陷。

因此，我们的目标不仅是完成清洗，更是通过优化前端流程，让清洗变得更简单、更高效，甚至在某些应用中采用“免清洗（No-Clean）”工艺，从根本上提升质量与效率。

## 2. SMT：钢网、贴片、回流的关键设置

SMT 是 PCBA 的心脏，超过80%的焊接缺陷都源于此。每一个环节的参数设置都直接影响最终焊点的质量和残留物的形态，从而决定了清洗的难度。

#### 钢网与锡膏印刷
这是焊接的起点。锡膏的量、形貌和位置决定了焊接的基础。
*   **钢网厚度与开孔**：钢网厚度（通常为0.1-0.15mm）和开孔尺寸（通常为焊盘的90%-100%）共同决定了锡膏的印刷量。过多的锡膏会导致桥连、锡珠，增加清洗负担；过少则可能导致虚焊或少锡。
*   **锡膏选择**：锡膏由焊锡粉和助焊剂组成。助焊剂的类型至关重要。
    *   **免洗型（No-Clean）**：残留物少且无腐蚀性，理论上可不清洗。但对于高可靠性要求的[高TG PCB](https://hilpcb.com/en/products/high-tg-pcb)或高频板，残留物仍可能影响信号完整性，建议清洗。
    *   **水洗型（Water-Soluble）**：活性高，焊接效果好，但残留物有强腐蚀性，**必须**用纯水彻底清洗干净。
    *   **松香型（Rosin）**：传统类型，根据活性分为R/RMA/RA，通常需要使用特定溶剂清洗。

#### 贴片精度
贴片机将元器件精确地放置在印刷了锡膏的焊盘上。位置偏移（X, Y, θ）会导致焊接缺陷，如立碑、偏移等，这些缺陷在返修时会产生额外的助焊剂残留，增加清洗的复杂性。

#### 回流焊接曲线
这是 SMT 的灵魂。回流焊炉内的温度曲线必须与锡膏规格、PCB 尺寸及厚度、元器件密度和热容精确匹配。一条典型的回流焊曲线包括四个温区：
1.  **预热区 (Preheat)**：缓慢升温，让 PCB 和元器件均匀受热，并让助焊剂中的溶剂挥发。
2.  **恒温区 (Soak)**：激活助焊剂，使其充分润湿焊盘和元器件引脚，去除氧化层。
3.  **回流区 (Reflow)**：温度超过焊锡熔点（如SAC305为217°C），锡膏熔化形成金属间化合物（IMC），完成焊接。峰值温度和时间是关键。
4.  **冷却区 (Cooling)**：快速降温，形成精细、牢固的焊点晶格结构。

<div class="type-1">
    <h4>回流焊曲线对清洗的影响</h4>
    <ul>
        <li><b>预热不足</b>：溶剂未充分挥发，回流时可能产生“锡珠飞溅”，散落在板面各处，难以清洗。</li>
        <li><b>峰值温度过高/时间过长</b>：助焊剂被“烤焦”，残留物碳化变硬，附着力极强，常规清洗方法难以去除。</li>
        <li><b>冷却过慢</b>：可能导致焊点粗糙，也影响残留物的最终形态。</li>
    </ul>
</div>

在 HILPCB，我们的 MES 系统会实时监控每块板的回流焊曲线，确保工艺窗口的稳定，从源头控制助焊剂残留物的状态，为后续的清洗打下良好基础。

## 3. THT/混装：波峰、选择焊与手焊协同

对于包含通孔元器件的[混合技术组装](https://hilpcb.com/en/products/smt-assembly)，焊接方式更为多样，对清洗的挑战也更大。

#### 波峰焊 (Wave Soldering)
将插好件的 PCB 以一定角度和速度通过熔融的锡波，完成焊接。
*   **挑战**：整个板的B面都会接触到助焊剂和高温焊锡，残留物覆盖面积大，且通孔内的残留物难以清除。
*   **对策**：
    *   **治具（Pallet）保护**：使用定制的耐高温治具，遮蔽已贴装的 SMT 元器件和无需焊接的区域，减少污染。
    *   **喷雾式助焊剂**：精确控制助焊剂的喷涂区域和用量，避免过量使用。
    *   **预热充分**：确保助焊剂在接触锡波前活性达到最佳，溶剂充分挥发。

#### 选择性焊接 (Selective Soldering)
使用微型锡缸和喷嘴，对指定的通孔焊点进行逐点或拖动焊接。
*   **优势**：精度高，热影响区小，几乎不污染周边区域。助焊剂也是局部涂覆，残留物极少。对于高密度、热敏元件多的[多层PCB](https://hilpcb.com/en/products/multilayer-pcb)来说，这是理想选择。
*   **清洗**：由于污染源集中，清洗变得非常简单，有时局部擦拭即可。

#### 手工焊接 (Manual Soldering)
用于补焊、返修或安装特殊元器件。
*   **挑战**：操作员的技能和习惯直接影响质量。烙铁温度过高、焊接时间过长、使用劣质助焊剂都会产生难以清洗的顽固残留。
*   **规范**：HILPCB 对手工焊接岗位有严格的 IPC 认证要求，统一使用高品质的免洗焊锡丝和助焊剂，并规定了标准作业程序（SOP），确保手工焊接点的一致性和洁净度。

## 4. 物料与文档准备：BOM、坐标、装配图、面向制造

“Garbage In, Garbage Out.” 生产的顺畅与否，始于设计和文档准备阶段。一份清晰、准确、完整的制造文件包是高质量组装的基石。

<div class="type-1">
    <h4>PCBA 制造文件包核心三要素</h4>
    <ul>
        <li><b>BOM (Bill of Materials)</b>: 清晰的物料清单，包含准确的制造商零件编号（MPN）、封装、位号和描述。一份混乱的BOM是延期和错误的开始。您可以使用 HILPCB 的 BOM Viewer 工具进行预检查。</li>
        <li><b>Centroid File (坐标文件)</b>: 也叫 Pick-and-Place 文件，提供每个元器件中心点的 X/Y 坐标和旋转角度，是贴片机编程的直接依据。</li>
        <li><b>Assembly Drawing (装配图)</b>: 提供元器件的极性（如二极管、电解电容）、方向（如连接器、IC的第一引脚）和特殊组装要求的可视化指导。</li>
    </ul>
</div>

在 HILPCB，我们强调 **DFMA (Design for Manufacturing and Assembly)**。在正式投产前，我们的工程师会审核您的文件，提出优化建议：
*   **Panelization (拼板)**：如何设计拼板的工艺边、V-cut、邮票孔，以确保生产效率和焊接过程中的结构稳定性。
*   **元件间距**：确保元件之间有足够的空间，便于贴装、焊接、检测和返修，也利于清洗溶剂的流动和干燥。
*   **焊盘设计**：遵循 IPC 标准，优化焊盘尺寸和形状，防止立碑、桥连等缺陷。

通过前期的 DFM 沟通，我们可以避免 90% 以上在生产中可能遇到的问题，确保焊接过程顺畅，从而让“cleaning after soldering”变得简单可控。

## 5. 检测与质量：SPI/AOI/X-Ray/功能测试如何配合

质量是生产出来的，不是检测出来的。但先进的检测设备是验证和监控生产过程的眼睛。它们协同工作，确保每个环节都符合标准。

| 检测设备 | 检测阶段 | 主要目的 | 对“清洗”的意义 |
| :--- | :--- | :--- | :--- |
| **SPI (Solder Paste Inspection)** | 锡膏印刷后 | 检测锡膏的高度、体积、面积、偏移，确保焊接源头正确。 | 从根源上避免因锡膏过多导致的锡珠，减少清洗对象。 |
| **AOI (Automated Optical Inspection)** | 回流焊/波峰焊后 | 检查错件、漏件、极性反、偏移、桥连、虚焊等表面缺陷。 | 及时发现焊接缺陷，避免带着缺陷进入清洗环节，减少返修带来的二次污染。 |
| **X-Ray Inspection** | 焊接后 | 检查不可见焊点，如 BGA、QFN 的气泡、桥连、枕头效应。 | 确保高密度器件的焊接质量，避免因内部缺陷返修而破坏已清洗的板面。 |
| **ICT/FCT (In-Circuit/Functional Test)** | 清洗后 | 测试电路的电气连接和板卡的实际功能是否符合设计要求。 | 残留物可能导致测试探针接触不良，影响测试结果。彻底的清洗是精准测试的前提。 |

这个检测闭环确保了问题在最早的阶段被发现和纠正。例如，SPI 发现锡膏印刷不良，我们会立即调整印刷参数并清洗错误的板，而不是等到回流焊后产生大量次品再去返修和深度清洗。

## 6. 常见缺陷与整改：立碑、桥连、空洞、焊盘脱落

了解常见缺陷及其成因，能帮助我们更好地理解工艺控制的重要性，以及它们如何增加清洗的复杂性。

| 焊接缺陷 | 主要原因 | 预防与整改措施 |
| :--- | :--- | :--- |
| **立碑 (Tombstoning)** | 芯片元件两端焊盘受热不均；焊盘设计不对称；贴片偏移。 | 优化PCB焊盘设计；调整回流焊预热区温度，确保均匀受热；校准贴片机精度。 |
| **桥连 (Bridging)** | 锡膏印刷过多；引脚间距过小；回流焊升温过快。 | 优化钢网开孔，减少锡膏量；调整回流焊曲线，减缓升温速率；进行DFM检查，确保引脚间距符合工艺能力。 |
| **空洞 (Voiding)** | 锡膏中溶剂或助焊剂在回流过程中未能完全排出；焊盘或元器件引脚受污染。 | 选用高质量锡膏；优化回流焊曲线，给予足够的时间让气体排出；确保来料（PCB和元器件）清洁。 |
| **焊盘脱落 (Pad Lifting)** | PCB质量问题；手工返修时烙铁温度过高或施力过大。 | 采购高质量的[FR-4 PCB](https://hilpcb.com/en/products/fr4-pcb)；对返修人员进行严格培训，控制温度和操作技巧。 |

每一种缺陷的返修，都意味着要局部使用助焊膏、烙铁和吸锡线，这会引入新的、更难处理的污染物。因此，最好的策略是通过严格的工艺控制和 DFM 来预防缺陷的发生。

## 7. 与 HILPCB 协同：DFM/工单/试产复盘

将一个设计原型转化为可靠的量产产品，需要设计工程师与组装厂的紧密协作。HILPCB 不仅是您的制造商，更是您的制造顾问。

<div class="type-6">
    <div class="title">HILPCB 一站式 PCBA 组装能力</div>
    <div class="pro-list">
        <div class="pro-item">
            <img src="https://placehold.co/64x64/4CAF50/FFFFFF?text=DFM" alt="DFM Analysis">
            <div class="pro-text">
                <h4>免费 DFM/DFA 分析</h4>
                <p>在您下单前，我们的工程师团队会提供专业的可制造性与可组装性分析报告，从源头规避风险。</p>
            </div>
        </div>
        <div class="pro-item">
            <img src="https://placehold.co/64x64/2196F3/FFFFFF?text=MES" alt="MES System">
            <div class="pro-text">
                <h4>全流程 MES 追溯</h4>
                <p>从物料入库到成品出货，每个环节都有条码管理，实现生产过程的全程可追溯，确保 IPC Class 2 或 Class 3 标准的达成。</p>
            </div>
        </div>
        <div class="pro-item">
            <img src="https://placehold.co/64x64/FF9800/FFFFFF?text=Clean" alt="Advanced Cleaning">
            <div class="pro-text">
                <h4>先进的清洗工艺</h4>
                <p>我们配备了在线式水洗机和超声波清洗设备，可根据您的产品要求（如医疗、汽车、航空）提供符合标准的清洗服务。</p>
            </div>
        </div>
        <div class="pro-item">
            <img src="https://placehold.co/64x64/E91E63/FFFFFF?text=Proto" alt="Prototype Assembly">
            <div class="pro-text">
                <h4>快速原型与小批量</h4>
                <p>我们专注于<a href="https://hilpcb.com/en/products/prototype-assembly">快速原型和小批量组装</a>，提供灵活、高效的服务，帮助您加速产品迭代与上市。</p>
            </div>
        </div>
    </div>
</div>

我们的合作流程非常简单：您通过我们的在线平台提交Gerber、BOM等文件，系统会自动进行初步分析。随后，我们的工程师会与您进行一对一的 DFM 沟通，确认所有工艺细节后，您即可在线下单。在试产阶段，我们会提供详细的试产报告（First Article Inspection Report），与您共同复盘，为批量生产扫清障碍。

“Cleaning after soldering”这堂课的核心，是建立一种系统性的质量思维。它始于设计，贯穿于物料、工艺和检测的每一个细节。当每一个环节都做到精确可控时，最终的清洗工作便水到渠成，产品的长期可靠性也得到了根本保障。

准备好将您的设计变为现实了吗？让我们从一份专业的 DFM 报告开始。

<!-- COMPONENT: BlogQuickQuoteInline -->