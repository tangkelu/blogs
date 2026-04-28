# P4-33 Material PDF Source Recovery Round 1

## Purpose

Move part of the P4-33 material PDF lane beyond claim-family inventory into source-backed reusable material facts.

This round uses local PDFs found under `/code/blogs/tmps/materias_pdf` only as preserved provenance copies. The reusable facts cite official AGC PDF URLs that were checked on `2026-04-28`.

## Inputs Inspected

- `/code/blogs/tmps/materias_pdf/AGC_RF-60TC_TDS.pdf`
- `/code/blogs/tmps/materias_pdf/AGC_RF-35TC_TDS.pdf`
- `/code/blogs/tmps/materias_pdf/AGC_METEORWAVE_4000_TDS.pdf`

## Added Source Records

- `agc-rf-60tc-datasheet`
- `agc-rf-35tc-datasheet`
- `agc-meteorwave-4000-datasheet`

## Added Fact Cards

- `materials-agc-rf-60tc`
- `materials-agc-rf-35tc`
- `materials-agc-meteorwave-4000`

## Source-Backed Data Unlocked

- `RF-60TC`: PTFE-based ceramic-filled fiberglass RF material with `Dk 6.15 +/- 0.15 at 10 GHz`, `Df 0.0020 at 10 GHz`, construction-specific thermal-conductivity values, CTE values, Td values, moisture absorption, and UL94 flammability posture.
- `RF-35TC`: PTFE-based ceramic-filled fiberglass low-loss / thermally conductive RF material with `Dk 3.5 +/- 0.05 at 10 GHz`, `Df 0.002 at 10 GHz`, thermal-conductivity values at `125 C`, CTE values, Td values, and physical / chemical properties.
- `METEORWAVE 4000`: ultra-low-loss laminate / prepreg material with separated `2 GHz` and `10 GHz` Dk/Df values, DMA Tg, Td, T-300, CTE, Z-expansion, moisture absorption, UL94 / IPC-4101 framing, and laminate-thickness boundary.

## Safe Reuse Classes

- Product identity and application framing from AGC datasheets.
- Numeric material properties only with their stated test frequency, method, construction, or temperature condition.
- Conservative material-selection context for RF, high-power RF, compact antenna, high-speed digital, and high-layer-count material discussions.

## Blocked Claim Classes

- Finished-board RF loss, antenna gain, amplifier lifetime, radar performance, satellite readiness, CAF lifetime, IST survival, controlled impedance, insertion loss, or thermal margin.
- APT / HIL / other supplier fabrication capability, qualification, certification, quality rate, yield, price, MOQ, stock, or lead time.
- Any claim that AGC typical values are guaranteed customer specification limits.

## Completion Status

- status: `source_backed_fact_layer_partial`
- scope: `three AGC material PDFs only`
- next lane: continue material PDF extraction for the remaining AGC, Rogers, Shengyi, Ventec, Taconic, TUC, Arlon / AD, and specialty laminate PDFs.
