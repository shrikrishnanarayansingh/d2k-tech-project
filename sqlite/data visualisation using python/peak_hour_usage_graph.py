import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite database
conn = sqlite3.connect('processed_data.db')

# Query to get peak hours data
query_peak_hours = """
    SELECT
        strftime('%H', tpep_pickup_datetime) AS hour_of_day,
        COUNT(*) AS num_trips
    FROM my_table
    GROUP BY hour_of_day
    ORDER BY num_trips DESC;
"""

# Load data into a DataFrame
peak_hours_data = pd.read_sql_query(query_peak_hours, conn)

# Plotting the data
plt.figure(figsize=(10, 6))
plt.bar(peak_hours_data['hour_of_day'], peak_hours_data['num_trips'], color='skyblue')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Trips')
plt.title('Peak Hours for Taxi Usage')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Close connection
conn.close()
