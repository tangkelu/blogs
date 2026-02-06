---
title: "Многослойная структура RDL Fan-out: Освоение взаимосвязи AI-чипов и вызовов высокоскоростного взаимодействия"
description: "Глубокий анализ основной технологии многослойной структуры RDL fan-out, охватывающий целостность сигналов высокой скорости, управление тепловыми процессами и проектирование питания/взаимодействия."
category: technology
date: "2025-11-17"
featured: true
image: ""
readingTime: 8
tags: ["RDL fan-out substrate stackup", "RDL fan-out substrate validation", "RDL fan-out substrate quick turn", "RDL fan-out substrate guide", "RDL fan-out substrate impedance control", "RDL fan-out substrate layout"]
---

Как инженер производственной валидации (ATE‑тестирование, надёжность в термоциклах и анализ дефектов массового производства), я каждый день сталкиваюсь с физическими пределами, которые диктует закон Мура. В области AI и HPC эта проблема доведена до предела: важна уже не только производительность одного кристалла, а то, насколько эффективно и надёжно можно интегрировать несколько chiplet в один package. Именно здесь ключевую роль играет **RDL fan-out substrate stackup**. Это не просто «физический мост» между чипом и внешним миром — это фактор, который определяет производительность, энергопотребление и надёжность всего AI‑ускорителя. Плохо спроектированный стек может привести к затуханию сигнала, шуму питания и даже к катастрофическим тепловым отказам — того, что мы всеми силами стараемся не допустить в серийной валидации.

