# Pack format

A **pack** is one Markdown file that bundles many project files, so a model's
output can populate the folder in a single reviewed step (`scripts/apply-pack.py`).
Used by the Builder to scaffold the ledger or a sprint's unit stubs.

Not wrapped in code fences. A sequence of file blocks; each begins with a `FILE:`
line and is delimited by a separator of **exactly 60 equals signs**:

    ============================================================
    FILE: PROJECT.md
    ============================================================
    <content of PROJECT.md>
    ============================================================
    FILE: units/0001-al-baqara-001/unit.md
    ============================================================
    <content of that unit>

## Apply
```
python3 scripts/apply-pack.py <pack>.md --dry-run    # preview
python3 scripts/apply-pack.py <pack>.md --apply      # write (.bak on overwrite)
```

## Refusals (validated before anything is written)
- absolute paths
- parent traversal (`..`)
- duplicate `FILE` sections
- protected files (`scripts/*.py`, `AGENTS.md`; override with `--allow-protected`)
- any path under `corpus/raw/` — packs must never write source text

## Caveat
A body line that is itself exactly 60 `=` or begins with `FILE:` would be read as
a delimiter. For planning/unit Markdown this almost never arises; avoid those two
patterns inside content.
