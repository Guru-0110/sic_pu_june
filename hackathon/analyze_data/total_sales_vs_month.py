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

# Group by month and count the quantity of sales
monthly_sales = df.groupby('month').size().reset_index(name='total_sales')

# Sort by total sales descending to get top 5 months
top5_months = monthly_sales.sort_values(by='total_sales', ascending=False).head(5)

# Sort top 5 months ascending for better visual (top-down bar chart)
top5_months = top5_months.sort_values('total_sales', ascending=True)

# Provide suggestion based on highest month
if not top5_months.empty:
    highest = top5_months.iloc[-1]  # Last row after ascending sort = highest sales month
    month, sales = highest['month'], highest['total_sales']
    suggestion_text = (f"Highest total sales in {month} with {sales} transactions.\n"
                       f"Plan stock and staff allocation efficiently for this peak month.")
    
    print("Suggestion:")
    print(suggestion_text)
else:
    suggestion_text = "No total sales data available."
    print(suggestion_text)

# Plot horizontal bar chart
plt.figure(figsize=(10,6))
plt.barh(top5_months['month'], top5_months['total_sales'], color='purple')
plt.xlabel('Total Sales')
plt.ylabel('Month')
plt.title('Top 5 Months with Highest Total Sales')

# Adjust layout to create space for suggestion and display it
plt.tight_layout(rect=[0, 0.15, 1, 1])  # leave 15% space at bottom

plt.gcf().text(0.02, 0.02, suggestion_text, fontsize=10, color='black',
               bbox=dict(facecolor='lightyellow', alpha=0.5))

plt.show()
