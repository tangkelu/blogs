---
title: "Как проектировать SMT stencil: что сначала фиксировать в aperture, толщине и окне печати"
description: "Прямой ответ о том, какую логику aperture, выбор толщины, контроль fine-pitch, связку с PCB pads и loop обратной связи производства нужно подтвердить в первую очередь."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 10
tags: ["SMT Stencil Design", "Stencil Design", "Печать паяльной пасты", "SMT Assembly", "PCBA DFM"]
---

# Как проектировать SMT stencil: что сначала фиксировать в aperture, толщине и окне печати

- **Первым нужно фиксировать не только толщину stencil, а то, какие структуры на плате труднее всего печатаются и чаще всего дают bridging или insufficient paste.**
- **Aperture stencil - это не механическая копия pad.**
- **Fine-pitch, центральные thermal pads и BGA не могут жить по одной простой логике.**
- **Многие дефекты, похожие на проблемы placement или reflow, на самом деле происходят из того, что pads PCB, solder mask и stencil никогда не были сведены вместе.**
- **Хороший серийный stencil опирается на SPI, AOI и X-ray feedback, а не только на один успешный пилот.**

> **Quick Answer**  
> Суть SMT stencil design не в выборе одной универсальной толщины, а в согласовании формы aperture, окна release, толщины, условий pad и production feedback вокруг самых критичных структур.

## Содержание

