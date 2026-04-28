---
fact_id: "standards-high-frequency-printed-board-and-material-boundary"
title: "IPC-6018 and IPC-4103 separate high-frequency printed-board scope from base-material scope"
topic: "High-frequency printed-board and material standards boundary"
category: "standards"
status: "verified"
confidence: "high"
must_refresh: true
reviewed_at: "2026-04-28"
source_ids:
  - "ipc-6018d-toc"
  - "ipc-4103b-toc"
  - "ipc-validation-services-qpl-ipc-4103-page"
tags: ["ipc", "ipc-6018", "ipc-4103", "high-frequency-pcb", "microwave-pcb", "base-materials", "qpl", "boundary"]
---

# Canonical Summary

> `IPC-6018` is the stronger public IPC anchor for high-frequency / microwave printed-board qualification and performance specification scope, while `IPC-4103` is the stronger public IPC anchor for high-speed / high-frequency base-material scope. Neither reference proves finished-board RF performance, supplier capability, material stock, or customer acceptance.

## Stable Facts

- The public `IPC-6018D` TOC identifies a high-frequency / microwave printed-board qualification and performance specification family.
- The public `IPC-6018D` TOC supports construction-scope vocabulary such as microstrip, stripline, mixed dielectric, multilayer, buried / blind via, and metal-core variants at metadata level.
- The public `IPC-4103B` TOC identifies a base-material specification family for high-speed / high-frequency printed-board applications.
- IPC's public `QPL IPC-4103` page supports the existence of qualified-product / manufacturing-site listing vocabulary for high-speed / high-frequency base materials and bonding-layer products.

## Conditions And Methods

- Use this card when drafts discuss high-frequency PCB, microwave PCB, high-speed base material, RF material, or supplier selection for RF / high-speed builds.
- Keep board specification scope (`IPC-6018`) separate from laminate / bonding-layer material scope (`IPC-4103`).
- Pair this card with exact material datasheets before using Dk, Df, Tg, Td, copper style, or prepreg values.
- Pair it with customer specifications, inspection records, and dated capability records before making finished-board qualification or supplier capability claims.

## Limits And Non-Claims

- This card does not reproduce IPC standard text or acceptance tables.
- It does not prove that any supplier conforms to `IPC-6018` or is listed under `IPC-4103`.
- It does not prove antenna gain, OTA performance, insertion loss, impedance tolerance, VNA frequency range, or production qualification.
- It does not support universal material rankings or universal stackup construction rules.

## Source Links

- https://www.ipc.org/TOC/IPC-6018D_TOC.pdf
- https://www.ipc.org/TOC/IPC-4103B.pdf
- https://www.electronics.org/ipc-validation-services-qualified-products-list-qpl-ipc-4103
