# Evidence Standard

Portfolio evidence should be technically useful, concise and honest.

## Minimum incident evidence

- Incident ID/title
- Reported symptom
- Impact
- Environment (sanitized)
- Timestamp/window when relevant
- Evidence collected
- Hypotheses considered
- Tests performed
- Root cause, if confirmed
- Resolution or escalation reason
- Verification
- Lesson / runbook improvement

## Good runbook characteristics

- Clear trigger: when to use it.
- Safe first checks.
- Commands with purpose, not command dumping.
- Expected interpretation of output.
- Stop/escalation conditions.
- Verification step.
- No secrets or private infrastructure assumptions.

## Good script characteristics

- Small and understandable.
- Clear input/output.
- Predictable exit codes.
- Safe failure behavior.
- README/example usage.
- No embedded credentials.

## Portfolio honesty

Use labels such as **lab**, **simulation**, or **home-lab observation** when appropriate. Never describe simulated evidence as production work.
