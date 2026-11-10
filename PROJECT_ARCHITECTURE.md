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



### 2. Preprocessing (preprocessing.py):
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


### 3. Training and Evaluation (main.py):
1) After preprocessing, we move to the machine learning model.

2) We use Logistic Regression as our classification algorithm.

3) Logistic Regression is a supervised machine learning algorithm.

4) It learns patterns from the training dataset.

5) The model uses the extracted URL features to distinguish between phishing and legitimate websites.

6) During training, the model learns the relationship between the input features and their corresponding labels.

7) Once training is completed, we test the model using the testing dataset.

8) We calculate the accuracy to measure the overall correctness of the model.

9) Precision measures how many URLs predicted as phishing are actually phishing.

10) Recall measures how many actual phishing URLs are correctly identified.

11) The F1 score provides a balance between precision and recall.

12) We also generate a classification report to view the performance metrics for each class.

13) Finally, the confusion matrix is displayed using the plots.py file.

14) It helps us understand the number of correct and incorrect predictions made by the model.


### 4. Interactive URL Detection (main.py):
1) Apart from training and testing, our project also provides an interactive URL detection feature.

2) The user can enter a website URL directly into the program.

3) The program extracts the required URL-related features from the entered URL.

4) These features are prepared in the same format used during model training.

5) The feature columns are aligned with the training feature columns.

6) This ensures that the model receives the correct input structure.

7) Missing feature columns are handled to maintain consistency.

8) The numerical features are scaled using the previously fitted StandardScaler.

9) We use the same scaler from preprocessing instead of creating a new one.

10) The processed URL features are then passed to the trained Logistic Regression model.

11) he model analyzes the input features and predicts the URL category.

12) If the URL is classified as phishing, the program displays a phishing warning.

13) If the URL is classified as legitimate, the program displays that the URL appears legitimate.

14) This makes our project useful for checking URLs interactively.


## Main files

| File | Responsibility |
|---|---|
| `main.py` | Model training, evaluation, and interactive URL prediction |
| `preprocessing.py` | Data cleaning, encoding, splitting, and scaling |
| `analysis.py` | Dataset exploration and visual analysis |
| `plots.py` | Confusion-matrix visualization |
| `phishing_features.csv` | Dataset used by the project |
| `requirements.txt` | Python package dependencies |


  




