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

# Check for command-line argument
if len(sys.argv) < 2:
    print("Please provide the month name as a command line argument.")
    sys.exit()

# Replace input() with sys.argv[1] so that we can directly choose the month on the user interface
selected_month = sys.argv[1]

# Filter data for the selected month
month_df = df[df['month'].str.lower() == selected_month.lower()]

if month_df.empty:
    print(f"No data available for {selected_month}.")
else:
    # Group by item_name to count quantity sold
    item_sales = month_df.groupby('item_name').size().reset_index(name='quantity_sold')

    # Identify top selling sweet(s)
    max_quantity = item_sales['quantity_sold'].max()
    top_sold_items = item_sales[item_sales['quantity_sold'] == max_quantity]

    sweet_names = ', '.join(top_sold_items['item_name'].values)
    suggestion_text = (f"Top selling sweet(s) in {selected_month}: {sweet_names} with {max_quantity} units.\n"
                       f"Ensure sufficient stock and continue promoting these popular items.")

    print("Suggestion:")
    print(suggestion_text)

    # Plot bar chart with top sweet highlighted
    plt.figure(figsize=(10,6))
    bars = plt.bar(item_sales['item_name'], item_sales['quantity_sold'], color='lightgreen')

    for bar, item in zip(bars, item_sales['item_name']):
        if item in top_sold_items['item_name'].values:
            bar.set_color('darkgreen')

    plt.xlabel('Sweet Name')
    plt.ylabel('Quantity Sold')
    plt.title(f'Top Selling Sweet in {selected_month} (Highlighted)')
    plt.xticks(rotation=45)

    # Adjust layout to create space for suggestion text
    plt.tight_layout(rect=[0, 0.15, 1, 1])

    # Display suggestion text on the graph
    plt.gcf().text(0.02, 0.02, suggestion_text, fontsize=10, color='black',
                   bbox=dict(facecolor='lightyellow', alpha=0.5))

    plt.show()
