# The Taḥrīr / Taʾlīf / Taḥqīq Method

**تحرير · تأليف · تحقيق** — a source-first method for producing Islamic-studies work with AI assistance without surrendering fidelity, attribution, verification, or scholarly judgement.

> **Draft for feedback.** This kit is intended for careful review by a select circle of users. Disagreement, counter-examples, and genre-specific objections are welcome. See `FEEDBACK.md`.

## The idea in one line

Formulate the work precisely, compose or transform it from retrieved sources one verifiable unit at a time, and verify every unit before distilling it into the registers it needs — adding no unmarked source-claims and hiding no uncertainty.

## The three movements

- **Taḥrīr (تحرير)** — precise formulation, disciplined editing, and methodological control. The project is interrogated until its purpose, sources, scope, conventions, unit plan, and verification standard are clear enough to proceed.
- **Taʾlīf (تأليف)** — composition, arrangement, translation, explanation, or distillation from retrieved and identified sources. Work proceeds unit by unit, not in bulk.
- **Taḥqīq (تحقيق)** — verification, establishment, checking, and audit. Every unit is checked against its sources, terminology rules, claims ledger, and output constraints. Ideally, verification is performed by a different model or reviewer from the one that produced the draft.

The order is a discipline: **formulate, compose, verify** — while verification continues throughout and not merely at the end.

## What this kit is for

Use it for Islamic studies work involving:

- OCR correction and text clean-up;
- diplomatic or normalised transcription;
- translation;
- commentary and annotation;
- terminology control;
- takhrīj or citation checking;
- manuscript or edition comparison;
- study notes and teaching materials;
- sermon, lecture, or public-facing distillation from verified material;
- publication preparation;
- independent audit of existing work.

It is deliberately generic across Islamic studies. Each project supplies its own discipline, madhhab, corpus, language, edition, citation style, audience, and fidelity rules.

## What this kit refuses

The method refuses to proceed from vagueness to polish. It does not reward lazy instructions, thin answers, shoddy source handling, or requests for confident conclusions without verification.

It refuses:

- primary text generated from model memory;
- invented vocalisation;
- invented attribution;
- invented citations;
- silent emendation;
- paraphrase presented as translation;
- interpretation presented as source text;
- bulk generation before unit verification;
- register-specific outputs derived from raw OCR or unverified drafts;
- final claims without a source handle, verified basis, or explicit editorial note.

## Run the method

1. Copy `project-scaffold/` to a new project folder.
2. Prompt the user with `method-kit/00-one-line-brief.md`.
3. Run the Discovery Gate using `method-kit/01-discovery-gate.md`.
4. If the Discovery Gate passes, create the project foundation with `method-kit/03-tahrir-formulation.md`.
5. Put source files into `project-scaffold/corpus/` or the copied project’s `corpus/` folder.
6. Process one unit at a time with `method-kit/04-taleef-compilation.md`.
7. Verify the unit with `method-kit/05-tahqiq-verification.md`.
8. Run the deterministic harness where applicable:

```bash
python3 scripts/verify-unit.py units/0001-illustrative-example --corpus corpus
```

9. Distil only verified units into registers with `method-kit/06-register-distillation.md`.
10. Keep the folder current using `method-kit/07-handoff.md`.

## Folder overview

```text
method-philosophy.md     Principles and rationale.
FEEDBACK.md              Questions for reviewers.
method-kit/              Ordered prompts for running the method.
skills/                  Reusable role and guardrail instructions.
project-scaffold/        Copy this for each new project.
templates/               Reusable file templates.
examples/                Example one-line briefs and review prompts.
LICENSE.md               CC BY-NC-SA 4.0 licence notice.
```

## Requirements

- Python 3 for the optional verification harness.
- No Python dependencies.
- Two or more models or reviewers are recommended where possible, especially for separating Taʾlīf from Taḥqīq.

## Status

Version 2 draft. Circulate for critique before relying on it in high-stakes scholarly production.
