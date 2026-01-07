---
title: "Copper coin: как удержать ultra-high-speed link и low-loss в high-speed SI PCB"
description: "Глубокий разбор технологии Copper coin: high-speed Signal Integrity, thermal management и power/interconnect design, чтобы помочь вам создать high-performance high-speed SI PCB."
category: technology
date: "2025-11-16"
featured: true
image: ""
readingTime: 8
tags: ["Copper coin", "Copper pillar", "Heavy copper 3oz+", "Hybrid stack-up (Rogers+FR-4)", "Via-in-Pad plated over (VIPPO)", "Controlled impedance"]
---
В эпоху data-driven систем, от data centers и AI accelerators до инфраструктуры 5G/6G, требования к пропускной способности растут экспоненциально. Серийные SerDes каналы 112G, 224G и выше становятся нормой, создавая новые вызовы для PCB design. Инженерам нужно одновременно выдерживать жесткие требования Signal Integrity (SI) и отводить огромную тепловую мощность современных high-performance чипов. В этом контексте **Copper coin** (embedded copper block) становится ключевым решением для баланса ultra-high-speed передачи и эффективного thermal management. Это не просто “радиаторный” элемент, а фундамент стабильности и надежности всей системы.

Как инженер, который много работал с измерениями TDR/VNA и анализом S-parameters, я знаю: каждый dB loss и каждая ps jitter могут “убить” линк. Традиционные методы вроде thermal via array уже не справляются с FPGA/ASIC/GPU на 150W и выше. В этой статье мы разберем **Copper coin**: принцип, влияние на SI и Power Integrity (PI), интеграцию с продвинутыми stack-up стратегиями и ключевые точки manufacturing контроля — чтобы вы могли управлять двойным вызовом high-speed PCB дизайна.

### Что такое Copper coin и в чем его ключевые преимущества?

**Copper coin** — это продвинутый manufacturing процесс, при котором заранее обработанный массивный медный блок (обычно высокочистая медь C1100) встраивается в подготовленную cavity или through-структуру внутри PCB. Блок напрямую контактирует с Thermal Pad тепловыделяющего устройства (например, чипа в BGA package) и выходит на обратную сторону платы, где может сопрягаться с крупным heatsink или chassis baseplate, формируя путь отвода тепла с очень низким тепловым сопротивлением.

Ключевые преимущества:

1.  **Высокая теплопроводность:** у меди ~400 W/m·K — намного выше, чем у FR-4 (~0.25 W/m·K) и выше эквивалентной теплопроводности plated vias. Массивный **Copper coin** быстро выводит тепло из Hot Spots, часто на порядки эффективнее thermal via array. Это помогает избежать троттлинга и деградации/повреждений.

2.  **Улучшение Power Integrity (PI):** блок часто подключают к GND. Из-за большой массивной металлической структуры он дает return path с очень низкой индуктивностью и импедансом для больших токов, снижает PDN impedance, подавляет Ground Bounce и SSN и обеспечивает стабильный reference plane для high-speed сигналов.

3.  **Повышение механической жесткости:** тяжелый медный блок увеличивает локальную жесткость в зоне BGA, снижая напряжения от CTE mismatch при вибрациях, ударах и thermal cycling, что повышает надежность пайки BGA.

4.  **Гибкость дизайна:** форму/размер/толщину **Copper coin** можно подстроить под package и требования по теплу (T-shape, I-shape и др.), оптимизируя heat path и механическую стыковку.

### Как Copper coin решает thermal management в high-speed системах?

В high-speed цифровых системах затухание тесно связано с температурой. Рост температуры чипа снижает производительность и нагревает dielectrics PCB, меняя Dk и Df. Это влияет на **Controlled impedance** и увеличивает loss, ухудшая SI.

**Copper coin** формирует “thermal highway”:

-   **Прямой контакт и эффективная проводимость:** Thermal Pad через TIM или прямую пайку сопрягается с гладкой поверхностью **Copper coin**, и тепло почти без барьеров уходит из junction в блок.
-   **Вертикальное и латеральное spreading:** кроме проводимости по Z, масса блока обеспечивает сильное spreading в X-Y, распределяя Hot Spots на большую площадь и снижая локальный перегрев.
-   **Прямой вывод на внешнее охлаждение:** backside блока обычно заподлицо (или слегка выступает) и может напрямую контактировать с heatsink, liquid cold plate или корпусом. Металл‑металл резко снижает сопротивление интерфейса по сравнению с FR-4 + vias.

