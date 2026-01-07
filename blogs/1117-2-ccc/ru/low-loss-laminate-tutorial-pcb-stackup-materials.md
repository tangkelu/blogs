---
title: "low loss laminate tutorial: первый урок по параметрам материалов и планированию stackup"
description: "low loss laminate tutorial про ключевые параметры материалов, stackup planning, trade-off impedance/thermal/cost и влияние производства — с таблицами сравнения и примерами для построения стандартной библиотеки stackup."
category: technology
date: "2025-11-17"
featured: true
image: ""
readingTime: 8
tags: ["low loss laminate tutorial", "hdI stackup tutorial", "hdmi pcb stackup guide", "surface finish comparison", "cti requirement explanation", "thermal reliability stackup"]
---
Привет! Я преподаватель HILPCB Stackup & Materials Academy. В разговоре с инженерами постоянно повторяется одна боль: когда вы делаете high‑speed дизайн, как выбрать правильный low loss laminate среди сотен PCB‑материалов — и спланировать stackup так, чтобы попасть в performance targets, не разрушив cost и manufacturability?

Многие команды делают over‑spec (например, Megtron 6 для 5Gbps) или under‑spec (пытаются «вытянуть» стандартный FR‑4 до 28Gbps) и сталкиваются с проблемами Signal Integrity (SI). Этот **low loss laminate tutorial** — «первая лекция» для команды: переводим абстрактные Dk/Df, CTI и fiber weave effect в практические шаги stackup planning, опираясь на опыт производства HILPCB, чтобы вы делали более разумные trade‑offs.

## 1. Старт stackup design: входные данные и ожидаемые выходы

Профессиональный stackup — это не «интуиция», а системный процесс. До начала соберите:

*   **Signal requirements:**
    *   Максимальный data rate (5Gbps, 10Gbps, 28Gbps+).
    *   Цели impedance control (50Ω single‑ended, 90Ω/100Ω differential).
    *   Общий insertion‑loss budget (dB).
*   **Power Integrity (PI) requirements:**
    *   Токи core device (влияют на copper thickness power planes).
    *   PDN target impedance (влияет на power/ground coupling).
*   **Thermal requirements:**
    *   Мощность и расположение основных источников тепла.
    *   Условия среды и подход к охлаждению — это напрямую определяет требования к **thermal reliability stackup**.
*   **Safety и reliability:**
    *   Стандарты (UL/CE и т.п.).
    *   **CTI requirement explanation**: нужна ли конкретная планка Comparative Tracking Index? Например, для power/industrial часто требуют CTI ≥ 175V (PLC=2) или выше.
    *   Target lifetime и рабочая среда (влияет на выбор high Tg).
*   **Механика и стоимость:**
    *   Максимальная толщина PCB.
    *   Target cost range.

Финальный результат stackup‑планирования — файл, в котором есть:
1.  Функции слоёв (signal/ground/power).
2.  Part number материалов по слоям (Core & Prepreg).
3.  Dielectric thickness и copper thickness по слоям.
4.  Итоговая толщина и допуски.
5.  Impedance targets + рекомендации width/spacing по слоям.
6.  Special process notes (backdrill, resin fill и т.п.).

## 2. Cheat sheet параметров: от FR-4 до low loss laminate

Выбор материала — половина успеха. Ниже — упрощённая `dk df table` по классам потерь (значения зависят от частоты и resin content).

<div class="div-type-1">
    <div class="div-type-1-title">Сравнение характеристик PCB‑материалов</div>
    <div class="div-type-1-content">
        <p>Таблица покрывает параметры от стандартного FR‑4 до extremely low‑loss материалов, чтобы быстро сузить выбор под data rate, рабочую температуру и safety‑требования.</p>
    </div>
</div>

| Класс материала | Типичные опции HILPCB | Dk (@10GHz) | Df (@10GHz) | Tg (°C) | Td (°C) | CTI (V) | Типовые применения |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Standard FR-4** | S1141, KB-6160 | ~4.2 | ~0.020 | 140 | 315 | 175 | Low‑frequency digital/analog, consumer electronics |
| **Mid Tg FR-4** | IT-158, S1155 | ~4.1 | ~0.018 | 150 | 330 | 175 | Multilayer, lead‑free assembly |
| **High Tg FR-4** | IT-180A, S1000 | ~4.0 | ~0.015 | 180 | 345 | 175 | Server, automotive, high‑reliability |
| **Medium loss** | TU-768, S7439 | ~3.8 | ~0.009 | 190 | 360 | 175 | < 10Gbps high‑speed, storage |
| **Low Loss** | TU-872SLK, S1000-2M | ~3.6 | ~0.005 | 190 | 360 | 175 | 10–25Gbps, server backplane, **hdmi pcb stackup guide** |
| **Very Low Loss** | I-Speed, M4S | ~3.3 | ~0.003 | 200 | 380 | 175 | 25–56Gbps, RF communications, test equipment |
| **Ultra Low Loss** | Megtron 6, Tachyon 100G | ~3.0 | ~0.002 | 210 | 400 | 175 | > 56Gbps, core networking, optical module |
| **RF** | Rogers RO4350B | 3.48 | 0.0037 | 280 | 390 | 600 | RF/microwave, antennas |

