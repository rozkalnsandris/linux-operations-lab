#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / ".github/github-api-access-v1.json").read_text())
startup = json.loads((ROOT / ".github/start-github-only.json").read_text())

assert manifest["shared_contract"]["repository"] == "rozkalnsandris/ops-workflows"
assert manifest["shared_contract"]["revision"] == "3bb0740b5f0a8ce631d2ff79f1acc4999ff6ed2c"
assert startup["github_api_access_contract"] == ".github/github-api-access-v1.json"
assert startup["default_mode"] == "FAST-LANE v2.3"

reads = manifest["read_policy"]
assert reads["authenticated_preferred"] is True
assert reads["serial_requests"] is True
assert reads["minimum_sufficient"] is True
assert reads["changed_files_on_demand"] is True
assert reads["tight_polling_forbidden"] is True
assert set(reads["dispositions"]) == {
    "PRIMARY_RATE_LIMIT_EXHAUSTED",
    "SECONDARY_RATE_LIMIT_SUSPECTED",
    "RETRY_AFTER_REQUIRED",
    "RESET_WAIT_REQUIRED",
    "READ_BACKOFF_REQUIRED",
    "TRANSPORT_RATE_LIMIT_METADATA_UNAVAILABLE",
}

mut = manifest["mutation_policy"]
assert mut["serial_requests"] is True
assert mut["no_duplicate_after_ambiguous_outcome"] is True
assert mut["read_only_reconciliation_after_ambiguity"] is True
assert mut["stop_after_ambiguity"] is True
assert set(mut["dispositions"]) == {
    "MUTATION_CONFIRMED_SUCCESS",
    "MUTATION_CONFIRMED_REJECTED_BEFORE_APPLY",
    "MUTATION_OUTCOME_UNKNOWN_RATE_LIMIT",
    "MUTATION_OUTCOME_UNKNOWN_TIMEOUT",
    "MUTATION_OUTCOME_UNKNOWN_TRANSPORT",
    "POST_MUTATION_RECONCILIATION_REQUIRED",
}

# Synthetic ambiguous outcomes must never authorize a retry mutation.
fixtures = {
    429: "MUTATION_OUTCOME_UNKNOWN_RATE_LIMIT",
    "timeout": "MUTATION_OUTCOME_UNKNOWN_TIMEOUT",
    "transport": "MUTATION_OUTCOME_UNKNOWN_TRANSPORT",
}
for _, disposition in fixtures.items():
    assert disposition in mut["dispositions"]
    assert "RETRY_MUTATION" not in mut["dispositions"]

assert startup["authority"]["merge_requires_explicit_owner_authorization"] is True
assert startup["authority"]["merge_never_implies_live"] is True
assert startup["authority"]["live_runtime_requires_separate_authorization"] is True
assert manifest["authority"]["merge_unchanged"] is True
assert manifest["authority"]["live_runtime_unchanged"] is True
assert manifest["authority"]["secrets_permissions_settings_unchanged"] is True

print("github-api-access contract: PASS")
