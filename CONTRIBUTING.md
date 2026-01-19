# Contributing to DiamondOps-Core

## Principles
- Core is contract-first and conservative.
- Prefer additive change.
- Avoid breaking changes unless necessary and justified.

## Pull Requests
Include:
- What changed (schemas/docs/standards)
- Impact on downstream repos
- Version bump guidance (PATCH/MINOR/MAJOR)

## Schema rules
- Prefer adding optional fields over changing required sets.
- When tightening validation, consider existing producers’ stored records.
