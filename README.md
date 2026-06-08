# The Taḥrīr / Taʾlīf / Taḥqīq Method

**تحرير · تأليف · تحقيق** — a method (not a tool) for producing Islamic-studies
work with AI assistance without surrendering fidelity, attribution, or scholarly
judgement. A **Builder** service role handles code (scraping, cleaning, parsing,
tooling) under the same fidelity discipline.

> **Draft, circulated for feedback.** See `method-philosophy.md` and `FEEDBACK.md`.

## The idea in one line

Formulate the work precisely; let the Builder acquire and prepare the corpus with
recorded, reversible tooling; compose from retrieved sources one verifiable unit
at a time; verify every unit (ideally a different model, deterministic check as
floor); then distil into the forms it needs, adding nothing.

## The movements (and the Builder)

- **Taḥrīr** — precise formulation; the Discovery Gate, then the ledger + sprint plan.
- **Builder** — the engineering hand: scrapers, cleaners, segmenters, the harness,
  register exporters, packs. Serves the movements; authors no scholarship.
- **Taʾlīf** — composition from verbatim corpus spans, a handle on every span.
- **Taḥqīq** — independent verification; the harness proves spans are in source.

## What's in here

```
method-philosophy.md     The principles. Read first.
FEEDBACK.md              How to critique the method.
method-kit/              Operator prompts, in order:
  00-one-line-brief.md      state the project in a single line
  01-discovery-gate.md      the munāqasha + refuse-to-proceed gate
  02-core-instructions.md   standing rules + role selection
  03-tahrir-formulation.md  write the foundation + sprint plan
  04-builder-execution.md   write/run code to prepare corpus + machinery
  05-taleef-compilation.md  compose a unit within the active sprint
  06-tahqiq-verification.md verify a unit (ideally a different model)
  07-register-distillation.md distil verified units into a register
  08-handoff.md             compact a session into the ledger
project-scaffold/        A new project folder:
  AGENTS.md                 canonical in-folder contract (read first)
  CLAUDE.md / CODEX.md      thin adapters for agentic tools
  PROJECT/CONVENTIONS/DECISIONS/UNCERTAINTIES/SOURCES/STATE.md   the ledger
  sprints/   planned stages (content or infrastructure); example included
  units/     per-unit work; worked example included
  corpus/    retrieved sources — raw/ (immutable) + clean/ (derived)
  registers/ distilled outputs
  src/ tests/  the Builder's code and its tests
  scripts/   verify-unit.py · apply-pack.py · normalise-arabic.py
  templates/sprint/  blank sprint quartet
  docs/      METHOD.md · GLOSSARY.md · PACK-FORMAT.md
```

## Tooling (Python 3, no dependencies)

```
python3 scripts/verify-unit.py units/0001-illustrative-example --corpus corpus   # fidelity harness
python3 scripts/apply-pack.py <pack>.md --dry-run | --apply                       # materialise many files
python3 scripts/normalise-arabic.py corpus/raw/<h>.txt --out corpus/clean/<h>.txt --check  # logged cleaning
```

The example harness run ends in `REVIEW` (one span de-vocalised) — a deliberate
demonstration of how a vocalisation mismatch is surfaced, not waved through.

## Requirements
- Python 3 for the scripts. No dependencies.
- Two or more AI models recommended (so Taḥqīq is independent of Taʾlīf), plus an
  agentic coding tool for the Builder role.
