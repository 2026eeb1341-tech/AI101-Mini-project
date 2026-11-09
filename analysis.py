
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("phishing_features.csv")
print("Dataset Shape:", df.shape)

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())
print("\nLabel Distribution:")
print(df["label"].value_counts())

df["label"].value_counts().plot(kind="bar")

plt.title("Benign vs Phishing URLs")
plt.xlabel("Label (0 = Benign, 1 = Phishing)")
plt.ylabel("Number of URLs")
plt.xticks(rotation=0)
plt.show()

# help taken from AI for this part
correlation = df.select_dtypes(include=["int64", "float64"]).corr()

plt.figure(figsize=(10, 7))
plt.imshow(correlation, cmap="coolwarm")
plt.colorbar()

plt.xticks(range(len(correlation.columns)),
           correlation.columns, rotation=90)
plt.yticks(range(len(correlation.columns)),
           correlation.columns)

plt.title("Feature Correlation Heatmap")
plt.tight_layout()
plt.show()

print("\nAnalysis Completed!")
