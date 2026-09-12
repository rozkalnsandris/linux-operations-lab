# Linux Operations Lab

Hands-on learning portfolio for **Junior Technical Support / Linux Operations / Application Support / NOC / Cloud Support** roles.

This repository is the public evidence layer of a 7-week study plan running from **14 September to 31 October 2026**. The goal is not to collect tools or present myself as a DevOps expert. The goal is to demonstrate safe, systematic troubleshooting and clear technical communication.

## Operating model

**symptom → evidence → hypothesis → test → root cause → fix/escalate → verify → document**

Each completed topic should leave inspectable evidence: a runbook, incident note, script, diagram, Docker example, monitoring investigation, or postmortem.

## 7-week roadmap

| Week | Dates | Focus | Primary evidence |
| --- | --- | --- | --- |
| 1 | 14–19 Sep | Linux fundamentals & CLI | Linux baseline runbook + mini incidents |
| 2 | 21–26 Sep | Linux troubleshooting & administration | Service/SSH/storage troubleshooting runbook |
| 3 | 28 Sep–3 Oct | Networking, DNS, HTTP/HTTPS & SSH | Network runbook + request-flow diagram |
| 4 | 5–10 Oct | Application support: API, SQL & logs | Application-support runbook + ticket/escalation examples |
| 5 | 12–17 Oct | Docker, monitoring & incidents | Demo Compose service + container runbook + incidents |
| 6 | 19–24 Oct | Bash/Python automation + support operations | Small operator scripts + Git evidence |
| 7 | 26–31 Oct | Candidate mode | Final blind incidents + portfolio assessment |

See [docs/PLAN.md](docs/PLAN.md) for the exact mapping from the study plan to repository evidence.

## Repository structure

```text
linux-operations-lab/
├── README.md
├── AGENTS.md
├── docs/
├── weeks/
├── notes/
├── architecture/
├── docker/
├── scripts/
├── monitoring/
├── runbooks/
├── incidents/
└── postmortems/
```

## Evidence rule

A topic is not complete because the theory was read or a video was watched. Good evidence answers:

- What was the symptom?
- What evidence did I collect?
- What hypothesis did I test?
- What was the root cause?
- What did I change, or why did I escalate?
- How did I verify recovery?
- What did I learn?

## Safety

Labs must be isolated and reversible. Production-like home services are not intentionally broken for practice. Read-only observation of real systems is fine; failure injection belongs in disposable test services, containers, test users/directories, or dedicated lab configurations.

Never commit secrets, tokens, passwords, private keys, customer data, private hostnames, or sensitive logs.

## Target by 1 November 2026

Be able to handle a realistic junior support/operations incident with safe fundamentals, structured evidence, concise English communication, honest escalation, and a portfolio that proves the work rather than just listing technologies.
