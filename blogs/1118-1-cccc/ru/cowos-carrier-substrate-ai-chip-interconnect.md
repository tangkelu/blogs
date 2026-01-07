---
title: "CoWoS carrier substrate: Packaging, PDN и high-speed interconnect для AI chiplet систем"
description: "Подробный разбор CoWoS carrier substrate: SI/PI, тепловой дизайн, ограничения routing/stack-up, DFM и надежность для решений AI chip interconnect и substrate PCB."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 8
tags: ["CoWoS carrier substrate", "CoWoS carrier substrate layout", "CoWoS carrier substrate routing", "data-center CoWoS carrier substrate", "CoWoS carrier substrate checklist", "CoWoS carrier substrate impedance control"]
---
С взрывным ростом AI и HPC спрос на вычисления растет экспоненциально. Чтобы преодолеть физические ограничения Moore’s Law, индустрия переходит к гетерогенной интеграции на базе Chiplet и advanced packaging 2.5D/3D. Среди решений CoWoS (Chip-on-Wafer-on-Substrate) от TSMC стал индустриальным ориентиром для топовых AI accelerators (например, NVIDIA H100/B200). В этой сложной архитектуре **CoWoS carrier substrate** — ключевой мост между silicon и внешним миром: качество design и manufacturing напрямую определяет производительность, энергопотребление и надежность.

Этот substrate — не «обычная плата», а микро‑система, где одновременно должны работать high-speed interconnect, стабильный PDN и эффективные тепловые пути. Он несет дорогие AI SoC и HBM stacks и обязан обеспечивать почти идеальную передачу сигнала и питания через десятки тысяч микронных соединений. Малейшая ошибка или дефект процесса может привести к отказу всего дорогостоящего модуля. Поэтому понимание ограничений и практик **CoWoS carrier substrate** критично для команд, создающих AI‑hardware. Highleap PCB Factory (HILPCB), имея опыт в advanced interconnect, предлагает решения IC substrate, помогая клиентам справляться с этими вызовами.

## Какие функции выполняет CoWoS substrate и как он устроен?

Чтобы понять роль substrate, важно увидеть его место в 2.5D упаковке. CoWoS использует Silicon Interposer для высокоплотной боковой интеграции нескольких dies (SoC и HBM). Но такой interposer нельзя напрямую припаять к обычной PCB motherboard: он большой и имеет сильно отличный CTE.

Здесь и нужен **CoWoS carrier substrate** — незаменимый мост, который выполняет три основные задачи:

1.  **Механическая опора и буфер напряжений:** substrate обеспечивает жесткую платформу и как промежуточный слой снижает mismatch между Silicon Interposer (CTE ≈ 2.6 ppm/°C) и application PCB (CTE ≈ 17 ppm/°C), защищая микросоединения от трещин при thermal cycling.

2.  **Fan‑out сигнала (RDL):** pitch Micro-bump на interposer очень мал (40–50μm), а pitch BGA balls под substrate намного больше (0.8–1.0mm). Внутренние тонкие слои RDL выполняют «расфасовку» сигнала с μm‑шага на mm‑шаг для внешней PCB.

3.  **Питание и отвод тепла:** AI chip потребляет огромный ток; substrate должен построить low‑impedance PDN от BGA до Micro-bumps и обеспечить тепловые каналы (Thermal Vias).

