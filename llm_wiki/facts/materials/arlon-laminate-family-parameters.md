# Fact Card: Arlon Laminate Family Parameters

## Fact Metadata

- **fact_id**: arlon_laminate_family_parameters
- **fact_type**: material_parameters
- **source_id**: apt_arlon_materials_page
- **authority_tier**: Tier-2
- **domain**: high_temperature_rf_materials
- **application**: aerospace_military_rf_pcb
- **date_extracted**: 2026-05-02
- **verification_status**: verified

## Product Series Overview

### 33N / 35N / 85N Series (Polyimide)

**Industry benchmark for extreme temperature survival**

| Property | 33N | 45N (comparison) | Notes |
|----------|-----|------------------|-------|
| **Dk @ 1 MHz** | 4.20 | 4.30 | Standard polyimide range |
| **Df @ 1 MHz** | 0.015 | 0.015 | Moderate loss at low freq |
| **Thermal Conductivity** | 0.20 W/m·K | 0.25 W/m·K | Lower than PTFE |
| **CTE X/Y** | 14 ppm/°C | 14 ppm/°C | Good stability |
| **CTE Z** | 45 ppm/°C | 45 ppm/°C | Moderate Z-axis expansion |
| **Moisture Absorption** | 1.20% | 0.15% | **Critical: 33N highly hygroscopic** |
| **Peel Strength** | 8.0 lb/in | 9.0 lb/in | Good adhesion |
| **Tg** | >250°C | 175°C | Exceptional thermal stability |
| **Dielectric Strength** | 1200 V/mil | 1200 V/mil | Excellent |
| **Flammability** | V-0 | V-0 | UL 94 |
| **Plasma Required** | No | No | Standard FR-4 desmear |

**Stocked at APTPCB**: 33N in 10-60 mil, 1/2 oz and 1 oz ED copper

**Primary Applications**: Commercial/military avionics, downhole drilling (MWD/LWD) boards, extreme-temp burn-in boards, engine control modules

**Key Characteristics**: Polyimide resins offer exceptional thermal stability with Tg >250°C and very low Z-axis expansion. Unlike PTFE, processes with standard FR-4 desmear chemistry. **Highly hygroscopic - strict baking required before lamination and reflow.**

**Operating Range**: -55°C to +260°C continuous operation

### 45N / 47N / 49N Series (High-Reliability Epoxy)

| Property | 45N | Notes |
|----------|-----|-------|
| **Dk @ 1 MHz** | 4.30 | |
| **Df @ 1 MHz** | 0.015 | |
| **Thermal Conductivity** | 0.25 W/m·K | |
| **CTE X/Y** | 14 ppm/°C | |
| **CTE Z** | 45 ppm/°C | |
| **Moisture Absorption** | 0.15% | Much lower than 33N |
| **Peel Strength** | 9.0 lb/in | Excellent |
| **Tg** | 175°C | High for epoxy |
| **Dielectric Strength** | 1200 V/mil | |
| **Flammability** | V-0 | |
| **Plasma Required** | No | Standard processing |

**Stocked at APTPCB**: 45N in 5-31 mil

**Primary Applications**: High-layer-count digital backplanes, military and commercial aerospace communications, demanding industrial controls

**Key Characteristics**: High-reliability, high-Tg (175-200°C) epoxy systems bridging the gap between standard FR-4 and pure polyimide. Excellent CAF resistance and lead-free assembly compatible. Entirely standard PCB manufacturing workflows.

### Thermount Series (55NT / 85NT)

| Property | 55NT | Notes |
|----------|------|-------|
| **Dk @ 1 MHz** | 3.50 | Lower than glass-reinforced |
| **Df @ 1 MHz** | 0.017 | |
| **Thermal Conductivity** | 0.15 W/m·K | Lowest in family |
| **CTE X/Y** | 7/9 ppm/°C | **Excellent low CTE** |
| **CTE Z** | 40 ppm/°C | |
| **Moisture Absorption** | 1.00% | High - requires baking |
| **Peel Strength** | 6.0 lb/in | Good for aramid |
| **Tg** | 260°C | High thermal stability |
| **Dielectric Strength** | 1000 V/mil | |
| **Flammability** | V-0 | |
| **Plasma Required** | No | Standard processing |

**Primary Applications**: Surface mount military boards with ceramic LCC packages, space-constrained avionics where weight is critical, dense multilayer designs

**Key Characteristics**: Uses non-woven aramid reinforcement instead of traditional glass fiber. Provides very low in-plane CTE and significantly lighter than standard polyimide. Eliminates glass-weave skew for high-speed signals. **Requires specialized routing and drilling to prevent aramid fiber tear.**

### CLTE-XT / CLTE-AT (Microwave PTFE)

| Property | CLTE-XT | TC350 (comparison) | AD250 (comparison) |
|----------|---------|--------------------|--------------------|
| **Dk @ 10 GHz** | 2.94 | 3.50 | 2.50 |
| **Df @ 10 GHz** | 0.0012 | 0.0020 | 0.0014 |
| **Thermal Conductivity** | 0.45 W/m·K | **1.00 W/m·K** | 0.22 W/m·K |
| **CTE X/Y** | 8 ppm/°C | 8 ppm/°C | 24 ppm/°C |
| **CTE Z** | 20 ppm/°C | **10 ppm/°C** | 190 ppm/°C |
| **Moisture Absorption** | 0.02% | 0.02% | 0.02% |
| **Peel Strength** | 8.0 lb/in | 8.0 lb/in | 12.0 lb/in |
| **Tg** | N/A (PTFE) | N/A (PTFE) | N/A (PTFE) |
| **Dielectric Strength** | 600 V/mil | 600 V/mil | 800 V/mil |
| **Flammability** | V-0 | V-0 | V-0 |
| **Plasma Required** | Yes | Yes | Yes |

