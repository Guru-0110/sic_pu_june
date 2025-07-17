# clean_data.py

import pandas as pd

# Step 1: Read the raw data
raw_data_path = r'C:\learning\sic_pu_june\hackathon\data\kanti_sweets_transactions.csv'
data = pd.read_csv(raw_data_path)

# Step 2: Drop the 'transaction_id' column
cleaned_data = data.drop('transaction_id', axis=1)

# Step 3: Save the cleaned data as clean_data.csv
cleaned_data_path = r'C:\learning\sic_pu_june\hackathon\data\clean_data.csv'
cleaned_data.to_csv(cleaned_data_path, index=False)

print(" Data cleaning completed. Cleaned data saved as clean_data.csv.")
