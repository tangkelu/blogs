---
title: "halogen free pcb materials: 22 FAQ по stackup и материалам (с audit checklist)"
description: "Практическая подборка из 22 FAQ по halogen free pcb materials: свойства материалов, hybrid lamination, контроль импеданса, TCDk и надёжность, плюс stackup audit checklist и маршрут валидации."
category: technology
date: "2026-01-03"
featured: true
image: ""
readingTime: 8
tags: ["halogen free pcb materials", "high current copper balancing", "surface finish comparison", "thermal reliability stackup", "glass weave skew mitigation", "backdrill planning guide"]
---
## Введение: зачем инженерам Halogen-Free PCB materials

На фоне ужесточения экологических требований (RoHS, REACH) и резкого роста спроса на высокоскоростную и высоконадежную передачу сигналов в 5G, AI server и automotive electronics, `halogen free pcb materials` перестали быть «эко-опцией» и стали техническим must-have для high-performance дизайнов. Но переход с традиционного FR-4 на Halogen-Free — это не простая замена. Он приносит новые риски и задачи: от поведения материала и окна процесса до impedance control и долгосрочной надёжности.

Этот `stackup faq` системно отвечает на 22 ключевых вопроса, которые чаще всего возникают у инженеров при работе с Halogen-Free материалами. Разбираем Dk/Df drift (`dk drift`), управление resin flow (`resin flow`), hybrid lamination, валидацию через impedance Coupon и другие практические аспекты — с решениями и профилактикой.

## Быстрый индекс FAQ по материалам/stackup

Чтобы быстро найти нужную тему, используйте таблицу.

| № | Тема | Ключевые метрики | Рекомендация |
| :--- | :--- | :--- | :--- |
| 1 | Определение Halogen-Free | Cl, Br < 900ppm | Проверить, что datasheet соответствует IPC-4101E |
| 2 | Halogen-Free vs стандартный FR-4 | Tg, Td, CTE, moisture absorption | Для thermal reliability выбирать Halogen-Free с высоким Tg/Td |
| 3 | Стоимость | цена материала, yield процесса | Оценивать TCO, а не только цену материала |
| 4 | Дрейф Dk/Df | Dk/Df vs частота/температура | Для симуляции использовать broadband Dk/Df, а не single-point |
| 5 | Glass weave skew | skew диффпары | Spread glass (например 1067, 1086) и/или routing под углом |
| 6 | Влияние resin content | эффективный Dk, толщина после lamination | Использовать material library HILPCB для точных данных resin content |
| 7 | Совместимость hybrid lamination | mismatch CTE, риск delamination | Подбирать материалы с близким CTE и подтверждать через lamination trials |
| 8 | Параметры lamination | ramp rate, pressure, time | Строго следовать профилю поставщика материала |
| 9 | Resin flow & fill | fill-способность, толщина меди | High Flow prepreg для high-copper и microvia зон |
| 10 | Drilling & machining | roughness стенки, износ сверла | Снизить feed rate и использовать качественные drills |
| 11 | Влага и baking | moisture absorption | Достаточно bake’ить cores и prepregs перед производством |
| 12 | Точность impedance control | допуски диэлектрика, вариация Dk | Замкнуть цикл: HILPCB simulation + impedance Coupon |
| 13 | Надёжность CAF | ion migration, insulation failure | Выбирать resin systems с лучшей CAF resistance |
| 14 | Thermal stress & delamination | Td, Z-CTE | Пик reflow держать значительно ниже Td |
| 15 | Совместимость surface finish | ENIG, OSP, ImAg | Для OSP окно уже — требуется строгий контроль процесса |
| 16 | High-current copper balancing | локальные перегревы, деформация | Оптимизировать медь и избегать контраста «много меди/нет меди» |
| 17 | Backdrill planning | residual stub length | Backdrilling снижает отражения в high-speed дизайнах |
| 18 | Halogen-Free для flex | flex life, стабильность размеров | Предпочитать adhesiveless Halogen-Free материалы |
| 19 | Halogen-Free опции для MCPCB | теплопроводность, выдерживаемое напряжение | Проверять Halogen-Free dielectric (thermal + HI-POT) |
| 20 | Laser drilling (LDA) | качество отверстия, carbonization | Настраивать энергию/пульсы под Halogen-Free resin |
| 21 | Температурный дрейф | TCDk | В wide-temperature учитывать TCDk в расчётах импеданса |
| 22 | Симметрия stackup | warpage | Делать stackup/copper/prepreg симметричными |

