# Project 7: Customer Segmentation for an Online Store

## Table of Contents  

[1. Project Description](#project-description)  
[2. Brief Data Overview](#brief-data-overview)  
[3. Project Stages](#project-stages)  
[4. Results](#results)  

### Project Description  

This project focuses on segmenting customers of an online store using machine learning clustering and dimensionality reduction techniques. By analyzing purchasing power, order frequency, and recency of purchases, we aim to identify customer segments and develop tailored engagement strategies to enhance marketing efforts and business profitability.

**Business Task**  

Segment existing customers, interpret the resulting clusters, and define strategies for effective interaction with each segment.

**Technical Task**  

As Data Science specialists, we will develop a clustering model to group customers based on their purchasing power, order frequency, and recency of their last purchase, and profile each cluster to inform marketing strategies.

**Main Objectives**  

1. **Comprehensive Data Exploration**: Analyze the dataset to uncover patterns and relationships influencing customer behavior.

2. **Identification of Key Factors**: Determine critical features driving customer segmentation to improve clustering accuracy.

3. **Innovative Approach**: Apply advanced clustering and dimensionality reduction techniques, such as PCA and t-SNE, to enhance model performance.  

:arrow_up:[Back to Table of Contents](#table-of-contents)

### Brief Data Overview 

The dataset contains over 500,000 transaction records from an online store, covering customer purchases across multiple countries. Key features include:

- **Transaction Data**: `InvoiceNo` (unique invoice ID, with 'C' indicating cancellations), `StockCode` (product ID), `Description` (product name), `Quantity`, `InvoiceDate`, `UnitPrice` (in pounds sterling).  

- **Customer Data**: `CustomerID` (unique customer ID), `Country` (customer’s country of residence). 

- **Derived Features**: Temporal features (e.g., month, day, hour of purchase) and return indicators.  

:arrow_up:[Back to Table of Contents](#table-of-contents)

### Project Stages  

1. **Data Familiarization and Enrichment**  
   We merged and cleaned transaction data, handled missing values in `CustomerID` and `Description`, removed duplicates, and created new features such as `QuantityCanceled`, `TotalPrice`, and temporal attributes (e.g., `year`, `month`, `day_of_week`).  

2. **Exploratory Data Analysis (EDA)**  
   We analyzed numerical and categorical features, identifying patterns such as peak order volumes in the UK, seasonal trends (end-of-year spikes), and absence of Saturday orders. Visualizations highlighted key relationships, including revenue and order distributions.  

3. **Data Transformation**  
   We encoded categorical features (e.g., `Country`), standardized numerical features using `StandardScaler`, and applied dimensionality reduction (PCA and t-SNE). Outliers were removed using the 95th percentile for `Frequency` and `Monetary` in the RFM table.  

4. **Clustering Task: Model Development**  
   We trained clustering models (`K-Means`, `GaussianMixture`, `AgglomerativeClustering`) on RFM features, selecting the optimal number of clusters (2–10) using the silhouette coefficient. K-Means on t-SNE-decomposed data yielded the best results.  

5. **Classification Task: Predicting Segments**  
   We transformed the clustering task into a classification problem, training ensemble models (`RandomForestClassifier`, `GradientBoostingClassifier`, `XGBoost`, `CatBoost`) to predict customer segments based on RFM features, with hyperparameter tuning via `GridSearchCV`.  

:arrow_up:[Back to Table of Contents](#table-of-contents)

### Results  

The following outcomes were achieved:  

- **Data Processing**: The dataset was cleaned, removing ~25% of rows with missing `CustomerID` or `Description`, duplicates, negative transactions (returns), and zero-priced items. The final dataset contained ~400,000 transactions across 7,983 unique customers. 

- **Exploratory Analysis**: The UK dominated in order volume, revenue, and customer count. Orders peaked in November–December, with no Saturday transactions and high activity from 10 AM to 3 PM. Outliers in `Quantity` and `UnitPrice` were identified and addressed.

- **Data Transformation**: RFM features (`Recency`, `Frequency`, `Monetary`) were created, outliers were filtered (95th percentile), and data was transformed using PCA (explaining ~70–80% variance) and t-SNE (KL divergence ~0.5–1.0).  

- **Model Training**: K-Means with 8 clusters on t-SNE-decomposed data achieved the highest silhouette score (~0.4–0.5). Classification models (XGBoost, CatBoost) predicted segments with accuracy ~ 98%.

- **Optimization**: Hyperparameters were tuned for RandomForestClassifier (`max_depth`, `n_estimators`, `criterion`) and GradientBoostingClassifier (`max_depth`, `learning_rate`, `n_estimators`), with training times of ~30–120 seconds.

- **Logging**: Results, including Accuracy score and plot with clustered distribution, were logged in Comet.ml ([link](https://www.comet.com/apiona13/clustering-and-dimensionality-reduction-algorithms/d4e3928fa39946feaab7a684124695e3)).

**Tools Used**: `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly` (`graph_objects`), `scikit-learn` (`StandardScaler`, `MinMaxScaler`, `PCA`, `t-SNE`, `KMeans`, `GaussianMixture`, `AgglomerativeClustering`, `GridSearchCV`, `RandomForestClassifier`, `GradientBoostingClassifier`), `xgboost`, `catboost`. 

:arrow_up:[Back to Table of Contents](#table-of-contents)

If you find this project interesting or useful, I would greatly appreciate it if you could star the repository and profile ⭐️⭐️⭐️!