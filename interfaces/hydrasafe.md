# HydraSafe Interface (v0.1)

HydraSafe emits:
- incident_event
- interlock_event
- sensor_reading (optional, aggregated)
- permit_artifact (document metadata only)

Optional export:
- sensor_reading (aggregated)

HydraSafe must not emit secrets. Only metadata + references.
