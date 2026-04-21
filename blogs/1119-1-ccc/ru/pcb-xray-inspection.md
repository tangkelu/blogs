---
title: "На что на самом деле должна смотреть PCB X-Ray inspection: дело не только в снимках voids"
description: "Практический разбор scope, defect interpretation, sampling logic, process feedback и traceability chain, которые нужно определить заранее для PCB X-Ray inspection."
category: technology
date: "2025-11-19"
featured: true
image: ""
readingTime: 10
tags: ["x-ray inspection", "pcba quality", "bga inspection", "void analysis", "traceability"]
---

# На что на самом деле должна смотреть PCB X-Ray inspection: дело не только в снимках voids

- **Первая задача X-Ray inspection не в том, удалось ли получить картинку скрытого дефекта, а в том, можно ли реально замкнуть качество hidden joints обратно на assembly process, sampling rules и traceability chain.** Публичные заголовки IPC-7095E и IPC-7093 прямо ставят в центр design и assembly process guidance, а это уже означает, что X-Ray нельзя рассматривать только как послесборочный разбор картинки.
- **X-Ray нельзя сводить к одному слову "void".** Для BGA, BTC, QFN, LGA и компонентов с большим bottom pad wetting, bridging, offset, head-in-pillow, consistency joints и распределение voids представляют собой разные категории риска.
- **Самый полезный результат X-Ray - не найти одну плохую плату, а суметь вернуть изображение к stencil design, solder paste, geometry pads, reflow profile и moisture exposure.** Если картинка не возвращается в process, improvement quality идет медленно.
- **Sampling strategy должна быть привязана к риску package, смене lot и стоимости отказа.** Новые packages, новые stencils, новая solder paste или новое окно reflow не должны автоматически наследовать прежнюю плотность sampling.
- **X-Ray images без привязки к lot number, equipment, program и judgment records дают слабую базу для последующей root-cause analysis и customer complaints.**

> **Quick Answer**  
> Суть PCB X-Ray inspection не в том, чтобы получить четкую картинку. Нужно заранее определить, какие packages обязательно проверять, какие hidden-joint risks важны для каждого package family, как findings возвращаются в process и как результат входит в traceability chain. Для BGA-, BTC- и reliability-critical PCBA X-Ray - это инструмент управления процессом, а не только приемочный контроль.

## Содержание

