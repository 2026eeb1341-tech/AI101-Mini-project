# PROJECT_ARCHITECTURE:

## overview:
The project classifies URLs as phishing (label `1`) or benign (label `0`) using a Logistic Regression model trained on pre-extracted URL features.

## Processing flow:

### 1. Dataset (phishing_features.csv):
  ** The dataset is stored in a CSV file named phishing_features.csv.
  ** It contains different features extracted from URLs.
  ** These features help identify the characteristics of legitimate and phishing websites.
  ** Each row represents a URL and its corresponding features.
  ** The target column contains the class label.
  ** The label indicates whether the URL is legitimate or phishing.
  ** This dataset is used to train and test our machine learning model.

### Preprocessing (preprocessing.py):
  ** First, the program loads the dataset using the Pandas library.
  ** It checks the dataset for duplicate records.
  ** Duplicate rows are removed to avoid unnecessary repetition.
  ** Rows with missing target labels are also removed.
  ** Missing numerical values are filled using the median of their respective columns.
  ** Missing values in the TLD (Top-Level Domain) feature are filled using the most frequently occurring value, known as the mode.
  ** The raw URL column is removed because the model works with extracted numerical and categorical features.
  ** The TLD feature is converted into numerical form using One-Hot Encoding.
  ** This allows the machine learning model to process different domain extensions.
  ** Next, the dataset is divided into training and testing sets.
  ** We use an 80:20 split, where 80% of the data is used for training and 20% for testing.
  ** Stratified splitting is applied to maintain the same proportion of phishing and legitimate URLs in both sets.
  ** After splitting, we apply StandardScaler to normalize the numerical features.
  ** The scaler is fitted only on the training data.
  ** The same fitted scaler is then applied to both training and testing data.
  ** Finally, the preprocessed data is made ready for model training and evaluation.
  




