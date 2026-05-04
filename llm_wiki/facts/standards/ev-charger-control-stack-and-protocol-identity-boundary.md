---
fact_id: "standards-ev-charger-control-stack-and-protocol-identity-boundary"
title: "IEC 61851, ISO 15118, SAE J1772, CCS, NACS, and OCPP sources support EV charger control-stack identity, not compliance or performance proof"
topic: "EV charger control stack and protocol identity boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-05-01"
source_ids:
  - "iec-61851-1-2017-product-page"
  - "iec-61851-23-2023-product-page"
  - "iec-61851-24-2023-product-page"
  - "iso-15118-1-2019-page"
  - "iso-15118-20-2022-page"
  - "sae-j1772-202401-recommended-practice-page"
  - "sae-j3400-2-202505-recommended-practice-page"
  - "charin-iso-iec-15118-communication-standard-page"
  - "open-charge-alliance-ocpp-protocols-page"
tags: ["ev-charger", "iec-61851", "iso-15118", "sae-j1772", "ccs", "nacs", "ocpp", "plc", "evse"]
---

# Canonical Summary

> Official IEC, ISO, SAE, CharIN, and Open Charge Alliance pages support one narrow EV-charger control-stack identity lane only. `IEC 61851-1`, `IEC 61851-23`, and `IEC 61851-24` may be used as EVSE and DC-charging standards-family nouns. `ISO 15118` may be used as the EV-to-EVSE communication standard family. `SAE J1772` may be used as the North America conductive charge-coupler family. `CCS` may be used as the combined-charging-system identity, `NACS` may be used via `SAE J3400/2`, and `OCPP` may be used as the charge-point to central-system protocol family. These sources do not prove that a specific charger, board, module, or supplier is compliant, interoperable, secure, certified, payment-ready, or field-proven.

## Stable Facts

- IEC publicly identifies `IEC 61851-1:2017` as `Electric vehicle conductive charging system - Part 1: General requirements`.
- IEC publicly states that `IEC 61851-1:2017` applies to EV supply equipment and covers the connection between EV supply equipment and the EV.
- IEC publicly identifies `IEC 61851-23:2023` as `Electric vehicle conductive charging system - Part 23: DC electric vehicle supply equipment`.
- IEC publicly identifies `IEC 61851-24:2023` as `Electric vehicle conductive charging system - Part 24: Digital communication between a DC EV supply equipment and an electric vehicle for control of DC charging`.
- ISO publicly identifies `ISO 15118-1:2019` as `Road vehicles -- Vehicle to grid communication interface -- Part 1: General information and use-case definition`.
- ISO publicly identifies `ISO 15118-20:2022` as the 2nd-generation network-layer and application-layer requirements part for vehicle-to-grid communication.
- CharIN publicly frames `Combined Charging System (CCS)` as an open and universal EV charging system and states that its CCS implementation guide covers charging process, safety, user authentication, payment authorization, and load balancing.
- CharIN publicly states that the `ISO/IEC 15118` communication standard uses a powerline communication module as required hardware.
- SAE publicly identifies `J1772_202401` as the conductive charge-coupler standard for EV/PHEV charging in North America and defines the inlet / mating-connector scope.
- SAE publicly identifies `J3400/2_202505` as the dimensional definition of the `SAE J3400 (NACS)` electric vehicle coupler.
- Open Charge Alliance publicly states that `OCPP` provides standardized communication between charge points and central systems and that it supports vendor-independent interoperability.

## Conditions And Methods

- Use this card for `/code/blogs/tmps/2026.4.29/en/ev-charger-pcb.md` only when the rewrite needs exact charging-standards or backend-protocol nouns.
- Keep `power stage`, `thermal`, `DFM/DFT/FCT`, and connector/harness language separate from this control-stack identity lane.
- Use `PLC` only as a generic communication-bearing noun here; do not infer a specific modem, carrier, or bandplan.
- Treat `CCS` as a system identity and `NACS` as an SAE J3400 coupler identity, not as proof of connector compatibility across every deployment.

## Limits And Non-Claims

- This card does not authorize exact power, current, voltage, creepage, clearance, surge, EMC, or lifetime claims.
- It does not authorize certification, interoperability, payment, billing, or field-readiness claims.
- It does not authorize `CCS2`, `HomePlug Green PHY`, `ISO 14443A/B`, `ISO 15693`, or `UL 2202` / `UL 2594` claims unless separately sourced.
- It does not authorize any claim that a specific PCB, charger, module, or supplier already implements or passes these standards.

## Open Questions

- Recover `ISO 15118` part-level and payment/access standards only if a future rewrite needs those exact nouns.
- Recover `UL`, `IEC 61000-4-5`, or `CISPR 32` sources only if a future rewrite needs safety or EMC standards wording.

## Source Links

- https://webstore.iec.ch/en/publication/33644
- https://webstore.iec.ch/en/publication/32973
- https://webstore.iec.ch/en/publication/32582
- https://www.iso.org/standard/69113.html
- https://www.iso.org/standard/77845.html
- https://saemobilus.sae.org/standards/j1772_202401-sae-electric-vehicle-plug-hybrid-electric-vehicle-conductive-charge-coupler
- https://saemobilus.sae.org/standards/j34002_202505-connectors-inlets-north-american-charging-system-nacs-electric-vehicles
- https://www.charin.global/technology/iso15118
- https://openchargealliance.org/protocols/ocpp-protocols/
