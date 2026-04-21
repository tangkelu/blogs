---
title: "Что нужно фиксировать в сборке chiplet-bridge substrate в первую очередь: окно bridge-зоны, коробление, underfill и поэтапные испытания"
description: "Практическое руководство по тому, что нужно замораживать в сборке chiplet-bridge substrate на раннем этапе: геометрия bridge-зоны, коробление, underfill, контроль и термоциклирование для проектов уровня UCIe и EMIB."
category: technology
date: "2025-11-19"
featured: true
image: ""
readingTime: 10
tags: ["chiplet packaging", "Bridge substrate", "Advanced packaging assembly", "UCIe", "EMIB", "Underfill"]
---

# Что нужно фиксировать в сборке chiplet-bridge substrate в первую очередь: окно bridge-зоны, коробление, underfill и поэтапные испытания

- **Первый вопрос для chiplet-bridge substrate не в плотности трассировки, а в том, есть ли у bridge-зоны повторяемое окно сборки.** В спецификациях UCIe UCIe определяется как открытый стандарт package-level die-to-die interconnect, охватывающий physical layer, protocol stack, software stack и compliance testing.
- **Bridge-структура не является просто более плотной версией BGA-substrate.** Intel описывает EMIB как небольшой кремниевый bridge, встроенный в substrate, чтобы обеспечить сверхплотное die-to-die соединение без полноразмерного кремниевого interposer.
- **Прототип, который включился, еще не означает готовый серийный процесс.** Intel Foundry разделяет wafer sort, die sort, burn-in, final test и system-level test, что прямо показывает необходимость поэтапного отсечения дефектов.
- **Bridge-зону, underfill, термоциклы и трассируемость отказов нужно рассматривать вместе.** Самый дорогой риск здесь обычно не полный отказ, а постепенная потеря стабильности под термомеханической нагрузкой, когда после этого сложно добраться до корневой причины.
- **Стабильный bridge-substrate - это не единичный образец, который работает, а bridge-зона, набор материалов, процесс сборки и план испытаний, которые воспроизводятся от лота к лоту.**

> **Quick Answer**  
> Суть сборки chiplet-bridge substrate в том, чтобы локальная bridge-структура, порядок установки, процесс underfill, контроль коробления и поэтапные испытания работали в одном повторяемом технологическом окне. Для проектов класса UCIe и EMIB важнее не то, что один образец запускается, а то, что bridge-зону можно повторяемо собрать, проверить, отследить и сохранить стабильной после термоциклирования.

## Содержание

