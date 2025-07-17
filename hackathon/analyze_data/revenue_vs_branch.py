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

# Group by branch_location and month to sum revenue
branch_month_revenue = df.groupby(['branch_location', 'month'])['purchase_cost'].sum().reset_index()

# Create combined branch-month column
branch_month_revenue['branch_month'] = branch_month_revenue['branch_location'] + ' - ' + branch_month_revenue['month']

# Sort by revenue descending and take top 5
top5_branch_month = branch_month_revenue.sort_values(by='purchase_cost', ascending=False).head(5)

# Sort for plotting top-down
top5_branch_month = top5_branch_month.sort_values('purchase_cost', ascending=True)

# Generate suggestion text
if not top5_branch_month.empty:
    highest = top5_branch_month.iloc[-1]  # Last row after ascending sort = highest
    branch, month, revenue = highest['branch_location'], highest['month'], highest['purchase_cost']
    suggestion_text = (f"Highest revenue: {branch} branch in {month} with ₹{revenue:.2f}.\n"
                       f"Focus promotions or new launches in this branch to maximise growth.")
    
    print("Suggestion:")
    print(suggestion_text)
else:
    suggestion_text = "No branch revenue data available."
    print(suggestion_text)

# Plot horizontal bar chart
plt.figure(figsize=(12,7))
plt.barh(top5_branch_month['branch_month'], top5_branch_month['purchase_cost'], color='teal')
plt.xlabel('Revenue')
plt.ylabel('Branch - Month')
plt.title('Top 5 Branch-Month Combinations with Highest Revenue')

# Display suggestion on plot
plt.gcf().text(0.02, 0.02, suggestion_text, fontsize=10, color='black',
               bbox=dict(facecolor='lightyellow', alpha=0.5))

plt.tight_layout()
plt.show()
