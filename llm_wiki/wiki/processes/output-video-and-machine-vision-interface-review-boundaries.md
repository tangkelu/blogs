---
topic_id: "processes-output-video-and-machine-vision-interface-review-boundaries"
title: "Output Video And Machine Vision Interface Review Boundaries"
category: "processes"
status: "active"
last_reviewed_at: "2026-05-04"
fact_ids:
  - "standards-output-video-and-machine-vision-interface-boundary"
  - "standards-embedded-imaging-serial-interface-boundary"
  - "methods-eo-ir-detector-owner-identity-and-interface-boundary"
  - "methods-pcba-dfm-dft-dfa-review-gate-positioning"
  - "methods-pcba-first-article-inspection-vs-high-speed-validation-boundary"
source_ids:
  - "itu-r-bt470-conventional-analogue-television-systems-page"
  - "hdmi-specifications-and-programs-page"
  - "smpte-top-standards-page"
  - "a3-gige-vision-standard-page"
  - "a3-usb3-vision-standard-page"
  - "mipi-csi-2-spec-page"
  - "mipi-d-phy-spec-page"
  - "mipi-dsi-2-spec-page"
  - "mipi-display-command-set-page"
  - "ti-lvds-overview-page"
  - "lynred-about-our-technologies-page"
  - "frontendapt-pcba-first-article-inspection-page-en"
tags: ["pal", "ntsc", "hdmi", "sdi", "gige-vision", "usb3-vision", "thermal-imaging", "output-video", "machine-vision", "routing-boundary"]
---

# Governance Summary

> Output-video and machine-vision interface wording is safe in this corpus only at interface identity and review-gate level. The active routing posture is: keep sensor-side links, output-video families, and machine-vision transports separate; allow legacy analogue-video nouns, `HDMI`, `SDI`, `GigE Vision`, and `USB3 Vision` only as identity-level interface vocabulary; and route performance, interoperability, certification, and product-readiness language through separate validation boundaries instead of turning an interface page into proof of capability.

## Routing Sequence

| Step | Safe question | What this page allows |
|---|---|---|
| 1. Interface identity | "Which output or transport family is being named?" | Legacy analogue-video, HDMI, SDI, GigE Vision, USB3 Vision as identity nouns |
| 2. Sensor-side separation | "Is the draft confusing sensor links with output links?" | Keep `MIPI`, `D-PHY`, `CSI-2`, `DSI-2`, and `LVDS` separate from output-video families |
| 3. Review workflow | "Does the draft need DFM, DFT, DFA, or FAI framing?" | Route launch and validation language to workflow gates |
| 4. Product boundary | "Is the draft drifting into output-quality or compliance proof?" | Keep those claims blocked or move them to narrower evidence lanes |

## What This Page Controls

- Use this page when a draft mentions analogue-video, HDMI, SDI, GigE Vision, or USB3 Vision by name.
- Treat the named families as standards-owner or vendor-family interface nouns only.
- Keep output-interface vocabulary separate from sensor-facing serial links and detector identity.
- Route release, inspection, and validation language to the broader workflow cards instead of using interface names as proof.

## Stable Facts

- ITU-R `BT.470` is the official recommendation-family anchor for conventional analogue television systems and supports guarded legacy analogue-video framing adjacent to `PAL` / `NTSC`.
- HDMI Licensing Administrator provides the current HDMI specifications landing page, supporting guarded `HDMI` interface identity.
- SMPTE publicly describes `SDI` and `HD-SDI` as a family of broadcast digital-video interfaces.
- A3 publicly maintains owner pages for `GigE Vision` and `USB3 Vision`, supporting guarded machine-vision transport identity.
- The embedded imaging serial-interface lane remains separate and continues to govern `MIPI CSI-2`, `MIPI D-PHY`, `MIPI DSI-2`, `MIPI Display Command Set`, and `LVDS`.
- EO/IR detector-owner identity remains separate and supports the detector family side of thermal-imaging and night-vision boards.
- Existing DFM / first-article / validation cards support the distinction between interface identity and launch-readiness evidence.

## Boundary Split

### Legacy Analogue Video Family

