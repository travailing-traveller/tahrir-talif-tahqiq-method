#!/usr/bin/env python3
"""
corpus-audit.py - machine-enforce the corpus integrity rule.

The verification harness trusts the corpus. So the corpus itself must be proven
honest: that nothing in corpus/clean/ was silently hand-edited, that every clean
file traces to an immutable raw source by a recorded derivation, and that no
untracked clean file has appeared. This script makes that a check, not a promise.

It reads corpus/MANIFEST.md, which records one block per derived file:

    ::: derive handle="bulaq-tafsir" raw="bulaq-tafsir.txt" sha256_raw="<hex>" sha256_clean="<hex>"
    cmd: python3 scripts/normalise-arabic.py {in} --out {out} --strip-tatweel
    :::

`cmd` is optional; omit it (or use `cmd: copy`) when clean == raw (identity).

Modes:
  (default)     integrity: hashes match, raw/clean exist, no orphan clean files.
  --reproduce   additionally re-run each recorded cmd on raw/ and confirm it
                yields clean/ byte-for-byte. Runs only in-repo python scripts,
                no shell, with a timeout.
  --record      compute hashes for a (handle, raw, clean, cmd) and add/update its
                manifest block, so recording provenance is one command.

Usage:
  python3 scripts/corpus-audit.py --corpus corpus
  python3 scripts/corpus-audit.py --corpus corpus --reproduce
  python3 scripts/corpus-audit.py --record --handle H --raw H.txt \
      [--clean H.txt] [--cmd "python3 scripts/normalise-arabic.py {in} --out {out} --strip-tatweel"]

Exit code 0 only if every check passes.
"""

import sys, os, re, argparse, hashlib, shlex, subprocess, tempfile, glob

ATTR_RE = re.compile(r'(\w+)\s*=\s*"([^"]*)"')
BLOCK_RE = re.compile(r'^:::[ \t]*derive([^\n]*)\n(.*?)\n:::[ \t]*$', re.S | re.M)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_manifest(text):
    entries = []
    for attr_str, body in BLOCK_RE.findall(text):
        attrs = dict(ATTR_RE.findall(attr_str))
        cmds = [ln.split("cmd:", 1)[1].strip()
                for ln in body.splitlines() if ln.strip().startswith("cmd:")]
        entries.append({
            "handle": attrs.get("handle", "").strip(),
            "raw": attrs.get("raw", "").strip(),
            "sha_raw": attrs.get("sha256_raw", "").strip(),
            "sha_clean": attrs.get("sha256_clean", "").strip(),
            "cmd": cmds[0] if cmds else "",
        })
    return entries


def safe_cmd(parts, root):
    """Permit only python(3) running a .py under scripts/ or src/. No shell."""
    if not parts:
        return "empty command"
    if os.path.basename(parts[0]) not in ("python", "python3"):
        return "command must invoke python3"
    script = next((p for p in parts[1:] if p.endswith(".py")), None)
    if not script:
        return "command must run a .py script"
    norm = script.replace("\\", "/")
    if not (norm.startswith("scripts/") or norm.startswith("src/")):
        return "script must live under scripts/ or src/"
    return None


