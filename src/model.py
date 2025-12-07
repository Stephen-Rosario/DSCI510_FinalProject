# src/model.p
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def split_data(df: pd.DataFrame, target="performance"):
    X = df.drop(columns=[target])
    y = df[target]
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model(X_train, y_train, use_gridsearch=False):
    if use_gridsearch:
        params = {
            "n_estimators": [100, 200],
            "max_depth": [5, 10, None],
            "min_samples_split": [2, 5, 10],
        }
        grid = GridSearchCV(RandomForestClassifier(random_state=42), params, cv=3, n_jobs=-1)
        grid.fit(X_train, y_train)
        return grid.best_estimator_
    else:
        model = RandomForestClassifier(random_state=42)
        model.fit(X_train, y_train)
        return model

def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    report = classification_report(y_test, preds)
    cm = confusion_matrix(y_test, preds)
    return acc, report, cm

