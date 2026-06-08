# Taḥrīr — Precise Formulation

*Run only after the Discovery Gate is satisfied. Produces the project's written
foundation, including the sprint plan. Composes no source content.*

The Discovery Gate has resolved the project. Now write its precise formulation
into the folder. Produce **planning and conventions only** — no āyāt, no reports,
no quotations.

Populate or update:

- **`AGENTS.md`** — fill `{PROJECT_TITLE}`; confirm the read order and rules fit
  this project.
- **`PROJECT.md`** — one-line brief; purpose and thesis; audience; register(s)
  and which is primary; base edition / riwāya; the definition of a **unit**; the
  verification standard; the division of labour across models.
- **`CONVENTIONS.md`** — transliteration, name forms, citation format, canonical
  term renderings. Be opinionated; list rejected alternatives.
- **`SOURCES.md`** — every source with edition identity, corpus handle, and trust
  level. Flag any not yet retrieved.
- **`DECISIONS.md`** — the load-bearing editorial decisions from discovery.
- **`UNCERTAINTIES.md`** — every open question carried forward.
- **`STATE.md`** — the phase, the **sprint plan** (the unit plan grouped into
  stages — see below), and the active sprint/unit.

## The sprint plan

Break the unit plan into **sprints** when the work spans many units or multiple
layers (a tafsīr pipeline, a multi-volume taḥqīq). For a single-unit work, skip
sprints and point `STATE.md` straight at the unit.

For each sprint, create `sprints/NNN-<slug>/` by copying `templates/sprint/`, and
fill its `requirements` (scope: which units/range, which layer/register, which
sources), `blueprint` (sequence, sources per unit, dependencies, verification
standard), `acceptance`, and `handoff`. Sequence sprints by dependency (e.g.
base-text before lexical before balāgha). Units are keyed by locus and may gain a
verified layer in a later sprint.

Then **stop.** Recommend the first sprint and its smallest useful first unit. If
the corpus must still be acquired, cleaned, or segmented, hand off to the
**Builder** (`04-builder-execution.md`) first; otherwise hand off to Taʾlīf
(`05-taleef-compilation.md`). Do not begin composing.
