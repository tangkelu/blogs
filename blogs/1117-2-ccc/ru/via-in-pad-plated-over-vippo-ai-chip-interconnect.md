---
title: "Via-in-Pad plated over (VIPPO): как решить задачи packaging и high-speed interconnect для AI chip interconnect и substrate PCBs"
description: "Deep dive по Via-in-Pad plated over (VIPPO): Signal Integrity, Power Integrity, теплопути, ключевые process controls и cost‑effective дизайн‑стратегии для высокопроизводительных AI interconnect и IC substrate PCBs."
category: technology
date: "2025-11-17"
featured: true
image: ""
readingTime: 8
tags: ["Via-in-Pad plated over (VIPPO)", "Copper pillar", "Hybrid stack-up (Rogers+FR-4)", "Backdrill quality control", "Heavy copper 3oz+", "Controlled impedance"]
---
Взрывной рост AI, HPC и data‑center нагрузок поднял требования к аппаратной базе на новый уровень. Мощность и пропускная способность AI accelerators, GPU и ASIC продолжают расти, усложняя проектирование и изготовление IC substrates и PCB. В этом контексте **Via-in-Pad plated over (VIPPO)** эволюционировала из «опции» в обязательный ключевой процесс: она напрямую влияет на SI, стабильность PDN и эффективность thermal management. С позиции thermal interface design engineer разберём, что такое **Via-in-Pad plated over (VIPPO)** и как она закрывает вызовы packaging и high‑speed interconnect для AI chip interconnect и substrates.

В HDI‑дизайне, особенно при работе с BGA 0.4 mm (и меньше) pitch, традиционный Dog‑bone fanout перестаёт обеспечивать нужную плотность трассировки. **Via-in-Pad plated over (VIPPO)** размещает via прямо под pad, заполняет его (conductive или non‑conductive материалом) и затем выполняет повторную металлизацию поверхности, формируя плоский, паяемый pad. Это экономит routing space и создаёт физическую основу для предельных электрических и тепловых характеристик. Понимание того, как HILPCB помогает оптимизировать AI interconnect/substrate дизайн, важно для успеха.

### Что такое Via-in-Pad plated over (VIPPO)?

По сути, **Via-in-Pad plated over (VIPPO)** — продвинутый процесс fabrication, решающий проблему routing congestion при высокой плотности компонентов. Типовой flow включает:

1.  **Drilling:** сверление via в центре pad для BGA/LGA/других SMD.
2.  **Via-wall plating:** нанесение меди на стенки via для межслойного соединения.
3.  **Filling:** полное заполнение via специализированной эпоксидой (conductive или non‑conductive). Критично исключить voids, иначе при reflow возможно разрушение пайки.
4.  **Planarization:** grinding или CMP для выравнивания поверхности заполняемого via «в ноль».
5.  **Plated-over cap:** повторная медная металлизация по выровненной поверхности via/pad для получения ровного контактного pad.
6.  **Surface finish:** ENIG, ImAg, OSP и т. д.

В сравнении с Dog‑bone **Via-in-Pad plated over (VIPPO)** устраняет короткую fanout‑дорожку, сокращает путь сигнала и позволяет ставить decoupling capacitors ближе к power pins IC. Для современных AI substrates это базовая оптимизация плотности и характеристик.

### Как VIPPO улучшает Signal Integrity (SI) на AI substrates?

AI‑системы работают на десятках и сотнях Gbps (например, PCIe 6.0, HBM3e). На таких частотах малейшие геометрические дефекты вызывают серьёзные SI‑проблемы. **Via-in-Pad plated over (VIPPO)** выступает «защитником» SI.

Во‑первых, VIPPO устраняет fan‑out trace Dog‑bone и резко сокращает путь от BGA ball до внутренней трассы. Это уменьшает паразитные L/C, снижает деградацию фронта и сглаживает discontinuity импеданса. Для диффпаров с **Controlled impedance** VIPPO обеспечивает более плавный переход и снижает reflections/jitter.

Во‑вторых, VIPPO снижает влияние via stub. В классическом multilayer through‑via проходит через все слои, и неиспользуемая часть образует stub, который резонирует на ВЧ. **Backdrill quality control** помогает убрать stub, но добавляет операции и стоимость. VIPPO в сочетании с blind/buried vias позволяет избежать stub уже на уровне дизайна и получить более «чистый» канал для SerDes и memory bus.

