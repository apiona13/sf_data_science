# Project 4: Machine Learning for Binary Classification

## Table of Contents  

[1. Project Description](#project-description)  
[2. Brief Data Overview](#brief-data-overview)  
[3. Project Stages](#project-stages)  
[4. Results](#results)  

### Project Description  

Patterns and key factors influencing clients’ decisions to open a deposit in a bank will be identified using machine learning techniques. Data will be explored to uncover characteristics of potential clients, enabling a clear definition of the target audience (TA) and increasing bank profitability through optimized marketing campaigns.

**Business Task** 

Characteristics that identify clients most likely to open a deposit in the bank will be determined to enhance the effectiveness of marketing campaigns.

**Technical Task** 

As a Data Science specialist, a machine learning model will be developed to predict whether a client will open a deposit based on their characteristics, addressing a binary classification task.

**Main Objectives**  

1. **Comprehensive Data Exploration**: Data will be thoroughly investigated beyond calculating metrics and generating visualizations to uncover meaningful insights.  

2. **Identification of Target Audience Traits**: Distinctive characteristics of potential clients will be revealed to clearly define the target audience and boost bank profitability.  

3. **Innovative Approach**: A variety of tools and techniques will be employed creatively to enhance prediction quality.

:arrow_up:[Back to Table of Contents](#table-of-contents)

### Brief Data Overview  

The dataset from a real bank contains the following information:  
- **Bank Client Data**: `age`, `job`, `marital`, `education`, `default`, `housing`, `loan`, `balance`.  
- **Last Contact Data**: `contact`, `month`, `day`, `duration`.  
- **Other Features**: `campaign`, `pdays`, `previous`, `poutcome`.  
- **Target Variable**: `deposit` (indicates whether a client will open a deposit, binary: yes/no).  

The dataset, stored in `bank_fin.csv`

:arrow_up:[Back to Table of Contents](#table-of-contents)

### Project Stages  

1. **Data Familiarization, Handling Missing Values, and Outliers**  
   The dataset will be explored, missing values in filled, implicit missing values replaced with mode values, and outliers removed using the interquartile range (IQR) method.

2. **Exploratory Data Analysis (EDA)**  
   Numerical and categorical features will be analyzed for correlations and patterns, with visualizations created to identify key trends and relationships.

3. **Data Transformation**  
   Categorical features will be encoded using `LabelEncoder` and one-hot encoding. The top features will be selected using `SelectKBest`. Data will be normalized using for models sensitive to scale.

4. **Classification Task: Logistic Regression and Decision Trees**  
   Baseline models, including logistic regression and decision trees, will be trained and evaluated.

5. **Classification Task: Ensemble Models and Final Prediction**  
   Advanced models, including random forest, gradient boosting, and stacking, will be trained. Hyperparameters for random forest will be optimized using Optuna.

:arrow_up:[Back to Table of Contents](#table-of-contents)

### Results  

The following outcomes were achieved:  

- **Data Processing**: Missing values were filled with the median, implicit missing values replaced with mode values, and 1057 outliers in `balance` removed using the IQR method

- **Exploratory Analysis**: Relationships between numerical and categorical features were analyzed, with visualizations highlighting key patterns. The top 3 most important features identified after fitting: `duration`, `poutcome_success`, and `balance`.

- **Data Transformation**: Categorical features were encoded using `LabelEncoder` and one-hot encoding. The top 15 features were selected using `SelectKBest`. Data was normalized with `MinMaxScaler` to ensure compatibility with sensitive models.

- **Model Training**: Models of varying complexity were trained, including logistic regression, decision trees, random forest, gradient boosting, and stacking.

- **Optimization**: Hyperparameters for the random forest model were optimized using Optuna

- **Logging**: Results, including accuracy, F1-Score, and confusion matrices, were logged in Comet.ml ([link](https://www.comet.com/apiona13/project-classification/2a0dfdff10ab4d4e9a3c9a26bc70f65d)).

- **Key Insights**: The duration of the last contact, the success of previous campaigns, and client balance were critical predictors of deposit openings, enabling targeted marketing strategies.

**Tools Used**: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn` (`LabelEncoder`, `MinMaxScaler`, `SelectKBest`, `train_test_split`, `LogisticRegression`, `DecisionTreeClassifier`, `RandomForestClassifier`, `GradientBoostingClassifier`, `StackingClassifier`), `optuna`, `comet_ml`.

:arrow_up:[Back to Table of Contents](#table-of-contents)

If you find this project interesting or useful, I would greatly appreciate it if you could star the repository and profile ⭐️⭐️⭐️!