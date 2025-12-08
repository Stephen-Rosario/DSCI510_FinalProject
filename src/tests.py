"""
tests.py

Unit tests for the DSCI510 Final Project pipeline.
This file checks:
- Data loading
- Preprocessing
- Model training pipeline
- End-to-end execution
"""

import unittest
import pandas as pd
import numpy as np

from src.load_data import load_student_data
from src.preprocess import preprocess_data
from src.model import train_test_split_and_train


class TestProject(unittest.TestCase):

    # ------------------------------------------------------------
    # Test 1: Data Loading
    # ------------------------------------------------------------
    def test_load_data(self):
        """Test that the UCI student dataset loads and contains expected columns."""
        df = load_student_data()

        # Must be a DataFrame
        self.assertIsInstance(df, pd.DataFrame)

        # Required columns (minimal expected subset)
        expected_cols = {"G1", "G2", "G3"}
        self.assertTrue(
            expected_cols.issubset(set(df.columns)),
            f"Missing expected grade columns: {expected_cols}"
        )

        # Should not be empty
        self.assertGreater(len(df), 0, "Loaded dataframe is empty")

    # ------------------------------------------------------------
    # Test 2: Preprocessing
    # ------------------------------------------------------------
    def test_preprocess(self):
        """Ensure preprocessing adds 'performance' and produces numeric model-ready data."""
        df = load_student_data()
        processed = preprocess_data(df)

        # Must contain performance column
        self.assertIn("performance", processed.columns)

        # Remove performance col to verify numeric transforms
        features_only = processed.drop(columns=["performance"])

        # Ensure all feature columns are numeric
        self.assertTrue(
            all(np.issubdtype(dtype, np.number) for dtype in features_only.dtypes),
            "Non-numeric values remain after preprocessing"
        )

        # Should not be empty
        self.assertGreater(len(processed), 0)

    # ------------------------------------------------------------
    # Test 3: Model Training
    # ------------------------------------------------------------
    def test_model_training(self):
        """Ensure model trains and returns required elements."""
        df = load_student_data()
        df = preprocess_data(df)

        model, X_test, y_test, y_pred = train_test_split_and_train(df)

        # Types
        self.assertIsNotNone(model)
        self.assertIsInstance(X_test, pd.DataFrame)
        self.assertIsInstance(y_test, pd.Series)

        # Predictions must match test-set length
        self.assertEqual(len(y_pred), len(y_test))

        # Predictions must be valid labels
        valid_labels = {"poor", "average", "excellent"}
        self.assertTrue(
            set(y_pred).issubset(valid_labels),
            f"Predictions include invalid labels: {set(y_pred)}"
        )

    # ------------------------------------------------------------
    # Test 4: End-to-End Pipeline
    # ------------------------------------------------------------
    def test_pipeline_end_to_end(self):
        """End-to-end test: load → preprocess → train → predict."""
        df = load_student_data()
        df = preprocess_data(df)
        model, X_test, y_test, y_pred = train_test_split_and_train(df)

        # Basic pipeline integrity checks
        self.assertGreater(len(df), 0)
        self.assertGreater(len(X_test), 0)
        self.assertEqual(len(y_pred), len(y_test))


if __name__ == "__main__":
    unittest.main()
