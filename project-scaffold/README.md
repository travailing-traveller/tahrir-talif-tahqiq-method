# Project Scaffold

Copy this folder for a new Taḥrīr / Taʾlīf / Taḥqīq Method project.

## First steps

1. Fill in `PROJECT.md` after the Discovery Gate passes.
2. Place retrieved source files in `corpus/`.
3. Record sources in `planning/SOURCE_LEDGER.md`.
4. Define units in `planning/UNITS.md`.
5. Work one unit at a time under `units/`.
6. Verify units before creating register outputs.

## Test the harness

From this folder:

```bash
python3 scripts/verify-unit.py units/0001-illustrative-example --corpus corpus
```

The example intentionally produces a `REVIEW` result because one span matches only after Arabic-diacritic normalisation. This demonstrates that the harness surfaces a caution rather than hiding it.
