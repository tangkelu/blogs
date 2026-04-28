# P4-37 `2025.8.1` Application / Inspection Official-Source Recovery Scout

Date: 2026-04-28
Model: `gpt-5.4`
Lane: `P4-37 official-source recovery scout`
Input batch: `/code/blogs/tmps/2025.8.1/en`
Prior map reviewed: `/code/blogs/llm_wiki/logs/p4-34-2025-8-1-pcba-process-and-service-blog-ingestion-map.md`

## Scope

This lane reviewed the `tmps` drafts as claim inventory only. It did not treat draft wording as fact and did not promote unsupported supplier capability, qualification, compliance, readiness, price, lead time, MOQ, yield, quality-rate, or application-fit claims.

Focus areas requested:

- FAI
- X-ray / AXI / BGA hidden-joint inspection
- HDMI / Ethernet / Wi-Fi / Bluetooth / GPS standards-boundary vocabulary
- automotive ADAS / ECU boundaries
- medical MRI / pacemaker boundaries
- aerospace / flight-control / defense boundaries
- application-specific blockers

## Changed Files

- Added `/code/blogs/llm_wiki/logs/p4-37-2025-8-1-application-inspection-official-source-recovery-scout.md`

## Lane Status

Status: `completed_at_claim_family_level`

Meaning:

- official-source candidates were identified and checked
- strongest fact-upgrade opportunities were identified
- blocked claim classes were made explicit
- no `facts/`, `wiki/`, source registry, or tracker edits were made in this lane because the user restricted edits to this log only

This is not full learning. Reusable `llm_wiki` facts still need a follow-on lane with permitted writes.

## Drafts Most Relevant To This Lane

- `pcb-first-article-inspection.md`
- `xray-pcb-inspection.md`
- `hdmi-pcb.md`
- `ethernet-pcb.md`
- `wifi-pcb.md`
- `bluetooth-pcb.md`
- `gps-pcb.md`
- `adas-pcb.md`
- `automotive-ecu-pcb.md`
- `mri-pcb.md`
- `pacemaker-pcb.md`
- `flight-control-pcb.md`
- adjacent risk spillover: `missile-pcb.md`, `drone-pcb.md`, `router-pcb.md`, `smart-tv-pcb.md`, `dashboard-pcb.md`

## Official Sources Checked

### Inspection / FAI / hidden-joint candidates

- SAE AS9102 family page: aerospace FAI requirement owner and status anchor  
  `https://saemobilus.sae.org/standards/as9102a-aerospace-first-article-inspection-requirement`
- SAE AS9145 page: APQP / PPAP owner and scope anchor  
  `https://saemobilus.sae.org/standards/as9145-aerospace-series-requirements-advanced-product-quality-planning-production-part-approval-process`
- IPC validation/QML page: official IPC high-level assembly acceptance vocabulary and explicit note that `IPC-J-STD-001` includes guidance on X-ray for conditions not visible otherwise  
  `https://www.ipc.org/ipc-validation-services-qualified-manufacturing-companies-qml-j-std-001610`
- IPC event page: official IPC acknowledgment that BGA defects and CT/X-ray inspection are relevant for voiding, non-wetting, and head-in-pillow analysis  
  `https://www.ipc.org/event/closer-look-ipc-x-ray-inspection-guidelines-bgas`

### Interface / networking / wireless standards owners

- HDMI Licensing Administrator official HDMI 2.1b page  
  `https://www.hdmi.org/spec/hdmi2_1/index.aspx`
- IEEE 802.3 Ethernet Working Group home  
  `https://www.ieee802.org/3/`
- IEEE P802.3dm automotive Ethernet task-force page  
  `https://www.ieee802.org/3/dm/index.html`
- Wi-Fi Alliance official certification certificate endpoints surfaced by search, showing certification is product- and feature-specific rather than generic PCB-level  
  example: `https://api.cert.wi-fi.org/api/certificate/download/public?variantId=139014`
- Bluetooth SIG official Core Specification page  
  `https://www.bluetooth.com/specifications/specs/core-specification/`
- GPS.gov official civil GPS accuracy / signal modernization page  
  `https://www.gps.gov/gps-accuracy`

### Automotive official standards / quality system anchors

- ISO official ISO 26262 package page  
  `https://www.iso.org/publication/PUB200262.html`
- ISO official ISO 26262 abstract pages confirming scope on safety-related E/E systems in road vehicles and boundary language  
  example: `https://www.iso.org/standard/51356.html`
- IATF official sanctioned-interpretations page confirming active standards-governance source for `IATF 16949:2016`  
  `https://www.iatfglobaloversight.org/iatf-169492016/iatf-169492016-sis/`
