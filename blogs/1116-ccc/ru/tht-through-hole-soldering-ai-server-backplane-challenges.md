---
title: "THT/through-hole soldering: как управлять высокоскоростными interconnect вызовами AI server backplane PCBs"
description: "Подробно о THT/through-hole soldering: SI, thermal management и power/interconnect design — чтобы создавать высокопроизводительные AI server backplane PCBs."
category: technology
date: "2025-11-16"
featured: true
image: ""
readingTime: 8
tags: ["THT/through-hole soldering", "AI server motherboard PCB mass production", "AI server motherboard PCB reliability", "AI server motherboard PCB stackup", "AI server motherboard PCB routing", "AI server motherboard PCB quick turn"]
---
При экспоненциальном росте потребности в AI и ML вычислениях hardware AI серверов сталкивается с беспрецедентными задачами. Как ключевой узел, соединяющий compute, storage и network подсистемы, backplane PCB напрямую определяет performance и стабильность системы. Хотя SMT является mainstream, для connector, которые несут high current, выдерживают множество циклов вставки и жесткие механические нагрузки, **THT/through-hole soldering** не устарел — он остается незаменимым благодаря высокой reliability.

Однако на скоростях PCIe 5.0/6.0 и выше традиционный THT становится существенным SI bottleneck. Управлять вызовами THT/through-hole soldering и балансировать mechanical strength, PI и high-speed SI — задача для AI hardware engineers и PCB manufacturers. Это требует не только сильного процесса, но и end-to-end оптимизации: материалы, stackup и сама технология soldering. HILPCB предоставляет advanced manufacturing и assembly сервисы, соответствующие требованиям next-gen AI серверов.

### Почему THT/through-hole soldering по-прежнему незаменим в AI server backplane

SMT силен по плотности и автоматизации, но в backplane сценариях THT дает физические преимущества, которые SMT не обеспечивает, поэтому THT — предпочтительная установка критических connector.

1.  **Максимальная механическая прочность и долговечность:** connector на backplane (например, Orthogonal Midplane Connectors, OCP NIC 3.0) крупные, с множеством pins и испытывают нагрузки от частых вставок. Pins THT проходят через PCB и полностью обволакиваются припоем, формируя соединение значительно прочнее SMT. Это критично для **AI server motherboard PCB reliability** и снижает отказы от вибраций и ударов.

2.  **Отличная способность переносить большие токи:** accelerator cards (GPU, TPU) легко превышают 1000W и требуют сотен ампер через backplane. Pins THT и PTH barrels имеют значительно больший поперечник, чем SMT pads, несут ток с меньшим сопротивлением и меньшим нагревом. Это стабилизирует PDN, снижает IR Drop и обеспечивает чистое питание.

3.  **Упрощенные тепловые пути:** pins THT также являются теплопроводящими каналами, отводя тепло в внутренние PWR/GND слои, где большие медные площади работают как heat spreader.

Поэтому в AI серверных системах, ориентированных на экстремальную performance, THT/through-hole soldering — это не “legacy”, а стратегический выбор для high-reliability и high-power interconnect.

### High-speed SI: SI вызовы THT vias и оптимизация

В эпоху 56/112 Gbps PAM4 сам via THT connector становится основной SI проблемой. Неоптимизированные vias сильно ухудшают сигнал.

*   **Via stub effect:** в multilayer PCB сигнал идет лишь между некоторыми слоями, а неиспользуемая часть via образует stub, который резонирует, вызывает отражения и Insertion Loss и может “закрыть” глаз.
*   **Impedance discontinuity:** barrel-геометрия via вызывает скачок импеданса, увеличивает Return Loss и вводит Jitter.
*   **Via-to-via Crosstalk:** в плотных полях connector соседние THT vias электромагнитно связаны, что вызывает crosstalk, особенно опасный для differential pairs.

Для решения нужны точное **AI server motherboard PCB routing** и производственная стратегия. Ключевая техника — **Back-drilling/Controlled Depth Drilling**, удаляющая лишний stub с противоположной стороны и минимизирующая резонанс. Успешный процесс обычно удерживает остаточный stub в пределах 10mil (~254μm), что требует высокой точности глубины. Anti-pad optimization, настройка reference planes и ground-via shielding также помогают улучшить matching и снизить crosstalk.

