import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

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

# Group by month and sum purchase_cost
monthly_revenue = df.groupby('month')['purchase_cost'].sum().reset_index()

# Generate suggestion text
if not monthly_revenue.empty:
    max_rev = monthly_revenue.loc[monthly_revenue['purchase_cost'].idxmax()]
    suggestion_text = (f"Highest revenue: {max_rev['month']} with ₹{max_rev['purchase_cost']:.2f}.\n"
                       f"Plan inventory and promotions accordingly for this peak month.")
    
    print("Suggestion:")
    print(suggestion_text)
else:
    suggestion_text = "No revenue data available."
    print(suggestion_text)

# Plot line graph
plt.figure(figsize=(10,6))
plt.subplots_adjust(bottom=0.25)  # Adjust bottom to create space for suggestion

plt.plot(monthly_revenue['month'], monthly_revenue['purchase_cost'], marker='o', color='green')
plt.xlabel('Month')
plt.ylabel('Total Revenue')
plt.title('Revenue vs. Month')
plt.xticks(rotation=45)

# Display suggestion text box below the graph
plt.tight_layout(rect=[0, 0.1, 1, 1])  # leaves space at bottom (10% of figure)
plt.gcf().text(0.02, 0.02, suggestion_text, fontsize=10, color='black',
               bbox=dict(facecolor='lightyellow', alpha=0.5))

plt.tight_layout()
plt.show()
