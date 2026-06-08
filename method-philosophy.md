# The Taḥrīr / Taʾlīf / Taḥqīq Method — Philosophy

**تحرير · تأليف · تحقيق**

*A discipline for producing Islamic-studies work with AI assistance without
surrendering fidelity, attribution, or scholarly judgement.*

> **Status: draft, circulated for feedback.** This document states principles,
> not commandments. It is offered to a small circle for criticism and
> refinement. Disagreement on any point below is the contribution being asked
> for — see `FEEDBACK.md`.

---

## What this is

A *method*, not a tool. It is a way of organising the work of turning sources
into faithful, well-attributed, multi-register scholarship — using AI for the
labour it is genuinely good at (retrieval, arrangement, drafting, distillation)
while structurally denying it the labour it is dangerous at (originating text,
vocalisation, and attribution from memory).

Three movements give the method its name:

- **Taḥrīr (تحرير)** — *precise formulation.* Thinking the work through:
  its purpose, audience, sources, conventions, unit of study, and the standard
  to which it will be held. Nothing is composed until this is sound.
- **Taʾlīf (تأليف)** — *composition.* Assembling the work from retrieved
  sources, one unit at a time, and distilling it into the registers it needs.
- **Taḥqīq (تحقيق)** — *verification.* Establishing that every span and every
  attribution answers to its source — ideally by an independent hand.

The order is also a discipline: **formulate, then compose, then verify** — and
verify continuously, unit by unit, never in bulk at the end.

---

## The principles

### 1. The primacy of fidelity (amāna)

Fidelity outranks fluency, completeness, elegance, and speed. When they
conflict, fidelity wins, every time, without negotiation. The cardinal sin of
this method is **fabrication** — a quotation that drifts from its source, a
vocalisation the model supplied, an attribution it confected, a chain it
smoothed. The whole apparatus exists to make that sin structurally hard to
commit and easy to detect.

This is *amāna*: the trust that what is transmitted is transmitted faithfully.
Where the classical tradition demanded *ḍabṭ* (precision) and *isnād* (a traced
chain) of a transmitter, this method demands a **handle** — a pointer from every
claim back to the exact source it rests on — and a **check** that the pointer
holds.

### 2. Retrieval-grounded, never memory-grounded

This is the single rule that does the most work. A model may *select, arrange,
translate, and distil* retrieved text. It may **never originate** primary text,
vocalisation, or attribution from its own weights. Every verbatim source span is
copied from a retrieved source held in the project's corpus, and tagged with the
handle of that source. If a span cannot be retrieved, it does not enter the
work — it enters the uncertainty ledger.

Language models are fluent at producing *plausible* classical Arabic, isnāds,
and citations that are subtly or wholly wrong. The method's answer is not to
trust the model to be accurate, but to remove its *opportunity* to invent.

### 3. Verify in small units, never in bulk

The work proceeds one **unit** at a time — one āya and its gloss, one report
and its takhrīj, one folio, one entry. A unit is composed, verified against its
sources, and only then closed. Bulk-generate-then-check is forbidden: across
pages, undetected drift accumulates until the apparatus is quietly corrupt. A
small, fully-verified unit cannot drift unseen. This is slower at first and far
safer throughout.

### 4. Division of labour, across different models where possible

The three movements are distinct roles, and the method is **model-agnostic** by
design — it assumes no single vendor, model, or chat thread. Where practical,
run the roles on **different models**, and in particular let **Taḥqīq be
performed by a different model from the one that performed Taʾlīf**. A verifier
that shares weights with the composer shares its blind spots; an independent
model is a genuinely independent check. The strongest check of all is not a
model at all — it is the deterministic verification harness, which answers to no
model's judgement.

No model is ever the source of truth. The sources are sovereign; the folder is
their faithful ledger; the human scholar is the final authority.

### 5. The work is thought through before it is built

This method front-loads thinking. Its **Discovery Gate** is a sustained,
one-question-at-a-time examination — a *munāqasha* — that walks the whole
decision tree of the project before a word is composed: purpose, thesis,
audience, registers, sources and their trust, recension and reading, conventions
of transliteration and citation, the unit of study, the standard of
verification, the treatment of contested material, and the division of labour.

The Gate is deliberately demanding, and it **will not proceed on inadequate
input.** Vague, evasive, contradictory, or "you decide" answers are named as
such and sent back. The method does not reward laziness or shoddiness; it makes
rigour the path of least resistance and shortcuts structurally difficult. A
project that cannot survive the Gate is not yet ready to be built — and that is
a finding, not a failure.

### 6. Uncertainty is preserved, never resolved by invention

Contested readings, unverified attributions, gaps in the corpus, and questions
that need a manuscript you do not have are recorded in the uncertainty ledger
and carried openly. The method never silently resolves an unknown to keep the
output tidy. Intellectual honesty about what is *not* established is part of the
fidelity it protects.

### 7. Registers preserve; they do not add

The same verified core is distilled into many registers — scholarly apparatus,
a sermon, an audio script, a simplified explainer, slides, a translation. A
register may **compress, reorder, translate, or omit**. It may **never add
propositional content** absent from the verified core. Every claim in a derived
register traces back to a unit it came from, so review of a register is review
of its *new* claims — of which there should be none.

### 8. Provenance and confidence travel with every claim

Every span carries a handle; every unit carries a confidence tag
(*verified-exact*, *verified-translation*, *paraphrase*, *unverified*). Outputs
that will be heard or read uncritically — a sermon, an audio narration — are
permitted to draw **only** from verified units. The places with the least
correction in the loop are allowed the least latitude.

### 9. The folder is the durable ledger; the chat is ephemeral

Models reset, threads vanish, vendors change. The project folder — its
conventions, decisions, sources, units, and verification records — is the
durable source of truth. A new collaborator, human or model, should be able to
read the folder and understand what is being made, from what, to what standard,
what has been decided, what remains uncertain, and what has been verified.

### 10. The human is the muḥaqqiq of record

Every claim that ships is the human scholar's responsibility, asserted under
their name and their *amāna*. AI output is a draft pending human verification;
nothing is published unverified. The method narrows the review surface and makes
errors visible — it does not transfer accountability to a machine, and it does
not confer the authority of a scholar on one.

---

## What this method does not do

- It does not make a language model a scholar, nor substitute for *ijāza*,
  training, or judgement.
- It does not guarantee correctness. It makes a specific failure — fabrication —
  hard to commit and easy to catch, and shrinks what a human must re-check. The
  rest of scholarship still has to be done.
- It does not validate the corpus. The harness proves a span matches the corpus
  *file*; it cannot prove the file matches the true source. A faithful copy of a
  faulty edition is still faithful to the wrong thing. Corpus trust — edition
  identity, OCR quality, vocalisation — is recorded in `SOURCES.md` and remains
  a human responsibility upstream of everything else.
- It does not remove the need for *adab*. A method can enforce a handle; it
  cannot enforce sincerity, proportion, or the fear of misrepresenting the
  words of the Prophet ﷺ, the salaf, or the scholars. That remains with the one
  doing the work.

---

## The shape of a session, in one breath

State the project in a single line → submit to the Discovery Gate and survive
its *munāqasha* → produce the **Taḥrīr** (the precise formulation and the
conventions, sources, and unit plan) → for each unit, **Taʾlīf** assembles it
from retrieved sources → **Taḥqīq**, ideally on another model, verifies it, with
the deterministic harness as the floor → distil verified units into the
**registers** the work needs, adding nothing → keep the folder current as the
ledger.

Formulate. Compose. Verify. In that order, and verify always.
