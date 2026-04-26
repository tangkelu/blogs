# H2 Impedance Tolerance Source Map

Date: 2026-04-25

## Purpose

This file maps the current local corpus into support classes for the `impedance_tolerance` H2 bucket.

It is a governance and source-mapping document.

It is not:

- a source registry record
- a fact card
- approval to publish transferable impedance-tolerance numbers

## Relation To H2 Policy

Under `h2-capability-number-policy.md`, impedance tolerance is a fabrication-capability numeric.

That means:

- internal process or product pages can support framing and recovery routing
- verification-posture pages can support measurement and evidence-layer language
- none of the current internal prose sources, by themselves, authorize a reusable transferable tolerance number
- future `keep` status still requires a dated capability record with scope and refresh discipline

## Source Classes

### 1. Downgrade / Framing Support

These sources are useful for explaining what controlled impedance is connected to, where it sits in stackup planning, and why it appears in multilayer or high-speed workflows.

They do not authorize reusable impedance-tolerance numerics.

#### `facts/methods/spread-glass-and-controlled-impedance-planning.md`

- role:
  - downgrade / framing support
- why it is useful:
  - connects impedance planning to glass style, resin system, copper profile, reference stackup, and validation planning
- why it is limited:
  - explicitly says reference stackups are starting templates only
  - explicitly says final geometry must be simulated and validated against actual material, copper, finish, and fabricator compensation data
- H2 handling:
  - use for intake-planning and workflow language
  - do not treat as evidence for a transferable tolerance band

#### `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`

- role:
  - downgrade / framing support
- why it is useful:
  - places controlled impedance inside broader advanced-PCB planning, stackup architecture, high-layer registration, and backdrill context
- why it is limited:
  - explicitly marks exact impedance tolerance, TDR coverage, coupon requirements, and VNA scope as refresh-sensitive
  - treats internal numeric capabilities as refresh-sensitive in general
- H2 handling:
  - use to keep impedance_tolerance separated from materials, SI, and other advanced-process buckets
  - do not lift numerics from this page into capability facts

#### `sources/registry/internal/frontendapt-pcb-high-speed-pcb-page-en.md`

- role:
  - downgrade / framing support
- why it is useful:
  - identifies high-speed build framing, low-loss stackups, backdrill, VIPPO, and impedance verification as a connected internal capability family
- why it is limited:
  - extraction notes explicitly say speed grades and impedance numbers are refresh-sensitive internal claims
- H2 handling:
  - use as routing metadata for future capability-record recovery
  - not valid as a standalone numeric source

#### `sources/registry/internal/frontendhil-high-speed-product-page-en.md`

- role:
  - downgrade / framing support
- why it is useful:
  - adds HIL-side high-speed, backdrill, low-loss stackup, and validation posture coverage
- why it is limited:
  - extraction notes explicitly say to use it as internal support, not source-of-truth
- H2 handling:
  - use for scope and wording control only
  - not for reusable tolerance numbers

#### `sources/registry/internal/frontendapt-pcb-multilayer-pcb-page-en.md`

- role:
  - downgrade / framing support
- why it is useful:
  - ties multilayer stackup, sequential lamination, backdrill, registration, and impedance language together
- why it is limited:
  - extraction notes explicitly say thickness, feature size, and impedance figures are internal claims requiring re-check before external publication
- H2 handling:
  - use to map which multilayer blog claims belong in the impedance_tolerance bucket
  - do not promote any page number directly

#### `sources/registry/internal/frontendhil-multilayer-pcb-product-page-en.md`

- role:
  - downgrade / framing support
- why it is useful:
  - provides HIL-side multilayer stackup and build-complexity framing with backdrill and TDR context
- why it is limited:
  - extraction notes explicitly say layer-count and process-capability numbers are internal support only
- H2 handling:
  - useful for recovery routing and non-claim boundaries
  - not valid for transferable tolerances

### 2. Verification-Posture Support

These sources are the strongest current support for how impedance claims should be verified or bounded.

They support evidence-layer language, not reusable impedance-tolerance numbers.

#### `facts/methods/controlled-impedance-tdr-verification-posture.md`

- role:
  - verification-posture support
- why it is useful:
  - explicitly summarizes that internal pages pair controlled-impedance targets with TDR, coupon-style validation, or similar measurement language
  - already states that tolerance bands, verification percentages, and coupon scope are refresh-sensitive internal claims
