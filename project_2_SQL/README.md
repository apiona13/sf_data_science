# Project 2: SQL-driven Data Analysis. HeadHunter Job Vacancy Analysis

## Table of Contents

[1. Project Description](#project-description)  
[2. Brief Data Overview](#brief-data-overview)  
[3. Project Stages](#project-stages)  
[4. Results](#results)  

### Project Description

Data from the HeadHunter job vacancy dataset will be analyzed using SQL queries executed via the `psycopg2` library. The focus is on exploring the dataset to uncover patterns and insights related to vacancies, employers, regions, and industries, with an emphasis on practicing SQL query development.

**Skills Practiced**

- Writing SQL queries to retrieve data from a database schema using Python.  
- Analyzing job vacancy data to identify trends and characteristics.  

:arrow_up:[Back to Table of Contents](#table-of-contents)

### Brief Data Overview 

The dataset contains job vacancy data from the HeadHunter platform, stored in the `project_sql` schema. It includes information about vacancies, employers, regions, industries, and related attributes.

:arrow_up:[Back to Table of Contents](#table-of-contents)

### Project Stages  

1. **Preliminary Data Analysis**  
   The dataset will be explored to determine the number of vacancies, employers, regions, and industries.

2. **Detailed Vacancy Analysis**  
   A deeper analysis of vacancies will be conducted, examining their distribution by region, salary information, work schedules, employment types, and required experience.

3. **Employer Analysis**  
   Employers posting vacancies will be analyzed, focusing on the number of vacancies per employer, their regional distribution, industries, and activity in million-plus cities in Russia.

4. **Domain-Specific Analysis**  
   Vacancies related to Data Science (DS) will be analyzed, including the number of DS vacancies, junior-level opportunities, key skill requirements, and salary expectations.

5. **Conclusions and Additional Queries**  
   General conclusions will be drawn, trends identified, and additional SQL queries practiced to further explore the dataset.

:arrow_up:[Back to Table of Contents](#table-of-contents)

### Results  

The following outcomes were achieved:  

- Proficiency in writing SQL queries was developed through code implementation using the `psycopg2` library. 

- Data retrieved via SQL queries was analyzed to uncover insights.  

- Conclusions were drawn based on the findings, including: 

  - The dataset contains **49197 vacancies**, **23501 employers**, spans **1362 regions**, and covers **294 industries**, with an average of **2.09 vacancies per employer**.

  - Moscow has the highest number of vacancies, with a growing trend toward remote work.  

  - Only **50% of vacancies** include salary information, and **55% require minimal experience**, while **15% require no experience**. 

  - **'Яндекс'** leads with **1933 vacancies** across **181 regions**, and **485 vacancies** in million-plus cities (25% of its total).

  - **1771 vacancies (8%)** are data-related, with **51 suitable for junior data scientists**, **229 requiring SQL/PostgreSQL**, and **357 requiring Python**.  

  - DS vacancies list an average of **6.41 key skills**, and salaries for candidates with **3+ years of experience** are **3.25 times higher** than for those without.

  - IT and data-related vacancies are likely to remain in demand, with higher salaries in developed cities and tech-driven industries.

**Tools Used**: `pandas`, `psycopg2`

:arrow_up:[Back to Table of Contents](#table-of-contents)

If you find this project interesting or useful, I would greatly appreciate it if you could star the repository and profile ⭐️⭐️⭐️!