import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite database
conn = sqlite3.connect('processed_data.db')


# Query to get trends in usage over the year
query_usage_trends = """
    SELECT
        strftime('%Y-%m', tpep_pickup_datetime) AS year_month,
        COUNT(*) AS num_trips
    FROM my_table
    GROUP BY year_month
    ORDER BY year_month;
"""

# Load data into a DataFrame
usage_trends_data = pd.read_sql_query(query_usage_trends, conn)

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(usage_trends_data['year_month'], usage_trends_data['num_trips'], marker='o', linestyle='-')
plt.xlabel('Year-Month')
plt.ylabel('Number of Trips')
plt.title('Trends in Taxi Usage Over the Year')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()

# Close connection
conn.close()
