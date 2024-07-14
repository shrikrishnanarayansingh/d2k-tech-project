import os
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import pyarrow.parquet as pq

# Set the base URL for the dataset
base_url = "https://d37ci6vzurychx.cloudfront.net/trip-data"

# Set the year for the dataset
year = 2019

# Create a directory to store the downloaded files
download_dir = f"downloads/parquet/project/{year}"
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Set the retry policy for network errors
retry_policy = Retry(total=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])

# Create a session with the retry policy
session = requests.Session()
session.mount("https://", HTTPAdapter(max_retries=retry_policy))

# Iterate over the months of the year
for month in range(1, 13):
    # Construct the URL for the Parquet file
    url = f"{base_url}/yellow_tripdata_{year}-{month:02d}.parquet"

    # Download the Parquet file with retries
    response = session.get(url)
    if response.status_code == 200:
        # Save the file to the download directory
        file_path_parquet = os.path.join(download_dir, f"yellow_tripdata_{year}-{month:02d}.parquet")
        with open(file_path_parquet, "wb") as f:
            f.write(response.content)
        print(f"Downloaded {file_path_parquet}")

        # Convert Parquet to CSV
        file_path_csv = os.path.join(download_dir, f"yellow_tripdata_{year}-{month:02d}.csv")
        try:
            table = pq.read_table(file_path_parquet)
            df = table.to_pandas()
            df.to_csv(file_path_csv, index=False)
            print(f"Converted to CSV: {file_path_csv}")
        except Exception as e:
            print(f"Error converting {file_path_parquet} to CSV: {e}")
        
    else:
        print(f"Error downloading {url}: {response.status_code}")
