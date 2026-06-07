# The Taḥrīr / Taʾlīf / Taḥqīq Method — Philosophy

**تحرير · تأليف · تحقيق**

*A discipline for producing Islamic-studies work with AI assistance without surrendering fidelity, attribution, verification, or scholarly judgement.*

> **Status: draft, circulated for feedback.** This document states principles and operating commitments. It is offered for criticism and refinement. Disagreement is part of the requested contribution.

## What this is

The Taḥrīr / Taʾlīf / Taḥqīq Method is a method, not a tool.

It is a way of organising scholarly work so that AI may assist with retrieval, arrangement, drafting, translation, comparison, and distillation without being allowed to originate primary text, vocalisation, attribution, or source claims from memory.

The method is built on one governing principle:

> **The source remains sovereign. The model assists; it does not authorise.**

## The three movements

### Taḥrīr — precise formulation

Taḥrīr is the disciplined formulation of the work before production begins. It defines the purpose, corpus, source hierarchy, unit of study, intended audience, output register, terminology policy, citation conventions, permitted operations, forbidden operations, and verification standard.

Nothing substantive is composed until this is clear.

### Taʾlīf — composition and arrangement

Taʾlīf is the controlled composition, arrangement, translation, annotation, explanation, or distillation of material from retrieved and identified sources.

It proceeds one unit at a time. A unit may be an āya and its gloss, one report, one lexical entry, one folio, one masʾalah, one passage, one marginal note, or another project-defined unit.

### Taḥqīq — verification and establishment

Taḥqīq checks that the unit answers to its source. It verifies quotations, source handles, translation fidelity, terminology, claims, uncertainties, and register constraints. Ideally, Taḥqīq is performed by a different model or reviewer from the one that performed Taʾlīf.

Verification is not merely a final stage. It is continuous, unit by unit.

## 1. The primacy of fidelity — amāna

Fidelity outranks fluency, elegance, completeness, speed, and productivity.

This is an expression of **amāna**. In Islamic scholarly transmission, reliability is not merely a matter of sounding plausible. It requires disciplined preservation, attribution, and accountability. Where the tradition demanded precision, restraint, and traceability from transmitters and scholars, this method demands a **handle**: a pointer from every source span, citation, and source-claim back to the exact file, page, unit, or reference on which it rests.

The cardinal sin of the method is fabrication: a quotation that drifts from its source, a vocalisation supplied from memory, an attribution confected, a reference guessed, a legal or theological implication smoothed into certainty.

The method exists to make such failures structurally difficult and easier to detect.

## 2. Retrieval-grounded, never memory-grounded

A model may select, compare, arrange, translate, summarise, and distil retrieved material. It may not originate primary text, vocalisation, attribution, isnād, bibliographic detail, page reference, or source claim from its own memory.

Every verbatim source span must come from a source present in the project corpus or from an explicitly approved external reference. Every span must carry a handle.

If a span cannot be retrieved, it does not enter the work as source text. It enters the uncertainty ledger.

## 3. The source, not the model, is the authority

No model is the source of truth. No chat thread is the source of truth. The project folder is the durable ledger of the sources, decisions, questions, risks, units, claims, terminology, and verification status.

A new human reviewer or model should be able to read the folder and understand:

- what is being made;
- from what sources;
- to what standard;
- what has been decided;
- what remains uncertain;
- what has been verified;
- what must not be claimed.

## 4. The user must think before the method proceeds

The method requires the user to think clearly and comprehensively before serious production begins.

The user first gives a single-line description of the intended project. That line guides the Discovery Gate.

The Discovery Gate then conducts a rigorous interview — a **munāqasha** — covering purpose, corpus, source status, scope, unit size, audience, register, fidelity requirements, citation rules, terminology, verification standard, risks, and smallest useful deliverable.

The method will not proceed if responses are vague, evasive, contradictory, lazy, or not thoughtful enough.

This refusal is not a defect. It is part of the method. A project that cannot survive the Discovery Gate is not yet ready.

## 5. Division of labour and model agnosticism

