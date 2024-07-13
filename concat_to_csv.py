import os
import pandas as pd

# Directory where the CSV files are located
folder_path = '/content/trip_data/'

# List to hold all the data frames from individual CSV files
all_data_frames = []

# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        # Read each CSV file into a pandas DataFrame
        df = pd.read_csv(file_path)
        # Append the DataFrame to the list
        all_data_frames.append(df)

# Concatenate all DataFrames into a single DataFrame
combined_df = pd.concat(all_data_frames, ignore_index=True)

# Path to the output combined CSV file
output_csv_path = '/content/trip_data/processed_data.csv'

# Write the combined DataFrame to a single CSV file
combined_df.to_csv(output_csv_path, index=False)

print(f'Combined CSV file saved to {output_csv_path}')
