---
title: "112G SerDes routing stackup: как справиться со стабильностью ultra-high-speed линков и low-loss вызовами для high-speed SI PCB"
description: "Подробный разбор 112G SerDes routing stackup: Channel Budget, выбор low-loss материалов, impedance и crosstalk control, via/connector transitions, equalization/jitter и DFM trade-offs для high-speed SI PCB."
category: technology
date: "2025-11-17"
featured: true
image: ""
readingTime: 8
tags: ["112G SerDes routing stackup", "112G SerDes routing reliability", "112G SerDes routing low volume", "low-loss 112G SerDes routing", "112G SerDes routing guide", "112G SerDes routing quick turn"]
---
На фоне взрывного роста потребности в bandwidth со стороны data centers, AI и 5G communications данные скорости вошли в эру 112Gbps/s. В этом контексте 112G SerDes стал core enabler для next-generation high-speed interconnect. Но на таких скоростях PCB design и manufacturing сталкиваются с беспрецедентными сложностями. Грамотно спроектированный **112G SerDes routing stackup** — это уже не «просто lamination», а systems engineering на стыке materials science, электромагнитной теории и precision fabrication. Он напрямую определяет signal integrity, стабильность линка и, в конечном счёте, успех продукта.

Эта статья — подробный **112G SerDes routing guide** с точки зрения design connector и via-transition. Мы пройдём весь путь: от Channel Budget и выбора материалов до manufacturability, чтобы помочь вам уверенно работать в этом сложном домене. Для команд, которые делают cutting-edge [high-speed PCB](https://hilpcb.com/en/products/high-speed-pcb), оптимизированный **112G SerDes routing stackup** — обязательная база. Highleap PCB Factory (HILPCB) опирается на глубокий high-speed опыт и поддерживает клиентов от prototype до volume.

### Почему 112G SerDes Channel Budget такой жёсткий?

В 112G SerDes всё начинается с Channel Budget. Channel Budget задаёт максимально допустимые signal loss и noise margin на физическом линке от transmitter (Tx) к receiver (Rx). По сравнению с предыдущими поколениями (28G/56G) бюджет 112G крайне мал — главным образом из‑за PAM4 signaling.

PAM4 передаёт 2 bits per symbol, вдвое снижая baud rate и снимая часть bandwidth pressure, но при этом уменьшает SNR примерно на ~9.5dB и резко повышает чувствительность к noise и attenuation. Nyquist frequency для 112G PAM4 достигает 28 GHz. На этих частотах PCB traces, vias и connectors вносят существенный Insertion Loss (IL).

Типовой 112G channel включает несколько частей — каждая «съедает» драгоценный loss budget:
*   **ASIC package:** Substrate traces и vias в BGA package — первые contributors потерь.
*   **PCB traces:** основной источник loss — dielectric loss, conductor loss (skin effect и copper roughness) и длина трасс.
*   **Vias:** Through/blind/buried vias — крупные impedance discontinuities, добавляющие reflection и дополнительный loss, особенно на больших [backplane PCB](https://hilpcb.com/en/products/backplane-pcb).
*   **Connectors:** High-speed connectors (QSFP-DD, OSFP) нужно точно моделировать, включая PCB launch region.
*   **Cable assembly (опционально):** для rack-to-rack interconnect cable и его connectors тоже входят в channel.

Total channel insertion loss обычно ограничивают ~30–35dB (@28GHz). Избыточный loss в одном элементе может сорвать link bring-up или вывести BER из спецификации. Поэтому точное channel modeling и корректная budget allocation — первый и самый критичный шаг в **112G SerDes routing stackup** design.

### Как выбрать правильные low-loss материалы?

Выбор материалов — фундамент **low-loss 112G SerDes routing**. На 28GHz потери обычного FR-4 неприемлемы, поэтому нужны low-loss/ultra-low-loss laminates, рассчитанные на high-speed. Ключевые метрики — Dk и Df.

*   **Dk:** влияет на propagation speed и characteristic impedance. В high-speed design нужен стабильный Dk по частоте, чтобы уменьшить dispersion. Более низкий Dk также позволяет делать трассы шире, снижая conductor loss.
*   **Df:** напрямую характеризует dielectric loss. Для 112G SerDes Df на 28GHz должен быть ниже 0.004 — часто ближе к 0.002.

Помимо Dk/Df, два фактора важны не меньше:

1.  **Fiber Weave Effect:** периодичность fiberglass weave создаёт локальную неоднородность Dk. Когда длина трассы сопоставима с weave pitch, variation импеданса и skew ухудшают differential signaling. Типовые меры:
    *   Использовать более «плоские» glass styles (например, 1078, 1067).
    *   Использовать Mechanically Spread Glass.
    *   Route с небольшим углом (например, 1–5°) относительно weave, чтобы избежать параллельного выравнивания.

2.  **Copper Roughness:** на высоких частотах skin effect заставляет ток течь по поверхности проводника. Шероховатый copper увеличивает эффективную длину пути и повышает conductor loss. Используйте очень smooth copper, например VLP или ULP; типичный Rq должен быть ниже 2 µm.

<div style="background-color:#F5F7FA; padding: 20px; border-radius: 8px; margin: 30px 0;">
<h3 style="text-align:center; color:#000000;">Сравнение характеристик материалов для high-speed PCB</h3>
<table style="width:100%; border-collapse: collapse; text-align:center;">
<thead style="background-color:#E0E0E0;">
<tr>
<th style="padding:12px; border:1px solid #ccc; color:#000000;">Класс материала</th>
<th style="padding:12px; border:1px solid #ccc; color:#000000;">Типичный Dk (@10GHz)</th>
<th style="padding:12px; border:1px solid #ccc; color:#000000;">Типичный Df (@10GHz)</th>
<th style="padding:12px; border:1px solid #ccc; color:#000000;">Target data rate</th>
<th style="padding:12px; border:1px solid #ccc; color:#000000;">Индекс стоимости</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">Standard FR-4</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">4.2 - 4.8</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">0.015 - 0.020</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">< 5 Gbps</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">1x</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">Mid-loss materials</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">3.6 - 4.0</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">0.008 - 0.012</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">10 - 28 Gbps</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">2x - 3x</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">Low-loss (e.g., Megtron 6)</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">3.2 - 3.6</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">0.002 - 0.004</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">28 - 112 Gbps</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">5x - 8x</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">Ultra-low-loss (e.g., Tachyon 100G)</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">< 3.0</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">< 0.002</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">112 Gbps and above</td>
<td style="padding:12px; border:1px solid #ccc; color:#000000;">> 10x</td>
</tr>
</tbody>
</table>
</div>

### Ключевые стратегии для impedance control и crosstalk management

В **112G SerDes routing stackup** точная impedance control и жёсткое подавление crosstalk — два дополнительных столпа качества сигнала.

**Impedance control:**
Differential impedance обычно 100Ω или 90Ω, с допуском вплоть до ±7% и даже ±5%. Любое отклонение геометрии от target impedance вызывает reflections, увеличивая insertion loss и jitter. Ключевые факторы:
*   **Trace width and thickness:** Etch accuracy в manufacturing определяет итоговую linewidth.
*   **Dielectric thickness:** Критичен контроль толщины PP (Prepreg) после lamination.
*   **Material Dk:** Для simulation нужно использовать Dk от laminate supplier с учётом resin content и lamination conditions.

**Crosstalk management:**
Crosstalk — это noise из-за EM coupling между соседними трассами. В 112G PAM4 системах, где SNR уже низкая, crosstalk часто является killer #1. Типовые стратегии:
*   **Увеличить spacing:** Spacing между differential pairs часто рекомендуют 3W и более; на критичных линках может потребоваться 5W или больше.
*   **Reference-plane continuity:** Обеспечить непрерывные reference GND/power planes под high-speed routing; не пересекать plane splits.
*   **Ортогональное routing между соседними signal layers:** Направления трассировки должны быть перпендикулярны, чтобы уменьшить broadside coupling.
*   **Ground-via shielding:** Стратегически расставлять Stitching Vias вокруг differential pairs, создавая эффект Faraday-cage и изоляцию шума.

Эффективный crosstalk control должен начинаться на этапе stackup planning, с использованием 3D full-wave EM simulators (например, Ansys HFSS, CST) для точного предсказания и оптимизации.

### Насколько важна оптимизация transitions для connectors и vias?

Как специалист по design transitions connector/via, могу уверенно сказать: на 112G качество transitions напрямую задаёт верхний предел channel performance. Неоптимизированная via или connector pad легко «съедают» несколько dB бюджета за счёт via loss и reflection.

**Via optimization:**
Via — сложная 3D структура. Паразитные capacitance и inductance создают сильные impedance discontinuities на 28GHz. Ключевые подходы:
*   **Back-drilling:** Одна из самых важных техник. Удаляя unused via stub со стороны backside, вы устраняете quarter-wavelength resonances и заметно улучшаете insertion loss и reflection. Контроль глубины backdrill — важный индикатор производственных возможностей фабрики.
*   **Anti-pad optimization:** Увеличение anti-pad opening в reference planes снижает паразитную capacitance и приближает импеданс к transmission line.
*   **Remove NFP:** Удаление Non-Functional Pads на внутренних слоях уменьшает паразитную capacitance и улучшает performance.
*   **Использовать [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) technology:** Microvias и меньшие pads резко сокращают физические размеры via и паразитные эффекты.
*   **Ground-via co-design:** Разместить 1–2 «кольца» ground vias вокруг signal via для low-inductance return path и подавления coupling.

**Connector optimization (Launch Tuning):**
Pin arrays у high-speed connectors (например, QSFP-DD) очень плотные, поэтому pad и fan-out design сложны. Необходима 3D simulation для fine-tune pad shapes, trace widths и reference-plane openings, чтобы match connector impedance и получить smooth transition.

<div style="background: #ffffff; border: 1px solid #e0e7ff; border-radius: 24px; padding: 40px 30px; margin: 30px 0; font-family: 'Segoe UI', system-ui, sans-serif; box-shadow: 0 15px 45px rgba(49, 27, 146, 0.1);">
<h3 style="text-align: center; color: #311b92; margin: 0 0 10px 0; font-size: 1.85em; font-weight: 800; letter-spacing: 0.5px;">🧬 Via transitions: матрица оптимизации для high-speed вертикальных линков</h3>
<p style="text-align: center; color: #673ab7; font-size: 1.05em; margin-bottom: 40px; font-weight: 500;">Убрать impedance jumps и parasitics, чтобы защитить 112G+ signal integrity</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 18px;">
<div style="background: #f8f7ff; border: 1px solid #ede7f6; border-radius: 18px; padding: 25px; border-left: 6px solid #673ab7; display: flex; flex-direction: column;">
<strong style="color: #311b92; font-size: 1.15em; margin-bottom: 15px;">01. Mandatory Backdrill и stub removal</strong>
<p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Execution standard:</strong> Полностью удалять via stubs, чтобы устранить резонансные точки на высокой частоте. Для data rate выше 28Gbps строго держать stub length в пределах <strong>< 10 mil</strong>, чтобы сохранить линейность bandwidth.</p>
</div>
<div style="background: #f8f7ff; border: 1px solid #ede7f6; border-radius: 18px; padding: 25px; border-left: 6px solid #673ab7; display: flex; flex-direction: column;">
<strong style="color: #311b92; font-size: 1.15em; margin-bottom: 15px;">02. Remove Non-functional Pads</strong>
<p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Execution standard:</strong> Удалять лишние inner-layer pads на слоях. Снижение parasitic capacitance улучшает TDR поведение и уменьшает reflection в via transition.</p>
</div>
<div style="background: #fdfbff; border: 1px solid #f3e5f5; border-radius: 18px; padding: 25px; border-left: 6px solid #9575cd; display: flex; flex-direction: column;">
<strong style="color: #4527a0; font-size: 1.15em; margin-bottom: 15px;">03. Точный Anti-pad design</strong>
<p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Execution standard:</strong> Использовать 3D full-wave solver для оптимизации размеров Anti-pad. Fine-tune via-to-plane spacing, чтобы компенсировать локальную индуктивность и обеспечить <strong>impedance continuity</strong> в вертикальном переходе.</p>
</div>
<div style="background: #fdfbff; border: 1px solid #f3e5f5; border-radius: 18px; padding: 25px; border-left: 6px solid #9575cd; display: flex; flex-direction: column;">
<strong style="color: #4527a0; font-size: 1.15em; margin-bottom: 15px;">04. Coaxial-like ground-via enclosure</strong>
<p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Execution standard:</strong> Размещать <strong>GND Stitching Vias</strong> симметрично вокруг signal vias, формируя coaxial-like return path, изолируя via crosstalk и уменьшая return-loop inductance.</p>
</div>
</div>
<div style="margin-top: 30px; padding: 25px; background: #f1f5f9; border-radius: 16px; border-left: 8px solid #334155;">
<strong style="color: #1e293b; font-size: 1.1em; display: block; margin-bottom: 8px;">🚀 Connector Launch Tuning:</strong>
<p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0;">Fine-tune fanout region под конкретный connector (например, QSFP-DD или PCIE 6.0). Подбирая pad edges и lamination gaps к reference plane, обеспечить smooth transition impedance от горизонтальной трассировки к вертикальному connector и минимизировать <strong>Total Insertion Loss</strong>.</p>
</div>
<div style="margin-top: 20px; padding: 20px; background: linear-gradient(90deg, #311b92, #673ab7); border-radius: 12px; color: #ffffff; text-align: center; font-size: 0.92em;">
💡 <strong>HILPCB manufacturing note:</strong> Backdrill depth tolerance напрямую влияет на поведение 112G link. Мы используем advanced laser depth-control system, чтобы держать <strong>Backdrill Tolerance в пределах ±2 mil</strong>, существенно снижая reflection loss на высокой частоте.
</div>
</div>

### Как equalization и jitter влияют на SerDes link performance?

Даже при оптимизированном **112G SerDes routing stackup** channel loss остаётся. Современные SerDes имеют мощные Equalization circuits для компенсации. Типовые блоки:
*   **Tx FFE:** Pre-emphasis усиливает high-frequency компоненты, компенсируя low-pass поведение channel.
*   **Rx CTLE:** Программируемый amplifier, который выборочно усиливает high-frequency, выравнивая channel response.
*   **Rx DFE:** Нелинейный equalizer, который компенсирует ISI от предыдущих символов.

Задача PCB — дать «smooth и предсказуемый» channel. Response с резонансами и резкими discontinuities делает equalizers трудными для конвергенции — или приводит к отказу.

Jitter — time-domain deviation и ещё один сильный враг high-speed links. Источники jitter со стороны PCB:
*   **Fiber weave effects в материале.**
*   **Reflections от impedance discontinuities.**
*   **Power Supply Noise:** PDN noise через SerDes power pins попадает в сигнал и создаёт jitter — подчёркивая важность co-design SI и PI.

Robust stackup снижает jitter и ISI на physical layer, уменьшает зависимость от SerDes equalization и повышает общую **112G SerDes routing reliability**.

### Как DFM балансирует performance и cost?

Теоретически идеальный **112G SerDes routing stackup** бессмысленен, если его нельзя изготовить экономично и надёжно. DFM нужно учитывать рано. Инженеры HILPCB рекомендуют early involvement, чтобы избежать manufacturability traps.

Ключевые DFM моменты:
*   **Line width/spacing control:** 112G часто требует 3/3mil (~75/75μm) или тоньше, что повышает требования к imaging и etching.
*   **Drilling accuracy:** Высокий layer count и высокий Aspect Ratio требуют очень высокой alignment accuracy в mechanical и laser drilling.
*   **Backdrill depth control:** Backdrill depth tolerance напрямую влияет на stub length и требует advanced Z-axis control equipment.
*   **Stackup symmetry:** Для снижения lamination warpage держите stackup максимально симметричным.
*   **Surface finish:** На 28GHz ENEPIG часто лучше ENIG благодаря flatness, corrosion resistance и поведению в условиях skin effect.

На early этапах—особенно когда нужен **112G SerDes routing quick turn**—тесная работа с advanced manufacturer и DFM review помогает избежать поздних дорогих redesign и ускоряет time to market.

<div style="background-color:#1A237E; color: #FFFFFF; padding: 20px; border-radius: 8px; margin: 30px 0;">
<h3 style="text-align:center; color:#FFFFFF;">Обзор high-speed PCB manufacturing capability HILPCB</h3>
<table style="width:100%; border-collapse: collapse; text-align:center;">
<thead style="background-color:#3F51B5;">
<tr>
<th style="padding:12px; border:1px solid #757575; color:#FFFFFF;">Process parameter</th>
<th style="padding:12px; border:1px solid #757575; color:#FFFFFF;">Capability</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">Max layer count</td>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">64 layers</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">Min line width/spacing</td>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">2.5 / 2.5 mil</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">Max Aspect Ratio</td>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">20:1</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">Backdrill depth tolerance</td>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">+/- 2 mil (50μm)</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">Impedance control tolerance</td>
<td style="padding:12px; border:1px solid #757575; color:#FFFFFF;">±5%</td>
</tr>
</tbody>
</table>
</div>

### Как обеспечить long-term reliability для 112G SerDes routing?

**112G SerDes routing reliability** — это не только попадание в electrical targets, но и стабильная работа на протяжении product life. Ключевые моменты:

*   **Thermal management:** 112G SerDes devices и optical modules рассеивают заметную мощность; stackup должен обеспечивать эффективные heat paths. Добавление thermal reference planes, материалы с лучшей теплопроводностью и грамотное размещение thermal vias помогают контролировать температуру и предотвращают performance drop или повреждения.
*   **Power Integrity (PI):** Low-impedance и стабильный PDN — основа. Правильный decoupling placement, широкие power planes и low-inductance via design подавляют supply noise и дают SerDes «clean power».
*   **CAF resistance:** В high-density PCBs с высоким электрическим градиентом CAF — потенциальный failure mode. Нужны high-CAF-resistance материалы и оптимизированные процессы drilling/plating.
*   **Consistency testing:** Для volume production выстроить строгие тесты — выборочно проверять characteristic impedance через TDR и измерять S-parameters на VNA для обеспечения lot-to-lot consistency.

### Как HILPCB поддерживает low-volume и quick-turn prototypes?

Мы понимаем, что быстрые итерации и prototype validation критичны для cutting-edge 112G SerDes. Многие проекты стартуют с потребностей **112G SerDes routing low volume**. HILPCB построила гибкую производственную систему, которая поддерживает путь от нескольких prototypes до full-scale volume.

Для проектов **112G SerDes routing quick turn** мы предлагаем:
*   **Expert DFM support:** бесплатные stackup recommendations и DFM analysis до заказа, чтобы сбалансировать performance и manufacturability.
*   **Strong material inventory:** склад mainstream **low-loss 112G SerDes routing** laminates (Isola, Rogers, Panasonic Megtron series и т. д.), чтобы избежать длинного procurement lead time.
*   **Dedicated prototype line:** rapid-turn линия для быстрого выпуска high-quality high-speed PCB.
*   **One-stop service:** кроме PCB fabrication, мы поддерживаем component sourcing и PCBA. Наша [turnkey assembly](https://hilpcb.com/en/products/turnkey-assembly) может управлять supply chain, чтобы вы фокусировались на R&amp;D.

Нужны ли вам validation boards **112G SerDes routing low volume** или сложные volume orders — у HILPCB есть capability и опыт, чтобы быть надёжным партнёром.

#

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

Создание robust и надёжного **112G SerDes routing stackup** — сложное systems engineering, требующее тонких trade-offs между SI, PI, thermal management и manufacturing. От строгого Channel Budget analysis и тщательно подобранных low-loss материалов до micron-level оптимизации vias и connector transitions — каждый нюанс важен.

По мере движения технологий к 224G и дальше эти принципы и вызовы будут только усиливаться. Выбор партнёра вроде HILPCB, который понимает и физику design, и top-tier manufacturing, может стать решающим преимуществом. Мы не только производитель, но и партнёр в технических инновациях, превращающий самые сложные design blueprints в high-performing физические продукты. Если вы запускаете новую high-speed программу и вам нужна надёжная **112G SerDes routing stackup** solution, свяжитесь с нашими техническими экспертами.

