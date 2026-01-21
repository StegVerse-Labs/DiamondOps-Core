# Canonical Documents (DiamondOps)

This document defines which documents in the DiamondOps ecosystem are canonical
(source of truth) and how downstream repositories must reference or synchronize them.

At this stage, DiamondOps-Core serves as both:
- the **domain contract authority** (schemas, compatibility, change policy), and
- the **platform posture authority** (positioning and liability boundaries).

These roles may be separated into distinct repositories in the future.
This document is written to remain valid across that transition.

---

## Canonical vs Repo-Local

- **Canonical** means the authoritative version lives in this repository and
  downstream repos must reference or sync it via StegDB automation.
- **Repo-local** means the document is specific to a repo and must not be
  automatically overwritten.

---

## Canonical Documents (Authoritative)

### Platform Posture & Liability
- `docs/POSITION.md`
- `docs/LIABILITY_BOUNDARY.md`

These define:
- scope of responsibility
- non-operational posture
- boundaries used for ToS, partner agreements, and underwriting

### Contract & Schema Governance
- `schemas/README.md`
- `docs/VERSIONING.md`
- `docs/COMPATIBILITY.md`
- `docs/SCHEMA_CHANGE_POLICY.md`

These define:
- schema meaning and intent
- versioning rules
- compatibility guarantees
- allowed vs breaking changes

---

## Explicitly Not Canonical Here

The following are intentionally **not** canonical:

- repo-specific READMEs
- CHANGELOGs
- product or workflow documentation unique to a repo
- demos, examples, and experiments

---

## How Canonical Sync Works

- **Source of truth:** `stegverse-labs/diamondops-core`
- **Router & publisher:** `stegverse-labs/stegdb`
- **Delivery:** PRs opened into downstream repos

StegDB uses templates so downstream repos may include minimal contextual framing
(e.g., repo name) without altering canonical meaning.

---

## Downstream Repo Requirements

Downstream repos must:

1. Keep canonical documents at expected paths.
2. Avoid editing canonical files locally.
3. Accept StegDB-generated PRs as the update mechanism.

Emergency fixes must be made in the canonical source first,
then propagated via StegDB.

---

## Notes on Future Separation

If DiamondOps platform posture is later moved to a dedicated `DiamondOps/` repo:

- `POSITION.md` and `LIABILITY_BOUNDARY.md` will move with it
- schema governance documents will remain in DiamondOps-Core
- StegDB manifests will be updated, not rewritten

No downstream repo behavior should need to change.
