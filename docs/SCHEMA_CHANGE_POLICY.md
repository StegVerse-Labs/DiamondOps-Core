# Schema Change Policy (DiamondOps-Core)

DiamondOps-Core schemas are contract definitions used across multiple repos.
Changes must preserve auditability and downstream stability.

## Allowed changes (preferred)

- New optional fields
- New schema files (new event types)
- Clarifications that do not change validation behavior

## Restricted changes (breaking)

- Changing required fields
- Changing field meaning/semantics
- Removing fields or schemas

Breaking changes require:
- MAJOR version bump
- migration notes
- deprecation window guidance

## Evidence integrity

Schemas must not require secrets or embed sensitive facility telemetry by default.
Prefer references (IDs/links) over embedded documents.