def audit(corpus, manifest_path, reproduce, root):
    if not os.path.isfile(manifest_path):
        print(f"No manifest at {manifest_path}.")
        print("If this project uses a raw+clean corpus, create one (see scripts/README.md).")
        # No manifest + no clean/ files is fine (single-layer project).
        cleans = glob.glob(os.path.join(corpus, "clean", "*.txt"))
        if cleans:
            print(f"FAIL: {len(cleans)} file(s) in clean/ but no manifest to vouch for them.")
            return 1
        print("PASS: nothing to audit (single-layer or empty corpus).")
        return 0

    entries = parse_manifest(open(manifest_path, encoding="utf-8").read())
    tracked = {e["handle"] for e in entries}
    fails = warns = oks = 0

    for e in entries:
        h = e["handle"]
        raw_p = os.path.join(corpus, "raw", e["raw"])
        clean_p = os.path.join(corpus, "clean", h + ".txt")

        if not e["raw"] or not os.path.isfile(raw_p):
            print(f"  [FAIL] {h}: raw missing -> {raw_p}"); fails += 1; continue
        if not os.path.isfile(clean_p):
            print(f"  [FAIL] {h}: clean missing -> {clean_p}"); fails += 1; continue

        if e["sha_raw"]:
            if sha256_file(raw_p) != e["sha_raw"]:
                print(f"  [FAIL] {h}: raw changed since recorded (raw is meant to be immutable)")
                fails += 1; continue
        else:
            print(f"  [WARN] {h}: no recorded sha256_raw (run --record)"); warns += 1

        if e["sha_clean"]:
            if sha256_file(clean_p) != e["sha_clean"]:
                print(f"  [FAIL] {h}: clean changed since recorded (silent edit?)")
                fails += 1; continue
        else:
            print(f"  [WARN] {h}: no recorded sha256_clean (run --record)"); warns += 1

        if reproduce:
            if e["cmd"] in ("", "copy"):
                same = open(raw_p, "rb").read() == open(clean_p, "rb").read()
                if not same:
                    print(f"  [FAIL] {h}: declared identity (copy) but clean != raw")
                    fails += 1; continue
            else:
                with tempfile.TemporaryDirectory() as td:
                    out = os.path.join(td, "out.txt")
                    cmd = e["cmd"].replace("{in}", raw_p).replace("{out}", out)
                    parts = shlex.split(cmd)
                    why = safe_cmd(parts, root)
                    if why:
                        print(f"  [FAIL] {h}: cannot reproduce - {why}"); fails += 1; continue
                    try:
                        subprocess.run(parts, cwd=root, timeout=60,
                                       stdout=subprocess.DEVNULL,
                                       stderr=subprocess.DEVNULL, check=True)
                    except Exception as ex:
                        print(f"  [FAIL] {h}: derivation command failed ({ex})")
                        fails += 1; continue
                    if not os.path.isfile(out) or \
                       open(out, "rb").read() != open(clean_p, "rb").read():
                        print(f"  [FAIL] {h}: re-running cmd did NOT reproduce clean")
                        fails += 1; continue
            print(f"  [ OK ] {h}: integrity + reproducible from raw")
            oks += 1
        else:
            print(f"  [ OK ] {h}: integrity (hashes match)")
            oks += 1

    # Orphans: clean files nobody vouches for.
    for cp in sorted(glob.glob(os.path.join(corpus, "clean", "*.txt"))):
        if os.path.basename(cp)[:-4] not in tracked:
            print(f"  [FAIL] orphan clean file (no manifest entry): {cp}")
            fails += 1
    # Raw without a derived clean: allowed, but flag it.
    for rp in sorted(glob.glob(os.path.join(corpus, "raw", "*.txt"))):
        if not any(e["raw"] == os.path.basename(rp) for e in entries):
            print(f"  [WARN] raw with no recorded derivation: {rp}")
            warns += 1

    print(f"\nResult: {oks} ok, {warns} warning(s), {fails} failure(s)")
    if fails:
        print("STATUS: FAIL - corpus integrity is not established.")
        return 1
    print("STATUS: PASS - corpus integrity established"
          + (" and reproducible." if reproduce else "."))
    return 0


def record(corpus, manifest_path, handle, raw, clean, cmd):
    raw_p = os.path.join(corpus, "raw", raw)
    clean_p = os.path.join(corpus, "clean", clean or (handle + ".txt"))
    for p in (raw_p, clean_p):
        if not os.path.isfile(p):
            sys.exit(f"ERROR: file not found: {p}")
    block = (
        f'::: derive handle="{handle}" raw="{raw}" '
        f'sha256_raw="{sha256_file(raw_p)}" sha256_clean="{sha256_file(clean_p)}"\n'
        f'cmd: {cmd}\n' if cmd else
        f'::: derive handle="{handle}" raw="{raw}" '
        f'sha256_raw="{sha256_file(raw_p)}" sha256_clean="{sha256_file(clean_p)}"\n'
    )
    block += ":::\n"
    text = open(manifest_path, encoding="utf-8").read() if os.path.isfile(manifest_path) else \
        "# Corpus derivation manifest\n\nMachine-checked provenance for derived corpus files.\n\n"
    pat = re.compile(r'^:::[ \t]*derive[^\n]*handle="' + re.escape(handle) +
                     r'".*?\n:::[ \t]*$', re.S | re.M)
    text = pat.sub(block.rstrip(), text) if pat.search(text) else text.rstrip() + "\n\n" + block
    with open(manifest_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Recorded '{handle}' in {manifest_path}.")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Corpus integrity audit.")
    ap.add_argument("--corpus", default="corpus")
    ap.add_argument("--manifest", default=None)
    ap.add_argument("--reproduce", action="store_true")
    ap.add_argument("--record", action="store_true")
    ap.add_argument("--handle"); ap.add_argument("--raw")
    ap.add_argument("--clean"); ap.add_argument("--cmd", default="")
    ap.add_argument("--root", default=os.getcwd())
    a = ap.parse_args()
    manifest_path = a.manifest or os.path.join(a.corpus, "MANIFEST.md")

    if a.record:
        if not (a.handle and a.raw):
            sys.exit("ERROR: --record needs --handle and --raw.")
        sys.exit(record(a.corpus, manifest_path, a.handle, a.raw, a.clean, a.cmd))
    sys.exit(audit(a.corpus, manifest_path, a.reproduce, os.path.abspath(a.root)))


if __name__ == "__main__":
    main()
