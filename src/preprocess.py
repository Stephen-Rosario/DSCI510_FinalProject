import pandas as pd

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize column names and remove whitespace."""
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower()
    return df

def encode_categoricals(df: pd.DataFrame, categorical_cols=None) -> pd.DataFrame:
    """Convert categorical columns into numeric codes."""
    df = df.copy()
    if categorical_cols is None:
        categorical_cols = df.select_dtypes(include=["object"]).columns

    for col in categorical_cols:
        df[col] = df[col].astype("category").cat.codes

    return df

def create_target_variable(df: pd.DataFrame) -> pd.DataFrame:
    """Create a performance category: poor, average, excellent."""
    df = df.copy()

    # Using G3 (final grade) for the target category
    df["performance"] = pd.cut(
        df["g3"],
        bins=[-1, 10, 15, 20],
        labels=["poor", "average", "excellent"]
    )

    return df

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """Pipeline wrapper for all preprocessing steps."""
    df = clean_column_names(df)
    df = encode_categoricals(df)
    df = create_target_variable(df)
    return df