---

## 22 вопроса и решения (FAQ)

### Часть 1: базовые свойства и выбор материала

#### Q1: Что считается настоящими `halogen free pcb materials`? Какой стандарт?
- **Проблема**: Многие материалы заявляют «Halogen-Free». Какова формальная дефиниция и как её проверить?
- **Типичный сценарий**: Поставка в ЕС требует compliance, но непонятно, как в datasheet подтвердить соответствие.
- **Метрики/тесты**: По IPC-4101E и IEC 61249-2-21: Cl < 900 ppm, Br < 900 ppm, суммарно Cl+Br < 1500 ppm.
- **Решение**: Запросить datasheet с заявлением по IPC-4101E и проверить значения по halogen content.
- **Профилактика**: Жёстко фиксировать part number материала в документах и BOM, добавляя «Halogen-Free per IPC-4101E», чтобы избежать подмен.

#### Q2: Halogen-Free FR-4 vs стандартный FR-4 — какие ключевые отличия?
- **Проблема**: Кроме экологии, чем Halogen-Free отличается по электрическим и тепловым параметрам от привычного FR-4 (например S1141)?
- **Типичный сценарий**: Обновление продукта до Halogen-Free версии и оценка влияния на thermal reliability.
- **Метрики/тесты**:
    - **Tg**: у Halogen-Free обычно выше (≥150°C, часто 170–180°C) против ~130–140°C у стандартного FR-4.
    - **Td**: Halogen-Free чаще >340°C, лучше thermal stability.
    - **Z-CTE**: до Tg близко; после Tg у Halogen-Free Z-CTE ниже, что повышает via reliability.
    - **Moisture absorption**: из-за иной resin chemistry (часто фосфор-азот) может быть чуть выше.
- **Решение**: Для multi-reflow и high-power applications переход на Halogen-Free может быть улучшением. Но обязательно контролировать влагу через pre-bake.
- **Профилактика**: Рано выбирать класс Tg/Td по требованиям `thermal reliability stackup`.

#### Q3: Halogen-Free всегда дороже? Как считать экономику?
- **Проблема**: Halogen-Free дороже — сильно ли растёт стоимость проекта?
- **Типичный сценарий**: Менеджер сомневается из-за бюджета.
- **Метрики/тесты**:
    - **Цена материала**: часто +10%–30% vs сопоставимый FR-4.
    - **Yield**: материал более brittle, окно drill/lamination уже — на старте yield может снизиться.
    - **Надёжность**: лучшая термостойкость снижает риск отказов и cost of warranty.
- **Решение**: Считать TCO: материал + потенциальный удар по yield + экономия на field failures/repair. Для high-performance/high-reliability TCO обычно оправдан.
- **Профилактика**: Работать с опытным производителем (например HILPCB), чтобы стабилизировать yield.

#### Q4: Почему Dk/Df так сильно гуляет у Halogen-Free (`dk drift`)?
- **Проблема**: Dk/Df заметно меняется с частотой и между лотами.
- **Типичный сценарий**: 25Gbps backplane: расхождение >5% между симуляцией и `impedance coupon`.
- **Метрики/тесты**: Broadband sweep на VNA (например 1–20GHz), S-parameters, извлечение Dk/Df через SPP/VFIT.
- **Решение**:
    1.  **Не использовать single-point**: значение из datasheet на 1GHz не подходит для high-speed.
    2.  **Переход на broadband модели**: запросить измеренные модели из material library HILPCB (например Djordjevic–Sarkar).
    3.  **Учитывать resin content**: разные prepreg styles дают разный effective Dk — нужна точная толщина после lamination и соответствующий Dk.
- **Профилактика**: На старте проекта зафиксировать конкретный материал/stackup и получить корректные модели симуляции.

#### Q5: Как снизить glass weave skew в Halogen-Free?
- **Проблема**: Eye diagram показывает высокий jitter; подозрение на glass weave skew.
- **Типичный сценарий**: PCIe Gen4/5 или 56G-PAM4 — skew диффпары выходит за бюджет.
- **Метрики/тесты**: TDR измерение разницы задержек внутри диффпары.
- **Решение**:
    1.  **Материал**: spread glass / более равномерные weave (например 1067, 1086, 2113) уменьшают локальные неоднородности Dk.
    2.  **Routing**: прокладывать диффпары под небольшим углом к weave (5–10°) или использовать умеренный zig-zag, чтобы усреднить доли resin/glass.
