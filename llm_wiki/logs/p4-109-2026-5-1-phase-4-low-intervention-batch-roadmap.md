Date: 2026-05-01
Lane: `P4-109 phase-4 low-intervention batch roadmap`
Input: `logs/p4-107-2026-5-1-ev-charger-lane-consumption-controller-integration.md`, `logs/p4-108-2026-5-1-neuromorphic-lane-consumption-controller-integration.md`, `logs/p4-67-2026-4-27-application-computing-sensor-defense-controller-summary.md`, `logs/p4-69-sensor-navigation-imaging-topic-aggregation.md`, `logs/p4-70-defense-ew-surveillance-targeting-topic-aggregation.md`, `logs/p4-71-targeting-laser-tof-and-pulsed-driver-source-backed-integration.md`, `logs/p4-72-sonar-transducer-front-end-source-backed-integration.md`, `logs/p4-73-radio-altimeter-rf-front-end-source-backed-integration.md`, `logs/p4-74-barometric-pressure-sensor-owner-source-backed-integration.md`, `logs/p4-76-eo-ir-detector-owner-source-backed-integration.md`, `logs/p4-77-embedded-imaging-serial-interface-source-backed-integration.md`, `logs/p4-78-thermal-imaging-output-video-and-machine-vision-interface-source-backed-integration.md`, `logs/p4-79-navigation-sensor-technology-owner-source-backed-integration.md`, `logs/p4-80-military-environmental-and-emi-standards-source-backed-integration.md`, `logs/p4-81-altimeter-aviation-standards-metadata-source-backed-integration.md`, `logs/p4-82-sonar-hydrophone-and-generic-beamforming-source-backed-integration.md`
Output: `logs/p4-109-2026-5-1-phase-4-low-intervention-batch-roadmap.md`
Scope status: `controller_planned`
Evidence status: `batch_execution_ready`

# Purpose

Set a low-intervention execution roadmap so subsequent Phase 4 work can be delegated to subagents in larger continuous batches, with controller integration only at batch boundaries rather than after every micro-step.

# Batch Decisions

## Batch A: Close The High-Value `2026.4.29` Normalization Work

- landed in this session:
  - `P4-106` smart-meter consumption explicit
  - `P4-107` EV-charger consumption explicit
  - `P4-108` neuromorphic consumption explicit
- deferred for now:
  - `hearing-aid` controller-normalization
  - `satellite` controller-normalization
- rationale:
  - `hearing-aid` and `satellite` already have sufficiently explicit draft-layer scope and blocked-claim posture
  - extra controller logs there would mostly restate known boundaries rather than close an active ambiguity

## Batch B: Execute `2026.4.27` Sensor / Navigation / Imaging Normalization

- recommended output type: `normalization`
- controller target:
  - convert the `2026.4.27` sensor / navigation / imaging slice into conservative draft-layer outputs using only already-landed support
- expected draft cluster:
  - `accelerometer-pcb.md`
  - `altimeter-pcb.md`
  - `compass-pcb.md`
  - `gyroscope-pcb.md`
  - `night-vision-pcb.md`
  - `sonar-pcb.md`
  - `thermal-imaging-pcb.md`
- execution rule:
  - prefer draft-layer consumption and scope normalization over any new authority recovery unless a publication-critical exact noun survives stripping

## Batch C: Decide The Next `2026.4.27` Residual After Batch B

- likely follow-on families:
  - defense / EW / surveillance / targeting normalization
  - targeted residual blocker scout only if a stripped draft still needs exact owner or standards nouns
- keep blocked by default:
  - `RS-170` / `STANAG 3350`
  - exact detector-performance numerics
  - exact RF architecture claims
  - exact hydrophone-array and beamforming implementation claims
  - mission, qualification, or supplier-proof language

# Controller Execution Mode

- subagents should receive whole-batch ownership rather than single-log micro-tasks
- the main controller should integrate results only when a batch reaches one of these boundaries:
  - a clear rewrite/normalization set is ready
  - a batch produces a hold or defer decision
  - tracker state must change to a new continuation point
- user intervention is not required between those boundaries unless:
  - a draft cannot be safely stripped without losing publication value
  - a new exact noun appears truly publication-critical
  - local files show conflicting tracker state

# Immediate Next Batch

1. keep `biological-computing` on hold
2. do not reopen `smart-meter`, `ev-charger`, or `neuromorphic` for another implicit-consumption check
3. assign the next long subagent batch to `2026.4.27` sensor / navigation / imaging normalization
4. update trackers only after that batch lands or is cleanly deferred

# Status

- active continuation state: `low_intervention_batch_mode_enabled`
- next controller entry: `2026_4_27_sensor_navigation_imaging_normalization_batch`
- tracker state: `updated_to_p4_109`
