# P4-86 EV Charger Control-Stack And Protocol Identity Source-Backed Integration

Date: 2026-05-01

## Purpose

Recover the next narrower authority lane after `P4-85`: the exact `IEC 61851-1`, `IEC 61851-23`, `IEC 61851-24`, `ISO 15118`, `SAE J1772`, `CCS`, `NACS`, and `OCPP` vocabulary appearing inside the EV-charger section of `ev-charger-pcb.md`.

This pass keeps `/code/blogs/tmps` drafts as claim inventory only. It does not promote exact power, current, voltage, creepage, clearance, surge, EMC, payment, certification, interoperability, or supplier-readiness claims.

## Inputs Reviewed

- `logs/p4-83-2026-4-29-expert-batch-controller-summary.md`
- `logs/p4-85-smart-meter-communication-protocol-identity-source-backed-integration.md`
- `/code/blogs/tmps/2026.4.29/en/ev-charger-pcb.md`
- existing local support:
  - `facts/methods/power-energy-inverter-charger-rewrite-boundary.md`
  - `facts/methods/thermal-pcb-platform-selection-posture.md`
  - `facts/methods/tht-pressfit-terminal-route-boundary.md`
  - `wiki/processes/power-energy-pcb-pcba-review-boundaries.md`
  - `facts/standards/automotive-medical-aerospace-application-qualification-boundary.md`

## Integrated Source-Backed Lane

### EV Charger Control-Stack And Protocol Identity Boundary

Added source records:

- `iec-61851-1-2017-product-page`
- `iec-61851-23-2023-product-page`
- `iec-61851-24-2023-product-page`
- `iso-15118-1-2019-page`
- `iso-15118-20-2022-page`
- `sae-j1772-202401-recommended-practice-page`
- `sae-j3400-2-202505-recommended-practice-page`
- `charin-iso-iec-15118-communication-standard-page`
- `open-charge-alliance-ocpp-protocols-page`

Added fact card:

- `standards-ev-charger-control-stack-and-protocol-identity-boundary`

Updated topic wiki:

- `processes-power-energy-pcb-pcba-review-boundaries`

Supported draft family:

- EV charger control-stack / bearer noun subset of `/code/blogs/tmps/2026.4.29/en/ev-charger-pcb.md`

What is now source-backed:

- exact `IEC 61851-1` may now be used as the EV supply equipment general-requirements family
- exact `IEC 61851-23` may now be used as the DC EV supply equipment family
- exact `IEC 61851-24` may now be used as the DC EVSE to EV digital-communication family
- exact `ISO 15118` may now be used as the EV-to-EVSE communication family
- exact `SAE J1772` may now be used as the North American conductive charge-coupler family
- exact `CCS` may now be used as the combined-charging-system identity
- exact `NACS` may now be used via `SAE J3400/2`
- exact `OCPP` may now be used as the charge-point to central-system protocol family

Still blocked:

- exact interoperability, conformance, or certification claims for any specific charger, board, module, or backend system
- exact payment, billing, security, or access-control claims
- exact EMC, surge, creepage, clearance, power, current, voltage, or lifetime claims
- exact connector compatibility, vehicle-compatibility, regional deployment, or field-readiness claims
- any claim that a specific PCB, module, or supplier already supports or achieves these communication outcomes

## Residual Disposition After P4-86

- `ev-charger-pcb.md` now has narrow source-backed support for:
  - exact `IEC 61851-1`, `IEC 61851-23`, and `IEC 61851-24` standards-family nouns
  - exact `ISO 15118` family nouns
  - exact `SAE J1772`, `CCS`, `NACS`, and `OCPP` communication / connector nouns
  - generic `PLC` wording only at naming level
- `ev-charger-pcb.md` still does not have source-backed support for:
  - exact interoperability, payment, safety, EMC, or certification behavior
  - exact charger power-stage or connector-current numerics
  - exact regional compatibility or field-deployment claims

## Draft Line Disposition Preserved

- downgradeable only:
  - `OCPP backend connectivity` when rewritten as protocol-identity vocabulary instead of deployment proof
  - `CCS/NACS Digital Communication` only after correction toward identity-only family wording
  - `Pilot Signal and Proximity` only as low-voltage control vocabulary
- still blocked:
  - `350 kW`, `500 A`, `800 V`, `50–100 kHz`, and slew-rate numerics
  - `MID`, `ANSI C12`, payment, NFC/RFID, `ISO 14443A/B`, `ISO 15693`, `UL 2202`, `UL 2594`, `IEC 61000-4-5`, and `CISPR 32` claims
  - exact `HomePlug Green PHY` or connector-compliance claims

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft family:
  - `2026.4.29` `ev-charger-pcb.md` at control-stack identity level only
- next likely action:
  - use the combined `P4-84`, `P4-85`, and `P4-86` identity lanes for conservative rewrites, then shift back to the remaining `2026.4.29` authority gaps outside smart-meter and EV-charger communication
