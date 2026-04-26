# P4-06 NQ-4 First Micro-Batch Closeout

Date: 2026-04-26

## Purpose

This note closes the first execution slice of `NQ-4` from `logs/p4-06-safe-wave-draft-feasibility-and-high-density-gap-queue.md`.

It records that the first `NQ-4` micro-batch is complete, that the queue has now passed its first payoff check, and that the remaining named-product tail is now split between `hold` and `close_as_not_needed` rather than automatic second-batch expansion.

This note is a micro-batch closeout and control document.

It is not:

- a full `NQ-4` queue closeout
- permission to reopen generic `FR-4`
- permission to reopen generic rigid-flex `polyimide / Kapton / UPILEX`
- permission to restore capability, standards, SI, PDN, thermal, or reliability numerics

## What Landed In This Micro-Batch

The first `NQ-4` micro-batch is now complete across two narrow lanes:

1. `FR-4` family-shortcut cleanup
2. flex exact-product normalization

Landed outputs:

- [isola-is410.md](/code/blogs/llm_wiki/facts/materials/isola-is410.md)
- [isola-370hr.md](/code/blogs/llm_wiki/facts/materials/isola-370hr.md)
- [isola-fr408.md](/code/blogs/llm_wiki/facts/materials/isola-fr408.md)
- [isola-fr408hr.md](/code/blogs/llm_wiki/facts/materials/isola-fr408hr.md)
- [p4-06-14-layer-evidence-pack.md](/code/blogs/llm_wiki/logs/p4-06-14-layer-evidence-pack.md) now carries `Arlon 85NT` as a guarded exact-product polyimide anchor

## What This Micro-Batch Changed

The first `NQ-4` micro-batch changed three things:

- safe-wave packs no longer need to lean as heavily on grouped Isola `FR-4 / high-Tg` examples when `IS410`, `370HR`, `FR408`, and `FR408HR` are the real recurring product names
- the current `14-layer` pack no longer understates the repo's flex exact-product layer by implying the usable polyimide anchor is only Panasonic-shaped
- `NQ-4` has now proven that part of the queue was a bounded exact-product hygiene pass, not a broad material expansion project

## What The Multi-Agent Reassessment Found

After the first micro-batch landed, multi-agent reassessment was run on lower-priority named-product candidates.

Current result:

- `Kapton HN`: `hold`
- `UPILEX-S`: `hold`
- `Shengyi S1150G`: `hold`
- `Shengyi S1141`: `hold`
- `ITEQ IT-180GF`: `close_as_not_needed`
- `ITEQ IT-140`: `close_as_not_needed`
- `ITEQ IT-158`: `close_as_not_needed`

Current reasons:

- these names do not yet have landed governed exact-product support strong enough to justify immediate admission
- current safe-wave packs do not gain enough near-term evidence-pack payoff from admitting them
- admitting `Kapton HN` or `UPILEX-S` now would create more branch-broadening pressure around generic rigid-flex `polyimide / Kapton / UPILEX` than exact-product payoff
- admitting `S1150G` now would widen the material queue without improving the current first-order safe-wave exact-product pressure as clearly as the landed Isola batch did
- admitting `S1141` now would widen the Shengyi queue without beating the current `S1000-2 / S1000-2M` high-Tg anchors in immediate safe-wave payoff
- `ITEQ IT-180GF / IT-140 / IT-158` do not justify new exact-product cards because current safe-wave material slots are already served by governed nearby support such as `IT-180A`, existing family-level `FR-4` handling, and current halogen-free context

## What This Closeout Does Not Mean

This micro-batch closeout does not mean:

- `NQ-4` is fully complete
- any lower-priority named-product candidate is now approved for a second batch
- generic `FR-4` or generic flex-material coverage is reopened
- any capability, standards, SI, thermal, or rigid-flex reliability numerics are now recoverable
- high-density draft readiness has materially changed

Current reality remains:

- safe-wave exact-product hygiene: stronger
- broad numeric readiness: unchanged

## Queue Effect

After this closeout:

- the first `NQ-4` micro-batch should be treated as complete
- `NQ-4` remains active only as a reassessment queue for lower-priority named-product gaps
- any second `NQ-4` batch still requires a separate payoff check before card creation

## Recommended Tracking Wording

Recommended wording:

- `NQ-4 first micro-batch is now closed after landing exact-product Isola cleanup plus Arlon 85NT pack normalization`
- `Kapton HN, UPILEX-S, and S1150G were reassessed and remain held because current safe-wave payoff is lower than branch-broadening risk`
- `Shengyi S1141` was reassessed and remains held because the current Shengyi exact-product anchors already cover the active safe-wave need
- `ITEQ IT-180GF, IT-140, and IT-158 were reassessed and closed as not needed for the current narrow NQ-4 scope`
- `NQ-4 remains active only as a narrow reassessment queue, not as a broad material expansion pass`

## Minimal One-Line Control Posture

- `NQ-4` first micro-batch is now complete, but lower-priority named-product candidates remain held, so the queue stays narrow and does not reopen generic `FR-4`, generic flex-material, or any blocked numeric branches
