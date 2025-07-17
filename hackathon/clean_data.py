import pandas as pd
import os
import sys

# Get current script directory
script_dir = os.path.dirname(__file__)

# Construct relative paths to raw data and cleaned data output
raw_data_path = os.path.join(script_dir, '..', 'data', 'kanti_sweets_transactions.csv')
cleaned_data_path = os.path.join(script_dir, '..', 'data', 'clean_data.csv')

# Check if raw data file exists
if not os.path.exists(raw_data_path):
    print(f"Raw data file not found at {raw_data_path}")
    sys.exit()

# Step 1: Read the raw data
data = pd.read_csv(raw_data_path)

# Step 2: Drop the 'transaction_id' column if it exists
if 'transaction_id' in data.columns:
    cleaned_data = data.drop('transaction_id', axis=1)
else:
    cleaned_data = data

# Step 3: Save the cleaned data as clean_data.csv
cleaned_data.to_csv(cleaned_data_path, index=False)

print("Data cleaning completed. Cleaned data saved as clean_data.csv.")
