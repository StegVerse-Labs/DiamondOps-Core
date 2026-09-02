#!/usr/bin/env python3
"""Validate the DiamondOps near-term revenue control plane using stdlib only."""
from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLAIMS = ROOT / "tasks" / "revenue-claims.json"
INVENTORY = ROOT / "docs" / "revenue" / "SESSION_EXECUTION_INVENTORY.md"
HANDOFF = ROOT / "docs" / "DIAMONDOPS_CORE_MIRROR_HANDOFF.md"
TRACKER = ROOT / "docs" / "revenue" / "REGISTRATION_AND_FUNDING_TRACKER.md"
FILING_ROOT = ROOT / "docs" / "Filing Docs"
ENTITY_FOLDERS = [
    "StegVerse-LLC",
    "StegVerse-Governance-LLC",
    "StegVerse-AI-LLC",
    "StegVerse-Infra-LLC",
    "Heavy-to-Healthy-LLC",
    "HydraSafe-LLC",
    "StegVerse-Holdings-LLC",
]
ENTITY_REQUIRED = [
    "00-Entity-Profile.md",
    "01-Texas-Formation/01-Form-205-Completion.md",
    "01-Texas-Formation/02-Form-05-904-Completion.md",
    "01-Texas-Formation/03-SOSUpload-Packet-Manifest.md",
    "02-Post-Formation-Governance/01-Operating-Agreement-Draft.md",
    "02-Post-Formation-Governance/02-Initial-Written-Consent.md",
    "03-EIN/01-SS-4-Completion-Worksheet.md",
    "04-Government-Procurement/01-SAM-Entity-Registration-Worksheet.md",
    "04-Government-Procurement/02-Texas-CMBL-Registration-Worksheet.md",
    "04-Government-Procurement/03-Texas-VetHUB-Readiness.md",
    "04-Government-Procurement/04-SBA-VetCert-Worksheet.md",
    "04-Government-Procurement/05-Capability-Statement-Draft.md",
    "04-Government-Procurement/06-Procurement-Submission-Checklist.md",
    "05-Receipts-and-Renewals/RECEIPT_REGISTER.md",
]

REQUIRED = [
    CLAIMS, INVENTORY, HANDOFF, TRACKER,
    FILING_ROOT / "README.md",
    FILING_ROOT / "00-Filing-Process" / "README.md",
    FILING_ROOT / "90-Government-Procurement-Common" / "README.md",
    FILING_ROOT / "90-Government-Procurement-Common" / "SOLICITATION_RESPONSE_MANIFEST.md",
]
ALLOWED = {"UNCLAIMED", "CLAIMED_FOR_IMPLEMENTATION", "CLAIMED_FOR_VALIDATION", "CLAIMED_FOR_INTEGRATION", "MACHINE_OWNED", "BLOCKED", "COMPLETE", "SUPERSEDED", "MERGED_INTO_CANONICAL_WORKSTREAM"}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_time(value: str) -> datetime:
    try:
        return datetime.fromisoformat(value)
    except ValueError as exc:
        fail(f"invalid ISO timestamp {value!r}: {exc}")


def main() -> None:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED if not path.is_file()]
    if missing:
        fail(f"missing required control-plane files: {', '.join(missing)}")

    filing_missing = []
    for entity in ENTITY_FOLDERS:
        for rel in ENTITY_REQUIRED:
            path = FILING_ROOT / entity / rel
            if not path.is_file():
                filing_missing.append(str(path.relative_to(ROOT)))
    if filing_missing:
        fail("missing filing workspace files: " + ", ".join(filing_missing))

    data = json.loads(CLAIMS.read_text(encoding="utf-8"))
    claims = data.get("claims")
    if not isinstance(claims, list) or not claims:
        fail("claims must be a non-empty list")

    seen: set[str] = set()
    for claim in claims:
        task_id = claim.get("task_id")
        if not task_id or task_id in seen:
            fail(f"missing or duplicate task_id: {task_id!r}")
        seen.add(task_id)
        state = claim.get("state")
        if state not in ALLOWED:
            fail(f"{task_id}: invalid state {state!r}")
        for field in ("originating_goal", "repository", "branch", "lane", "role", "claimed_at", "release_condition", "expected_evidence", "next_task_after_release"):
            if not claim.get(field):
                fail(f"{task_id}: missing {field}")
        parse_time(claim["claimed_at"])
        if state in {"CLAIMED_FOR_IMPLEMENTATION", "CLAIMED_FOR_VALIDATION", "CLAIMED_FOR_INTEGRATION", "MACHINE_OWNED", "BLOCKED"}:
            expires = claim.get("expires_at")
            if not expires:
                fail(f"{task_id}: active or blocked claim lacks expires_at")
            parse_time(expires)
        if not isinstance(claim.get("surfaces"), list) or not claim["surfaces"]:
            fail(f"{task_id}: surfaces must be a non-empty list")

    inventory = INVENTORY.read_text(encoding="utf-8")
    for task_id in seen:
        if task_id not in inventory:
            fail(f"{task_id}: absent from session execution inventory")

    handoff = HANDOFF.read_text(encoding="utf-8")
    for required_text in ("SESSION_EXECUTION_INVENTORY.md", "revenue-claims.json", "Canonical continuation"):
        if required_text not in handoff:
            fail(f"handoff missing required reference: {required_text}")

    filing_count = len(ENTITY_FOLDERS) * len(ENTITY_REQUIRED)
    print(f"PASS: validated {len(claims)} claims, {len(REQUIRED)} control-plane files, and {filing_count} entity filing documents")


if __name__ == "__main__":
    main()