**Stocked at APTPCB**: CLTE-XT in 10-60 mil

**CLTE-XT Primary Applications**: Phased-array radar antennas, low-PIM cellular base station feeds, collision avoidance radar, space communications

**CLTE-XT Key Characteristics**: Commercial microwave laminate with extremely low loss and Z-axis CTE perfectly matched to copper (20 ppm/°C) for superior plated through-hole reliability in multilayer RF boards. Phase stable over temperature.

**TC350 Primary Applications**: High-power amplifiers (PA), tower-mounted amplifiers (TMA), GaN and GaAs device mounting, broadcast transmitters

**TC350 Key Characteristics**: Thermally enhanced microwave laminate offering exceptional thermal conductivity (1.0 W/m·K) to pull heat away from active RF components. Maintains stable Dk and low loss. **Lowest CTE Z (10 ppm/°C) in family for excellent PTH reliability.**

**AD Series Primary Applications**: GPS/GNSS patch antennas, dielectric resonator antennas (DRA), miniaturized filters, broadband base station antennas

**AD Series Key Characteristics**: Antenna-grade PTFE composites offering wide range of dielectric constants. AD1000 (Dk 10.2) allows extreme miniaturization of patch antennas and filters.

### CuClad / DiClad / IsoClad (Legacy PTFE)

| Property | Value | Notes |
|----------|-------|-------|
| **Dk Range** | 2.17-2.60 | Ultra-low Dk options |
| **Df** | 0.0009 | **Absolute lowest loss** |

**Primary Applications**: Legacy military radar systems, EW receivers, specialized low-loss stripline networks, VNA test fixtures

**Key Characteristics**: Legacy PTFE materials critical for mature military and aerospace programs. CuClad 217/DiClad 880 provide absolute lowest dielectric loss in Arlon portfolio.

### 37N / 38N / HF-50 (Bondply Systems)

| Property | Value | Notes |
|----------|-------|-------|
| **Type** | Low-flow polyimide prepregs | 37N |
| **Type** | Microwave bondplys | HF-50 |

**Primary Applications**: Hybrid PTFE/FR-4 lamination, rigid-flex interfaces, metal-backed power amplifier boards

**Key Characteristics**: Low-flow polyimide prepregs (37N) and specialized microwave bondplys (HF-50) essential for hybrid stack-ups, rigid-flex bonding, and attaching metal cores to RF sub-assemblies.

## Processing Summary by Chemistry

| Chemistry | Desmear | Baking | Special Handling |
|-----------|---------|--------|------------------|
| **Polyimide (33N, 35N)** | Standard FR-4 | **Mandatory pre-bake** | Moisture sensitive (1.2%) |
| **Epoxy (45N, 47N)** | Standard FR-4 | Standard | Standard workflows |
| **Aramid (Thermount)** | Standard | Pre-bake | Special routing/drilling |
| **PTFE (CLTE, TC, AD)** | **Plasma required** | Standard | Plasma etch workflows |

## Material Selection Guide

### For Extreme Temperature (-55°C to +260°C)
- **33N/35N Polyimide**: Industry standard, highest Tg
- **Thermount 85NT**: When weight and CTE also matter

### For High-Reliability Digital
- **45N/47N Epoxy**: CAF resistant, lead-free compatible, cost-effective vs polyimide

### For Low-Loss RF (< 0.002 Df)
- **CLTE-XT**: Best choice for phase stability and PTH reliability
- **TC350**: When thermal management also critical
- **AD250**: For antenna applications

### For Hybrid Designs
- **37N Bondply**: Polyimide-based bonding
- **HF-50**: Microwave-optimized bondply

## Critical Design Notes

1. **33N Polyimide Moisture**: 1.20% absorption rate - strict pre-bake mandatory before lamination and assembly
2. **CLTE-XT PTH Reliability**: Z-axis CTE (20 ppm/°C) closely matches copper - superior for multilayer RF
3. **TC350 Thermal**: 1.0 W/m·K thermal conductivity - excellent for GaN/GaAs power devices
4. **Thermount Handling**: Aramid fiber requires specialized routing to prevent tear-out

## Source Reference

> "来自 APTPCB Arlon 材料已审核静态页面, 发布于 aptpcb.com"
> - Source: apt_arlon_materials_page
> - URL: file:///code/hileap/frontendAPT/public/static/materials/en/arlon-pcb.json
> - Authority: Tier-2 (internal_published_page)

## Usage Notes

These parameters enable:
- Aerospace/military material selection (-55°C to +260°C)
- RF/microwave material selection for low loss
- Thermal management calculations
- CTE-matched designs for ceramic component compatibility
- Hybrid stack-up design with bondply selection

## Key Differentiators vs Competitors

- **Arlon 33N vs Rogers 3000**: Similar thermal performance, different processing
- **CLTE-XT vs Taconic RF-35**: CLTE-XT has better Z-axis CTE matching to copper (20 vs 30 ppm/°C)
- **TC350 vs TF-260**: TC350 has significantly higher thermal conductivity (1.0 vs ~0.3 W/m·K)

## Limitations

- Polyimide moisture sensitivity requires strict process control
- PTFE materials require plasma processing capability
- Thermount requires specialized drilling parameters
- Premium pricing vs standard FR-4