- what it supports safely:
  - impedance should be described together with verification
  - TDR / coupon language is part of the evidence model
  - verification posture is stronger than bare design-intent language
- what it does not support:
  - a universal transferable impedance tolerance
  - identical TDR coverage on every board or program

#### `wiki/testing/validation-ladder-from-e-test-to-si-verification.md`

- role:
  - verification-posture support
- why it is useful:
  - clearly separates electrical-test coverage, impedance correlation, and deeper SI / RF verification
  - warns against blending TDR and VNA into one undifferentiated proof claim
- what it supports safely:
  - impedance verification belongs to a staged evidence ladder
  - TDR is not the same as full-path SI validation
  - customer-facing coverage and maximum-frequency claims require re-checking before publication
- what it does not support:
  - any fixed tolerance number
  - any universal coverage percentage
  - any standard-scope validation package promise

#### `sources/registry/internal/frontendapt-pcb-pcb-impedance-control-page-en.md`

- role:
  - verification-posture support and candidate upstream input
- why it is useful:
  - this is the clearest internal source family for controlled-impedance build framing, TDR verification, simulation, and channel language
- why it is limited:
  - extraction notes explicitly say impedance tolerances and verification coverage are refresh-required internal claims
  - notes also say to separate engineering posture from customer-facing promises
- H2 handling:
  - use as the primary internal pointer when requesting a future dated capability record
  - do not treat the page itself as a durable numeric anchor

#### `sources/registry/internal/frontendapt-materials-controlled-impedance-stackups-page-en.md`

- role:
  - verification-posture support and candidate upstream input
- why it is useful:
  - connects reference stackups, TDR/VNA coupon planning, downloadable templates, and design checklist language
- why it is limited:
  - extraction notes explicitly say reference stackups are planning aids, not universal rules
  - refresh notes say layer-count examples and impedance ranges must be re-checked when templates or ranges change
- H2 handling:
  - use as evidence that controlled impedance requires stackup and coupon planning
  - do not reuse embedded ranges as generalized shop capability

### 3. Non-Claim Boundaries

These sources are especially valuable because they say what the current corpus cannot safely claim.

They should be cited inside future H2 recovery work to prevent overclaiming.

#### `facts/methods/controlled-impedance-tdr-verification-posture.md`

- boundary value:
  - does not say every board is shipped with identical TDR coverage
  - does not claim a universal impedance tolerance across all structures or programs

#### `facts/methods/spread-glass-and-controlled-impedance-planning.md`

- boundary value:
  - does not guarantee a specific impedance tolerance for every stackup
  - does not replace SI simulation or production coupon measurement

#### `wiki/testing/validation-ladder-from-e-test-to-si-verification.md`

- boundary value:
  - exact maximum validated frequency, validation scope, report depth, and fixture details must refresh before publishing
  - TDR is not full-path insertion-loss or S-parameter validation

#### `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`

- boundary value:
  - exact impedance tolerance, TDR coverage, coupon requirements, and VNA scope must refresh before publishing
  - internal numeric capability claims are refresh-sensitive

#### relevant internal registry records

- boundary value:
  - multiple records explicitly flag impedance numbers as internal, refresh-sensitive, support-only, or not source-of-truth
- implication:
  - current registry records help route recovery but do not authorize transferable tolerance numbers

### 4. Candidate Upstream Inputs For Future Dated Capability Record

These are the best current upstream inputs if a future Tier 1 dated capability record is created for `impedance_tolerance`.

They are candidates because they identify the internal source family, terminology, verification model, and likely owning pages.

They are not themselves the future capability record.

#### primary candidate set

- `sources/registry/internal/frontendapt-pcb-pcb-impedance-control-page-en.md`
  - closest current internal registry anchor to controlled-impedance-specific tolerance and TDR language
- `facts/methods/controlled-impedance-tdr-verification-posture.md`
  - best current normalized summary of how internal pages connect targets to measurement
- `sources/registry/internal/frontendapt-materials-controlled-impedance-stackups-page-en.md`
  - strongest current pointer for coupon, stackup-template, and planning-side inputs

#### secondary candidate set

- `sources/registry/internal/frontendapt-pcb-high-speed-pcb-page-en.md`
  - useful when impedance tolerance is embedded in high-speed build language
- `sources/registry/internal/frontendapt-pcb-multilayer-pcb-page-en.md`
  - useful when the claim appears in multilayer service framing rather than a dedicated impedance page
