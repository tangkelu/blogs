---
title: "data-center 112G SerDes routing: Ограничения SI для ultra‑high-speed и low‑loss каналов"
description: "Разбор data-center 112G SerDes routing: channel budget, материалы, stack-up, Impedance Control, via/connector transitions, DFM и валидация для high-speed SI PCB."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 8
tags: ["data-center 112G SerDes routing", "112G SerDes routing guide", "112G SerDes routing low volume", "high-speed 112G SerDes routing", "112G SerDes routing layout", "112G SerDes routing impedance control"]
---
На фоне взрывного роста AI/ML и cloud computing трафик внутри data center увеличивается беспрецедентно. Чтобы успевать, индустрия быстро переходит с 56G NRZ/PAM4 на 112G PAM4 SerDes. Это не просто “x2 скорость”: требования к SI становятся намного жестче. Успешная **data-center 112G SerDes routing** — это system engineering на стыке материалов, EM, термики и precision manufacturing. С точки зрения measurement/compliance разберем ключевые сложности 112G и практические меры.

От BGA pads в package, через трассы PCB и vias, через connector/backplane до приемника — канал определяет, восстановится ли 112G. Дискретности импеданса, избыточный dielectric loss или неудачные vias быстро “съедают” бюджет и приводят к BER. Полная стратегия **high-speed 112G SerDes routing** должна учитывать материалы, stack-up, Impedance Control и производственные допуски с самого начала.

### Почему channel budget для 112G такой жесткий?

112G PAM4 имеет Nyquist 28 GHz, поэтому loss/noise становятся критичными. В сравнении с NRZ глаз PAM4 сжат по вертикали до 1/3 и SNR margin падает. Поэтому Insertion Loss (IL) budget — один из главных constraints для **data-center 112G SerDes routing**.

Типичный 112G LR‑канал ограничивают ~30–35 dB @ 28GHz, распределяя по package, PCB, vias, connector и Rx.

- **Insertion Loss (IL):** основная проблема; FR-4 слишком loss при 28 GHz.
- **Return Loss (RL):** отражения из-за дискретностей; дают ISI.
- **Crosstalk:** высокая плотность → NEXT/FEXT и падение SNR.
- **COM:** Channel Operating Margin учитывает IL/RL/crosstalk и Equalizer; COM‑оптимизация стала стандартом.

Чтобы вписаться в бюджет, нужны точные end‑to‑end модели и тесная работа с опытным производителем (например HILPCB).

### Low‑loss материалы: фундамент 112G

На 28 GHz Dk/Df определяют затухание. Выбор материалов — первый шаг для **data-center 112G SerDes routing**.

- **Dk/Df:** часто нужны Ultra Low Loss материалы (Df < 0.004 @ 10GHz): Tachyon 100G, Megtron 6/7/8, Rogers RO4000. Стабильность Dk важна для **112G SerDes routing impedance control**.
- **Skin Effect:** ток у поверхности → выше потери.
- **Copper Roughness:** шероховатость увеличивает loss; использовать VLP/HVLP.
- **Fiber Weave Effect:** стекло vs смола → локальные вариации Dk, ripple импеданса и skew; Spread Glass и угол трассировки 1–5°.

<div style="background-color:#F5F7FA; padding:20px; border-radius:8px; margin: 20px 0;">
<h3 style="text-align:center; color:#000000;">Сравнение материалов high-speed PCB</h3>
<table style="width:100%; border-collapse:collapse; text-align:center;">
<thead style="background-color:#E0E0E0;">
<tr>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Класс</th>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Материалы</th>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Df @ 10GHz</th>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Dk @ 10GHz</th>
<th style="padding:10px; border:1px solid #ccc; color:#000000;">Скорость</th>
</tr>
</thead>
<tbody>
<tr>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Standard loss</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">FR-4 (Standard)</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~0.020</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~4.5</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">< 5 Gbps</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Medium loss</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">FR408HR / S1000-2</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~0.010</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~3.6</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">10-28 Gbps</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Low loss</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Megtron 4 / I-Speed</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~0.005</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~3.4</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">28-56 Gbps</td>
</tr>
<tr>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Ultra low loss</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">Megtron 6 / Tachyon 100G</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">< 0.002</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">~3.0</td>
<td style="padding:10px; border:1px solid #ccc; color:#000000;">56-112G+ Gbps</td>
</tr>
</tbody>
</table>
</div>

