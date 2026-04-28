# P4-26 Kingboard Official Source Recovery

Date: 2026-04-27

## Purpose

This pass follows `P4-25` by recovering official KBLaminates source records for the Kingboard material drafts under `/code/blogs/tmps/en`.

The goal is not to rewrite blogs. The goal is to promote only official-source-backed product values into reusable `llm_wiki` facts and keep blog-only or estimated claims blocked.

## Sources Added

- `kblaminates-kb-6150-technical-information`
- `kblaminates-kb-6160-kb-6060-technical-information`
- `kblaminates-kb-6160-kb-6060-processing-guide`
- `kblaminates-kb-6164-kb-6064-technical-information`
- `kblaminates-kb-6165-kb-6065-technical-information`
- `kblaminates-kb-6165f-kb-6065f-technical-information`
- `kblaminates-kb-6167f-kb-6067f-technical-information`
- `kblaminates-hf-140-pp-hf140-technical-information`
- `kblaminates-hf-170-pp-hf170-technical-information`
- `kblaminates-kb-3200g-pp-kb3200g-technical-information`
- `kblaminates-pi-520g-pp-pi520g-technical-information`

## Fact Cards Added

- `materials-kingboard-kb-6150`
- `materials-kingboard-kb-6160`
- `materials-kingboard-kb-6164`
- `materials-kingboard-kb-6165`
- `materials-kingboard-kb-6165f`
- `materials-kingboard-kb-6167f`
- `materials-kingboard-hf-140`
- `materials-kingboard-hf-170`
- `materials-kingboard-kb-3200g`
- `materials-kingboard-pi-520g`

## Draft Corrections

- `KB-6160` is now anchored to the current official 2025 KBLaminates PDF, which lists `Tg 138 C`, `Td 310 C`, `Dk 4.4 @ 1 GHz`, and `Df 0.018 @ 1 GHz`. The draft's older `Tg 135 C`, `Td 305 C`, and `Dk 4.25 @ 1 GHz` values must not be reused unless a separate official source is attached.
- `KB-6165` `Td` conflict is resolved for current reuse as `Td 348 C` from the official 2025 KBLaminates PDF.
- `HF-140` and `HF-170` now have official PDF-backed exact-product facts, not merely draft-level claim inventory.
- `KB-3200G` moves from `needs_official_source` to exact-product source-scoped material coverage, but its channel-speed, insertion-loss, and high-speed interface claims remain blocked.
- `PI-520G` moves from source-recovery priority to exact-product source-scoped material coverage; `PI-515G` remains blocked / needs official source.

## Superseded Blocked List

This list was accurate at the end of `P4-26`, but it has been superseded by `P4-28`.

`P4-28` recovered official KBLaminates sources and exact-product facts for:

- `KB-6160A`
- `KB-6160F`
- `KB-6160LC`
- `KB-6160LC(C)`
- `KB-6165C`
- `KB-6165LE`
- `KB-6167GMD`
- `KB-6167GLD`
- `KB-6168LE`
- `KB-6169GT`
- `PI-515G`

No product in the original P4-25 residual list remains blocked for lack of official KBLaminates source.

## Non-Unlocked Claim Families

This batch does not unlock:

- Kingboard portfolio ranking or cost ladder
- generic FR-4 average values
- HIL/APT material stocking, sourcing, lead time, quote speed, cost, or yield claims
- finished-board compliance proof
- application qualification, AEC, PPAP, medical, aerospace, or defense claims
- PCIe / USB / DDR / Ethernet / PAM4 support claims
- insertion-loss budgets, eye margin, BER, VNA/S-parameter promises, or trace-length limits
- maximum layer count, aspect ratio, annular-ring, drilling, registration, or other fabricator capability numerics
- process recipes from the KB-6160 processing guide as transferable manufacturing instructions

## Completion Status

This batch upgrades a substantial portion of `/code/blogs/tmps/en` from claim-family disposition into official exact-product material facts.

The remaining Kingboard drafts were completed in `P4-28` at official exact-product material-property level.
