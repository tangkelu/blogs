---
fact_id: "materials-kingboard-kb-6160"
title: "Kingboard KB-6160 baseline material card"
topic: "KB-6160"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-27"
source_ids:
  - "kblaminates-kb-6160-kb-6060-technical-information"
  - "kblaminates-kb-6160-kb-6060-processing-guide"
tags: ["kingboard", "kblaminates", "kb-6160", "kb-6060", "fr-4", "materials"]
---

# Canonical Summary

> `KB-6160` is an exact-product KBLaminates conventional FR-4 laminate / prepreg system with official technical-information and processing-guide coverage. Current official values supersede the older draft numbers in `/code/blogs/tmps/en/kb-6160-pcb.md`.

## Stable Facts

- KBLaminates identifies `KB-6160` laminate with `KB-6060` prepreg and references `UL E123995`.
- The official table references `IPC-4101E/21`.
- For the stated specimen scope, the table lists thermal stress `>=180 sec` at `Float 288 C / Unetched`, `Tg 138 C` by `IPC-TM-650 2.4.25 DSC`, `T-260 >10 min` by `IPC-TM-650 2.4.24.1 TMA`, and `Td 310 C` by `IPC-TM-650 2.4.24.6 TGA`.
- The table lists Z-axis CTE `Alpha 1 60 ppm/C`, `Alpha 2 300 ppm/C`, and total expansion `4.3%` from `50 to 260 C`.
- The table lists flammability `V-0` by `UL94 E-24/125`.
- The table lists `Dk 4.6 @ 1 MHz` and `Dk 4.4 @ 1 GHz`, plus `Df 0.016 @ 1 MHz` and `Df 0.018 @ 1 GHz`, by `IPC-TM-650 2.5.5.9`, etched, `RC50%`.
- The table lists CTI `>=175 V`, dielectric breakdown `>=45 kV`, arc resistance `125 sec`, water absorption `0.17%`, and flexural strength `600 / 500 N/mm2`.
- The processing guide states its recommendations do not cover all PCB designs or processing environments and must be adjusted for actual use conditions.

## Conditions And Methods

- Keep the specimen note attached: typical value of specimen thickness is `1.6 mm`, `#7628 x 8`.
- Treat all values as typical reference values unless the source states a minimum or other bound.
- Use processing-guide values only as process-sensitivity context, not as universal recipes.

## Limits And Non-Claims

- This card does not authorize use of the draft's stale `Tg 135 C`, `Td 305 C`, or `Dk 4.25 @ 1 GHz` values as current official facts.
- It does not prove lead-free suitability for a particular board, reflow count, via aspect ratio, throughput, cost, or lead time.
- It does not turn drilling or lamination guidance into HIL/APT capability claims.

## Source Links

- https://www.kblaminates.com/en/upload/ueditor/20250313/KB-6160%2CKB-6060.pdf
- https://www.kblaminates.com/en/upload/ueditor/20250528/KB-6160-Processing-Guide.pdf
