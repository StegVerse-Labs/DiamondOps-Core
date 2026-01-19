# Changelog — DiamondOps-Core

All notable changes to DiamondOps-Core are documented here.

DiamondOps-Core defines the **contract layer** for the DiamondOps platform.
Changes are conservative, versioned, and compatibility-aware.

---

## [0.3.0] — Infrastructure-Complete Core
### Added
- `asset_inspection_event` schema  
  Used by ReactorOps for inspections, audits, and prepurchase evaluations.
- `retrofit_event` schema  
  Tracks retrofit lifecycle (proposal → completion) with expected impact metadata.
- `sensor_reading` schema (optional)  
  Aggregated, metadata-only sensor readings for safety and trend analysis.
- Clarified HydraSafe and ReactorOps interface exports to reference finalized schemas.

### Changed
- Interfaces updated to remove “future schema” language.
- Core now fully supports:
  - safety events
  - maintenance events
  - inspections
  - retrofits
  - yield and downtime analytics

### Impact
- No breaking changes.
- Downstream repos should pin **Core v0.3.x** to access complete operational contracts.

---

## [0.2.0] — Governance & Wiring
### Added
- `RELEASE.md` defining versioning and compatibility rules.
- `CONTRIBUTING.md` with contract-first contribution standards.
- `SECURITY.md` clarifying public-safe posture.
- Issue templates for contract change requests and bug reports.
- Pull request template for compatibility review.

### Impact
- No schema changes.
- Governance only.

---

## [0.1.0] — Initial Core Contracts
### Added
- Baseline schemas:
  - `run_record`
  - `incident_event`
  - `maintenance_event`
  - `downtime_event`
  - `interlock_event`
  - `permit_artifact`
  - `lab_report`
- Platform standards:
  - safety levels
  - uptime definitions
  - yield classification
- Initial interface contracts for HydraSafe, ReactorOps, and YieldOS.
- Vision, architecture, and compliance boundary documentation.

---

## Versioning Notes
- PATCH: clarifications, doc fixes, validation tightening
- MINOR: additive schemas or optional fields
- MAJOR: breaking schema changes (requires migration notes)

Downstream repos are expected to pin to a compatible Core version.