- AEC official document hub confirming AEC-Q standards are component qualification documents  
  `https://www.aecouncil.com/AECDocuments.html`

### Medical / MRI / pacemaker official anchors

- FDA MRI overview  
  `https://www.fda.gov/radiation-emitting-products/medical-imaging/mri-magnetic-resonance-imaging`
- FDA MRI benefits and risks page with `MR Safe`, `MR Conditional`, `MR Unsafe` boundary language and implant risk framing  
  `https://www.fda.gov/radiation-emitting-products/mri-magnetic-resonance-imaging/benefits-and-risks`
- FDA MRI information for industry  
  `https://www.fda.gov/radiation-emitting-products/mri-magnetic-resonance-imaging/mri-information-industry`
- FDA EMC page for medical devices  
  `https://www.fda.gov/electromagnetic-compatibilityemc`
- FDA CT / implantable electronic heart device page with official pacemaker/ICD MRI boundary wording  
  `https://www.fda.gov/radiation-emitting-products/electronic-medical-devices-x-ray-imaging-and-radiation-therapy-what-know-and-how-prevent-damage/preventing-damage-implantable-electronic-heart-devices-during-ct-scans`
- FDA cochlear implant MRI safety page, useful as a regulator example for implant MRI labeling logic  
  `https://www.fda.gov/medical-devices/cochlear-implants/cochlear-implants-and-mri-safety`

### Aerospace / flight-control / defense anchors

- FAA software and airborne electronic hardware page  
  `https://www.faa.gov/aircraft/air_cert/design_approvals/air_software/software_regs`
- FAA AC 20-152A page, explicitly naming circuit board assemblies within airborne electronic hardware guidance  
  `https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/1041323`
- FAA AC 00-72 page for AEH best practices  
  `https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/1032452`
- FAA aircraft certification / production approval pages  
  `https://www.faa.gov/aircraft/air_cert/design_approvals/air_software`  
  `https://www.faa.gov/aircraft/air_cert/production_approvals`
- SAE AS9100 landing page  
  `https://saemobilus.sae.org/standards/as9100-quality-systems-aerospace-model-quality-assurance-design-development-production-installation-servicing`
- DDTC / ITAR public portal surfaced but not fully useful for clause-level extraction in this lane  
  `https://www.pmddtc.state.gov/itar/`

## Strongest Fact-Upgrade Opportunities

These are the highest-signal upgrades that can be made from official sources without inflating supplier claims.

### 1. FAI can be rewritten as a documentation / objective-evidence gate, not a universal capability proof

Best upgrade path:

- use SAE AS9102 for aerospace FAI vocabulary: performing and documenting FAI, objective evidence, design/specification accountability
- use SAE AS9145 only for APQP / PPAP relationship where aerospace/regulated production planning is discussed
- keep generic PCB/PCBA FAI wording conservative unless an IPC or internal validated process source is added

What this upgrades:

- weak draft language about “bridge prototype and volume manufacturing”
- unsupported claims that FAI itself proves process capability, Cp/Cpk readiness, or mass-production conformance

### 2. X-ray / AXI content can be upgraded around hidden-joint visibility boundaries

Best upgrade path:

- use IPC high-level language that X-ray helps inspect solder conditions not visible otherwise
- use IPC BGA event language to anchor defect vocabulary such as voiding, non-wetting, and head-in-pillow
- frame AXI / CT as one inspection layer among AOI, ICT, functional test, and process controls

What this upgrades:

- “BGA hidden-joint inspection” language
- “X-ray for non-visible solder conditions” language
- “2D versus 3D/CT use-case distinction” at a high level

What it does not support:

- absolute detection guarantees
- exact resolution, angle, magnification, or defect-capture-rate numbers
- “best method” claims without controlled comparative evidence

### 3. HDMI drafts can be corrected to standards-owner language

Best upgrade path:

- HDMI Licensing Administrator page supports that HDMI 2.1b is the current official HDMI specification page checked on 2026-04-28
- safe vocabulary: higher resolutions, refresh rates, and bandwidth capability up to `48 Gbps`

What this upgrades:

- replace vague “HDMI 2.1 specifications” wording with standards-owner phrasing
- keep claims at interface/spec capability level, not PCB vendor qualification level

Blocked boundary:

- do not claim a PCB house “ensures compliance with HDMI specifications” without product-level compliance test evidence and licensed test context

### 4. Ethernet drafts can be upgraded to standards-owner vocabulary and automotive boundary separation

Best upgrade path:

- IEEE 802.3 is the official Ethernet standards owner
- use terms like `IEEE 802.3 Ethernet Working Group`, `PHY`, `MAC`, and automotive Ethernet as a standards family / task-force area rather than as generic PCB proof
- note that automotive Ethernet evolution is active; P802.3dm is still a task force, so avoid pretending every automotive Ethernet feature is settled and production-proven

