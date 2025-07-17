from prophet import Prophet
import pandas as pd
import matplotlib.pyplot as plt


data_path = r'C:\learning\sic_pu_june\hackathon\data\clean_data.csv'
df = pd.read_csv(data_path)


df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.to_period('M')
monthly_sales = df.groupby('month').size().reset_index(name='total_sales')
monthly_sales['month'] = monthly_sales['month'].dt.to_timestamp()

# Rename for Prophet
df_prophet = monthly_sales.rename(columns={'month':'ds', 'total_sales':'y'})

# Initialize and fit model
model = Prophet()
model.fit(df_prophet)

# Forecast next 12 months
future = model.make_future_dataframe(periods=12, freq='M')
forecast = model.predict(future)

# Plot forecast with enhanced details
fig, ax = plt.subplots(figsize=(12, 6))

# Plot historical data
ax.plot(df_prophet['ds'], df_prophet['y'], 'ko-', label='Actual Sales')

# Plot forecasted data
ax.plot(forecast['ds'], forecast['yhat'], 'b-', label='Predicted Sales')

# Plot upper and lower bounds for confidence interval
ax.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], color='skyblue', alpha=0.3, label='Confidence Interval')

# Labels and title
ax.set_title("Forecasted Sales for Next 12 Months", fontsize=14)
ax.set_xlabel("Date", fontsize=12)
ax.set_ylabel("Total Sales", fontsize=12)
ax.legend()
ax.grid(True)

plt.xticks(rotation=45)
plt.tight_layout()

# Suggestion for maximum future sales month and checks only for the furthur data from the present
future_forecast = forecast[forecast['ds'] > df_prophet['ds'].max()]

if not future_forecast.empty:
    max_row = future_forecast.loc[future_forecast['yhat'].idxmax()]
    max_month = max_row['ds'].strftime('%B %Y')
    max_sales = max_row['yhat']

    # Add suggestion text on the graph for the better understanding
    suggestion_text = (f" Predicted peak month: {max_month}\n"
                       f"Expected sales: {max_sales:.0f} transactions")

    ax.text(0.10,0.10, suggestion_text, fontsize=10, color='black',
            transform=ax.transAxes,
            bbox=dict(facecolor='lightyellow', alpha=0.5))   # can change the position of the suggestion table by first 2 values

    print(suggestion_text)
else:
    print("No future forecast data available.")

plt.show()

# Display future forecast values for reference
print(future_forecast[['ds', 'yhat']])
