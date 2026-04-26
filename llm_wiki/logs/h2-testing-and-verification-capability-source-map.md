# H2 Testing And Verification Capability Source Map

Date: 2026-04-26

## Purpose

This file maps the current corpus into support classes for the `testing_and_verification_capability` H2 bucket.

It is a governance and source-mapping document.

It is not:

- a source registry record
- a fact card
- approval to publish transferable verification-scope or coverage numbers

## Relation To H2 Policy

Under `h2-capability-number-policy.md`, testing and verification capability is a fabrication-capability numeric bucket whenever it becomes a scope, coverage, or service promise.

That means:

- internal quality, impedance, high-speed, and backplane pages can support framing and recovery routing
- method cards can support scope separation and boundary language
- none of the current internal prose sources, by themselves, authorize reusable verification numerics
- future `keep` status still requires a dated capability record with scope and refresh discipline

## Source Classes

### 1. Downgrade / Framing Support

These sources are useful for explaining how validation fits into multilayer, high-speed, and quality workflows.

They do not authorize reusable verification numerics.

#### `facts/methods/advanced-validation-scope-segmentation.md`

- role:
  - downgrade / framing support
- why it is useful:
  - separates baseline electrical test, TDR, destructive metrology, and deeper SI validation
- why it is limited:
  - explicitly says exact maximum frequency, coverage percentage, and program scope must be re-checked before publication
- H2 handling:
  - use for workflow language and claim splitting
  - do not treat as evidence for a transferable scope number

#### `facts/methods/controlled-impedance-tdr-verification-posture.md`

- role:
  - downgrade / framing support
- why it is useful:
  - keeps impedance targets tied to verification posture
- why it is limited:
  - explicitly says tolerance bands, coverage, and coupon scope are refresh-sensitive internal claims
- H2 handling:
  - use for intake-planning and workflow language
  - do not promote numeric scope claims from this card

#### `wiki/testing/validation-ladder-from-e-test-to-si-verification.md`

- role:
  - downgrade / framing support
- why it is useful:
  - clearly separates electrical test, impedance correlation, and deeper SI / RF verification
- why it is limited:
  - exact maximum frequency, report depth, and package scope must refresh before publishing
- H2 handling:
  - use to keep validation layers separated
  - do not lift numerics from this page into capability facts

#### `sources/registry/internal/frontendapt-pcb-quality-page-en.md`

- role:
  - downgrade / framing support
- why it is useful:
  - strongest current internal pointer for quality-system, electrical test, TDR, and microsection wording
- why it is limited:
  - internal scope language is not a dated public capability record
- H2 handling:
  - use as routing metadata for future capability-record recovery
  - not valid as a standalone numeric source

#### `sources/registry/internal/frontendapt-pcb-high-speed-pcb-page-en.md`

- role:
  - downgrade / framing support
- why it is useful:
  - identifies higher-speed build framing and validation posture
- why it is limited:
  - extraction notes explicitly say speed grades and validation numbers are refresh-sensitive internal claims
- H2 handling:
  - use for routing and non-claim boundaries only

#### `sources/registry/internal/frontendhil-high-speed-product-page-en.md`

- role:
  - downgrade / framing support
- why it is useful:
  - adds HIL-side high-speed validation posture coverage
- why it is limited:
  - extraction notes explicitly say to use it as support, not source-of-truth
- H2 handling:
  - use for scope and wording control only

#### `sources/registry/internal/frontendapt-backplane-pcb-page-en.md`

- role:
  - downgrade / framing support
- why it is useful:
  - helpful when validation scope is embedded in backplane-specific language
- why it is limited:
  - current wording remains internal scope framing, not governed numeric authority
- H2 handling:
  - use to map which high-speed validation claims belong in this bucket

#### `sources/registry/internal/frontendhil-backplane-product-page-en.md`

- role:
  - downgrade / framing support
- why it is useful:
  - corroborates HIL-side backplane validation posture
- why it is limited:
  - process and validation figures are support-only
