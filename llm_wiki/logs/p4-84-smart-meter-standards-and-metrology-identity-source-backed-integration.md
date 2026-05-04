# P4-84 Smart-Meter Standards And Metrology Identity Source-Backed Integration

Date: 2026-05-01

## Purpose

Recover the next narrower authority lane after `P4-83`: the exact `IEC 62052`, `IEC 62053`, `MID`, `ANSI C12`, and `AMI` vocabulary appearing inside `smart-meter-pcb.md`.

This pass keeps `/code/blogs/tmps` drafts as claim inventory only. It does not promote compliance claims, exact accuracy outcomes, exact safety thresholds, anti-tamper effectiveness, long-life proof, protocol behavior, supplier readiness, or HILPCB-specific regional-documentation claims.

## Inputs Reviewed

- `logs/p4-83-2026-4-29-expert-batch-controller-summary.md`
- `/code/blogs/tmps/2026.4.29/en/smart-meter-pcb.md`
- existing local support:
  - `wiki/processes/power-energy-pcb-pcba-review-boundaries.md`
  - `facts/methods/power-energy-inverter-charger-rewrite-boundary.md`
  - `facts/methods/thermal-pcb-platform-selection-posture.md`
  - `facts/methods/tht-pressfit-terminal-route-boundary.md`

## Integrated Source-Backed Lane

### Smart-Meter Standards And Metrology Identity Boundary

Added source records:

- `iec-62052-11-2020-product-page`
- `iec-62052-31-2015-product-page`
- `iec-62053-21-2020-product-page`
- `iec-62053-22-2020-product-page`
- `iec-62053-23-2020-product-page`
- `eurlex-2014-32-eu-measuring-instruments-directive-page`
- `ansi-blog-c12-1-2026-code-for-electricity-metering`
- `ansi-blog-c12-20-2015-accuracy-classes-page`
- `nist-nistir-7823-ami-release-announcement`

Added fact card:

- `standards-smart-meter-standards-and-metrology-identity-boundary`

Updated topic wiki:

- `processes-power-energy-pcb-pcba-review-boundaries`

Supported draft family:

- smart-meter standards / metrology / regional-framework subset of `/code/blogs/tmps/2026.4.29/en/smart-meter-pcb.md`

What is now source-backed:

- exact `IEC 62052-11` may now be used as the named general metering-equipment and type-testing document family
- exact `IEC 62052-31` may now be used as the named product-safety document family in this IEC meter cluster
- exact `IEC 62053-21`, `IEC 62053-22`, and `IEC 62053-23` may now be used as named particular-requirements document families for active-energy or reactive-energy meter classes, with type-test-only posture
- exact `MID` may now be used as the EU `Directive 2014/32/EU` framework, with `MI-003` as the active-electrical-energy-meter annex identity
- exact `ANSI C12.20` may now be kept only as a historical/public accuracy-class noun under current ANSI public framing that routes through `ANSI C12.1`
- exact `AMI` may now be kept as institutional system-context vocabulary rather than draft-only marketing language

Still blocked:

- `complies with IEC 62052/62053`
- `MID-certified`, `ANSI C12.20 compliant`, or utility-approval claims
- exact `Class 0.5S`, `revenue-grade`, `0.1% channel accuracy`, or no-recalibration claims
- exact creepage, clearance, hi-pot, impulse, or surge numerics
- `20-year field life`, anti-tamper effectiveness, or supplier-readiness claims
- exact communication-protocol claims for `DLMS`, `PRIME`, `G3-PLC`, `Wi-SUN`, `NB-IoT`, `LTE-M`, or head-end integration

## Residual Disposition After P4-84

- `smart-meter-pcb.md` now has narrow source-backed support for:
  - exact `IEC 62052-11`, `IEC 62052-31`, `IEC 62053-21/22/23`, `MID`, `MI-003`, historical `ANSI C12.20`, and `AMI` vocabulary
  - the distinction between general metering requirements, product-safety framing, particular accuracy-class document families, and EU legal-metrology framework language
- `smart-meter-pcb.md` still does not have source-backed support for:
  - exact performance or lifetime outcomes
  - exact safety thresholds or test values
  - protocol implementation or interoperability claims
  - supplier qualification or documentation-support claims

## Draft Line Disposition Preserved

- downgradeable only:
  - `AMI Networks` and `Advanced Metering Infrastructure (AMI)` as system-context language
  - `High-Voltage Isolation Under IEC 62052/62053` only when rewritten as standards-family naming rather than proof wording
  - `IEC 62052-11`, `IEC 62053-21/22/23`, `MID`, and `ANSI C12.20` as exact document-family or framework nouns
- still blocked:
  - `IEC 62052-11, IEC 62053-21/22/23, and UL 2735 define safety isolation, impulse withstand, and environmental requirements`
  - `Class 0.5S revenue-grade accuracy`
  - `survives 6 kV impulse withstand testing`
  - `supports documentation packages for MID ... and regional certification requirements`

## Status

- integration status: `source_backed_fact_layer_partial`
- upgraded draft family:
  - `2026.4.29` `smart-meter-pcb.md` at standards / metrology / framework identity level only
- next likely action:
  - recover a separate smart-meter communication-protocol identity lane only if future rewrites must retain exact `DLMS/COSEM`, `IEC 62056`, `PRIME`, `G3-PLC`, `Wi-SUN`, `NB-IoT`, or related utility-network nouns