- [Что в инженерной работе нужно смотреть первым на chiplet-bridge substrate?](#overview)
- [Сводка ключевых правил и параметров](#rules)
- [Почему проектирование substrate должно строиться вокруг сборочного окна bridge-зоны?](#bridge-window)
- [Почему коробление, underfill и термоциклы нужно считать одной задачей?](#warpage-underfill)
- [Почему known good die, поэтапные испытания и трассируемость отказов нужно планировать заранее?](#kgd-test)
- [Как валидировать сборку chiplet-bridge substrate перед производством?](#validation)
- [Следующие шаги с HILPCB](#next-steps)
- [FAQ](#faq)
- [Публичные источники](#references)
- [Автор и техническая проверка](#author)

<a id="overview"></a>
## Что в инженерной работе нужно смотреть первым на chiplet-bridge substrate?

Сначала смотрят на **bridge-зону, локальную плоскостность, коробление, underfill, поэтапные испытания и проверку в термоциклах**.

Это не просто задача "уложить больше сигналов в меньшую площадь". В UCIe package-level interconnect, software model и compliance testing рассматриваются в одной системе координат. В публичных материалах Intel по EMIB прямо сказано, что соединение строится вокруг небольшого кремниевого bridge, встроенного в substrate. Intel Foundry дополнительно показывает разделение на die sort, burn-in, final test и system-level test.

Поэтому более надежная последовательность раннего review обычно такая:

1. **Подтвердить, что геометрия bridge-зоны, порядок сборки и локальная плоскостность укладываются в повторяемое окно процесса.**
2. **Оценивать коробление, течение underfill и напряжения от отверждения вместе с bridge-зоной.**
3. **Проверить, что тестовая стратегия позволяет отделять дефекты die от дефектов bridge-сборки.**
4. **Сразу включить термоциклирование и failure analysis в пилотный план.**
5. **До запуска определить точки контроля, образцы для шлифов и схему lot traceability.**

Если в проекте уже есть сверхплотная bridge-зона с microvia и fine-pitch структурами, разумно рано привлекать производственные границы [IC Substrate PCB](https://hilpcb.com/en/products/ic-substrate-pcb) и [HDI PCB](https://hilpcb.com/en/products/hdi-pcb), а не разбираться с ними перед самым пилотом.

<a id="rules"></a>
## Сводка ключевых правил и параметров

| Правило / параметр | Рекомендуемый подход | Почему это важно | Как проверять | Что будет, если игнорировать |
|---|---|---|---|---|
| Окно bridge-зоны | Отдельно проверять локальную геометрию и плоскостность вокруг bridge | Основной риск сконцентрирован локально, а не в среднем по плате | Структурный review, локальный осмотр, coplanarity | Первые образцы собираются, но пилот плохо повторяется |
| Контроль коробления | Отслеживать форму после ламинации, установки, underfill и reflow | Многоматериальные локальные структуры очень чувствительны к короблению | Warpage tracking, сравнение этапов процесса | Выход сначала падает по coplanarity и bridge placement |
| Поведение underfill | Контролировать полноту заполнения, voids и напряжения отверждения | Underfill может как защищать, так и создавать новый источник напряжений | X-ray, шлиф, сравнение до и после термоциклов | Ранние образцы проходят, а ресурс уходит |
| Поэтапные испытания | Разделять test die, test assembly и финальный system test | Позволяет быстро отделить дефекты die от дефектов bridge | Die sort, burn-in, final test, SLT | Корневая причина смешивается |
| Цепочка трассируемости | Связывать material lots, reflow history, underfill и samples | Многие дефекты bridge-зоны скрытые | Lot records, sample ID, FA flow | После отказа сложно восстановить картину |
| Термоциклическая валидация | Считать термоциклы основным этапом, а не дополнением | Риск ресурса часто запускается термомеханическими напряжениями | Термоциклы, шлифы, структурное сравнение | Bring-up проходит, а долговечность рушится |

| Сценарий проекта | Самый типичный фокус сборки |
|---|---|
| UCIe package-level bridge | Выравнивание bridge, локальная плоскостность, слоистая стратегия тестов |
| EMIB-подобный embedded bridge | Cavity в substrate, напряжения около bridge, underfill и контроль |
| Multi-die / multi-chiplet substrate | Порядок установки, нагрузка на bridge, термоциклы, traceability |

<div style="background: linear-gradient(135deg, #eef2fb 0%, #f7f0ea 100%); border: 1px solid #dcdfee; border-radius: 20px; padding: 24px; margin: 28px 0;">
  <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px;">
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #6d59a0; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #56457f; font-weight: 700;">Bridge Zone Is the Real Product</div>
      <div style="margin-top: 8px; color: #2f2941;">Для bridge-substrate настоящая технологическая цель - не среднее качество всей панели, а способность bridge-зоны оставаться собираемой, контролируемой и повторяемой.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #8a6849; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #6b5239; font-weight: 700;">Warpage Comes Early</div>
      <div style="margin-top: 8px; color: #382e24;">При тонком substrate, смешанных материалах и локально высокой плотности коробление часто становится убийцей выхода раньше электрических проблем.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4d7b68; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #3a5f51; font-weight: 700;">Underfill Is a Reliability Process</div>
      <div style="margin-top: 8px; color: #23342d;">Underfill - это не косметика, а процесс, определяющий надежность. Неполное заполнение или неверные напряжения отверждения напрямую сокращают срок службы.</div>
    </div>
    <div style="background: rgba(255,255,255,0.84); border-left: 4px solid #4a7393; border-radius: 14px; padding: 16px;">
      <div style="font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; color: #38586f; font-weight: 700;">Testing Must Be Layered</div>
      <div style="margin-top: 8px; color: #243440;">Без разделения испытаний на die, package и system потом почти невозможно отделить дефекты bridge-зоны от дефектов самого die.</div>
    </div>
  </div>
</div>

<a id="bridge-window"></a>
## Почему проектирование substrate должно строиться вокруг сборочного окна bridge-зоны?

Потому что **bridge-зона - самый чувствительный, наименее воспроизводимый и часто первый деградирующий локальный участок всего substrate**.

Intel публично описывает EMIB как небольшой кремниевый bridge, встроенный в substrate для сверхплотного соединения между die. Такая архитектура переводит фокус с усредненного качества всей платы на локальное технологическое окно bridge.

На раннем этапе нужно фиксировать прежде всего следующее:

- **Не усиливает ли локальное распределение меди вокруг bridge механические напряжения?**
- **Не добавляет ли последовательность установки лишнюю тепловую историю в bridge-зону?**
- **Достаточны ли плоскостность и coplanarity возле bridge для повторяемой сборки?**
- **Остаются ли microvia, pads и края cavity внутри реального технологического окна?**

Если bridge-зону не рассматривать как отдельный объект процесса, пилотные сборки обычно не срываются резко. Чаще окно просто оказывается слишком узким и зависимым от ручной подстройки. Поэтому имеет смысл рано подключать возможности [IC Substrate PCB](https://hilpcb.com/en/products/ic-substrate-pcb) и [HDI PCB](https://hilpcb.com/en/products/hdi-pcb).

<a id="warpage-underfill"></a>
## Почему коробление, underfill и термоциклы нужно считать одной задачей?

Потому что **ресурсный риск bridge-substrate редко возникает из-за одного события. Обычно это накопленный результат тепловой истории и напряжений материалов.**

Bridge-substrate обычно проходит ламинацию, операции сборки в зоне bridge, die attach, underfill, reflow и последующие тепловые испытания. Каждый шаг способен изменить локальное напряженное состояние. Underfill не всегда автоматически полезен. Он может перераспределять напряжения, но неполное заполнение, повышенная пустотность или несогласованное отверждение также создают новый механизм отказа.

Наиболее полезно рассматривать вместе:

1. **Изменение локального коробления до и после underfill**
2. **Целостность bridge-зоны до и после термоциклов**
3. **Сосредоточены ли voids, загрязнение или плохое заполнение в плотных участках**
4. **Появляются ли после термоциклов новые трещины или признаки delamination**

Если underfill оценивают только по внешнему виду и не связывают с термоциклами и структурой bridge, ресурс почти всегда переоценивается. Для engineering samples такой контроль лучше рано включать в план [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/).

<a id="kgd-test"></a>
## Почему known good die, поэтапные испытания и трассируемость отказов нужно планировать заранее?

Потому что **самая дорогая ошибка в advanced packaging - не сам дефект, а потеря возможности быстро понять, где источник: die, bridge-зона или процесс**.

Intel Foundry в своем потоке advanced chiplet test публично показывает wafer sort, die sort, burn-in, final test и system-level test и отдельно подчеркивает доставку known good die до финальной сборки. Для bridge-substrate это означает:

- **Испытания должны быть поэтапными, а не сводиться к финальному включению**
- **Die sort и known good die уменьшают шум в анализе отказов bridge**
- **Burn-in и system-level test лучше выявляют пограничные термомеханические дефекты**
- **Lot traceability и привязка образцов должны существовать до пилота**

Без этих основ отказы дальше выглядят как случайный брак образцов, странности после термоциклов или нестабильность между лотами, но без ясности, виноваты ли die, bridge, underfill или история сборки. Если продукт затем входит в более высокий серверный или ускорительный уровень, полезно увязать пакетный взгляд с системной логикой из [Why AI Server Motherboards Can Power Up but Still Fail in Production](/code/blogs/blogs/1119-1-ccc/ru/ai-server-motherboard-reliability.md).

<a id="validation"></a>
## Как валидировать сборку chiplet-bridge substrate перед производством?

Реальная цель - **замкнуть контур между bridge-зоной, underfill, термоциклами и стабильностью между лотами**.

Наиболее полезный путь валидации обычно включает:

| Элемент валидации | На какой вопрос отвечает | Что лучше наблюдать |
|---|---|---|
| Проверка локальной структуры / coplanarity | Находится ли bridge-зона в окне сборки? | Плоскостность вокруг bridge, локальная форма платы, состояние после установки |
| X-ray / шлиф | Полностью ли сформированы underfill и скрытые структуры? | Voids, полнота заполнения, зоны концентрации дефектов |
| Сравнение до и после термоциклов | Сохраняет ли bridge-зона стабильность под ресурсной нагрузкой? | Трещины, delamination, визуальный и электрический дрейф |
| Поэтапные испытания | Можно ли разделить эффекты die, assembly и system behavior? | Аномалии в die sort, burn-in, final test и SLT |
| Сравнение нескольких лотов | Достаточно ли широко технологическое окно для серии? | Разброс между платами, дрейф параметров, признаки проблемного лота |

Если проект уже подходит к пилотной сборке, эти проверки нужно сразу включать в производственный и тестовый план. Когда окно bridge, поведение underfill, доказательства по термоциклам и структура тестов сходятся, финальные требования гораздо проще оформить в [Quote / RFQ](https://hilpcb.com/en/quote/).

<a id="next-steps"></a>
## Следующие шаги с HILPCB

Если вы работаете над проектом UCIe, EMIB или другим chiplet bridge substrate, следующим шагом обычно становится перевод "advanced packaging assembly" в реальные производственные входные данные:

- Если главный вопрос в bridge-зоне, microvia и локальных сверхтонких структурах, сначала используйте направления [IC Substrate PCB](https://hilpcb.com/en/products/ic-substrate-pcb) и [HDI PCB](https://hilpcb.com/en/products/hdi-pcb), чтобы зафиксировать локальные пределы процесса.
- Если цель пилота - проверить окно bridge-зоны, коробление и underfill, включайте эти пункты как можно раньше в review по [PCB Prototype](https://hilpcb.com/en/services/pcb-prototype/).
- Если критичны стабильность между лотами и восстановление причин отказа, заранее задавайте cross-section, X-ray, material lots и traceability параметров.
- Когда окно bridge, структура тестов и требования по термоциклам уже устойчивы, переводите комплект в [SMT Assembly](https://hilpcb.com/en/products/smt-assembly) или [Quote / RFQ](https://hilpcb.com/en/quote/).

<a id="faq"></a>
## FAQ

<!-- faq:start -->

### Основная сложность chiplet-bridge substrate - это плотность трассировки?

Не только. Чаще сложнее локальное окно сборки bridge-зоны, коробление, underfill, термоциклы и логика поэтапных испытаний.

### Почему структуры типа EMIB делают сборку более чувствительной?

Потому что EMIB использует небольшой кремниевый bridge, встроенный в substrate, для сверхплотного локального соединения. Из-за этого критичнее становятся локальная плоскостность, порядок установки, напряжения в bridge и поведение underfill.

### Делает ли underfill надежность автоматически лучше?

Нет. Если заполнение неполное, есть voids или после отверждения формируется неудачное напряженное состояние, underfill сам становится источником отказа.

### Почему так рано нужно планировать поэтапные испытания и трассируемость?

Потому что многие дефекты bridge-substrate - скрытые. Без разделения die / package / system и без привязки к lot потом трудно быстро выйти на реальную root cause.

### Что важнее всего зафиксировать перед изготовлением или пилотом?

В первую очередь нужно зафиксировать окно сборки bridge-зоны, стратегию контроля коробления, underfill, поэтапные испытания, валидацию в термоциклах и цепочку трассируемости отказов.

<!-- faq:end -->

<a id="references"></a>
## Публичные источники

1. [Specifications | UCIe Consortium](https://www.uciexpress.org/specifications)  
   Использовано для подтверждения тезисов о UCIe как об открытом package-level die-to-die стандарте, охватывающем physical layer, protocol stack, software stack и compliance testing.

2. [Intel® Stratix® 10 FPGAs Overview - Intel EMIB Packaging Technology](https://www.intel.com/content/www/us/en/products/details/fpga/stratix/10/article.html)  
   Использовано для подтверждения того, что EMIB применяет небольшой кремниевый bridge, встроенный в substrate, без большого кремниевого interposer.

3. [Advanced Packaging Innovations | Intel Foundry Packaging](https://www.intel.com/content/www/us/en/foundry/packaging.html)  
   Использовано для описания поэтапных advanced chiplet test с wafer sort, die sort, burn-in, final test, system-level test и подачей known good die до финальной сборки.

4. [EMIB Technology Brief | Intel](https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2025-07/emib-product-brief.pdf)  
   Использовано для дополнения темы встроенных bridge-структур в cavity substrate, стандартных package-assembly flows и более жесткого microbump pitch, локализованного в bridge-зоне.

<a id="author"></a>
## Автор и техническая проверка

- Автор: команда HILPCB по контенту для advanced packaging и high-density assembly
- Техническая проверка: инженерная команда по PCB process, assembly, термомеханике и failure analysis
- Последнее обновление: 2025-11-19
