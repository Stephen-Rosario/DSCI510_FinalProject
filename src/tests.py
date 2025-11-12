import unittest
from worldbank import get_world_bank_indicator

class TestWorldBankAPI(unittest.TestCase):

    def test_education_spending_data(self):
        df = get_world_bank_indicator("PRT", "SE.XPD.TOTL.GD.ZS", 2010, 2023)
        self.assertFalse(df.empty, "Education spending data should not be empty.")
        self.assertIn("year", df.columns)
        self.assertIn("value", df.columns)

    def test_tertiary_enrollment_data(self):
        df = get_world_bank_indicator("PRT", "SE.TER.ENRR", 2010, 2023)
        self.assertFalse(df.empty, "Tertiary enrollment data should not be empty.")
        self.assertIn("year", df.columns)
        self.assertIn("value", df.columns)

if __name__ == "__main__":
    unittest.main()
