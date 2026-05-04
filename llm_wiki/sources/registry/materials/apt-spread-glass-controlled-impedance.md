# Source Record: APT Spread-Glass & Controlled Impedance Materials

## Source Metadata

- **source_id**: apt_spread_glass_controlled_impedance
- **source_type**: internal_published_page
- **authority_tier**: Tier-2
- **organization**: APTPCB
- **title**: Spread-Glass FR-4 & Controlled Impedance Stackups | APTPCB
- **url**: file:///code/hileap/frontendAPT/public/static/materials/en/spread-glass-fr4.json, file:///code/hileap/frontendAPT/public/static/materials/en/controlled-impedance-stackups.json
- **canonical_url**: https://aptpcb.com/en/materials/spread-glass-fr4, https://aptpcb.com/en/materials/controlled-impedance-stackups
- **date_published**: 2026-05-01
- **date_accessed**: 2026-05-02
- **must_refresh**: false

## Content Summary

Spread-glass technology and controlled impedance stackups for high-speed digital applications.

### Spread-Glass Technology

**Problem**: Fiber-weave effect causes differential pair skew in 10-112 Gbps channels.
- Standard woven glass has Dk variation (glass ~6.1, resin ~2.8)
- Causes timing differences that collapse signal eye

**Solution**: Mechanically spread glass fabrics
| Style | Construction | Skew Performance |
|-------|------------|------------------|
| **1035** | Spread single-ply | Excellent |
| **1067** | Spread single-ply | Excellent |
| **2116-SG** | Spread dual-ply | Very good |
| **3313** | Spread dual-ply | Good |

### Skew Mitigation Results
- **Before**: Significant skew from fiber-weave
- **After**: ≤1.0 ps/inch skew with spread-glass

### Controlled Impedance Stackups
| Layers | Structure | Typical Impedance | Tolerance |
|--------|-----------|-------------------|-----------|
| **2L** | Microstrip | 50Ω SE | ±10% |
| **4L** | Microstrip/Stripline | 50Ω SE, 100Ω diff | ±10% |
| **6L** | Dual stripline | 50Ω SE, 100Ω diff | ±5% |
| **6L HDI** | Microvia build-up | Various | ±5% |
| **8L Hybrid** | Rogers + FR-4 | RF + digital | ±5% |
| **10L+** | Backplane | SE/Diff stripline | ±5% |

### Applications
- PCIe Gen5 (32 GT/s)
- 56G/112G PAM4 SerDes
- 400G Ethernet
- DDR5 memory interfaces
- Advanced switch fabrics

### Copper Options
- VLP (Very Low Profile)
- HVLP (Hyper Very Low Profile)
- For reduced conductor loss

### Validation
- TDR coupons measured on every build
- VNA insertion-loss sweeps to 40 GHz
- Skew coupons for spread-glass verification
- COM/eye-diagram analysis available

## Extraction Notes

Tier-2 internal source for spread-glass and controlled-impedance capabilities. Critical for 56G+ high-speed digital designs.
