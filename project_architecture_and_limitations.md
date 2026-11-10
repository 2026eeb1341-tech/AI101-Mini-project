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



# MODEL_LIMITATIONS:

## What the Model Can and Cannot Do

Our project uses Logistic Regression, a supervised machine learning algorithm, to classify URLs into two categories: phishing and legitimate.

The model makes predictions based on different URL-related features, such as URL length, number of dots, HTTPS usage, IP-address information, suspicious keywords, and Top-Level Domain (TLD) information.

By learning patterns from the training dataset, the model can identify characteristics commonly associated with phishing URLs and use them to classify previously unseen inputs.

However, although the model provides a useful approach to phishing detection, it has certain limitations that must be considered when interpreting its predictions and performance.

## 1. Limitations of the Model

### 1.1 Dependency on the Dataset

1) The performance of our machine learning model depends heavily on the quality and diversity of the dataset used during training.
2) The model learns patterns only from the examples provided in the training data.
3) If the dataset contains limited examples or does not represent different types of phishing attacks, the model may fail to identify certain malicious URLs.
4) It may perform differently when tested on URLs collected from different sources or at a later point in time.
5) Therefore, a good performance on the current dataset does not necessarily guarantee the same performance in real-world situations.

### 1.2 Imbalanced Dataset

1) A dataset is considered imbalanced when one class contains significantly more samples than another.
2) In our project, the number of phishing URLs and legitimate URLs may not be equally distributed.
3) This can influence how the Logistic Regression model learns and makes predictions.
4) The model may become more biased towards the class with a larger number of training examples.
5) In such situations, accuracy alone may give a misleading impression of the model's performance.
6) For example, a model may achieve high accuracy while failing to identify a considerable number of actual phishing URLs.
7) To understand its performance more effectively, we also consider precision, recall, F1 score, and the confusion matrix.

### 1.3 Possibility of Overly Optimistic Results

1) Sometimes, a machine learning model may produce unusually high evaluation scores.
2) However, high accuracy does not always mean that the model will perform equally well on completely new data.
3) Similar or duplicate records appearing in both training and testing datasets can make the evaluation results look better than they actually are.
4) Patterns introduced during dataset collection may also influence the model's predictions.
5) Certain features may indirectly reveal information about the target label, resulting in data leakage.
6) These issues can cause the model to perform well during testing but less effectively in real-world situations.
7) Testing the model with a separate dataset collected from an independent source can provide a more reliable estimate of its generalisation ability.

### 1.4 Changing Phishing Techniques

1) Phishing attacks continuously evolve as attackers develop new techniques to deceive users.
2) Attackers may change URL structures, domain names, suspicious keywords, and other characteristics.
3) Our model identifies phishing URLs based on patterns learned from the available training dataset.
4) If attackers introduce new URL patterns that were not represented during training, the model may fail to recognize them.
5) Features that are useful for identifying phishing URLs today may become less effective in the future.
6) Therefore, the model may require periodic retraining with updated and diverse datasets to remain useful.

### 1.5 No Live Website Reputation Verification

1) Our current project primarily focuses on analysing URL-related features.
2) It does not directly communicate with live threat-intelligence services or browser security databases.
3) As a result, it cannot verify whether a domain has already been reported as malicious by security organisations.
4) It also does not continuously monitor website reputation or check newly reported phishing domains.
5) A URL may appear structurally normal while still leading to a malicious website.
6) Integrating trusted and regularly updated threat-intelligence services could improve the detection capabilities of the project.

### 1.6 Predictions Are Not Always Accurate

1) The output generated by our Logistic Regression model is a prediction based on learned patterns, not a guaranteed security verdict.
2) Like other machine learning models, it can produce incorrect classifications.
3) A legitimate URL may sometimes be incorrectly identified as phishing. This is known as a false positive.
4) Similarly, a phishing URL may be incorrectly classified as legitimate. This is known as a false negative.
5) False negatives are particularly important because they may allow potentially harmful URLs to go unnoticed.
6) Therefore, users should not assume that a URL is completely safe simply because our model classifies it as legitimate.
7) Similarly, a phishing prediction should be treated as a warning that requires further verification.

## 2. Possible Improvements in the Future

To improve the accuracy, reliability, and practical usefulness of our project, several enhancements can be considered:

1. **Use More Diverse Datasets:** Include larger and more diverse datasets collected from multiple trusted sources to help the model recognize a wider range of phishing patterns.

2. **Independent Dataset Testing:** Evaluate the trained model using a completely separate dataset collected from a different source or time period to measure its ability to generalise.

3. **Error Analysis:** Study false positives and false negatives to identify the situations in which the model makes incorrect predictions.

4. **Duplicate Detection:** Check for identical or highly similar URLs across training and testing datasets to reduce the possibility of data leakage.

5. **Model Comparison:** Compare Logistic Regression with other machine learning algorithms, such as Random Forest, Decision Tree, and Support Vector Machine, to evaluate their relative performance.

6. **Automated Feature Testing:** Develop automated tests to ensure that URL feature extraction produces consistent results during both model training and live prediction.

7. **Experiment Reproducibility:** Record dataset versions, preprocessing configurations, model parameters, and evaluation results so that experiments can be repeated and compared reliably.

8. **Threat Intelligence Integration:** Explore integration with trusted and up-to-date threat-intelligence services to verify whether URLs or domains have previously been identified as malicious.

9. **Regular Model Updates:** Periodically retrain and evaluate the model using updated datasets to account for changes in phishing techniques.

10. **Improved Detection Techniques:** Explore additional URL, domain, and website-related features to improve the model's ability to distinguish between legitimate and malicious websites.

## 3. Responsible Use of the Project

1) This project is primarily developed for educational purposes, experimentation, and demonstration of machine learning techniques in cybersecurity.
2) It demonstrates how URL-related features can be used to identify patterns associated with phishing websites.
3) However, it should not be considered a complete cybersecurity solution or used as the only method for determining whether a website is safe.
4) The model's predictions should always be interpreted with caution.
5) Users should avoid entering passwords, banking details, or other sensitive personal information on websites they do not trust.
6) Suspicious URLs should be verified using reliable security tools and trusted sources before interacting with them.

## 4. Conclusion

Our Phishing URL Detection project demonstrates the practical application of machine learning in identifying potentially malicious URLs.

Although Logistic Regression provides a useful starting point, its performance depends on the quality of the dataset, the relevance of the extracted features, and the ability to recognize changing phishing patterns.

Understanding these limitations is important because it helps us interpret the model's results realistically rather than relying only on evaluation scores.

With improvements such as independent dataset testing, better feature extraction, model comparison, and threat-intelligence integration, the project could be developed into a more reliable and effective phishing detection system.

  