### Точный Impedance Control и дисциплина трассировки

В **high-speed 112G SerDes routing** любое отклонение от 90Ω/100Ω diff увеличивает отражения и jitter. Нужны точный stack-up (Polar Si9000), match P/N (1–2 mil), отсутствие 90°, непрерывные reference planes и контроль процесса (etch/lamination/TDR).

### Vias и connector transitions

- **Via Stub:** резонансы и notch в S21; **Back-drilling** для stub 5–10 mil.
- **Via optimization:** 3D EM (HFSS, CST) для pad/antipad/barrel.
- **Connector footprint:** QSFP-DD/OSFP co‑optimization; Non-Circular Pad и локальные вырезы земли.
- Microvias и blind/buried vias в [HDI PCB](https://hilpcb.com/en/products/hdi-pcb).

<div style="background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); color: #ffffff; padding: 40px 30px; margin: 30px 0; border-radius: 24px; font-family: system-ui, -apple-system, sans-serif; border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);">
<h3 style="text-align: center; color: #a78bfa; margin: 0 0 10px 0; font-size: 1.85em; font-weight: 800; letter-spacing: 0.5px;">📡 112G SerDes PHY: правила для vias и переходов</h3>
<p style="text-align: center; color: rgba(255, 255, 255, 0.6); font-size: 1.05em; margin-bottom: 40px; font-weight: 500;">Непрерывность импеданса и подавление common-mode в PAM4</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px;">
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">01. Stub и Back-drill</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Правило:</strong> stub **&lt;8 mil** и full‑depth back-drill, чтобы увести первую резонансную точку &gt;40GHz.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">02. Antipad через 3D EM</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Правило:</strong> co‑optimize antipad/pad в <strong>3D full-wave EM</strong> и держать variation diff в **±5%**.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">03. Shadowing Vias</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Правило:</strong> **2–4** GND return vias вокруг пары diff для изоляции лучше **-40dB**.</p>
</div>
<div style="background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 20px; padding: 25px; border-top: 5px solid #8b5cf6;">
<strong style="color: #a78bfa; font-size: 1.15em; display: block; margin-bottom: 12px;">04. Breakout BGA и процесс</strong>
<p style="color: rgba(255, 255, 255, 0.85); font-size: 0.92em; line-height: 1.7; margin: 0;"><strong>Правило:</strong> для 0.8mm pitch и меньше — **VIPPO**; при dog‑bone компенсировать ширину короткого сегмента.</p>
</div>
</div>
<div style="margin-top: 35px; padding: 25px; background: rgba(139, 92, 246, 0.1); border-radius: 16px; border-left: 8px solid #8b5cf6; font-size: 0.95em; line-height: 1.7; color: #ddd6fe;">
💡 <strong>Note:</strong> успех 112G часто зависит от <strong>Back-drill Tolerance</strong>. Подтвердите Laser Back-drilling/T-Control, чтобы избежать неожиданных notch.
</div>
</div>

### Layout и equalization

Spacing 3W/5W, Guard Trace, Stripline предпочтительнее для длинных линий, ортогональная трассировка соседних слоев, аккуратный breakout без сильного дробления reference planes. PDN noise → jitter, поэтому decoupling и PDN simulation обязательны. Equalization: Tx FFE (Pre/De‑emphasis), Rx CTLE/DFE; используйте IBIS-AMI и оптимизируйте COM.

<div style="background: #0f172a; padding: 30px; border-radius: 24px; margin: 25px 0; border: 1px solid rgba(255, 255, 255, 0.1); box-shadow: 0 20px 40px rgba(0,0,0,0.4); font-family: system-ui, -apple-system, sans-serif;">
<h3 style="text-align: center; color: #f8fafc; margin: 0 0 5px 0; font-size: 1.6em; font-weight: 700;">📊 112G PAM4: отчет sign-off симуляции</h3>
<p style="text-align: center; color: #94a3b8; font-size: 0.95em; margin-bottom: 30px;">COM summary</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 20px;">
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 16px; text-align: center;">
<h4 style="margin: 0 0 12px 0; color: #94a3b8; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px;">IL</h4>
<p style="margin: 10px 0; font-size: 1.8em; font-weight: 800; color: #f43f5e;">-32.0 <span style="font-size: 0.5em;">dB</span></p>
<div style="background: rgba(244, 63, 94, 0.1); color: #fb7185; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 8px;">Nyquist: 28 GHz</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; font-size: 0.85em; color: #64748b;">Target: &lt; -35 dB</div>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 16px; text-align: center;">
<h4 style="margin: 0 0 12px 0; color: #94a3b8; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px;">COM</h4>
<p style="margin: 10px 0; font-size: 1.8em; font-weight: 800; color: #10b981;">4.5 <span style="font-size: 0.5em;">dB</span></p>
<div style="background: rgba(16, 185, 129, 0.1); color: #34d399; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 8px;">PASS</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; font-size: 0.85em; color: #64748b;">IEEE: &gt; 3.0 dB</div>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255,  255, 255, 0.1); padding: 20px; border-radius: 16px; text-align: center;">
<h4 style="margin: 0 0 12px 0; color: #94a3b8; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px;">ILD</h4>
<p style="margin: 10px 0; font-size: 1.8em; font-weight: 800; color: #38bdf8;">1.2 <span style="font-size: 0.5em;">dB</span></p>
<div style="background: rgba(56, 189, 248, 0.1); color: #7dd3fc; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 8px;">Ripple: good</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; font-size: 0.85em; color: #64748b;">Target: &lt; 2.0 dB</div>
</div>
<div style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255,  255, 255, 0.1); padding: 20px; border-radius: 16px; text-align: center;">
<h4 style="margin: 0 0 12px 0; color: #94a3b8; font-size: 0.9em; text-transform: uppercase; letter-spacing: 1px;">ERL</h4>
<p style="margin: 10px 0; font-size: 1.8em; font-weight: 800; color: #10b981;">12.5 <span style="font-size: 0.5em;">dB</span></p>
<div style="background: rgba(16, 185, 129, 0.1); color: #34d399; padding: 4px 12px; border-radius: 20px; font-size: 0.85em; display: inline-block; margin-bottom: 8px;">OK</div>
<div style="border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 10px; font-size: 0.85em; color: #64748b;">Target: &gt; 9.5 dB</div>
</div>
</div>
<div style="margin-top: 25px; padding: 15px; background: rgba(56, 189, 248, 0.05); border-radius: 12px; border-left: 4px solid #38bdf8; font-size: 0.9em; color: #cbd5e1; line-height: 1.6;">
💡 <strong>Note:</strong> IL = -32dB, запас до -35dB — 3dB. Перед серией выполните Monte Carlo по <strong>HVLP copper roughness</strong>.
</div>
</div>

### DFM и тестирование

Учитывайте допуски (Monte Carlo), выбирайте surface finish ENIG/ENEPIG с учетом reliability, выполняйте DFM до Gerber/ODB++. Валидируйте VNA (S‑parameters), TDR и Eye/BER (BER < 1E-6).

#

<!-- COMPONENT: BlogQuickQuoteInline -->

## Заключение

Успешная **data-center 112G SerDes routing** требует end‑to‑end подхода: ultra low‑loss материалы, точный stack-up/Impedance Control, оптимизация vias/connectors и приоритет DFM. Рассматривайте канал как единую систему, используйте EM/IBIS-AMI симуляции и подтверждайте измерениями. Партнер типа HILPCB ускоряет вывод продукта и помогает удерживать производственную повторяемость для 112G и выше.

