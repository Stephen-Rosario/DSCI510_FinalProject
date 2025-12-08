import pandas as pd


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the raw student dataframe and engineer features for modeling.

    Steps
    -----
    * drop duplicates
    * drop rows with missing final grade G3
    * create categorical target label 'performance' based on G3
    * remove grade columns G1, G2, G3 from features
    * one-hot encode categorical columns
    * fill any remaining NaNs with 0
    * return a model-ready DataFrame with numeric features + 'performance'
    """
    # Work on a copy to avoid mutating caller's data
    df = df.copy()

    # 1. Basic cleaning
    df = df.drop_duplicates()
    df = df.dropna(subset=["G3"])

    # 2. Create performance label from final grade G3
    def grade_to_label(g3):
        if g3 >= 15:
            return "excellent"
        elif g3 >= 10:
            return "average"
        else:
            return "poor"

    df["performance"] = df["G3"].apply(grade_to_label)

    # 3. Drop raw grade columns from features
    for col in ["G1", "G2", "G3"]:
        if col in df.columns:
            df = df.drop(columns=col)

    # 4. Separate target so we don't encode it
    y = df["performance"]
    X = df.drop(columns=["performance"])

    # 5. One-hot encode categorical columns (object / category)
    cat_cols = X.select_dtypes(include=["object", "category"]).columns.tolist()
    X_encoded = pd.get_dummies(
        X,
        columns=cat_cols,
        drop_first=True,
        dtype=int  # ensure numeric (no bools)
    )

    # 6. Handle any remaining missing values
    X_encoded = X_encoded.fillna(0)

    # 7. Combine features and target back together
    processed = X_encoded.copy()
    processed["performance"] = y.values

    return processed
