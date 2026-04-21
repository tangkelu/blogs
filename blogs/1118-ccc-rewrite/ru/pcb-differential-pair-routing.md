---
title: "Как разводить дифференциальные пары на PCB: практические правила по импедансу, опорной плоскости, skew и структурам via"
description: "Прямой ответ о целевом импедансе, непрерывности опорной плоскости, симметрии, компенсации длины, via stub и производственной валидации, которые нужно проверять в первую очередь."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["Differential pair routing", "High-speed PCB", "PCB layout", "Signal integrity", "Controlled impedance", "PCB stackup"]
---

# Как разводить дифференциальные пары на PCB: практические правила по импедансу, опорной плоскости, skew и структурам via

- **Сначала нужно фиксировать не абсолютную equal length, а то, под какой стандарт или datasheet target вообще проектируется пара.** Для PTN3222 eUSB2 NXP задает **85 ohm differential impedance**, а AN13335 для automotive Ethernet маршрутизирует MDI как **100 ohm** edge-coupled microstrip или stripline.
- **Симметрия важнее, чем просто маленький зазор между линиями.** Intel AN528 прямо указывает, что обе линии должны электрически выглядеть одинаково, иначе появляется differential-to-common-mode conversion.
- **Непрерывность reference plane и переходы между слоями часто ломают канал раньше, чем основной прямой участок.**
- **Serpentine tuning, anti-pad и via stub нельзя применять как шаблон по умолчанию.**
- **Серийная годность дифференциальной пары появляется только тогда, когда stackup, tolerance, breakout и validation определены вместе.**

> **Quick Answer**  
> Суть routing дифференциальной пары на PCB в том, чтобы сохранить симметричную среду распространения на реальном stackup, с реальной толщиной меди и реальными переходными структурами. Сначала фиксируют target impedance и skew budget, потом контролируют same-layer routing, непрерывную reference plane, симметричные vias и аккуратную компенсацию длины, а затем проверяют изготовленный результат через coupon, TDR или системный тест.

## Содержание