- **Профилактика**: Для `glass weave skew mitigation` сочетать spread glass и routing под углом.

### Часть 2: производство и технологические вызовы

#### Q6: Как resin content влияет на effective Dk и толщину stackup?
- **Проблема**: Выбор prepreg выглядит случайным — какой практический эффект?
- **Типичный сценарий**: Используют много prepreg styles ради общей толщины, а после lamination импеданс «уезжает».
- **Метрики/тесты**: Dk_effective = (Dk_glass * V_glass) + (Dk_resin * V_resin). Resin Dk (~3.0–3.4) заметно ниже glass fiber Dk (~6.0–6.5).
- **Решение**: Препреги с большим resin content (например 106, 1080) дают более низкий Dk после lamination. В stackup нужно точно считать толщины после lamination и resin content по слоям. Инструменты **Stackup simulation** HILPCB используют проверенные данные.
- **Профилактика**: Делать stackup review с опытными инженерами/CAM; не смешивать слишком много prepreg styles и держать близкий resin content.

<div class="div-type-5-container">
    <div class="div-type-5-title">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 15v-2h2v2h-2zm2-4h-2V7h2v6z" fill="#007BFF"></path></svg>
        Ценность сервиса HILPCB
    </div>
    <div class="div-type-5-content">
        <p><strong>Точный stackup — с первого раза.</strong> Устали от Dk/Df drift и impedance mismatch? HILPCB — не только производитель, но и партнёр по материалам и stackup. Мы предоставляем:</p>
        <ul>
            <li><strong>Полную material library:</strong> популярные Halogen-Free материалы с измеренными broadband Dk/Df данными.</li>
            <li><strong>Профессиональную stackup simulation:</strong> Polar Si9000 и Ansys HFSS плюс производственный опыт для высокой корреляции симуляции и реальности.</li>
            <li><strong>Closed-loop validation:</strong> от симуляции и производства до теста <strong>Impedance Coupon</strong> — с end-to-end поддержкой данных.</li>
        </ul>
    </div>
</div>

#### Q7: Какие риски у hybrid lamination с high-frequency материалами (например Rogers)?
- **Проблема**: Можно ли в одном stackup сочетать Halogen-Free FR-4 и Rogers 4350B?
- **Типичный сценарий**: Mixed-signal плата: RF слой на Rogers, цифровые слои на Halogen-Free.
- **Метрики/тесты**:
    - **CTE match**: проверить X/Y/Z CTE; большой mismatch создаёт стресс, delamination или via cracking в температурных циклах.
    - **Совместимость профилей lamination**: разные оптимальные температура/давление/время.
    - **Химическая совместимость resin systems**: возможны нежелательные реакции под heat/pressure.
- **Решение**:
    1.  Подбирать комбинации с максимально близким CTE.
    2.  Делать lamination trials с **hybrid lamination lab** HILPCB.
    3.  Настраивать профиль lamination под окно, приемлемое для обоих материалов.
- **Профилактика**: Рано обсуждать hybrid lamination с производителем. Для критических изделий — mono-material stackup или bondplies для hybrid (например Rogers 3000 series).

#### Q8: Чем отличаются параметры lamination от стандартного FR-4?
- **Проблема**: Можно ли «по привычке» применить FR-4 lamination recipe к Halogen-Free?
- **Типичный сценарий**: Используют один профиль для всех FR-4 материалов и получают whitening/delamination на Halogen-Free.
- **Метрики/тесты**: Lamination profile: ramp rate, cure temperature, cure time, pressure.
- **Решение**: Нет. Halogen-Free resin (часто PN) имеет иной механизм отверждения, обычно требует более высокой температуры и более долгого cure time. Следовать рекомендациям поставщика.
- **Профилактика**: Держать отдельную, валидированную Halogen-Free recipe и явно указывать её в traveler.

