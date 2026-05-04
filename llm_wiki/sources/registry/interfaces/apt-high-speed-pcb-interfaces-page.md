# Source Record: APT High-Speed PCB Interfaces Page

## Source Metadata

- **source_id**: apt_high_speed_pcb_interfaces_page
- **source_type**: internal_published_page
- **authority_tier**: Tier-2
- **organization**: APTPCB
- **title**: High-Speed PCB Manufacturing | 10–112G, ±5% Impedance | APTPCB
- **url**: file:///code/hileap/frontendAPT/public/static/pcb/en/high-speed-pcb.json
- **canonical_url**: https://aptpcb.com/en/pcb/high-speed-pcb
- **date_published**: 2026-05-01
- **date_accessed**: 2026-05-02
- **must_refresh**: false

## Content Summary

APTPCB high-speed PCB manufacturing capabilities supporting 10–112 Gbps SERDES interfaces, including PCIe Gen5/Gen6, and PAM4 channels.

## Interface Support

### Data Rates
| Interface | Speed | Support Status |
|-----------|-------|----------------|
| PCIe Gen5 | 32 GT/s | Supported |
| PCIe Gen6 | 64 GT/s | Supported |
| 56G PAM4 | 56 Gbps | Supported |
| 112G PAM4 | 112 Gbps | Supported |
| Ethernet 100G | 100 Gbps | Supported |
| Ethernet 400G | 400 Gbps | Reference design support |

### Material Requirements
- Dk ≤ 3.5
- Df ≤ 0.0015
- Low-roughness copper (Ra ≤ 1.5 µm)
- VLP/HVLP copper foil

### Manufacturing Capabilities
- 3/3 mil line/space (LDI imaging)
- 0.20 mm mechanical drills
- 0.067 mm laser microvias
- Controlled backdrill (< 0.25 mm stubs)
- VIPPO (Via-in-Pad Plated Over)
- ±5% impedance control

## Interface-Specific Features

### PCIe Support
- Gen5/Gen6 channel compliance
- Refclk distribution
- Lane margining considerations

### High-Speed Ethernet
- 100G/400G backplane support
- CDR and retimer integration
- BER compliance

### PAM4 Signaling
- 56G/112G PAM4 optimized stackups
- Loss budget management
- COM (Channel Operating Margin) compliance

## Validation Capabilities

- TDR (Time Domain Reflectometry)
- VNA (Vector Network Analyzer)
- S-parameter measurement to 30 GHz
- Eye diagram analysis
- Insertion loss verification

## Compliance Notes

High-speed designs require:
- Stackup co-design with SI team
- Material selection validation
- Impedance coupon verification
- Signal integrity reporting

## Extraction Notes

Extracted from APTPCB published high-speed PCB page. This is a Tier-2 internal source representing confirmed manufacturing capabilities for high-speed digital interfaces.
