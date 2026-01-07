---
title: "stackup documentation guide: process-driven playbook для PCB manufacturing и testing"
description: "Используя stackup documentation guide как backbone, этот end-to-end walkthrough покрывает manufacturing детали, quality-control checkpoints и DFM/DFT советы: от материалов и imaging до soldermask, SMT и test validation."
category: technology
date: "2025-11-17"
featured: true
image: ""
readingTime: 8
tags: ["stackup documentation guide", "soldermask exposure tutorial", "smt stencil design tutorial", "pcb fabrication process steps", "yield improvement roadmap", "surface finish selection tips"]
---
Здравствуйте, я преподаватель HILPCB Manufacturing Academy. В ежедневной работе я часто вижу, что многие design engineers воспринимают `stackup documentation guide` как «просто» документ, который задаёт lamination structure и impedance control. Но с точки зрения manufacturing-and-test это «genesis blueprint» и «execution constitution» всего production flow. Он определяет не только electrical performance, но и глубоко влияет на yield, reliability и cost на каждом этапе — от incoming materials до финального functional testing.

Сегодня мы используем этот core документ как нить, чтобы пройти весь PCB manufacturing и test flow. Это не только **pcb manufacturing tutorial**, но и **yield improvement roadmap**, который связывает design intent и manufacturing reality. Мы разложим сложные процессы на SOP-стиль steps и checklists, чтобы ваша команда действительно «встроила в мышление» DFM (Design for Manufacturability) и DFT (Design for Testability).

## Manufacturing flow overview: от Stackup document к физическому продукту

Подробный `stackup documentation guide` — отправная точка fabrication. Он задаёт materials, thickness, copper weight и tolerances — параметры, которые определяют process window на линии производства. Таблица ниже показывает, как ключевые manufacturing steps напрямую маппятся на информацию в Stackup document.

| Process Step | Core Objective | Key Control Parameters | Related Stackup Info |
| :--- | :--- | :--- | :--- |
| **Laminate preparation** | Убедиться, что materials соответствуют design requirements | Material type, board thickness, copper thickness, dimensional accuracy | Core и prepreg (PP) types, Dk/Df, Tg, CAF resistance |
| **Inner-layer imaging** | Точно воспроизвести inner-layer patterns | Exposure energy, develop time, registration (±25 µm) | Inner-layer copper thickness (например, 0.5 oz, 1 oz), minimum line/space |
| **Lamination** | Спрессовать multilayer структуру в одну | Temperature/pressure/time profile, resin-flow control | Stack order, PP type/quantity, overall thickness tolerance (±10%) |
| **Drilling** | Создать through holes и mounting holes | Spindle speed, feed rate, hole-position accuracy (±50 µm) | Hole size, hole type (PTH/NPTH/blind/buried), hole density, minimum annular ring |
| **Plating** | Построить межслойное electrical connection | Rectifier current density, bath chemistry, copper thickness (>20 µm) | Aspect ratio, copper thickness requirements |
| **Outer-layer imaging** | Точно воспроизвести outer-layer patterns | Registration, etch-factor control | Outer-layer copper thickness, impedance-trace width, BGA/QFN pad sizes |
| **Soldermask** | Защитить traces и определить solderable areas | Ink type/thickness, exposure accuracy, curing conditions | Soldermask color, minimum Solder Mask Dam width |
| **Surface finish** | Обеспечить solderability и защиту | Plating thickness (например, ENIG: Au 0.03–0.08 µm), flatness | [Surface Finish](/blog/pcb-surface-finish/) (HASL, ENIG, OSP, etc.) |
| **SMT assembly** | Разместить и припаять components | Paste volume, placement accuracy, reflow profile | BOM, packages, pad design |
| **Test & validation** | Убедиться в electrical function и reliability | Coverage, fault-diagnosis accuracy | Test-point layout, net connectivity |

## Precision control of imaging, etching, and soldermask

Trace width и spacing напрямую связаны с signal integrity и impedance control, и эти параметры жёстко заданы в Stackup document. Manufacturing challenge — точно воспроизвести эти числа на реальной плате.

