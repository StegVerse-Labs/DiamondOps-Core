# Release Process (DiamondOps-Core)

## Versioning
DiamondOps-Core uses SemVer.

- PATCH: clarifications, doc fixes, schema tightening that does not break validators
- MINOR: additive schema changes (new optional fields, new schemas)
- MAJOR: breaking changes (removed/renamed fields, required changes)

## Compatibility Contract
Downstream repos (HydraSafe, ReactorOps, YieldOS, CrystalWorks) should pin a Core version:
- In their `RELEASE.md` under “Core Compatibility”
- In their release notes

## How to cut a release
1. Update `CHANGELOG.md`
2. Ensure schemas remain valid JSON Schema draft 2020-12
3. Create a GitHub Release tag: `vX.Y.Z`
4. In release notes, include:
   - Breaking changes (if any)
   - Migration guidance (if any)

## Migration notes
If MAJOR:
- add `docs/migrations/vX.md`
