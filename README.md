# Dry Bean Type Classification using Machine Learning

## Project Overview

This project automates the classification of dry bean varieties using Machine Learning. The goal is to replace the manual bean-sorting process with an intelligent system that can accurately identify bean types based on their physical characteristics extracted through computer vision techniques.

The solution helps improve classification accuracy, reduce manual effort, lower operational costs, and support scalable quality-control processes in the agriculture industry.

## Dataset

* Dataset: Dry Bean Dataset
* Total Records: 13,611
* Features: 16 numerical attributes
* Target Classes: 7 bean varieties

  * Seker
  * Barbunya
  * Bombay
  * Cali
  * Dermason
  * Horoz
  * Sira

## Project Workflow

1. Data Loading and Exploration
2. Exploratory Data Analysis (EDA)
3. Missing Value and Outlier Treatment
4. Feature Scaling and Preprocessing
5. Class Imbalance Handling using SMOTE
6. Model Training and Evaluation
7. Hyperparameter Tuning using GridSearchCV
8. Model Comparison and Selection
9. Streamlit Application Development
10. Model Deployment

## Machine Learning Models Used

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier
* K-Nearest Neighbors (KNN)
* Support Vector Machine (SVM)
* Naive Bayes
* Extra Trees Classifier
* Gradient Boosting Classifier

## Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* Cross Validation

## Best Model

After comparing multiple algorithms and performing hyperparameter tuning, the best-performing model was selected and saved using Pickle for deployment.

## Streamlit Application

The application allows users to enter bean measurements and instantly predict the bean variety.

### Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Imbalanced-learn (SMOTE)
* Streamlit
* Pickle

## Business Impact

* Reduces manual classification effort
* Improves classification accuracy
* Speeds up quality-control operations
* Supports scalable agricultural automation
* Enables real-time bean variety prediction

## Author

Bhushan Mandekar
