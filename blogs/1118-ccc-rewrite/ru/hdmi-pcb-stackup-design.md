---
title: "Как задавать HDMI PCB stackup: 100 ohm differential, loss budget и connector transitions"
description: "Прямой ответ о целевой версии, 100 ohm differential impedance, reference planes, material loss и connector transitions, которые нужно оценивать в первую очередь при проектировании HDMI PCB stackup."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["HDMI PCB", "PCB stackup design", "Controlled impedance", "High-speed PCB", "TMDS routing", "FRL design"]
---

# Как задавать HDMI PCB stackup: 100 ohm differential, loss budget и connector transitions

- **Смысл HDMI stackup не в количестве слоев, а в том, сколько производственного запаса у линка остается на целевой скорости.**
- **Базовая цель по-прежнему 100 ohm differential, но реальная сложность в том, удержит ли ее производство.**
- **Непрерывность reference plane и launch transitions часто съедают margin раньше, чем прямые участки трассы.**
- **Не каждой HDMI-плате нужен premium low-loss material, но и обычный FR-4 подходит не для всех проектов.**
- **Validation должна опираться на реальные fabrication data.**

> **Quick Answer**  
> Цель HDMI PCB stackup design состоит в том, чтобы 100 ohm differential pairs, continuous reference planes, low-loss geometry и connector transitions одновременно работали на целевой версии и lane rate. Stackup действительно хорош только тогда, когда после lamination, etching и assembly link margin все еще сохраняется.

## Содержание