Потребность в вычислениях для AI растёт экспоненциально и толкает упаковку к 2.5D/3D‑интеграции. В таких условиях традиционные wire bonding и flip‑chip перестают удовлетворять требованиям по плотности десятков тысяч I/O. **RDL fan-out substrate stackup** вводит тончайшие уровни разводки (Redistribution Layer, RDL), выполненные по технологиям, близким к полупроводниковым процессам, и реализует fan‑out соединение от микронных pad на die к миллиметровым solder ball на подложке. Это снимает «узкое место» по I/O‑плотности и обеспечивает более короткие/качественные пути для высокоскоростных интерфейсов (например, HBM3e). Наша задача в валидации — доказать, что такие сложные стеки сохраняют целостность после жёстких производственных процессов и в реальных условиях эксплуатации. Базой для такого уровня сложности являются передовые технологии [IC Substrate PCB](https://hilpcb.com/en/products/ic-substrate-pcb) от производителей уровня Highleap PCB Factory (HILPCB).

## Почему стек подложки для AI критически важен?

В AI‑проектах подложка давно вышла за рамки «обычной PCB» — она стала частью package и фундаментом производительности. Для AI‑ускорителя, где есть вычислительные ядра, стеки HBM и I/O‑модули, значимость **RDL fan-out substrate stackup** проявляется так:

1. **Плотность I/O и пространство под трассировку:** современные AI‑GPU имеют десятки/сотни тысяч I/O. RDL‑уровни с L/S 2µm/2µm (или тоньше) обеспечивают беспрецедентную плотность.
2. **Пути передачи high‑speed сигналов:** скорость интерфейса HBM3/3e превышает 9.6 Gbps/pin; сигнал может деградировать уже через десятки микрометров. Правильный RDL‑стек минимизирует длину критических путей и обеспечивает понятный return path.
3. **Power Integrity (PI):** AI‑нагрузки создают огромные dI/dt‑пики. Плоскости питания и земли должны быть толстыми, непрерывными и тесно связанными для сверхнизкой импедансной трассы и оптимального размещения развязки.
4. **Тепловые каналы:** TDP > 1000W — уже не редкость. Выбор материалов (высокая теплопроводность диэлектрика), thermal via arrays и толщина металла напрямую влияют на теплоотвод.

С точки зрения валидации каждый нюанс — от согласования CTE до надёжности microvia — определяет, пройдут ли изделия термоциклы (например, −40°C…125°C), HAST и другие стресс‑тесты.

## Как RDL переопределяет высокоплотную межсоединительную архитектуру

RDL (Redistribution Layer) — ключевая технология advanced packaging. Это тонкие металлические слои разводки, формируемые полупроводниковыми процессами (sputtering, plating, lithography) на wafer или panel. В отличие от традиционных субтрактивных процессов PCB/подложек, RDL часто выполняется аддитивно/полуаддитивно и даёт гораздо более высокую точность.

В fan‑out упаковке RDL «перераспределяет» тесно расположенные I/O‑pad на die по более широкой области, совместимой с BGA‑pitch. Это даёт:

* **Substrate‑free подход:** в FO‑WLP чип встраивается в EMC (эпоксидный компаунд), а RDL формируется прямо на EMC и поверхности die — без классической BT‑подложки.
* **Очень короткий interconnect‑путь:** за счёт прямого соединения снижаются индуктивности/ёмкости по сравнению с flip‑chip через C4 bumps и interposer/substrate — критично для GHz‑сигналов и [high-speed PCB](https://hilpcb.com/en/products/high-speed-pcb).
* **Гибкая гетерогенная интеграция:** RDL как «электрическое полотно» упрощает объединение разнородных chiplet и делает SiP практичным.

Для массовой валидации RDL добавляет новые риски: дефекты (open/short, неравномерная ширина) требуют более точного AOI и электротеста. Адгезия RDL к EMC/поверхности чипа и механическая стойкость при температурных циклах — частые точки отказа. Поэтому надёжный **RDL fan-out substrate stackup** должен учитывать эти факторы на этапе проектирования.

<div style="background: #ffffff; border: 1px solid #ddd6fe; border-radius: 24px; padding: 40px 30px; margin: 30px 0; font-family: 'Segoe UI', system-ui, sans-serif; box-shadow: 0 15px 50px rgba(102, 51, 153, 0.1);">
<h3 style="text-align: center; color: #4b0082; margin: 0 0 15px 0; font-size: 1.85em; font-weight: 800; border-bottom: 4px solid #663399; padding-bottom: 15px; display: inline-block; width: 100%;">⚙️ Проектирование RDL Fan‑Out Substrate: ключевые принципы передовых процессов</h3>
<p style="text-align: center; color: #64748b; font-size: 1.05em; margin-bottom: 40px;">В RDL Fan-out Substrate Layout необходима совместная оптимизация по нескольким физическим доменам для достижения высокой выходности и производительности</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 18px;">
<div style="background: #f5f3ff; border: 1px solid #ede9fe; border-radius: 18px; padding: 25px; border-top: 6px solid #663399; display: flex; flex-direction: column;">
<strong style="color: #4c1d95; font-size: 1.15em; margin-bottom: 15px;">01. Баланс напряжений и симметрия</strong>
<p style="color: #475569; font-size: 0.9em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Логика:</strong> для контроля <strong>warpage</strong> стек должен быть физически симметричным. Балансируйте плотность меди в RDL и толщины диэлектрика так, чтобы напряжения компенсировались в термоциклах reflow, предотвращая трещины подложки и расслоение.</p>
</div>
<div style="background: #f5f3ff; border: 1px solid #ede9fe; border-radius: 18px; padding: 25px; border-top: 6px solid #663399; display: flex; flex-direction: column;">
<strong style="color: #4c1d95; font-size: 1.15em; margin-bottom: 15px;">02. Сверхнизкопотерные материалы (ABF/PI)</strong>
<p style="color: #475569; font-size: 0.9em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Логика:</strong> выбор материалов должен соответствовать целям <strong>Low Dk / Low Df</strong>. Приоритет — передовые диэлектрики вроде <strong>ABF (Ajinomoto Build-up Film)</strong>. CTE должен быть близок к кремнию, чтобы снизить риск усталости соединений.</p>
</div>
<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 18px; padding: 25px; border-top: 6px solid #64748b; display: flex; flex-direction: column;">
<strong style="color: #1e293b; font-size: 1.15em; margin-bottom: 15px;">03. Качественный reference plane и return path</strong>
<p style="color: #475569; font-size: 0.9em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Логика:</strong> для каждого высокоскоростного RDL‑уровня нужен соседний и непрерывный <strong>reference plane</strong>. Запрещайте трассировку через split, чтобы минимизировать индуктивность петли и удержать SI на 112G и выше.</p>
</div>
<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 18px; padding: 25px; border-top: 6px solid #64748b; display: flex; flex-direction: column;">
<strong style="color: #1e293b; font-size: 1.15em; margin-bottom: 15px;">04. Архитектура microvia</strong>
<p style="color: #475569; font-size: 0.9em; line-height: 1.7; margin: 0; flex-grow: 1;"><strong>Логика:</strong> предпочтительны <strong>staggered microvias</strong> (шахматные) для повышения надёжности. При stacked‑микровиях строго контролируйте число уровней и качество заполнения, чтобы исключить дефекты металлизации и разрушения при тепловом расширении.</p>
</div>
</div>
<div style="margin-top: 30px; padding: 25px; background: linear-gradient(90deg, #4b0082, #2d3748); border-radius: 16px; color: #ffffff;">
<strong style="color: #d8b4fe; font-size: 1.1em; display: block; margin-bottom: 8px;">🚀 Возможности HILPCB по advanced packaging: от прототипа до серии</strong>
<p style="color: rgba(255,255,255,0.9); font-size: 0.92em; line-height: 1.7; margin: 0;">Для ультратонких линий RDL fan‑out подложек HILPCB обеспечивает <strong>L/S ≤ 5/5μm</strong>. Интегрируя AOI и вакуумную прессовку, мы достигаем высокой согласованности импеданса и физической надёжности на каждом уровне переразводки.</p>
</div>
</div>

## Основные SI‑проблемы в RDL fan‑out дизайне

Целостность сигналов (SI) критична для корректной передачи данных. В **RDL fan-out substrate stackup** с экстремальной плотностью и частотами проблемы SI проявляются особенно сильно.

Первое — **RDL fan-out substrate impedance control**. Разрывы импеданса вызывают отражения, закрытие eye‑diagram и рост BER. На микронных трассах RDL малейшие вариации ширины, толщины диэлектрика и Dk приводят к заметному дрейфу импеданса. Точный контроль требует field solver и строгого контроля процесса. HILPCB использует тест‑купоны и TDR для контроля и удерживает точность обычно в пределах ±5% по партиям. Для первого приближения можно использовать онлайн‑калькулятор импеданса.

Второе — **crosstalk**. На плотных RDL‑слоях параллельные линии сильно связываются. Стратегии:

* **Увеличить расстояние** (часто правило 3W).
* **Экранирующие GND‑трассы** между чувствительными сигналами.
* **Оптимизация по слоям** (разведение HS‑сетей по разным слоям, ортогональные направления).
* **Непрерывные reference plane**.

Наконец, **insertion loss** (потери диэлектрика + проводника/skin effect) становится критичен >10GHz. Ultra‑low‑loss материалы и снижение шероховатости меди помогают.

## Как управлять тепловыми hot spot в плотном RDL‑стеке

Тепловая часть — ахиллесова пята AI‑упаковки. В типичном **RDL fan-out substrate stackup** тепло проходит путь chiplet → TIM → RDL → EMC → core подложки → радиатор. Любое «узкое место» приводит к накоплению тепла.

В валидации термоциклы и power‑cycling помогают выявить слабые места. Ключевые подходы:

1. **Интегрированные решения отвода:** прямой контакт радиатора с EMC или backside die (IHS / direct liquid cooling).
2. **Оптимизация TIM:** баланс теплопроводности, адгезии и долговременной надёжности; liquid metal эффективен, но несёт риск утечки/коррозии.
3. **Латеральное распределение тепла:** толстые copper planes/coins внутри RDL и core.
4. **Плотные thermal via arrays:** заполненные тепловые vias под кристаллом для вертикальных каналов отвода.

Тепловое моделирование нужно подключать заранее, чтобы выявлять hot spot и выбирать материалы/структуру ещё до дорогостоящих тестов.

<div style="background-color:#ECEFF1;padding:20px;border-radius:10px;margin:20px 0;">
<h3 style="color:#000000;text-align:center;border-bottom:3px solid #00796B;padding-bottom:10px;">Сравнение материалов термоинтерфейса (TIM)</h3>
<table style="width:100%;text-align:center;color:#000000;border-collapse:collapse;">
<thead style="background-color:#B0BEC5;color:#000000;">
<tr>
<th style="padding:10px;border:1px solid #78909C;">Тип материала</th>
<th style="padding:10px;border:1px solid #78909C;">Типичная теплопроводность (W/m·K)</th>
<th style="padding:10px;border:1px solid #78909C;">Плюсы</th>
<th style="padding:10px;border:1px solid #78909C;">Минусы/риски</th>
</tr>
</thead>
<tbody>
<tr style="background-color:#FAFAFA;">
<td style="padding:10px;border:1px solid #CFD8DC;">Термопаста</td>
<td style="padding:10px;border:1px solid #CFD8DC;">1 - 12</td>
<td style="padding:10px;border:1px solid #CFD8DC;color:#1E3A8A;">Дёшево, легко наносить</td>
<td style="padding:10px;border:1px solid #CFD8DC;color:#333333;">Возможны pump‑out/высыхание со временем</td>
</tr>
<tr style="background-color:#FFFFFF;">
<td style="padding:10px;border:1px solid #CFD8DC;">Материал фазового перехода (PCM)</td>
<td style="padding:10px;border:1px solid #CFD8DC;">3 - 9</td>
<td style="padding:10px;border:1px solid #CFD8DC;color:#1E3A8A;">Высокая надёжность, нет pump‑out</td>
<td style="padding:10px;border:1px solid #CFD8DC;color:#333333;">Нужна температура фазового перехода для лучшей работы</td>
</tr>
<tr style="background-color:#FAFAFA;">
<td style="padding:10px;border:1px solid #CFD8DC;">Теплопроводящий гель</td>
<td style="padding:10px;border:1px solid #CFD8DC;">2 - 10</td>
<td style="padding:10px;border:1px solid #CFD8DC;color:#1E3A8A;">Хорошо заполняет зазоры, низкие напряжения</td>
<td style="padding:10px;border:1px solid #CFD8DC;color:#333333;">Теплопроводность ниже, чем у топ‑решений</td>
</tr>
<tr style="background-color:#FFFFFF;">
<td style="padding:10px;border:1px solid #CFD8DC;">Жидкий металл</td>
<td style="padding:10px;border:1px solid #CFD8DC;">> 70</td>
<td style="padding:10px;border:1px solid #CFD8DC;color:#1E3A8A;">Очень высокая теплопроводность</td>
<td style="padding:10px;border:1px solid #CFD8DC;color:#333333;">Проводит ток, может корродировать Al, сложное применение</td>
</tr>
</tbody>
</table>
</div>

## Что характеризует устойчивый PDN (Power Distribution Network)?

Цель PDN — обеспечить стабильное и чистое питание для миллиардов транзисторов в широком диапазоне динамики нагрузки. Ключ — достижение target impedance на пути от VRM до транзисторов.

В **RDL fan-out substrate stackup** пиковые токи требуют сверхнизкой импедансной характеристики от DC до GHz:

* **Многоуровневое развязывание:** bulk на плате (НЧ), MLCC на подложке (СЧ), on‑chip (ВЧ).
* **Низкоиндуктивные петли:** тесная связь power↔GND planes.
* **Выделенные и непрерывные power/GND слои:** без split.
* **Оптимизация vias:** параллельные vias для снижения L; размещение decap как можно ближе.

В ATE‑тестировании PDN проверяют, например, по уровню ripple (условно ±3% в worst‑case).

## Как спланировать технологичный RDL fan-out substrate layout

Идеальный на бумаге **RDL fan-out substrate stackup** бессмысленен, если его нельзя надёжно и экономично произвести. Для DFM‑ориентированного layout важно:

1. **Следовать design rules производителя:** min L/S, min microvia, возможности plating, точность выравнивания.
2. **Контроль warpage:** равномерное и симметричное распределение меди.
3. **Надёжность microvia:** контролировать aspect ratio и следовать рекомендациям по stacked/staggered.
4. **Эффективная панелизация:** учитывать panelization ещё на этапе проектирования.

Раннее взаимодействие с HILPCB и получение их **RDL fan-out substrate guide** помогает избежать поздних итераций.

<div style="background-color:#1A237E;color:#FFFFFF;padding:20px;border-radius:10px;margin:20px 0;">
<h3 style="color:#FFFFFF;text-align:center;border-bottom:2px solid #82B1FF;padding-bottom:10px;">Производственные возможности HILPCB для IC Substrate</h3>
<p style="text-align:center;font-size:0.9em;">Наши расширенные возможности позволяют реализовать самые сложные RDL fan-out substrate дизайны.</p>
<table style="width:100%;text-align:center;color:#FFFFFF;border-collapse:collapse;">
<thead style="background-color:#283593;color:#FFFFFF;">
<tr>
<th style="padding:10px;border:1px solid #3F51B5;">Параметр</th>
<th style="padding:10px;border:1px solid #3F51B5;">Возможности</th>
<th style="padding:10px;border:1px solid #3F51B5;">Параметр</th>
<th style="padding:10px;border:1px solid #3F51B5;">Возможности</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:8px;border:1px solid #303F9F;">Макс. число слоёв</td>
<td style="padding:8px;border:1px solid #303F9F;">56 Layers</td>
<td style="padding:8px;border:1px solid #303F9F;">Min line/space</td>
<td style="padding:8px;border:1px solid #303F9F;">15µm / 15µm</td>
</tr>
<tr>
<td style="padding:8px;border:1px solid #303F9F;">Тип базового материала</td>
<td style="padding:8px;border:1px solid #303F9F;">BT, ABF, MIS</td>
<td style="padding:8px;border:1px solid #303F9F;">Мин. лазерное отверстие</td>
<td style="padding:8px;border:1px solid #303F9F;">50µm</td>
</tr>
<tr>
<td style="padding:8px;border:1px solid #303F9F;">Контроль импеданса</td>
<td style="padding:8px;border:1px solid #303F9F;">±5%</td>
<td style="padding:8px;border:1px solid #303F9F;">Макс. толщина</td>
<td style="padding:8px;border:1px solid #303F9F;">6.0mm</td>
</tr>
<tr>
<td style="padding:8px;border:1px solid #303F9F;">Surface finish</td>
<td style="padding:8px;border:1px solid #303F9F;">ENEPIG, OSP, Immersion Sn</td>
<td style="padding:8px;border:1px solid #303F9F;">Сертификации</td>
<td style="padding:8px;border:1px solid #303F9F;">ISO9001, IATF16949, UL</td>
</tr>
</tbody>
</table>
</div>

## Как выполнять RDL fan-out substrate validation для обеспечения надёжности

После завершения дизайна и производства начинается **RDL fan-out substrate validation** (обычно по JEDEC/IPC), включающая:

* **Electrical test (ATE):** open/short/соединяемость по каждому I/O; для HS‑интерфейсов — eye/jitter/BER.
* **Thermal Cycle Test (TCT):** например −55°C…125°C сотни/тысячи циклов; выявляет CTE‑стрессы, трещины microvia, усталость и delamination.
* **HAST/bHAST:** высокотемпературный/влажностный/давление режим для ускорения проникновения влаги; проверка адгезии и коррозии.
* **Mechanical shock & vibration:** имитация ударов/вибраций; прочность BGA и внутренних interconnect.
* **Physical analysis (PA):** cross‑section, dye‑and‑pry, SEM/TEM для определения root cause и улучшения окон процесса.

Успешная **RDL fan-out substrate validation** даёт уверенность в серийном запуске.

## Как ускорить разработку через RDL fan-out substrate quick turn

В конкурентной AI‑среде time‑to‑market решает всё. Классический цикл изготовления подложек может занимать недели, что слишком медленно. **RDL fan-out substrate quick turn** стремится сократить прототипирование и малые серии до нескольких дней.

Ключевые факторы:

* **Стандартизованные материалы/процессы** (предвалидация, наличие на складе).
* **Цифровой front‑end engineering** (автоматизированный DFM/CAM).
* **Выделенный fast‑track** для быстрых заказов.
* **Интегрированная supply chain**.

Quick‑turn от HILPCB в сочетании с [small-batch assembly](https://hilpcb.com/en/products/small-batch-assembly) ускоряет цикл «изготовление → тест → итерация».

<!-- COMPONENT: BlogQuickQuoteInline -->

## Заключение: освоить RDL fan-out substrate stackup — значит освоить будущее AI

**RDL fan-out substrate stackup** — сердце современной AI‑упаковки: это сложная система, объединяющая материаловедение, полупроводниковые процессы, высокочастотную электромагнитку и теплотехнику. От точного **RDL fan-out substrate impedance control** до технологичного **RDL fan-out substrate layout** нужна тесная кооперация между разработкой и производством. Выбор партнёра вроде HILPCB, который поддерживает полный цикл — от **RDL fan-out substrate guide** до **RDL fan-out substrate validation** и **RDL fan-out substrate quick turn** — помогает с самого начала выстроить баланс производительности, стоимости и надёжности.