### Etch process window: превращаем цифры в реальность

Etching — субтрактивный процесс: он удаляет лишний copper и оставляет traces. Но etchant атакует не только вниз, он также etch’ит латерально, создавая undercut. Для компенсации мы применяем “etch compensation” к design data — заранее расширяем traces на phototool.

<div class="div-style-1">

#### Process window: trace etching

- **Target**: добиться ±10% tolerance на design trace width.
- **Input**: copper thickness, заданная stackup (например, 1 oz HTE Copper).
- **Key parameters**:
    - **Etch compensation**: для 1 oz copper обычно нужно 25–35 µm compensation.
    - **Etch rate**: 1.2–1.8 m/min, контролируется chemistry concentration и temperature.
    - **Undercut control**: high-precision spray systems и dedicated etchants удерживают undercut в пределах 12 µm.
- **Inspection method**: 100% AOI, плюс cross-section analysis для критических линий, чтобы измерить line/space.
- **DFM tip**: при [impedance control design](/blog/what-is-impedance-control-in-pcb/) согласуйте с fabricator capability по etch tolerance и оставьте достаточный design margin.

</div>

### soldermask exposure tutorial: это больше, чем “зелёная краска”

Solder mask — “outer layer” PCB, но её роль далеко не только эстетика. Она задаёт solderable areas и предотвращает solder bridging во время assembly. HILPCB использует LDI (Laser Direct Imaging), которое обеспечивает более высокую точность, чем традиционный film exposure.

<div class="div-style-3">

#### Soldermask LDI process steps

1.  **Surface pretreatment**: chemical cleaning + mechanical brushing для увеличения surface roughness и обеспечения ink adhesion.
2.  **Ink coating**: в cleanroom равномерно нанести liquid photoimageable soldermask через automated screen printing или spray. Контролировать thickness: 8–15 µm на pads и 20–30 µm на traces.
3.  **Pre-curing**: короткий bake при 75–85°C, чтобы tack-dry ink перед LDI exposure.
4.  **LDI exposure**: laser сканирует soldermask напрямую (без film); registration может достигать ±15 µm. Критично для формирования soldermask dams между fine-pitch parts (например, 0.4 mm BGA).
5.  **Developing**: промывка в developer; unexposed areas удаляются, открывая pads.
6.  **Final curing**: длительный bake в tunnel oven при ~150°C, чтобы полностью cure soldermask и обеспечить сильные физико-химические свойства.

Это классический **soldermask exposure tutorial**: ключ — контроль energy и accuracy, чтобы soldermask dams не трескались и не “уезжали”.

## Drilling, plating, and PTH quality control

Vias — это “vertical highways” multilayer boards, и их reliability критична. Stackup document задаёт via types (through, blind, buried) и sizes, которые напрямую влияют на выбор drilling и plating.

### Drilling: accuracy и качество hole wall

High aspect-ratio holes (board thickness / hole diameter) сложны и для drilling, и для plating. Например, hole 0.2 mm через board 2.0 mm даёт aspect ratio 10:1.

- **Drilling control**: HILPCB использует high-speed pneumatic spindles (>150k RPM) и X-Ray-assisted registration, чтобы обеспечить точное inner-layer pad alignment. Для microvias (<0.15 mm) применяется laser drilling.
- **Plasma de-smear**: heat от drilling может расплавить resin и создать smear, который закрывает inner-layer copper и ухудшает electrical connection. Plasma De-smear удаляет resin residue со стенок отверстия и обеспечивает надёжную copper adhesion в последующем plating.

### PTH copper: фундамент reliability

Copper thickness и uniformity внутри отверстий во многом определяют, переживёт ли PCB thermal shock (например, при soldering) и long-term operation. Стандарты вроде IPC-6012 обычно требуют average PTH copper thickness ≥ 20 µm.

