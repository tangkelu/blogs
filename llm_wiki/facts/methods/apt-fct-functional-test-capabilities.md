# Fact Card: APT FCT (Functional Circuit Test) Capabilities

## Fact Metadata

- **fact_id**: apt_fct_functional_test_capabilities
- **fact_type**: test_capabilities
- **source_id**: apt_pcba_functional_test_fct
- **authority_tier**: Tier-2
- **domain**: pcba_testing
- **application**: functional_verification
- **date_extracted**: 2026-05-02
- **verification_status**: verified

## FCT Overview

Functional Circuit Test is the final verification step ensuring assembled boards operate correctly under real-world conditions.

### Core Capabilities

| Parameter | Capability |
|-----------|------------|
| **Test Fixtures** | Custom tailored design |
| **Test Environment** | Real operating conditions |
| **Coverage** | Power to outputs complete verification |
| **Documentation** | Full test records |
| **NPI Turnaround** | 24-48 hours |

### Testing Scope

| Test Category | Specific Tests |
|---------------|----------------|
| **Power Verification** | Power-on, voltage levels, current draw, power sequencing |
| **Signal Integrity** | Clock signals, data lines, control signals, edge rates |
| **Communication** | UART, SPI, I2C, USB, Ethernet, CAN, wireless interfaces |
| **Load Testing** | Performance under rated load, thermal performance |
| **Firmware** | Loading, verification, version checking, checksum |
| **Analog Circuits** | Voltage references, ADC/DAC performance, sensor readings |
| **Digital Logic** | Logic states, timing verification, protocol compliance |
| **Sensors/Actuators** | Calibration, accuracy, response time |

### Test Development Process

1. **Test Plan Creation**: Define test requirements and coverage
2. **Fixture Design**: Custom mechanical/electrical interface
3. **Test Program Development**: Code and configuration
4. **Golden Sample Validation**: Baseline with known-good unit
5. **Production Deployment**: Full implementation

### Types of FCT

| FCT Type | Description | Application |
|----------|-------------|-------------|
| **Power-On Test** | Basic power-up and idle state | All products |
| **Parametric Test** | Measure voltage, current, frequency, timing | Precision analog |
| **Communication Test** | Verify data links and protocols | Networked devices |
| **Functional Simulation** | Simulate real operating scenarios | Complex systems |
| **Boundary Test** | Test at operating limits | Ruggedized products |
| **Environmental** | Temperature, humidity during test | Harsh environment |

### Quality Integration

| Integration Point | Description |
|-------------------|-------------|
| **Inspection Chain** | AOI + X-Ray + ICT → FCT |
| **Process Control** | SPI feedback loop data integration |
| **Defect Tracking** | PPM monitoring with failure analysis |
| **Traceability** | Barcode + lot linking to test records |
| **Standards** | IPC-A-610 Class 2/3 compliance |

### FCT vs ICT Comparison

| Aspect | FCT | ICT |
|--------|-----|-----|
| **Test Level** | System/Functional | Component/Electrical |
| **Power State** | Powered, operating | Unpowered or limited power |
| **Coverage** | End-to-end functionality | Component values and connections |
| **Fixtures** | Complex, application-specific | Standard bed-of-nails |
| **Cost** | Higher | Lower |
| **Value** | Validates real operation | Validates correct assembly |

### When to Use FCT

**Required For**:
- Complex digital systems with firmware
- Products with communication interfaces
- Analog precision circuits
- Safety-critical applications
- High-reliability requirements

**Recommended When**:
- ICT coverage is insufficient (<80%)
- Functional behavior is complex
- Customer requires operational verification
- Field failure costs are high

### Test Documentation

| Document Type | Content |
|---------------|---------|
| **Test Report** | Pass/fail, measurements, limits |
| **Failure Analysis** | Failed tests, diagnostic data |
| **Trace Record** | Serial number, date, operator |
| **Statistics** | Yield, trends, Cpk |

---

## Source Reference

> "来自 APTPCB 已审核静态页面, 发布于 aptpcb.com"
> - Source: apt_pcba_functional_test_fct
> - URL: file:///code/hileap/frontendAPT/public/static/pcba/en/fct-test.json
> - Authority: Tier-2 (internal_published_page)

## Usage Notes

FCT validates that the PCBA performs its intended function, not just that it passes electrical tests. Essential for:
- Firmware-based products
- Communication devices
- Complex systems
- High-reliability applications

## Design for Test (DFT) for FCT

1. **Test Points**: Access to critical signals
2. **Firmware Hooks**: Test mode support
3. **Self-Test Capabilities**: Built-in diagnostics
4. **Interface Access**: Debug ports, programming headers
5. **Load Simulation**: Test under realistic conditions
