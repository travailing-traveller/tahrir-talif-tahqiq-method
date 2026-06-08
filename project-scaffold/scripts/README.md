# scripts/

Python 3, no dependencies. The Builder owns these; Taḥqīq runs the harness.

## verify-unit.py — fidelity verification harness
Checks every verbatim span in a unit has a handle and is present in its cited
corpus file.
```
python3 scripts/verify-unit.py units/NNNN-<slug> --corpus corpus        # or --corpus corpus/clean
```
OK = exact match; WARN = matches only after diacritic normalisation (adjudicate
tashkīl/ḍabṭ); FAIL = no handle, missing source, or text absent (possible
fabrication). Exit 0 only when every span is a clean OK. It proves a span matches
the corpus file, not that the file matches the true source — see `../SOURCES.md`.

## apply-pack.py — pack importer
Unpacks a single Markdown pack (FILE: markers + 60-equals separators) into many
files in one reviewed step.
```
python3 scripts/apply-pack.py <pack>.md --dry-run
python3 scripts/apply-pack.py <pack>.md --apply
```
Refuses absolute paths, parent traversal, duplicate FILE sections, protected
files, and anything under `corpus/raw/`. Format: `../docs/PACK-FORMAT.md`.

## normalise-arabic.py — Builder cleaning utility
Derives a CLEAN text from a RAW source via only the normalisations you request,
reporting exactly what changed; never touches the input.
```
python3 scripts/normalise-arabic.py corpus/raw/<h>.txt --out corpus/clean/<h>.txt \
    --strip-tashkil --normalise-alef [--check]
```
Record the exact command in `../DECISIONS.md` so the clean layer is reproducible.

## corpus-audit.py — corpus integrity audit

Machine-enforces the no-silent-corruption rule. Reads `corpus/MANIFEST.md` and
proves every `corpus/clean/<h>.txt` still hashes to its recorded value, traces to
an immutable `corpus/raw/<h>.txt`, and that no untracked clean file exists.

```
python3 scripts/corpus-audit.py --corpus corpus              # integrity (fast, no exec)
python3 scripts/corpus-audit.py --corpus corpus --reproduce  # also re-run cmd, match clean
python3 scripts/corpus-audit.py --record --handle H --raw H.txt \
    --cmd 'python3 scripts/normalise-arabic.py {in} --out {out} --strip-tatweel'
```

- **integrity** (default): SHA-256 of each raw and clean matches the manifest;
  flags silently edited clean files, changed raw, and orphan clean files.
- **--reproduce**: re-runs each recorded derivation (in-repo python only, no
  shell) and confirms it yields the committed clean byte-for-byte.
- **--record**: computes hashes and adds/updates a manifest block.

Run it before a Builder hands off prepared text; make it an acceptance criterion
of any infrastructure sprint. `demo-derived` + `MANIFEST.md` are an illustrative
example — delete them in a real project.
