import pandas as pd
from io import StringIO

def load_student_data(math_path, por_path):
    # Clean quotes and parse with semicolon delimiter
    def clean_and_parse(path):
        with open(path, encoding="utf-8") as f:
            lines = [line.replace('"', '') for line in f]
        df = pd.read_csv(StringIO(''.join(lines)), sep=";")
        return df

    math = clean_and_parse(math_path)
    por = clean_and_parse(por_path)

    print(f"Loaded {len(math)} math records with {len(math.columns)} columns")
    print(f"Loaded {len(por)} portuguese records with {len(por.columns)} columns")

    math["subject"] = "math"
    por["subject"] = "portuguese"
    students = pd.concat([math, por], ignore_index=True)

    print(f"Loaded {len(students)} rows and {len(students.columns)} columns")
    return students
