import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite database
conn = sqlite3.connect('processed_data.db')


# Query to get passenger count vs. average fare data
query_passenger_fare = """
    SELECT
        passenger_count,
        AVG(fare_amount) AS avg_fare
    FROM my_table
    GROUP BY passenger_count
    ORDER BY passenger_count;
"""

# Load data into a DataFrame
passenger_fare_data = pd.read_sql_query(query_passenger_fare, conn)

# Plotting the data
plt.figure(figsize=(8, 6))
plt.bar(passenger_fare_data['passenger_count'], passenger_fare_data['avg_fare'], color='salmon')
plt.xlabel('Passenger Count')
plt.ylabel('Average Fare Amount ($)')
plt.title('Effect of Passenger Count on Trip Fare')
plt.xticks(passenger_fare_data['passenger_count'])
plt.tight_layout()
plt.show()

# Close connection
conn.close()