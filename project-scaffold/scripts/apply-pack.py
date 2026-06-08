#!/usr/bin/env python3
"""
apply-pack.py - pack importer for the Taḥrīr / Taʾlīf / Taḥqīq method.

Unpacks a single Markdown "pack" into many project-relative files in one
reviewed step, so a model's planning output (the ledger, a sprint's unit stubs)
becomes real files on disk without copy-paste. Dependency-free (Python 3).

Pack format (NOT wrapped in code fences):

    ============================================================   <- 60 '='
    FILE: PROJECT.md
    ============================================================
    <content of PROJECT.md>
    ============================================================
    FILE: units/0001-al-baqara-001/unit.md
    ============================================================
    <content of that unit>

Usage:
    python3 scripts/apply-pack.py <pack.md> --dry-run
    python3 scripts/apply-pack.py <pack.md> --apply [--no-backup] [--root DIR] [--allow-protected]

Refuses, before writing anything: absolute paths, parent traversal (..),
duplicate FILE sections, protected starter files, and ANY path under
corpus/raw/ (the immutable layer - a pack must never write source text).
"""

import sys, os, re, argparse

SEP_RE = re.compile(r'^={60}$')
FILE_RE = re.compile(r'^FILE:\s*(.+?)\s*$')

# Tooling/contract files a pack must not clobber.
PROTECTED = {
    "scripts/apply-pack.py",
    "scripts/verify-unit.py",
    "scripts/normalise-arabic.py",
    "scripts/corpus-audit.py",
    "AGENTS.md",
}
# Path prefixes a pack must never write into.
PROTECTED_PREFIXES = ("corpus/raw/",)


def parse_args(argv):
    ap = argparse.ArgumentParser(description="Pack importer.")
    ap.add_argument("pack")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--no-backup", action="store_true")
    ap.add_argument("--allow-protected", action="store_true")
    ap.add_argument("--root", default=os.getcwd())
    return ap.parse_args(argv[1:])


def parse_pack(text):
    blocks, cur = [], None
    for line in text.split("\n"):
        if SEP_RE.match(line.strip()):
            continue
        m = FILE_RE.match(line)
        if m:
            if cur:
                blocks.append(cur)
            cur = {"path": m.group(1).strip(), "body": []}
            continue
        if cur is not None:
            cur["body"].append(line)
    if cur:
        blocks.append(cur)
    out = []
    for b in blocks:
        body = "\n".join(b["body"]).lstrip("\n").rstrip() 
        out.append({"path": b["path"], "content": body + "\n" if body else ""})
    return out


def reason_unsafe(rel, allow_protected):
    if not rel:
        return "empty path"
    if os.path.isabs(rel):
        return "absolute path not allowed"
    norm = rel.replace("\\", "/")
    if ".." in norm.split("/"):
        return "parent traversal (..) not allowed"
    for pre in PROTECTED_PREFIXES:
        if norm.startswith(pre):
            return f"writes into protected layer '{pre}' (immutable)"
    if norm in PROTECTED and not allow_protected:
        return "protected starter file (use --allow-protected to override)"
    return None


def main():
    args = parse_args(sys.argv)
    if args.dry_run == args.apply:
        sys.exit("ERROR: choose exactly one of --dry-run or --apply.")
    if not os.path.isfile(args.pack):
        sys.exit(f"ERROR: pack not found: {args.pack}")

    blocks = parse_pack(open(args.pack, encoding="utf-8").read())
    if not blocks:
        sys.exit("ERROR: no FILE: blocks found. Is this a valid pack?")

    errors, seen = [], set()
    for b in blocks:
        why = reason_unsafe(b["path"], args.allow_protected)
        if why:
            errors.append(f"  {b['path'] or '(blank)'} -> {why}")
        if b["path"] in seen:
            errors.append(f"  {b['path']} -> duplicate FILE section")
        seen.add(b["path"])
    if errors:
        print("ERROR: refused, nothing written:")
        print("\n".join(errors))
        sys.exit(1)

    root = os.path.abspath(args.root)
    print(f"Pack:  {args.pack}")
    print(f"Root:  {root}")
    print(f"Mode:  {'APPLY' if args.apply else 'DRY-RUN'}")
    print(f"Files: {len(blocks)}\n")

    created = overwritten = backed = 0
    for b in blocks:
        dest = os.path.join(root, b["path"])
        exists = os.path.isfile(dest)
        n = len(b["content"].encode("utf-8"))
        print(f"  [{'overwrite' if exists else 'create   '}] {b['path']}  ({n} bytes)")
        if not args.apply:
            continue
        os.makedirs(os.path.dirname(dest) or ".", exist_ok=True)
        if exists and not args.no_backup:
            with open(dest + ".bak", "w", encoding="utf-8") as f:
                f.write(open(dest, encoding="utf-8").read())
            backed += 1
        with open(dest, "w", encoding="utf-8") as f:
            f.write(b["content"])
        overwritten += exists
        created += not exists

    print()
    if args.apply:
        print(f"Done. {created} created, {overwritten} overwritten, {backed} backed up (.bak).")
    else:
        print("DRY-RUN complete. No files written. Re-run with --apply to write.")


if __name__ == "__main__":
    main()
