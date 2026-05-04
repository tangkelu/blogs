# P4-85 Smart-Meter Communication Protocol Identity Source-Backed Integration

Date: 2026-05-01

## Purpose

Recover the next narrower authority lane after `P4-84`: the exact `DLMS/COSEM`, `IEC 62056`, `PRIME`, `G3-PLC`, `Wi-SUN`, `Zigbee`, `NB-IoT`, and `LTE-M` vocabulary appearing inside the communication section of `smart-meter-pcb.md`.

This pass keeps `/code/blogs/tmps` drafts as claim inventory only. It does not promote interoperability claims, exact protocol behavior, exact RF or PLC band claims, exact antenna or coupling rules, certification claims, utility-approval claims, head-end architecture claims, long-life proof, or supplier-readiness claims.

## Inputs Reviewed

- `logs/p4-84-smart-meter-standards-and-metrology-identity-source-backed-integration.md`
- `/code/blogs/tmps/2026.4.29/en/smart-meter-pcb.md`
- existing local support:
  - `facts/standards/smart-home-protocol-identity-boundary.md`
  - `facts/standards/smart-meter-standards-and-metrology-identity-boundary.md`
  - `wiki/processes/power-energy-pcb-pcba-review-boundaries.md`
  - `sources/registry/standards/csa-zigbee-faq.md`

## Integrated Source-Backed Lane

### Smart-Meter Communication Protocol Identity Boundary

Added source records:

- `dlms-core-specifications-page`
- `iec-62056-5-3-2023-product-page`
- `iec-62056-6-2-2017-product-page`
- `prime-alliance-advanced-metering-page`
- `g3-alliance-g3-technologies-page`
- `wi-sun-fan-page`
- `3gpp-the-cellular-internet-of-things-page`
- `3gpp-nb-iot-complete-page`

Reused existing source record:

- `csa-zigbee-faq`

Added fact card:

- `standards-smart-meter-communication-protocol-identity-boundary`

Updated topic wiki:

- `processes-power-energy-pcb-pcba-review-boundaries`

Supported draft family:

- smart-meter communication protocol / bearer noun subset of `/code/blogs/tmps/2026.4.29/en/smart-meter-pcb.md`

What is now source-backed:

- exact `DLMS/COSEM` may now be used as the named data-exchange application-layer plus object-model family, with public linkage to the `IEC 62056` suite
- exact `IEC 62056-5-3` may now be used as the named DLMS/COSEM application-layer document family
- exact `IEC 62056-6-2` may now be used as the named COSEM interface-classes document family
- exact `PRIME` may now be used as a named narrowband PLC technology family
- exact `G3-PLC` may now be used as a named PLC technology family distinct from `G3-Hybrid`
- exact `Wi-SUN` may now be used as a named field-area-network wireless technology family
- exact `Zigbee` may now be kept as a named `IEEE 802.15.4`-based wireless technology family
- exact `NB-IoT` and `LTE-M` may now be kept as named 3GPP cellular-IoT technology families

Still blocked:

- exact interoperability, conformance, or certification claims for any specific meter, board, concentrator, or head-end system
- exact protocol-stack mapping between `DLMS/COSEM` and `PRIME`, `G3-PLC`, `Wi-SUN`, `Zigbee`, `NB-IoT`, or `LTE-M`
- exact RF bands, PLC bandplans, data rates, range, latency, antenna rules, or cellular-module selection claims
- `best smart-meter protocol by region`, `supports utility head-end integration`, or equivalent deployment-architecture claims
- any claim that a specific PCB, module, or supplier already supports or achieves these communication outcomes

## Residual Disposition After P4-85

- `smart-meter-pcb.md` now has narrow source-backed support for:
  - exact `DLMS/COSEM` and `IEC 62056` standards-family nouns
  - exact `PRIME`, `G3-PLC`, `Wi-SUN`, `Zigbee`, `NB-IoT`, and `LTE-M` communication-family nouns
  - generic `PLC`, `RF mesh`, and `utility head-end system` wording only at naming level
- `smart-meter-pcb.md` still does not have source-backed support for:
  - exact protocol implementation or interoperability behavior
  - exact regional wireless or PLC deployment claims
  - exact metrology, safety, anti-tamper, lifetime, or supplier-capability outcomes

## Draft Line Disposition Preserved

- downgradeable only:
  - `Communication Stack: RF, PLC, and Cellular` when rewritten as protocol-identity vocabulary instead of performance or layout proof
  - `DLMS Protocol Meter Board` only after correction toward `DLMS/COSEM` family wording
  - `utility head-end system` only as a utility-side endpoint label
- still blocked:
  - `manages PLC or RF communication with the utility's head-end system`
  - exact `Sub-GHz RF mesh`, PLC coupling, `NB-IoT`, or `LTE-M` implementation claims
  - exact regional frequencies, module examples, or coexistence claims

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft family:
  - `2026.4.29` `smart-meter-pcb.md` at communication protocol identity level only
- next likely action:
  - use the combined `P4-84` and `P4-85` smart-meter lanes for conservative rewrites, then shift back to the remaining `2026.4.29` authority gaps outside smart-meter communication