<div style="background-color:#F5F7FA; padding: 20px; border-radius: 8px; margin: 20px 0;">
<h3 style="text-align:center; color:#000000;">Сравнение SI до/после оптимизации THT via (simulation @ 28 GHz)</h3>
<table style="width:100%; border-collapse:collapse; color:#000000;">
<thead style="background-color:#E0E0E0;">
<tr>
<th style="padding:12px; border:1px solid #ccc; text-align:left;">Показатель</th>
<th style="padding:12px; border:1px solid #ccc; text-align:left;">Standard THT via (unoptimized)</th>
<th style="padding:12px; border:1px solid #ccc; text-align:left;">Optimized THT via (with back-drill)</th>
<th style="padding:12px; border:1px solid #ccc; text-align:left;">Улучшение</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:12px; border:1px solid #ccc;">Insertion Loss</td>
<td style="padding:12px; border:1px solid #ccc;">-4.5 dB (severe attenuation)</td>
<td style="padding:12px; border:1px solid #ccc;">-1.2 dB (significantly improved)</td>
<td style="padding:12px; border:1px solid #ccc; background-color:#E8F5E9;">Improved 73%</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #ccc;">Return Loss</td>
<td style="padding:12px; border:1px solid #ccc;">< -10 dB (strong reflection)</td>
<td style="padding:12px; border:1px solid #ccc;">< -18 dB (good match)</td>
<td style="padding:12px; border:1px solid #ccc; background-color:#E8F5E9;">Reflection reduced > 8 dB</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #ccc;">Stub resonance point</td>
<td style="padding:12px; border:1px solid #ccc;">~15 GHz (limits bandwidth)</td>
<td style="padding:12px; border:1px solid #ccc;">> 40 GHz (moved out of band)</td>
<td style="padding:12px; border:1px solid #ccc; background-color:#E8F5E9;">Resonance shifted > 160%</td>
</tr>
</tbody>
</table>
</div>

### Как stackup backplane влияет на THT performance

Грамотный **AI server motherboard PCB stackup** — основа высокопроизводительного THT/through-hole soldering. Stackup задает электрические свойства и напрямую влияет на manufacturability и cost.

Выбор материалов критичен: для high-speed backplane обычно используют Ultra-Low Loss материалы (Megtron 6/7, Tachyon 100G) с низкими Dk/Df. Плоские copper foils (HVLP) и Spread Glass помогают минимизировать Fiber Weave Effect и обеспечить более равномерный импеданс differential pairs.

Также важны layer count и толщина: backplane часто имеют 20–40 слоев и толщину >6mm. Это усложняет THT, особенно из-за Aspect Ratio. Высокий aspect ratio (18:1+) требует очень равномерного plating; тонкие участки могут привести к opens или проблемам reliability.

Наконец, необходима непрерывность reference planes для чистого return path. В зоне connector каждый signal via должен иметь рядом сплошной GND/PWR reference plane. Splits/voids разрывают возврат, повышают EMI и crosstalk. HILPCB может помочь, опираясь на опыт [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb).

### Power integrity (PI): high current вызовы THT connector

Backplane должны стабильно питать сотни и тысячи cores. THT connector — ключевые элементы, и PI напрямую влияет на стабильность.

Главный вызов — огромный ток и IR Drop. Например, GPU connector может переносить >500A на 12V или 48V. Даже при низком сопротивлении pins падение на трассах/vias/pins становится значительным. Слишком большой drop вызывает undervoltage, throttling или crash.

