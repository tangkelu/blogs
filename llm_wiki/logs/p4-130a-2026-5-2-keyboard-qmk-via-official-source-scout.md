# P4-130a 2026-05-02 Keyboard QMK VIA Official Source Scout

Date: 2026-05-02
Lane: `P4-129 lane 1`
Scope: `QMK and VIA official-source scout only`
Status: `completed_at_claim_boundary_level`

## Purpose

Identify the minimum current official pages that can bound `QMK` identity vocabulary, `VIA` identity vocabulary, and conservative `QMK`/`VIA` compatibility-boundary wording for keyboard PCB language.

This pass is scout-only. It does not create source records, fact cards, wiki pages, or draft rewrites.

## Scope Guard

Allowed in this pass:

- official `QMK` pages
- official `VIA` pages
- identity-level vocabulary
- compatibility-boundary wording only

Explicitly out of scope:

- `NKRO`
- `RGB`
- battery
- latency
- market positioning
- HIL capability claims
- controller-family recommendations
- product-performance claims

## Candidate Official Pages

### QMK identity and keyboard metadata boundary

1. `QMK Firmware`
   - URL: `https://docs.qmk.fm/`
   - Why it matters:
     - official identity anchor for `QMK`
     - states QMK is an open-source community centered around computer input devices including keyboards
     - establishes `QMK Firmware`, `QMK Configurator`, `QMK Toolbox`, and the official documentation set as first-party ecosystem vocabulary

2. `info.json Reference | QMK Firmware`
   - URL: `https://docs.qmk.fm/reference_info_json`
   - Why it matters:
     - official keyboard metadata and definition vocabulary
     - supports bounded wording around `keyboard_name`, `manufacturer`, `url`, `processor`, and related keyboard-definition fields
     - useful for conservative PCB-language around keyboard identity metadata without drifting into unsupported feature claims

### VIA identity and compatibility boundary

3. `VIA`
   - URL: `https://caniusevia.com/`
   - Why it matters:
     - official identity anchor for `VIA`
     - establishes VIA as the official configurator/docs surface for compatible keyboards

4. `Configuring QMK | VIA`
   - URL: `https://caniusevia.com/docs/configuring_qmk/`
   - Why it matters:
     - strongest current official bridge between `VIA` compatibility wording and `QMK` implementation vocabulary
     - shows that VIA works by communicating with firmware running on the device across USB
     - shows that enabling the VIA feature in QMK, creating a `via` keymap target, and updating `info.json` / `rules.mk` are part of compatibility setup
     - supports guarded wording that VIA compatibility is configuration-dependent, not automatic

5. `Specification | VIA`
   - URL: `https://caniusevia.com/docs/specification/`
   - Why it matters:
     - official keyboard-definition vocabulary for `VIA`
     - supports bounded use of terms such as keyboard definition, `vendorId`, `productId`, matrix, layouts, and layout options
     - explicitly ties VIA keyboard definition to keyboard identity and matrix/layout structure

6. `Supported Keyboards | VIA`
   - URL: `https://caniusevia.com/docs/supported_keyboards/`
   - Why it matters:
     - official product-level compatibility appendix
     - can bound future exact-board wording when a claim needs a product-specific VIA support anchor
     - should be used cautiously because it is a compatibility list, not a general feature-claim source

## Minimum Recovery Set

If a later source-record pass needs the smallest viable set for this lane, the best minimum pack is:

- `https://docs.qmk.fm/`
- `https://docs.qmk.fm/reference_info_json`
- `https://caniusevia.com/docs/configuring_qmk/`
- `https://caniusevia.com/docs/specification/`

Add `https://caniusevia.com/docs/supported_keyboards/` only when a product-specific `VIA-compatible` claim must be bounded to an official support list.

## Safe Claim Classes

- `QMK` may be described as an official keyboard-firmware ecosystem / documentation authority for programmable input devices including keyboards.
- A keyboard PCB may be described conservatively as `QMK-based` or `designed for QMK firmware` only when the wording stays at firmware-ecosystem identity level.
- `QMK` keyboard-definition vocabulary may safely include `keymap`, `keycodes`, and `info.json` metadata framing.
- `VIA` may be described as an official keyboard configuration ecosystem / configurator authority.
- `VIA-compatible` wording is safe only as bounded compatibility language, not as a universal keyboard attribute.
- Official compatibility vocabulary may refer to:
  - VIA communicating with firmware on the device across USB
  - a separate `via` keymap/build target in `QMK`
  - `info.json` and `rules.mk` configuration relevance
  - keyboard-definition JSON concepts such as `vendorId`, `productId`, matrix, layouts, and layout options
- Product-specific `VIA-supported` wording is only safe when tied to the official `Supported Keyboards` appendix or an exact official keyboard page.

## Blocked Claim Classes

- claims that all custom keyboard PCBs support `QMK`
- claims that all `QMK` keyboards are automatically `VIA-compatible`
- claims that `VIA` compatibility is inherent without exact firmware/configuration support
- claims that a specific unnamed PCB is `VIA-supported`
- claims that `QMK` or `VIA` support proves plug-and-play behavior across all hosts or all operating systems
- `NKRO`, anti-ghosting, RGB, lighting, battery, latency, wireless, or polling claims
- controller-family support claims unless an exact official controller-source lane is opened separately
- HILPCB capability, manufacturing readiness, compliance, or service claims

## Recommended Source-Record Titles

These are recommendations only for a later source-record pass:

- `QMK Firmware Documentation`
- `QMK info.json Reference`
- `VIA Official Site`
- `VIA Configuring QMK`
- `VIA Specification`
- `VIA Supported Keyboards`

## Outcome

Recovery result for this scout:

- `QMK` identity authority: `recoverable_now`
- `VIA` identity authority: `recoverable_now`
- `QMK` / `VIA` compatibility-boundary authority: `recoverable_now`
- exact product-level `VIA-supported` wording: `recoverable selectively from official supported-keyboards appendix`

No blocker prevents a later official-source record pass for identity and compatibility-boundary language.