- **Control method**: мы формируем проводящий base layer Electroless Copper, затем утолщаем PTH и surface copper через Pattern Plating. Plating lines HILPCB используют advanced dynamic current control и high-circulation filtration, чтобы получать плотные и равномерные deposits даже в high-aspect-ratio holes.
- **Inspection**: регулярная cross-section analysis с metallography microscopes измеряет PTH copper thickness и проверяет hole-wall quality на voids, cracks и связанные defects.

## SMT soldering and assembly essentials

После fab bare board процесс переходит в PCBA (Printed Circuit Board Assembly). Pad design, soldermask definition и component placement — всё это задано stackup document — напрямую влияет на успех SMT.

### Stencil design: источник качества solder paste printing

Solder paste printing — первый SMT step и причина более 60% soldering defects. Хороший **smt stencil design tutorial** подчёркивает, что stencil design решает многое.

- **Aperture design**: size/shape apertures определяет paste volume. Мы соблюдаем area ratio (>0.66) и aspect ratio (>1.5), чтобы избежать неполного paste release. Для fine parts (0201 и 0.4 mm BGA) используются electropolished или nano-coated stencils для улучшения release.
- **Thickness selection**: stencil thickness (обычно 100–150 µm) выбирается по самым мелким pitch components на плате — классический пример связи design intent и process constraints.

### Reflow soldering: искусство temperature profiling

Reflow soldering permanently связывает components с PCB. Ключ — точный profile control, чтобы активировать flux, расплавить solder и сформировать надёжный IMC.

<div class="div-style-1">

#### Process window: lead-free reflow temperature profile

- **Target**: яркие, полные solder joints без cold joints, opens, tombstoning и т. п.
- **Input**: solder paste datasheet (например, SAC305), PCB laminate/thickness, maximum component thermal mass.
- **Key parameters**:
    - **Preheat**: 150–180°C, 60–90 s, мягкий ramp чтобы избежать thermal shock.
    - **Soak**: 180–210°C, 60–120 s, активировать flux и выровнять температуру платы.
    - **Reflow**: peak 240–250°C; time above liquidus (217°C) 45–75 s.
    - **Cooldown**: cooling rate < 4°C/s для мелкозернистой структуры и высокой joint strength.
- **Inspection method**: HILPCB использует 3D SPI, 3D AOI и X-Ray inspection для 100% мониторинга качества soldering.

</div>

## Cleaning, conformal coating, and reliability protection

Для high-reliability применений (medical, automotive, aerospace) критичны чистота после solder и защита.

- **Cleaning**: даже “no-clean” flux оставляет residues, которые могут вызвать electrochemical migration (ECM) в humid или high-voltage среде и привести к shorts. HILPCB предлагает aqueous cleaning и использует ion chromatography (IC) для проверки чистоты, обеспечивая ionic residue ниже limits (например, IPC J-STD-001 требует <1.56 µg/cm² NaCl эквивалента).
- **Conformal coating**: после cleaning и drying селективный spray прозрачного conformal coating обеспечивает сильную защиту от humidity, salt fog и mold, значительно увеличивая lifetime в harsh environments.

## Testing matrix: убедиться, что каждый node корректен

DFT должен быть применён end-to-end. Если продукт нельзя адекватно тестировать, качество гарантировать нельзя. Мы используем staged testing matrix, чтобы обеспечить coverage.

| Test Stage | Test Method | Primary Goal | Coverage / defect types |
| :--- | :--- | :--- | :--- |
| **After bare-board fab** | Flying Probe Test (FPT) / Bed of Nails | Validate opens/shorts | 100% net connectivity; etch/drill defects |
| **After SMT** | 3D AOI | Inspect soldering appearance | Wrong/missing parts, polarity, cold joints, bridging, tombstoning |
| **SMT critical parts** | 3D X-Ray | Inspect hidden joints (BGA, QFN) | BGA shorts, voids, Head-in-Pillow (HoP) |
| **PCBA circuit level** | ICT | Check component parameters and nets | Wrong values, opens/shorts, digital logic functions |
| **PCBA functional level** | FCT | Simulate end use and validate functions | Firmware programming, I/O, interfaces, power |
| **System level** | SLT / Burn-in | Validate stability and performance in real conditions | Compatibility issues, intermittent faults, early failures |
| **Reliability validation** | HALT/HASS, temp-humidity cycling, vibration | Evaluate long-term reliability and margin | Weak points, potential failure modes |

