import pandas as pd

def clean_column_names(df):
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower()
    return df

def encode_categoricals(df):
    df = df.copy()
    cat_cols = df.select_dtypes(include=["object"]).columns
    for col in cat_cols:
        df[col] = df[col].astype("category").cat.codes
    return df

def create_target_variable(df):
    df = df.copy()
    df["performance"] = pd.cut(
        df["g3"],
        bins=[-1, 10, 15, 20],
        labels=["poor", "average", "excellent"]
    )
    return df

def preprocess(df):
    df = clean_column_names(df)
    df = encode_categoricals(df)
    df = create_target_variable(df)
    return df

