import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

def plot_confusion_matrix(y_test, y_pred):

    cm = confusion_matrix(y_test, y_pred)

    cm_df = pd.DataFrame(cm, index=["Actual Benign", "Actual Phishing"], columns=["Predicted Benign", "Predicted Phishing"])

    print("\nConfusion Matrix:")
    print(cm_df)

    cm_df.plot(kind="bar", figsize=(8, 5))

    plt.title("Phishing URL Detection ")
    plt.xlabel("Actual Class")
    plt.ylabel("Number of Predictions")
    plt.legend(title="Predicted Class")

    plt.show()