- [Что сначала проверять в routing дифференциальных пар PCB?](#overview)
- [Сводная таблица ключевых правил и параметров](#rules)
- [Почему дифференциальную пару нужно сначала определять через стандарт и stackup?](#standards-stackup)
- [Почему symmetry, skew и serpentine tuning так часто используют неправильно?](#symmetry-skew)
- [Почему reference plane, layer transition и via stub являются зонами высокого риска?](#planes-vias)
- [Как валидировать routing до производства?](#validation)
- [Следующие шаги с HILPCB](#next-steps)
- [Часто задаваемые вопросы (FAQ)](#faq)
- [Открытые источники](#references)
- [Информация об авторе и проверке](#author)

<a id="overview"></a>
## Что сначала проверять в routing дифференциальных пар PCB?

Начинать нужно с **целевого импеданса интерфейса, stackup, опорной плоскости, симметрии и стратегии перехода между слоями**.

Это не значит "просто провести две параллельные линии" и не значит "сначала закончить layout, потом попросить фабрику посчитать импеданс". Разные протоколы, PHY и connectors требуют разных правил. NXP AN13462 задает для eUSB2 **85 ohm differential impedance** и запрещает high-speed pair пересекать plane split. NXP AN13335 задает для automotive Ethernet MDI **100 ohm** differential routing и ограничивает mismatch между connector и choke до **1 mm**. Intel 82566 добавляет для gigabit Ethernet **100 ohm differential impedance (±20%)** и pair mismatch менее **50 mil**.

Значит, сначала нужно подтвердить:

1. **Требует ли интерфейс 85, 90, 95 или 100 ohm differential**
2. **Откуда берется допустимый intra-pair skew budget**
3. **Идет ли трасса как microstrip или stripline и остается ли reference plane непрерывной**
4. **Разрешены ли переходы между слоями и как будут обработаны return current и stubs**
5. **Способен ли производитель стабильно выдержать такую геометрию в заданном stackup**

<a id="rules"></a>
## Сводная таблица ключевых правил и параметров

| Правило / параметр | Метод | Почему это важно | Как проверить | Что будет, если игнорировать |
|---|---|---|---|---|
| Target impedance | Сначала брать из стандарта или datasheet | Не все дифференциальные пары равны 100 ohm | Standard, datasheet, stackup review | Ширина и зазор изначально неверны |
| Symmetry | Держать одинаковыми сечение, reference environment и transitions | Асимметрия вызывает mode conversion | Layout review, 3D review | Больше common-mode noise |
| Same-layer routing | По возможности вести всю пару на одном слое | Переходы добавляют discontinuity | Post-route review, via count | Больше skew и reflection |
| Reference plane | Держать ее непрерывной и близкой | Plane split ломает return path | Plane review | Хуже EMI и mode conversion |
| Length compensation | Делать только по реальному budget и рядом с mismatch point | Плохой serpentine создает impedance ripple | Skew review, TDR, simulation | Компенсация сама создает проблему |
| Via / stub | Минимизировать vias; при переходе использовать симметричные signal via + GND via | Via discontinuity - типичный high-speed risk | TDR, cross-section, backdrill review | Local reflection, ISI, обход return current |

<a id="standards-stackup"></a>
## Почему дифференциальную пару нужно сначала определять через стандарт и stackup?

Вывод: **target impedance и геометрия не являются универсальным шаблоном; они получаются из требований интерфейса и реального производственного stackup.**

Документы NXP и Intel это показывают прямо. Для eUSB2 задано **85 ohm**, для automotive Ethernet MDI - **100 ohm**, и Intel true differential I/O тоже работает в логике **100 ohm**. Поэтому рабочий порядок обычно такой:

1. **Зафиксировать импеданс из стандарта, datasheet или reference design**
2. **Выбрать microstrip или stripline с учетом loss, connector и EMI**
3. **Согласовать с производителем материалы, thickness dielectric, copper thickness и process compensation**
4. **И только потом записать width, spacing и tolerance в layout rules**

<a id="symmetry-skew"></a>
## Почему symmetry, skew и serpentine tuning так часто используют неправильно?

Вывод: **потому что многие команды принимают equal length за признак правильной разводки, игнорируя structural symmetry и локальные изменения coupling.**

Intel AN528 требует для идеальной дифференциальной пары электрического равенства двух линий и skew, максимально близкого к нулю. Из этого следует:

- **Symmetry - это не только длина, но и сечение, dielectric, nearby copper и transitions**
- **Skew связан с изменениями reference environment**
- **Плохо размещенный serpentine может иметь худший импеданс, чем основная линия**

Intel AN875 дополнительно показывает, что trombone compensation создает loosely coupled zones и изменяет delay per unit length. NXP поэтому рекомендует делать length tuning рядом с местом реального mismatch.

<a id="planes-vias"></a>
## Почему reference plane, layer transition и via stub являются зонами высокого риска?

Вывод: **как только пара меняет слой, пересекает split или оставляет stub, первый риск обычно возникает в return path и локальной discontinuity.**

NXP запрещает plane splits на high-speed differential path и рекомендует одинаковый слой, минимум vias и отсутствие лишних stubs. Intel добавляет:

- Остаток via barrel работает как capacitive stub
- При смене слоя return current нужны nearby GND vias
- Структура vias на обеих линиях пары должна быть симметричной

Типичные high-risk зоны:

1. **Корень BGA breakout**
2. **Connector launch**
3. **Области AC-coupling capacitors и common-mode parts**
4. **Layer-transition vias и anti-pad zones**
5. **Необработанные through-via stubs в толстых платах**

<a id="validation"></a>
## Как валидировать routing до производства?

Вывод: **ценная validation доказывает не только то, что в CAD пара разведена как pair, а то, что после производства сохраняются и геометрия, и системное поведение.**

| Пункт валидации | На какой вопрос отвечает | Что наблюдать |
|---|---|---|
| Stackup / impedance review | Соответствует ли target geometry реальной производимости | Width, spacing, copper, dielectric, tolerance |
| Coupon / TDR | Близки ли реальные impedance и transitions к target | Impedance plateau, local discontinuity, via effect |
| Cross-section | Сместили ли ламинация и травление структуру | Real trace width, copper, dielectric, anti-pad |
| System test | Здорова ли пара с реальными devices и connectors | Eye diagram, link training, BER, EMI |
| Multi-board comparison | Риск идет от design или от build variation | Межплатный разброс, lot consistency |

<a id="next-steps"></a>
## Следующие шаги с HILPCB

- Сначала закрыть stackup, layers и reference strategy через [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb) и [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb).
- Использовать [Impedance Calculator](https://hilpcb.com/en/tools/impedance-calculator/) до начала routing.
- При плотном breakout параллельно проверить окно fanout и via structures для [HDI PCB](https://hilpcb.com/en/products/hdi-pcb).
- Готовые stackup, impedance table, critical diff pairs и validation method передавать сразу в [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/) или [Quote / RFQ](https://hilpcb.com/en/quote/).

<a id="faq"></a>
## Часто задаваемые вопросы (FAQ)

<!-- faq:start -->

### Дифференциальные пары по умолчанию всегда делают на 100 ohm?

Нет. Например, для eUSB2 используется 85 ohm, а для многих Ethernet и high-speed I/O - 100 ohm.

### Достаточно ли просто equal length?

Нет. Без электрической симметрии reference plane, nearby copper, vias и anti-pads возможна mode conversion даже при равной длине.

### Дифференциальной паре нельзя менять слой?

Можно, но как можно реже. Каждый переход нужно проектировать как единую структуру с signal via, GND via, anti-pad и return path.

### Удобно ли делать весь serpentine в одном месте?

Обычно нет. Length compensation должна быть ближе к месту mismatch и не должна сама становиться новой discontinuity.

### Почему plane split опасен даже для дифференциальной пары?

Потому что дифференциальная пара не работает отдельно от reference plane. Split меняет return path и усиливает common-mode noise.

<!-- faq:end -->

<a id="references"></a>
## Открытые источники

1. [Intel AN 528: PCB Dielectric Material Selection and Fiber Weave Effect on High-Speed Channel Routing](https://cdrdv2-public.intel.com/654621/an528.pdf)  
   Подтверждает выводы о symmetry, низком skew и влиянии fiber weave.

2. [Intel AN 875: P/N De-skew Strategy on Differential Pairs](https://www.intel.com/content/www/us/en/docs/programmable/683262/current/p-n-de-skew-strategy-on-differential-pairs.html)  
   Подтверждает риск impedance ripple и mode conversion при trombone compensation.

3. [Intel AN 958: Via Discontinuity](https://www.intel.com/content/www/us/en/docs/programmable/683073/current/via-discontinuity.html)  
   Подтверждает обсуждение via stub, симметричных signal vias и GND vias для return current.

4. [Intel 82566 Layout Checklist](https://www.intel.com/content/dam/doc/design-guide/82566-gbe-layout-checklist-ver-1-0.pdf)  
   Подтверждает production checklist по 100 ohm, pair mismatch, расстоянию до GND vias и avoidance of stubs.

5. [NXP AN13462 PTN3222 Layout Guidelines](https://www.nxp.com/docs/en/application-note/AN13462.pdf)  
   Подтверждает требования eUSB2 к 85 ohm, symmetry, matching, avoidance of plane split и via reduction.

6. [NXP AN13335 PCB Design Guidelines for Automotive Ethernet](https://www.nxp.com/docs/en/application-note/AN13335.pdf)  
   Подтверждает контекст 100 ohm MDI, ground symmetry и common-mode risk.

7. [Intel Agilex 5 True Differential I/O Interface PCB Routing Guidelines](https://www.intel.com/content/www/us/en/docs/programmable/821801/current/true-differential-i-o-interface-pcb.html)  
   Подтверждает контекст 100 ohm и уместность backdrill для уменьшения stub effects.

<a id="author"></a>
## Информация об авторе и проверке

- Автор: команда контента HILPCB по high-speed interconnect и SI
- Техническая проверка: команды PCB process, signal integrity и connector engineering
- Последнее обновление: 2025-11-18
