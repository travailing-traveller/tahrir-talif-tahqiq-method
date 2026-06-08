# Feedback wanted

This is a draft method shared with a small circle. The useful contribution is
disagreement. Some axes where critique would help most:

1. **The three movements** — is Taḥrīr / Taʾlīf / Taḥqīq the right division, and
   the right naming? Does the order mislead (verification is continuous, not last)?
2. **The retrieval-grounded rule** — is "never originate primary text from
   memory" workable in your actual sources, or are there cases where no corpus is
   retrievable and the rule needs a principled exception?
3. **The unit** — is the per-unit, verify-before-close discipline practical at the
   scale you work, or does it need a coarser/finer grain for some genres?
4. **The verification harness** — what does it miss? Arabic normalisation choices
   (alef forms, tā marbūṭa, alef maqṣūra) are debatable; so is strict-vs-normalised
   tashkīl. The harness cannot judge attribution, translation, or corpus accuracy
   — is the division between "machine-checkable" and "human-only" drawn correctly?
5. **The Discovery Gate's refusal** — is "will not proceed on inadequate answers"
   too rigid, or exactly right? Where is the line between rigour and obstruction?
6. **Registers add nothing** — is the no-new-propositional-content rule too
   strict for genuinely pedagogical registers (a sermon often *applies* a text)?
   How should faithful application differ from added claims?
7. **Gaps** — what discipline is missing entirely? (Translation review? Handling
   of multiple recensions in one unit? Versioning of the corpus?)

Mark up the files directly, or note section + objection. Concrete counter-examples
from real work are worth more than general agreement.

8. **The Builder layer & corpus integrity** — the kit now ships a deterministic
   audit (`corpus-audit.py`): a SHA-256 manifest proving clean/ is unedited and,
   with --reproduce, regenerable from raw/ by the recorded command. Is the manifest
   format right? Is hashing the correct granularity (vs per-line, or signing)? And
   is re-running recorded commands the right reproducibility guarantee, or too
   coupled to deterministic tools?
