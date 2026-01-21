# Compatibility (DiamondOps-Core)

Downstream repos (HydraSafe, ReactorOps, YieldOS, StegBrain) should pin the
DiamondOps-Core version they validate against.

## Compatibility intent

- MINOR and PATCH releases are intended to be backward compatible.
- MAJOR releases may include breaking changes and require downstream updates.

## Recommended pinning

Downstream validation should pin a compatible range, for example:
- `^0.3.0` (compatible MINOR/PATCH) or
- exact pin for regulated environments.

## Schema drift

If a downstream repo emits payloads that fail validation due to schema drift:
- treat this as documentation drift, not operational failure
- remediation is via PR, not runtime enforcement
