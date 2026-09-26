# FAST-LANE v2.3 adoption

This repository adopts the shared Agent Work Cycle v2.3 routing contract from `rozkalnsandris/ops-workflows` at canonical revision `274d58f2d9d3cb86feded2751b8f9009a4501f6b` for fleet rollout issue `#124`.

## Repository classification

- Deployment profile: `source-only`.
- START: minimum-sufficient bootstrap for one current lane with safe same-scope auto-continuation when unblocked.
- WRITE_PREFLIGHT_COMPACT: adopted through the existing `.github/github-api-access-v1.json` adapter.
- AUTO-RUN FULL normalized state: `NOT_APPLICABLE`; this repository has no local FULL controller/schema and this rollout does not create one.
- Queue vNext: not applicable and not activated.

## Local rules remain authoritative

`AGENTS.md` remains the repository-local normative source. In particular:

- Notion remains canonical for study schedule, daily sessions, progress and current learning scope.
- GitHub remains canonical for public technical evidence; this adoption does not create a second independent roadmap in Issues.
- Evidence must remain truthful and based on actual labs or clearly marked simulations.
- Practice must not intentionally disrupt real household or production-like services.
- Secrets, credentials, personal data, sensitive logs and private infrastructure details remain forbidden.
- The first-job study-plan scope remains authoritative; this rollout does not authorize unrelated platform tooling.

## Authority boundaries

This is governance/source routing only. It grants no merge, LIVE/runtime, credentials, permissions/settings, retry/rollback/cleanup, deploy, production-data or Queue vNext authority. Merge remains explicit owner authority, and merge never implies LIVE.

Mutable PR/CI/review/main state must always be read fresh from GitHub and is not stored in the bootstrap manifest.
