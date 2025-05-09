# Project 3: EDA & Future Engineering for Machine Learning

## Table of Contents  

[1. Project Description](#project-description)  
[2. Brief Data Overview](#brief-data-overview)  
[3. Project Stages](#project-stages)  
[4. Results](#results)  

### Project Description  

This project focuses on predicting hotel ratings on Booking.com based on a dataset of 515,000 hotel reviews across Europe. By applying machine learning techniques, the goal is to enhance data from the initial dataset to improve user recommendations and provide actionable insights for hotel management. The dataset includes diverse features such as reviewer feedback, hotel characteristics, and geographical data, which are explored and engineered to optimize model performance.

**Business Task**  

Develop a machine learning model to accurately predict hotel ratings, enabling better recommendations for Booking.com users and insights for hotel management to improve services.

**Technical Task**  

As a Data Science specialist, first of all our task is EDA, data preprocessing, feature engineering. Then a regression model will be developed to predict the `reviewer_score` (hotel rating) using features like review text, tags, and geographical coordinates. Our main metric is the Mean Absolute Percentage Error (MAPE).

**Main Objectives**  

1. **Comprehensive Data Exploration**: Analyze the dataset to identify patterns and relationships between features and the target variable (`reviewer_score`).

2. **Identification of Key Factors**: Determine critical features influencing hotel ratings to improve prediction accuracy.  

3. **Innovative Approach**: Apply creative feature engineering and preprocessing techniques, such as geocoding missing coordinates and encoding categorical variables, to enhance model performance.  

:arrow_up:[Back to Table of Contents](#table-of-contents)

### Brief Data Overview 

The dataset contains approximately 515,000 hotel reviews from `hotels_train.csv` (386,803 rows) and `hotels_test.csv` (128,935 rows), covering hotels across Europe. Key features include:  

- **Review Data**: `reviewer_score` (target), `negative_review`, `positive_review`, `review_total_negative_word_counts`, `review_total_positive_word_counts`.  
- **Hotel Data**: `hotel_address`, `hotel_name`, `average_score`, `total_number_of_reviews`, `additional_number_of_scoring`.  
- **Reviewer Data**: `reviewer_nationality`, `total_number_of_reviews_reviewer_has_given`.  
- **Temporal Data**: `review_date`, `days_since_review`.  
- **Geographical Data**: `lat`, `lng` (with some missing values).  
- **Tags**: `tags` describing trip type, room type, and other characteristics.  

:arrow_up:[Back to Table of Contents](#table-of-contents)

### Project Stages  

1. **Data Familiarization and Enrichment**  
   The dataset was loaded, cleaned, and enriched with new features. Missing `lat` and `lng` values were filled using geocoding with the `Nominatim API` based on `hotel_address`. New features were created.

2. **Exploratory Data Analysis (EDA)**  
   Numerical and categorical features were analyzed using correlation analysis and visualizations (e.g., bar charts of feature correlations with `reviewer_score`). No strong correlations were found, indicating the need for feature engineering.

3. **Data Transformation**  
   Categorical features were preprossesed and encoded using. Numerical features were standardized using `StandardScaler`. Feature selection was explored with `chi-2 test` and `ANOVA test` and the top features (`imp_features`) were used for modeling.

4. **Regression Task: Baseline Model**  
   A `RandomForestRegressor` was trained as the baseline model, achieving a MAPE of 0.13453 on the test set.

5. **Create a Prediction on a Test Dataset and Create a submission**
   A prediction was created and file with submission was uploaded to Kaggle

:arrow_up:[Back to Table of Contents](#table-of-contents)

### Results  

The following outcomes were achieved:  

- **Data Processing**: The dataset was cleaned, with missing `lat` and `lng` values filled using geocoding. New features were created, including temporal features (`year_of_review`, `month_of_review`) and tag-based metrics (`qty_of_tags`). 

- **Exploratory Analysis**: Correlation analysis revealed no strong linear relationships with `reviewer_score`, emphasizing the importance of feature engineering. Key features included `average_score`, `review_total_negative_word_counts`, and `review_total_positive_word_counts`.  

- **Data Transformation**: Categorical features were encoded, and numerical features were standardized. The top features were selected for modeling, ensuring compatibility with the `RandomForestRegressor`.  

- **Model Training**: The `RandomForestRegressor` achieved a MAPE of 0.13230 on the training set and 0.13453 on the test set, improving from the baseline MAPE of 0.1413.  

- **Submission**: Predictions were generated for the test set

**Key Insights**: Feature engineering (e.g., geocoding, temporal features) and careful preprocessing were critical for improving model performance. The `RandomForestRegressor` provided robust predictions, with minimal overfitting, suitable for real-world applications like hotel rating recommendations.  

**Tools Used**: `pandas`, `numpy`, `category_encoders` (`BinaryEncoder`), `scipy.stats`, `matplotlib`, `seaborn`, `scikit-learn` (`train_test_split`, `StandardScaler`, `feature_selection`, `RandomForestRegressor`, `mean_absolute_percentage_error`), `geopy` (`Nominatim`), `time`.  

:arrow_up:[Back to Table of Contents](#table-of-contents)

If you find this project interesting or useful, I would greatly appreciate it if you could star the repository and profile ⭐️⭐️⭐️!