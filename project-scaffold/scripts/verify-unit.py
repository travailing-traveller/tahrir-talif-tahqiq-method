#!/usr/bin/env python3
"""Simple deterministic source-span verifier for a unit folder.

Usage:
    python3 scripts/verify-unit.py units/0001-illustrative-example --corpus corpus

The script expects a unit.json file with:

{
  "unit_id": "...",
  "spans": [
    {"span_id": "S1", "source_id": "source-file-without-txt", "quote": "..."}
  ]
}

It checks whether each quote appears exactly in corpus/<source_id>.txt.
If not, it removes Arabic combining marks and checks again. A normalised match
is reported as REVIEW, not PASS, because vocalisation and orthographic choices
may matter in Islamic studies work.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ARABIC_MARKS = re.compile(r"[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED]")

def strip_marks(text: str) -> str:
    return ARABIC_MARKS.sub("", text)

def load_unit(unit_dir: Path) -> dict:
    unit_file = unit_dir / "unit.json"
    if not unit_file.exists():
        raise SystemExit(f"ERROR: missing {unit_file}")
    return json.loads(unit_file.read_text(encoding="utf-8"))

def main() -> int:
    parser = argparse.ArgumentParser(description="Verify unit source spans against corpus files.")
    parser.add_argument("unit_dir", type=Path)
    parser.add_argument("--corpus", type=Path, required=True)
    args = parser.parse_args()

    unit = load_unit(args.unit_dir)
    spans = unit.get("spans", [])
    if not spans:
        print("ERROR: unit has no spans")
        return 1

    failures = 0
    reviews = 0
    passes = 0

    print(f"Verifying unit: {unit.get('unit_id', args.unit_dir.name)}")

    for span in spans:
        span_id = span.get("span_id", "UNKNOWN")
        source_id = span.get("source_id")
        quote = span.get("quote", "")
        if not source_id or not quote:
            print(f"FAIL  {span_id}: missing source_id or quote")
            failures += 1
            continue

        source_file = args.corpus / f"{source_id}.txt"
        if not source_file.exists():
            print(f"FAIL  {span_id}: missing source file {source_file}")
            failures += 1
            continue

        source_text = source_file.read_text(encoding="utf-8")
        if quote in source_text:
            print(f"PASS  {span_id}: exact match in {source_file.name}")
            passes += 1
        elif strip_marks(quote) in strip_marks(source_text):
            print(f"REVIEW {span_id}: match after Arabic-mark normalisation only")
            reviews += 1
        else:
            print(f"FAIL  {span_id}: quote not found in {source_file.name}")
            failures += 1

    print("---")
    print(f"Summary: {passes} pass, {reviews} review, {failures} fail")

    if failures:
        return 1
    if reviews:
        return 2
    return 0

if __name__ == "__main__":
    sys.exit(main())
