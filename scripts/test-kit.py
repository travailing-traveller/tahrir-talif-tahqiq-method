#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
for rel in [
    'README.md',
    'method-philosophy.md',
    'FEEDBACK.md',
    'LICENSE.md',
    'project-scaffold/scripts/verify-unit.py',
    'project-scaffold/units/0001-illustrative-example/unit.json',
    'project-scaffold/corpus/sample-source.txt',
]:
    path = root / rel
    if not path.exists():
        print(f'MISSING {rel}')
        sys.exit(1)

cmd = [sys.executable, str(root/'project-scaffold/scripts/verify-unit.py'), str(root/'project-scaffold/units/0001-illustrative-example'), '--corpus', str(root/'project-scaffold/corpus')]
result = subprocess.run(cmd, text=True, capture_output=True)
print(result.stdout)
if result.returncode != 2:
    print(result.stderr)
    print(f'Unexpected verifier exit code: {result.returncode}; expected 2 for REVIEW example')
    sys.exit(1)
print('Kit smoke test passed: expected REVIEW result observed.')
