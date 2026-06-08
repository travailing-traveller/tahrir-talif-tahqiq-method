#!/usr/bin/env python3
"""
verify-unit.py - fidelity verification harness for the Tahrir / Ta'lif / Tahqiq method.

Checks that every verbatim source span in a unit is (a) tagged with a source
handle and (b) actually present in the cited corpus file. This is a
DETERMINISTIC, model-independent check: it does not ask any model whether a
quotation is faithful - it proves it against the local corpus by string match.

IMPORTANT LIMITATION: this proves a span matches the CORPUS file, not that the
corpus file matches the true source. Corpus trust (OCR quality, edition
identity, vocalisation accuracy) is recorded in SOURCES.md and remains the
human muhaqqiq's responsibility. The harness narrows the review surface; it
does not remove it.

Usage:
    python3 scripts/verify-unit.py units/0001-illustrative-example/unit.md --corpus corpus
    python3 scripts/verify-unit.py units/0001-illustrative-example           --corpus corpus

Span format inside unit.md:

    ::: span handle="bulaq-tafsir" loc="2:255"
    <verbatim arabic copied from corpus/bulaq-tafsir.txt>
    :::

Exit code 0 only if every span matches its cited source EXACTLY. A span that
matches only after diacritic-insensitive normalisation is reported as a WARNING
(a tashkil/dabt question for a human), and a span absent from its source is a
FAILURE (possible fabrication or drift). Either non-clean result exits 1.
"""

import sys, os, re, argparse, unicodedata

SPAN_RE = re.compile(r'^:::[ \t]*span([^\n]*)\n(.*?)\n:::[ \t]*$', re.S | re.M)
ATTR_RE = re.compile(r'(\w+)\s*=\s*"([^"]*)"')

# Arabic harakat, Qur'anic annotation marks, superscript alef, and tatweel,
# stripped only for the lenient (diacritic-insensitive) comparison.
_DIACRITICS = (
    "\u0610\u0611\u0612\u0613\u0614\u0615\u0616\u0617\u0618\u0619\u061A"
    "\u064B\u064C\u064D\u064E\u064F\u0650\u0651\u0652\u0653\u0654\u0655"
    "\u0656\u0657\u0658\u0659\u065A\u065B\u065C\u065D\u065E\u065F\u0670"
    "\u06D6\u06D7\u06D8\u06D9\u06DA\u06DB\u06DC\u06DF\u06E0\u06E1\u06E2"
    "\u06E3\u06E4\u06E5\u06E6\u06E7\u06E8\u06EA\u06EB\u06EC\u06ED"
    "\u0640"  # tatweel
)
_DIA_TABLE = {ord(c): None for c in _DIACRITICS}


def normalise(s):
    """Diacritic-insensitive, letter-form-insensitive normalisation for the
    lenient comparison only. Strict matching never uses this."""
    s = unicodedata.normalize("NFC", s)
    s = s.translate(_DIA_TABLE)
    for a in "\u0623\u0625\u0622\u0671":   # hamzated / wasla alef -> bare alef
        s = s.replace(a, "\u0627")
    s = s.replace("\u0649", "\u064A")        # alef maqsura -> ya
    s = s.replace("\u0624", "\u0648")        # waw-hamza -> waw
    s = s.replace("\u0626", "\u064A")        # ya-hamza  -> ya
    s = s.replace("\u0629", "\u0647")        # ta marbuta -> ha
    s = re.sub(r"\s+", " ", s).strip()
    return s


def parse_attrs(s):
    return {k: v for k, v in ATTR_RE.findall(s)}


def find_unit_file(path):
    if os.path.isdir(path):
        cand = os.path.join(path, "unit.md")
        if os.path.isfile(cand):
            return cand
        sys.exit(f"ERROR: no unit.md found in {path}")
    if not os.path.isfile(path):
        sys.exit(f"ERROR: unit file not found: {path}")
    return path


def main():
    ap = argparse.ArgumentParser(description="Fidelity verification harness.")
    ap.add_argument("unit", help="path to a unit.md or a unit directory")
    ap.add_argument("--corpus", default="corpus", help="path to the corpus dir")
    args = ap.parse_args()

    unit_file = find_unit_file(args.unit)
    text = open(unit_file, encoding="utf-8").read()
    spans = SPAN_RE.findall(text)

    print(f"Unit:   {unit_file}")
    print(f"Corpus: {args.corpus}")
    print(f"Spans:  {len(spans)}\n")

    if not spans:
        print("WARN: no '::: span' blocks found.")
        print("A unit that asserts content but cites no verbatim source is itself")
        print("a finding - record it in UNCERTAINTIES.md before proceeding.")
        return 0

    failures = warnings = oks = 0
    for i, (attr_str, content) in enumerate(spans, 1):
        attrs = parse_attrs(attr_str)
        handle = attrs.get("handle", "").strip()
        quoted = content.strip()
        label = f"span {i}" + (f' ({attrs.get("loc")})' if attrs.get("loc") else "")

        if not handle:
            print(f"  [FAIL] {label}: no source handle "
                  f"(no-claim-without-a-handle gate)")
            failures += 1
            continue

        corpus_path = os.path.join(args.corpus, handle + ".txt")
        if not os.path.isfile(corpus_path):
            print(f"  [FAIL] {label}: source not found -> {corpus_path}")
            failures += 1
            continue

        source = open(corpus_path, encoding="utf-8").read()
        if quoted in source:
            print(f"  [ OK ] {label}: exact match in '{handle}'")
            oks += 1
        elif normalise(quoted) in normalise(source):
            print(f"  [WARN] {label}: matches '{handle}' only after "
                  f"diacritic-insensitive normalisation - adjudicate tashkil/dabt")
            warnings += 1
        else:
            print(f"  [FAIL] {label}: NOT found in '{handle}' "
                  f"(possible fabrication or drift)")
            failures += 1

    print(f"\nResult: {oks} ok, {warnings} warning(s), {failures} failure(s)")
    if failures:
        print("STATUS: FAIL - do not mark this unit verified.")
        return 1
    if warnings:
        print("STATUS: REVIEW - strict match failed on some spans; a human "
              "must adjudicate before this unit is marked verified.")
        return 1
    print("STATUS: PASS - every span matched its cited source exactly.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
