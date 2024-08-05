# Weather Analysis

This project demonstrates how to analyze a weather dataset using both Python and SQL. The dataset contains various weather attributes such as temperature, humidity, wind speed, and visibility. The project is divided into two parts:

    Part 1: Python Analysis
    Part 2: SQL Analysis

## Part 1: Python Analysis
### Objectives
1. Find all records where the weather was exactly clear.
2. Find the number of times the wind speed was exactly 4 km/hr.
3. Check if there are any NULL values present in the dataset.
4. Rename the column "Weather" to "Weather_Condition."
5. What is the mean visibility of the dataset?
6. Find the number of records where the wind speed is greater than 24 km/hr and visibility is equal to 25 km.
7. What is the mean value of each column for each weather condition?
8. Find all instances where the weather is clear and the relative humidity is greater than 50, or visibility is above 40.
9. Find the number of weather conditions that include snow.
    
### Implementation

The analysis uses the pandas library to load and manipulate the dataset. Various operations such as filtering, aggregating, and checking for null values are performed to extract meaningful insights from the data.

    weather.ipynb
    
## Part 2:SQL Analysis
### Objectives
1. Find all records where the weather was exactly clear.
2. Find the number of times the wind speed was exactly 4 km/hr.
3. Check if there are any NULL values present in the dataset.
4. Find the mean visibility of the dataset.

### Implementation
The dataset is loaded into a SQLite database, and SQL queries are used to extract insights from the data.

     weather.py
     weather_data.db

## Requirements

* Python
* pandas
* sqlite3

### How to Run
1. Clone the repository.
2. Ensure you have the necessary Python libraries installed (pandas, sqlite3).
3. Run the Python script to perform the analysis.
