---
lane: "P4-59C digital priority encoder official-source scout"
title: "Official-source recovery scout for digital priority-encoder identity"
status: "source_backed_fact_layer_partial_candidate"
reviewed_at: "2026-04-30"
owner_scope: "/code/blogs/llm_wiki/logs/p4-59c-2025-11-10-digital-priority-encoder-official-source-recovery-scout.md"
input_files:
  - "/code/blogs/tmps/2025.11.10/en/encoder‑circuit.md"
  - "/code/blogs/llm_wiki/logs/p4-58c-2025-11-10-encoder-circuit-authority-scout.md"
  - "/code/blogs/llm_wiki/logs/p4-58-parallel-scout-controller-summary.md"
---

# Purpose

- Assigned lane: `P4-59C digital priority encoder official-source scout`
- Goal: recover the narrowest official-source-backed lane for `digital priority encoder` identity without carrying over the draft's mixed `mechanical encoder` claims.
- Draft content was treated as claim inventory only, not as authority.
- Edit boundary honored: this output log only.

# Inputs Checked

## Draft and prior internal logs

- `/code/blogs/tmps/2025.11.10/en/encoder‑circuit.md`
- `/code/blogs/llm_wiki/logs/p4-58c-2025-11-10-encoder-circuit-authority-scout.md`
- `/code/blogs/llm_wiki/logs/p4-58-parallel-scout-controller-summary.md`

## Official public sources checked

1. Texas Instruments product page for `SN74LS148`
   - https://www.ti.com/product/SN74LS148
2. Texas Instruments datasheet for `SN74LS148`
   - https://www.ti.com/lit/gpn/sn74ls148
3. Texas Instruments product page for `SN74HC148`
   - https://www.ti.com/product/SN74HC148
4. onsemi datasheet for `MC14532B`
   - https://www.onsemi.com/pdf/datasheet/mc14532b-d.pdf

# Draft Split Result

## Digital logic claim family

- encoder / priority encoder identity
- `8-line to 3-line` or `2^n to n` style compression framing
- highest-priority input wins when multiple inputs are active
- enable / valid / cascade behavior
- example IC references such as `SN74LS148`

## Mechanical encoder claim family

- absolute vs incremental
- rotary vs linear
- single-turn vs multi-turn
- SSI / EnDat / pulse outputs
- IP ratings, vibration, dust, moisture, bearings, couplers, mounting, positioning accuracy, repeatability

## Split conclusion

- The draft is not a single recoverable authority lane.
- `Digital priority encoder` and `mechanical position encoder` are separate identity families and must not be promoted together.

# Official-Source Recovery Findings

## What TI directly supports

From TI product and datasheet pages:

- `SN74LS148` is identified as an `8-line to 3-line priority encoder`.
- TI states that priority decoding ensures only the highest-order data line is encoded.
- TI states the device encodes eight data lines to three-line binary `(octal)`.
- TI states cascading is supported through `EI` / `EO` signals.
- TI states the inputs and outputs for this family are active low.

## What onsemi directly supports

From the `MC14532B` datasheet:

- `MC14532B` is identified as an `8-Bit Priority Encoder`.
- onsemi states the primary function is to provide a binary address for the active input with the highest priority.
- onsemi documents eight data inputs plus an enable input.
- onsemi documents three address outputs plus `GS` and `Eout`.
- onsemi includes a truth table showing the highest-priority-active-input behavior for the device.

## Cross-vendor conclusion

- There is now enough official support to establish that `digital priority encoder` is a standard logic-device category documented by logic vendors.
- There is enough support to name a narrow example-device lane around `8-line to 3-line priority encoder` identity and vendor-documented enable / cascade behavior.
- This support does not justify broad pedagogical claims about all encoder circuits, nor does it justify any mechanical encoder selection guidance.

# Narrowest Promotable Lane

- lane name: `digital priority encoder identity`
- recommended status: `source_backed_fact_layer_partial`
- identity boundary:
  - a digital priority encoder is a logic device family that encodes the highest-priority active input into a smaller binary-address output
  - promotable example devices include vendor-documented `8-line to 3-line priority encoder` parts such as TI `SN74LS148` / `SN74HC148` and onsemi `MC14532B`
  - vendor-documented companion behavior includes enable / group-select / cascade-style signals where explicitly stated by the vendor datasheet

# Exact Conservative Unlock Justified

The exact conservative unlock justified by these sources is:

- promote a small fact layer that says `digital priority encoder` is a standard logic-device category
- support that lane with vendor-specific examples for `8-line to 3-line priority encoder` parts
- allow tightly scoped statements that these example devices encode the highest-priority active input and expose vendor-documented enable or cascade-related pins

This unlock does **not** justify:

- promoting the draft's general `2^n input to n output` teaching as a universal sourced rule
- promoting generic Boolean equations, troubleshooting rules, fan-in advice, DFM advice, PCB layout advice, or application claims beyond vendor-labeled examples
- promoting `SN74LS148` as a current procurement recommendation without product-status qualification
- promoting any mechanical encoder content from this draft

# Blocked Claims

## Still blocked in the digital lane

- universal or textbook-level encoder definitions not directly tied to the sourced vendor devices
- the draft's worked truth tables and Boolean expressions as general teaching content
- broad application claims such as memory address decoding, interrupt prioritization, I/O expansion, multiplexers, demultiplexers, and signal compression unless separately sourced for those uses
- troubleshooting claims such as floating-input behavior, startup-invalid behavior, or heavy fan-in optimization as reusable wiki facts
- any unsourced numeric performance, power, delay, loading, or compatibility claims beyond what a specific vendor page states for a specific part

## Fully blocked mechanical lane

- absolute / incremental
- rotary / linear
- single-turn / multi-turn
- SSI / EnDat / pulse-output framing
- IP ratings, environmental durability, bearing or coupler selection
- positioning accuracy, repeatability, response time, fail-safe installation guidance

# Residual Gaps

- no local `sources/`, `facts/`, or `wiki/` record has been created yet for this recovered lane
- no separate official-source lane has yet been built for `simple binary encoder` identity apart from `priority encoder`
- no separate official-source lane has yet been built for the draft's application examples
- no official-source mechanical encoder lane has been recovered

# Promotion Judgment

- Does this lane now appear promotable to `source_backed_fact_layer_partial`?
  - `Yes`, but only for the narrow `digital priority encoder identity` lane described above.
- Is the full mixed `encoder-circuit.md` draft promotable?
  - `No`.

# Changed Files

- `/code/blogs/llm_wiki/logs/p4-59c-2025-11-10-digital-priority-encoder-official-source-recovery-scout.md`

