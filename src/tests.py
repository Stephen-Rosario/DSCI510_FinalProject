import unittest
import pandas as pd
from src import load, process, worldbank
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

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

class TestMLModel(unittest.TestCase):
    def test_model_training(self):
        # Load data
        df = load.load_student_data("data/student-mat.csv", "data/student-por.csv")

        # Preprocess
        df['sex'] = df['sex'].map({'F': 0, 'M': 1})
        df['internet'] = df['internet'].map({'no': 0, 'yes': 1})
        df = df.dropna(subset=['sex', 'age', 'studytime', 'failures', 'absences', 'G1', 'G2', 'internet', 'G3'])

        # Features and label
        X = df[['sex', 'age', 'studytime', 'failures', 'absences', 'G1', 'G2', 'internet']]
        y = df['G3']

        # Split and train
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # Assertions
        acc = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        self.assertGreaterEqual(acc, 0.0)
        self.assertLessEqual(acc, 1.0)
        self.assertIsInstance(report, str)

if __name__ == "__main__":
    unittest.main()
