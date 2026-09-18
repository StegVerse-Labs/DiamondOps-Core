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

The canonical HydraSafe commercial task `HYDRA-COMMERCIAL-001` is now indexed by `task.v1` COSV `20010000110000` in the HydraSafe task registry; task ownership and the `REV-001` revenue lineage are unchanged.

The HydraSafe commercial lane has explicit Gmail send authorization from `rigel@stegverse.org`, but the currently connected Gmail provider identity does not match that sender; no outreach was sent and no prospect stage advanced. The existing `HYDRA-COMMERCIAL-001` task and `REV-001` lineage remain unchanged.

Four authorized Outlook outreach messages are now provider-observed from `rigel@stegverse.org`: Great Lakes Crystal Technologies, Seki Diamond Systems, Carat Systems, and Element Six are `CONTACTED`; Plasmability remains `READY_FOR_OUTREACH`. No inbound reply or commercial-validation predicate is yet observed.


### HydraSafe response observation — 2026-09-18

`HYDRA-COMMERCIAL-001` remains the canonical HydraSafe commercial task. A materially later Outlook recheck found no authentic prospect reply and no delivery-failure notice for the four contacted Tier-A records. No commercial-validation predicate advanced; see `customer-acquisition/hydrasafe/` and the HydraSafe canonical handoff for the current evidence state.
