---
title: "temperature cycling basics：PCB测试与检验的基础步骤"
description: "围绕temperature cycling basics讲解飞针、ICT、功能、AOI/SPI 以及可靠性测试的目标、流程与判据，附测试矩阵与资料准备要点。"
category: technology
date: "2025-12-16"
featured: true
image: ""
readingTime: 8
tags: ["temperature cycling basics", "inspection criteria pcb", "dft checklist beginner", "visual inspection checklist", "warp flatness check", "bed of nails tutorial"]
---
各位新同事，欢迎来到 HILPCB 测试实验室（Test Lab）。

在你们正式接触昂贵的测试设备之前，我希望大家先建立一个核心观念：**PCB 制造不是结束，而是验证的开始。** 一块外观完美的电路板，如果无法在极寒的北欧户外工作，或者在赤道的高温下死机，那么它就是电子垃圾。

今天这堂课，我们将围绕 **temperature cycling basics（温度循环基础）** 这一核心概念，向外延伸至电气测试、光学检验以及更广泛的可靠性测试。作为新人，你们需要掌握“为什么测”、“如何测”以及“怎么判”。

<div class="alert alert-info">
  <strong>核心要点：</strong> 测试不仅仅是为了发现坏板，更是为了验证设计余量（Design Margin）。Temperature cycling basics 的本质是利用物理热胀冷缩原理，提前诱发潜在的早期失效（Infant Mortality）。
</div>

## temperature cycling basics 要回答哪些质量问题？

在深入具体的测试操作前，我们必须理解物理层面的挑战。PCB 是由铜、玻璃纤维（FR4）、阻焊油墨、锡膏和各种元器件组成的复合体。

这里有一个关键术语：**CTE（热膨胀系数，Coefficient of Thermal Expansion）**。

