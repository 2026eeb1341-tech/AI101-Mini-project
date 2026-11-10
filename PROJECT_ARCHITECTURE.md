# PROJECT_ARCHITECTURE:

## overview:
The project classifies URLs as phishing (label `1`) or benign (label `0`) using a Logistic Regression model trained on pre-extracted URL features.

## Processing flow:

### 1. Dataset (phishing_features.csv):
1) The dataset is stored in a CSV file named phishing_features.csv.
2) It contains different features extracted from URLs.
3) These features help identify the characteristics of legitimate and phishing websites.
4) Each row represents a URL and its corresponding features.
5) The target column contains the class label.
6) The label indicates whether the URL is legitimate or phishing.
7) This dataset is used to train and test our machine learning model.

### Preprocessing (preprocessing.py):
1) First, the program loads the dataset using the Pandas library.
2) It checks the dataset for duplicate records.
3) Duplicate rows are removed to avoid unnecessary repetition.
4) Rows with missing target labels are also removed.
5) Missing numerical values are filled using the median of their respective columns.
6) Missing values in the TLD (Top-Level Domain) feature are filled using the most frequently occurring value, known as the mode.
7) The raw URL column is removed because the model works with extracted numerical and categorical features.
8) The TLD feature is converted into numerical form using One-Hot Encoding.
9) This allows the machine learning model to process different domain extensions.
10) Next, the dataset is divided into training and testing sets.
11) We use an 80:20 split, where 80% of the data is used for training and 20% for testing.
12) Stratified splitting is applied to maintain the same proportion of phishing and legitimate URLs in both sets.
13) After splitting, we apply StandardScaler to normalize the numerical features.
14) The scaler is fitted only on the training data.
15) The same fitted scaler is then applied to both training and testing data.
16) Finally, the preprocessed data is made ready for model training and evaluation.
  




