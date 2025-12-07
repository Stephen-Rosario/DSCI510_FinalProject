"""
Basic unit tests for the DSCI 510 final project.

Run from the project root as:
    python -m src.tests
"""

import unittest

from src.load_data import load_student_data
from src.preprocess import preprocess
from src.model import train_test_split_and_train
from src.analysis import run_t_test


class TestProject(unittest.TestCase):
    def test_load_data(self):
        """Raw UCI data loads with expected shape and columns."""
        df = load_student_data()

        # UCI combined dataset should have 1044 rows
        self.assertEqual(df.shape[0], 1044)

        # Raw data should still have original 'G3' column name
        self.assertIn("G3", df.columns)

    def test_preprocess(self):
        """Preprocessing creates lower-case columns and a performance label."""
        df = load_student_data()
        processed = preprocess(df)

        # After preprocessing, columns are lower-case
        self.assertIn("g3", processed.columns)

        # New target label must exist
        self.assertIn("performance", processed.columns)

        # No missing labels
        self.assertFalse(processed["performance"].isna().any())

    def test_model_training(self):
        """Model training returns predictions of correct length."""
        df = preprocess(load_student_data())
        model, X_test, y_test, y_pred = train_test_split_and_train(df)

        # Predictions and true labels should be same length
        self.assertEqual(len(y_test), len(y_pred))

        # Sanity-check: accuracy is at least better than random
        acc = (y_test == y_pred).mean()
        self.assertGreaterEqual(acc, 0.5)

    def test_t_test_runs(self):
        """t-test helper returns numeric statistics."""
        df = preprocess(load_student_data())
        t_stat, p_value = run_t_test(df)

        self.assertIsInstance(t_stat, float)
        self.assertIsInstance(p_value, float)


if __name__ == "__main__":
    unittest.main()
