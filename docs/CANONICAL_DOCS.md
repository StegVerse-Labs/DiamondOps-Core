# Canonical Documents (DiamondOps)

This document defines which files in the DiamondOps ecosystem are **canonical** (source of truth) and how other repos must **reference or synchronize** them.

DiamondOps is documentation-first. Canonical documents exist to make platform posture, liability boundaries, and contributor rules consistent across all repos.

## Canonical vs Repo-Local

- **Canonical** means: the authoritative version lives in **DiamondOps** and downstream repos must **sync** or **reference** it.
- **Repo-local** means: the document is specific to that repo and should not be automatically overwritten.

## Canonical Documents

The following files are canonical and must remain consistent across the ecosystem:

### Governance & Liability
- `docs/LIABILITY_BOUNDARY.md`
- `docs/POSITION.md`

### Security & Contribution Norms
- `SECURITY.md`
- `CONTRIBUTING.md`

## Optional Canonicals (Add Later)

These are candidates for canonization once they stabilize:

- `docs/TERMINOLOGY.md`
- `docs/SYSTEM_ARCHITECTURE.md`
- `docs/VISION.md`

If any of these become canonical, they must be added to the automation manifest in StegDB and rolled out via PRs.

## Repo-Local Documents (Not Canonical)

These are intentionally repo-specific:

- `README.md`
- `CHANGELOG.md`
- product-specific docs (e.g., retrofit procedures, inspection packets, runbooks unique to a repo)
- marketing or pitch documents (unless explicitly canonized)

## How Canonical Sync Works

Canonical documents are distributed by automation:

- **Source of truth:** `StegVerse/DiamondOps`
- **Publisher:** `StegVerse/StegDB`
- **Delivery:** PRs opened into each target repo

StegDB uses templates so each target repo can include minor repo-specific context (e.g., the repo name) while preserving canonical meaning.

## Requirements for Downstream Repos

Downstream repos must:

1. Keep canonical docs at the expected paths (e.g., `docs/LIABILITY_BOUNDARY.md`).
2. Avoid editing canonical docs directly in downstream repos.
3. Accept updates via StegDB-generated PRs.

If an emergency patch is required in a downstream repo, the canonical copy in DiamondOps must be updated immediately afterward, followed by a StegDB rollout PR.

## Notes

- Canonical documents must remain **documentation-only** and must not embed secrets or customer data.
- The liability boundary statement is the authoritative boundary used for ToS, partner agreements, and underwriting references.