What this upgrades:

- removes supplier-authored impedance and spacing numerics lacking official support
- introduces standards-boundary wording without overclaiming compliance

### 5. Wi-Fi and Bluetooth drafts can be corrected to certification-boundary language

Best upgrade path:

- Wi-Fi Alliance certification is product- and feature-specific
- Bluetooth SIG compliance is specification- and qualification-program specific
- both families support “designed for” or “intended for” wording better than “compliant” or “certified” wording at bare PCB level

What this upgrades:

- blocks “802.11 compliant PCB” and “Bluetooth 5.x compliant PCB” claims unless the finished module/device has actual certification/qualification evidence
- supports safer vocabulary such as:
  - Wi-Fi: `Wi-Fi CERTIFIED` is a product certification outcome from Wi-Fi Alliance
  - Bluetooth: interoperable Bluetooth devices are defined against the Bluetooth Core Specification and associated qualification materials

### 6. GPS drafts can be upgraded with official civil-signal boundary vocabulary

Best upgrade path:

- GPS.gov supports use of L1, L2, and L5 civil-signal modernization framing
- safe wording: GNSS / GPS receiver designs may target civil bands and multi-constellation operation

What this upgrades:

- removes unsupported sensitivity and positioning-performance marketing claims
- supports civil-signal naming without pretending module-level navigation accuracy from PCB layout alone

### 7. ADAS / ECU drafts can be upgraded by separating functional safety, quality management, and component qualification

Best upgrade path:

- ISO 26262: functional safety framework for safety-related E/E systems in road vehicles
- IATF 16949: automotive quality-management framework
- AEC-Q100: component-level qualification, not finished-PCB qualification

What this upgrades:

- blocks repeated draft error of treating `AEC-Q100` as a PCB or assembly qualification
- blocks “ISO 26262-compliant PCB manufacturing” unless the claim is carefully scoped to participation in a larger safety lifecycle
- supports accurate phrasing like:
  - `used in systems developed under ISO 26262 processes`
  - `automotive quality-management systems may be aligned to IATF 16949`
  - `components may be selected to AEC-Q standards`

### 8. MRI and pacemaker drafts can be upgraded by switching from “medical-ready PCB” claims to device-labeling and risk-boundary language

Best upgrade path:

- FDA MRI pages support hazard vocabulary around static field, gradient field, and RF energy
- FDA uses `MR Safe`, `MR Conditional`, and `MR Unsafe` for device labeling context
- FDA pages show electrically active implants can malfunction in the MR environment and that unknown MRI safety status should be assumed unsafe

What this upgrades:

- blocks unsupported “MRI-compatible PCB” and “pacemaker-ready PCB” marketing language
- supports safer phrasing such as:
  - `devices intended for MRI environments need device-level MR safety evaluation and labeling`
  - `implantable and active devices require device-specific MRI conditions of safe use`
  - `PCB design alone does not establish MRI safety or implant safety`

### 9. Flight-control / aerospace drafts can be upgraded by moving from generic “certified production” language to FAA / SAE / RTCA boundary language

Best upgrade path:

- FAA AC 20-152A and AC 00-72 support airborne electronic hardware design assurance framing
- FAA explicitly mentions custom devices, COTS IP, COTS devices, and circuit board assemblies in airborne electronic hardware guidance
- AS9100 is a QMS anchor, not proof that a PCB is approved for flight use

What this upgrades:

- blocks “flight-certified PCB” claims
- supports wording such as:
  - `circuit board assemblies may be part of airborne electronic hardware subject to design-assurance processes`
  - `avionics acceptance requires program-specific certification and approval evidence`

## Highest-Risk Blocked Claims

These claims appeared or were strongly implied in drafts and should remain blocked until supported by stronger evidence than the sources checked here.

### Inspection / FAI / AXI

- Cp / Cpk / MSA / gauge R&R / control-limit claims tied to a specific supplier process
- exact X-ray resolution such as `1 µm` or `1-2 µm`
- exact viewing-angle, magnification, or defect-detection rates
- “AXI guarantees hidden-joint integrity”
- “FAI proves manufacturing capability for mass production”

### HDMI / Ethernet / Wi-Fi / Bluetooth / GPS

- interface/protocol compliance of a bare PCB
- HDMI / Ethernet / Wi-Fi / Bluetooth certification or compliance claims without device-level testing records
- exact routing dimensions, skew values, spacing rules, and impedance tolerances presented as universal standards requirements
- RF range, throughput, sensitivity, BER, protocol pass-rate, or eye-diagram outcome claims tied to the supplier

