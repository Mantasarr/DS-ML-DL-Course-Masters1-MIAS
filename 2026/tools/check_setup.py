"""Verify a student installation before Session 1.

    python tools/check_setup.py

Exits 0 if everything needed for Sessions 1-7 is present and the pinned data
snapshot loads. Exits 1 with specific instructions otherwise.
"""

from __future__ import annotations

import importlib
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

EXPECTED = {
    "numpy": "2.5.2",
    "pandas": "3.0.5",
    "sklearn": "1.9.0",
    "scipy": "1.18.0",
    "matplotlib": "3.11.1",
    "seaborn": "0.13.2",
    "pyarrow": "25.0.1",
    "xgboost": "3.4.1",
}

problems: list[str] = []
warnings: list[str] = []

print("=" * 66)
print("COURSE SETUP CHECK")
print("=" * 66)

major, minor = sys.version_info[:2]
py = f"{major}.{minor}.{sys.version_info[2]}"
if (major, minor) != (3, 12):
    warnings.append(f"Python {py} - the course is pinned to 3.12.x. Minor risk.")
print(f"  python           {py}")

for name, want in EXPECTED.items():
    try:
        mod = importlib.import_module(name)
    except ImportError:
        problems.append(f"{name} is not installed - run: pip install -r requirements.txt")
        print(f"  {name:16s} MISSING")
        continue
    got = getattr(mod, "__version__", "unknown")
    mark = "" if got == want else f"  (expected {want})"
    if got != want:
        warnings.append(f"{name} is {got}, course pins {want}. Numbers may differ slightly.")
    print(f"  {name:16s} {got}{mark}")

print()
try:
    from src.data import PATHS, load_raw, set_seed

    if not PATHS.snapshot.exists():
        problems.append(
            f"Data snapshot missing: {PATHS.snapshot}\n"
            "     It ships with the repository - re-clone or ask the instructor. "
            "Do NOT download a fresh snapshot from Inside Airbnb."
        )
        print("  data snapshot     MISSING")
    else:
        set_seed()
        df = load_raw()
        ok_shape = df.shape == (15293, 90)
        print(f"  data snapshot     loaded {df.shape[0]:,} rows x {df.shape[1]} columns"
              f"{'' if ok_shape else '  (expected 15293 x 90)'}")
        if not ok_shape:
            problems.append(
                f"Snapshot shape is {df.shape}, expected (15293, 90). Wrong file?"
            )
except Exception as exc:  # noqa: BLE001 - report anything to the student
    problems.append(f"Could not load the data: {type(exc).__name__}: {exc}")
    print(f"  data snapshot     ERROR - {type(exc).__name__}")

print()
print("=" * 66)
if warnings:
    print(f"{len(warnings)} warning(s):")
    for w in warnings:
        print(f"   ! {w}")
if problems:
    print(f"{len(problems)} problem(s) to fix before Session 1:")
    for p in problems:
        print(f"   x {p}")
    sys.exit(1)
print("Setup is good. You are ready for Session 1.")
