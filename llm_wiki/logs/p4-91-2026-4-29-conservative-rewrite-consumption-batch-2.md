# P4-91 2026.4.29 Conservative Rewrite Consumption Batch 2

Date: 2026-05-01

## Purpose

Consume the already-landed `P4-84` through `P4-88` narrow authority lanes directly in the draft layer by rewriting four more `/code/blogs/tmps/2026.4.29/en` drafts into conservative, prompt-usable versions.

This pass does not add new authority. It only removes unsupported claims and rewrites each draft so it stays inside the already-landed smart-meter, EV-charger, hearing-aid, and satellite identity or metadata boundaries plus generic board-review posture.

## Inputs Reviewed

- `logs/p4-84-smart-meter-standards-and-metrology-identity-source-backed-integration.md`
- `logs/p4-85-smart-meter-communication-protocol-identity-source-backed-integration.md`
- `logs/p4-86-ev-charger-control-stack-and-protocol-identity-source-backed-integration.md`
- `logs/p4-87-hearing-aid-wireless-and-telecoil-identity-source-backed-integration.md`
- `logs/p4-88-satellite-space-material-outgassing-and-class-3a-metadata-integration.md`
- `facts/standards/smart-meter-standards-and-metrology-identity-boundary.md`
- `facts/standards/smart-meter-communication-protocol-identity-boundary.md`
- `facts/standards/ev-charger-control-stack-and-protocol-identity-boundary.md`
- `facts/standards/hearing-aid-wireless-and-telecoil-identity-boundary.md`
- `facts/standards/space-material-outgassing-and-class-3a-metadata-boundary.md`
- `wiki/processes/power-energy-pcb-pcba-review-boundaries.md`
- `wiki/processes/hearing-aid-pcb-review-boundaries.md`
- `tmps/2026.4.29/en/smart-meter-pcb.md`
- `tmps/2026.4.29/en/ev-charger-pcb.md`
- `tmps/2026.4.29/en/hearing-aid-pcb.md`
- `tmps/2026.4.29/en/satellite-pcb.md`

## Draft Consumption Result

Rewritten drafts:

- `tmps/2026.4.29/en/smart-meter-pcb.md`
- `tmps/2026.4.29/en/ev-charger-pcb.md`
- `tmps/2026.4.29/en/hearing-aid-pcb.md`
- `tmps/2026.4.29/en/satellite-pcb.md`

What changed:

- removed unsupported deployment, qualification, interoperability, regulatory-proof, and supplier-readiness claims
- removed unsupported exact numerics for metrology performance, power, current, voltage, EMC, audio behavior, launch environment, thermal cycling, vibration, shock, and life claims
- kept only already-landed safe nouns inside each draft's authority boundary
- rewrote each article around conservative PCB review, interface planning, manufacturability review, subsystem partitioning, material or protocol identity handling, and prototype-to-production handoff posture
- rewrote frontmatter `description` and `tags` where needed to remove blocked capability or proof language

Per-draft safe noun handling:

- `smart-meter-pcb.md`
  - kept guarded `IEC 62052-11`, `IEC 62052-31`, `IEC 62053-21/22/23`, `MID`, `MI-003`, historical `ANSI C12.20`, `AMI`, `DLMS/COSEM`, `IEC 62056`, `PRIME`, `G3-PLC`, `Wi-SUN`, `Zigbee`, `NB-IoT`, and `LTE-M` only at identity or standards-context level
  - removed or downgraded exact metrology-performance, tamper-efficacy, field-life, interoperability, utility-approval, and supplier-capability claims
- `ev-charger-pcb.md`
  - kept guarded `IEC 61851-1`, `IEC 61851-23`, `IEC 61851-24`, `ISO 15118`, `SAE J1772`, `CCS`, `NACS`, `OCPP`, and generic `PLC` only at identity or board-integration level
  - removed or downgraded exact power, current, voltage, isolation, EMC, certification, payment, interoperability, `CCS2`, `HomePlug Green PHY`, `UL 2202`, `UL 2594`, and supplier-capability claims
- `hearing-aid-pcb.md`
  - kept guarded `LE Audio`, `Auracast`, `telecoil`, and `induction loop systems` only at identity or integration-review level
  - removed or downgraded codec, antenna/body-loss, audio numeric, regulatory, venue-rollout, implant-extension, and supplier-capability claims
- `satellite-pcb.md`
  - kept guarded `ASTM E595`, NASA outgassing screening context, `IPC-6012FS`, `Class 3`, and guarded `Class 3A` only at metadata or review-boundary level
  - removed or downgraded qualification, launch-environment, radiation, thermal-cycle, vibration, shock, coating-subtype, supplier-capability, and mission-readiness claims

## What Is Now Prompt-Usable

These four drafts are now usable as conservative drafts for:

- smart-meter standards and communication identity framing without metrology-proof or utility-approval overclaiming
- EV charger control-stack and connector/protocol identity framing without power, compliance, or payment overclaiming
- hearing-aid wireless and telecoil integration-review framing without codec, audio-performance, or regulatory overclaiming
- satellite board-review framing around outgassing screening and `IPC-6012FS` / `Class 3` metadata without qualification or mission-readiness overclaiming

## Still Blocked

- any exact metrology-performance, tamper, field-life, utility-approval, or interoperability proof claim in `smart-meter-pcb.md`
- any exact power, current, voltage, isolation, EMC, payment, certification, or `CCS2` / `HomePlug Green PHY` / `UL 2202` / `UL 2594` claim in `ev-charger-pcb.md`
- any codec, audio-performance, antenna/body-loss, regulatory, venue-rollout, implant, or supplier-readiness claim in `hearing-aid-pcb.md`
- any qualification, radiation, launch-environment, thermal-cycle, vibration, shock, coating-subtype, or mission-readiness claim in `satellite-pcb.md`
- any HILPCB-specific validated performance, qualification, or supplier-readiness claim across these drafts

## Status

- draft status: `conservative_rewrite_ready`
- supporting authority status: `unchanged_from_p4_84_through_p4_88`
- next likely action:
  - continue conservative rewrite consumption for the remaining `2026.4.29` drafts that already route safely through existing layers
  - reopen new authority recovery only if a publication-critical exact noun cannot be removed or downgraded
