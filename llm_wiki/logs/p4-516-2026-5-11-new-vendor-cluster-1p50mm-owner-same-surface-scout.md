# P4-516 New Vendor Cluster 1.50 mm Owner Same-Surface Scout

Date: 2026-05-11
Parent surfaces:

- `logs/p4-515-2026-5-11-post-p4-514-residual-priority-and-completion-gap-rerank.md`
- `logs/p4-514-2026-5-11-nexperia-wlcsp-same-surface-and-1p50-false-positive-no-reopen.md`
- `logs/backlog.md`
- `logs/phase-status.md`

Execution mode: `controller_owned_negative_scout`

## Purpose

Check a new current-public official owner cluster for the still-open `1.50 mm` BGA/CSP residual, but only in vendor classes that have not already been closed.

## Checked Vendor Cluster

- Samsung
- Micron
- SK hynix
- Nuvoton
- ROHM
- Socionext

## Vendors And Pages Checked

### Samsung

- `https://download.semiconductor.samsung.com/resources/data-sheet/DS_K4B1G1646I_BY_M_Rev1_1-1.pdf`
- current-public owner datasheet surface for `K4B1G1646I`
- surfaced package drawing is `96FBGA`
- visible pitch in the search-extracted package dimension is `0.80`, not `1.50`
- result stayed below reopen

### Micron

- `https://www.micron.com/content/dam/micron/global/public/products/customer-service-note/csn33-bga-user-guide.pdf`
- current-public owner BGA user guide
- visible `1.50mm` appears only as a pitch-class boundary in JEDEC terminology (`E >= 1.50mm`), not as a same-surface package drawing that pairs true `1.50 mm` identity with footprint geometry
- the PCB guidance is generic BGA design guidance, with pad-type and opening examples, not a qualifying `1.50 mm` package-specific owner row
- result stayed below reopen

### SK hynix

- current-public official search only surfaced general packaging-technology material and a facility portal guide
- no qualifying public BGA/CSP package drawing or datasheet exposing true `1.50 mm` pitch identity plus same-surface footprint geometry surfaced in this scout
- result stayed below reopen

### Nuvoton

- `https://www.nuvoton.com/export/resource-files/en-us--DS_MA35D1_Series_EN_Rev1.13.pdf`
- current-public owner datasheet surface for `MA35D1`
- surfaced BGA package types are `BGA 312-Ball (15x15x1.4mm, 0.8mm pitch)` and `BGA 364-Ball (14x14x1.4mm, 0.65mm pitch)`
- no visible `1.50 mm` pitch identity on the same package surface
- result stayed below reopen

### ROHM

- `https://fscdn.rohm.com/en/products/databook/catalog/common/P_Serial_EEPROM_Selection_Guide_EN.pdf`
- current-public owner selection guide
- surfaced packages are `VCSP` / `UCSP`, not BGA/CSP owner rows for the present residual
- visible ball pitch values are `0.5` or `0.4`, not `1.50`
- result stayed below reopen

### Socionext

- `https://www.socionext.com/en/products/assp/gdc/SC172x/`
- `https://www.socionext.com/en/products/assp/gdc/SC1701/`
- `https://www.socionext.com/en/products/assp/radar-sensor/SC1232/`
- `https://www.socionext.com/en/products/assp/radar-sensor/SC1233/`
- current-public product pages expose BGA package classes, but the surfaced pitches are `1.0mm` or `0.8mm`
- no qualifying same-surface `1.50 mm` owner package drawing or datasheet surfaced in this scout
- result stayed below reopen

## Gate Result

- no vendor in the checked cluster cleared the gate
- no current-public official owner source candidate was found that visibly exposes both true `1.50 mm` pitch identity and same-surface printed PCB land-pattern / footprint geometry

## Non-Reopen Filters Used

- `1.50` in body-size or package-dimension context is not pitch identity
- pitch identity without same-surface footprint or land-pattern geometry is not enough
- generic BGA design guidance is not a package-specific reopen candidate
- WCSP / CSP / UCSP / VCSP non-BGA families are excluded unless they explicitly show the needed same-surface `1.50 mm` BGA/CSP row
- sub-`1.50 mm` pitches such as `1.0`, `0.8`, `0.65`, `0.5`, and `0.4` stay below reopen
- search results that do not expose a qualifying owner package drawing or datasheet are not reopen signals

## Final Verdict

No current-public official owner source candidate cleared the `1.50 mm` BGA/CSP residual gate in the checked vendor cluster.