- [Что инженеру нужно проверить сначала в PCB X-Ray inspection?](#overview)
- [Ключевые правила и сводная таблица параметров](#rules)
- [Какие продукты и типы корпусов должны включать X-Ray в routine control?](#scope)
- [Какие defects и сигналы X-Ray должен реально искать?](#defects)
- [Почему главная ценность X-Ray - это process feedback, а не сама картинка?](#process)
- [Почему sampling strategy и traceability chain нужно проектировать вместе?](#sampling)
- [Следующие шаги с HILPCB](#next-steps)
- [FAQ](#faq)
- [Публичные источники](#references)
- [Автор и техническая проверка](#author)

<a id="overview"></a>
## Что инженеру нужно проверить сначала в PCB X-Ray inspection?

Сначала нужно смотреть на **package type, hidden-joint risk, defect interpretation logic, sampling strategy и traceability method**.

Это не просто вопрос "умеет ли машина делать снимок" и не только вопрос "превысил ли void ratio порог". IPC-7095E для BGA и IPC-7093 для Bottom Termination Components включают design и assembly process guidance уже на уровне публичного scope. IPC также в сообщении по J-STD-001J отметил добавленные иллюстрации для bubbles, наблюдаемых в X-Ray images. В совокупности эти публичные факты уже показывают: X-Ray должен работать на design, assembly, inspection и reliability, а не только на одноразовое image-based accept / reject.

Что обычно стоит зафиксировать до pilot:

- **какие packages и какие lots обязаны входить в routine X-Ray control**
- **какие hidden-joint risks критичны для каждой package family**
- **ориентирована ли interpretation на voiding, wetting, bridging, offset или consistency**
- **как меняется sampling density при новых packages, новых process windows и разных уровнях риска**
- **как images, judgments и process data входят в traceability chain**

Для проектов с большим числом hidden joints обычно разумно одновременно рассматривать process windows [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) и [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly), а не позволять inspection strategy и assembly strategy жить отдельно.

<a id="rules"></a>
## Ключевые правила и сводная таблица параметров

| Правило / параметр | Рекомендуемый подход | Почему это важно | Как проверять | Что будет, если проигнорировать |
| --- | --- | --- | --- | --- |
| Scope inspection | Сначала определить, какие package types и какие сценарии отказа требуют X-Ray | High-risk joints не должны ждать field failure, чтобы их проверили | NPI review, package list, quality plan | Критичный риск hidden joint будет пропущен |
| Focus interpretation | Разные packages требуют разного фокуса, а не только voiding | BGA, BTC и QFN не отказывают одинаково | Review изображений first article, package classification | Снимки есть, выводы слабые |
| Process feedback | Каждое изображение должно трассироваться к stencil, paste, pad и reflow | Ценность inspection - в улучшении process | Связать image records с process parameters | Дефекты найдены, но не устранены |
| Sampling strategy | Адаптировать sampling по risk level, process change и condition lot | Жесткий шаблон sampling может скрыть новый риск | План sampling для first article и production | Изменения высокого риска остаются незамеченными |
| Traceability chain | Архивировать image, board ID, program, shift и judgment вместе | Это нужно для failure analysis и complaint handling | Review MES / logs, привязка к lot | Позднее root cause превращается в догадку |
| Coordination design | Рано проверять pad design, via in pad и opening bottom pad | Многие X-Ray findings начинаются еще на стадии layout и package design | DFM review, package check | После сборки assembly window оказывается слишком узким |

<div style="background: linear-gradient(135deg, #eef2f7 0%, #eef6f2 100%); border: 1px solid #dbe2e9; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.86); border-left: 4px solid #64748b; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #4e5e73; font-weight: 700;">Scope</div>
      <div style="margin-top: 8px; color: #27313a;">Сначала нужно определить, какие packages и какие ситуации с lot требуют routine X-Ray. Без scope inspection становится реактивной.</div>
    </div>
    <div style="background: rgba(255,255,255,0.86); border-left: 4px solid #517a8d; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #40616f; font-weight: 700;">Defect</div>
      <div style="margin-top: 8px; color: #25333d;">Разные packages чувствительны к разным defects hidden joint. Voiding, bridging, offset и head-in-pillow нельзя оценивать по одному шаблону.</div>
    </div>
    <div style="background: rgba(255,255,255,0.86); border-left: 4px solid #5e7b65; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #4a6251; font-weight: 700;">Feedback</div>
      <div style="margin-top: 8px; color: #28322b;">Если image нельзя вернуть к stencil, solder paste, pad design и reflow, улучшение yield останется медленным.</div>
    </div>
    <div style="background: rgba(255,255,255,0.86); border-left: 4px solid #8a7650; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6c5d40; font-weight: 700;">Traceability</div>
      <div style="margin-top: 8px; color: #382f24;">Без board ID, lot, program и decision records X-Ray images слабо помогают в customer complaints и failure analysis.</div>
    </div>
  </div>
</div>

<a id="scope"></a>
## Какие продукты и типы корпусов должны включать X-Ray в routine control?

Как правило, **packages со скрытыми соединениями, дорогим rework, зависимостью thermal path от bottom pad или высокой стоимостью field failure лучше всего подходят для routine X-Ray**.

IPC-7095E написан вокруг BGA, а IPC-7093 - вокруг BTC / Bottom Termination Components. Уже это показывает, что такие корпуса плохо подходят для выпуска только по AOI или visual inspection. Практический engineering-вопрос тут не "есть ли у нас X-Ray machine?", а "можем ли мы позволить себе узнать о плохой пайке такого корпуса только на functional test или уже в поле?"

Типичные объекты для routine X-Ray:

- **BGA, CSP и другие hidden-ball packages**
- **QFN, LGA и devices с большими exposed bottom pads**
- **power devices, где важны thermal path и consistency joints**
- **high-layer-count, fine-pitch или dense PCBA с дорогим rework**
- **automotive, medical, industrial-control и communications boards с более высокой требовательностью к reliability**

Если проект уже движется к batch assembly, обычно лучше заранее внести эти packages в pre-control list для [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) или [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly), чем решать после first article, "что стоило бы просветить".

<a id="defects"></a>
## Какие defects и сигналы X-Ray должен реально искать?

Потому что **реальная задача X-Ray не в вопросе "есть ли void?", а в выявлении тех hidden-joint failure modes, которые значимы для данного package**.

BTC и BGA несут разные риски, именно поэтому IPC рассматривает их в разных стандартах. Для BGA более важны проверки wetting, collapse, offset, bridging и рисков типа head-in-pillow. Для BTC, QFN и больших bottom-pad devices фокус чаще идет на distribution joints снизу, location voids, coverage joints и consistency.

Самые полезные наблюдения обычно включают:

- **сформировалась ли у joint разумная непрерывная wetting shape**
- **есть ли bridging или локальные аномальные кластеры скрытых соединений**
- **концентрируются ли voids в критичных thermal или stress regions**
- **есть ли заметный разброс geometry на одинаковом компоненте внутри одного lot**
- **указывает ли локальная anomaly на design, printing или reflow behavior**

Если на плате есть также большие thermal pads, complex power areas или высокая thermal density, полезно рассматривать pad и heat-path structure вместе с [High-Thermal PCB](https://hilpcb.com/en/products/high-thermal-pcb), а не относиться к X-Ray как к чисто post-assembly action.

<a id="process"></a>
## Почему главная ценность X-Ray - это process feedback, а не сама картинка?

Потому что **важный вопрос не в том, что есть одна плохая плата, а в том, почему та же anomaly повторяется**.

IPC-7093 и IPC-7095 - это документы design and assembly process guidance, а не просто атласы картинок. Это означает, что изображение нужно читать вместе со stencil aperture strategy, состоянием solder paste, pad design, via in pad treatment, moisture exposure components и reflow profile. Без этой связки X-Ray может только сказать "здесь есть проблема", но не "почему она повторяется снова и снова".

Какие process factors стоит чаще всего возвращать назад:

- **подходит ли stencil thickness и aperture strategy данному package**
- **стабильны ли type, lot, storage и usage condition solder paste**
- **корректны ли pad design, solder-mask definition и via in pad treatment**
- **соответствует ли reflow profile корпусу и условиям платы**
- **не были ли упущены moisture exposure, warpage или изменение формы package / PCB**

Если проект еще в prototype или pilot, обычно лучше планировать такие feedback loops вместе с [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/), а не превращать X-Ray в отдельный reject report.

<a id="sampling"></a>
## Почему sampling strategy и traceability chain нужно проектировать вместе?

Потому что **управляющая ценность X-Ray зависит от того, когда проверять, сколько проверять и можно ли вернуть результат обратно в process**.

Публичный контекст обновления J-STD-001J уже показывает, что interpretation X-Ray images все более формализуется внутри assembly acceptance practice. На языке engineering это означает, что sampling strategy не может оставаться фиксированным шаблоном. Она должна меняться вместе с package risk, process maturity, process changes и стоимостью отказа.

Более robust подход обычно включает:

1. **Повышать inspection density на первых lots с новыми packages, новыми stencils, новой paste или новыми reflow programs.**
2. **Давать higher priority fine-pitch BGA, большим bottom pads и critical thermal devices.**
3. **Привязывать sampling results к board ID, shift, program, solder-paste lot и equipment settings.**
4. **Заранее определить escalation rules для более плотного sampling или 100% inspection при повторении abnormal patterns.**
5. **Архивировать image judgments вместе с corrective actions, а не отдельно от них.**

Без traceability chain X-Ray images помогают только в текущем решении. С traceability chain они становятся инструментом complaint handling, failure analysis и continuous process improvement. Для проектов, близких к production, обычно лучше сразу прописывать это в [Quote / RFQ](https://hilpcb.com/en/quote/) или ранних quality instructions.

<a id="next-steps"></a>
## Следующие шаги с HILPCB

Если вы вводите BGA, QFN, большие bottom-pad devices или другой проект с большим числом hidden joints, следующий шаг обычно в том, чтобы превратить "inspection" в "process control input":

- Когда главный вопрос - качество assembly hidden joints, сначала включать critical packages и control points в review [SMT Assembly](https://hilpcb.com/en/products/smt-assembly).
- Когда производство PCB, sourcing, placement и test должны быть закрыты как единый процесс, использовать [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) для выравнивания workflow boundaries.
- Когда на плате есть high-heat-density parts или большие exposed thermal pads, пересматривать pad и heat-path design вместе с [High-Thermal PCB](https://hilpcb.com/en/products/high-thermal-pcb).
- Когда package choice, pad design и process window нужно доказать заранее, переносить эти checkpoints сначала в [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/).
- Когда scope, sampling logic, interpretation method и traceability expectations уже определены, переносить полный набор требований в [Quote / RFQ](https://hilpcb.com/en/quote/).

<a id="faq"></a>
## FAQ

<!-- faq:start -->

### X-Ray inspection в основном про процент voids?

A: Нет. Voids - лишь одна категория риска. На многих продуктах wetting, bridging, offset, head-in-pillow, coverage joints и consistency между lots важны не меньше, а иногда больше.

### Какие продукты особенно нуждаются в routine X-Ray?

A: Продукты с большим числом hidden joints, дорогим rework, зависимостью thermal path от bottom pad или высокой требовательностью к reliability - самые сильные кандидаты для routine X-Ray control.

### Почему одного AOI недостаточно?

A: Потому что многие критичные joints находятся под корпусом, где AOI их не видит, а именно эти места часто определяют thermal path и long-term reliability.

### Почему команды могут просматривать много X-Ray images и все равно медленно улучшать process?

A: Частая причина в том, что изображения не связаны со stencil, solder paste, reflow, pad design и lot data. В результате anomalies видны, а root cause не закрывается.

### Что важнее всего зафиксировать до production?

A: Сначала нужно зафиксировать inspection scope, defect-interpretation logic, sampling strategy, escalation triggers и traceability chain. Эти решения влияют на долгосрочное quality control сильнее, чем один результат inspection.

<!-- faq:end -->

<a id="references"></a>
## Публичные источники

1. [IPC-7095E Table of Contents](https://www.ipc.org/TOC/IPC-7095E_toc.pdf)  
   Подтверждает, что IPC-7095E позиционируется как design and assembly process guidance для BGA.

2. [IPC-7093 Table of Contents](https://www.ipc.org/TOC/IPC-7093.pdf)  
   Подтверждает, что IPC-7093 ориентирован на Bottom Termination Components и содержит разделы по X-Ray usage, repair и reliability.

3. [IPC Releases J Revisions to Two Leading Standards for Electronics Assembly](https://www.electronics.org/news-release/ipc-releases-j-revisions-two-leading-standards-electronics-assembly)  
   Подтверждает публичный контекст того, что в J-STD-001J были добавлены иллюстрации, связанные с bubbles в X-Ray images.

<a id="author"></a>
## Автор и техническая проверка

- Автор: контент-команда HILPCB по PCBA quality
- Техническая проверка: инженерная команда по assembly process, inspection и reliability
- Последнее обновление: 2025-11-19
