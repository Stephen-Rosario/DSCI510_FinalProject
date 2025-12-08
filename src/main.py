"""
main.py
Runs the full DSCI510 Final Project pipeline:
1. Load data
2. Preprocess data
3. Train model and evaluate
4. Run statistical analysis (t-test)
5. Save plots and print results
"""

import pandas as pd

from src.load_data import load_student_data
from src.preprocess import preprocess_data
from src.model import train_test_split_and_train
from src.analysis import run_t_test   # or compute_ttest if you renamed it
from src.analysis import create_all_plots


def run_pipeline():
    print("=== Student Performance Pipeline ===")

    # ------------------------------------------------------------
    # 1. Load raw data
    # ------------------------------------------------------------
    print("Loading UCI student datasets...")
    df = load_student_data()
    print(f"Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns.")

    # ------------------------------------------------------------
    # 2. Preprocess data
    # ------------------------------------------------------------
    print("Preprocessing data...")
    df_processed = preprocess_data(df)

    # ------------------------------------------------------------
    # 3. Train model
    # ------------------------------------------------------------
    print("Training model...")
    model, X_test, y_test, y_pred = train_test_split_and_train(df_processed)

    # Evaluate accuracy
    accuracy = (y_test == y_pred).mean()
    print(f"\nMODEL ACCURACY: {accuracy:.4f}\n")

    # ------------------------------------------------------------
    # 4. Statistical analysis
    # ------------------------------------------------------------
    print("Running t-test (Internet vs No Internet)...")
    t_stat, p_value = run_t_test(df_processed)
    print(f"T-Test → t={t_stat:.4f}, p={p_value:.4f}")

    # ------------------------------------------------------------
    # 5. Generate visualizations
    # ------------------------------------------------------------
    print("Generating visualizations...")
    create_all_plots(df_processed)

    print("Pipeline complete. All plots saved to the 'results' folder.")


if __name__ == "__main__":
    run_pipeline()

