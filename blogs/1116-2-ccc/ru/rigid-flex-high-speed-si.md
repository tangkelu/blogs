---
title: "Rigid-flex PCB: ultra-high-speed link и low-loss вызовы для high-speed signal integrity"
description: "Разбор Rigid-flex PCB: high-speed SI, thermal management и проектирование power/interconnect для высокопроизводительных PCB."
category: technology
date: "2025-11-16"
featured: true
image: ""
readingTime: 8
tags: ["Rigid-flex PCB", "Copper coin", "ENIG/ENEPIG/OSP", "Backdrill quality control", "Hybrid stack-up (Rogers+FR-4)", "Microvia/stacked via"]
---
Как инженер по измерениям и валидации консистентности (TDR/VNA, извлечение S-parameters), я знаю: в современных ultra-high-speed и high-density дизайнах выбор interconnect технологии напрямую решает судьбу системы. **Rigid-flex PCB** с 3D routing и высокой надёжностью становится ключевым решением для сложных задач high-speed SI. Это не просто носитель схемы — это способ обеспечить канал от chip до connector с высокой согласованностью.

В статье, со стороны SI verification, мы разбираем преимущества и вызовы Rigid-flex PCB и показываем, как материалы, stackup и manufacturing процессы позволяют контролировать attenuation, crosstalk и impedance discontinuities на 28G/56G/112G+. Фокус: Hybrid stack-up, Microvia/stacked via, surface finish, backdrill и Copper coin thermals.

### Почему Rigid-flex PCB — ключевой выбор для high-speed

Соединение rigid плат через кабели/коннекторы вносит сильные discontinuitiy impedance и loss на Gbps. Каждая смена среды “съедает” eye opening и jitter budget. Rigid-flex объединяет rigid и flex без механических интерфейсов, улучшая IL/RL, 3D упаковку, reliability и снижая общий TCO (за счёт меньшего числа деталей и сборочных операций).

### Hybrid stack-up для оптимизации SI и стоимости

Low-loss материалы (Rogers/Megtron) улучшают SI, но дороги. **Hybrid stack-up (Rogers+FR-4)** комбинирует:
- high-speed layers на Rogers/Tachyon,
- power/low-speed на High-Tg FR-4.

Важные моменты: симметрия stackup против warpage, совместимость материалов в lamination и корректные Dk/Df в impedance моделях.

<div style="background-color:#F5F7FA; padding: 20px; border-radius: 8px; margin: 20px 0;">
<h3 style="color:#000000; text-align:center;">Hybrid stackup: сравнение performance и cost</h3>
<table style="width:100%; border-collapse: collapse; color:#000000;">
<thead style="background-color:#E0E0E0;">
<tr>
<th style="padding:12px; border:1px solid #ccc; text-align:left;">Stackup</th>
<th style="padding:12px; border:1px solid #ccc; text-align:left;">Use case</th>
<th style="padding:12px; border:1px solid #ccc; text-align:left;">SI</th>
<th style="padding:12px; border:1px solid #ccc; text-align:left;">Relative cost</th>
<th style="padding:12px; border:1px solid #ccc; text-align:left;">Manufacturing complexity</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:12px; border:1px solid #ccc;">All FR-4</td>
<td style="padding:12px; border:1px solid #ccc;">&lt; 5 Gbps</td>
<td style="padding:12px; border:1px solid #ccc;">Средняя</td>
<td style="padding:12px; border:1px solid #ccc;">★</td>
<td style="padding:12px; border:1px solid #ccc;">Низкая</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #ccc;">Hybrid stack-up (Rogers+FR-4)</td>
<td style="padding:12px; border:1px solid #ccc;">5 - 56 Gbps</td>
<td style="padding:12px; border:1px solid #ccc;">Отличная</td>
<td style="padding:12px; border:1px solid #ccc;">★★★</td>
<td style="padding:12px; border:1px solid #ccc;">Высокая</td>
</tr>
<tr>
<td style="padding:12px; border:1px solid #ccc;">All Rogers/Megtron</td>
<td style="padding:12px; border:1px solid #ccc;">&gt; 56 Gbps / RF</td>
<td style="padding:12px; border:1px solid #ccc;">Максимальная</td>
<td style="padding:12px; border:1px solid #ccc;">★★★★★</td>
<td style="padding:12px; border:1px solid #ccc;">Средняя</td>
</tr>
</tbody>
</table>
</div>

### Microvia/stacked via в Rigid-flex PCB

При BGA pitch 0.5mm и ниже механические through-hole не дают нужной плотности. **Microvia/stacked via** становится стандартом: microvia laser (<150µm) с низкими паразитиками и stacked via для компактного вертикального interconnect. Требуются laser drilling и plated-filled с жёстким контролем и microsection, что важно для [HDI PCB](https://hilpcb.com/en/products/hdi-pcb).

### Уникальные SI сложности flex зоны

1) сложнее impedance control из-за Polyimide/Coverlay толерансов; 2) bending меняет геометрию и delay, важны симметрия дифф.пар и Neutral Axis; 3) hatched ground нарушает return path и повышает риск crosstalk/EMI.

