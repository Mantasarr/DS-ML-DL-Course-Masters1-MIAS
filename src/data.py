"""Project paths, seeding, and raw data access.

This module grows with the course. Right now it does three things and nothing
more, deliberately: Session 1 is about making first contact with data yourself,
not about calling a helper that has already done the work.

    from src.data import PATHS, load_raw, set_seed
"""

from __future__ import annotations

import os
import random
from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent

#: The pinned snapshot. Do not re-download: Inside Airbnb rotates snapshots
#: quarterly and every figure in the course notes is tied to this one.
SNAPSHOT = "listings_barcelona_2026-06-24.csv.gz"

#: Reproducibility. Every notebook calls set_seed(SEED) in its first code cell.
SEED = 42


@dataclass(frozen=True)
class Paths:
    root: Path = ROOT
    raw: Path = ROOT / "data" / "raw"
    interim: Path = ROOT / "data" / "interim"
    sealed: Path = ROOT / "data" / "SEALED_TEST"

    @property
    def snapshot(self) -> Path:
        return self.raw / SNAPSHOT


PATHS = Paths()


def set_seed(seed: int = SEED) -> int:
    """Seed every generator we use. Call this before anything stochastic.

    Returns the seed so it can be printed or logged - a run whose seed is not
    recorded is not reproducible, even if it was seeded.
    """
    random.seed(seed)
    np.random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    return seed


def load_raw(**kwargs) -> pd.DataFrame:
    """Load the pinned snapshot exactly as published - no cleaning, no coercion.

    Anything that looks wrong in the result is genuinely in the source file and
    is yours to deal with. ``low_memory=False`` only silences a chunked-inference
    warning; it changes no values.
    """
    if not PATHS.snapshot.exists():
        raise FileNotFoundError(
            f"Snapshot not found at {PATHS.snapshot}.\n"
            "Run tools/check_setup.py to diagnose your installation."
        )
    kwargs.setdefault("low_memory", False)
    return pd.read_csv(PATHS.snapshot, **kwargs)


def split_by_host(
    df: pd.DataFrame,
    test_size: float = 0.2,
    seed: int = SEED,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Split so that no host appears in both halves.

    Written together in Session 2. It lives here so that every notebook and every
    student gets the *identical* split - otherwise milestone results are not
    comparable and the Session 12 reveal means nothing.

    Note the test fraction comes out near, not exactly, ``test_size``: whole hosts
    move together, and one host owns 588 listings. Asking for 20% yields 17.4%.
    """
    from sklearn.model_selection import GroupShuffleSplit

    splitter = GroupShuffleSplit(n_splits=1, test_size=test_size, random_state=seed)
    train_idx, test_idx = next(splitter.split(df, groups=df["host_id"]))
    train, test = df.iloc[train_idx].copy(), df.iloc[test_idx].copy()

    overlap = set(train["host_id"]) & set(test["host_id"])
    if overlap:  # a guard, not a formality: this invariant is the whole point
        raise AssertionError(f"{len(overlap)} hosts appear in both halves")
    return train, test


def describe_environment() -> pd.DataFrame:
    """Versions of everything that can change a numeric result."""
    import sklearn

    rows = [("python", ".".join(map(str, __import__("sys").version_info[:3])))]
    for mod in (np, pd, sklearn):
        rows.append((mod.__name__, mod.__version__))
    return pd.DataFrame(rows, columns=["package", "version"])
