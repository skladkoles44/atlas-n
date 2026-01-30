# How to add information (ATLAS N)

This repo is primarily a knowledge base. New information must land in the correct "topic path" and be discoverable from the topic index.

## Where to put what

1) Notes (observations / test reports / invariants / design decisions)
- Path: topics/atlas-n/notes/
- Filename: NICK-YYYY-MM-DD.md
- Status: tested / sketch / hypothesis
- Never include secrets: IP, domains, keys, configs, personal data.

2) Canon / contracts (rules that must be enforced)
- Path: rules/canonical/
- Update only when the rule itself changes. Keep it minimal and executable where possible.

3) Papers (long-form narrative / formal writeups)
- Path: papers/atlas-n/
- Use when it’s a cohesive document, not a note.

## Index rule (mandatory)

Any new note must be linked from:
- topics/atlas-n/index.md

Reason: discovery. If it's not linked, it doesn't exist.

## Minimal note template

Status: tested / sketch / hypothesis
Confidence: low / medium / high
Date: YYYY-MM-DD
Author: NICK

Text:
- What changed / what was observed
- Invariant(s)
- Evidence (aggregated only, no secrets)