- Safe posture: describe legacy analogue-video output context using guarded wording adjacent to `PAL` / `NTSC`.
- Safe companion layers:
  `standards-embedded-imaging-serial-interface-boundary`,
  `methods-eo-ir-detector-owner-identity-and-interface-boundary`.
- Stop line: do not publish `RS-170`, `STANAG 3350`, exact analogue-system mapping, or deployment doctrine from this page.

### Digital Video Output Family

- Safe posture: describe digital display or broadcast output context using guarded `HDMI` or `SDI` interface-family vocabulary.
- Safe companion layers:
  `methods-pcba-dfm-dft-dfa-review-gate-positioning`,
  `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary`.
- Stop line: do not publish subtype, bitrate, cable reach, frame-rate, latency, or compliance claims.

### Machine Vision Transport Family

- Safe posture: describe machine-vision transport options using `GigE Vision` or `USB3 Vision` nouns at interface-standard level.
- Safe companion layers:
  `standards-embedded-imaging-serial-interface-boundary`,
  `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary`.
- Stop line: do not publish plug-and-play proof, cable-length claims, interoperability proof, or registered-compliant-product language.

### Sensor-Side Interface Separation

- Safe posture: keep `MIPI CSI-2`, `MIPI D-PHY`, `MIPI DSI-2`, `MIPI Display Command Set`, and `LVDS` as sensor-facing or display-facing serial-interface nouns.
- Safe companion layer:
  `standards-embedded-imaging-serial-interface-boundary`.
- Stop line: do not collapse sensor-side serial links into output-video family claims.

### EO/IR Detector Boundary

- Safe posture: keep detector families at owner-identity level when the same board also names thermal-imaging or night-vision sensors.
- Safe companion layer:
  `methods-eo-ir-detector-owner-identity-and-interface-boundary`.
- Stop line: do not convert detector identity into optics, video-chain, or target-recognition proof.

## Common Misreadings

- `HDMI` does not prove bitrate, latency, or compliant finished-product behavior.
- `SDI` does not prove output quality, cable reach, or interoperability.
- `GigE Vision` and `USB3 Vision` do not prove machine-vision interoperability or compliance by themselves.
- `PAL` or `NTSC` wording does not prove exact analogue-system mapping or regional doctrine.
- Sensor-side `MIPI` or `LVDS` links are not the same as output-video transport families.
- Interface naming does not prove validation, qualification, or supplier-readiness.

## Explicit Blocked Claims

- `interface-performance proof`: do not claim bandwidth, frame-rate, latency, cable-length, compression, or interoperability proof from this page.
- `universal machine-vision doctrine`: do not claim a single interface strategy applies to all machine-vision or output-video boards.
- `certification or product-readiness claims`: do not claim that a PCB, camera, or output board is certified, qualified, compliant, or product-ready because it names an interface family.
- `cost/lead-time/yield claims`: do not derive commercial, schedule, or yield conclusions from interface naming.

## Must Refresh Before Publishing

- any exact `RS-170` or `STANAG 3350` wording
- any exact SDI subtype, HDMI version, or machine-vision compliance statement
- any bandwidth, frame-rate, latency, cable-length, compression, or interoperability numeric
- any statement that moves from interface identity into product validation, qualification, or supplier proof

## Related Fact Cards

- `standards-output-video-and-machine-vision-interface-boundary`
- `standards-embedded-imaging-serial-interface-boundary`
- `methods-eo-ir-detector-owner-identity-and-interface-boundary`
- `methods-pcba-dfm-dft-dfa-review-gate-positioning`
- `methods-pcba-first-article-inspection-vs-high-speed-validation-boundary`

## Primary Sources

- https://www.itu.int/rec/R-REC-BT.470/en
- https://www.hdmi.org/spec/index
- https://www.smpte.org/top-standards
- https://www.automate.org/a3-content/vision-standards-gige-vision
- https://www.automate.org/a3-content/usb3-vision-standard
- https://www.mipi.org/specifications/csi-2
- https://www.mipi.org/specifications/d-phy
- https://www.mipi.org/specifications/dsi-2
- https://www.mipi.org/specifications/display-command-set
- https://www.ti.com/product-category/interface/lvds/overview.html
- https://www.lynred.com/about-our-technologies
- /code/hileap/frontendAPT/public/static/pcba/en/first-article-inspection.json