#### Q9: Как `resin flow` влияет на fill в heavy-copper и BGA зонах?
- **Проблема**: Microvias под BGA часто имеют недостаточный fill (voiding).
- **Типичный сценарий**: Рядом с плотным signal layer расположены большие copper planes; после lamination толщина над медью меньше, импеданс ниже.
- **Метрики/тесты**: Cross-section: заполнение смолой вокруг внутренней меди и полнота fill в зоне BGA.
- **Решение**:
    1.  **Выбрать правильный prepreg**: по толщине меди и плотности; для microvia fill и high copper использовать High Flow prepreg.
    2.  **Улучшить copper balance**: в `high current copper balancing` добавить hatched copper в разреженных областях для уменьшения разницы плотности.
- **Профилактика**: Оценивать copper coverage по слоям и подбирать prepreg styles; CAM HILPCB выполняет DFM и предупреждает о рисках resin fill.

#### Q10: Halogen-Free более brittle — что меняется в drilling и machining?
- **Проблема**: Chipping по краю при V-Cut или routing.
- **Типичный сценарий**: Hole wall roughness и fiber pull-out ухудшают качество plating.
- **Метрики/тесты**: Тесты roughness, статистика срока службы сверл.
- **Решение**:
    1.  **Оптимизировать drilling**: снизить feed rate и повысить spindle speed.
    2.  **Использовать специализированные drills**: геометрия/покрытие под high-Tg/high-hardness.
    3.  **Корректные entry/exit boards**: улучшают качество стенки отверстия.
- **Профилактика**: Отдельная база параметров для Halogen-Free и контроль износа сверл.

<div class="cta-container">
    <p>Ваш stackup уже учёл все эти факторы? Если есть сомнения — это как раз та точка, где мы можем помочь.</p>
    Загрузите ваш stackup и получите бесплатный экспертный review
</div>

### Часть 3: надёжность и тесты

#### Q11: У Halogen-Free выше moisture absorption — нужен ли специальный baking?
- **Проблема**: После reflow наблюдается popcorning. В чём причина?
- **Типичный сценарий**: Плохой контроль влажности на складе; материал после вскрытия сразу идёт в производство.
- **Метрики/тесты**: Moisture absorption обычно 0.15%–0.35% против ~0.1%–0.2% у стандартного FR-4.
- **Решение**: Да. Bake cores и prepregs перед lamination, а также bake готовых PCBs перед SMT по условиям поставщика (например 120°C, 4–8 часов).
- **Профилактика**: Стандарты хранения/handling, humidity indicator cards и обязательный pre-bake перед запуском. Критично для `thermal reliability stackup`.

#### Q12: Как обеспечить точность impedance control на Halogen-Free PCBs?
- **Проблема**: Даже при симуляции на данных поставщика, `impedance coupon` выходит за допуск.
- **Типичный сценарий**: Цель 50Ω single-ended; измерение 46–54Ω, не проходит ±5%.
- **Метрики/тесты**: TDR на coupon структурах, сравнение с целевым и симуляцией.
- **Решение**: Типичный кейс `material troubleshooting`.
    1.  **Калибровать производственные параметры**: etch compensation и контроль толщины диэлектрика должны быть отражены в модели.
    2.  **Контролировать лоты материалов**: использовать один и тот же lot cores/prepregs для одной партии.
    3.  **Closed-loop feedback**: отдавать результаты coupon в CAM для тонкой настройки компенсации ширины.
- **Профилактика**: Выбирать производителя с сильным process control. HILPCB делает stackup simulation на стадии quotation и контролирует **Impedance Coupon** в производстве.

#### Q13: Halogen-Free материалы более подвержены CAF?
- **Проблема**: Есть мнение, что из-за resin chemistry риск CAF выше.
- **Типичный сценарий**: Industrial-control изделие в высокой влажности/напряжении; life test выявляет micro-shorts, подтверждённые как CAF.
- **Метрики/тесты**: CAF accelerated aging (например 85°C/85%RH с bias) и мониторинг изоляции.
- **Решение**: Выбирать Halogen-Free материалы с подтверждённой CAF resistance; улучшение drilling (меньше повреждений) и качественный desmear тоже снижают риск.
- **Профилактика**: Для серверов/automotive учитывать CAF resistance как ключевой критерий при выборе материала.

