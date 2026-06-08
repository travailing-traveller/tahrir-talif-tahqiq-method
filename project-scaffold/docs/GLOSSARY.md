# Glossary

- **Taḥrīr (تحرير)** — precise formulation; the planning/decision phase.
- **Taʾlīf (تأليف)** — composition; assembling and distilling.
- **Taḥqīq (تحقيق)** — verification; establishing the text answers to its source.
- **Builder** — the engineering service role: writes/runs code to prepare the
  corpus and operate the machinery. Produces no scholarly content.
- **Munāqasha (مناقشة)** — the relentless one-question-at-a-time examination that
  drives the Discovery Gate.
- **Amāna (أمانة)** — faithful trust in transmission; the value behind fidelity.
- **Ḍabṭ (ضبط)** — precision/accuracy of transmission, incl. vocalisation.
- **Unit** — one verifiable slice of the work, keyed by locus.
- **Sprint (marḥala / مرحلة)** — a planned stage grouping units; content or
  infrastructure. Carries requirements / blueprint / acceptance / handoff.
- **Span** — a verbatim stretch of source text, copied from the corpus and tagged
  with a handle. The atom of fidelity.
- **Handle** — a source identifier; the corpus filename stem a span cites.
- **Corpus** — the retrieved source texts. `raw/` immutable; `clean/` derived by
  logged scripts. Spans verify against the layer named in `CONVENTIONS.md`.
- **Pack** — a single Markdown file of many `FILE:` blocks, materialised onto disk
  by `scripts/apply-pack.py` (see `PACK-FORMAT.md`).
- **Manifest** — `corpus/MANIFEST.md`: machine-checked provenance for each derived
  clean file (raw origin, derivation command, SHA-256 of both); enforced by
  `scripts/corpus-audit.py`.
- **Register** — an output form distilled from verified units, adding nothing.
- **Confidence tag** — `verified-exact` | `verified-translation` | `paraphrase`
  | `unverified`, carried by each unit.
- **Ledger** — the project folder itself, the durable source of truth.
- **AGENTS.md** — the canonical in-folder contract every model/person reads first.
