import pandas as pd
from io import StringIO

def load_student_data(math_path, por_path):
    # Helper function to clean and parse CSV files
    def clean_and_parse(path):
        # Open the file and remove all double quotes from each line
        with open(path, encoding="utf-8") as f:
            lines = [line.replace('"', '') for line in f]
        # Use StringIO to read the cleaned text into a DataFrame with semicolon delimiters
        df = pd.read_csv(StringIO(''.join(lines)), sep=";")
        return df

    # Load and clean both math and Portuguese student datasets
    math = clean_and_parse(math_path)
    por = clean_and_parse(por_path)

    # Print loaded record summaries for each dataset
    print(f"Loaded {len(math)} math records with {len(math.columns)} columns")
    print(f"Loaded {len(por)} portuguese records with {len(por.columns)} columns")

    # Add a 'subject' column to differentiate the two datasets
    math["subject"] = "math"
    por["subject"] = "portuguese"

    # Combine the two datasets into one unified DataFrame
    students = pd.concat([math, por], ignore_index=True)

    # Print the total combined dataset shape
    print(f"Loaded {len(students)} rows and {len(students.columns)} columns")
    return students

