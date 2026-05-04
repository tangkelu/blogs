# Fact Card: Taconic PTFE/Ceramic Laminate Family Parameters

## Fact Metadata

- **fact_id**: taconic_ptfe_laminate_family_parameters
- **fact_type**: material_parameters
- **source_id**: apt_taconic_materials_page
- **authority_tier**: Tier-2
- **domain**: rf_microwave_materials
- **application**: high_frequency_pcb
- **date_extracted**: 2026-05-02
- **verification_status**: verified

## Product Series Overview

### TLY Series (Ultra-Low Loss)

| Property | TLY-5A | TLY-3 | Test Method |
|----------|--------|-------|-------------|
| **Dk @ 10 GHz** | 2.17 ±0.02 | 2.33 ±0.02 | IPC-TM-650 2.5.5.5 |
| **Df @ 10 GHz** | 0.0009 | 0.0009 | IPC-TM-650 2.5.5.5 |
| **Thermal Conductivity** | 0.23 W/m·K | 0.26 W/m·K | ASTM E1461 |
| **CTE X/Y** | 25 ppm/°C | 18 ppm/°C | IPC-TM-650 2.4.41 |
| **CTE Z** | 280 ppm/°C | 280 ppm/°C | IPC-TM-650 2.4.41 |
| **Moisture Absorption** | 0.02% | 0.02% | IPC-TM-650 2.6.2.1 |
| **Peel Strength** | 6 lb/in | 8 lb/in | IPC-TM-650 2.4.8 |
| **Tg** | N/A (PTFE) | N/A (PTFE) | IPC-TM-650 2.4.25 |
| **Dielectric Strength** | 800 V/mil | 800 V/mil | IPC-TM-650 2.5.6.2 |
| **Flammability** | V-0 | V-0 | UL 94 |
| **Plasma Desmear** | Required | Required | - |

**Applications**: Satellite LNA boards, Ka-band phased-array antenna feeds, military EW wideband receivers, stripline power combiners, VNA calibration substrates

**Key Characteristics**: Lowest-loss Taconic laminate. Woven fiberglass reinforcement provides mechanical stability while PTFE matrix delivers ultra-low dielectric loss. Very low moisture absorption (0.02%).

### TLX Series (Moderate Loss)

| Property | TLX-8 | Notes |
|----------|-------|-------|
| **Dk @ 10 GHz** | 2.55 ±0.04 | Higher than TLY enabling more compact traces |
| **Df @ 10 GHz** | 0.0019 | Moderate loss |
| **Thermal Conductivity** | 0.26 W/m·K | |
| **CTE X/Y** | 15 ppm/°C | Good dimensional stability |
| **CTE Z** | 280 ppm/°C | |
| **Moisture Absorption** | 0.02% | Very low |
| **Peel Strength** | 8 lb/in | Good adhesion |
| **Plasma Desmear** | Required | PTFE processing |

**Applications**: Base-station duplexers and bandpass filters, Wilkinson power dividers, GPS/GNSS patch arrays, radar transmit/receive modules

**Key Characteristics**: Moderate-loss PTFE with slightly higher Dk than TLY. Good balance of electrical performance and dimensional stability.

### TLC Series (Economy PTFE)

| Property | Value | Notes |
|----------|-------|-------|
| **Dk Range** | 2.95-3.20 | Entry-level RF performance |
| **Df @ 10 GHz** | 0.0020 | Better than FR-4, lower than TLY/TLX |
| **Processing** | Plasma desmear required | Less demanding than pure-TLY |

**Applications**: Wi-Fi 6/7 front-end modules, Bluetooth antenna boards, ISM-band industrial monitoring radios, automotive V2X communication

**Key Characteristics**: Cost-reduced PTFE entry point for applications needing better-than-FR-4 RF performance without justifying TLY premium.

### RF-35 Series (Ceramic-Filled PTFE)

| Property | RF-35A2 | Notes |
|----------|---------|-------|
| **Dk @ 10 GHz** | 3.50 ±0.05 | Tight tolerance |
| **Df @ 10 GHz** | 0.0018 | Lower than RO4350B |
| **Thermal Conductivity** | 0.62 W/m·K | Good heat spreading |
| **CTE X/Y** | 14 ppm/°C | Excellent stability |
| **CTE Z** | 30 ppm/°C | Better than RO4350B (32) |
| **Moisture Absorption** | 0.06% | Low |
| **Peel Strength** | 8 lb/in | Strong adhesion |
| **Tg** | >280°C | High temperature stability |
| **Dielectric Strength** | 750 V/mil | |
| **Flammability** | V-0 | |
| **Plasma Desmear** | Recommended (PTFE) | For optimal via reliability |

**Applications**: Sub-6 GHz 5G macro and small-cell antennas, power amplifier pallets, GPS receivers, WLAN enterprise access points, general commercial RF

**Stocked Thicknesses**: 10-60 mil with 1/2 oz and 1 oz ED copper

**Key Characteristics**: ORCER family ceramic-filled PTFE. Dk 3.50 with tight ±0.05 tolerance. Notably lower Df than Rogers RO4350B (0.0018 vs 0.0037 = 51% lower loss). Lead-free solder compatible.

### CER Series (High-Dk Ceramic)

