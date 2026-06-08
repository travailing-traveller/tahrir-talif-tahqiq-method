# src/

The Builder's code: scrapers, cleaners, segmenters, register exporters, and any
project-local tooling. Production transforms of source text must be deterministic,
logged in `DECISIONS.md`, and never mutate `corpus/raw/`. Keep secrets out of the
repo.
