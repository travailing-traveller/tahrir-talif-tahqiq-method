# The method, in brief

This folder is produced with the **Taḥrīr / Taʾlīf / Taḥqīq** method, with a
**Builder** service role for code. `AGENTS.md` is the binding contract; this is
the orientation.

- **Taḥrīr** — formulate the project precisely (Discovery Gate → ledger + sprint
  plan). Composes nothing.
- **Builder** — the engineering hand: writes and runs code to acquire, clean, and
  segment the corpus, run the harness, export registers, and apply packs. Adds no
  scholarly content; bound by the same fidelity rules, more strictly, because code
  can corrupt text at scale silently.
- **Taʾlīf** — compose one unit at a time from verbatim corpus spans (handles on
  every span); originate no primary text from memory.
- **Taḥqīq** — verify each unit, ideally on a different model, with the harness as
  the floor.

Distil **verified** units into the **registers** the work needs, adding nothing.

## Structure
- **Unit** — the atom of content and verification, keyed by locus.
- **Sprint (marḥala)** — a planned stage grouping units; **content** sprints
  (compose/verify) or **infrastructure** sprints (Builder prepares corpus/tooling).
- **Corpus** — `raw/` (immutable) and `clean/` (derived by logged scripts); spans
  verify against the layer named in `CONVENTIONS.md`.

First files to read: see the read order in `AGENTS.md`. Pack format: `PACK-FORMAT.md`.
