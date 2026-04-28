---
fact_id: "materials-kingboard-material-selection-boundaries"
title: "Kingboard material selection boundaries"
topic: "Kingboard laminate selection"
category: "materials"
status: "verified"
confidence: "high"
must_refresh: false
reviewed_at: "2026-04-27"
source_ids:
  - "kblaminates-kb-6150-technical-information"
  - "kblaminates-kb-6160-kb-6060-technical-information"
  - "kblaminates-kb-6164-kb-6064-technical-information"
  - "kblaminates-kb-6165-kb-6065-technical-information"
  - "kblaminates-kb-6165f-kb-6065f-technical-information"
  - "kblaminates-kb-6167f-kb-6067f-technical-information"
  - "kblaminates-hf-140-pp-hf140-technical-information"
  - "kblaminates-hf-170-pp-hf170-technical-information"
  - "kblaminates-kb-3200g-pp-kb3200g-technical-information"
  - "kblaminates-pi-520g-pp-pi520g-technical-information"
  - "kblaminates-kb-6160a-kb-6060a-technical-information"
  - "kblaminates-kb-6160f-kb-6060f-technical-information"
  - "kblaminates-kb-6160lc-technical-information"
  - "kblaminates-kb-6160lc-c-technical-information"
  - "kblaminates-kb-6165c-kb-6065c-technical-information"
  - "kblaminates-kb-6165le-kb-6065le-technical-information"
  - "kblaminates-kb-6167gmd-kb-6067gmd-technical-information"
  - "kblaminates-kb-6167gld-kb-6067gld-technical-information"
  - "kblaminates-kb-6168le-kb-6068le-technical-information"
  - "kblaminates-kb-6169gt-kb-6069gt-technical-information"
  - "kblaminates-pi-515g-pp-pi515g-technical-information"
tags: ["kingboard", "kblaminates", "selector", "tier-normalization", "materials"]
---

# Canonical Summary

> Kingboard material selection can be described as source-scoped product positioning across FR-4, low-CTE, high-Tg, halogen-free, low-loss, and PI-series families. It must not become a cost ladder, portfolio ranking, or speed-to-material mapping.

## Safe Groupings

- Conventional normal-Tg FR-4: `KB-6150`, `KB-6160`, `KB-6160A`.
- Low-CTE / modified standard FR-4: `KB-6160F`, `KB-6160LC`, `KB-6160LC(C)`, `KB-6164`, `KB-6165`, `KB-6165F`, `KB-6165C`, `KB-6165LE`.
- High-Tg / low-CTE FR-4: `KB-6167F`, `KB-6168LE`.
- Halogen-free normal/high-Tg: `HF-140`, `HF-170`.
- Halogen-free or low-loss digital material examples: `KB-3200G`, `KB-6167GMD`, `KB-6167GLD`.
- High-Tg / PI-series halogen-free examples: `PI-515G`, `PI-520G`.
- High-Tg / high-CTI exact-product example: `KB-6169GT`.

## Correction Notes

- `KB-6160` is anchored to the current official PDF values: `Tg 138 C`, `Td 310 C`, `Dk 4.4 @ 1 GHz`, and `Df 0.018 @ 1 GHz`. Older draft values are not reusable unless separately sourced.
- `KB-6165` `Td` is source-scoped to official `Td 348 C`.
- `PI-520G` does not validate `PI-515G`; both now have separate exact-product sources.
- `KB-3200G`, `KB-6167GMD`, `KB-6167GLD`, and `KB-6169GT` material properties do not validate channel-speed or interface-compliance claims.

## Conditions And Methods

- Use exact-product fact cards for numeric values.
- Use this card only for safe grouping language and blocked-claim hygiene.
- Keep product suffixes intact.

## Limits And Non-Claims

- No cost ladder.
- No portfolio ranking.
- No speed-to-material mapping.
- No PCIe / USB / DDR / Ethernet / PAM4 support claim.
- No application qualification, AEC, PPAP, medical, aerospace, defense, or finished-board compliance proof.
- No HIL/APT stocking, sourcing, supplier-status, lead-time, yield, or capability proof.
- No manufacturing recipe or process-window guarantee.

## Source Links

- https://www.kblaminates.com/
