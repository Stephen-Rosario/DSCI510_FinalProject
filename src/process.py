from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Categorizes the final grade into three performance tiers
def categorize_final_grade(grade):
    if grade >= 15:
        return "excellent"  # High-performing students
    elif grade >= 10:
        return "average"    # Mid-performing students
    else:
        return "poor"       # Low-performing students

# Trains a Random Forest model and evaluates its performance
def train_model(X_train, X_test, y_train, y_test):
    # Initialize the classifier
    model = RandomForestClassifier(random_state=42)
    
    # Fit the model to the training data
    model.fit(X_train, y_train)
    
    # Predict labels on the test set
    y_pred = model.predict(X_test)
    
    # Generate a detailed classification report
    report = classification_report(y_test, y_pred)
    
    # Compute overall accuracy
    accuracy = accuracy_score(y_test, y_pred)
    
    # Return the model and evaluation metrics
    return model, report, accuracy


