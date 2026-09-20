# AGENTS.md

## Purpose

This repository is a **learning evidence and portfolio repository** for the Junior Technical Support / Linux Operations study plan.

## Source of truth

- **Notion** is canonical for schedule, daily sessions, progress, Quizlet QA status, and what is currently being studied.
- **GitHub** is canonical for public technical evidence produced by the study plan.
- Do not create a second independent roadmap in GitHub Issues.

## Working rules

1. Keep changes aligned with the current Notion module/day.
2. Prefer meaningful evidence over tool collection.
3. Use English for portfolio-facing artifacts, incident notes, runbooks, scripts and READMEs.
4. A completed practical topic should leave inspectable evidence.
5. Do not claim production experience that did not happen.
6. Do not invent incident results. Evidence must come from an actual lab or clearly marked simulation.
7. Keep failure injection isolated and reversible.
8. Do not intentionally disrupt real household/production-like services for practice.
9. Never commit secrets, tokens, credentials, private keys, personal data, sensitive logs, or private infrastructure details.
10. Do not add Kubernetes, Terraform, Ansible, Helm, GitOps, advanced cloud or unrelated platform tooling before the study plan reaches those topics after the first-job phase.

## Evidence format

Use this reasoning chain whenever possible:

**symptom → evidence → hypothesis → test → root cause → fix/escalate → verify → lesson**

## Repository mapping

- `weeks/` — scope and evidence checklist for each study week.
- `notes/` — concise learning notes that are worth keeping public.
- `runbooks/` — reusable troubleshooting procedures.
- `incidents/` — individual lab/simulated incident records.
- `postmortems/` — deeper reviews when an incident warrants one.
- `scripts/` — small Bash/Python operator utilities.
- `docker/` — Week 5 container lab artifacts.
- `monitoring/` — Prometheus/Grafana investigation evidence.
- `architecture/` — diagrams and request/service-flow explanations.

## Change granularity

Avoid issue/PR micro-management for daily learning evidence. Small evidence updates can be grouped into coherent commits. Structural changes should be documented clearly and remain consistent with the Notion plan.

<!-- BEGIN AGENT-WORK-CYCLE-V1-MANAGED -->
## Agent Work Cycle v1

Shared governance contract: `rozkalnsandris/ops-workflows/docs/AGENT_WORK_CYCLE_V1.md` with machine invariants in `policy/agent-work-cycle-v1.json`. Repository-local rules remain authoritative and may be stricter.

### GitHub-first tool and transport priority

- Use connected GitHub tooling by default for repository/source/file/branch/commit/PR/issue/CI/review work whenever it can complete the task with equivalent correctness and evidence. Do not use RDC, SSH, a local checkout, shell `git`, `gh`, or `curl` merely as a substitute for supported GitHub-native work.
- Use RDC/host shell only for the smallest step that genuinely requires host-local execution or observation and cannot be obtained through GitHub, such as local filesystem/process/runtime state, `sudo`/root, systemd, Docker, packages, networking, mounts, permissions/ownership, or another command that must execute on that host.
- For mixed work use GitHub -> minimal required host step -> GitHub. Return to GitHub for canonical source and durable repository evidence.
- RDC is execution/transport only; it is never source-of-truth or authorization authority and never widens owner authority, protected-data access, retry/rollback/cleanup, merge, repository-settings, secrets, or permissions scope.

### Work-cycle and owner gates

- START uses minimum-sufficient retrieval for one current lane; SYNC is incremental refresh; `turpini` resumes the same safe scope.
- Safe source/docs/tests work may proceed through Draft PR, CI/review and Ready where local rules permit.
- MERGE remains explicit unless a separately activated local FULL mode validly grants issue-scoped merge authority. Merge never implies LIVE.
- LIVE/deploy/runtime/credential/permission/production-data mutation requires the exact repository-local authorization that applies to that class/target.
- After the first authorized mutation begins, error, timeout, drift, ambiguity or authorization uncertainty is fail-closed: collect only necessary read-only evidence and STOP unless recovery was explicitly pre-authorized.
<!-- END AGENT-WORK-CYCLE-V1-MANAGED -->
