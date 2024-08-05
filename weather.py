import pandas as pd
import sqlite3
import os

# Define a shorter variable for your directory path
base_dir = 'C:/Users/HP/Programming/Lux/Weather'

# Load the dataset using the base directory variable
data = pd.read_csv(os.path.join(base_dir, 'weather_data/1. Weather Data.csv'))

# Remove any leading/trailing spaces from column names
data.columns = data.columns.str.strip()

print(data.columns)

# Create a SQLite database (or connect to an existing one)
conn = sqlite3.connect('weather_data.db')

# Load the DataFrame into the SQLite database
data.to_sql('weather', conn, if_exists='replace', index=False)

# Define a function to run SQL queries
def run_query(query):
    return pd.read_sql_query(query, conn)

# Example SQL queries for the project
# 1. Find all records where the weather was exactly clear
query1 = 'SELECT * FROM weather WHERE "Weather" = "Clear"'
clear_weather_sql = run_query(query1)

# 2. Find the number of times the wind speed was exactly 4 km/hr
query2 = 'SELECT COUNT(*) FROM weather WHERE "Wind Speed_km/h" = 4'
wind_speed_4_sql = run_query(query2)

# 3. Check if there are any NULL values present in the dataset
query3 = '''
SELECT COUNT(*) FROM weather 
WHERE "Weather" IS NULL OR "Wind Speed_km/h" IS NULL OR "Visibility_km" IS NULL OR "Rel Hum_%" IS NULL
'''
null_values_sql = run_query(query3)

# 4. Find the mean visibility of the dataset
query4 = 'SELECT AVG("Visibility_km") FROM weather'
mean_visibility_sql = run_query(query4)

# Display results
print("All records where the weather was exactly clear:\n", clear_weather_sql)
print("\nNumber of times the wind speed was exactly 4 km/hr:", wind_speed_4_sql.iloc[0, 0])
print("\nAre there any NULL values present in the dataset?", null_values_sql.iloc[0, 0] > 0)
print("\nMean visibility of the dataset:", mean_visibility_sql.iloc[0, 0])

# Close the database connection
conn.close()
