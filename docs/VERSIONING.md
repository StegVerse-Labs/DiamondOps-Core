# Versioning (DiamondOps-Core)

DiamondOps-Core uses Semantic Versioning (SemVer): MAJOR.MINOR.PATCH.

## What a change means

- PATCH: fixes wording, examples, typos, or clarifies intent without changing validation
- MINOR: additive schema changes (new optional fields, new schema files)
- MAJOR: breaking changes (required fields changed, semantics changed, removals)

## Rules

- Prefer additive evolution (MINOR) over breaking changes.
- Breaking changes require:
  - explicit migration notes
  - a deprecation window
  - downstream repo pin guidance