<div style="background-color:#F5F7FA;padding:20px;border-radius:8px;margin:20px 0;">
<h3 style="color:#000000;text-align:center;border-bottom:3px solid #64B5F6;padding-bottom:10px;">Сравнение характеристик via‑технологий</h3>
<table style="width:100%;border-collapse:collapse;text-align:center;color:#000000;">
<thead style="background-color:#F5F5F5;color:#000000;">
<tr>
<th style="padding:12px;border:1px solid #ddd;">Параметр</th>
<th style="padding:12px;border:1px solid #ddd;border-bottom:3px solid #4CAF50;">Via-in-Pad plated over (VIPPO)</th>
<th style="padding:12px;border:1px solid #ddd;border-bottom:3px solid #FFC107;">Dog-bone via (Dog-Bone Via)</th>
<th style="padding:12px;border:1px solid #ddd;border-bottom:3px solid #F44336;">Open via-in-pad (Via-in-Pad Open)</th>
  </tr>
</thead>
<tbody>
<tr>
<td style="padding:12px;border:1px solid #ddd;">Плотность трассировки</td>
<td style="padding:12px;border:1px solid #ddd;color:#1E3A8A;"><b>Очень высокая</b></td>
<td style="padding:12px;border:1px solid #ddd;">Низкая</td>
<td style="padding:12px;border:1px solid #ddd;">Высокая</td>
</tr>
<tr>
<td style="padding:12px;border:1px solid #ddd;">Длина пути сигнала</td>
<td style="padding:12px;border:1px solid #ddd;color:#1E3A8A;"><b>Минимальная</b></td>
<td style="padding:12px;border:1px solid #ddd;">Длинная</td>
<td style="padding:12px;border:1px solid #ddd;">Короткая</td>
</tr>
<tr>
<td style="padding:12px;border:1px solid #ddd;">Паразитная индуктивность</td>
<td style="padding:12px;border:1px solid #ddd;color:#1E3A8A;"><b>Минимальная</b></td>
<td style="padding:12px;border:1px solid #ddd;">Высокая</td>
<td style="padding:12px;border:1px solid #ddd;">Низкая</td>
</tr>
<tr>
<td style="padding:12px;border:1px solid #ddd;">Тепловые характеристики</td>
<td style="padding:12px;border:1px solid #ddd;color:#1E3A8A;"><b>Отличные</b></td>
<td style="padding:12px;border:1px solid #ddd;">Слабые</td>
<td style="padding:12px;border:1px solid #ddd;">Средние</td>
</tr>
<tr>
<td style="padding:12px;border:1px solid #ddd;">Сложность производства</td>
<td style="padding:12px;border:1px solid #ddd;">Высокая</td>
<td style="padding:12px;border:1px solid #ddd;">Низкая</td>
<td style="padding:12px;border:1px solid #ddd;">Средняя</td>
</tr>
<tr>
<td style="padding:12px;border:1px solid #ddd;">Надёжность пайки</td>
<td style="padding:12px;border:1px solid #ddd;color:#1E3A8A;"><b>Высокая (void‑free)</b></td>
<td style="padding:12px;border:1px solid #ddd;">Высокая</td>
<td style="padding:12px;border:1px solid #ddd;">Низкая (риск solder wicking)</td>
</tr>
</tbody>
</table>
</div>

### Роль VIPPO в thermal management

Современные AI chips могут иметь TDP в сотни ватт и выше 1000W. Без эффективного отвода тепла неизбежны throttling и деградация. **Via-in-Pad plated over (VIPPO)** работает как микро‑теплоканал.

При заполнении via термопроводящим материалом (или даже при non‑conductive filling, где основную роль играет plated copper) VIPPO создаёт низкое тепловое сопротивление от pad чипа к внутренним большим плоскостям GND/power. Эти planes распределяют heat как heat spreader. В high‑power дизайнах часто формируют VIPPO‑array под источником тепла — «матрицу thermal pillars».

