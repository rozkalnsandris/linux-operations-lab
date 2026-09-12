# Study Plan → GitHub Evidence Map

The private Notion workspace controls dates, daily tasks and completion status. This document mirrors only the portfolio-relevant scope so the public repository remains understandable on its own.

## Week 1 — Linux Fundamentals & CLI — 14–19 September

**Learn:** shell, filesystem, processes, packages, users/groups, permissions, systemd basics, CPU/RAM/disk basics.

**GitHub evidence:**
- `notes/w1d1-linux-shell.md` and other concise notes when useful.
- `runbooks/linux-baseline.md`.
- At least 2 mini incident records under `incidents/`.
- Week summary in `weeks/week-01-linux-fundamentals/README.md`.

## Week 2 — Linux Troubleshooting & System Administration — 21–26 September

**Learn:** services, journalctl, SSH, permissions failures, storage, memory/process pressure, systematic diagnosis and escalation.

**GitHub evidence:**
- `runbooks/linux-service-troubleshooting.md`.
- At least 3 incident records covering service failure, permission/storage and SSH/access.
- Week summary in `weeks/week-02-linux-troubleshooting/README.md`.

## Week 3 — Networking, DNS, HTTP/HTTPS & SSH — 28 September–3 October

**Learn:** IP/subnet/gateway, routing, DNS/DHCP, TCP/UDP, ports, HTTP, TLS, NAT/firewall basics and SSH flow.

**GitHub evidence:**
- `runbooks/network-troubleshooting.md`.
- Request-flow diagram under `architecture/`.
- At least 3 incidents: DNS, port/connectivity, HTTP/TLS.
- Week summary in `weeks/week-03-networking/README.md`.

## Week 4 — Application Support: API, SQL & Logs — 5–10 October

**Learn:** REST/HTTP, JSON, curl, headers/auth basics, application logs, read-only SQL, DB connectivity, request flow and basic code reading.

**GitHub evidence:**
- `runbooks/application-support.md`.
- 3 ticket/incident examples: API auth/input, HTTP 5xx, DB/data investigation.
- Safe sample queries/examples without real data.
- Week summary in `weeks/week-04-application-support/README.md`.

## Week 5 — Docker, Monitoring & Incidents — 12–17 October

**Learn:** images, containers, Compose, volumes, networks, ports, env vars, logs, healthchecks, resources, Prometheus/Grafana incident diagnosis.

**GitHub evidence:**
- Demo stack under `docker/`.
- `runbooks/container-troubleshooting.md`.
- Monitoring evidence under `monitoring/`.
- At least 3 Docker/monitoring incident records.
- Week summary in `weeks/week-05-docker-monitoring/README.md`.

## Week 6 — Bash/Python Automation + Support Operations — 19–24 October

**Learn:** small Bash/Python utilities, Git basics, ticket lifecycle, escalation quality and technical English.

**GitHub evidence:**
- At least 3 small utilities under `scripts/`.
- README for each utility or a clear consolidated scripts README.
- Example support/ticket evidence.
- Week summary in `weeks/week-06-automation-support-ops/README.md`.

## Week 7 — Candidate Mode — 26–31 October

**Practice:** blind incidents, mock interviews, English explanations, CV/GitHub polish and targeted application readiness.

**GitHub evidence:**
- At least 10 documented incidents total across the repository.
- 3–5 useful runbooks.
- 3 small operator scripts.
- Docker demo + monitoring evidence.
- `FINAL-ASSESSMENT.md` with strengths, remaining gaps and next steps.
- Week summary in `weeks/week-07-candidate-mode/README.md`.

## Deliberately out of scope before 1 November

Kubernetes/K3s, Terraform, Ansible, Helm, ArgoCD/Flux, advanced AWS/Azure, advanced Python, Platform Engineering, service mesh and unrelated infrastructure expansion.
