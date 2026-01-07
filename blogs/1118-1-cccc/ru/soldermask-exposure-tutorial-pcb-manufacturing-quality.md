---
title: "soldermask exposure tutorial: white paper по PCB manufacturing и quality management"
description: "Подробный soldermask exposure tutorial: process capability, yield improvement, quality tools, test coverage и traceability—плюс DFM/DFT/DFR checklist для совместной оптимизации с заказчиком."
category: technology
date: "2025-11-18"
featured: true
image: ""
readingTime: 9
tags: ["soldermask exposure tutorial", "smt stencil design tutorial", "x ray inspection checklist", "pcb fabrication process steps"]
---
## 1. Executive summary: цели качества и business metrics

В HILPCB качество — это основа операционной системы, а не отдельная инспекция. В этом white paper мы описываем end‑to‑end quality management по цепочке fabrication → assembly → test и показываем, как data‑driven process control, quality tools и DFM/DFT/DFR‑кооперация позволяют выпускать PCB выше ожиданий клиента.

Как точный **soldermask exposure tutorial** задаёт ключевые параметры exposure (energy, alignment, time) для защиты трасс и точного открытия pads, так и система HILPCB переносит такой же уровень контроля на каждый этап от входных материалов до отгрузки. Цель — “zero defect”, измеряемая:

* **FPY:** > 99.5%  
* **CPK:** ключевые процессы > 1.67  
* **PPM:** < 100  
* **OTD:** > 98%

<div class="div-type-1">
    <h3>Core capability highlights</h3>
    <p>Quality в HILPCB — это культура. Мы инвестируем в automation, цифровые системы и обучение, соединяя lean manufacturing и Industry 4.0, чтобы обеспечить стабильность и предсказуемость от prototype до volume.</p>
</div>

---

## 2. Manufacturing capability data: от чертежа к физической плате

| Process Step | Key Capability | Process Control Metrics | Mass Production Case |
| :--- | :--- | :--- | :--- |
| **Inner-layer imaging** | Min line/space: 2.5/2.5 mil | Post-etch width tolerance: ±10% | 5G base-station RF unit |
| **Drilling** | Min mechanical drill: 0.15mm; laser: 0.075mm | Hole position: ±0.025mm; wall roughness: < 25μm | Medical endoscope sensor board |
| **PTH & plating** | Hole copper: > 20μm; uniformity: > 90% | Plating CPK > 1.67; panel uniformity < 15% | Automotive ADAS controller |
| **Outer-layer imaging** | Registration: ±12.5μm | AOI coverage: 100%; false-call rate < 5% | HPC server motherboard |
| **Soldermask** | LDI exposure, min dam: 0.05mm | Mask thickness: 10–20μm (pads); alignment CPK > 2.0 | Consumer wearable device |
| **Surface finish** | ENIG/HASL/OSP/ImmAg/ImmSn | ENIG Au: 0.03–0.08μm; salt spray > 48h | Industrial PLC module |
| **Profiling** | Dim tolerance: ±0.1mm | V-Cut: ±0.05mm; CNC outline: ±0.075mm | Drone flight-control system |

В soldermask‑процессе мы следуем принципам **soldermask exposure tutorial**. Используя LDI вместо film exposure, мы убираем ошибки из‑за растяжения пленки и обеспечиваем точные openings для fine‑pitch BGA/QFN, предотвращая bridging.

---

## 3. Quality tools: data-driven оптимизация процесса

- **SPC** на plating/etch/lamination, контрольные карты.
- **CPK** внутренний стандарт > 1.67.
- **MSA** (GR&R) для валидных измерений.
- **8D** + замыкание в FMEA.
- цифровые dashboards FPY/PPM/OEE.

<div class="div-type-6">
    <h3>Our manufacturing strength</h3>
    <p>Мы интегрируем quality tools и цифровые системы в платформу, которая умеет диагностировать, оптимизировать и предотвращать проблемы, снижая quality risk.</p>
</div>

---

## 4. SMT/assembly capability и defect control

Наша DFM‑практика детальна как **smt stencil design tutorial**. Ключевые точки: 3D SPI 100%, pick&place 01005/0.3mm pitch BGA, отдельные reflow profiles, AOI до/после, X‑ray 2D/3D с **x ray inspection checklist** (Voiding <25%, bridging, Head‑in‑Pillow, alignment).

---

## 5. Test coverage: многоуровневая валидация

| Test Type | Description | Coverage | Target Defects |
| :--- | :--- | :--- | :--- |
| **ICT** | Probes test points; checks opens/shorts and values. | 85%–95% component-level defects | Opens, shorts, wrong/missing parts, wrong values |
| **FPT** | Flying probes without nail bed. | 80%–90% component-level defects | Similar to ICT with higher flexibility |
| **FCT** | End-use simulation; validates functions. | 100% functional modules | Functional failures, out-of-spec, logic errors |
| **Hipot** | High-voltage insulation/clearance test. | Safety-critical power paths | Breakdown, insufficient clearance |
| **Burn-in** | Long run under harsh conditions. | 100% finished products | Early-life failures, latent solder defects |
| **Reliability tests** | Temp cycling, vibration, drop, salt spray. | Sampling or per customer | Insufficient margin, poor robustness |

---

## 6. Traceability: жизненный архив от компонентов до изделия

Serial/barcode с bare board; привязка lots материалов; автоматический сбор параметров SPI/placement/reflow/AOI; интеграция ICT/FCT; data lake + визуализация для быстрого RCA и точного recall‑scope.

---

## 7. DFM/DFT/DFR checklist: совместная оптимизация

Checklist охватывает: materials/stackup, soldermask dam, via-in-pad, panelization, fiducials, stencil apertures, test points, JTAG/SWD, thermal, ESD, conformal coating и др.

<div class="div-type-3">
    <h3>Collaborative improvement path</h3>
    <p><strong>Early design involvement:</strong> до Gerber‑release мы можем выполнить DFM/DFT/DFR оценку по schematic/ME и убрать риски на ранней стадии.</p>
</div>

---

## 8. Case study и call to action

Кейс medical PCBA: voiding BGA >30% + crosstalk → FCT <80%. Действия: Via-in-Pad resin plug + planarization, оптимизация stencil, SI sim + reroute/stackup + ground vias, +3 RF test points. Итог: voiding <5%, FPY **99.7%**, -6 недель.

[**Свяжитесь с engineering team для бесплатного DFM review**](/contact-us)

<!-- COMPONENT: BlogQuickQuoteInline -->

## Conclusion

Этот материал описывает process capability, yield improvement, quality tools, test coverage и traceability, а также DFM/DFT/DFR checklist. Раннее подключение HILPCB DFM/DFA ускоряет prototype и volume при сохранении качества и compliance.

> Для fabrication/assembly: [Turnkey Assembly](https://hilpcb.com/en/products/turnkey-assembly) или [SMT Assembly](https://hilpcb.com/en/products/smt-assembly).

