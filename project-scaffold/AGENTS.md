# AGENTS.md — Canonical Project Contract

**Read this first.** Any model or person working in this folder is bound by it.
The folder — not the chat — is the source of truth.

This project follows the **Taḥrīr / Taʾlīf / Taḥqīq** method, with a **Builder**
service role for code. `docs/METHOD.md` summarises it and the kit's
`method-philosophy.md` gives the principles; this file is the binding contract.

## Project
- Title: {PROJECT_TITLE}
- See `PROJECT.md` for purpose, audience, registers, the unit definition, the
  verification standard, and the division of labour across models.

## Read order (every session)
1. `AGENTS.md` (this file)
2. `PROJECT.md` — identity, unit definition, verification standard
3. `STATE.md` — current phase, active sprint, active unit
4. `CONVENTIONS.md` — house style; and which corpus layer spans verify against
5. `DECISIONS.md` — settled editorial AND engineering decisions
6. `UNCERTAINTIES.md` — open questions; never resolve by inventing
7. `SOURCES.md` — sources, handles, trust levels
8. the active sprint under `sprints/NNN-*/`
9. the active unit under `units/NNNN-*/`

## Non-negotiable rules
1. **Fidelity (amāna)** outranks fluency, completeness, and speed. The cardinal
   sin is fabrication.
2. **Retrieval-grounded, never memory-grounded.** Never originate primary text,
   tashkīl, or attribution from memory. Copy verbatim spans from the corpus.
3. **Every span carries a handle** — `::: span handle="..." loc="..." :::`.
4. **Preserve unknowns** in `UNCERTAINTIES.md`.
5. **One unit at a time.** A unit closes only when Taḥqīq passes.
6. **Registers add nothing** the verified core does not support.
7. **The corpus is sacred.** `corpus/raw/` is immutable; `corpus/clean/` is
   derived only by recorded, re-runnable scripts. Tooling must never silently
   alter source text — a clean step that corrupts text would pass verification
   while being wrong.
8. **The human is the muḥaqqiq of record.** AI output is a draft pending
   verification.

## Roles
- **Taḥrīr** — formulate and decide (Discovery Gate → `PROJECT.md` /
  `CONVENTIONS.md` / `SOURCES.md` + the sprint plan). Composes no content. (`01`,`03`)
- **Builder** — writes and runs code to prepare the corpus and operate the
  machinery (scraping, cleaning, segmenting, the harness, register export,
  packs). Produces **no** scholarly content; serves the three movements. Runs in
  an agentic coding tool. (`04`)
- **Taʾlīf** — compose a unit from retrieved sources; distil registers. (`05`,`07`)
- **Taḥqīq** — verify a unit. Run on a **different model** from Taʾlīf where
  possible. The deterministic harness is the floor. (`06`)

## Sprints (marḥala)
A **sprint** is a planned stage grouping units; use them for multi-unit /
multi-layer work (a tafsīr pipeline), skip them for a single-unit work. Each
sprint carries `requirements` / `blueprint` / `acceptance` / `handoff`. Sprints
may be **content** sprints (Taʾlīf/Taḥqīq produce and verify units) or
**infrastructure** sprints (Builder prepares corpus/tooling); the quartet fits
both — an infrastructure sprint's acceptance includes tests and a fidelity check
that transformations did only what they declare. Units are long-lived and keyed
by locus; a sprint may add a verified layer to existing units.

## Corpus layers
- `corpus/raw/<handle>.txt` — immutable, exactly as acquired.
- `corpus/clean/<handle>.txt` — derived from raw by logged scripts; regenerable
  from raw + scripts. (Simple projects may use a single flat `corpus/<handle>.txt`.)
- Record in `CONVENTIONS.md` which layer spans verify against, and point the
  harness there (`--corpus corpus/clean`).
- Every derived `clean/` file is recorded in `corpus/MANIFEST.md` (raw origin,
  derivation command, and SHA-256 of both). `corpus-audit.py` enforces it.

## Folder map
- `PROJECT.md` `STATE.md` `CONVENTIONS.md` `DECISIONS.md` `UNCERTAINTIES.md`
  `SOURCES.md` — the durable ledger
- `sprints/` — planned stages (content or infrastructure)
- `units/` — per-unit content, keyed by locus
- `corpus/` — retrieved source texts (`raw/` immutable, `clean/` derived)
- `registers/` — distilled outputs from verified units
- `src/` `tests/` — the Builder's code and its tests
- `scripts/` — `verify-unit.py` (fidelity harness), `apply-pack.py` (importer),
  `normalise-arabic.py` (logged cleaning utility), `corpus-audit.py` (integrity audit)
- `templates/sprint/` — a blank sprint quartet
- `docs/` — `METHOD.md`, `GLOSSARY.md`, `PACK-FORMAT.md`

## Tooling
```
python3 scripts/verify-unit.py units/NNNN-<slug> --corpus corpus/clean   # verify
python3 scripts/apply-pack.py <pack>.md --dry-run                        # preview pack
python3 scripts/apply-pack.py <pack>.md --apply                          # write pack
python3 scripts/normalise-arabic.py corpus/raw/<h>.txt --out corpus/clean/<h>.txt --check
python3 scripts/corpus-audit.py --corpus corpus [--reproduce]       # prove corpus integrity
```
A unit is not verified until the harness is clean, or a WARN is adjudicated and
the decision logged in `DECISIONS.md`. The importer refuses absolute paths, `..`,
duplicate `FILE` sections, protected files, and anything under `corpus/raw/`.
Before a Builder hands off prepared text, `corpus-audit.py` must pass: it proves
every `clean/` file still hashes to its recorded value, traces to an immutable
`raw/` source, and (with `--reproduce`) is regenerable from raw by the recorded
command. Provenance is recorded in `corpus/MANIFEST.md` (via `--record`).