В приложениях с очень большими токами (например, мощные DC/DC) часто применяют **Heavy copper 3oz+**. **Copper coin** может интегрироваться с thick copper layers, формируя устойчивую электро‑термическую систему: переносить сотни ампер и эффективно отводить Joule heat.

<div style="background-color: #F5F7FA; padding: 20px; border-radius: 8px; margin: 20px 0;">
<h3 style="text-align: center; color: #000000;">Сравнение эффективности решений для отвода тепла</h3>
<table style="width:100%; border-collapse: collapse; text-align: center;">
<thead style="background-color: #E0E0E0;">
<tr>
<th style="padding: 12px; border: 1px solid #ccc; color: #000000;">Параметр</th>
<th style="padding: 12px; border: 1px solid #ccc; color: #000000;">Copper Coin</th>
<th style="padding: 12px; border: 1px solid #ccc; color: #000000;">Thermal via array (Thermal Vias)</th>
<th style="padding: 12px; border: 1px solid #ccc; color: #000000;">Vapor chamber embedded (Vapor Chamber)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Эквивалентная теплопроводность</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Очень высокая (≈400 W/m·K)</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Низкая–средняя (50-150 W/m·K)</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Экстремально высокая (1500-2000+ W/m·K)</td>
</tr>
<tr>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Тепловое сопротивление</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Очень низкое</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Выше</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Очень низкое</td>
</tr>
<tr>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Влияние на routing</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Большая keep-out зона</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Можно вести между vias, но с ограничениями</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Очень большая keep-out зона</td>
</tr>
<tr>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Стоимость manufacturing</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Высокая</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Низкая</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Очень высокая</td>
</tr>
<tr>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Типовые сценарии</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">High-power ASIC/FPGA, optical modules</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Medium/low-power устройства, package QFN</td>
<td style="padding: 12px; border: 1px solid #ccc; color: #000000;">Server CPU/GPU с экстремальными требованиями по теплу</td>
</tr>
</tbody>
</table>
</div>

### Двойное влияние на SI: возможности и риски

С точки зрения SI, **Copper coin** — “двухсторонний меч”. Правильное применение повышает производительность, а игнорирование рисков может привести к failure линка.

**Возможности (позитивные эффекты):**

