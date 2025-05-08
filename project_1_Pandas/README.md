# Project 1: Data Analysis and Visualization of Resumes

## Table of Contents

[1. Project Description](#project-description)  
[2. Problem Statement](#problem-statement)  
[3. Data Overview](#data-overview)  
[4. Project Stages](#project-stages)  
[5. Results](#results)

### Project Description

This project focuses on analyzing a dataset of approximately 44,744 job seeker resumes from the [hh.ru](hh.ru) platform to uncover patterns in demographics, work experience, education, and salary expectations. The dataset requires preprocessing to transform unstructured text into structured features, followed by exploratory data analysis (EDA) and visualization to identify trends and anomalies.  

:arrow_up:[to table of contents](#table-of-contents)

### Problem Statement

The goal is to preprocess and clean the dataset, create new features, and perform EDA to provide actionable insights for recruitment strategies. Prepare a data for next stages of Machine Learning 

**Quality Metrics**  

- New categorical and numerical features created for analysis.  

- Dataset cleaned of duplicates, missing values, and outliers. 

- Comprehensive EDA conducted with visualizations to reveal data distributions and dependencies.  

**Skills Practiced** 

- Writing clean Python code using Pandas for data manipulation.

- Creating visualizations with Matplotlib, Seaborn, and Plotly Express.

- Applying statistical methods for outlier detection and data cleaning.  

:arrow_up:[to table of contents](#table-of-contents)

### Data Overview  

The dataset includes 44,744 resumes from hh.ru with 12 features. A supplementary dataset provides currency exchange rates for salary conversions.  

- **Main Dataset**
- **Exchange Rates**

:arrow_up:[to table of contents](#table-of-contents)

### Project Stages  

1. **Feature Engineering**: Created new categorical (e.g., **`Пол`** ("Gender"), **`Образование`** ("Education")) and numerical (e.g., **`Возраст`** ("Age"), **`Опыт работы (год)`** ("Work Experience (years)")) features from text columns, removing unnecessary columns. 

2. **Exploratory Data Analysis**: Analyzed distributions and dependencies using histograms, boxplots, bar charts, heatmaps, and scatter plots with Pandas, Matplotlib, Seaborn, and Plotly Express. 

3. **Data Cleaning**: Removed duplicates, filled missing **`Опыт работы`** , and dropped rows with missing workplace or position data.  

4. **Outlier Detection and Removal**: Manually removed resumes with salaries, work experience exceeding age, and age outliers using a modified z-score method (4-sigma relaxation to the right).  

:arrow_up:[to table of contents](#table-of-contents)

### Results  

The project delivered:  

- **New Features**: Structured categorical (e.g., **`Город`** ("City"), **`Готовность к переезду`** ("Readiness for Relocation")) and numerical (e.g., **`ЗП (руб)`** ("Salary (RUB)")) features for enhanced analysis.

- **Cleaned Dataset**: Free of duplicates, missing values, and outliers, ensuring data quality.  

- **Key Insights**:

  - **Age**: Most job seekers are 25–38 years old (median ~30, mode 30), with anomalies at >100 years and ~15 years.

  - **Work Experience**: Majority have 0–180 months (median ~100, mode 81), with outliers at 1188 months. 

  - **Salary**: Most desire <100K RUB, with extreme outliers at 8M and 25M RUB.  

  - **Education & Salary**: Higher education correlates with higher median salaries (~30% higher than secondary education). 

  - **City & Salary**: Moscow job seekers expect the highest salaries, followed by Saint Petersburg; million-plus and other cities show similar medians.  

  - **Relocation & Business Trips**: Job seekers open to both have the highest salary expectations.  

  - **Age vs. Experience**: Normal correlation, with anomalies where experience exceeds age.  

The analysis provides actionable insights for optimizing recruitment by aligning strategies with job seeker profiles.  

**Tools Used**: `Pandas`, `NumPy`, `Matplotlib`, `Seaborn`, `Plotly Express`

:arrow_up:[to table of contents](#table-of-contents)

If you find this project interesting or useful, I’d greatly appreciate it if you could star the repository and profile ⭐️⭐️⭐️!