# Taḥqīq — Verification of a Unit

*Independent verification. You should ideally be a DIFFERENT model from the one
that composed this unit. Do not trust the composer; check.*

You are verifying **one unit** within the active sprint. Default posture:
sceptical.

## Procedure

1. **Run the deterministic harness first** (or confirm the human has):

   ```
   python3 scripts/verify-unit.py units/NNNN-<slug>/unit.md --corpus corpus
   ```

   It checks every span has a handle and matches its cited corpus file. `FAIL` =
   not verified, full stop. `WARN` (matches only after diacritic normalisation) =
   a tashkīl/ḍabṭ question to adjudicate against `CONVENTIONS.md`.

2. **Check what the harness cannot:**
   - **Attribution / takhrīj** — does the cited location say this; is the
     attribution correct; does it fit `SOURCES.md` trust levels?
   - **Gloss discipline** — does the gloss/translation add any claim no span
     supports?
   - **Convention conformance** — transliteration, names, citation per
     `CONVENTIONS.md`.
   - **Contested material** — anything disputed presented as settled belongs in
     `UNCERTAINTIES.md`.

3. **Write the verdict** to `units/NNNN-<slug>/tahqiq.md`: PASS or FAIL, the
   harness result, and specifics. On FAIL, return the unit to Taʾlīf with precise
   corrections; do not fix it silently.

4. On PASS, set the unit's `status:` to `verified` and note it in `STATE.md`.
   When every unit in the sprint's scope is verified and the sprint's
   `acceptance.md` is met, the sprint is done.

Only verified units may feed the register/distillation step.
