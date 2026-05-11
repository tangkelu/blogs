# P4-504 Reset Quiet-Routing Candidate Scout No-Reopen Successor

Date: 2026-05-11
Execution mode: `subagent_aided_residual_candidate_scout`
Model: `gpt-5`
Lane owner: `P4-504 handbook residual scout for 【PCB必备】194页-PCB设计规范经验之书.pdf`

## Purpose

Recheck whether the `194页 RK3588 handbook` phrases around `RESETn / nPOR`, pin-side filter parts, and noise avoidance are now strong enough and non-overlapping enough to justify one more independent `D5` authority lane.

This pass does not land a new fact card unless the lane clears both bars:

1. materially stronger primary authority than handbook wording alone
2. low enough overlap with already-landed quiet-routing, entry-path, and local-placement boundaries

## Input Files Inspected

- `/code/blogs/tmps/PCB资料/【PCB必备】194页-PCB设计规范经验之书.pdf`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-194页-PCB设计规范经验之书/pages/page-0107.txt`
- `/code/blogs/tmps/pcb_pdf_extracted_full/PCB必备-194页-PCB设计规范经验之书/pages/page-0168.txt`
- `/code/blogs/llm_wiki/logs/p4-282e-2026-5-7-rk3588-handbook-lane-emc-esd-and-dfm-review-boundaries.md`
- `/code/blogs/llm_wiki/logs/p4-402-2026-5-10-d5-connector-adjacent-esd-entry-path-boundary-route.md`
- `/code/blogs/llm_wiki/logs/p4-468-2026-5-11-d3-remote-feedback-and-quiet-sense-point-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/connector-adjacent-esd-protection-and-entry-path-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/remote-feedback-and-quiet-sense-point-routing-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/processor-power-pin-local-decoupling-capacitor-placement-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/power-pin-and-decoupling-dedicated-plane-connection-boundary.md`
- `/code/blogs/llm_wiki/facts/methods/switch-mode-power-emc-placement-and-hot-loop-boundary.md`

## Candidate Evidence Rechecked

Handbook-side phrases recovered in this scout:

- `RESETn复位信号远离板边缘和金属接插件`
- `RESETn复位信号的滤波电容需要尽量靠近其所对应的芯片管脚放置`
- `RESETn复位信号需要远离DCDC,RF等干扰强的信号`
- `RK3588 nPOR管脚的100nF电容必须靠近管脚`

Primary-source family checked in this scout:

- TI reset-trace layout wording around noisy signals, board edge, and local reset capacitor placement
- Microchip reset-noise / RC-filter wording in noisy-environment framing
- Microchip reset-line routing care and local reset-side passive placement wording

## Overlap Recheck

### 1. The lane does not clear the current non-overlap bar

- `connector-adjacent-esd-protection-and-entry-path-boundary` already owns `source -> protection -> protected IC` entry-path posture and explicitly keeps reset-line recipes out of scope.
- `remote-feedback-and-quiet-sense-point-routing-boundary` already owns one quiet, short, noise-sensitive routing family away from switching-noise regions.
- `switch-mode-power-emc-placement-and-hot-loop-boundary` already owns the local noise-region avoidance posture around `DCDC` and other switching-power disturbance sources.
- `processor-power-pin-local-decoupling-capacitor-placement-boundary` and `power-pin-and-decoupling-dedicated-plane-connection-boundary` already absorb much of the currently recoverable `near-pin local passive placement` posture, even though they are not reset-specific.

### 2. The lane still lacks a clean enough reset-specific residual above those cards

- no direct landed `RESETn` or `nPOR` fact or source exists today
- however, the remaining recoverable wording mostly decomposes into already-landed sub-surfaces:
  - quiet sensitive routing
  - avoidance of noisy switching regions
  - connector or board-edge exposure awareness
  - local near-pin passive placement
- what remains most reset-specific is still too close to handbook recipe territory such as exact capacitor value, exact via handling, exact topology ordering, or exact RK3588 implementation detail

## Route Decision

- `no_new_fact_card_landed`
- `no_new_source_record_landed`
- `no_handbook_successor_count_change`
- `candidate_stays_below_reopen`

Updated:

- `/code/blogs/llm_wiki/logs/backlog.md`
- `/code/blogs/llm_wiki/logs/phase-status.md`
- `/code/blogs/llm_wiki/logs/update-log.md`

## Why It Stayed Below Reopen

- the candidate is real enough to track as handbook claim inventory
- it is not clean enough yet to justify another reusable fact card without repeating already-landed logic
- future reopen would need materially stronger reset-specific authority that exceeds the current quiet-routing and local-placement ceiling rather than merely resembling it

## What This Scout Fixes

- future AI should not assume that `RESETn / nPOR` automatically clears the reopen bar just because no fact card is named after reset yet
- future AI should not reopen this candidate on the same source layer unless a stronger reset-specific source appears above the current overlap ceiling
- current handbook state remains at the prior `four D3 routes plus five D5 routes` ceiling