По структуре типичный CoWoS substrate — высокоплотный Build-up на материалах уровня ABF (Ajinomoto Build-up Film). Layer count часто 8–16 (и выше). Плотные microvias, fine routing и большие power/ground planes — вершина производства [IC Substrate PCB](https://hilpcb.com/en/products/ic-substrate-pcb).

## Как справляться с SI‑вызовами из-за HBM3/3e?

HBM — стандарт для AI accelerators. У HBM3/3e полоса на один stack превышает 1.2TB/s: тысячи линий работают параллельно на высокой частоте. Эти сигналы идут от HBM к interposer, затем через **CoWoS carrier substrate** к SoC. Поэтому Signal Integrity (SI) — критична.

Ключевые проблемы SI:

*   **Insertion Loss:** затухание; более низкие Dk/Df снижают потери.
*   **Reflection:** дискретности импеданса вызывают отражения и искажения.
*   **Crosstalk:** связь между соседними линиями добавляет шум.

Хороший **CoWoS carrier substrate layout** строится на строгих правилах:

Первое: **CoWoS carrier substrate impedance control** как базовый уровень. Высокоскоростные трассы должны быть линиями с импедансом 50Ω (или по спецификации интерфейса). Нужны точные расчеты ширины, толщины диэлектрика и расстояния до reference plane. Инструменты вроде онлайн impedance calculator от HILPCB помогают на старте.

Второе: length matching и минимизация длины. HBM — параллельный широкий bus, где DQ и DQS требуют очень малого mismatch, чтобы избежать skew. Путь BGA → interposer тоже должен быть максимально коротким.

Третье: управление crosstalk. В плотных областях увеличивают spacing, добавляют ground shields и оптимизируют stack‑up. Stripline между двумя ground planes дает сильную экранировку и важна для **CoWoS carrier substrate routing**.

<div style="background-color:#F5F7FA; padding: 20px; border-radius: 8px; margin: 30px 0;">
<h3 style="color:#000000; border-bottom: 3px solid #64B5F6; padding-bottom: 10px;">Сдвиг SI‑требований HBM (уровень substrate)</h3>
<table style="width:100%; border-collapse: collapse; text-align:center; color:#000000;">
<thead style="background-color:#F5F5F5; color:#000000;">
<tr>
<th style="padding:12px; border: 1px solid #ddd;">Показатель</th>
<th style="padding:12px; border: 1px solid #ddd;">HBM2e</th>
<th style="padding:12px; border: 1px solid #ddd;">HBM3/3e</th>
<th style="padding:12px; border: 1px solid #ddd;">Влияние на CoWoS substrate</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:12px; border: 1px solid #ddd;">Скорость на pin</td>
<td style="padding:12px; border: 1px solid #ddd;">~3.6 Gbps</td>
<td style="padding:12px; border: 1px solid #ddd;">~9.0 Gbps+</td>
<td style="padding:12px; border: 1px solid #ddd; color:#1E3A8A;">Более строгие требования к loss материала и точности импеданса</td>
</tr>
<tr>
<td style="padding:12px; border: 1px solid #ddd;">Ширина bus</td>
<td style="padding:12px; border: 1px solid #ddd;">1024-bit</td>
<td style="padding:12px; border: 1px solid #ddd;">1024-bit</td>
<td style="padding:12px; border: 1px solid #ddd;">Очень высокая routing density; сложнее crosstalk control</td>
</tr>
<tr>
<td style="padding:12px; border: 1px solid #ddd;">Допуск импеданса</td>
<td style="padding:12px; border: 1px solid #ddd;">±10%</td>
<td style="padding:12px; border: 1px solid #ddd;">±7% или жестче</td>
<td style="padding:12px; border: 1px solid #ddd; color:#1E3A8A;">Нужны более продвинутые процессы и tighter control</td>
</tr>
<tr>
<td style="padding:12px; border: 1px solid #ddd;">Бюджет insertion loss канала</td>
<td style="padding:12px; border: 1px solid #ddd;">Относительно мягкий</td>
<td style="padding:12px; border: 1px solid #ddd;">Крайне жесткий</td>
<td style="padding:12px; border: 1px solid #ddd;">Ultra low‑loss материалы (например ABF) становятся обязательными</td>
</tr>
</tbody>
</table>
</div>

## Почему PDN критичен для AI chip?

Если SI — это «магистраль» данных, то Power Integrity (PI) — «фундамент». При параллельных вычислениях токи могут резко изменяться (высокий di/dt). Плохой PDN приводит к IR Drop и Ground Bounce и может вызвать деградацию производительности или сбой системы.

Цель PDN для **CoWoS carrier substrate** — обеспечить путь питания с крайне низким импедансом от BGA до Micro-bumps во всем диапазоне частот:

*   **Low‑impedance planes:** выделить достаточное число слоев под power/ground и держать их максимально непрерывными.
*   **Decap стратегия:** большие Decap рядом с BGA для low‑freq, маленькие рядом с die для high‑freq; оптимизация через PI simulation.
*   **Минимизация loop inductance:** размещать power/ground vias ближе друг к другу, особенно важно для `data-center CoWoS carrier substrate`.

Для `data-center CoWoS carrier substrate` с мощностью 1000W+ PDN становится и тепловой задачей: большие токи дают Joule heating в меди, поэтому PDN и thermal design должны быть связаны.

## Какие thermal стратегии применяют в CoWoS substrate?

Thermal management — одна из самых сложных задач AI packaging. 1000W+ TDP на небольшой площади означает экстремальный heat flux. **CoWoS carrier substrate** — важный путь теплопередачи и влияет на peak temperature и надежность.

Эффективная стратегия многопутевая:

1.  **Основной путь (вверх):** через die, TIM и heat spreader (lid) в внешнее охлаждение.
2.  **Вторичный путь (вниз):** часть тепла идет через Micro-bumps и interposer в **CoWoS carrier substrate**, затем через BGA — в system board; это помогает снизить температуру HBM.

Оптимизации на уровне substrate:

*   **Thermal Vias:** плотные, заполненные via под die, которые быстро проводят тепло вниз.
*   **Более теплопроводные материалы:** диэлектрики и copper foils с лучшей проводимостью.
*   **Оптимизация copper planes:** сохранять медь для выравнивания температуры (в рамках электрических ограничений).
*   **Co‑simulation:** thermal co‑simulation chip‑package‑substrate‑system для поиска hot spots и подбора via‑матрицы.

<div style="background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); color: #ffffff; padding: 40px 30px; margin: 30px 0; border-radius: 24px; font-family: system-ui, -apple-system, sans-serif; border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);">
<h3 style="text-align: center; color: #a78bfa; margin: 0 0 10px 0; font-size: 1.85em; font-weight: 800; letter-spacing: 0.5px;">🛠️ CoWoS substrate: engineering sign‑off checklist</h3>
<p style="text-align: center; color: rgba(255, 255, 255, 0.6); font-size: 1.05em; margin-bottom: 40px; font-weight: 500;">Проверка физограничений на уровне системы для 2.5D high-density interconnect packaging</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px;">
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-left: 6px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">01. SI и частотная область</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Проверка:</strong> допуск diff‑импеданса ≤ ±5%? для 112G/224G выполнена симуляция **CoWoS carrier substrate impedance control**? S‑parameters (IL/RL) имеют margin выше 28GHz?</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-left: 6px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">02. PI и динамика PDN</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Проверка:</strong> Target Impedance PDN соответствует экстремальным transient current? индуктивность монтажа Decap минимизирована через **ESR/ESL modeling**?</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-left: 6px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">03. Heat flux и тепловая симуляция</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Проверка:</strong> покрытие матрицы Thermal Via достаточно для 500W+? выполнена **CFD thermal-flow simulation** для предотвращения hot spots и throttling?</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-left: 6px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">04. DFM и управление механическим stress</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Проверка:</strong> min L/S в пределах процесса поставщика? stack‑up имеет реальную <strong>зеркальную симметрию</strong> для контроля Warpage?</p>
</div>
</div>
<div style="margin-top: 35px; padding: 25px; background: rgba(139, 92, 246, 0.1); border-radius: 16px; border-right: 8px solid #8b5cf6; font-size: 0.95em; line-height: 1.7; color: #ddd6fe;">
💡 <strong>Insight HILPCB:</strong> для выбора материалов CoWoS <strong>CTE matching</strong> — линия жизни надежности. Так как substrate несет Silicon Interposer, выбирайте package-grade материалы с высоким модулем и низким CTE (ABF или advanced BT), чтобы уменьшить механический stress на Micro-bumps при thermal cycling.
</div>
</div>

## Какие производственные ограничения задают правила для stack-up и routing?

Теоретически идеальный дизайн должен соответствовать реальным ограничениям производства. **CoWoS carrier substrate** — вершина технологий [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) и IC substrate, поэтому DFM правила здесь очень жесткие.

Ключевые ограничения:

*   **Fine line:** RDL требует очень малого line/space (10μm/10μm или меньше).
*   **Microvia:** лазерные microvias; их диаметр, pad size и stacking (Stacked vs. Staggered) ограничены процессом. Stacked microvias экономят место, но требуют точного выравнивания и via‑fill, влияя на yield и reliability.
*   **Warpage:** большие substrates (100mm x 100mm+) склонны к warpage в thermal процессах; stack‑up должен быть симметричным (распределение меди и диэлектрика).
*   **Handling материалов:** ABF чувствителен к температуре, влажности и чистоте.

Успешная стратегия **CoWoS carrier substrate routing** выполняет электрические требования и учитывает bottlenecks производства, что требует раннего взаимодействия с производителем вроде HILPCB. DFM‑команда помогает выявлять риски и оптимизировать **CoWoS carrier substrate layout** под баланс performance/cost/yield.

## Как обеспечить долгосрочную надежность?

Для data-center AI servers 7x24 надежность критична. Отказ **CoWoS carrier substrate** — катастрофа. Риски:

*   **Термо‑механический stress:** mismatch CTE и thermal cycling приводят к усталости соединений и трещинам.
*   **Microvia reliability:** interface cracks и opens.
*   **Electromigration:** при высокой current density проводники истончаются со временем.

Нужна дисциплина по IPC/JEDEC: проверенные материалы, минимизация stress concentrators и квалификационные тесты (TCT, HAST, drop). Полная **CoWoS carrier substrate checklist** должна включать эти проверки.

<div style="background-color:#1A237E; color: #FFFFFF; padding: 20px; border-radius: 8px; margin: 30px 0;">
<h3 style="color:#FFFFFF; border-bottom: 2px solid #90CAF9; padding-bottom: 10px;">Матрица возможностей HILPCB (advanced IC substrate)</h3>
<table style="width:100%; border-collapse: collapse; text-align:center; color:#FFFFFF;">
<thead style="background-color:rgba(255, 255, 255, 0.1); color:#FFFFFF;">
<tr>
<th style="padding:12px; border: 1px solid #424242;">Параметр</th>
<th style="padding:12px; border: 1px solid #424242;">Возможность HILPCB</th>
<th style="padding:12px; border: 1px solid #424242;">Значение для CoWoS</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:12px; border: 1px solid #424242;">Макс. число layers</td>
<td style="padding:12px; border: 1px solid #424242;">До 56 layers</td>
<td style="padding:12px; border: 1px solid #424242;">Сложный PDN и high‑density routing</td>
</tr>
<tr>
<td style="padding:12px; border: 1px solid #424242;">Min line/space</td>
<td style="padding:12px; border: 1px solid #424242;">8μm / 8μm</td>
<td style="padding:12px; border: 1px solid #424242;">Ultra‑dense RDL и трассировка HBM интерфейса</td>
</tr>
<tr>
<td style="padding:12px; border: 1px solid #424242;">Диаметр laser microvia</td>
<td style="padding:12px; border: 1px solid #424242;">Min 50μm</td>
<td style="padding:12px; border: 1px solid #424242;">Высокоплотные межслойные соединения</td>
</tr>
<tr>
<td style="padding:12px; border: 1px solid #424242;">Точность impedance control</td>
<td style="padding:12px; border: 1px solid #424242;">±5%</td>
<td style="padding:12px; border: 1px solid #424242;">Поддержка **CoWoS carrier substrate impedance control**</td>
</tr>
<tr>
<td style="padding:12px; border: 1px solid #424242;">Core материалы</td>
<td style="padding:12px; border: 1px solid #424242;">ABF / BT / Low-Loss Materials</td>
<td style="padding:12px; border: 1px solid #424242;">Отличные high-speed и thermal свойства</td>
</tr>
</tbody>
</table>
</div>

## Выбор поставщика: что оценивать?

Учитывая критичность **CoWoS carrier substrate**, выбор партнера определяет успех:

1.  **Техническая глубина:** опыт IC substrate и ABF build-up? понимание SI/PI уровня [High-speed PCB](https://hilpcb.com/en/products/high-speed-pcb)? кейсы `data-center CoWoS carrier substrate`?
2.  **Process capability:** LDI, vacuum etching, точность выравнивания, допуски импеданса и управление yield.
3.  **Quality system:** ISO 9001, IATF 16949, AOI, X-Ray, cross‑section.
4.  **Supply chain:** ABF часто дефицитен; нужна устойчивость.
5.  **Сервис и ко‑инжиниринг:** DFM, симуляции и услуги [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly).

HILPCB с более чем 10‑летним опытом high‑end PCB и IC substrate и пониманием потребностей AI/HPC — подходящий партнер для next‑gen AI hardware.

<!-- COMPONENT: BlogQuickQuoteInline -->

## Заключение

**CoWoS carrier substrate** — это не просто “connection board”, а фундамент современной AI compute. От multi‑TB/s сигналов HBM3/3e до чистого питания для 1000W‑класса silicon и устойчивости к thermal cycling — каждый аспект находится на грани технологий.

Высокопроизводительный и надежный **CoWoS carrier substrate** требует междисциплинарных компетенций SI, PI, термики, материалов и precision manufacturing, а также тесной работы с партнером, который обладает реальными capability и строгим quality control. С ростом спроса на advanced packaging стратегическая важность **CoWoS carrier substrate** будет только увеличиваться.

