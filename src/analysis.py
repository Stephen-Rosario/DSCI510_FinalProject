"""
analysis.py

Visualization and statistical analysis helpers:
- grade distribution
- correlation heatmap
- study time vs. final grade boxplot
- two-sample t-test (Internet vs. No Internet)
"""

from __future__ import annotations

from pathlib import Path
from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats

from .config import (
    RESULTS_DIR,
    CORRELATION_HEATMAP_FILE,
    GRADE_DISTRIBUTION_FILE,
    STUDYTIME_BOXPLOT_FILE,
)

# Ensure results directory exists
PLOT_DIR = Path(RESULTS_DIR)
PLOT_DIR.mkdir(parents=True, exist_ok=True)


# -------------------------------------------------------------------
# Visualization helpers
# -------------------------------------------------------------------
def plot_grade_distribution(df: pd.DataFrame) -> None:
    """Histogram of final grades (G3)."""
    plt.figure(figsize=(8, 5))
    sns.histplot(df["G3"], bins=10, kde=False)
    plt.title("Final Grade Distribution (G3)")
    plt.xlabel("Final Grade (G3)")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(PLOT_DIR / GRADE_DISTRIBUTION_FILE, bbox_inches="tight")
    plt.close()


def plot_correlation_heatmap(df: pd.DataFrame) -> None:
    """Correlation heatmap for numeric features including G3."""
    numeric_df = df.select_dtypes(include=[np.number])

    plt.figure(figsize=(10, 8))
    corr = numeric_df.corr()
    sns.heatmap(corr, cmap="coolwarm", annot=False)
    plt.title("Correlation Heatmap (Numeric Features)")
    plt.tight_layout()
    plt.savefig(PLOT_DIR / CORRELATION_HEATMAP_FILE, bbox_inches="tight")
    plt.close()


def plot_studytime_boxplot(df: pd.DataFrame) -> None:
    """Boxplot of final grade by study time group."""
    plt.figure(figsize=(8, 5))
    sns.boxplot(x="studytime", y="G3", data=df)
    plt.title("Final Grade vs. Weekly Study Time")
    plt.xlabel("Study Time (1–4)")
    plt.ylabel("Final Grade (G3)")
    plt.tight_layout()
    plt.savefig(PLOT_DIR / STUDYTIME_BOXPLOT_FILE, bbox_inches="tight")
    plt.close()


def generate_plots(df: pd.DataFrame) -> None:
    """
    Run all visualizations. This is what main.py calls when it prints
    'Generating visualizations...'.
    """
    plot_grade_distribution(df)
    plot_correlation_heatmap(df)
    plot_studytime_boxplot(df)


# -------------------------------------------------------------------
# Statistical test
# -------------------------------------------------------------------
def compute_ttest(df: pd.DataFrame) -> Tuple[float, float]:
    """
    Two-sample t-test comparing final grade (G3) for students
    with Internet access vs. no Internet.

    Parameters
    ----------
    df : pandas.DataFrame
        Preprocessed dataset that still contains an 'internet' column and
        the original 'G3' final grade.

    Returns
    -------
    t_stat : float
        t-statistic for the two-sample test.
    p_value : float
        Two-sided p-value.
    """
    if "internet" not in df.columns or "G3" not in df.columns:
        raise ValueError("Expected 'internet' and 'G3' columns in dataframe.")

    internet_yes = df.loc[df["internet"] == "yes", "G3"]
    internet_no = df.loc[df["internet"] == "no", "G3"]

    # Drop missing just in case
    internet_yes = internet_yes.dropna()
    internet_no = internet_no.dropna()

    t_stat, p_value = stats.ttest_ind(internet_yes, internet_no, equal_var=False)

    return float(t_stat), float(p_value)

