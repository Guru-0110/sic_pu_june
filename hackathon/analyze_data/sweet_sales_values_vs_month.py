import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

# Get current script directory
script_dir = os.path.dirname(__file__)

# Construct relative path to data folder
data_path = os.path.join(script_dir, '..', 'data', 'clean_data.csv')

# Check if data file exists
if not os.path.exists(data_path):
    print(f"Data file not found at {data_path}")
    sys.exit()

# Read cleaned data
df = pd.read_csv(data_path)

# Convert 'date' to datetime and extract month
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.strftime('%B')

# Replace input() with sys.argv[1] so that we can directly choose the sweet on The user Interface
if len(sys.argv) < 2:
    print("Please provide the sweet name as a command line argument.")
    sys.exit()

selected_sweet = sys.argv[1]

# Filter data for the selected sweet
sweet_df = df[df['item_name'].str.lower() == selected_sweet.lower()]

if sweet_df.empty:
    print(f"No sales data available for {selected_sweet}.")
else:
    # Group by month to count quantity sold
    monthly_sales = sweet_df.groupby('month').size().reset_index(name='quantity_sold')

    # Prepare suggestion text based on highest selling month 
    max_sales = monthly_sales.loc[monthly_sales['quantity_sold'].idxmax()]
    suggestion_text = (f"Highest sales for {selected_sweet}: {max_sales['month']} "
                       f"with {max_sales['quantity_sold']} units.\n"
                       f"Consider promotions or stock prioritisation in {max_sales['month']} to maximise sales.")

    print("Suggestion:")
    print(suggestion_text)

    # Plot
    plt.figure(figsize=(10,6))
    plt.bar(monthly_sales['month'], monthly_sales['quantity_sold'], color='skyblue')
    plt.xlabel('Month')
    plt.ylabel('Quantity Sold')
    plt.title(f'{selected_sweet} Sales Quantity vs. Month')
    plt.xticks(rotation=45)

    plt.tight_layout(rect=[0, 0.15, 1, 1])  # leaves space at bottom

    # Display suggestion box on the graph
    plt.gcf().text(0.02, 0.02, suggestion_text, fontsize=10, color='black',
                   bbox=dict(facecolor='lightyellow', alpha=0.5))

    plt.show()