<div class="div-type-4-container">
    <div class="div-type-4-title">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z" fill="#D32F2F"></path></svg>
        Предупреждение: игнорирование свойств материала может привести к катастрофе
    </div>
    <div class="div-type-4-content">
        <p>Переносить стандартные FR-4 параметры дизайна и процесса на `halogen free pcb materials` — частая, но крайне опасная ошибка. Это может привести к:</p>
        <ul>
            <li><strong>Потере контроля импеданса:</strong> неверные Dk/Df модели «ломают» high-speed каналы.</li>
            <li><strong>Delamination / popcorning партии:</strong> неправильные lamination/baking параметры проявляются в reflow.</li>
            <li><strong>Долгосрочным отказам:</strong> CAF или via stress cracking вызывают field failures.</li>
        </ul>
        <p>При внедрении новых материалов необходимы серьёзная валидация и партнёрство с опытным производителем.</p>
    </div>
</div>

#### Q14: Как оценить и обеспечить thermal-stress reliability для Halogen-Free stackup?
- **Проблема**: Широкий температурный диапазон — как избежать проблем от расширения/сжатия?
- **Типичный сценарий**: Avionics: -40°C…+125°C, риск разрушения PTH из-за Z expansion.
- **Метрики/тесты**: TMA для Z-CTE; temperature cycling (-40°C to 125°C, 1000 cycles) + microsection на трещины.
- **Решение**:
    1.  **Выбирать low Z-CTE материалы**: меньший post-Tg Z-CTE.
    2.  **Оптимизировать дизайн**: Tear Drop, избегать высоких aspect ratio.
    3.  **Проводить IST**: Interconnect Stress Test для ускоренной оценки thermo-mechanical reliability.
- **Профилактика**: Делать `thermal reliability stackup` анализ на стадии дизайна, учитывая Tg, Td, CTE и реальные условия.

#### Q15: Есть ли специальные требования к surface finish на Halogen-Free?
- **Проблема**: OSP на Halogen-Free показывает худшую solderability, чем на FR-4.
- **Типичный сценарий**: В `surface finish comparison` ENIG adhesion также кажется слабее.
- **Метрики/тесты**: Wetting balance, pull/shear тесты.
- **Решение**: У Halogen-Free иная surface energy/химия, что влияет на реакции с химическими ваннами.
    - **OSP**: настраивать micro-etch rate и концентрацию, чтобы получить равномерную защитную плёнку.
    - **ENIG**: усилить pretreatment (degrease, micro-etch) для достаточной roughness и чистоты меди, улучшая адгезию Ni/Au.
- **Профилактика**: Сообщать производителю, что используется Halogen-Free, чтобы активировать оптимизированные параметры surface finish.

### Часть 4: advanced applications и design

#### Q16: Как делать copper balancing для high-current Halogen-Free PCBs?
- **Проблема**: Локальный перегрев и лёгкий warpage под нагрузкой.
- **Типичный сценарий**: С одной стороны большие power/ground planes, с другой — разреженные control signals.
- **Метрики/тесты**: IR термография, измерение warpage.
- **Решение**: Типичная задача `high current copper balancing`.
    1.  **Симметричный copper fill**: hatched copper на сигнальных/нефункциональных участках для выравнивания copper coverage.
    2.  **Симметричный stackup**: зеркальность относительно центра (copper weights, dielectric thickness, материалы).
    3.  **Улучшить теплоотвод**: thermal vias под горячими компонентами для отвода в внутренние/нижние copper planes.
- **Профилактика**: Учитывать copper balance ещё на стадии layout и использовать EDA анализ copper coverage.

#### Q17: Backdrilling в high-speed Halogen-Free — что важно в планировании?
- **Проблема**: При скоростях >28Gbps нужен ли backdrilling на Halogen-Free?
- **Типичный сценарий**: Through-vias образуют длинные stubs и ухудшают SI.
- **Метрики/тесты**: VNA S21 и точки резонанса stub.
- **Решение**: Да, часто нужен. Dk у Halogen-Free обычно немного выше, чем у некоторых ultra-low-loss материалов, поэтому влияние stub более чувствительно. `backdrill planning guide`:
    1.  **Точно считать stub length**: держать < 1/10 длины волны.
    2.  **Контролировать глубину backdrill**: убрать stub без повреждения signal layer; обычно оставляют 5–7mil запас.
- **Профилактика**: Планировать backdrill на уровне stackup/routing и явно указывать в fabrication drawing.

