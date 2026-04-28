---
fact_id: "materials-ventec-vt-42"
title: "Ventec VT-42 standard FR-4 material card"
topic: "VT-42"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-28"
source_ids: ["ventec-vt-42-datasheet-page"]
tags: ["ventec", "vt-42", "standard-fr4", "fr4", "dicy-cured", "tg140", "laminate", "prepreg"]
---

# Canonical Summary

> VT-42 is a Ventec dicy-cured standard FR4.0 laminate / prepreg with Tg 140 C positioning. It is a baseline FR-4 material row, not a generic default for all FR-4 builds.

## Stable Facts

- Ventec identifies VT-42 as a laminate / prepreg with UL approval `E214381`, version `B4`, IPC-4101E `/21`.
- Ventec frames VT-42 around computer, communication equipment, instrumentation, TV, VCR, electronic game machine, LCD, and automotive contexts.
- The sheet lists Tg `140 C` by DSC / `IPC-TM-650 2.4.25`.
- The same sheet lists Td `310 C` by `ASTM D3850`, T260 `20 min`, T288 `2 min`, and thermal stress at `288 C` as `300 s`.
- The same sheet lists Z-axis CTE before Tg `50 ppm/C`, after Tg `250 ppm/C`, total expansion from `50 C to 260 C` as `3.75%`, X-Y CTE `12~14 ppm/C`, and MOT `130 C`.
- The sheet lists Dk `4.2` at `1 GHz` by `IPC-TM-650 2.5.5.9`.
- The sheet lists Df `0.015` at `1 GHz` by `IPC-TM-650 2.5.5.9`.
- The same sheet lists moisture absorption `0.25%`, CTI `Grade 3 (175~250)`, arc resistance `240 s`, and flammability `V-0`.
- The sheet lists core thickness availability from `0.002 in / 0.05 mm` to `0.200 in / 5 mm`, copper foil availability from `1/4 oz` to `12 oz`, and multiple E-glass styles.

## Conditions And Methods

- Preserve `1 GHz` and IPC-TM-650 `2.5.5.9` on Dk / Df values.
- Treat all data as typical values, matching the source note.
- Treat availability ranges and reverse-treated-copper guidance as Ventec product context, not supplier stock or generic process-window proof.
- Do not use this row as a universal FR-4 average.

## Limits And Non-Claims

- This card does not prove automotive, LCD, communication-equipment, TV, or instrumentation finished-board performance.
- It does not prove supplier build success, product reliability, qualification, or acceptance for a specific stackup.
- It does not prove APT, HIL, or any other supplier certification, yield, price, MOQ, stock, or lead time.

## Source Links

- https://www.ventec-group.com/products/standard-fr4/vt-42/datasheet/
