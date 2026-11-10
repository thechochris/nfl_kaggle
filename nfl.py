from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parent / "spreadspoke_scores.csv"


def load_scores() -> pd.DataFrame:
    """Load the NFL game score dataset from the project directory."""
    return pd.read_csv(DATA_PATH)


__all__ = ["load_scores"]