当温度变化时，不同材料的膨胀或收缩速率是不同的。例如，FR4 基材的膨胀率通常比铜大，而陶瓷元器件的膨胀率又极低。
*   **问题所在：** 当环境温度剧烈波动时，PCB 内部会产生巨大的机械应力。这种应力会拉扯导通孔（Via）的铜壁，或者剪切元器件的焊点。
*   **测试目标：** Temperature cycling basics 就是通过模拟这种反复的“热-冷-热”过程，来回答以下问题：
    1.  **孔壁完整性：** 镀铜层是否会断裂？（特别是 [High Tg PCB](https://hilpcb.com/en/products/high-tg-pcb) 在高温下的表现）。
    2.  **焊点可靠性：** BGA 锡球是否会因为应力疲劳而开裂？
    3.  **分层风险：** 多层板的层间结合力是否足够？

理解了这一点，你就明白了为什么我们在实验室里要如此关注温度变化对电路板的影响。

## 飞针与 ICT：何时使用、如何准备测试点？

在进行破坏性的可靠性测试之前，我们首先要确保板子在电气上是导通的，且没有短路。这就是电气测试（E-Test）的领域。

### 飞针测试 (Flying Probe)
对于打样或小批量订单（如 [Prototype Assembly](https://hilpcb.com/en/products/prototype-assembly)），我们通常使用飞针测试。
*   **原理：** 几根探针像“飞”一样在板子上快速移动，逐个测量网络。
*   **优点：** 不需要制作夹具，启动成本低。
*   **缺点：** 速度慢，不适合大批量。

### ICT 测试 (In-Circuit Test) & Bed of Nails Tutorial
当产量上来后，飞针就太慢了。这时我们需要用到“针床”（Bed of Nails）。
*   **原理：** 制作一个布满探针的夹具，一次性压下，所有探针同时接触 PCB 上的测试点。
*   **Bed of Nails Tutorial 核心：**
    1.  **对准：** 夹具必须精准对位，否则探针会扎坏元器件或扎在阻焊上。
    2.  **压力：** 针床下压需要巨大的机械力，必须进行 **warp flatness check（翘曲度检查）**，防止板子被压断。
    3.  **DFT Checklist Beginner（初学者可测性设计清单）：**
        *   是否每个网络都有至少一个测试点（Test Point）？
        *   测试点直径是否 > 0.8mm（推荐值）？
        *   测试点之间是否保持了安全间距（通常 > 2.54mm 以降低夹具成本）？

<div class="alert alert-success">
  <strong>流程指引：</strong>
  <ol>
    <li><strong>CAM 数据处理：</strong> 提取网表（Netlist）。</li>
    <li><strong>DFT 审查：</strong> 检查测试点覆盖率。</li>
    <li><strong>选择方案：</strong> 样品选飞针，量产选 ICT。</li>
    <li><strong>执行测试：</strong> 记录开路（Open）和短路（Short）数据。</li>
  </ol>
</div>

## 功能/上电测试：脚本、夹具与判据

ICT 只能告诉你“线路通了，电阻值对不对”，但它不能告诉你“产品能不能跑起来”。这就需要功能测试（FCT）。

对于复杂的板子，比如 [High Speed PCB](https://hilpcb.com/en/products/high-speed-pcb) 或带有 MCU 的控制板，我们需要烧录固件并模拟实际工作场景。

*   **测试夹具：** 通常是定制的，带有电源接口、通讯接口（USB/UART/CAN）和模拟负载。
*   **测试脚本：** 自动化软件会发送指令并读取反馈。例如：“发送指令 A，期望收到数据 B”。
*   **判据：**
    *   **电压/电流：** 静态电流是否在规格书范围内？（过大通常意味着芯片损坏或微短路）。
    *   **通讯握手：** 芯片是否能正确响应 ID 读取指令？
    *   **LED/蜂鸣器：** 人机交互部件是否工作正常？

## AOI/SPI/X-Ray：光学检测如何发现缺陷？

电气测试能发现“死板”，但有些缺陷是“隐性”的，或者仅仅是外观不达标。这时我们需要光学检测。

### SPI (Solder Paste Inspection)
在 [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) 产线的最前端，SPI 检查锡膏印刷的体积、高度和面积。
*   **重点：** 锡膏印少了会导致虚焊，印多了会导致连锡短路。

### AOI (Automated Optical Inspection)
贴片回流焊之后，AOI 机器通过摄像头扫描板子。
*   **Visual Inspection Checklist (AOI 重点):**
    *   **缺件 (Missing):** 元器件飞了。
    *   **极性 (Polarity):** 二极管或电容贴反了。
    *   **立碑 (Tombstoning):** 元器件一端翘起。
    *   **偏移 (Shift):** 元器件没对准焊盘。

### X-Ray 检测
对于 BGA、QFN 等引脚藏在本体下面的元器件，光靠看是看不到的。X-Ray 可以穿透封装看到内部焊点。
*   **判据：** 气泡率（Voiding）通常要求小于 25%（IPC 标准）。

## 可靠性入门：热循环、湿热、振动、跌落

这是本堂课的重头戏，也是 **temperature cycling basics** 发挥作用的地方。可靠性测试通常是破坏性的或压力性的，用于验证产品的寿命。

### 1. 温度循环 (Temperature Cycling)
这是最基础也是最重要的环境应力筛选（ESS）。
*   **设置：** 将 PCB 放入高低温试验箱。
*   **参数示例：** -40°C (保持 30分钟) <-> +125°C (保持 30分钟)，循环 500 次。
*   **斜率 (Ramp Rate)：** 温度变化的快慢。普通的 Cycling 较慢（如 5-10°C/min），而热冲击（Thermal Shock）则是瞬间切换（< 10秒）。
*   **失效模式：** 这里的失效通常表现为 [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb) 的导通孔断裂，或者不同材质结合处的微裂纹。

### 2. 湿热测试 (Temperature Humidity Bias - THB)
*   **目的：** 检查 PCB 的绝缘性能和抗迁移能力（CAF）。
*   **典型条件：** 85°C / 85% RH（双 85 测试）。
*   **关注点：** 潮气侵入会导致绝缘电阻下降，甚至发生电化学迁移导致短路。

### 3. 机械应力：振动与跌落
*   **振动：** 模拟运输或车载环境。重点检查重型元器件（如电感、大电容）是否会震脱。
*   **跌落：** 模拟手持设备掉落。重点检查 [Rigid-Flex PCB](https://hilpcb.com/en/products/rigid-flex-pcb) 的连接处是否断裂。

### 测试矩阵与判据对照表

为了让大家更直观地理解，我整理了一份 HILPCB 实验室常用的测试矩阵：

| 测试项目 | 核心关键词 | 典型标准 (IPC/JEDEC) | 目的 | 关键判据 (Inspection Criteria PCB) |
| :--- | :--- | :--- | :--- | :--- |
| **温度循环** | Temperature Cycling Basics | IPC-TM-650 2.6.7 | 验证 CTE 匹配度与焊点疲劳寿命 | 阻值变化 < 10%；无裂纹；无分层 |
| **热冲击** | Thermal Shock | IPC-TM-650 2.6.7.2 | 模拟极端温差突变 | 孔壁镀层无断裂；盲埋孔无分离 |
| **翘曲度检查** | Warp Flatness Check | IPC-TM-650 2.4.22 | 确保 SMT 贴装平整度 | 弓曲/扭曲度 < 0.75% (SMT) |
| **可焊性** | Solderability | J-STD-003 | 验证焊盘表面处理活性 | 润湿面积 > 95% |
| **切片分析** | Microsection | IPC-TM-650 2.1.1 | 内部结构微观检查 | 镀铜厚度达标；层间对位准确 |

## 测试报告与追溯：记录哪些数据？

在 HILPCB，我们常说：“没有记录的测试等于没测。”

一份合格的测试报告必须包含可追溯性（Traceability）。当客户拿着一块失效的板子回来时，我们需要能查到它出生时的所有数据。

### 必须记录的数据点：
1.  **环境条件：** 测试时的室温、湿度。
2.  **设备参数：** 比如 temperature cycling 的升温速率、驻留时间。
3.  **失效位置：** 如果是 ICT 报错，具体是哪个 Net（网络）？哪个 Pin（引脚）？
4.  **图像证据：** AOI/X-Ray 的截图，显微镜下的切片图。

### 缺陷分级 (Defect Classification)
在填写 **inspection criteria pcb** 报告时，我们要将缺陷分级：
*   **致命缺陷 (Critical):** 导致产品无法使用或有安全隐患（如短路、起火风险）。
*   **主要缺陷 (Major):** 性能下降，可能导致寿命缩短（如锡少、轻微空洞）。
*   **次要缺陷 (Minor):** 外观瑕疵，不影响功能（如丝印模糊、轻微划痕）。

## HILPCB 测试实验室能提供什么？

作为新人，你们很幸运能加入 HILPCB。我们的实验室不仅服务于内部生产，也对外提供独立的第三方检测服务。

<div class="row">
  <div class="col-md-6">
    <h3>硬件能力</h3>
    <ul>
      <li><strong>高精度飞针测试机：</strong> 适应细间距 HDI 板。</li>
      <li><strong>环境应力筛选仓：</strong> 覆盖 -70°C 至 +150°C 的宽温域。</li>
      <li><strong>3D X-Ray & CT 扫描：</strong> 无损透视多层板内部结构。</li>
      <li><strong>阻抗测试仪：</strong> 专为 <a href="https://hilpcb.com/en/tools/impedance-calculator">Impedance Control</a> 验证服务。</li>
    </ul>
  </div>
  <div class="col-md-6">
    <h3>软件与服务</h3>
    <ul>
      <li><strong>DFM/DFT 咨询：</strong> 在设计阶段介入，优化可测试性。</li>
      <li><strong>失效分析 (FA)：</strong> 提供切片、SEM（扫描电镜）分析报告。</li>
      <li><strong>定制化治具开发：</strong> 为特殊异形板设计 ICT/FCT 夹具。</li>
    </ul>
  </div>
</div>

无论客户需要的是简单的 [Single/Double Layer PCB](https://hilpcb.com/en/products/single-double-layer-pcb) 还是复杂的 [IC Substrate PCB](https://hilpcb.com/en/products/ic-substrate-pcb)，我们都有一套完整的测试流程来守门。

<!-- COMPONENT: BlogQuickQuoteInline -->

## 结语

掌握 **temperature cycling basics** 只是你们在 HILPCB 实验室的第一步。从飞针的灵动到 ICT 的高效，从 AOI 的火眼金睛到环境仓的残酷考验，每一个环节都是为了确保交付到客户手中的每一块 PCB 都能经得起时间的考验。

接下来，请大家领取各自的 **DFT checklist beginner** 手册，我们将移步到设备区进行实操演示。记住，测试不仅是检验，更是对品质的承诺。