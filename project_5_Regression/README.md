# Project 5: Machine Learning for Regression Task

## Table of Contents  

[1. Project Description](#project-description)  
[2. Brief Data Overview](#brief-data-overview)  
[3. Project Stages](#project-stages)  
[4. Results](#results)  

### Project Description  

The duration of taxi trips in New York will be predicted using machine learning techniques to optimize fare estimation and business processes. Data will be explored to uncover factors influencing trip duration, enabling accurate predictions and improved operational efficiency.

**Business Task**  

Key factors affecting taxi trip duration will be identified to enhance fare prediction accuracy.

**Technical Task**  

As a Data Science specialist, a machine learning model will be developed to predict trip duration in seconds based on trip and environmental characteristics, addressing a regression task.

**Main Objectives**  

1. **Comprehensive Data Exploration**: Data will be thoroughly analyzed to uncover meaningful patterns beyond basic metrics and visualizations.  

2. **Identification of Key Factors**: Critical features influencing trip duration will be revealed to improve prediction accuracy. 

3. **Innovative Approach**: A variety of tools and techniques will be applied creatively to enhance model performance.

:arrow_up:[Back to Table of Contents](#table-of-contents)

### Brief Data Overview 

The dataset, covering January to June 2016, contains approximately 1.5 million records with the following information:  
- **Trip Data**: Pickup and dropoff locations, timestamps, passenger count, trip duration.  
- **Weather Data**: Temperature, precipitation, and other conditions.  
- **Holiday Data**: U.S. holidays impacting traffic.  
- **OSRM API Data**: Routing details, including distances and travel times.  

:arrow_up:[Back to Table of Contents](#table-of-contents)

### Project Stages  

1. **Data Familiarization and Enrichment**  
   Multiple data sources will be merged, cleaned, and enriched with new features through feature engineering, such as distance and time calculations.

2. **Exploratory Data Analysis (EDA)**  
   Numerical and categorical features will be analyzed for patterns, with visualizations created to identify key relationships.

3. **Data Transformation**  
   Categorical features will be encoded, the top features selected using `SelectKBest`, and data normalized using `MinMaxScaler` for models sensitive to scale.

4. **Regression Task: Baseline Models**  
   Baseline models, including linear regression, model with polynomial features, model with l2 regulazation, and decision trees, will be trained and evaluated.

5. **Regression Task: Ensemble Models and Final Prediction**  
   Advanced models, including gradient boosting and XGBoost, will be trained, with hyperparameters optimized to improve predictions.

:arrow_up:[Back to Table of Contents](#table-of-contents)

### Results  

The following outcomes were achieved:  

- **Data Processing**: A dataset of ~1.5 million trips was created by merging trip, weather, holiday, and OSRM data. No missing values were found.

- **Exploratory Analysis**: Visualizations highlighted key patterns, with `total_distance`, `haversine_distance`, and `pickup_hour` identified as the top 3 most important features. 

- **Data Transformation**: Categorical features were encoded, and the top 25 features were selected. Data was normalized to ensure model compatibility.  

- **Model Training**: Models of varying complexity were trained, including linear regression, regresiion in polynomial features, model with l2 regulazation, decision trees, gradient boosting, and XGBoost.

- **Optimization**: Hyperparameters for the gradient boosting model were optimized to enhance performance.  

- **Logging**: Results, including RMSLE and Median Absolute Error, were logged in Comet.ml ([link](https://www.comet.com/apiona13/project-regression/e33ca42f464847a180126c1e0f6963f6)).
  
- **Key Insights**: Distance metrics and pickup time were critical predictors of trip duration, enabling optimized fare estimation strategies.  

**Tools Used**: `pandas`, `numpy`, `scipy.stats`, `matplotlib`, `seaborn`, `plotly`, `scikit-learn` (`train_test_split`, `SelectKBest`, `MinMaxScaler`, `LinearRegression`, `PolynomialFeatures`, `linear_model.Ridge`, `DecisionTreeRegressor`, `RandomForestRegressor`, `GradientBoostingRegressor`), `xgboost`, `comet_ml`.

:arrow_up:[Back to Table of Contents](#table-of-contents)

If you find this project interesting or useful, I would greatly appreciate it if you could star the repository and profile ⭐️⭐️⭐️!