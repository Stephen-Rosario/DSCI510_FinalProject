import os
from load import load_student_data
from worldbank import fetch_indicator

def main():
    # Load student data
    data_dir = os.path.join("data")
    math_path = os.path.join(data_dir, "student-mat.csv")
    por_path = os.path.join(data_dir, "student-por.csv")

    print("Loading student data...")
    students = load_student_data(math_path, por_path)
    print(f"Loaded {students.shape[0]} rows and {students.shape[1]} columns")

    # Preview the data
    print(students.head())

    # Fetch World Bank indicators
    print("\nFetching macro-level education data...")
    gov_spend = fetch_indicator("SE.XPD.TOTL.GD.ZS")  # Gov spending
    enroll_rate = fetch_indicator("SE.TER.ENRR")      # Tertiary enrollment

    print("\nGovernment Spending Data:")
    print(gov_spend.head())

    print("\nEnrollment Rate Data:")
    print(enroll_rate.head())

if __name__ == "__main__":
    main()