Эта **testing matrix** — backbone нашей quality assurance: от микроскопических solder joints до system-level functionality.

## Quality and traceability: сила данных

В современном manufacturing quality не «добавляется инспекцией» — она “built in” и “managed in”.

- **SPC (Statistical Process Control)**: мы ставим SPC monitoring points на ключевых шагах (etching, plating, reflow), чтобы в real time отслеживать process parameters (например, chemistry concentration, oven temperature). Если тренды уходят, система мгновенно предупреждает, чтобы engineers вмешались до того, как дефекты станут системными.
- **MES (Manufacturing Execution System)**: линии HILPCB полностью управляются MES. У каждой PCB/PCBA есть уникальный QR code как “ID card”. От incoming materials (через smart warehousing system) до shipment — все process data, equipment parameters, personnel information и test results привязываются к этому QR code. Это даёт настоящую end-to-end traceability: при обнаружении issues impact локализуется за минуты — будь то конкретный component lot или equipment-parameter anomaly в заданном временном окне.

<div class="cta-box">
    <p>Идеальный Stackup design требует столь же сильного manufacturing и test партнёра, чтобы стать реальностью. MES HILPCB и comprehensive test capability обеспечивают точное исполнение design intent и дают полностью прозрачные traceability data. Хотите увидеть, как ваш следующий проект может выиграть?</p>
    Upload ваши Gerber files сейчас, чтобы получить DFM/DFT evaluation
</div>

## HILPCB’s integrated manufacturing + test capability

Превратить `stackup documentation guide` в high-reliability electronic product требует advanced equipment, строгих процессов и специализированной экспертизы. HILPCB предоставляет больше, чем fabrication — мы даём one-stop solution от design optimization до test validation.

<div class="div-style-6">

#### HILPCB core manufacturing and test capabilities

- **Advanced PCB fabrication**:
    - **Materials**: поддержка high-frequency/high-speed materials вроде Rogers, Taconic и Isola.
    - **Processes**: 20+ layers, 0.15 mm mechanical microvias, laser blind/buried vias, step copper/step slots, backdrilling, gold fingers и другие сложные builds.
    - **Precision control**: LDI exposure, plasma cleaning, X-Ray registration для yield в [HDI](/blog/what-is-hdi-pcb/) builds.

- **Smart PCBA assembly**:
    - **Automated lines**: полностью автоматизированные paste printers, high-speed placement и 12-zone reflow ovens; поддержка 01005 placement.
    - **Closed-loop inspection**: 3D SPI + 3D AOI + 3D X-Ray закрывают data loop и оптимизируют printing/placement parameters в real time.
    - **Smart storage**: temperature/humidity controlled intelligent storage для защиты components, особенно MSD parts.

- **Comprehensive test lab**:
    - **In-house test capability**: ICT/FCT development + flying probe testers, high-resolution X-Ray, environmental chambers (temperature/humidity), vibration tables, salt-spray chambers и т. д.
    - **Reliability services**: полная validation **reliability checklist**, включая thermal shock, mechanical shock, vibration tests и HALT/HASS accelerated life testing.

#

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

`stackup documentation guide` — мост между design и manufacturing. Понимать, как она влияет на каждый downstream step — от etch compensation и reflow profiles до test-point planning — обязательный навык для каждого сильного инженера. В HILPCB мы не только исполняем ваш документ, но и выступаем DFM/DFT партнёром. С process-driven, data-driven и intelligent manufacturing/test системами мы обеспечиваем точную и надёжную реализацию design intent — превращая его в продукты с высокой market competitiveness.

> Need fabrication and assembly support? Свяжитесь с HILPCB [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) или [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) для DFM/DFT recommendations.