Этот board‑level путь работает вместе с package‑level решениями (vapor chamber) и system‑level охлаждением (fan, liquid). На слоях **Heavy copper 3oz+** теплоперенос улучшается: толстая медь быстрее распределяет тепло в плоскости. Как производитель [Heavy Copper PCB](https://hilpcb.com/en/products/heavy-copper-pcb), Highleap PCB Factory (HILPCB) контролирует etch и lamination, чтобы VIPPO и heavy copper сочетались надёжно.

### Как VIPPO улучшает Power Integrity (PI)?

AI chips требуют PDN с очень низкой импедансом, чтобы подавлять шум при больших di/dt. **Via-in-Pad plated over (VIPPO)** усиливает PI несколькими способами.

Во‑первых, VIPPO даёт максимально короткие и прямые связи power/ground, уменьшая индуктивность между planes и pins. По V = L * (di/dt) это снижает rail noise.

Во‑вторых, VIPPO позволяет располагать decoupling capacitors на обратной стороне BGA‑массива почти «back‑to‑back» с power/ground pins, минимизируя loop inductance и улучшая высокочастотное развязывание.

Кроме того, VIPPO хорошо сочетается с **Copper pillar** в advanced packaging. **Copper pillar** обеспечивает ниже сопротивление, выше ток и лучшую теплопроводность, чем классические bumps, и широко используется в Flip‑Chip. VIPPO даёт соответствующую high‑density, low‑impedance посадочную структуру на substrate‑стороне, поддерживая низкоимпедансный путь тока до кристалла.

<div style="background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); color: #1e293b; padding: 35px; border-radius: 24px; margin: 30px 0; font-family: system-ui, -apple-system, sans-serif; border: 1px solid #e2e8f0; box-shadow: 0 15px 40px rgba(0, 0, 0, 0.05);">
<h3 style="text-align: center; color: #0f172a; margin: 0 0 10px 0; font-size: 1.85em; font-weight: 800; letter-spacing: -0.5px;">🚀 HILPCB: ключевые производственные метрики для next‑gen AI substrates</h3>
<p style="text-align: center; color: #64748b; font-size: 1.05em; margin-bottom: 35px; font-weight: 500;">Вычисления large models: экстремальная плотность interconnect и high‑current power архитектуры</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 18px;">
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 20px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 8px;">Ultra‑high lamination capability</strong>
<p style="font-size: 32px; font-weight: 900; margin: 10px 0; color: #1e3a8a;">56 <span style="font-size: 16px; font-weight: 600; color: #64748b;">Layers</span></p>
<p style="font-size: 0.85em; color: #64748b; line-height: 1.5; margin: 0;">Опыт в **Any-layer HDI** и mixed lamination для структурной стабильности 800G switches и compute cards.</p>
</div>
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 20px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 8px;">VIPPO &amp; microvia process</strong>
<p style="font-size: 32px; font-weight: 900; margin: 10px 0; color: #1e3a8a;">0.15 <span style="font-size: 16px; font-weight: 600; color: #64748b;">mm</span></p>
<p style="font-size: 0.85em; color: #64748b; line-height: 1.5; margin: 0;">Поддержка **Via-in-Pad** filling и plated‑over. Оптимизация fanout BGA и routing escape для AI chips с огромным pin count.</p>
</div>
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 20px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 8px;">Экстремальный контроль импеданса и SI</strong>
<p style="font-size: 32px; font-weight: 900; margin: 10px 0; color: #1e3a8a;">±5 <span style="font-size: 20px; font-weight: 600; color: #64748b;">%</span></p>
<p style="font-size: 0.85em; color: #64748b; line-height: 1.5; margin: 0;">Строгое соответствие **PCIe 6.0/7.0** благодаря high‑precision etch compensation.</p>
</div>
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 20px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 8px;">High‑load current и управление мощностью</strong>
<p style="font-size: 32px; font-weight: 900; margin: 10px 0; color: #1e3a8a;">12 <span style="font-size: 20px; font-weight: 600; color: #64748b;">oz</span></p>
<p style="font-size: 0.85em; color: #64748b; line-height: 1.5; margin: 0;">Thick‑copper power layers для AI core до 1000W+ — снижение PDN drop и температурного роста.</p>
</div>
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 20px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 8px;">Advanced material integration</strong>
<p style="font-size: 1.1em; font-weight: 800; margin: 15px 0; color: #1e3a8a; line-height: 1.4;">ABF / Megtron 8 / Rogers</p>
<p style="font-size: 0.85em; color: #64748b; line-height: 1.5; margin: 0;">Полная поддержка **Ajinomoto Build-up Film (ABF)** и Ultra‑Low Loss RF материалов.</p>
</div>
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 20px; padding: 25px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 8px;">Fine‑line и substrate технологии</strong>
<p style="font-size: 32px; font-weight: 900; margin: 10px 0; color: #1e3a8a;">2/2 <span style="font-size: 16px; font-weight: 600; color: #64748b;">mil</span></p>
<p style="font-size: 0.85em; color: #64748b; line-height: 1.5; margin: 0;">Использование **mSAP** для ultra‑fine routing под высокую плотность interconnect в Chiplet архитектурах.</p>
</div>
</div>
<div style="margin-top: 35px; padding: 25px; background: #eff6ff; border-radius: 16px; border-left: 8px solid #3b82f6; font-size: 0.95em; line-height: 1.7; color: #1e40af;">
💡 <strong>Совет HILPCB:</strong> для AI substrates 56 layers и выше критично matching <strong>Z-axis CTE</strong>. Включайте симуляцию **Warpage** на этапе stackup, чтобы обеспечить coplanarity при пайке больших BGA.
</div>
</div>

### Влияние VIPPO на сложные stackup‑дизайны

**Via-in-Pad plated over (VIPPO)** — основа для ultra‑dense HDI и сложных [IC Substrate PCB](https://hilpcb.com/en/products/ic-substrate-pcb). Она позволяет выполнять fine‑pitch BGA fanout без увеличения layer count, что важно для стоимости и толщины.

В mixed‑signal системах с RF и high‑speed digital часто применяют **Hybrid stack-up (Rogers+FR-4)**: [Rogers PCB](https://hilpcb.com/en/products/rogers-pcb) для RF и FR‑4/ABF‑like для цифровой части. VIPPO подходит и здесь, обеспечивая высокую плотность и контролируемые межматериальные переходы для SI/PI.

VIPPO также сочетается с microvias (stacked/staggered), формируя 3D interconnect сеть: сигнал вводится с поверхности через VIPPO, а затем быстро распределяется по слоям через microvias, минимизируя Z‑axis путь.

### Ключевые QC‑точки в VIPPO fabrication

VIPPO даёт сильные преимущества, но требует строгого process control:

1.  **Качество заполнения:** vacuum‑assisted filling для void‑free. Voids при reflow расширяются и вызывают pad lifting, BGA opens или Head‑in‑Pillow.
2.  **Planarity:** точный контроль grinding/polishing (часто ±0.5 mil). Неплоскостность ухудшает печать пасты и пайку.
3.  **Адгезия copper cap:** достаточная peel strength; иначе возможна delamination при thermal shock.
4.  **Размерная точность:** контроль диаметра, позиции и геометрии pad.

В отличие от **Backdrill quality control** (глубина и stub removal), VIPPO требует QC по filling/planarization/re‑plating и более высокого Cpk. HILPCB использует AOI, X‑ray и micro‑section анализ для соответствия IPC‑6012 Class 3 и выше.

<div style="background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); color: #1e293b; padding: 35px; border-radius: 24px; margin: 30px 0; font-family: system-ui, -apple-system, sans-serif; border: 1px solid #e2e8f0; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);">
<h3 style="text-align: center; color: #0f172a; margin: 0 0 10px 0; font-size: 1.75em; font-weight: 800; letter-spacing: -0.5px;">🎯 VIPPO process: точки sign‑off для high‑density design и производства</h3>
<p style="text-align: center; color: #64748b; font-size: 1.05em; margin-bottom: 35px; font-weight: 500;">Core‑гайд по оптимизации плотности BGA fanout и Signal Integrity</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 18px; padding: 25px; border-top: 6px solid #2563eb;">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 12px;">01. Void-free filling</strong>
<p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Правило:</strong> заполнение должно быть полностью плотным. Остаточные пузырьки расширяются при reflow и приводят к pad lifting или cracking пайки.</p>
</div>
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 18px; padding: 25px; border-top: 6px solid #2563eb;">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 12px;">02. Surface planarity</strong>
<p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Правило:</strong> planarity напрямую определяет solder yield. Контролируйте etch‑back и grinding, чтобы минимизировать recess/protrusion и снизить риск opens/HoP.</p>
</div>
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 18px; padding: 25px; border-top: 6px solid #2563eb;">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 12px;">03. Aspect ratio и plating challenges</strong>
<p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Правило:</strong> высокий aspect ratio усложняет проникновение химии и resin filling. Для thick boards заранее согласуйте параметры vacuum filling, чтобы избежать underfill.</p>
</div>
<div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 18px; padding: 25px; border-top: 6px solid #2563eb;">
<strong style="color: #1e40af; font-size: 1.1em; display: block; margin-bottom: 12px;">04. Cost effectiveness и выборочное применение</strong>
<p style="color: #475569; font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Правило:</strong> VIPPO дороже из‑за filling/grinding/re‑plating. Применяйте локально: BGA core ниже 0.8 mm pitch или зоны с максимальными требованиями к термике и return path/SI.</p>
</div>
</div>
<div style="margin-top: 35px; padding: 25px; background: #eff6ff; border-radius: 16px; border-left: 8px solid #2563eb; font-size: 0.95em; line-height: 1.7; color: #1e40af;">
💡 <strong>Tip HILPCB:</strong> для VIPPO pads рекомендуем выделенную линию cap plating <strong>POFV</strong>, чтобы повысить peel strength и снизить риск delamination при тяжёлых thermal cycling.
</div>
</div>

### VIPPO и advanced packaging (например, Copper Pillar)

Advanced packaging (2.5D/3D, CoWoS, Foveros) — ключ к дальнейшему росту: чипы соединяются через interposer или direct bonding в SiP. **Via-in-Pad plated over (VIPPO)** здесь выступает мостом между сложным packaging и main PCB.

Особенно это заметно в связке с **Copper pillar**: по сравнению с solder bumps, **Copper pillar** даёт ниже сопротивление, выше ток и лучшую теплопроводность и часто используется в Flip‑Chip. Малый pitch требует высокой плотности и точности pad‑структур, и VIPPO обеспечивает такие планарные pads. Для HBM, где тысячи interconnect‑линий критичны к импедансу и длине, VIPPO повышает равномерность на уровне substrate и помогает достигать целей [High-Speed PCB](https://hilpcb.com/en/products/high-speed-pcb).

### Как балансировать преимущества VIPPO и стоимость?

VIPPO — value‑added процесс и стоит дороже стандартных vias из‑за resin fill и дополнительных операций. Поэтому ключ к cost‑effective дизайну — выборочное применение.

Используйте VIPPO там, где она действительно нужна: ultra‑fine‑pitch BGA breakout, high‑speed fanout, зоны под мощными источниками тепла. В остальных областях применяйте менее дорогие решения (microvias/стандартные vias). С опытным производителем вроде HILPCB ранний DFM помогает определить, где VIPPO даёт максимальный ROI и где можно снизить стоимость альтернативами — в том числе в **Hybrid stack-up (Rogers+FR-4)** проектах. Наша компетенция [HDI PCB](https://hilpcb.com/en/products/hdi-pcb) покрывает комплекс решений, включая VIPPO.

#

<!-- COMPONENT: BlogQuickQuoteInline -->

## Заключение: VIPPO — обязательный шаг к будущему AI hardware

**Via-in-Pad plated over (VIPPO)** превратилась из «nice‑to‑have» в ключевую enabling технологию для AI/HPC. Она обеспечивает экстремальную плотность, улучшенную SI, эффективные теплопути и стабильный PDN, напрямую закрывая вызовы современных AI chips. Без VIPPO многие сложные substrate‑дизайны было бы трудно реализовать.

Чтобы извлечь максимум, нужна тесная кооперация design и производителя и понимание design rules, ограничений процесса и QC‑пунктов. С HILPCB вы получаете точный контроль **Controlled impedance**, опыт **Heavy copper 3oz+** и понимание интерфейсов **Copper pillar**, что ускоряет путь от дизайна до надёжной серийной реализации.

Свяжитесь с HILPCB для быстрого расчёта и запуска вашего AI substrate проекта — вместе построим следующую технологическую волну.