| Property | CER-10 | CER-20/30 | Notes |
|----------|--------|-----------|-------|
| **Dk Range** | 10.0 | 20.0-30.0 | Extremely high Dk |
| **Dk Tolerance** | ±0.25 | - | Tight for high-Dk |
| **Df @ 10 GHz** | 0.0035 | - | Moderate loss |
| **Thermal Conductivity** | 0.42 W/m·K | - | |
| **CTE X/Y** | 8 ppm/°C | - | Excellent stability |
| **CTE Z** | 20 ppm/°C | - | Very low |
| **Moisture Absorption** | 0.05% | - | Low |
| **Peel Strength** | 5 lb/in | - | Good for ceramic-filled |
| **Dielectric Strength** | 600 V/mil | - | |
| **Plasma Desmear** | Required | - | |

**Stocked Thicknesses**: CER-10 in 20-40 mil

**Applications**: Dielectric resonator antennas (DRA), compact cavity filters, horn antenna feed elements, miniaturized GPS L1/L2 patch antennas

**Key Characteristics**: Extremely high dielectric constant enables physically small antennas and filters. Ceramic loading provides excellent Dk stability over temperature.

### fastRise 27/27HF (Bonding Prepreg)

| Property | Value | Notes |
|----------|-------|-------|
| **Dk @ 10 GHz** | 2.72 ±0.04 | Low-loss bonding |
| **Df @ 10 GHz** | 0.0014 | Minimal signal degradation |
| **Thermal Conductivity** | 0.28 W/m·K | |
| **CTE X/Y** | 12 ppm/°C | Good match to cores |
| **CTE Z** | 40 ppm/°C | |
| **Moisture Absorption** | 0.03% | Very low |
| **Peel Strength** | 6 lb/in | Adequate for bonding |
| **Tg** | >250°C | Thermoset stability |
| **Dielectric Strength** | 700 V/mil | |
| **Flammability** | V-0 | |

**Applications**: Hybrid Taconic TLY/FR-4 multilayer boards, hybrid Rogers RO4350B/FR-4 bonding, high-speed digital boards with integrated RF sections

**Key Characteristics**: Specifically designed as bonding prepreg for hybrid multilayer builds combining PTFE signal cores with FR-4 structural cores. Low-loss resin system minimizes signal degradation at bond interface. Compatible with both Taconic and Rogers RF cores.

### TacLam (Pure PTFE Bonding Film)

| Property | Value | Notes |
|----------|-------|-------|
| **Dk** | 2.10-2.35 | Matches TLY/TLX cores |
| **Df** | 0.0008 | Ultra-low loss |

**Applications**: All-PTFE multilayer stripline networks for satellite transponders, defense radar antenna panels requiring uniform PTFE dielectric

**Key Characteristics**: Ultra-low-loss PTFE bonding film for all-PTFE multilayer constructions. Requires careful lamination press-profile management.

### TF Series (Thermally Enhanced)

| Property | TF-260 | TF-290 | Notes |
|----------|--------|--------|-------|
| **Dk Range** | 2.60 | 2.90 | - |
| **Df** | 0.0015-0.0020 | - | Low loss |

**Applications**: GaN and GaAs power amplifier boards for 5G base stations, high-power RF transmitter modules, tower-mounted amplifiers (TMA)

**Key Characteristics**: Thermally optimized PTFE laminates with improved thermal conductivity for power amplifier applications where substrate heat spreading matters.

## RF-35A2 vs Rogers RO4350B Comparison

| Property | RF-35A2 | RO4350B | Advantage |
|----------|---------|---------|-----------|
| Dk @ 10 GHz | 3.50 ±0.05 | 3.48 ±0.05 | Essentially identical |
| Df @ 10 GHz | 0.0018 | 0.0037 | RF-35: 51% lower loss |
| Thermal Conductivity | 0.62 W/m·K | 0.62 W/m·K | Matched |
| CTE Z | 30 ppm/°C | 32 ppm/°C | RF-35: Slightly better |
| Processing | PTFE Plasma | FR-4 Chemistry | Different workflows |
| Cost | 10-15% lower | Benchmark | RF-35: More cost-effective |

**Critical Note**: RF-35 is PTFE-based while RO4350B is hydrocarbon thermoset. RF-35 requires dedicated PTFE plasma desmear equipment vs standard FR-4 chemistry for RO4350B.

## Processing Requirements

All PTFE-based Taconic materials (TLY, TLX, TLC, RF-35, CER, TF series) require:
- **Plasma desmear** for via reliability (industry standard for PTFE/ceramic PTFE)
- Specialized drill programs (different speeds/feeds than FR-4)
- Controlled lamination profiles (temperature/pressure)
- Etch parameters optimized for PTFE

## Source Reference

> "来自 APTPCB Taconic 材料已审核静态页面, 发布于 aptpcb.com"
> - Source: apt_taconic_materials_page
> - URL: file:///code/hileap/frontendAPT/public/static/materials/en/taconic-pcb.json
> - Authority: Tier-2 (internal_published_page)

## Usage Notes

These parameters enable:
- RF/microwave material selection for specific frequency bands
- Stack-up design with exact Dk/Df values
- Thermal management calculations
- CTE-matched designs for reliability
- Cost-performance optimization

## Design Recommendations

- **< 3 GHz**: RF-35 cost-effective with good performance
- **3-10 GHz**: TLX or RF-35 depending on loss budget
- **> 10 GHz**: TLY series for lowest loss
- **Miniaturized antennas**: CER-10 for compact designs
- **Hybrid designs**: fastRise 27 for Taconic/FR-4 bonding
- **All-PTFE multilayer**: TacLam bonding film

## Limitations

- PTFE requires plasma processing (not all PCB shops capable)
- Higher CTE Z than thermoset alternatives (affects PTH reliability)
- Premium pricing compared to FR-4
- Some series require longer lead times if not stocked
