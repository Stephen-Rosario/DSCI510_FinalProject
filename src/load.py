import pandas as pd

def load_student_data(math_path: str, por_path: str) -> pd.DataFrame:
    # Load the CSVs
    math = pd.read_csv(math_path, sep=";")
    por = pd.read_csv(por_path, sep=";")
    
    # Add subject labels
    math["subject"] = "math"
    por["subject"] = "Portuguese"

    # Combine datasets
    combined = pd.concat([math, por], ignore_index=True)

    return combined
