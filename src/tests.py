import unittest
from src import load, process, worldbank
import pandas as pd


class TestLoadFunctions(unittest.TestCase):

    def test_load_student_data(self):
        math_path = "data/student-mat.csv"
        por_path = "data/student-por.csv"
        df = load.load_student_data(math_path, por_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)
        self.assertIn("subject", df.columns)

class TestProcessFunctions(unittest.TestCase):

    def test_categorize_final_grade(self):
        self.assertEqual(process.categorize_final_grade(15), "excellent")
        self.assertEqual(process.categorize_final_grade(10), "average")
        self.assertEqual(process.categorize_final_grade(5), "poor")

class TestWorldBankFunctions(unittest.TestCase):

    def test_fetch_indicator(self):
        df = worldbank.fetch_indicator("SE.XPD.TOTL.GD.ZS", country="PT", start=2010, end=2020)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIn("year", df.columns)
        self.assertIn("value", df.columns)


if __name__ == "__main__":
    unittest.main()
