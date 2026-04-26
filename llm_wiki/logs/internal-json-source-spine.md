# Internal JSON Source Spine

Last updated: 2026-04-24

## Purpose

This file tracks the English non-blog JSON content that should be treated as the internal data spine for `frontendAPT` and `frontendHIL`.

It does not convert every JSON file into a fact card. Instead, it defines the source universe so future batches can extract facts systematically and avoid repeatedly rediscovering the same internal pages.

## Scope Rules

- Include English non-blog JSON only.
- Exclude generated `.output`, `.nuxt`, cache, dependency, and `node_modules` files.
- Exclude blog markdown and blog payloads.
- Treat these files as `internal support`, not external primary sources.
- Numeric claims from these files require refresh before publication if used as firm customer-facing commitments.

## frontendAPT English JSON

Root:

- `/code/hileap/frontendAPT/public/static`

Covered English source groups:

- `capabilities/en`: `7` files
- `industries/en`: `10` files
- `materials/en`: `10` files
- `pcb/en`: `33` files
- `pcba/en`: `32` files
- `resources/en`: `6` files

Total covered English APT non-blog JSON files: `98`.

### APT Capabilities

- `public/static/capabilities/en/ceramic-pcb.json`
- `public/static/capabilities/en/flex-pcb.json`
- `public/static/capabilities/en/hdi-pcb.json`
- `public/static/capabilities/en/index.json`
- `public/static/capabilities/en/metal-pcb.json`
- `public/static/capabilities/en/rigid-flex-pcb.json`
- `public/static/capabilities/en/rigid-pcb.json`

### APT Industries

- `public/static/industries/en/aerospace-defense-pcb.json`
- `public/static/industries/en/automotive-electronics-pcb.json`
- `public/static/industries/en/communication-equipment-pcb.json`
- `public/static/industries/en/drone-uav-pcb.json`
- `public/static/industries/en/industrial-control-pcb.json`
- `public/static/industries/en/medical-pcb.json`
- `public/static/industries/en/power-energy-pcb.json`
- `public/static/industries/en/robotics-pcb.json`
- `public/static/industries/en/security-equipment-pcb.json`
- `public/static/industries/en/server-data-center-pcb.json`

### APT Materials

- `public/static/materials/en/arlon-pcb.json`
- `public/static/materials/en/controlled-impedance-stackups.json`
- `public/static/materials/en/index.json`
- `public/static/materials/en/isola-pcb.json`
- `public/static/materials/en/megtron-pcb.json`
- `public/static/materials/en/rf-rogers.json`
- `public/static/materials/en/rogers-pcb-manufacturing.json`
- `public/static/materials/en/spread-glass-fr4.json`
- `public/static/materials/en/taconic-pcb.json`
- `public/static/materials/en/teflon-pcb.json`

### APT PCB

- `public/static/pcb/en/advanced-pcb-manufacturing.json`
- `public/static/pcb/en/antenna-pcb.json`
- `public/static/pcb/en/backplane-pcb.json`
- `public/static/pcb/en/ceramic-pcb.json`
- `public/static/pcb/en/flex-pcb.json`
- `public/static/pcb/en/fr4-pcb.json`
- `public/static/pcb/en/hdi-pcb.json`
- `public/static/pcb/en/heavy-copper-pcb.json`
- `public/static/pcb/en/high-frequency-pcb.json`
- `public/static/pcb/en/high-layer-count-pcb.json`
- `public/static/pcb/en/high-speed-pcb.json`
- `public/static/pcb/en/high-tg-pcb.json`
- `public/static/pcb/en/high-thermal-pcb.json`
- `public/static/pcb/en/index.json`
- `public/static/pcb/en/industry-solutions.json`
- `public/static/pcb/en/mass-production-pcb-manufacturing.json`
- `public/static/pcb/en/metal-core-pcb.json`
- `public/static/pcb/en/microwave-pcb.json`
- `public/static/pcb/en/multi-layer-laminated-structure.json`
- `public/static/pcb/en/multilayer-pcb.json`
- `public/static/pcb/en/npi-small-batch-pcb-manufacturing.json`
- `public/static/pcb/en/pcb-conformal-coating.json`
- `public/static/pcb/en/pcb-drilling.json`
- `public/static/pcb/en/pcb-fabrication-process.json`
- `public/static/pcb/en/pcb-impedance-control.json`
- `public/static/pcb/en/pcb-profiling.json`
- `public/static/pcb/en/pcb-prototype.json`
- `public/static/pcb/en/pcb-quality.json`
- `public/static/pcb/en/pcb-stack-up.json`
- `public/static/pcb/en/pcb-surface-finishes.json`
- `public/static/pcb/en/quick-turn-pcb.json`
- `public/static/pcb/en/rigid-flex-pcb.json`
- `public/static/pcb/en/special-pcb-manufacturing.json`