### Automotive

- `AEC-Q100` or other AEC-Q claims as proof of PCB or PCBA qualification
- `ISO 26262 compliant manufacturing` as a generic supplier status
- ADAS / brake-by-wire / steer-by-wire / autonomous readiness claims
- PPAP, EMC, functional safety, or long-life automotive readiness claims without program evidence

### Medical

- `ISO 13485 certified` unless a directly verified certificate is provided
- MRI-safe / MRI-compatible / MR-conditional claims for boards or assemblies absent device labeling evidence
- pacemaker, neurostimulator, or implantable-device suitability claims
- biocompatibility claims for PCB materials unless tied to the final patient-contact system and validated use case

### Aerospace / defense

- AS9100 or FAA guidance as proof of flight qualification
- `ITAR compliant manufacturing` or defense eligibility without current legal/compliance evidence
- military / missile / defense / mission-critical readiness claims
- lead-time or fast-turn claims for regulated aerospace or defense hardware

## Application-Specific Boundary Notes

### ADAS / ECU

- ISO 26262 is about safety-related E/E systems and lifecycle activities, not a shortcut badge for a PCB shop.
- AEC-Q standards apply to components.
- Automotive Ethernet remains standards-active; do not collapse draft vocabulary into “all automotive Ethernet is solved and qualified.”

### MRI

- FDA framing is hazard-first: static field, time-varying field, RF heating, device motion, malfunction, and image degradation.
- MRI claims must be device-level, condition-specific, and labeling-backed.

### Pacemaker / implantables

- FDA explicitly distinguishes `MR Conditional` and `MR Unsafe`.
- Unknown MRI status should be treated as unsafe.
- Implantable-device suitability cannot be inferred from PCB materials, assembly cleanliness, or general medical-market language.

### Flight control / avionics

- FAA design-assurance guidance covers airborne electronic hardware and circuit board assemblies in a certification context.
- QMS claims and workmanship class claims are not the same as airworthiness approval.

### Defense / missile

- DDTC / ITAR and defense status claims require a legal/export-control evidence chain, not just technical marketing language.
- `missile-pcb.md` is especially high risk and should not be upgraded from this source set except for strong cautionary boundary wording.

## Residual Gaps

These gaps remained after the official-source scout and should drive a follow-on fact-writing lane.

- direct official-source support for generic commercial PCB FAI outside aerospace terminology
- more specific IPC document-backed wording for AXI, void interpretation, and hidden-joint acceptance boundaries
- official Wi-Fi Alliance public program pages were not fetchable cleanly in this environment; certification certificate artifacts were enough to confirm product-specific certification logic but not ideal for reusable fact extraction
- exact current Bluetooth qualification workflow pages beyond the core specification landing page
- direct public official text for `IATF 16949` scope statement beyond governance/sanctioned-interpretation pages
- direct public official `ISO 13485` scope wording if medical-manufacturing drafts are later rehabilitated
- stronger official defense/export-control source extraction from DDTC / eCFR if defense pages are to be retained at all

## Best Follow-On Fact Cards To Create When Edits Are Permitted

- `facts/methods/fai-objective-evidence-and-process-capability-boundary.md`
- `facts/methods/axi-hidden-joint-inspection-boundary-official-source-pack.md`
- `facts/standards/hdmi-2-1b-official-capability-boundary.md`
- `facts/standards/ieee-802-3-ethernet-standards-owner-and-automotive-boundary.md`
- `facts/standards/wifi-certified-product-level-boundary.md`
- `facts/standards/bluetooth-core-specification-and-qualification-boundary.md`
- `facts/standards/gps-civil-signal-boundary-l1-l2-l5.md`
- `facts/standards/iso-26262-vs-iatf-16949-vs-aec-q-boundary.md`
- `facts/standards/fda-mr-safe-conditional-unsafe-boundary.md`
- `facts/standards/faa-airborne-electronic-hardware-cba-boundary.md`

## Bottom Line

The best recovery opportunities are not supplier-proof claims. They are boundary upgrades:

- FAI as objective evidence and documentation, not automatic capability proof
- X-ray / AXI as concealed-joint visibility support, not universal acceptance proof
- HDMI / Ethernet / Wi-Fi / Bluetooth / GPS as standards-owner vocabulary, not bare-PCB compliance proof
- ADAS / ECU as lifecycle / QMS / component-qualification separation
- MRI / pacemaker as FDA MR-labeling and implant-risk boundaries
- flight-control / aerospace / defense as certification and export-control boundary language, not generic “qualified manufacturer” claims

This lane leaves the batch safer to rewrite, but not yet fully learned into `llm_wiki`.