- [Что сначала проверять в HDMI PCB stackup design?](#overview)
- [Сводная таблица ключевых правил и параметров](#rules)
- [Почему HDMI stackup нужно начинать с loss budget по скорости и длине?](#loss-budget)
- [Почему 100 ohm differential impedance должна быть привязана к реальному производству?](#impedance)
- [Почему connectors, layer changes и stubs опаснее прямых трасс?](#transitions)
- [Как валидировать HDMI stackup перед производством?](#validation)
- [Следующие шаги с HILPCB](#next-steps)
- [Часто задаваемые вопросы (FAQ)](#faq)
- [Открытые источники](#references)
- [Информация об авторе и проверке](#author)

<a id="overview"></a>
## Что сначала проверять в HDMI PCB stackup design?

Начинать нужно с **целевой версии HDMI, lane rate, длины трассы на плате, reference planes и connector transitions**.

Недостаточно просто применить стандартные high-speed rules к differential pair. HDMI 2.1b поднимает общую пропускную способность до **48Gbps**, а TI для HDMI 2.1 FRL указывает lane rates **3/6/8/10/12Gbps**. Поэтому первые вопросы такие:

1. **Это действительно HDMI 2.0 TMDS или уже HDMI 2.1 FRL?**
2. **Заставляют ли длина трассы и положение коннектора использовать layer changes или длинные stubs?**
3. **Достаточен ли обычный FR-4 или уже нужен lower-loss material system?**
4. **Остается ли reference plane непрерывной по всему пути?**
5. **Может ли фабрика стабильно делать целевую 100 ohm differential geometry?**

<a id="rules"></a>
## Сводная таблица ключевых правил и параметров

| Правило / параметр | Как оценивать | Почему это важно | Как проверять | Что будет, если игнорировать |
|---|---|---|---|---|
| Версия HDMI и скорость | Четко разделять TMDS до 6Gbps и FRL до 12Gbps/lane | Скорость задает loss budget и material window | Спецификация, datasheet, protocol settings | Неверный stackup, зажатая eye и EMI margin |
| Differential impedance | Держать HDMI pairs около 100 ohm differential | Базовое требование к transmission structure | Impedance calculation, coupon, TDR | Больше отражений и уже eye opening |
| Reference plane | Держать pair рядом с continuous reference plane по всему пути | Continuity return path влияет на SI и EMI | Layout review, проверка layer changes | Больше mode conversion и radiation risk |
| Материал и copper | Выбирать по длине, скорости и roughness меди вместе | Потери и production spread растут с частотой | Stackup review, microsection, insertion-loss test | Prototype работает, серия становится критичной |
| Connector / via transition | Launch, anti-pad, stub и layer changes оценивать отдельно | Переходы часто ломаются раньше прямых сегментов | 3D modeling, TDR, measured waveform | Black screen, artifacts, intermittent instability |
| Manufacturing consistency | Design values должны соответствовать реальной geometry фабрики | Lamination и etching сдвигают размеры | Microsection, coupon, lot comparison | Margin плавает от lot к lot |

<div style="background: linear-gradient(135deg, #eef4fb 0%, #eef7f5 100%); border: 1px solid #d6e0ea; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4b7aa7; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #365b7e; font-weight: 700;">Version Sets the Stackup</div>
      <div style="margin-top: 8px; color: #223544;">HDMI 2.0 и HDMI 2.1 не должны жить на одной расплывчатой логике stackup. Сначала определяется lane rate, затем материал, слои и length budget.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4f7d6c; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #395d51; font-weight: 700;">100 Ohm Must Survive Fabrication</div>
      <div style="margin-top: 8px; color: #22352e;">100 ohm - это не только software target value. Это значение должно сохраняться после lamination, etching и реальной copper surface geometry.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #8a6a4a; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6a523a; font-weight: 700;">Launch Regions Kill Margin Fast</div>
      <div style="margin-top: 8px; color: #3a2e24;">На HDMI-платах margin часто сначала теряется в connector launch, layer changes и stubs, а не в длинных прямых сегментах.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #8a5d78; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6b4760; font-weight: 700;">Validate the Real Geometry</div>
      <div style="margin-top: 8px; color: #3d2636;">Зрелый HDMI stackup подтверждается coupons, microsections и TDR / insertion-loss data, показывающими, что изготовленная geometry близка к модели.</div>
    </div>
  </div>
</div>

<a id="loss-budget"></a>
## Почему HDMI stackup нужно начинать с loss budget по скорости и длине?

Вывод: **потому что выбор material family и самого stackup определяется реальной lane rate, длиной трассы и числом transitions, а не общими привычками для этого интерфейса.**

HDMI 2.1b поднимает total bandwidth до **48Gbps**. TI указывает для FRL до **12Gbps** на lane и до **6Gbps** для HDMI 2.0b TMDS. Поэтому важны вопросы:

- **Какова длина пути на плате?**
- **Сколько в тракте connectors, ESD, redrivers и layer changes?**
- **Хватает ли еще margin у FR-4?**
- **Не перешел ли проект уже в область, где нужен lower-loss material и более жесткий dielectric control?**

<a id="impedance"></a>
## Почему 100 ohm differential impedance должна быть привязана к реальному производству?

Вывод: **потому что 100 ohm в HDMI - это не абстрактная цель, а физический результат lamination thickness, etch compensation и реальной copper geometry.**

TI в нескольких HDMI-документах явно требует 100 ohm differential. В серии это значение уходит из-за:

- реальной dielectric thickness после lamination
- etched line width вместо нарисованной
- copper roughness
- solder mask, формы reference plane и соседней меди

<a id="transitions"></a>
## Почему connectors, layer changes и stubs опаснее прямых трасс?

Вывод: **потому что прямые HDMI trace segments часто контролируемы, а launch, vias и layer changes намного легче создают local impedance steps, mode conversion и дополнительный loss.**

Отдельно стоит оценивать:

- есть ли continuous reference plane под connector launch
- оптимизированы ли via pad и anti-pad под целевой переход
- помогают ли ground vias замыкать return current при смене слоя
- нужно ли укорачивать или back-drill through-hole stubs
- сохраняется ли симметрия pair после breakout

<a id="validation"></a>
## Как валидировать HDMI stackup перед производством?

Вывод: **полезная HDMI validation доказывает не только наличие 100 ohm pair на чертеже, а то, что изготовленная плата действительно удерживает цель.**

Практичный путь validation обычно включает:

| Validation item | На какой вопрос отвечает | Что наблюдать |
|---|---|---|
| Impedance coupon | Умеет ли фабрика повторяемо делать целевую geometry? | Цель 100 ohm и spread между lots |
| Microsection | Сместили ли lamination и etching структуру? | Dielectric thickness, line width, copper profile |
| TDR или insertion-loss test | Здоровы ли transitions и весь путь? | Local discontinuities, straight vs transition regions |
| Сравнение нескольких плат | Достаточно ли широк process window? | Consistency eye / impedance / loss |
| System-level test | Работает ли stackup с реальными connectors и devices? | Resolution, artifacts, black-screen threshold, EMI |

<a id="next-steps"></a>
## Следующие шаги с HILPCB

- Сначала свести target material, copper foil и направление stackup через [High Speed PCB](https://hilpcb.com/en/products/high-speed-pcb).
- Рано использовать [Impedance Calculator](https://hilpcb.com/en/tools/impedance-calculator/) для оценки geometry под 100 ohm differential.
- Если на плате есть connector breakout, layer changes и более плотный fan-out, одновременно проверить [Multilayer PCB](https://hilpcb.com/en/products/multilayer-pcb) или [HDI PCB](https://hilpcb.com/en/products/hdi-pcb).
- Когда stackup, coupon plan и launch review стабилизированы, их лучше сразу включить в [Quote / RFQ](https://hilpcb.com/en/quote/) или [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/).

<a id="faq"></a>
## Часто задаваемые вопросы (FAQ)

<!-- faq:start -->

### Для каждой HDMI 2.1 платы нужен premium low-loss material?

Не обязательно. Все зависит от реальной lane rate, длины пути и количества transitions.

### Достаточно ли просто нарисовать pair на 100 ohm?

Нет. Реальный результат зависит еще и от lamination, etch compensation, roughness и reference plane.

### Нужен ли непрерывный reference plane для HDMI differential pairs?

Да. Differential routing не отменяет необходимость в стабильном return path.

### Проблемы HDMI чаще возникают в трассе или в переходе коннектора?

Очень часто в connector launch, via layer change или stub.

### Почему нужны coupon или TDR?

Потому что они показывают, соответствует ли изготовленная geometry модели.

<!-- faq:end -->

<a id="references"></a>
## Открытые источники

1. [HDMI 2.1b Specification Overview](https://www.hdmi.org/spec/hdmi2_1/index.aspx)  
   Подтверждает официальный контекст 48Gbps и более высоких resolution / refresh.

2. [TI TMDS1204 Datasheet](https://www.ti.com/lit/ds/symlink/tmds1204.pdf)  
   Подтверждает FRL rates 3/6/8/10/12Gbps.

3. [TI TDP158 Product Page / Datasheet](https://www.ti.com/product/TDP158)  
   Подтверждает контекст HDMI 2.0b / 6Gbps TMDS.

4. [TI TPD12S016 PCB Layout Guidelines for HDMI ESD Protection](https://www.ti.com/lit/an/slla324/slla324.pdf)  
   Подтверждает правила 100 ohm HDMI и необходимость контролировать transitions.

5. [TI HDMI Design Guide](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/138/5684.Texas-Instruments-HDMI-Design-Guide.pdf)  
   Подтверждает совместный review layer stack, controlled impedance, reference planes и vias.

6. [TI Processor Documentation Example: TMDS Differential Signal Traces 100Ω ±10%](https://www.ti.com/lit/ds/sprs870b/sprs870b.pdf)  
   Подтверждает официальную формулировку 100 ohm ±10%.

<a id="author"></a>
## Информация об авторе и проверке

- Автор: HILPCB team по high-speed interface и stackup content
- Техническая проверка: команды PCB process, SI и high-speed connector engineering
- Последнее обновление: 2025-11-18
