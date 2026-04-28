# P4-17 USB-C Charger Source Supplement

Date: 2026-04-27

## Purpose

Continue the empty-image data-first program without writing blogs.

This round narrows one known P4-16 gap:

- `type-c-charger` had manufacturing-boundary support, but lacked a non-blog USB-C / USB PD / PPS source layer.

This round also rechecked two adjacent weak areas without drafting:

- medical / conformal coating pages
- RF / mmWave / isolator pages

The result is that USB-C needed and received source-layer supplementation, while medical coating and RF/mmWave still need narrower future source work only if the intended article promise exceeds the current conservative boundary.

## Source Layer Added

New USB-IF source registry records:

- `sources/registry/standards/usb-if-type-c-cable-connector-spec-r2-0.md`
- `sources/registry/standards/usb-if-type-c-functional-test-spec-2024-03-03.md`
- `sources/registry/standards/usb-if-pd-compliance-updates-page.md`
- `sources/registry/standards/usb-if-type-c-compliance-updates-page.md`
- `sources/registry/standards/usb-if-connector-qbs-guidelines-page.md`
- `sources/registry/standards/usb-if-qbs-information-page.md`
- `sources/registry/standards/usb-if-type-c-language-guidelines-2023.md`

These records provide primary-source anchors for:

- USB Type-C / USB-C vocabulary
- connector and cable ecosystem scope
- Type-C functional-test and `VIF` vocabulary
- USB PD / Type-C compliance-update context
- QbS program context
- USB Type-C public language discipline

## Updated Fact And Topic Layer

Updated:

- `facts/methods/usb-c-pd-pps-protocol-context-boundary.md`
- `wiki/processes/usb-c-charger-readiness-classification.md`

New posture:

- `type-c-charger` moves from `boundary_ready_for_conservative_rewrite` to `boundary_ready_with_usb_if_vocabulary`.
- The article can now safely use controlled terms such as `USB Type-C`, `USB-C`, `USB Power Delivery`, `PPS`, `VIF`, compliance update, and QbS context.
- The article still must stay anchored to PCB / PCBA manufacturing concerns:
  connector-zone planning, protection placement context, controller / power-stage separation, inspection, and powered FCT handoff.

## Still Blocked

This round does not unlock:

- exact USB-C pinout, CC behavior, cable-marker behavior, role-swap behavior, alternate-mode behavior, or connector mechanical prescriptions
- exact USB PD / PPS revision claims, message flows, voltage / current / power-mode tables, source / sink tables, EPR / SPR tables, or charger output modes
- USB-IF certification, logo use, QbS eligibility, interoperability, adapter compatibility, safety, compliance, thermal-rise, efficiency, reliability, or fast-charge performance claims
- charger power, current, temperature, efficiency, lifetime, output, creepage / clearance, ESD rating, surge rating, or protection-topology claims

## Readiness Impact

| slug | previous posture | updated posture | note |
| --- | --- | --- | --- |
| `type-c-charger` | `boundary_ready_for_conservative_rewrite` | `boundary_ready_with_usb_if_vocabulary` | still no protocol table or performance claims |
| `ultra-fast-charger-power-energy` | `boundary_ready_with_blocked_performance_claims` | unchanged | can borrow manufacturing and test-flow vocabulary only |
| `central-inverter-power-energy` | `adjacent_context_only` | unchanged | use only to prevent connector / cable / protocol drift |

## Adjacent Gap Review

### Medical / Conformal Coating

Current posture:

- source coverage already includes IPC-CC-830C metadata, Electrolube, HumiSeal, APT / HIL coating pages, APT medical page, and PCBA quality / inspection pages
- the main gap is not basic source absence
- the main risk is application overclaim:
  biocompatibility, sterilization compatibility, patient-contact suitability, ISO 13485, FDA applicability, coating thickness, cure schedule, cleanliness threshold, masking dimensions, or acceptance criteria

Disposition:

- `conformal-coating-medical-imaging-wearable` remains `needs_refresh_then_go`
- a future supplement should add formal medical-material / sterilization / biocompatibility sources only if the intended article genuinely needs those topics
- otherwise the safer rewrite path is still protection workflow, masking / keep-access decisions, contamination / moisture exposure context, and inspection / test handoff

### RF / mmWave / Isolator

Current posture:

- source coverage already includes 3GPP 38-series / TS 38.104 identity anchors, Analog Devices / Qorvo phased-array and phase-shifter context, Smiths Interconnect isolator / circulator sources, and internal telecom / high-frequency / microwave pages
- the current layer supports system-context vocabulary and conservative PCB execution boundaries
- it does not support RF performance, RF budgets, named band proof, part-selection metrics, or supplier qualification claims

Disposition:

- `5g-isolator-5g-telecom` remains `hold_for_part_performance_sources` if the article promise requires component behavior
- `mmwave-5g-5g-telecom` remains `hold_or_context_only` unless a future source pass adds narrower mmWave architecture / measurement / validation support
- `antenna-system-5g-telecom` remains usable only as feed / launch / transition / shielding review context, not antenna-performance content

## Verification Notes

- Scoped source / fact / topic reference validation should be run after this file lands.
- `git diff --check` should be run after shared log integration.