- `sources/registry/internal/frontendhil-high-speed-product-page-en.md`
  - useful for HIL-side consistency checking
- `sources/registry/internal/frontendhil-multilayer-pcb-product-page-en.md`
  - useful for HIL-side multilayer consistency checking

## Sources That Explicitly Require Refresh Or Do Not Authorize Transferable Tolerance Numbers

### explicitly refresh-sensitive

- `facts/methods/controlled-impedance-tdr-verification-posture.md`
  - exact tolerance bands, verification percentages, and coupon scope are refresh-sensitive internal claims
- `wiki/testing/validation-ladder-from-e-test-to-si-verification.md`
  - exact maximum frequency, scope, report depth, and package details must refresh before publishing
- `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`
  - exact impedance tolerance, TDR coverage, coupon requirements, and VNA scope must refresh before publishing
- `sources/registry/internal/frontendapt-pcb-pcb-impedance-control-page-en.md`
  - impedance tolerances and verification coverage are refresh-required internal claims
- `sources/registry/internal/frontendapt-materials-controlled-impedance-stackups-page-en.md`
  - impedance ranges and layer-count examples must be re-checked when templates or ranges change
- `sources/registry/internal/frontendapt-pcb-high-speed-pcb-page-en.md`
  - speed grades and impedance numbers are refresh-sensitive internal claims
- `sources/registry/internal/frontendapt-pcb-multilayer-pcb-page-en.md`
  - impedance figures are internal claims requiring re-check before external publication

### not valid for transferable tolerance numbers on their own

- all current internal registry records in this bucket
  - because they are internal support pages, not Tier 1 dated capability records
- `facts/methods/controlled-impedance-tdr-verification-posture.md`
  - because it is a methods posture card, not a capability record
- `facts/methods/spread-glass-and-controlled-impedance-planning.md`
  - because it is planning guidance and explicitly non-guarantee language
- `wiki/testing/validation-ladder-from-e-test-to-si-verification.md`
  - because it governs evidence layers, not specific tolerance commitments
- `wiki/processes/advanced-pcb-fabrication-and-stackup-planning.md`
  - because it is a broad process frame and explicitly marks exact impedance claims as refresh-sensitive

## What Is Still Missing

- a Tier 1 dated internal capability record for impedance tolerance with explicit scope
- clear scope split by structure or program type instead of one blended controlled-impedance promise
- explicit ownership and refresh discipline for tolerance commitments and verification-coverage language
- a governed distinction between:
  - tolerance commitment
  - coupon / TDR verification posture
  - optional advanced validation scope
- a reusable rule for when internal impedance numbers may enter evidence packs versus remain framing-only

## Recommended Source-Ingestion Order For Future Recovery

1. `sources/registry/internal/frontendapt-pcb-pcb-impedance-control-page-en.md`
   - first because it is the clearest current internal pointer to impedance-specific tolerance and TDR language
2. `facts/methods/controlled-impedance-tdr-verification-posture.md`
   - next because it already normalizes the verification model and non-claim boundaries
3. `sources/registry/internal/frontendapt-materials-controlled-impedance-stackups-page-en.md`
   - then capture stackup-template and coupon-planning dependencies so recovery does not flatten into one promise
4. `wiki/testing/validation-ladder-from-e-test-to-si-verification.md`
   - use to lock evidence-layer boundaries before ingesting any numbers
5. `sources/registry/internal/frontendapt-pcb-high-speed-pcb-page-en.md`
   - use for high-speed context reconciliation
6. `sources/registry/internal/frontendapt-pcb-multilayer-pcb-page-en.md`
   - use for multilayer-service reconciliation
7. `sources/registry/internal/frontendhil-high-speed-product-page-en.md`
   - use as HIL-side cross-check
8. `sources/registry/internal/frontendhil-multilayer-pcb-product-page-en.md`
   - use as final HIL-side cross-check

## Current Bucket Decision

Current corpus support for `impedance_tolerance` is good enough for:

- framing controlled impedance as a coupled stackup-and-verification problem
- separating TDR / coupon posture from broader SI validation
- stating non-claim boundaries
- routing future dated capability-record recovery

Current corpus support is not good enough for:

- publishing a reusable transferable impedance-tolerance number
- claiming universal TDR coverage or identical validation scope across all programs
- converting internal page numerics into capability fact-card content