Решения:
*   **Heavy copper / ultra-heavy copper:** использовать 3oz+ медь на PWR/GND, снижая сопротивление planes. HILPCB выполняет [Heavy Copper PCB](https://hilpcb.com/en/products/heavy-copper-pcb).
*   **Оптимизация power path:** широкие и короткие трассы, больше THT pins/vias в параллель, чтобы уменьшить сопротивление.
*   **Точное decoupling размещение:** достаточный decoupling рядом с power connector для transient current и подавления noise.

Robust PDN — фундамент yield и долгосрочной стабильности **AI server motherboard PCB mass production**.

<div style="background:linear-gradient(135deg, #E1BEE7, #CE93D8); color:#311B92; padding: 20px; border-radius: 8px; margin: 20px 0;">
<h3 style="text-align:center; color:#311B92;">Key points for THT power integrity design</h3>
<ul style="list-style-type: none; padding-left: 0;">
<li style="margin-bottom: 10px; display: flex; align-items: center;"><span style="font-size: 20px; margin-right: 10px;">✅</span> <strong>Minimize loop inductance:</strong> держать PWR/GND pins рядом и сокращать return path.</li>
<li style="margin-bottom: 10px; display: flex; align-items: center;"><span style="font-size: 20px; margin-right: 10px;">✅</span> <strong>Control IR Drop:</strong> считать IR Drop через PI simulation и оптимизировать heavy copper или дополнительными planes.</li>
<li style="margin-bottom: 10px; display: flex; align-items: center;"><span style="font-size: 20px; margin-right: 10px;">✅</span> <strong>Strategic decoupling:</strong> многоуровневая сеть между connector и load (например, VRM).</li>
<li style="margin-bottom: 10px; display: flex; align-items: center;"><span style="font-size: 20px; margin-right: 10px;">✅</span> <strong>Electro-thermal co-design:</strong> учитывать Joule heating и не допускать ухудшения **AI server motherboard PCB reliability**.</li>
</ul>
</div>

### Thermal management и reliability стратегия для THT soldering

Soldering — финальный и самый критичный шаг. Для толстых backplane с высокой thermal mass традиционный Wave Soldering сложен: PCB забирает много тепла, а в зоне пайки температура недостаточна, что приводит к cold joints и дефектам.

Поэтому современные процессы чаще используют:
*   **Selective Soldering:** мини-nozzle локально греет/паяет только область THT, точно контролируя тепло и избегая thermal shock для SMT; идеально для SMT+THT.
*   **Pin-in-Paste / Intrusive Reflow:** печать пасты в отверстия, установка pins и reflow всей платы. Паста заполняет barrel и формирует надежный joint. SMT-совместимо, упрощает процесс и удобно для **AI server motherboard PCB quick turn**.

Долгосрочная reliability также требует соблюдения IPC-A-610 по Barrel Fill (обычно 75%+). Для контроля voids/cracks используется X-Ray NDT.

### DFM: обеспечить manufacturability и yield THT backplane

Теоретически идеальная [backplane PCB](https://hilpcb.com/en/products/backplane-pcb) может столкнуться с низким yield, высоким cost и даже невозможностью производства, если DFM игнорируется. Для сложных THT backplane DFM особенно важен.

*   **Aspect Ratio:** толщина / минимальный диаметр сверления. Слишком высокий AR ухудшает plating в центре отверстия. Нужно учитывать capability производителя.
*   **Annular Ring:** медное кольцо вокруг отверстия. Должно быть достаточно широким с учетом drilling tolerances и IPC классов.
*   **Spacing и tolerances:** hole-to-copper, hole-to-hole и back-drill depth tolerance напрямую влияют на электрические параметры и yield.

HILPCB предоставляет бесплатный DFM анализ: инженеры проверяют файлы до производства, выявляют сложности и предлагают оптимизации для **AI server motherboard PCB mass production**.

<div style="background-color:#1A237E; color:white; padding: 20px; border-radius: 8px; margin: 20px 0;">
<h3 style="text-align:center; color:white;">HILPCB high-complexity backplane manufacturing capability</h3>
<table style="width:100%; border-collapse:collapse; color:white;">
<thead style="background-color:#3F51B5;">
<tr>
<th style="padding:12px; border:1px solid #7986CB; text-align:left;">Process parameter</th>
<th style="padding:12px; border:1px solid #7986CB; text-align:left;">HILPCB capability</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:12px; border:1px solid #7986CB;">Max layer count</td>
<td style="padding:12px; border:1px solid #7986CB;">64 layers</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #7986CB;">Max PCB thickness</td>
<td style="padding:12px; border:1px solid #7986CB;">10.0 mm</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #7986CB;">Max drill aspect ratio</td>
<td style="padding:12px; border:1px solid #7986CB;">20:1</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #7986CB;">Back-drill depth control</td>
<td style="padding:12px; border:1px solid #7986CB;">± 50 µm</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #7986CB;">Impedance control tolerance</td>
<td style="padding:12px; border:1px solid #7986CB;">± 5%</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #7986CB;">Supported materials</td>
<td style="padding:12px; border:1px solid #7986CB;">Megtron 6/7, Rogers, Tachyon 100G, etc.</td>
</tr>
</tbody>
</table>
</div>

### Как HILPCB обеспечивает high-reliability THT/through-hole soldering

HILPCB сочетает advanced equipment, строгий process control и инженерную экспертизу, чтобы каждая операция THT/through-hole soldering соответствовала самым высоким стандартам.

1.  **Advanced fabrication & assembly equipment:** высокоточная mechanical/laser drilling, advanced plating lines и автоматизация selective soldering + intrusive reflow обеспечивают стабильность.
2.  **Строгий quality control:** AOI для внутренних слоев, X-Ray для регистрации multilayer и barrel fill. Electrical tests и reliability tests (например, thermal shock) обеспечивают надежность каждой [backplane PCB](https://hilpcb.com/en/products/backplane-pcb).
3.  **One-stop solution:** оптимизация **AI server motherboard PCB stackup** и **AI server motherboard PCB routing**, quick turn, массовое производство и сервис [through-hole assembly](https://hilpcb.com/en/products/through-hole-assembly) дают seamless delivery, повышают качество и сокращают time-to-market для **AI server motherboard PCB quick turn**.

#

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

**THT/through-hole soldering** остается критически важным для современных AI server backplane. Это уже не “простая пайка вставных компонентов”, а комплексная инженерия, объединяющая high-speed SI, PI, thermal management и precision manufacturing. Успех требует тесной кооперации между design engineers и опытным производителем вроде HILPCB.

Используя advanced back-drilling, тщательно проработанный stackup, robust PDN и управляемые soldering процессы, можно совместить преимущества reliability THT connector с требованиями high-speed передачи. Если вы разрабатываете next-gen AI servers, switches или HPC и ищете партнера, который глубоко понимает и решает задачи THT/through-hole soldering, HILPCB — отличный выбор.

