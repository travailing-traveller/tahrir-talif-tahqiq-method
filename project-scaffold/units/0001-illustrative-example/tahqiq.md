# Taḥqīq — Unit 0001 (illustrative)

- Harness: `python3 scripts/verify-unit.py units/0001-illustrative-example --corpus corpus`
- Result (as shipped): 1 OK, 1 WARN → **REVIEW** (span 2 matches only after
  diacritic normalisation — a deliberate demonstration of the tashkīl warning).

Verdict: **not verified** — this is a mechanism demo, not real content. In a real
unit you would either restore the tashkīl on span 2 to match the source exactly,
or record a ḍabṭ decision in `DECISIONS.md`, then re-run to a clean PASS.
