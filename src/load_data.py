"""
load_data.py

Functions for loading the UCI student performance datasets.
"""

from pathlib import Path
from typing import Optional

import pandas as pd

from .config import MAT_FILE, POR_FILE


def _ensure_file_exists(path: Path) -> None:
    """Raise a clear error if a required CSV is missing."""
    if not path.exists():
        raise FileNotFoundError(
            f"Required data file not found: {path}\n"
            "Place the original UCI CSVs in the local 'data/' folder "
            "(not tracked in git)."
        )


def load_student_data(
    math_path: Optional[Path] = None,
    por_path: Optional[Path] = None,
) -> pd.DataFrame:
    """
    Load and combine the student-mat.csv and student-por.csv datasets.

    Parameters
    ----------
    math_path : Path or None
        Optional override path for the math CSV. If None, MAT_FILE from
        config.py is used.
    por_path : Path or None
        Optional override path for the Portuguese CSV. If None, POR_FILE
        from config.py is used.

    Returns
    -------
    df : pandas.DataFrame
        Combined raw dataset with 1044 rows and 33 columns when using
        the original UCI CSVs.
    """
    mat_path = Path(math_path) if math_path is not None else MAT_FILE
    por_path = Path(por_path) if por_path is not None else POR_FILE

    _ensure_file_exists(mat_path)
    _ensure_file_exists(por_path)

    # UCI files are semicolon-separated
    df_mat = pd.read_csv(mat_path, sep=";")
    df_por = pd.read_csv(por_path, sep=";")

    # Simple row-wise concatenation – preserves original 33 columns
    df = pd.concat([df_mat, df_por], ignore_index=True)

    return df

