# Taʾlīf — Composition of a Unit

*Assembles one unit within the active sprint. Composes nothing from memory.*

You are composing **one unit only** — the active unit named in `STATE.md`, within
the active sprint. Read `AGENTS.md`'s read order first: `PROJECT.md`,
`CONVENTIONS.md`, `SOURCES.md`, `DECISIONS.md`, `UNCERTAINTIES.md`, and the active
sprint's `requirements` / `blueprint`. Stay within the sprint's scope.

## Rules for this unit

1. Pull every primary-text span **verbatim from the corpus**. Copy it; never
   retype from knowledge. Wrap each:

   ```
   ::: span handle="<source-handle>" loc="<āya/page/folio>"
   <exact text from corpus/<source-handle>.txt>
   :::
   ```

2. If a span you need is not in the corpus, **do not supply it.** Record the gap
   in `UNCERTAINTIES.md` and continue with what is retrievable.
3. Add gloss/translation/arrangement **around** the spans. Every claim must trace
   to a span in this unit. The gloss may explain and connect; it may not
   introduce a fact, quotation, or attribution no span supports.
4. If this unit already exists from a prior sprint, **add your layer** to it
   rather than overwriting — keep earlier verified layers intact.
5. Apply a confidence tag (`verified-exact`, `verified-translation`, `paraphrase`,
   `unverified`). Until Taḥqīq passes, status is `needs-tahqiq`.
6. Write to `units/NNNN-<slug>/unit.md`. Touch no unit outside the sprint scope.

When drafted, hand to Taḥqīq (`06-tahqiq-verification.md`) — ideally a **different
model**. Do not mark it verified yourself.
