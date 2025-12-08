from pathlib import Path

from .load_data import load_student_data
from .preprocess import preprocess_data
from .worldbank import fetch_worldbank_data, merge_macro_features
from .model import split_data, train_model, evaluate_model
from .analysis import (
    plot_grade_distribution,
    plot_studytime,
    correlation_heatmap,
    internet_ttest,
)


def ensure_results_dir(path: str = "results"):
    """Ensure results directory exists."""
    Path(path).mkdir(parents=True, exist_ok=True)


def run_pipeline():
    print("=== Student Performance Pipeline ===")

    # Ensure results folder exists
    ensure_results_dir()

    # 1. Load UCI Data
    print("Loading UCI student datasets...")
    df = load_student_data()
    print(f"Loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns.")

    # 2. Preprocess data
    print("Preprocessing data...")
    df = preprocess_data(df)

    # 3. World Bank Data
    print("Fetching macro indicators from the World Bank API...")
    macro_df = fetch_worldbank_data()
    df = merge_macro_features(df, macro_df)
    print("World Bank macro features merged into dataset.")

    # 4. Modeling Pipeline
    print("Splitting data and training model...")
    X_train, X_test, y_train, y_test = split_data(df, target="performance")

    model = train_model(
        X_train,
        y_train,
        use_gridsearch=True,  # enables extra credit
    )

    print("Evaluating model...")
    accuracy, confusion, report = evaluate_model(model, X_test, y_test)

    print(f"\nMODEL ACCURACY: {accuracy:.4f}")
    print("\nClassification Report:")
    print(report)
    print("\nConfusion Matrix:")
    print(confusion)

    # 5. Analysis + Plots
    print("Generating visualizations...")
    plot_grade_distribution(df)
    plot_studytime(df)
    correlation_heatmap(df)

    print("Running t-test (Internet vs. No Internet)...")
    t_stat, p_val = internet_ttest(df)
    print(f"T-Test → t={t_stat:.4f}, p={p_val:.4f}")

    print("\nPipeline complete. All plots saved to the 'results' folder.\n")
