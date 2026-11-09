import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


df = pd.read_csv("phishing_features.csv")
df = df.drop_duplicates()
df = df.dropna(subset=["label"])

numerical_columns = [
    "url_length",
    "num_dots",
    "has_https",
    "has_ip",
    "num_subdirs",
    "num_params",
    "suspicious_words"
]
for column in numerical_columns:
    df[column] = df[column].fillna(df[column].median())

df["tld"] = df["tld"].fillna(df["tld"].mode()[0])
df = df.drop("url", axis=1)
df = pd.get_dummies(df, columns=["tld"], drop_first=True, dtype=int)

X = df.drop("label", axis=1)
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
feature_columns = X.columns
