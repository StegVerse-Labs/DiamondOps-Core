# Canonical Documents (DiamondOps Platform)

This document defines which documents are canonical **within the DiamondOps
platform posture** and how downstream repos must reference them.

DiamondOps is documentation-first. These canonicals exist to keep platform
positioning, liability boundaries, and non-operational scope consistent across
all DiamondOps-related repositories.

This file does **not** define schema meaning or contract semantics.
Those live in **DiamondOps-Core**.

---

## What “Canonical” Means Here

A document is canonical if:

- the authoritative version lives in `StegVerse/DiamondOps`
- downstream repos must **reference or sync** it
- downstream repos must not redefine or contradict its meaning

Canonical documents may be:
- link-only references, or
- excerpts rendered via templates

Distribution is handled by **StegDB** via PRs.

---

## Platform Canonicals (Authoritative)

The following documents are canonical for DiamondOps platform posture:

### Governance & Liability
- `docs/LIABILITY_BOUNDARY.md`
- `docs/POSITION.md`

These statements are authoritative for:
- Terms of Service
- partner agreements
- insurance and underwriting references
- external descriptions of DiamondOps scope

---

## Explicitly Not Canonical Here

The following are **not** canonical in this repo:

- schema definitions
- schema versioning rules
- schema change or compatibility policies

Those live in:
- `StegVerse/DiamondOps-Core`

---

## Repo-Local Documents (Not Canonical)

These documents are intentionally repo-specific and must not be overwritten:

- `README.md`
- `CHANGELOG.md`
- repo-specific product documentation
- demos, examples, and experiments

---

## How Canonical Sync Works

- **Source of truth:** `StegVerse/DiamondOps`
- **Router & publisher:** `StegVerse/StegDB`
- **Delivery mechanism:** PRs opened into downstream repos

Templates are used so downstream repos may include minor contextual framing
(e.g., repo name) without altering canonical meaning.

---

## Rules for Downstream Repos

Downstream repos must:

1. Keep platform canonicals at the expected paths.
2. Avoid editing canonical files locally.
3. Accept StegDB-generated PRs as the update mechanism.

Emergency fixes must be made in the canonical source repo first,
then propagated via StegDB.

---

## Notes

- Canonical documents must remain documentation-only.
- Canonicals must not embed secrets, customer data, or operational telemetry.
- Platform canonicals define **scope and responsibility boundaries only**.
