#!/usr/bin/env python3
"""
normalise-arabic.py - Builder utility: derive a CLEAN text from a RAW source.

Applies only the normalisations you explicitly request, reports exactly what it
changed, and never touches the input. The RAW layer stays immutable; the CLEAN
layer is regenerable at any time from RAW + this command. This is how the
Builder prepares text without becoming a back door for fabrication.

Usage:
    python3 scripts/normalise-arabic.py corpus/raw/<h>.txt --out corpus/clean/<h>.txt \
        [--strip-tashkil] [--normalise-alef] [--alef-maqsura] [--ta-marbuta] \
        [--strip-tatweel] [--collapse-space] [--check]

  --check    report what WOULD change; write nothing.

Record the exact command used in DECISIONS.md so the clean layer is reproducible.
Nothing is normalised unless you ask for it - the defaults change nothing.
"""

import sys, os, re, argparse, unicodedata

TASHKIL = (
    "\u0610\u0611\u0612\u0613\u0614\u0615\u0616\u0617\u0618\u0619\u061A"
    "\u064B\u064C\u064D\u064E\u064F\u0650\u0651\u0652\u0653\u0654\u0655"
    "\u0656\u0657\u0658\u0659\u065A\u065B\u065C\u065D\u065E\u065F\u0670"
    "\u06D6\u06D7\u06D8\u06D9\u06DA\u06DB\u06DC\u06DF\u06E0\u06E1\u06E2"
    "\u06E3\u06E4\u06E5\u06E6\u06E7\u06E8\u06EA\u06EB\u06EC\u06ED"
)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("infile")
    ap.add_argument("--out")
    ap.add_argument("--strip-tashkil", action="store_true")
    ap.add_argument("--normalise-alef", action="store_true")
    ap.add_argument("--alef-maqsura", action="store_true")
    ap.add_argument("--ta-marbuta", action="store_true")
    ap.add_argument("--strip-tatweel", action="store_true")
    ap.add_argument("--collapse-space", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    if not os.path.isfile(a.infile):
        sys.exit(f"ERROR: input not found: {a.infile}")
    if not a.check and not a.out:
        sys.exit("ERROR: provide --out, or use --check to preview.")

    text = open(a.infile, encoding="utf-8").read()
    s = unicodedata.normalize("NFC", text)
    report = []

    def count(before, after, label):
        d = sum(1 for x, y in zip(before, after) if x != y) + abs(len(before) - len(after))
        if before != after:
            report.append(f"  {label}: changed (~{d} codepoints)")

    if a.strip_tashkil:
        b = s; s = s.translate({ord(c): None for c in TASHKIL}); count(b, s, "strip-tashkil")
    if a.strip_tatweel:
        b = s; s = s.replace("\u0640", ""); count(b, s, "strip-tatweel")
    if a.normalise_alef:
        b = s
        for ch in "\u0623\u0625\u0622\u0671":
            s = s.replace(ch, "\u0627")
        count(b, s, "normalise-alef")
    if a.alef_maqsura:
        b = s; s = s.replace("\u0649", "\u064A"); count(b, s, "alef-maqsura->ya")
    if a.ta_marbuta:
        b = s; s = s.replace("\u0629", "\u0647"); count(b, s, "ta-marbuta->ha")
    if a.collapse_space:
        b = s; s = re.sub(r"[ \t]+", " ", s); count(b, s, "collapse-space")

    print(f"Input:  {a.infile}")
    print(f"Output: {a.out if a.out else '(check only)'}")
    print("Operations applied:" if report else "Operations applied: none (output identical to input)")
    for line in report:
        print(line)

    if a.check:
        print("\nCHECK only - nothing written.")
        return
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    with open(a.out, "w", encoding="utf-8") as f:
        f.write(s)
    print(f"\nWrote {a.out}. RAW input untouched. Record the command in DECISIONS.md.")


if __name__ == "__main__":
    main()
