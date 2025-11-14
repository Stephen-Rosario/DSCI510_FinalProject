import os
import pandas as pd
from load import load_student_data
from worldbank import fetch_indicator
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def train_model(data):
    # Select relevant numeric and categorical columns
    feature_cols = ['sex', 'age', 'studytime', 'failures', 'absences', 'G1', 'G2', 'internet']
    df = data.copy()
    
    # Encode categorical variables
    df['sex'] = df['sex'].map({'F': 0, 'M': 1})
    df['internet'] = df['internet'].map({'no': 0, 'yes': 1})

    # Drop rows with missing or invalid values
    df = df.dropna(subset=feature_cols + ['G3'])

    X = df[feature_cols]
    y = df['G3']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    return acc, report

def main():
    data_dir = os.path.join("data")
    os.makedirs(data_dir, exist_ok=True)

    math_path = os.path.join(data_dir, "student-mat.csv")
    por_path = os.path.join(data_dir, "student-por.csv")

    print("Loading student data...")
    students = load_student_data(math_path, por_path)
    print(f"Loaded {students.shape[0]} rows and {students.shape[1]} columns")
    print(students.head())

    print("\nFetching macro-level education data...")
    gov_spend = fetch_indicator("SE.XPD.TOTL.GD.ZS")  # Government spending
    enroll_rate = fetch_indicator("SE.TER.ENRR")      # Tertiary enrollment

    print("\nGovernment Spending Data:")
    print(gov_spend.head())

    print("\nEnrollment Rate Data:")
    print(enroll_rate.head())

    # Save fetched data
    gov_spend.to_csv(os.path.join(data_dir, "government_spending.csv"))
    enroll_rate.to_csv(os.path.join(data_dir, "enrollment_rate.csv"))
    print("\nSaved World Bank data to CSV files.")

    # Train and evaluate model
    print("\nTraining model to predict G3 (final grade)...")
    accuracy, class_report = train_model(students)
    print(f"\nModel Accuracy: {accuracy:.2f}")
    print("\nClassification Report:")
    print(class_report)

if __name__ == "__main__":
    main()

