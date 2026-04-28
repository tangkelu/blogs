# P4-28 Kingboard Residual Source Recovery

Date: 2026-04-27

## Purpose

This pass executes the source-recovery portion of `P4-27` for remaining Kingboard products that were still blocked after `P4-26`.

Blog drafts under `/code/blogs/tmps/en` remain claim inventories only. Numeric facts in this pass are promoted only from official KBLaminates / Kingboard sources.

## Source Recovery Matrix

| Product | Official source found | Source URL | Disposition | Notes |
| --- | --- | --- | --- | --- |
| `KB-6160A` | yes | `https://www.kblaminates.com/upload/portal/20210630/202106301817329155.pdf` | `source_recovered` | Official KBLaminates PDF. A newer 2025 upload-path candidate returned 404 during recovery, so the working official portal PDF is used. |
| `KB-6160F` | yes | `https://www.kblaminates.com/upload/ueditor/20250313/KB-6160F%2CKB-6060F.pdf` | `source_recovered` | Official technical-information PDF for laminate `KB-6160F` and prepreg `KB-6060F`. |
| `KB-6160LC` | yes | `https://www.kblaminates.com/upload/ueditor/20251222/KB-6160LC.pdf` | `source_recovered` | Official technical-information PDF discovered through the official product index. |
| `KB-6160LC(C)` | yes | `https://www.kblaminates.com/upload/ueditor/20251222/KB-6160LC%28C%29.pdf` | `source_recovered` | Official technical-information PDF discovered through the official product index. |
| `KB-6165C` | yes | `https://www.kblaminates.com/en/upload/ueditor/20250313/KB-6165C%2CKB-6065C.pdf` | `source_recovered` | Official technical-information PDF for laminate `KB-6165C` and prepreg `KB-6065C`. |
| `KB-6165LE` | yes | `https://www.kblaminates.com/upload/ueditor/20250313/KB-6165LE%2CKB-6065LE.pdf` | `source_recovered` | Official technical-information PDF for laminate `KB-6165LE` and prepreg `KB-6065LE`. |
| `KB-6167GMD` | yes | `https://www.kblaminates.com/en/upload/ueditor/20250313/KB-6167GMD%2CKB-6067GMD.pdf` | `source_recovered` | Official technical-information PDF. Interface/channel claims remain blocked. |
| `KB-6167GLD` | yes | `https://www.kblaminates.com/en/upload/ueditor/20250313/KB-6167GLD%2CKB-6067GLD.pdf` | `source_recovered` | Official technical-information PDF. PAM4 / PCIe / Ethernet / loss-budget claims remain blocked. |
| `KB-6168LE` | yes | `https://www.kblaminates.com/en/upload/ueditor/20250313/KB-6168LE%2CKB-6068LE.pdf` | `source_recovered` | Official technical-information PDF. Reliability-cycle and mission-application claims remain blocked. |
| `KB-6169GT` | yes | `https://www.kblaminates.com/en/upload/ueditor/20250313/KB-6169GT%2CKB-6069GT.pdf` | `source_recovered` | Official technical-information PDF. 56G / 112G / PAM4 / channel-budget claims remain blocked. |
| `PI-515G` | yes | `https://www.kblaminates.com/en/upload/ueditor/20250313/PI-515G%2CPP-PI515G.pdf` | `source_recovered` | Official technical-information PDF. Keep separate from `PI-520G` and generic polyimide claims. |

## Source Records Added

- `kblaminates-kb-6160a-kb-6060a-technical-information`
- `kblaminates-kb-6160f-kb-6060f-technical-information`
- `kblaminates-kb-6160lc-technical-information`
- `kblaminates-kb-6160lc-c-technical-information`
- `kblaminates-kb-6165c-kb-6065c-technical-information`
- `kblaminates-kb-6165le-kb-6065le-technical-information`
- `kblaminates-kb-6167gmd-kb-6067gmd-technical-information`
- `kblaminates-kb-6167gld-kb-6067gld-technical-information`
- `kblaminates-kb-6168le-kb-6068le-technical-information`
- `kblaminates-kb-6169gt-kb-6069gt-technical-information`
- `kblaminates-pi-515g-pp-pi515g-technical-information`

## Fact Cards Added

- `materials-kingboard-kb-6160a`
- `materials-kingboard-kb-6160f`
- `materials-kingboard-kb-6160lc`
- `materials-kingboard-kb-6160lc-c`
- `materials-kingboard-kb-6165c`
- `materials-kingboard-kb-6165le`
- `materials-kingboard-kb-6167gmd`
- `materials-kingboard-kb-6167gld`
- `materials-kingboard-kb-6168le`
- `materials-kingboard-kb-6169gt`
- `materials-kingboard-pi-515g`

## Non-Unlocked Claim Families

This pass does not unlock:

- drill-cost percentages
- impedance-shift percentages
- cost deltas
- lead time
- regional compliance proof
- OEM mandate claims
- reliability-cycle guarantees
- aspect-ratio capability
- HIL/APT material stocking or fabrication capability
- yield
- finished-board qualification
- PCIe / USB / DDR / Ethernet / PAM4 support
- insertion-loss budgets
- channel compliance
- trace-length limits

## Completion Status

Source recovery is complete for all products that remained blocked after `P4-26`.

No product in the original P4-25 residual list remains blocked for lack of official KBLaminates source.

Selector, prepreg-boundary, and topic-wiki integration was completed through:

- `materials-kingboard-material-selection-boundaries`
- `materials-kingboard-prepreg-construction-data-boundaries`
- `wiki-materials-kingboard-laminate-selection-and-boundaries`
