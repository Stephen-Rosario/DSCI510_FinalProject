import os
from src.load import load_student_data
# from src.worldbank import fetch_indicator 

def main():
    data_dir = os.path.join("data")
    math_path = os.path.join(data_dir, "student-mat.csv")
    por_path = os.path.join(data_dir, "student-por.csv")

    print("Loading student data...")
    students = load_student_data(math_path, por_path)
    print(f"Loaded {students.shape[0]} rows and {students.shape[1]} columns")


    print(students.head())

if __name__ == "__main__":
    main()
