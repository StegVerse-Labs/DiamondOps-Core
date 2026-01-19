# DiamondOps-Core

DiamondOps-Core defines shared contracts for the DiamondOps platform: schemas, terminology, standards, and interface specs used by HydraSafe, ReactorOps, YieldOS, and CrystalWorks.

This repo is intentionally conservative:
- schemas are treated as contracts
- changes are versioned
- downstream repos should pin to a Core release

## Contents
- `schemas/` — canonical event + record schemas
- `standards/` — platform standards (safety levels, uptime, yield classes)
- `interfaces/` — integration/event contracts between components
- `docs/` — vision, architecture, and compliance boundaries

## Versioning
SemVer:
- PATCH: clarifications, non-breaking schema additions
- MINOR: additive schema changes with backwards compatibility
- MAJOR: breaking schema changes + migration notes

## Status
- v0.1.0: initial contract set
