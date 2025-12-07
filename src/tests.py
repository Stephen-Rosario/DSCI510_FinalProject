import unittest
from src.load_data import load_student_data
from src.preprocess import preprocess
from src.model import split_data, train_model
import pandas as pd

class TestProject(unittest.TestCase):

    def test_load_data(self):
        df = load_student_data()
        self.assertFalse(df.empty)
        self.assertIn("G3".lower(), df.columns)

    def test_preprocess(self):
        df = load_student_data()
        df = preprocess(df)
        self.assertIn("performance", df.columns)

    def test_split_data(self):
        df = preprocess(load_student_data())
        X_train, X_test, y_train, y_test = split_data(df, target="performance")
        self.assertGreater(len(X_train), 0)
        self.assertGreater(len(X_test), 0)

    def test_train_model(self):
        df = preprocess(load_student_data())
        X_train, X_test, y_train, y_test = split_data(df, "performance")
        model = train_model(X_train, y_train, use_gridsearch=False)
        preds = model.predict(X_test)
        self.assertEqual(len(preds), len(y_test))

if __name__ == "__main__":
    unittest.main()

