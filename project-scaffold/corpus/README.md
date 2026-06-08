# corpus/

The local store of **retrieved** source texts — the ground truth spans are
checked against. Two patterns:

- **Single layer (simple projects):** one `<handle>.txt` per source at the top of
  `corpus/`. The shipped example uses this (`sample-source.txt`).
- **Raw + clean (Builder projects):**
  - `corpus/raw/<handle>.txt` — **immutable**, exactly as acquired. Never edit by
    hand or in place.
  - `corpus/clean/<handle>.txt` — **derived** from raw by recorded, re-runnable
    scripts (e.g. `scripts/normalise-arabic.py`). Regenerable from raw + scripts.

Record each source's edition identity and trust level in `../SOURCES.md`, and
record which layer spans are verified against in `../CONVENTIONS.md`. Point the
harness at that layer, e.g. `--corpus corpus/clean`.

The harness proves a span matches the corpus *file*; it cannot prove the file
matches the true source. Curating trustworthy corpus text is the human's job,
upstream of everything else. `sample-source.txt` is an illustrative placeholder —
delete it in a real project.

## Integrity (raw + clean projects)

Every derived `clean/<h>.txt` is recorded in `MANIFEST.md` — its raw origin, the
exact derivation command, and the SHA-256 of both layers. `scripts/corpus-audit.py`
proves clean has not been silently edited, traces to immutable raw, and (with
`--reproduce`) is regenerable from raw by the recorded command. Record provenance
with `corpus-audit.py --record`. The shipped `raw/demo-derived.txt`,
`clean/demo-derived.txt`, and `MANIFEST.md` are an illustrative example — delete
them in a real project.
