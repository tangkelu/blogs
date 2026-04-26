---
fact_id: "materials-ventec-vt-870"
title: "Ventec VT-870 baseline material card"
topic: "VT-870"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-24"
source_ids: ["ventec-vt-870-datasheet", "ventec-tec-speed-rf-family-page"]
tags: ["ventec", "vt-870", "tec-speed-20", "rf-materials", "hydrocarbon-ceramic"]
---

# Canonical Summary

> VT-870 is a Ventec tec-speed 20.0 ceramic-filled hydrocarbon laminate system positioned as a process-friendlier RF option for antenna, power amplifier, automotive radar, and other microwave builds that do not need soft PTFE as the default starting point.

## Stable Facts

- Ventec describes VT-870 as a high-Tg ceramic-filled hydrocarbon laminate and prepreg system.
- The official properties sheet lists `Dk 3.48 +/- 0.05 at 10 GHz` by `IPC-TM-650 2.5.5.5 clamped stripline`.
- The same sheet lists design Dk `3.66` by differential phase length method.
- The same sheet lists `Df 0.0031 at 2.5 GHz` and `Df 0.0037 at 10 GHz` by cavity resonator.
- Ventec lists `Tg 280 C`, `Td 392 C`, `T288 >120 min`, thermal stress at `288 C >600 s`, and UL 94 `V-0`.
- The sheet also lists X/Y/Z CTE values of `10 / 11 / 31 ppm/C`, thermal conductivity `0.69 W/mK`, and lead-free process compatibility `Yes`.
- Ventec states VT-870 is available with both `HTE` and `HVLP` copper foil, and explicitly notes HVLP foil for PIM-sensitive applications.
- The datasheet frames VT-870 around `cellular base station antenna and power amplifiers`, `automotive radar`, `broadcast-satellite LNB`, and `RFID`.
- Ventec states VT-870 conforms to `IPC-4103 /11`.

## Conditions And Methods

- Keep clamped-stripline Dk separate from design Dk.
- Keep laminate values separate from the VT-870PP prepreg table.
- Treat the application list as manufacturer positioning, not as automatic design signoff.

## Limits And Non-Claims

- This card does not claim VT-870 is lower loss than RO3003 or RT/duroid 5880.
- It also does not prove that a hydrocarbon laminate can replace PTFE in every radar or satellite design.

## Open Questions

- Whether to add a dedicated `VT-870 vs RO4350B vs Astra MT77` selector card

## Source Links

- https://www.ventec-group.com/media/1957/180720tecspeed20-vt-870.pdf
- https://www.ventec-group.com/products/tec-speed-rf/