### APT PCBA

- `public/static/pcba/en/aoi-inspection.json`
- `public/static/pcba/en/bga-qfn-fine-pitch.json`
- `public/static/pcba/en/bga-reballing.json`
- `public/static/pcba/en/box-build-assembly.json`
- `public/static/pcba/en/cable-assembly.json`
- `public/static/pcba/en/component-sourcing.json`
- `public/static/pcba/en/components-bom.json`
- `public/static/pcba/en/fct-test.json`
- `public/static/pcba/en/final-quality-inspection.json`
- `public/static/pcba/en/first-article-inspection.json`
- `public/static/pcba/en/flex-rigid-flex.json`
- `public/static/pcba/en/flying-probe-testing.json`
- `public/static/pcba/en/harness-assembly.json`
- `public/static/pcba/en/ic-programming.json`
- `public/static/pcba/en/ict-test.json`
- `public/static/pcba/en/incoming-quality-control.json`
- `public/static/pcba/en/index.json`
- `public/static/pcba/en/mass-production.json`
- `public/static/pcba/en/npi-assembly.json`
- `public/static/pcba/en/pcb-conformal-coating.json`
- `public/static/pcba/en/pcb-selective-soldering.json`
- `public/static/pcba/en/pcb-stencil.json`
- `public/static/pcba/en/quality-system.json`
- `public/static/pcba/en/small-batch.json`
- `public/static/pcba/en/smt-tht.json`
- `public/static/pcba/en/smt-tnt.json`
- `public/static/pcba/en/spi-inspection.json`
- `public/static/pcba/en/support-services.json`
- `public/static/pcba/en/testing-quality.json`
- `public/static/pcba/en/turnkey-assembly.json`
- `public/static/pcba/en/x-ray-inspection.json`
- `public/static/pcba/en/xray-inspection.json`

### APT Resources

- `public/static/resources/en/dfm-guidelines.json`
- `public/static/resources/en/downloads-materials.json`
- `public/static/resources/en/downloads.json`
- `public/static/resources/en/faq.json`
- `public/static/resources/en/glossary-terms.json`
- `public/static/resources/en/index.json`

## frontendHIL English JSON

Roots:

- `/code/hileap/frontendHIL/public/static/products/en`
- `/code/hileap/frontendHIL/data/service-landings/en`

Covered English source groups:

- `products/en`: `24` files
- `service-landings/en`: `3` files

Total covered English HIL non-blog JSON files: `27`.

### HIL Products

- `public/static/products/en/backplane-pcb.json`
- `public/static/products/en/box-build-assembly.json`
- `public/static/products/en/ceramic-pcb.json`
- `public/static/products/en/flex-pcb.json`
- `public/static/products/en/fr4-pcb.json`
- `public/static/products/en/halogen-free-pcb.json`
- `public/static/products/en/hdi-pcb.json`
- `public/static/products/en/heavy-copper-pcb.json`
- `public/static/products/en/high-frequency-pcb.json`
- `public/static/products/en/high-speed-pcb.json`
- `public/static/products/en/high-tg-pcb.json`
- `public/static/products/en/high-thermal-pcb.json`
- `public/static/products/en/ic-substrate-pcb.json`
- `public/static/products/en/large-volume-assembly.json`
- `public/static/products/en/metal-core-pcb.json`
- `public/static/products/en/multilayer-pcb.json`
- `public/static/products/en/rigid-flex-pcb.json`
- `public/static/products/en/rogers-pcb.json`
- `public/static/products/en/single-double-layer-pcb.json`
- `public/static/products/en/small-batch-assembly.json`
- `public/static/products/en/smt-assembly.json`
- `public/static/products/en/teflon-pcb.json`
- `public/static/products/en/through-hole-assembly.json`
- `public/static/products/en/turnkey-assembly.json`

### HIL Service Landings

- `data/service-landings/en/pcb-prototype.json`
- `data/service-landings/en/pcb-surface-finish.json`
- `data/service-landings/en/quick-turn-pcb.json`

## First Extraction Priority

The largest newly visible gap is PCBA. Priority extraction order:

1. PCBA assembly flow and mixed-technology execution
2. SPI / AOI / X-ray / ICT / FCT layered quality stack
3. FAI, traceability, and quality-system gates
4. Component sourcing and BOM lifecycle controls
5. Box build / harness / system integration
6. Materials and industry pages after PCBA baseline is covered

