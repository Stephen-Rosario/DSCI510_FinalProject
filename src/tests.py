"""
Basic unit tests for the DSCI 510 final project.

Run from the project root as:
    python -m src.tests
"""

import unittest
import pandas as pd

from src.load_data import load_student_data
from src.preprocess import preprocess_data
from src.model import train_test_split_and_train
from src.analysis import run_t_test


class TestProject(unittest.TestCase):

    # ------------------------------------------------------------
    # Test 1: Data Loading
    # ------------------------------------------------------------
    def test_load_data(self):
        """Test that the UCI dataset loads and contains expected columns."""
        df = load_student_data()

        # Basic checks
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)

        # Case-insensitive checks
        cols_lower = [c.lower() for c in df.columns]
        self.assertIn("g3", cols_lower)
        self.assertIn("internet", cols_lower)

    # ------------------------------------------------------------
    # Test 2: Preprocessing
    # ------------------------------------------------------------
    def test_preprocess(self):
        """Ensure preprocessing removes NA and produces numeric model-ready data."""
        df = load_student_data()
        processed = preprocess_data(df)

        self.assertGreater(len(processed), 0)
        self.assertEqual(processed.isna().sum().sum(), 0)
        self.assertIn("performance", processed.columns)

    # ------------------------------------------------------------
    # Test 3: Model Training
    # ------------------------------------------------------------
    def test_model_training(self):
        """Train a model and ensure predictions are generated."""
        df = load_student_data()
        df = preprocess_data(df)

        model, X_test, y_test, y_pred = train_test_split_and_train(df)

        self.assertIsNotNone(model)
        self.assertEqual(len(y_test), len(y_pred))

    # ------------------------------------------------------------
    # Test 4: T-Test Analysis
    # ------------------------------------------------------------
    def test_t_test_runs(self):
        """Check that t-test returns numeric t-statistic and p-value."""
        df = load_student_data()
        df = preprocess_data(df)

        t_stat, p_value = run_t_test(df)

        self.assertIsInstance(t_stat, float)
        self.assertIsInstance(p_value, float)


if __name__ == "__main__":
    unittest.main()
