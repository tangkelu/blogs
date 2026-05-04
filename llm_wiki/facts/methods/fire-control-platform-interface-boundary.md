---
fact_id: "methods-fire-control-platform-interface-boundary"
title: "Targeting and fire-control writing is source-backed only at platform-interface and bus-boundary level"
topic: "fire-control platform interface boundary"
category: "methods"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-30"
source_ids:
  - "mil-std-1553-data-bus-page"
  - "mil-hdbk-1553-multiplex-application-handbook-page"
  - "bosch-can-protocols-page"
  - "ieee-8023-ethernet-working-group"
  - "gps-gov-civil-gps-accuracy-page"
tags: ["targeting", "fire-control", "mil-std-1553", "can", "ethernet", "gps", "platform-interface", "sensor-input"]
---

# Canonical Summary

> Current DLA, Bosch, IEEE, and GPS.gov sources support one narrow interface lane only: `targeting` drafts may describe a control board as sitting between sensor-input paths and platform communication links, and may name interface families such as `MIL-STD-1553`, `CAN`, `Ethernet`, and GPS receiver context at standards-owner level. The current evidence layer does not support turning that into ballistic-computation proof, weapon-system authority, bus compliance, interoperability proof, or qualification claims.

## Stable Facts

- The official DLA `MIL-STD-1553` page identifies the standard as a `digital time division command/response multiplex data bus` and states that it covers data-bus techniques, interface electronics, concept of operation, and electrical / functional formats.
- The official DLA `MIL-HDBK-1553` page identifies a formal application handbook oriented around how to apply `MIL-STD-1553B`.
- Bosch's official CAN page supports `Classical CAN`, `CAN FD`, and `CAN XL` as a real protocol family under the `Controller Area Network` noun family.
- The official IEEE 802.3 Working Group page remains the standards-owner anchor for Ethernet family vocabulary.
- GPS.gov remains a government source for GPS receiver-system context rather than bare-board positioning proof.

## Conditions And Methods

- Use this card when `targeting-pcb.md` needs a safer route than generic `fire control network` or `weapons interface` marketing.
- Safe posture: describe the board as integrating sensor-input paths and platform communication links, with guarded interface-family vocabulary and system-context wording.
- Pair this lane with the existing laser time-of-flight boundary when the draft also discusses laser timing or pulsed-driver sections.
- Pair this lane with the existing interface / positioning boundary when the draft also mentions Ethernet or GPS context beyond the narrow `targeting` lane.

## Limits And Non-Claims

- This card does not authorize ballistic computation, firing-solution accuracy, weapon release, laser-designator authority, or mission-performance claims.
- It does not authorize `MIL-STD-1553 compliant PCB`, `CAN-qualified PCB`, `Ethernet-certified PCB`, or `GPS-accurate PCB` claims.
- It does not authorize bus timing, throughput, jitter, redundancy, galvanic-isolation, EMC, cybersecurity, or interoperability claims.
- It does not authorize HILPCB deployment, defense-prime approval, customer, or military-program proof.

## Open Questions

- Add narrower owner or standards sources later if a future rewrite must retain exact video-interface, IMU-bus, or optical-sensor protocol language beyond the current platform-interface lane.
- Add stronger public authority later if a future rewrite must retain detailed `fire-control computer` architecture rather than conservative interface-boundary wording.

## Source Links

- https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=36973
- https://quicksearch.dla.mil/qsDocDetails.aspx?ident_number=54141
- https://www.bosch-semiconductors.com/products/ip-modules/can-protocols/
- https://www.ieee802.org/3/
- https://www.gps.gov/gps-accuracy
