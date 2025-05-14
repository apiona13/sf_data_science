# Project 6: Text Classification with Naive Bayes Classifier

## Table of Contents 
 
[1. Project Description](#project-description)  
[2. Brief Data Overview](#brief-data-overview)  
[3. Project Stages](#project-stages)  
[4. Results](#results)  

### Project Description

This project focuses on classifying emails as spam or non-spam using a Naive Bayes Classifier to automate email filtering. The dataset will be preprocessed, and a machine learning model will be developed to predict email labels, addressing challenges like class imbalance and text data handling.

**Business Task**  

Develop a model to accurately classify emails as spam or non-spam to improve email filtering efficiency and user experience.

**Technical Task** 

As a Data Science specialist, a machine learning model will be built to predict a binary label (spam or non-spam) based on email text features, solving a classification task.

**Main Objectives**  

1. **Comprehensive Data Exploration**: Analyze the dataset to understand class distribution and text characteristics.  
2. **Effective Preprocessing**: Handle missing values and convert text into a suitable format for modeling.  
3. **Innovative Approach**: Optimize model performance through hyperparameter tuning and robust evaluation.

:arrow_up:[Back to Table of Contents](#table-of-contents)

### Brief Data Overview 

The dataset (`spam_or_not_spam.csv`) contains:  
- **Email Text**: Content of emails, preprocessed with placeholders (e.g., `NUMBER` for digits).  
- **Target Variable**: Binary label (`0` for non-spam, `1` for spam).  
- **Class Distribution**: Imbalanced, with 83.3% non-spam and 16.7% spam emails.  

:arrow_up:[Back to Table of Contents](#table-of-contents)

### Project Stages  

1. **Data Loading and Exploration**  
   Load the dataset, calculate class distribution, and visualize the spam/non-spam ratio.

2. **Data Preprocessing**  
   Remove missing values, handle empty strings, and vectorize text data for modeling.

3. **Train-Test Split**  
   Perform stratified train-test splitting (75% train, 25% test) to preserve class distribution.

4. **Model Training and Evaluation**  
   Train a Complement Naive Bayes model and evaluate it using multiple classification metrics.

5. **Hyperparameter Tuning**  
   Optimize the `alpha` parameter using cross-validation to enhance model performance.

:arrow_up:[Back to Table of Contents](#table-of-contents)

### Results  

The following outcomes were achieved:  

- **Data Processing**: Missing values were removed, and email text was vectorized using feature engineering techniques.

- **Exploratory Analysis**: Class imbalance was identified (83.3% non-spam, 16.7% spam) and visualized, guiding model selection.

- **Data Transformation**: Text data was converted to a numerical format, and stratified splitting ensured balanced class representation.  

- **Model Training**: A Complement Naive Bayes model was trained, suitable for imbalanced text classification.

- **Optimization**: Hyperparameter tuning via `GridSearchCV` identified an optimal `alpha=0.78476`, achieving a model accuracy of 0.991 (tuning time: 84.84 seconds).  

- **Evaluation**: The model was assessed using `accuracy`, `precision`, `recall`, `F1-score`, `confusion matrix`, and `ROC-AUC`, demonstrating high performance with low false positives for spam.  

- **Key Insights**: The Complement Naive Bayes model effectively handled class imbalance, with stable performance for `alpha` values up to 1, enabling reliable spam filtering.  

**Tools Used**: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn` (`train_test_split`, `GridSearchCV`, `ComplementNB`, `classification_report`, `confusion_matrix`, `roc_curve`), `time`.

:arrow_up:[Back to Table of Contents](#table-of-contents)

If you find this project interesting or useful, I would greatly appreciate it if you could star the repository and profile ⭐️⭐️⭐️!