**Как читать ключевые параметры:**

*   **Dk (dielectric constant):** низкий Dk обычно даёт более широкие трассы при той же impedance; важнее стабильность Dk, чем абсолютное значение.
*   **Df (dissipation factor):** главный параметр потерь; для >5Gbps Df < 0.01 — базовый ориентир.
*   **Tg:** температура стеклования; high Tg (≥170°C) повышает термостабильность и снижает риски при lead‑free.
*   **Td:** температурная деградация; отражает long‑term thermal reliability.
*   **CTI:** устойчивость к tracking; стандартный FR‑4 часто CTI ~175V (PLC=2), специальные применения могут требовать 600V (PLC=0).

## 3. Core stackup patterns: шаблоны 4/6/8/10 слоёв

Теория должна быть «привязана» к практике. Ниже — production‑proven шаблоны как отправная точка.

| Layer count | Stackup (функции) | Core | PP | Итоговая толщина (mm) | Типовое применение |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **4-layer** | SIG/GND/PWR/SIG | 1.0mm Core | 2x 1080 | 1.2 | IoT, MCU control, low‑cost |
| **6-layer** | SIG/GND/SIG/PWR/GND/SIG | 0.5mm Core | 3x 2116 | 1.6 | Embedded, DDR3/4 motherboard |
| **8-layer** | SIG/GND/SIG/PWR/GND/SIG/GND/SIG | 0.2mm Core | 4x 2116/1080 | 1.6 | PCIe, USB3.x, HDMI, HPC |
| **10-layer** | SIG/GND/SIG/GND/PWR/PWR/GND/SIG/GND/SIG | 0.15mm Core | 5x 1080/106 | 1.6 | Server motherboard, сложные **hdI stackup tutorial** |

## 4. Принципы координации signal/power/ground/copper thickness

<div class="div-type-3">
    <div class="div-type-3-title">Golden rules для stackup planning</div>
    <ol>
        <li>
            <h6>Приоритет — непрерывные reference planes</h6>
            <p>High‑speed signal layers должны быть рядом с цельным ground/power plane. Избегайте routing над split — это частая причина EMI и crosstalk.</p>
        </li>
        <li>
            <h6>High‑speed лучше на внутренних слоях</h6>
            <p>Stripline (GND‑SIG‑GND) обычно даёт лучшую EMI‑экранировку и стабильность impedance, чем Microstrip (SIG‑GND).</p>
        </li>
        <li>
            <h6>Плотно связывайте power и ground planes</h6>
            <p>Соседние PWR/GND дают plane capacitance и снижают PDN impedance в HF.</p>
        </li>
        <li>
            <h6>Trade‑off по copper thickness</h6>
            <p>Signal layers обычно 0.5oz (18μm) или 1oz (35μm). Power planes для больших токов могут требовать 2oz (70μm)+ и усиливают требования к <strong>thermal reliability stackup</strong>.</p>
        </li>
        <li>
            <h6>Симметрия stackup против warpage</h6>
            <p>Держите симметрию по материалам/меди/распределению меди — асимметрия увеличивает риск warpage в lamination и reflow.</p>
        </li>
    </ol>
</div>

## 5. Hybrid lamination и special materials: когда стандартных опций недостаточно

Hybrid stackup (например, RF + FR‑4) требует отдельного пресс‑окна, контроля CTE mismatch и аккуратного сверления. Для высоких скоростей также важно учитывать roughness и стабильность Dk/Df в диапазоне.

## 6. Manufacturing impact: «последняя миля» от чертежа к физической PCB

То, что ломает проекты чаще всего:

- неполный stackup drawing (без part number и допусков),
- отсутствие требований к impedance coupons/TDR,
- игнорирование etch bias и plating‑толщин,
- чрезмерно агрессивные line/space без учёта capability фабрики.

## 7. Как HILPCB помогает со stackup design?

<div class="div-type-6">
    <div class="div-type-6-title">Возможности HILPCB, связанные со stackup решениями</div>
    <div class="div-type-6-content">
        <p>HILPCB поддерживает планирование stackup, подбор материалов, контроль допусков и подтверждение impedance (TDR/cross‑section). Это снижает риски SI/PI ещё до выпуска manufacturing data.</p>
    </div>
</div>

<div class="cta-container">
    <div class="cta-text">
        <strong>Нужен быстрый stackup review?</strong> Отправьте требования по data rate/impedance/толщине — и мы предложим production‑ready stackup с учётом DFM и допусков.
    </div>
    <a class="cta-button" href="/">Upload Gerber</a>
</div>

### Summary

- Начинайте с требований (loss budget, impedance targets, токи/тепло, CTI/Tg).
- Выбирайте материал по Df/Dk и стабильности, а не «по бренду».
- Закладывайте симметрию и continuous reference planes.
- Фиксируйте допуски и измерения (impedance coupons, TDR, cross‑section).

## Conclusion

Этот **low loss laminate tutorial** — базовая рамка, которая помогает планировать stackup как инженерную систему. Когда материал, stackup и допуски согласованы с производством и измерениями, high‑speed проект становится предсказуемым и повторяемым.