#### Q18: Есть ли Halogen-Free варианты для FPC и Rigid-Flex?
- **Проблема**: Нужна гибкость плюс Halogen-Free requirement.
- **Типичный сценарий**: Портативное медицинское устройство с многократными сгибами.
- **Метрики/тесты**: Flex-life testing.
- **Решение**: Да. Есть Halogen-Free PI и coverlay. Ключ — adhesiveless конструкции: традиционные adhesives могут содержать галогены и хуже выдерживают динамическую гибку.
- **Профилактика**: В [Rigid-Flex PCB](/rigid-flex-pcb) явно указывать Halogen-Free PI и bondplies.

#### Q19: Как выбрать Halogen-Free решение для MCPCB?
- **Проблема**: LED требует MCPCB по теплу, а заказчик требует Halogen-Free.
- **Типичный сценарий**: Алюминиевый MCPCB для high-power LED: баланс thermal conductivity, dielectric strength и Halogen-Free.
- **Метрики/тесты**: Thermal conductivity (W/m·K) и HI-POT.
- **Решение**: Ключ — изоляционный теплоотводящий dielectric layer. Доступны Halogen-Free thermal dielectrics с керамическими наполнителями (Al2O3, BN). Выбирать по теплопроводности и выдерживаемому напряжению.
- **Профилактика**: Для [MCPCB](/mcpcb) запрашивать подробные datasheets и валидировать на образцах.

#### Q20: Как Halogen-Free влияет на laser drilling microvias?
- **Проблема**: Laser drilling на Halogen-Free HDI даёт нестабильное качество и carbonization residue.
- **Типичный сценарий**: Дно blind via шероховатое, страдает plating/fill reliability.
- **Метрики/тесты**: Microsection формы отверстия и качества стенки.
- **Решение**: Halogen-Free resin иначе поглощает энергию лазера, чем стандартный FR-4. Нужно переоптимизировать параметры (CO2 vs UV, pulse energy/frequency, количество проходов) для чистых отверстий без carbonization.
- **Профилактика**: Выбирать фабрику с опытом Halogen-Free HDI и базой параметров (например HILPCB).

#### Q21: Насколько критичен TCDk у Halogen-Free PCBs?
- **Проблема**: Большие перепады температуры — будет ли drift импеданса?
- **Типичный сценарий**: Automotive radar или RF unit: -40°C…105°C, высокая phase stability.
- **Метрики/тесты**: TCDk (ppm/°C), измерения S-parameters по температуре.
- **Решение**: У Halogen-Free TCDk обычно более выражен, чем у high-frequency laminates (например Rogers). В wide-temperature нужно учитывать изменение импеданса и задержки.
    1.  **Выбирать low TCDk** как критерий.
    2.  **Симулировать с TCDk** и проверить диапазон вариаций.
- **Профилактика**: Не ограничиваться комнатной температурой — нужна wide-temperature оценка.

#### Q22: Почему Halogen-Free чаще даёт warpage и как предотвратить через stackup?
- **Проблема**: После wave solder заметный warpage приводит к BGA дефектам.
- **Типичный сценарий**: Сложная 12-layer server motherboard, warpage выше лимита после assembly.
- **Метрики/тесты**: Диагональный warpage; IPC обычно <0.75%.
- **Решение**: Из-за молекулярной структуры Halogen-Free может накапливать больше внутренних напряжений при cure. Самое эффективное — симметрия.
    1.  **Структурная симметрия**: зеркальный stackup (диэлектрики, copper weights, prepregs).
    2.  **Симметрия распределения меди**: медь равномерно по слоям, без контраста сторон.
    3.  **Process control**: симметричный layup и контроль охлаждения для снижения напряжений.
- **Профилактика**: Симметрия в stackup — базовый метод контроля warpage и важный фактор yield в [PCB Assembly](/pcb-assembly).

---

## Stackup audit checklist

Для системной проверки stackup с `halogen free pcb materials` используйте checklist перед отправкой в производство.

