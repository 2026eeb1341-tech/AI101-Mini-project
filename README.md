# Phishing URL Detection Using Logistic Regression

## 1. Project Overview
This project uses Machine Learning, specifically Logistic Regression, to classify URLs as phishing or legitimate based on URL-related features.

## 2. Project Objective
The main objective is to develop a classification model that identifies potentially phishing URLs and distinguishes them from legitimate URLs.

## 3. Team Members and Roles
- **Execution Lead:** 2026MCB1521
- **PPT Lead:** 2026AIB1061
- **Video Lead:** 2026EEB1344
- **Documentation Lead:** 2026EEB1341

## 4. Dataset Description
- **Dataset:** Phishing URLs Dataset with Extracted Features
- **Source:** [Kaggle Dataset](https://www.kaggle.com/datasets/victusadi/phishing-urls-dataset-with-extracted-features)
- **Total records:** 160,064
- **Total columns:** 13
- **Target column:** `label`
  - `1` – Phishing URL
  - `0` – Legitimate URL

The dataset contains URL-related features such as URL length, number of dots, HTTPS presence, IP address presence, suspicious words, special characters, digit count, and entropy.

## 5. Tools and Technologies
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

## 6. Methodology

1. Load the dataset using Pandas.
2. Explore the dataset and check for duplicate records.
3. Separate input features and the target variable.
4. Exclude non-numeric or unsuitable columns, including the URL, TLD, and `num_subdirs` feature.
5. Split the dataset into training and testing sets using an 80:20 ratio.
6. Use `random_state=42` and stratified splitting.
7. Train a Logistic Regression model with `max_iter=1000` and `class_weight="balanced"`.
8. Evaluate the model using classification metrics.

## 7. Model Evaluation

The model was evaluated on the test dataset.

| Metric | Result |
|---|---:|
| Accuracy | 99.85% |
| Balanced Accuracy | 99.93% |
| ROC-AUC | 99.99% |

**Confusion Matrix:**

`[[164, 0], [47, 31802]]`

The model achieved high evaluation scores on the selected test split.

**Important Limitation:** The dataset has a severe class imbalance, and the unusually high evaluation scores may be influenced by dataset-specific patterns. These results do not guarantee the same performance on real-world URLs. Independent testing on external data is needed.

## 8. How to Run

1. Clone the repository:

   `git clone https://github.com/2026eeb1341-tech/AI101-Mini-project.git`

2. Open the project folder:

   `cd AI101-Mini-project`

3. Install the required dependencies:

   `pip install -r requirements.txt`

4. Run the project:

   `python main.py`

## 9. Presentation and Demonstration
- **Presentation:** Project PPT will be included in the repository.
- **Video Demonstration:** Project demonstration video link will be provided in the repository.

## 10. AI Use Disclosure
Any AI assistance used during the development and documentation of this project will be disclosed according to the course requirements.

## 11. Conclusion
This project demonstrates how Logistic Regression can be used for phishing URL classification using extracted URL features. The evaluation results show strong performance on the available test split, while further external testing is necessary to assess real-world reliability.
