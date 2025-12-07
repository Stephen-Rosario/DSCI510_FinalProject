import unittest
import pandas as pd

from src.load_data import load_student_data
from src.preprocess import preprocess_data
from src.model import train_model
from src.analysis import compute_ttest


class TestProject(unittest.TestCase):

    def test_load_data(self):
        """Test that the UCI dataset loads and contains expected columns."""
        df = load_student_data()

        # Basic checks
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)

        # Case-insensitive column check
        cols_lower = [col.lower() for col in df.columns]
        self.assertIn("g3", cols_lower)
        self.assertIn("internet", cols_lower)

    def test_preprocess_data(self):
        """Ensure preprocess removes NA and creates proper output."""
        df = load_student_data()
        processed = preprocess_data(df)

        self.assertGreater(len(processed), 0)
        self.assertNotIn(processed.isna().sum().sum(), [None, float("nan")])
        self.assertIn("G3", processed.columns)  # original case preserved

    def test_train_model(self):
        """Train a model and ensure accuracy metric is returned."""
        df = load_student_data()
        df = preprocess_data(df)

        model, X_test, y_test, accuracy = train_model(df)

        self.assertIsNotNone(model)
        self.assertIsInstance(accuracy, float)
        self.assertGreaterEqual(accuracy, 0.0)
        self.assertLessEqual(accuracy, 1.0)

    def test_ttest(self):
        """Check t-test output structure."""
        df = load_student_data()
        df = preprocess_data(df)

        t_stat, p_value = compute_ttest(df)

        self.assertIsInstance(t_stat, float)
        self.assertIsInstance(p_value, float)


if __name__ == "__main__":
    unittest.main()

