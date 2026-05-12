# P4-518 New Vendor Cluster 0.75 mm Owner Same-Surface Scout

Date: 2026-05-11
Parent surfaces:

- `logs/p4-515-2026-5-11-post-p4-514-residual-priority-and-completion-gap-rerank.md`
- `logs/p4-517-2026-5-11-new-vendor-cluster-1p50mm-owner-same-surface-scout-2.md`
- `logs/backlog.md`
- `logs/phase-status.md`

Execution mode: `controller_owned_negative_scout`

## Purpose

Check one new current-public official owner cluster for the still-open `0.75 mm` BGA/CSP residual, limited to vendor classes not already closed.

## Checked Vendor Cluster

- Samsung
- Micron
- SK hynix
- Fujitsu
- Toshiba
- Nuvoton

## Vendors And Pages Checked

### Samsung

- `https://download.semiconductor.samsung.com/resources/data-sheet/DS_K4B1G1646I_BY_M_Rev1_1-1.pdf`
- current-public owner datasheet for `K4B1G1646I`
- visible package class is `96FBGA`
- the surfaced pitch is `0.80`, not `0.75`
- package dimensions are visible, but the page does not clear the current `0.75 mm` residual

### Micron

- `https://assets.micron.com/adobe/assets/urn%3Aaaid%3Aaem%3A087330f6-6d71-4575-b622-cb10f20cdaf0/renditions/original/as/gddr7-product-brief.pdf`
- `https://assets.micron.com/adobe/assets/urn%3Aaaid%3Aaem%3A4c418a2e-a221-456c-bc5b-46e1392055ee/original/as/csn33-bga-user-guide.pdf`
- current-public owner surfaces do expose true `0.75 mm` ball pitch
- `GDDR7` shows `Package dimensions 12 x 14 x 1.1 mm` and `Ball pitch 0.75mm / 0.75mm/0.73mm`
- the BGA user guide only gives JEDEC pitch-class framing and generic BGA guidance, not a same-surface package drawing or footprint row that exceeds the current stack
- result stayed below reopen

### SK hynix

- `https://news.skhynix.com/sk-hynix-enhances-leadership-in-graphics-memory-with-introduction-of-industry-best-gddr7/`
- `https://news.skhynix.com/packaging-technology-a-key-to-next-generation-semiconductor-competitiveness-how-far-has-sk-hynix-come/`
- current-public SK hynix search surfaces are packaging-technology articles and newsroom material
- no qualifying package drawing, datasheet, or package-information page exposing true `0.75 mm` pitch identity plus same-surface footprint geometry surfaced in this scout
- result stayed below reopen

### Fujitsu

- `https://www.fujitsu.com/jp/group/fsl/imagesgig5/MB85R8M2T-DS501-00054-1v0-J.pdf`
- `https://www.fujitsu.com/uk/Images/MB85R8M2T.pdf`
- current-public owner datasheet surfaces do expose true `0.75 mm` pitch identity
- the package row is `48-pin plastic FBGA (BGA-48P-M24)` with `lead pitch 0.75 mm`
- the page shows package dimensions, but no same-surface printed PCB land-pattern or footprint geometry strong enough to exceed the current gate
- result stayed below reopen

### Toshiba

- `https://toshiba.semicon-storage.com/us/semiconductor/design-development/package/power-management-ics.html`
- `https://toshiba.semicon-storage.com/us/semiconductor/design-development/eda-cad-lib/land-pattern-library.html`
- `https://toshiba.semicon-storage.com/us/semiconductor/product/intelligent-power-ics/automotive-driver-ics.html`
- `https://toshiba.semicon-storage.com/ap-en/semiconductor/design-development/package/detail.UDFN6.html`
- current-public Toshiba pages checked in this scout expose package-size and land-pattern-library navigation, but not a qualifying BGA/CSP owner row with true `0.75 mm` pitch identity on the same package surface
- when `0.75` appears here, it is package height or a non-qualifying family context, not a same-surface BGA/CSP pitch row
- result stayed below reopen

### Nuvoton

- `https://www.nuvoton.com/export/resource-files/en-us--DS_MA35D1_Series_EN_Rev1.13.pdf`
- current-public owner datasheet surface exposes BGA package classes such as `BGA 312-Ball (15x15x1.4mm, 0.8mm pitch)` and `BGA 364-Ball (14x14x1.4mm, 0.65mm pitch)`
- no visible `0.75 mm` BGA/CSP row surfaced on the same page
- result stayed below reopen

## Gate Result

- no vendor in the checked cluster cleared the gate
- no current-public official owner source candidate was found that visibly exposes both true `0.75 mm` package identity and same-surface printed PCB land-pattern / footprint geometry strong enough to exceed the current stack

## Non-Reopen Filters Used

- `0.75` in package height, marketing copy, or generic family framing is not enough
- true `0.75 mm` pitch identity without same-surface footprint or land-pattern geometry is not enough
- same-surface geometry without a clear owner `0.75 mm` BGA/CSP row is not enough
- generic BGA user guides and packaging-technology articles do not count as package-specific owner rows
- family pages, lineup pages, and package-size listings without a qualifying `0.75 mm` package drawing stay below reopen
- sub-`0.75 mm` or non-qualifying BGA pitches such as `0.80` and `0.65` stay below reopen

## Final Verdict

No current-public official owner source candidate cleared the `0.75 mm` BGA/CSP residual gate in the checked vendor cluster.

