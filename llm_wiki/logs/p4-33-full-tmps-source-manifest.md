# P4-33 Full `/code/blogs/tmps` Source Manifest

## Purpose

This manifest records the current `/code/blogs/tmps` corpus before full P4-33 learning proceeds. It is deletion-safe at directory and batch level. Lane logs provide per-topic and per-claim-family disposition.

## Snapshot

- snapshot_date: `2026-04-28`
- root: `/code/blogs/tmps`
- total_files: `1419`
- english_markdown_drafts: `715`
- english_dated_batches: `29`
- local_material_pdfs: `167`
- image_or_asset_dirs:
  - `/code/blogs/tmps/2025.12.20/图片`
  - `/code/blogs/tmps/2025.12.29/图片`
  - `/code/blogs/tmps/2026.1.13/图片`
  - `/code/blogs/tmps/2026.1.27/图片`
  - `/code/blogs/tmps/2026.1.6/图片`
  - `/code/blogs/tmps/2026.2.25/img`
  - `/code/blogs/tmps/2026.3/图片`
  - `/code/blogs/tmps/2026.4.1/图片`
  - `/code/blogs/tmps/2026.4.24/图片`

## Batch Inventory

| batch | english_md_count | P4-33 lane ownership | current durable status |
|---|---:|---|---|
| `2025.7` | 5 | Lane B / existing P4-32 | `completed_at_existing_layer_routing_level` via `p4-32-2025-7-mixed-service-blog-ingestion-map.md` |
| `2025.7.14` | 25 | Lane C | `source_backed_fact_layer_partial` |
| `2025.7.22` | 10 | Lane A | `completed_at_claim_family_level` |
| `2025.7.23` | 26 | Lane A | `completed_at_claim_family_level` |
| `2025.7.28` | 10 | Lane B | `completed_at_claim_family_level` |
| `2025.8.1` | 32 | Lane B | `completed_at_claim_family_level` |
| `2025.8.12` | 57 | Lane D | `completed_at_claim_family_level` |
| `2025.8.22` | 40 | Lane E | `completed_at_claim_family_level` |
| `2025.8.30` | 15 | Lane D | `source_backed_fact_layer_partial` |
| `2025.10.1` | 28 | Lane F | `completed_at_claim_family_level` |
| `2025.10.13` | 38 | Lane F | `completed_at_claim_family_level` |
| `2025.10.20` | 40 | Lane C | `source_backed_fact_layer_partial` |
| `2025.10.25` | 49 | Lane C / Lane D | `source_backed_fact_layer_partial` |
| `2025.11.3` | 18 | Lane G delta | `completed_at_claim_family_level` |
| `2025.11.10` | 16 | Lane B | `completed_at_claim_family_level` |
| `2025.11.17` | 16 | Lane G delta | `completed_at_claim_family_level` |
| `2025.11.27` | 14 | Lane F | `completed_at_claim_family_level` |
| `2025.12.10` | 10 | Lane A / Lane D | `completed_at_claim_family_level` |
| `2025.12.17` | 14 | Lane E | `completed_at_claim_family_level` |
| `2025.12.20` | 29 | Lane E / Lane F | `completed_at_claim_family_level` |
| `2025.12.29` | 48 | Lane B / Lane E | `completed_at_claim_family_level` |
| `2025.07.13` | 11 | Lane C | `source_backed_fact_layer_partial` |
| `2026.1.6` | 20 | Lane D | `source_backed_fact_layer_partial` |
| `2026.1.13` | 40 | Lane E / existing P4-30 analogy | `source_backed_fact_layer_partial` |
| `2026.1.27` | 30 | Lane E | `completed_at_claim_family_level` |
| `2026.2.25` | 17 | Lane A / existing P4-25 to P4-28 analogy | `source_backed_fact_layer_partial` |
| `2026.3` | 20 | Lane A / Lane D / existing P4-29 analogy | `source_backed_fact_layer_partial` |
| `2026.4.1` | 27 | Lane C / existing P4-31 analogy | `completed_at_claim_family_level` |
| `2026.4.24` | 10 | Lane C / existing P4-20 analogy | `source_backed_fact_layer_partial` |