- H2 handling:
  - useful for cross-checking wording, not for numeric promotion

### 2. Posture Support

These sources are the strongest current support for how the bucket should be described, bounded, and split.

They support process posture and governance, not reusable numerics.

#### `facts/methods/advanced-validation-scope-segmentation.md`

- role:
  - posture support
- what it supports safely:
  - validation scope is layered
  - electrical test, impedance checks, and deeper SI work should not be flattened into one bucket
- what it does not support:
  - fixed test-package numerics
  - coverage promises

#### `facts/methods/controlled-impedance-tdr-verification-posture.md`

- role:
  - posture support
- what it supports safely:
  - impedance claims should stay tied to verification language
  - coupon / TDR correlation belongs in the evidence model
- what it does not support:
  - transferable tolerance or scope numerics

#### `facts/methods/high-speed-interface-system-context.md`

- role:
  - posture support
- what it supports safely:
  - higher-speed system migrations explain why stronger validation planning may be needed
- what it does not support:
  - direct validation-package claims
  - board-level capability proof

### 3. Non-Claim Boundaries

These sources are especially valuable because they say what the current corpus cannot safely claim.

#### `facts/methods/advanced-validation-scope-segmentation.md`

- boundary value:
  - does not prove every order receives the full advanced validation stack
  - does not prove all test types are standard-scope

#### `facts/methods/controlled-impedance-tdr-verification-posture.md`

- boundary value:
  - does not say every board is shipped with identical TDR coverage
  - does not claim a universal verification scope or tolerance package

#### `wiki/testing/validation-ladder-from-e-test-to-si-verification.md`

- boundary value:
  - TDR is not full-path SI validation
  - exact scope, frequency, and package detail must refresh before publishing

#### relevant internal registry records

- boundary value:
  - multiple records explicitly flag validation numbers as internal, refresh-sensitive, support-only, or not source-of-truth
- implication:
  - current registry records help route recovery but do not authorize transferable scope or coverage numbers

### 4. Candidate Upstream Inputs For Future Dated Capability Record

These are the best current upstream inputs if a future Tier 1 dated capability record is created for `testing_and_verification_capability`.

They are candidates because they identify internal source families, terminology, and likely owning pages.

They are not themselves the future capability record.

#### primary candidate set

- `sources/registry/internal/frontendapt-pcb-quality-page-en.md`
  - closest current internal registry anchor to electrical-test, TDR, and microsection wording
- `facts/methods/advanced-validation-scope-segmentation.md`
  - best current normalized summary of layered validation scope
- `facts/methods/controlled-impedance-tdr-verification-posture.md`
  - strongest pointer for impedance-related verification language

#### secondary candidate set

- `sources/registry/internal/frontendapt-pcb-high-speed-pcb-page-en.md`
  - useful when validation scope is embedded in higher-speed build language
- `sources/registry/internal/frontendhil-high-speed-product-page-en.md`
  - useful for HIL-side consistency checking
- `sources/registry/internal/frontendapt-backplane-pcb-page-en.md`
  - useful when scope language appears in backplane-specific posture
- `sources/registry/internal/frontendhil-backplane-product-page-en.md`
  - useful HIL-side cross-check for backplane validation wording

## Sources That Explicitly Require Refresh Or Do Not Authorize Transferable Verification Numbers

### explicitly refresh-sensitive

- `facts/methods/advanced-validation-scope-segmentation.md`
  - exact maximum frequency, coverage percentage, or environmental-test condition must be re-checked before publication
- `facts/methods/controlled-impedance-tdr-verification-posture.md`
  - tolerance bands, coverage percentages, and coupon scope are refresh-sensitive
- `wiki/testing/validation-ladder-from-e-test-to-si-verification.md`
  - exact maximum frequency, validation scope, report depth, and package details must refresh before publishing
- current internal registry records in this bucket
  - internal validation and quality figures are support-only until re-issued as dated capability records

### not valid for transferable verification numbers on their own

- all current internal registry records in this bucket
  - because they are internal support pages, not Tier 1 dated capability records