| Категория | Checkpoint | Параметры / требования | Owner |
| :--- | :--- | :--- | :--- |
| **Выбор материалов** | 1. Part number материала явно указан? | e.g., Shengyi S1000-2M, ITEQ IT-180A | Design Eng. |
| | 2. Соответствует Halogen-Free? | IPC-4101E, Cl/Br < 900ppm | Design Eng. |
| | 3. Tg/Td/CTE подходят приложению? | Tg > 170°C, Td > 340°C | Design Eng. |
| | 4. Источник Dk/Df надёжный? | broadband данные, не single-point | SI Eng. |
| | 5. CAF resistance оценена? | CAF report поставщика | Reliability Eng. |
| **Структура stackup** | 6. Stackup симметричен? | mirror symmetry dielectric/copper/prepreg | CAM Eng. |
| | 7. Prepreg styles разумны? | меньше типов; близкий resin content | CAM Eng. |
| | 8. Толщины после lamination посчитаны? | учитывать resin flow и copper coverage | HILPCB Eng. |
| | 9. Общая толщина в допуске? | e.g., 1.6mm ±10% | Design Eng. |
| | 10. Hybrid совместимость подтверждена? | CTE и профиль lamination | HILPCB Eng. |
| **Impedance control** | 11. Цели и допуски определены? | e.g., 50Ω ±7%, 90Ω ±5% | SI Eng. |
| | 12. Модель импеданса калибрована? | etch comp, resin thickness | CAM Eng. |
| | 13. Impedance Coupons предусмотрены? | включить все типы | Design Eng. |
| | 14. Width/spacing в capability? | e.g., Min L/S = 3/3mil | CAM Eng. |
| | 15. Reference planes непрерывны? | избегать crossing splits | SI Eng. |
| **DFM/DFA** | 16. Copper balance оптимизирован? | coverage по слоям близкая | Layout Eng. |
| | 17. Min drill / aspect ratio? | e.g., 0.2mm, Aspect Ratio < 10:1 | CAM Eng. |
| | 18. Стратегия BGA pad/via? | Via-in-Pad, Dog-bone | Layout Eng. |
| | 19. Backdrill требования описаны? | depth, diameter, nets | SI Eng. |
| | 20. Surface finish указан? | ENIG, OSP, ImAg, etc. | Design Eng. |
| **Надёжность** | 21. Via design надёжен? | Tear Drop, Annular Ring > 4mil | Layout Eng. |
| | 22. Glass weave skew учтён? | spread glass, routing под углом | SI Eng. |
| | 23. Baking requirements переданы? | перед lamination и перед SMT | Process Eng. |
| | 24. Warpage риск оценён? | симметрия, большие панели | Mech. Eng. |
| | 25. Требования к тестам определены? | TDR, IST, CAF, HI-POT | QA Eng. |

<div class="div-type-6-container">
    <div class="div-type-6-title">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM14 13v4h-4v-4H7l5-5 5 5h-3z" fill="#4CAF50"></path></svg>
        Производственные возможности HILPCB
    </div>
    <div class="div-type-6-content">
        <p>Мы не только понимаем сложность `halogen free pcb materials`, но и умеем реализовать её в производстве. HILPCB предлагает:</p>
        <ul>
            <li><strong>Широкий склад материалов:</strong> десятки Halogen-Free материалов (high-speed, high-frequency, high-Tg) от Shengyi, ITEQ, Panasonic и др.</li>
            - <strong>Точное оборудование:</strong> высокоточное mechanical drilling, laser drilling и plasma desmear, оптимизированные под жёсткие и brittle материалы.
            - <strong>Advanced lamination:</strong> высокотемпературные прессы с точным контролем ramp, поддержка Halogen-Free и сложных hybrid stackups.
            - <strong>Полный набор тестов:</strong> TDR по импедансу, IST по надёжности и VNA S-parameters, чтобы гарантировать строгие стандарты.
        </ul>
        <p>Выбирая HILPCB, вы выбираете партнёра, который умеет управлять сложными материалами и процессами. Мы помогаем воплотить ваши [high-frequency PCB designs](/high-frequency-pcb) и [high-speed PCB designs](/high-speed-pcb) в реальный продукт.</p>
    </div>
</div>

<!-- COMPONENT: BlogQuickQuoteInline -->

## Итог

Переход с FR-4 на `halogen free pcb materials` — это технический upgrade, а не простой swap. Он требует повышенного внимания к дизайну, симуляции и производству. Ключевой вызов — понять и контролировать новые переменные: нестабильный Dk/Df, особенности lamination, более высокий thermal stress и механическая brittleness.

Эти FAQ помогают структурировать риски и практические меры. Ключ к успеху: **ранняя работа с материалами, симуляция на точных моделях и глубокое взаимодействие с опытным производителем**.

<div class="cta-container">
    <p>Готовы запускать следующий Halogen-Free PCB проект? Команда HILPCB поможет на каждом шаге.</p>
    Запросите расчёт и техническую консультацию
</div>
