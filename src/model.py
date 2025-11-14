# src/model.py
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def train_random_forest(data, target="G3"):
    # Drop rows with missing values
    data = data.dropna(subset=[target])

    # Features to use (drop non-predictive or post-outcome columns)
    features = data.drop(columns=["G1", "G2", "G3", "subject"])
    features = pd.get_dummies(features, drop_first=True)

    # Labels
    labels = data[target]

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

    # Model
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Metrics
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    r2 = r2_score(y_test, y_pred)

    return model, rmse, r2