<div style="background: #ffffff; border: 1px solid #d1c4e9; border-radius: 24px; padding: 40px 30px; margin: 30px 0; font-family: 'Segoe UI', system-ui, sans-serif; box-shadow: 0 15px 45px rgba(103,58,183,0.08);">
<h3 style="text-align: center; color: #311b92; margin: 0 0 40px 0; font-size: 1.8em; font-weight: 800; border-bottom: 4px solid #9575cd; padding-bottom: 15px; display: inline-block; width: 100%;">🌀 Flex zone: матрица high-speed SI & reliability</h3>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px;">
<div style="background: #f3e5f5; border: 1px solid #e1bee7; border-radius: 18px; padding: 25px; border-top: 6px solid #9575cd; display: flex; flex-direction: column;">
<strong style="color: #4527a0; font-size: 1.15em; margin-bottom: 12px;">01. Circular Traces & impedance</strong>
<p style="color: #475569; font-size: 0.9em; line-height: 1.7; margin: 0; flex-grow: 1;">Использовать <strong>Circular Traces</strong> в зоне bending и избегать 90°/45°.</p>
</div>
<div style="background: #f3e5f5; border: 1px solid #e1bee7; border-radius: 18px; padding: 25px; border-top: 6px solid #9575cd; display: flex; flex-direction: column;">
<strong style="color: #4527a0; font-size: 1.15em; margin-bottom: 12px;">02. Teardrop</strong>
<p style="color: #475569; font-size: 0.9em; line-height: 1.7; margin: 0; flex-grow: 1;">Добавлять <strong>Teardrop</strong> на переходе pad-trace для повышения прочности.</p>
</div>
<div style="background: #fdfbff; border: 1px solid #ede7f6; border-radius: 18px; padding: 25px; border-top: 6px solid #7e57c2; display: flex; flex-direction: column;">
<strong style="color: #311b92; font-size: 1.15em; margin-bottom: 12px;">03. Stiffener</strong>
<p style="color: #475569; font-size: 0.9em; line-height: 1.7; margin: 0; flex-grow: 1;">Размещать <strong>FR-4/PI stiffener</strong> у connector/SMT зон.</p>
</div>
<div style="background: #fdfbff; border: 1px solid #ede7f6; border-radius: 18px; padding: 25px; border-top: 6px solid #7e57c2; display: flex; flex-direction: column;">
<strong style="color: #311b92; font-size: 1.15em; margin-bottom: 12px;">04. No-via в динамической зоне</strong>
<p style="color: #475569; font-size: 0.9em; line-height: 1.7; margin: 0; flex-grow: 1;">Не размещать vias в зоне <strong>Bending Radius</strong>; переходы слоёв выносить в rigid/static зоны.</p>
</div>
</div>
<div style="margin-top: 30px; background: #311b92; color: #ffffff; padding: 25px; border-radius: 16px; border-left: 8px solid #9575cd;">
<strong style="color: #b39ddb; font-size: 1.1em; display: block; margin-bottom: 8px;">🚀 HILPCB: balanced copper design</strong>
<p style="color: rgba(255,255,255,0.9); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Staggered Traces</strong> снижает twist (I-Beam Effect) и удерживает impedance variation на низком уровне после миллионов bends.</p>
</div>
</div>

### Surface finish и высокочастотные потери

OSP даёт гладкую поверхность и часто минимальный loss, но ограничен по reflow. ENIG/ENEPIG добавляют nickel layer, увеличивающий loss на высоких частотах (>10GHz). Для 28Gbps+ по возможности использовать OSP или Immersion Gold без nickel, балансируя reliability/cost.

### Backdrill quality control

Via stub резонирует (¼ λ) и создаёт провал S21. Backdrill удаляет stub, но требует точного контроля глубины и проверки остатка через TDR/microsection. Без **Backdrill quality control** возможен overdrill и failure.

<div style="background-color:#1A237E; color: #FFFFFF; padding: 20px; border-radius: 8px; margin: 20px 0;">
<h3 style="color:#FFFFFF; text-align:center;">HILPCB high-precision manufacturing capability</h3>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; text-align: center;">
<div style="background-color: #283593; padding: 15px; border-radius: 6px;">
<h4 style="margin: 0 0 10px 0; color:#FFFFFF;">Max layer count</h4>
<p style="margin: 0; font-size: 1.2em;">64L (Rigid), 20L (Rigid-flex)</p>
</div>
<div style="background-color: #283593; padding: 15px; border-radius: 6px;">
<h4 style="margin: 0 0 10px 0; color:#FFFFFF;">Min trace/space</h4>
<p style="margin: 0; font-size: 1.2em;">2.5 / 2.5 mil</p>
</div>
<div style="background-color: #283593; padding: 15px; border-radius: 6px;">
<h4 style="margin: 0 0 10px 0; color:#FFFFFF;">Impedance tolerance</h4>
<p style="margin: 0; font-size: 1.2em;">±5%</p>
</div>
<div style="background-color: #283593; padding: 15px; border-radius: 6px;">
<h4 style="margin: 0 0 10px 0; color:#FFFFFF;">Backdrill depth tol.</h4>
<p style="margin: 0; font-size: 1.2em;">±0.05mm</p>
</div>
</div>
</div>

### Copper coin для локальной термики

**Copper coin** — встраиваемый медный блок, который через Thermal Vias формирует эффективный вертикальный теплопуть. Требует точного контроля и advanced lamination/CNC.

### Как HILPCB обеспечивает consistency manufacturing и тестов

DFM + simulation support, точные **Microvia/stacked via**, строгий **Backdrill quality control**, стабильные **ENIG/ENEPIG/OSP**, измерения VNA/TDR (S-parameters, impedance coupons), а также one-stop сервис до [SMT assembly](https://hilpcb.com/en/products/smt-assembly).

#

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

**Rigid-flex PCB** — уже mainstream технология для миниатюризации, интеграции и high-speed. Успех требует понимания материалов, EM и manufacturing. Стратегическое применение **Hybrid stack-up (Rogers+FR-4)**, **Microvia/stacked via**, **ENIG/ENEPIG/OSP**, **Backdrill quality control** и **Copper coin** помогает выйти за пределы традиционных PCB. С опытным партнёром вроде HILPCB сложные rigid-flex designs превращаются в высокопроизводительные продукты.

