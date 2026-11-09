from sklearn.linear_model import LogisticRegression
import math
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


model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)


y_pred = model.predict(X_test)


print("Model Evaluation Results")

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, zero_division=0))
print("Recall:", recall_score(y_test, y_pred, zero_division=0))
print("F1 Score:", f1_score(y_test, y_pred, zero_division=0))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


plot_confusion_matrix(y_test, y_pred)
print("\n--- URL TESTING ---")

url = input("Enter a URL: ")

url_length = len(url)
num_dots = url.count(".")
has_https = 1 if url.startswith("https") else 0

num_subdirs = url.count("/") - 2
num_params = url.count("&") + (1 if "?" in url else 0)

suspicious_words = 0

words = ["login", "verify", "update", "secure", "password"]

for word in words:
    if word in url.lower():
        suspicious_words += 1

hostname = url.split("://")[-1].split("/")[0]
tld = hostname.split(".")[-1]

has_ip = 0

if hostname.replace(".", "").isdigit():
    has_ip = 1

special_char_count = 0
digits_count = 0

for char in url:
    if not char.isalnum():
        special_char_count += 1
    if char.isdigit():
        digits_count += 1

entropy = 0

for char in set(url):
    probability = url.count(char) / len(url)
    entropy = entropy - probability * math.log2(probability)
url_data = pd.DataFrame([{
    "url_length": url_length,
    "num_dots": num_dots,
    "has_https": has_https,
    "has_ip": has_ip,
    "num_subdirs": num_subdirs,
    "num_params": num_params,
    "suspicious_words": suspicious_words,
    "special_char_count": special_char_count,
    "digits_count": digits_count,
    "entropy": entropy,
    "tld": tld
}])


url_data = pd.get_dummies(url_data, columns=["tld"], dtype=int)

url_data = url_data.reindex(columns=feature_columns, fill_value=0)

url_data = scaler.transform(url_data)

result = model.predict(url_data)
print(url_data)

if result[0] == 1:
    print("This URL is Phishing")
else:
    print("This URL is Benign")
print("\n--- URL TESTING ---")

url = input("Enter a URL: ")

url_length = len(url)
num_dots = url.count(".")
has_https = 1 if url.startswith("https") else 0

num_subdirs = url.count("/") - 2
num_params = url.count("&") + (1 if "?" in url else 0)

suspicious_words = 0

words = ["login", "verify", "update", "secure", "password"]

for word in words:
    if word in url.lower():
        suspicious_words += 1
        hostname = url.split("://")[-1].split("/")[0]
tld = hostname.split(".")[-1]

has_ip = 0

if hostname.replace(".", "").isdigit():
    has_ip = 1

special_char_count = 0
digits_count = 0

for char in url:
    if not char.isalnum():
        special_char_count += 1
    if char.isdigit():
        digits_count += 1

entropy = 0

for char in set(url):
    probability = url.count(char) / len(url)
    entropy = entropy - probability * math.log2(probability)
    url_data = pd.DataFrame([{
    "url_length": url_length,
    "num_dots": num_dots,
    "has_https": has_https,
    "has_ip": has_ip,
    "num_subdirs": num_subdirs,
    "num_params": num_params,
    "suspicious_words": suspicious_words,
    "special_char_count": special_char_count,
    "digits_count": digits_count,
    "entropy": entropy,
    "tld": tld
}])


url_data = pd.get_dummies(url_data, columns=["tld"], dtype=int)

url_data = url_data.reindex(columns=feature_columns, fill_value=0)

url_data = scaler.transform(url_data)

result = model.predict(url_data)
print(url_data)

if result[0] == 1:
    print("This URL is Phishing")
else:
    print("This URL is Benign")
