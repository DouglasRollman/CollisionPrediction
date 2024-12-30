# NYC Collision & Vehicle Data Analysis

## Overview
This project analyzes two raw datasets from **NYC Open Data**, focusing on motor vehicle collisions and vehicle involvement in New York City. The goal was to uncover trends and make predictions using various factors such as time series, weather, and location data.

### Datasets:
1. **Motor Vehicle Collisions - Crashes**  
   - 2,108,711 instances  
   - 29 columns  
   
2. **Motor Vehicle Collisions - Vehicles**  
   - 4.23 million data points  
   - 25 features  

Both datasets required extensive data cleaning and preprocessing due to missing values and inconsistencies.

## Data Challenges & Solutions

### Pattern Identification in Location Data:
- A significant number of records had missing **LATITUDE** and **LONGITUDE** values. These missing values were not random but occurred consistently for accidents on specific geographic areas—primarily bridges across the city.
- This pattern suggested that the missing data was due to the inability to capture precise location data for incidents occurring on bridges, rather than data being randomly missing.

### Data Cleaning & Preprocessing:
- We identified and addressed location data issues by removing approximately **25,000 records** where location data was unreliable or missing.
- Custom **regular expressions** were developed to clean the dataset by resolving misspellings and formatting inconsistencies, ensuring better data quality and consistency for analysis.

## Algorithms Used

We employed a variety of machine learning algorithms to predict key outcomes:

- **Prediction Targets:**  
   - Number of persons killed  
   - Number of vehicles involved  
   - Number of persons injured  

- **Algorithms:**
   - Decision Tree
   - Linear Regression
   - K-Nearest Neighbors (KNN with 5 neighbors)
   - Random Forest  
   - Additional Decision Tree modeling  

## Tools & Techniques

- **Programming Language:** Python
- **Libraries & Tools:**  
  - **pandas** for data manipulation  
  - **sklearn** for machine learning algorithms  
  - **Matplotlib** and **Seaborn** for data visualization  



