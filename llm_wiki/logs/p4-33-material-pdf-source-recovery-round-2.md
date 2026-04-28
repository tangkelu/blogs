# P4-33 Material PDF Source Recovery Round 2

## Purpose

Continue the P4-33 material PDF lane by converting four additional AGC local PDFs into official-source-backed material facts.

This round uses local PDFs found under `/code/blogs/tmps/materias_pdf` as provenance copies. The reusable facts cite official AGC PDF URLs that returned `200 OK` on `2026-04-28`.

## Inputs Inspected

- `/code/blogs/tmps/materias_pdf/AGC_METEORWAVE_8000_TDS.pdf`
- `/code/blogs/tmps/materias_pdf/AGC_N4000-13SI_TDS.pdf`
- `/code/blogs/tmps/materias_pdf/AGC_N7000-3_TDS.pdf`
- `/code/blogs/tmps/materias_pdf/AGC_NF-30_TDS.pdf`

## Added Source Records

- `agc-meteorwave-8000-datasheet`
- `agc-n4000-13si-datasheet`
- `agc-n7000-3-datasheet`
- `agc-nf-30-datasheet`

## Added Fact Cards

- `materials-agc-meteorwave-8000`
- `materials-agc-n4000-13si`
- `materials-agc-n7000-3`
- `materials-agc-nf-30`

## Source-Backed Data Unlocked

- `METEORWAVE 8000`: extremely-low-loss high-speed laminate / prepreg data with separated `2 GHz` and `10 GHz` Dk/Df values, TMA/DMA Tg split, Td, T-300, CTE, Z-expansion, moisture absorption, UL94 / IPC-4101 framing, and minimum laminate-thickness boundary.
- `N4000-13 SI`: high-speed epoxy laminate / prepreg data with `50% resin content` Dk/Df values separated by `2.5 GHz Split Post Cavity` and `10 GHz Stripline`, plus Tg, Td, T-260/T-288, CTE, Z-expansion, moisture absorption, UL94 / IPC-4101 framing, and design-dependent lead-free assembly note.
- `N7000-3`: toughened polyimide laminate / prepreg data with distinct `1 GHz`, `2.5 GHz`, and `10 GHz` electrical values, DSC Tg, Td, T-260, thermal conductivity, CTE, Z-expansion, moisture absorption, and UL94 / IPC-4101 framing.
- `NF-30`: non-reinforced ceramic-filled PTFE composite data with `10 GHz` IPC Dk/Df values, `77 GHz` microstrip-resonator Dk context, TCDk, Td, thermal conductivity, CTE, T288, moisture absorption, methylene chloride resistance, and processing notes.

## Safe Reuse Classes

- Exact-product material identity and AGC application framing.
- Numeric material properties only with their stated frequency, method, resin-content, construction, or temperature condition.
- Conservative high-speed, signal-integrity, severe-condition polyimide, microwave, and mmWave material-selection context.

## Blocked Claim Classes

- Finished-board 100 Gbps, backplane, switch, router, radar, automotive, aerospace, avionics, petroleum, burn-in, antenna, GPS, insertion-loss, channel-budget, CAF lifetime, NASA outgassing, or qualification claims.
- APT / HIL / other supplier fabrication capability, process window, laser microvia yield, plasma desmear capability, controlled impedance, certification, quality rate, yield, price, MOQ, stock, or lead time.
- Any claim that AGC typical values are guaranteed customer specification limits.

## Completion Status

- status: `source_backed_fact_layer_partial`
- scope: `four additional AGC material PDFs only`
- cumulative P4-33 material PDF source-backed upgrade: `7` AGC exact-product rows
- next lane: continue source-backed extraction for Rogers candidates while keeping candidate-only logs separate from accepted fact cards.
