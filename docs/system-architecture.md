# System Architecture (v0.1)

## Components
- HydraSafe: hazard infrastructure + compliance artifacts + safety events
- ReactorOps: retrofit/refurb operations + maintenance events
- YieldOS: run tracking + analytics + dashboards (no closed-loop control in v0.1)
- CrystalWorks: R&D programs + controlled experiment metadata

## Data Flow (conceptual)
HydraSafe + ReactorOps emit events -> YieldOS ingests -> dashboards + reports.
CrystalWorks uses the same schema set in "research mode".

## Boundary
DiamondOps documentation focuses on lawful, safety-first operations and analytics.
It does not provide guidance to bypass safety systems or perform hazardous construction without qualified professionals.
