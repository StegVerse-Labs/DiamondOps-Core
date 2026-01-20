# DiamondOps-Core Schemas

These schemas define the **contract layer** for the DiamondOps platform.
They exist so different systems (HydraSafe, ReactorOps, YieldOS, CrystalWorks, and StegBrain)
can exchange operational metadata predictably.

## What schemas are for
Schemas are used to:
- validate event payloads (consistency and completeness)
- enable ingestion and analytics (YieldOS)
- support audits and incident review (HydraSafe/Compliance)
- preserve an evidence trail without storing secrets

## What schemas are NOT for
Schemas are not:
- equipment control instructions
- a substitute for engineering judgment
- a place to store secrets, credentials, or sensitive facility telemetry by default

## Design principles
1. **Contract-first, conservative changes**
   - Prefer additive changes (new optional fields) over breaking changes.
2. **Metadata-first**
   - Store references (links/IDs) rather than embedding sensitive documents.
3. **Auditability**
   - Timestamps, IDs, categories, and summaries must support human review.
4. **Interoperability**
   - Schema names match event names (e.g., `incident_event.schema.json`).

## Naming conventions
- Schema files: `<event_title>.schema.json`
- Example event instances (recommended): `<event_title>.json`

## Versioning
DiamondOps-Core uses SemVer.
Downstream repos should pin the Core version they validate against.

## Quick map of common schemas
- `run_record` — run metadata (start/end, status, type, recipe reference)
- `incident_event` — safety incidents and corrective actions
- `interlock_event` — interlock trips/resets
- `permit_artifact` — compliance evidence references (metadata only)
- `maintenance_event` — maintenance work performed and parts used
- `downtime_event` — downtime windows and root-cause classification
- `asset_inspection_event` — inspection outcomes + risk rating
- `retrofit_event` — retrofit lifecycle + expected impact (proposal → completion)
- `lab_report` — lab report metadata + references
- `sensor_reading` — optional aggregated sensor readings (metadata only)

## Compatibility note
StegBrain and YieldOS validators treat these schemas as source of truth.
Changes here can impact automation behavior across repos.
