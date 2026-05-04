# Source Record: APT Flying Probe Testing (FPT) Page

## Source Metadata

- **source_id**: apt_flying_probe_testing_page
- **source_type**: internal_published_page
- **authority_tier**: Tier-2
- **organization**: APTPCB
- **title**: Flying Probe Testing (FPT) for PCB & PCBA | APTPCB
- **url**: file:///code/hileap/frontendAPT/public/static/pcba/en/flying-probe-testing.json
- **canonical_url**: https://aptpcb.com/en/pcba/flying-probe-testing
- **date_published**: 2026-05-01
- **date_accessed**: 2026-05-02
- **must_refresh**: false

## Content Summary

APTPCB Flying Probe Testing (FPT) platform for fixture-free electrical verification of bare PCBs and assembled PCBAs.

### Key Advantages vs Bed-of-Nails

- **Zero fixture cost** - Software-driven, ideal for frequent design changes
- **High accuracy** - Fine-pitch, densely populated area access
- **Fast setup** - Rapid prototyping support
- **Non-destructive** - No special test pads or board modifications required

### Testing Capabilities

- Continuity & open circuit verification
- Short-circuit detection
- Component value measurement (R/C/L)
- Diode/transistor polarity & functionality
- Power net and isolation testing

### Design Guidelines for Optimal FPT

1. **Test Point Accessibility**: Distribute across board, avoid obstructions, dual-side coverage
2. **Test Point Features**: 0.5-1mm diameter typical, circular standard, smooth conductive finish (ENIG/HASL), adequate solder mask clearance
3. **Board Clamping**: Designated non-critical clamping areas, edge clearance, stable support
4. **Board Dimensions**: Verify max/min board size and thickness compatibility
5. **Component Height**: Ensure probe clearance, strategic tall component placement

### Test Process

1. Expert FPT test program creation (design analysis, test point mapping, sequence planning)
2. Program upload and verification (secure transfer, calibration, initial test run)
3. Automated electrical & power test signal application (board loading, probe positioning, signal application, measurement, real-time analysis, fault detection, results logging)

### PCB vs PCBA FPT Distinction

| Aspect | Bare PCB FPT | PCBA FPT |
|--------|--------------|----------|
| Focus | PCB integrity (traces, vias, pads) | PCB + all components |
| Timing | After fab, before assembly | After assembly |
| Tests | Continuity, shorts, impedance, isolation | All PCB tests + component verification |
| Accessibility | Full, unobstructed | May be limited by components |
| Speed | Typically faster | Generally slower |
| Faults | Manufacturing defects | PCB defects + placement + component issues |

### Applications

- Prototyping cycles acceleration
- Small to medium production runs
- Complex or densely populated boards
- Design verification without fixture investment

### Quality Integration

- NPI turnaround: 24-48 hours
- Part of inspection chain: AOI + X-Ray + ICT/FCT
- Process control with SPI feedback loop
- Defect tracking with PPM monitoring
- Traceability: Barcode + lot
- IPC-A-610 Class 2/3

## Extraction Notes

Tier-2 internal source for flying probe testing capabilities. Key differentiator from ICT is fixture-free operation making it ideal for prototypes and low-medium volume.
