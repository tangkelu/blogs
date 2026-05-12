# P4-517 New Vendor Cluster 1.50 mm Owner Same-Surface Scout 2

Date: 2026-05-11
Parent surfaces:

- `logs/p4-515-2026-5-11-post-p4-514-residual-priority-and-completion-gap-rerank.md`
- `logs/p4-516-2026-5-11-new-vendor-cluster-1p50mm-owner-same-surface-scout.md`
- `logs/backlog.md`
- `logs/phase-status.md`

Execution mode: `controller_owned_negative_scout`

## Purpose

Check one new current-public official owner cluster for the still-open `1.50 mm` BGA/CSP residual, limited to vendor classes not already closed and not already checked in `P4-516`.

## Checked Vendor Cluster

- Mitsubishi Electric
- Sony
- NEC
- Fujitsu
- Alps Alpine
- Panasonic

## Vendors And Pages Checked

### Mitsubishi Electric

- `https://www.mitsubishielectric.com/semiconductors/design_support/catalog/index.html`
- `https://www.mitsubishielectric.com/semiconductors/?FILENAME=mgf2430a.pdf`
- `https://www.mitsubishielectric.com/semiconductors/powerdevices/datasheets/ipm/g1_series/pm300cg1c065.pdf`
- current-public owner material is power-device / optical-device / module centered, not a qualifying BGA/CSP package drawing or package-information page for the present residual
- no visible same-surface `1.50 mm` pitch + footprint geometry candidate surfaced
- result stayed below reopen

### Sony

- `https://www.sony-semicon.com/en/products/lsi-ic/tof-ldd.html`
- `https://www.sony-semicon.com/en/products/is/industry/tof/spad-tof.html`
- `https://www.sony-semicon.com/en/products/is/medical/endoscope/IMX446-447.html`
- `https://altair.sony-semicon.com/products/alt1210/`
- `https://altair.sony-semicon.com/products/alt1255/`
- current-public owner pages expose BGA / CSP / WLCSP family labels, but the surfaced pitches are `BGA-49P`, `BGA-152`, or WLCSP-class packaging, not a visible `1.50 mm` same-surface owner row
- no current-public owner package drawing or datasheet exposing both true `1.50 mm` pitch identity and same-surface footprint geometry surfaced in this scout
- result stayed below reopen

### NEC

- `https://www.nec.com/en/global/techrep/journal/g05/n03/pdf/a222.pdf`
- `https://www.nec.com/en/global/techrep/journal/g06/n05/pdf/t060513.pdf`
- `https://www.nec.com/en/global/techrep/journal/g07/n04/pdf/070410.pdf`
- current-public NEC surfaces found in this scout are technical reports on packaging / system integration, not owner package drawings or package-information rows with visible `1.50 mm` pitch identity
- the visible pitch evidence is sub-`1.50 mm` research framing or generic BGA mention, not same-surface printed PCB land-pattern geometry for the residual
- result stayed below reopen

### Fujitsu

- `https://www.fujitsu.com/us/Images/bga-484p-m07.pdf`
- `https://www.fujitsu.com/us/Images/bga-544p-m04.pdf`
- `https://www.fujitsu.com/us/Images/tebga-484p-m09.pdf`
- `https://www.fujitsu.com/us/Images/package-guide.pdf`
- current-public owner package PDFs are real package-information pages, but the surfaced pitch classes are `1.00 mm`, `1.27 mm`, or `0.80 mm`
- no visible same-surface `1.50 mm` pitch identity plus footprint geometry surfaced
- result stayed below reopen

### Alps Alpine

- `https://tech.alpsalpine.com/e/products/detail/SCTA3A0103/`
- `https://tech.alpsalpine.com/e/products/detail/HGARPS011A/`
- `https://tech.alpsalpine.com/e/products/detail/HGDESM033A/`
- `https://tech.alpsalpine.com/e/products/detail/SPEF220100/`
- `https://tech.alpsalpine.com/e/products/detail/SKPSAAE010/`
- `https://tech.alpsalpine.com/e/products/detail/SKSCLDE010/`
- `https://tech.alpsalpine.com/e/products/detail/SPVT230202/`
- `https://tech.alpsalpine.com/e/products/detail/RDC506A03A/`
- current-public owner product pages are connector, sensor, or switch pages with land-dimension sections, not qualifying BGA/CSP package drawings for the present residual
- no visible `1.50 mm` pitch identity on the same package surface surfaced in this scout
- result stayed below reopen

### Panasonic

- `https://industrial.panasonic.com/ww/applications/solution-mdls/ic-package`
- `https://industrial.panasonic.com/ww/electronic-materials/products/app-ic-package`
- `https://industrial.panasonic.com/ww/products/pt/adv-sc-pkg-em`
- `https://industrial.panasonic.com/ww/electronic-materials/products/sem`
- `https://na.industrial.panasonic.com/products/electronic-materials/ic-packaging-materials/series/134677`
- `https://na.industrial.panasonic.com/products/electronic-materials/ic-packaging-materials/lineup/lexcm-gx-substrates`
- current-public Panasonic surfaces in this scout are electronic-materials / encapsulation / substrate pages, not package-owner drawings or datasheets for a `1.50 mm` BGA/CSP row
- they mention BGA / CSP / FC-BGA as application classes, but do not expose a qualifying same-surface `1.50 mm` package identity + footprint geometry candidate
- result stayed below reopen

## Gate Result

- no vendor in the checked cluster cleared the gate
- no current-public official owner source candidate was found that visibly exposes both true `1.50 mm` pitch identity and same-surface printed PCB land-pattern / footprint geometry

## Non-Reopen Filters Used

- `1.50` in body-size, package-length, or product-version context is not pitch identity
- pitch identity without same-surface footprint or land-pattern geometry is not enough
- package-family pages, materials pages, or generic semiconductor technology pages are not reopen signals
- sub-`1.50 mm` pitches such as `1.27`, `1.0`, `0.8`, `0.65`, `0.5`, and `0.4` stay below reopen
- WLCSP / CSP / VCSP / UCSP / module / materials pages are excluded unless they explicitly show the needed same-surface `1.50 mm` BGA/CSP row
- technical-report / research-paper BGA mentions do not count as owner package drawings
- search results that do not expose a qualifying owner package drawing or datasheet are not reopen signals

## Final Verdict

No current-public official owner source candidate cleared the `1.50 mm` BGA/CSP residual gate in the checked vendor cluster.

