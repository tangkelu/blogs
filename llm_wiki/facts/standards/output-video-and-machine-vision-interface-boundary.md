---
fact_id: "standards-output-video-and-machine-vision-interface-boundary"
title: "Output-video and machine-vision interface sources support identity context, not PCB compliance or performance"
topic: "output video and machine vision interface boundary"
category: "standards"
status: "verified"
confidence: "medium"
must_refresh: true
reviewed_at: "2026-04-30"
source_ids:
  - "itu-r-bt470-conventional-analogue-television-systems-page"
  - "hdmi-specifications-and-programs-page"
  - "smpte-top-standards-page"
  - "a3-gige-vision-standard-page"
  - "a3-usb3-vision-standard-page"
tags: ["pal", "ntsc", "hdmi", "sdi", "gige-vision", "usb3-vision", "thermal-imaging", "output-video", "machine-vision", "compliance-boundary"]
---

# Canonical Summary

> ITU-R, HDMI LA, SMPTE, and A3 sources support a conservative output-video and machine-vision interface boundary for writing: legacy analogue-video wording adjacent to `PAL` / `NTSC`, guarded `HDMI` and `SDI` digital-video-interface nouns, and guarded `GigE Vision` / `USB3 Vision` machine-vision transport nouns are source-backed at identity level only. These sources do not prove that a PCB, layout, supplier, or finished camera product meets exact video-standard subtypes, performance numerics, interoperability, or compliance outcomes.

## Stable Facts

- ITU-R `BT.470` is the official recommendation-family anchor for conventional analogue television systems and is the conservative standards basis for legacy analogue-video wording adjacent to `PAL` / `NTSC`.
- HDMI Licensing Administrator provides a current official HDMI specifications landing page, making `HDMI` a safe standards-owner digital video / display interface noun.
- SMPTE's standards overview explicitly treats `Serial Digital Interface (SDI and HD-SDI)` as a family of broadcast digital-video interfaces.
- A3 provides official public pages for both `GigE Vision` and `USB3 Vision`, making them safe machine-vision interface-standard nouns at owner-identity level.
- This lane is narrower than a generic `video output` claim: it supports exact interface-family naming, not performance proof.

## Conditions And Methods

- Use this card when `thermal-imaging-pcb.md` needs a conservative route for exact output or transport nouns that were explicitly blocked by the earlier serial-interface lane.
- Prefer phrases such as `legacy analogue-video output context`, `digital video interface`, `broadcast video interface family`, `machine-vision transport interface`, or `designed around` unless narrower compliance or test evidence is attached.
- Pair this lane with `standards-embedded-imaging-serial-interface-boundary` when a draft also names `LVDS`, `MIPI CSI-2`, or other sensor-side serial interfaces.
- Pair this lane with `methods-eo-ir-detector-owner-identity-and-interface-boundary` when the same draft also names cooled / uncooled IR detector families.

## Limits And Non-Claims

- This card does not authorize exact `RS-170` or `STANAG 3350` claims because current public standards-owner support for those nouns is still insufficient in this batch.
- It does not authorize exact `PAL` versus `NTSC` implementation detail, regional doctrine, connector doctrine, or standard-equivalence mapping.
- It does not authorize subtype, bitrate, cable-length, latency, frame-rate, compression, interoperability, or compliance claims for `HDMI`, `SDI`, `GigE Vision`, or `USB3 Vision`.
- It does not authorize `HDMI-compliant PCB`, `SDI-compliant PCB`, `GigE Vision compliant camera board`, `USB3 Vision compliant camera board`, or product-certification claims.
- It does not prove that HILPCB or any supplier can build, validate, qualify, or certify a finished thermal-imaging product around these interfaces.

## Open Questions

- Recover a stronger public source later if future rewrites must retain exact `RS-170` or `STANAG 3350` nouns rather than generic legacy-video framing.
- Recover narrower standards-owner or product-owner sources later if future rewrites must retain exact SDI subtype, HDMI version, or machine-vision compliance language.

## Source Links

- https://www.itu.int/rec/R-REC-BT.470/en
- https://www.hdmi.org/spec/index
- https://www.smpte.org/top-standards
- https://www.automate.org/a3-content/vision-standards-gige-vision
- https://www.automate.org/a3-content/usb3-vision-standard