- [Что сначала проверять в SMT stencil design?](#overview)
- [Сводная таблица ключевых правил и параметров](#rules)
- [Почему стратегия aperture на самом деле управляет объемом пасты и release?](#aperture)
- [Почему толщину stencil нужно выбирать от самой чувствительной структуры?](#thickness)
- [Почему stencil нужно оценивать вместе с PCB pads, solder mask и параметрами assembly?](#pcb-dfm)
- [Почему серийному stencil нужна петля обратной связи по данным?](#feedback)
- [Следующие шаги с HILPCB](#next-steps)
- [Часто задаваемые вопросы (FAQ)](#faq)
- [Открытые источники](#references)
- [Информация об авторе и проверке](#author)

<a id="overview"></a>
## Что сначала проверять в SMT stencil design?

Начинать стоит с **самого чувствительного package, геометрии aperture, толщины stencil, условий pad PCB, параметров печати и validation data**.

Обычно сначала нужно понять:

- **Какой package задает самую маленькую aperture**
- **Какие pads требуют специальной обработки**
- **Защищает ли базовая толщина самый критичный компонент**
- **Не ломают ли pad, solder mask и vias окно печати еще до печати**
- **Какие данные пилота должны вернуться в следующую версию stencil**

<a id="rules"></a>
## Сводная таблица ключевых правил и параметров

| Правило / параметр | Метод | Почему это важно | Как проверить | Что будет, если игнорировать |
| --- | --- | --- | --- | --- |
| Найти самый критичный компонент | Сначала найти самую маленькую aperture, pitch и сложный thermal pad | Эти структуры задают предел | Package review, BOM check | Толщина определяется большими деталями |
| Стратегия aperture | Делить по типу package, а не брать 1:1 | Управляет объемом пасты и release | SPI, test print, сравнение дефектов | Bridging, insufficient paste, slump |
| Выбор толщины | Сначала защищать самую чувствительную структуру | Толщина напрямую управляет release window | First article, transfer study | Fine-pitch зоны срываются первыми |
| Связка с PCB | Рассматривать pad, solder mask и via treatment вместе со stencil | Многие дефекты начинаются со стороны PCB | DFM review, Gerber compare | Настройка stencil не лечит причину |
| Спецструктуры | Отдельно оценивать QFN center pad, BGA, PoP и step stencil | Эти зоны теряют контроль быстрее всех | X-ray, SPI, post-reflow appearance | Voids, head-in-pillow, drift |
| Обратная связь по данным | Привязать SPI/AOI/X-ray к ревизии stencil | Иначе серия не сходится | Version history, Pareto | Одни и те же дефекты повторяются |

| Публичное эмпирическое правило | Инженерный смысл |
| --- | --- |
| IPC-7525C: нет одной жесткой нормы для всех stencil | Aperture и толщину нужно оценивать в контексте проекта |
| Indium StencilCoach: прямоугольные aperture часто фильтруют по `W/t > 1.5` | Удобно для раннего скрининга |
| Indium StencilCoach: круглые/квадратные aperture часто фильтруют по `> 0.66` | Особенно полезно для BGA/CSP |

<div style="background: linear-gradient(135deg, #f7f4ef 0%, #f3f8f2 100%); border: 1px solid #e2ddd4; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #8a6448; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6f513b; font-weight: 700;">Aperture Controls Volume</div>
      <div style="margin-top: 8px; color: #382d24;">Aperture одновременно задает объем пасты, путь release и стабильность печати.</div>
    </div>
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #59745f; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #47604c; font-weight: 700;">Thickness Follows The Weakest Link</div>
      <div style="margin-top: 8px; color: #29352c;">Толщина stencil должна сначала защищать самую трудную для печати структуру.</div>
    </div>
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #506d91; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #405978; font-weight: 700;">PCB And Stencil Are Coupled</div>
      <div style="margin-top: 8px; color: #253544;">Без согласования pad, solder mask и vias даже хороший stencil лишь локально компенсирует проблемы.</div>
    </div>
    <div style="background: rgba(255,255,255,0.88); border-left: 4px solid #8a6174; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #714b5e; font-weight: 700;">Data Must Update The Stencil</div>
      <div style="margin-top: 8px; color: #392833;">Если SPI, AOI и X-ray не меняют версию stencil, дефекты возвращаются как будто случайные.</div>
    </div>
  </div>
</div>

<a id="aperture"></a>
## Почему стратегия aperture на самом деле управляет объемом пасты и release?

Вывод: **потому что aperture определяет, как паста выходит из stencil и превращается в контролируемый solder joint.**

Сначала стоит зафиксировать:

- **Нужны ли QFP/QFN участкам уменьшение или особая форма aperture**
- **Попадают ли BGA/CSP зоны в разумное окно area ratio**
- **Нужно ли сегментировать центральный thermal pad**
- **Нужно ли делить устройства на разные aperture families**

<a id="thickness"></a>
## Почему толщину stencil нужно выбирать от самой чувствительной структуры?

Вывод: **потому что предел печатаемости платы почти всегда задается самой маленькой aperture или самым тяжелым местом для release.**

Перед freeze нужно проверить:

- **Где находятся самые маленькие aperture**
- **Защищает ли единая толщина fine-pitch зоны**
- **Нужен ли step stencil**
- **Нужно ли компенсировать большие pads формой aperture, а не общей толщиной**

<a id="pcb-dfm"></a>
## Почему stencil нужно оценивать вместе с PCB pads, solder mask и параметрами assembly?

Вывод: **потому что многие дефекты печати являются не проблемой stencil как такового, а проблемой pad, solder mask, via и package recommendation, которые не были сведены вместе.**

В одном цикле стоит проверить:

- **Совпадают ли размеры pad с рекомендуемым land pattern**
- **Не сжимает ли solder mask реальное окно пасты**
- **Не меняют ли via-in-pad, plugging и surface finish поведение печати**
- **Нужна ли отдельная стратегия control voids для thermal pad**

<a id="feedback"></a>
## Почему серийному stencil нужна петля обратной связи по данным?

Вывод: **потому что хороший серийный stencil - это не тот, который однажды напечатал приемлемый образец, а тот, который повторяет близкий результат от партии к партии.**

Практичная петля обратной связи обычно включает:

1. **Классификацию критичных семейств компонентов.**
2. **Привязку дефектов к семействам aperture.**
3. **Привязку толщины к mix компонентов.**
4. **Совместный анализ X-ray и SPI.**
5. **Возврат изменений в controlled documents.**

<a id="next-steps"></a>
## Следующие шаги с HILPCB

- Для aperture strategy и package classification сначала подключить [SMT Assembly](https://hilpcb.com/en/products/smt-assembly).
- Если sourcing, assembly и reflow window идут вместе, замораживать стратегию вместе с [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly).
- Для ранней проверки чертежей использовать [Gerber Viewer](https://hilpcb.com/en/tools/gerber-viewer/).
- Чтобы раньше увидеть риски, выносить критичные структуры в [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/).
- [PCB Surface Finish](https://hilpcb.com/en/services/pcb-surface-finish/) тоже нужно обсуждать заранее.

<a id="faq"></a>
## Часто задаваемые вопросы (FAQ)

<!-- faq:start -->

### Обычно достаточно правила 1:1 между aperture и pad?

A: Нет. Разные packages требуют разного баланса между объемом пасты, release и wetting.

### Почему толщину нельзя выбирать только по самому крупному компоненту?

A: Потому что предел печати обычно задается самой маленькой и самой трудной для release aperture.

### Почему BGA и центральные thermal pads почти всегда требуют отдельного подхода?

A: Потому что они сильнее усиливают voids, head-in-pillow, uneven collapse и drift.

### Почему проблемы stencil так часто уходят корнями в PCB pads?

A: Потому что pad, solder mask, via treatment и land pattern напрямую формируют поведение печати.

### Что важнее всего зафиксировать до производства?

A: Классификацию компонентов, aperture strategy, базовую толщину или решение по step stencil, правила связки с PCB pads и контур обратной связи SPI/AOI/X-ray.

<!-- faq:end -->

<a id="references"></a>
## Открытые источники

1. [IPC-7525C TOC, Stencil Design Guidelines](https://www.ipc.org/TOC/IPC-7525C_TOC.pdf)  
   Подтверждает, что stencil design - отдельная дисциплина и не существует одной нормы для всех проектов.

2. [StencilCoach Standard Apertures | Indium Corporation](https://software.indium.com/stencil-coach/standard-apertures.php)  
   Подтверждает эмпирические правила для aspect ratio и area ratio.

3. [IPC Standards](https://www.ipc.org/ipc-standards)  
   Подтверждает совместное рассмотрение стандартов stencil, PCB и assembly.

4. [Meet Your Standards | IPC-A-610](https://www.ipc.org/meet-your-standards)  
   Подтверждает, что финальная оценка идет по приемлемости готовых solder joints.

<a id="author"></a>
## Информация об авторе и проверке

- Автор: контент-команда HILPCB по PCBA и assembly
- Техническая проверка: команды SMT process, DFM и quality engineering
- Последнее обновление: 2025-11-18