## Local Material PDF Buckets

These counts come from filename-level classification only. They are routing aids, not source records.

| bucket | pdf_count | notes |
|---|---:|---|
| Rogers / legacy high-frequency family naming | 38 | Includes RO-series, RT/duroid, TMM, RO4000 / RO3000, Kappa, MAGTREX, Radix, CuClad / IsoClad / DiClad / Anteo-like names. Some may require manual vendor validation. |
| AGC | 36 | Filename prefix `AGC_`; includes METEORWAVE, N4000, N7000, RF, TLC/TLE/TLF/TLX/TLY families. |
| Shengyi | 57 | Includes Shengyi S-series, SF-series, Autolad, LNB, mmWave, SCGA files. |
| Ventec | 23 | Includes VT-series laminate and prepreg / no-flow files. |
| Taconic explicit | 1 | Explicit `Taconic RF-35.pdf`; other Taconic-like families may exist under non-explicit names. |
| TUC / ThunderClad | 10 | Includes `tu-*` and `thunderclad` datasheets. |
| Other / needs manual classification | 2 | Requires lane A manual classification before source use. |

## Already Known Durable Coverage

The following related coverage already exists and must be reused rather than duplicated:

- `P4-20` through `P4-24`: layer-count, material, IMS, rigid-flex / flex material, UPILEX-S coverage and boundaries.
- `P4-25` through `P4-28`: Kingboard material ingestion and official-source recovery.
- `P4-29`: APTPCB RO3003 / RO3006 / Rogers draft ingestion.
- `P4-30`: HILPCB input-device draft ingestion across four subagent lane logs.
- `P4-31`: APTPCB260401 2-layer draft ingestion.
- `P4-32`: `2025.7` mixed service draft ingestion.

## Draft Authority Boundary

The drafts are professional PCB / PCBA engineering inputs. They are valid for:

- terminology
- outline structure
- engineering problem framing
- claim-family discovery
- source-gap discovery
- topic clustering

They are not valid by themselves for:

- material-property numbers
- stackup, geometry, process-window, or inspection-threshold numbers
- supplier capability or qualification claims
- certification, compliance, or regulator claims
- price, lead time, MOQ, stock, yield, throughput, or quality-rate claims
- medical, automotive, aerospace, military, RF/mmWave, or high-reliability readiness claims

## Active P4-33 Subagent Lanes

| lane | output log | status |
|---|---|---|
| A materials / PDFs | `logs/p4-33-lane-a-materials-pdf-and-draft-matching.md` | `completed_at_claim_family_level` |
| B PCBA / testing / quality | `logs/p4-33-lane-b-pcba-testing-quality.md` | `completed_at_claim_family_level` |
| C fabrication structures | `logs/p4-33-lane-c-fabrication-structures.md` | `source_backed_fact_layer_partial` |
| D RF / high-speed / impedance | `logs/p4-33-lane-d-rf-high-speed-impedance.md` | `source_backed_fact_layer_partial` |
| E applications | `logs/p4-33-lane-e-applications.md` | `completed_at_claim_family_level` |
| F commercial / service taxonomy | `logs/p4-33-lane-f-commercial-service-taxonomy.md` | `completed_at_claim_family_level` |
| G delta November batches | `logs/p4-33-lane-g-delta-2025-11-3-and-2025-11-17.md` | `completed_at_claim_family_level` |

## Immediate Gaps

- The first-round delta gap for `2025.11.3` and `2025.11.17` is now closed through Lane G at claim-family level.
- The PDF bucket counts are filename-level only; no PDF should become a source record until source identity and extraction scope are confirmed.
- Current P4-33 progress is still batch / lane intake. It does not mean the full `715`-draft corpus is fully learned at fact level.
