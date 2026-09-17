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

## HydraSafe commercial activation

Near-term customer acquisition is governed by parent revenue goal `REV-001` and HydraSafe task `HYDRA-COMMERCIAL-001`. The active prospect workflow lives in [`customer-acquisition/hydrasafe/`](customer-acquisition/hydrasafe/) and current coordination state is preserved in [`docs/DIAMONDOPS_CORE_MIRROR_HANDOFF.md`](docs/DIAMONDOPS_CORE_MIRROR_HANDOFF.md).

As of 2026-09-17, five leading U.S. Tier-A prospects have been re-verified against current public evidence and moved to `READY_FOR_OUTREACH`. Four prospect-specific Outlook drafts are prepared but unsent. No prospect is recorded as `CONTACTED`, and no problem confirmation, assessment acceptance, authorized-document-set discussion, paid-scope willingness, or decision-maker referral has yet been evidenced.
