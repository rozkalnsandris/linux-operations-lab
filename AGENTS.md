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
