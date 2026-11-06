from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

from preprocessing import X_train, X_test, y_train, y_test
from plots import plot_confusion_matrix

# Train the model
model = LogisticRegression(max_iter=1000)

model.fit(X_test, y_train)  # Error 1

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("Model Evaluation Results")

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, zero_division=0))
print("Recall:", recall_score(y_test, y_pred, zero_division=0))
print("F1 Score:", f1_score(y_test, y_pred, zero_division=0))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Display confusion matrix
plot_confusion_matrix(y_train, y_pred)  # Error 2
