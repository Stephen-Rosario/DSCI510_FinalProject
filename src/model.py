"""
model.py
Provides functions for splitting data, training the machine learning model,
and producing evaluation outputs.
"""

from typing import Tuple

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.base import ClassifierMixin


def train_test_split_and_train(
    df: pd.DataFrame,
) -> Tuple[ClassifierMixin, pd.DataFrame, pd.Series, pd.Series]:
    """
    Split data into train/test sets, train a RandomForest model,
    and return model + X_test + y_test + predictions.

    Parameters
    ----------
    df : pandas.DataFrame
        Preprocessed dataset including the target column "performance".

    Returns
    -------
    model : RandomForestClassifier
        Trained model.
    X_test : pandas.DataFrame
        Test features.
    y_test : pandas.Series
        True test labels.
    y_pred : pandas.Series
        Predictions for the test set.
    """

    # Ensure target column exists
    if "performance" not in df.columns:
        raise ValueError("Expected target column 'performance' not found in dataframe.")

    # Features and target
    X = df.drop(columns=["performance"])
    y = df["performance"]

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    # Train the model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Predictions as a pandas Series for compatibility with tests
    y_pred = pd.Series(model.predict(X_test), index=y_test.index)

    return model, X_test, y_test, y_pred