The method works best when different roles are separated, and preferably performed by different models or reviewers.

Do not ordinarily allow one model to discover, compose, verify, rewrite, and audit its own work without separation.

The roles are:

- Discovery Lead;
- Source Clerk;
- Text Processor;
- Translator / Composer;
- Verifier;
- Register Editor;
- Final Auditor.

Different models have different strengths and blind spots. A verifier that shares the same assumptions as the composer may miss the same errors. The strongest check is a human scholar assisted by deterministic checks and independent review.

The method is model-agnostic by design. It should not depend on one platform, vendor, interface, or conversation.

## 6. Verify in small units, never in bulk

Bulk-generate-then-check is forbidden for serious scholarly work.

The work proceeds one unit at a time. A unit is composed, checked, classified, and only then closed. If undetected drift occurs in bulk, the whole apparatus becomes quietly corrupt. Small units make fidelity visible.

Each unit should record:

- unit ID;
- source handle(s);
- operation performed;
- output;
- claims introduced;
- terminology decisions;
- uncertainties;
- verification status;
- reviewer.

## 7. Confidence must travel with claims

Every source span and every claim should carry an appropriate status. Suggested tags:

- `verified-exact` — the span exactly matches the cited source;
- `verified-normalised` — the span matches after approved normalisation;
- `verified-translation` — translation checked against the source;
- `paraphrase` — derived from the source but not a direct translation;
- `editorial-judgement` — an explicit judgement by the reviewer;
- `application` — reflective or pedagogical application, not source-claim;
- `unverified` — not yet established;
- `requires-review` — human or specialist review needed;
- `rejected` — not acceptable for output.

Outputs that will be heard or read uncritically — sermons, public summaries, audio scripts, teaching handouts — may draw only on material appropriate to their risk level.

## 8. Uncertainty is preserved, never resolved by invention

Uncertainty is a scholarly asset, not an embarrassment.

The method preserves:

- unreadable text;
- uncertain readings;
- possible OCR corruption;
- disputed attribution;
- unclear referents;
- ambiguous syntax;
- contested legal implications;
- terminology requiring review;
- missing citations;
- source hierarchy questions.

Uncertainty belongs in the uncertainty or questions ledger. It must not be hidden for the sake of tidy prose.

## 9. Registers preserve; they do not smuggle source-claims

A verified core may be distilled into different registers: academic prose, annotated edition, teaching notes, slides, sermon, lecture outline, public summary, Arabic scholarly prose, or publication copy.

A register may compress, reorder, simplify, explain, or apply. It may not present new propositional source-claims as though they were contained in the verified base.

For teaching and devotional registers, faithful application is permitted, but it must remain clearly distinguishable from claims about what the source itself says.

## 10. The human is the muḥaqqiq of record

AI output is a draft pending verification. The method narrows the review surface and makes errors more visible, but it does not transfer responsibility to a machine.

Every claim that ships remains the responsibility of the human editor, translator, teacher, author, or scholar who chooses to rely on it.

The method can enforce handles, ledgers, and checks. It cannot enforce sincerity, adab, proportionality, or fear of misrepresenting the Qurʾān, the Prophet ﷺ, the early Muslims, or the scholarly tradition. That remains with the one doing the work.

## What this method does not do

- It does not make a model a scholar.
- It does not replace training, judgement, language competence, ijāza, or specialist review.
- It does not guarantee correctness.
- It does not validate the corpus itself.
- It does not prove that a printed edition, scan, OCR, or transcription is accurate.
- It does not remove the need to read, think, check, and take responsibility.

The method reduces specific risks: fabrication, drift, unsupported claims, untracked uncertainty, and premature polishing. The rest of scholarship still has to be done.

## The loop in one breath

State the project in one line → survive the Discovery Gate → formulate the project foundations through Taḥrīr → compose or transform one retrieved unit through Taʾlīf → verify it through Taḥqīq, preferably independently → distil verified units into approved registers → keep the folder as the durable ledger.

Formulate. Compose. Verify. In that order — and verify always.