-   **Стабильный reference plane:** подключенный к GND блок дает очень стабильный “нулевой” reference. Это особенно важно для differential pairs: обе линии видят одинаковую среду, **Controlled impedance** удерживается лучше, а common-mode conversion уменьшается.
-   **Снижение crosstalk:** блок выступает как крупная ground структура и помогает изолировать области платы, например физически разделять noisy power и чувствительные SerDes, снижая EMI и crosstalk.
-   **Температурная стабильность:** удерживая температуру, **Copper coin** стабилизирует Dk/Df материалов (например, [Rogers PCB](https://hilpcb.com/en/products/rogers-pcb)). Для long-reach и high-data-rate даже небольшие дрейфы Dk/Df приводят к impedance mismatch и росту loss.

**Риски (негативные эффекты):**

-   **Разрыв reference:** если high-speed net пересекает край блока, reference plane становится не непрерывным. Return current вынужден обходить, увеличивается площадь петли и растут отражения/излучение/EMI.
-   **Скачок импеданса:** даже при трассировке “над” блоком поле меняется, потому что reference снизу меняется с тонкой фольги на массив меди. Часто импеданс резко падает (ёмкостная дисконтиниуитетность) и возникают отражения.
-   **Блокировка routing:** блок создает крупную keep-out область и усложняет high-density BGA fan-out.

Чтобы справиться, нужно планировать заранее: не вести high-speed через край; ставить плотные ground Stitching Vias по периметру; использовать 3D EM simulation для моделирования влияния на соседние transmission lines и корректировать width/spacing для компенсации импеданса.

### Интеграция Copper coin со stack-up стратегией

Успешная реализация **Copper coin** требует тесной интеграции с stack-up design — особенно в сложных системах с high-speed и high-power. Одна структура редко закрывает все требования.

Здесь помогает **Hybrid stack-up (Rogers+FR-4)**: low-loss материалы (Rogers, Megtron series) для критических слоев, FR-4 для power/ground и low-speed.

Интеграция **Copper coin** в **Hybrid stack-up (Rogers+FR-4)** дает оптимальный баланс:
1.  **Максимум производительности:** differential pairs 56G/112G+ на Rogers слоях, чтобы минимизировать insertion loss и dispersion, а **Copper coin** отводит тепло от ASIC/FPGA на top.
2.  **Контроль стоимости:** дорогие low-loss материалы используются только там, где они нужны.
3.  **Интеграция дизайна:** нужно точно задать thickness, embed depth и взаимосвязь с слоями. Верх блока должен обеспечить хорошую Co-planarity с внешним медным слоем для надежной пайки BGA.

В плотной BGA области вокруг блока важен и **Via-in-Pad plated over (VIPPO)**. VIPPO делает vias прямо в pads, затем заполняет проводящей смолой и плакирует сверху, получая плоскую поверхность pad. Это сокращает routing и снижает паразитные L/C, помогая high-density fan-out. Органическое сочетание **Copper coin**, **Hybrid stack-up (Rogers+FR-4)** и **Via-in-Pad plated over (VIPPO)** — “тройка” современного [high-speed PCB](https://hilpcb.com/en/products/high-speed-pcb) дизайна.

<div style="background: #ffffff; border: 1px solid #d1c4e9; border-top: 6px solid #673ab7; border-radius: 16px; padding: 30px; margin: 30px 0; font-family: 'Segoe UI', system-ui, sans-serif; box-shadow: 0 10px 30px rgba(103,58,183,0.08);">
<h3 style="text-align: center; color: #311b92; margin: 0 0 30px 0; font-size: 1.6em; font-weight: 800; border-bottom: 2px solid #b39ddb; padding-bottom: 15px; display: flex; align-items: center; justify-content: center;">🔥 Copper Coin: ключевые пункты design и thermal management</h3>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">
<div style="background: #f3e5f5; border: 1px solid #e1bee7; padding: 20px; border-radius: 12px; display: flex; flex-direction: column;">
<strong style="color: #4a148c; font-size: 1.1em; margin-bottom: 10px; display: flex; align-items: center;">📍 Раннее физическое планирование</strong>
<p style="color: #311b92; font-size: 0.9em; line-height: 1.6; margin: 0; flex-grow: 1;">С самого начала зафиксируйте геометрию и embed depth <strong>Copper Coin</strong>. Рассматривайте его как Mechanical Constraint и точно совмещайте с Thermal Pad силового устройства.</p>
</div>
<div style="background: #f3e5f5; border: 1px solid #e1bee7; padding: 20px; border-radius: 12px; display: flex; flex-direction: column;">
<strong style="color: #4a148c; font-size: 1.1em; margin-bottom: 10px; display: flex; align-items: center;">🛤️ Сигналы и return path</strong>
<p style="color: #311b92; font-size: 0.9em; line-height: 1.6; margin: 0; flex-grow: 1;">Не прокладывайте high-speed сигналы через физические gaps между блоком и reference plane. На краю размещайте <strong>Stitch Vias</strong>, обеспечивая непрерывность return path и снижая риск избыточного <strong>EMI</strong>.</p>
</div>
<div style="background: #f3e5f5; border: 1px solid #e1bee7; padding: 20px; border-radius: 12px; display: flex; flex-direction: column;">
<strong style="color: #4a148c; font-size: 1.1em; margin-bottom: 10px; display: flex; align-items: center;">🌡️ Оптимизация TIM</strong>
<p style="color: #311b92; font-size: 0.9em; line-height: 1.6; margin: 0; flex-grow: 1;">Используйте <strong>TIM</strong> с высокой теплопроводностью между package и блоком. Жестко контролируйте <strong>Bondline Thickness (BLT)</strong>, чтобы снизить контактное тепловое сопротивление.</p>
</div>
<div style="background: #ede7f6; border: 1px solid #d1c4e9; padding: 20px; border-radius: 12px; display: flex; flex-direction: column;">
<strong style="color: #311b92; font-size: 1.1em; margin-bottom: 10px; display: flex; align-items: center;">🏭 Согласование manufacturing (HILPCB)</strong>
<p style="color: #311b92; font-size: 0.9em; line-height: 1.6; margin: 0; flex-grow: 1;">Ранний технический диалог с <strong>Highleap PCB Factory</strong>: заранее оцените <strong>Coin Coplanarity</strong>, контроль overflow клея после press-fit и риск mismatch <strong>CTE</strong> между материалами.</p>
</div>
</div>
<div style="margin-top: 25px; padding: 15px; background: #e8eaf6; border-radius: 8px; border-left: 5px solid #3f51b5; font-size: 0.88em; color: #283593; line-height: 1.6;">
<strong>Технический insight:</strong> по сравнению с thermal via array, embedded Copper Coin может повысить эффективность теплопередачи на <strong>10×+</strong>. Для RF power amp на <strong>GaN</strong> с очень высокой power density, T-Coin или I-Coin embedding часто является лучшим путем для миллисекундного transient охлаждения.
</div>
</div>

### Copper pillar vs Copper coin: различия и выбор

При обсуждении внутренних металлических thermal структур часто упоминают **Copper pillar**. Хотя оба подхода используют медь, они заметно различаются по структуре, применению и процессу.

-   **Определение и структура:**
    -   **Copper coin:** отдельный массивный блок, заранее обработанный и встроенный в PCB через press-fit/bonding; обычно крупный и покрывает большую часть footprint package.
    -   **Copper pillar:** медные “столбики”, сформированные plating’ом, меньшего диаметра и часто в виде плотных arrays; это могут быть solid pillars или Cu-filled vias.

-   **Основные применения:**
    -   **Copper coin:** “точечный” отвод тепла от одного high-power устройства — макро перенос тепла.
    -   **Copper pillar:** тонкая (micro) термокомпенсация и вертикальный interconnect; часто в HDI/IC substrates как conductive/thermal path или micro thermal pillar array под чипом.

-   **Как выбирать:**
    -   Для BGA с TDP > 100W — **Copper coin** практически безальтернативен.
    -   Для нескольких распределенных low-power устройств (например, QFN power IC) или крайне плотных зон, где важны вертикальная связь и теплопроводность, выгоднее **Copper pillar** arrays.
    -   В некоторых проектах оба подхода комбинируют: **Copper coin** для основного тепла, **Copper pillar** — для локальных hotspots.

Итого: **Copper coin** — “тяжелая артиллерия” для core thermal; **Copper pillar** — “точечный инструмент” для распределенных electro-thermal задач.

### Manufacturing этапы и quality control для Copper coin PCB

Embedded массивный металл в точный [multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb) — сложная задача. Успех зависит от точности процесса и QC. Highleap PCB Factory (HILPCB) накопила глубокий опыт по **Copper coin**.

Ключевые этапы:

1.  **Cavity routing:** высокоточный CNC milling кавити в частично ламинированном стеке; контроль глубины определяет итоговую coplanarity.
2.  **Изготовление блока и surface treatment:** микронные допуски; surface treatment (например, ENIG) для надежного bonding и пайки.
3.  **Press-fit & bonding:** установка блока в cavity; interference fit и/или высокотеплопроводный клей. Температура/давление строго контролируются, чтобы не повредить базовый материал PCB.
4.  **Planarization:** grinding/polishing для устранения перепадов высоты; coplanarity для BGA обычно в пределах ±1 mil.
5.  **Дальнейшие lamination и plating:** после embedding выполняются внешняя lamination, drilling и plating; химия и температура должны не ухудшать интерфейс bonding.

QC проходит через весь процесс: X-Ray для проверки внутренних соединений и отсутствия voids, cross-section анализ интерфейса, профилометрия для coplanarity. Для **Heavy copper 3oz+** у HILPCB есть специализированные линии etching/plating, обеспечивающие точность и равномерность thick copper рисунка.

<div style="background-color: #1A237E; color: #FFFFFF; padding: 20px; border-radius: 8px; margin: 20px 0;">
<h3 style="text-align: center; color: #FFFFFF;">HILPCB: advanced process capability</h3>
<table style="width:100%; border-collapse: collapse; text-align: center;">
<thead style="background-color: #3F51B5;">
<tr>
<th style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">Параметр процесса</th>
<th style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">Возможности HILPCB</th>
<th style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">Значение для Copper Coin</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">Макс. число слоев</td>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">64 layers</td>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">Поддержка сложных high-speed backplane и server mainboard</td>
</tr>
<tr>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">Диапазон толщины меди</td>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">0.5oz - 20oz</td>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">Полная поддержка Heavy copper 3oz+ и выше</td>
</tr>
<tr>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">Точность impedance control</td>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">±5%</td>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">Надежная Controlled impedance для high-speed каналов</td>
</tr>
<tr>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">Мин. механическое сверление</td>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">0.15mm</td>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">Поддержка HDI и тонких Via-in-Pad структур</td>
</tr>
<tr>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">Контроль coplanarity</td>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">±0.025mm (1 mil)</td>
<td style="padding: 12px; border: 1px solid #7986CB; color: #FFFFFF;">Надежность пайки BGA и HF connectors</td>
</tr>
</tbody>
</table>
</div>

### Simulation: как точно предсказать характеристики Copper coin

Учитывая сильное влияние **Copper coin** и его стоимость, multi-physics simulation до hardware build крайне важна: она валидирует дизайн, выявляет риски на ранней стадии и помогает избежать дорогих переделок.

Обычно выполняют два направления:

1.  **Thermal simulation:**
    -   **Цель:** рассчитать junction temperature, распределение температур по PCB и heat flow paths.
    -   **Инструменты:** Ansys Icepak, Flotherm, SimScale и др.
    -   **Inputs:** точные 3D модели (stack-up, **Copper coin**, package, TIM, heatsink), термосвойства материалов, power dissipation и условия среды.
    -   **Результаты:** подтвердить эффективность, оптимизировать геометрию и оценить необходимость более мощного внешнего охлаждения.

2.  **Electromagnetic simulation:**
    -   **Цель:** оценить влияние на SI и PI.
    -   **Инструменты:** Ansys HFSS, CST Microwave Studio, Keysight ADS и др.
    -   **SI:** извлечь S-parameters transmission lines с учетом **Copper coin**, анализировать insertion/return loss и crosstalk, особенно для трасс возле края, чтобы удержать **Controlled impedance**.
    -   **PI:** анализ PDN impedance по частоте и проверка подавления шума за счет низкоимпедансного ground path.

Успех следует принципу “Garbage In, Garbage Out”: нужны корректные параметры материалов, детальная геометрия и настройки, соответствующие manufacturing. Команда HILPCB может выполнить DFM review и связать допуски/базу материалов с моделями, чтобы симуляция максимально соответствовала финальному изделию.

### Перспективы: Copper coin в будущем data center и AI hardware

С ростом power density чипы на 300W и даже 500W станут обычным явлением. В этих условиях **Copper coin** будет использоваться шире и станет еще важнее.

-   **Next-gen data centers:** в SerDes 224G+ бюджеты loss/jitter крайне ограничены. Стабилизируя температуру, **Copper coin** косвенно удерживает стабильность low-loss материалов в **Hybrid stack-up (Rogers+FR-4)** и поддерживает long-reach (LR) backplane и optical-module interconnect.
-   **AI/HPC accelerators:** GPU и AI чипы — главные потребители мощности. **Copper coin** — одна из самых эффективных PCB-level технологий охлаждения, позволяющая держать частоты на максимуме.
-   **CPO:** Co-Packaged Optics уменьшает электрические расстояния, но увеличивает heat flux density; **Copper coin** и похожие embedded thermal структуры становятся ключевыми для CPO substrates.
-   **Automotive electronics:** потребности по отводу тепла для IGBT, LiDAR и domain controller растут; **Copper coin** имеет большой потенциал в high-reliability приложениях.

В сочетании с high-density процессами вроде **Via-in-Pad plated over (VIPPO)**, **Copper coin** сможет поддерживать packages с большим количеством pins и меньшим pitch, раздвигая границы производительности.

#

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

**Copper coin** — это не просто продвинутое охлаждение, а системное решение, которое влияет на весь high-speed PCB design. Оно связывает thermal management, SI и PI и становится обязательным инструментом для экстремальной производительности. От точного контроля **Controlled impedance** и баланса cost/performance через **Hybrid stack-up (Rogers+FR-4)** до высокой плотности с **Via-in-Pad plated over (VIPPO)** — успешное применение **Copper coin** отражает системную сложность современного PCB.

Однако эта технология требует очень высокого уровня manufacturing. Выбор партнера вроде Highleap PCB Factory (HILPCB) критичен. Мы изготавливаем [Heavy copper PCB](https://hilpcb.com/en/products/heavy-copper-pcb) по строгим требованиям и обеспечиваем end-to-end поддержку: design review, simulation support и [turnkey PCBA assembly](https://hilpcb.com/en/products/turnkey-assembly), чтобы ваша инновация стала надежным продуктом.

Если вы разрабатываете next-gen high-performance решения и сталкиваетесь с тяжелыми задачами по теплу и SI, свяжитесь с нашими техническими экспертами. Давайте вместе использовать **Copper coin**, чтобы создать для вашего продукта мощный и при этом “cool” core.

