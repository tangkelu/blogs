# P4-46 Source-Backed Integration

Date: 2026-04-29

## Purpose

Convert the strongest remaining `P4-45` USB taxonomy blocker into reusable `llm_wiki` data by adding official USB-IF source records, one standards boundary fact card, and one topic wiki page for connector taxonomy versus capability and certification language.

This pass keeps `/code/blogs/tmps` drafts as claim inventory only. It does not promote draft-originated universal speed tables, power tables, Thunderbolt comparisons, Alt Mode behavior, adapter capability, consumer adoption, ranking, buying advice, or current product-specific certification claims.

## Inputs Reviewed

- `logs/p4-45-source-backed-integration.md`
- `logs/p4-44-source-backed-integration.md`
- `logs/p4-40-2025-11-3-consumer-rf-usb-ptfe-official-source-recovery-scout.md`
- `/code/blogs/tmps/2025.11.3/en/types-of-usb-ports.md`
- `/code/blogs/tmps/2025.11.3/en/type-c-charger.md`
- `/code/blogs/tmps/2025.11.3/en/type-c-charger-pcb.md`
- existing USB-IF Type-C / PD / QbS source records and charger-boundary facts already present in `llm_wiki`

## Source Records Added

- `sources/registry/standards/usb-if-cables-and-connectors-compliance-updates-page.md`
- `sources/registry/standards/usb-if-usb-logo-usage-guidelines-2024.md`
- `sources/registry/standards/usb-if-usb4-v2-80gbps-announcement.md`

These official USB-IF records add:

- dynamic connector and cable certification-lifecycle context for Mini, Micro, USB Type-C, and cable-logo policy
- official USB logo and word-mark boundary context
- official USB4 Version 2.0 / `USB 80Gbps` family identity and branding boundary context

## Fact Card Added

- `facts/standards/usb-connector-and-certified-capability-taxonomy-boundary.md`

This fact card upgrades the `types-of-usb-ports` family from `blocked_pending_official_source` to a conservative source-backed taxonomy layer.

What is now source-backed:

- connector-family vocabulary versus protocol/generation-family vocabulary
- the boundary that `USB Type-C` / `USB-C` naming is not the same as `USB4`, `Power Delivery`, or certified capability proof
- the boundary that certified charger/performance labels are separate USB-IF program artifacts
- dynamic legacy-connector certification and cable-policy context that must be refreshed before publication

## Topic Wiki Added

- `wiki/processes/usb-connector-and-capability-taxonomy-boundaries.md`

This page makes the new boundary prompt-consumable for:

- `/code/blogs/tmps/2025.11.3/en/types-of-usb-ports.md`
- `/code/blogs/tmps/2025.11.3/en/type-c-charger.md`
- `/code/blogs/tmps/2025.11.3/en/type-c-charger-pcb.md`

## What This Unlocks

- `types-of-usb-ports.md` can now be conservatively rewritten as a taxonomy-and-boundary article:
  - connector shapes
  - capability-family separation
  - logo/certification boundary
  - caution that exact capability depends on the exact product and cable
- `type-c-charger.md` and `type-c-charger-pcb.md` can now reference the broader USB taxonomy boundary without drifting into unsupported universal port claims.

## Still Blocked

- universal or current `2025/2026` speed, power, Alt Mode, cable, or market-adoption tables
- Thunderbolt identity or compatibility claims without exact Intel and platform-vendor sources
- DisplayPort / HDMI adapter claims without exact VESA or platform-vendor sources
- claims that USB-C automatically means `USB4`, `PD`, `fast charging`, `video`, or high-end cable capability
- exact product, cable, charger, dock, motherboard, or adapter certification claims without current listing evidence
- consumer-recommendation language such as `best port`, `future-proof`, or `universal standard` without dated methodology

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft family: `2025.11.3` USB taxonomy and charger-adjacent boundary lane
- next likely residual lanes:
  - remote-control protocol authority
  - general electronics education / schematic-symbol authority
  - IGBT vs MOSFET official device-context lane
  - HDI / BOM / PCB cost-driver evidence
