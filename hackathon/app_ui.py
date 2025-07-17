import tkinter as tk
import subprocess
import pandas as pd


root = tk.Tk()
root.title("Welcome to Kanti Sweets Analytics")
root.geometry("800x600")
root.configure(bg='#fff4e6')  # Peach cream background

font_style = ("Calibri", 16)
title_font = ("Calibri", 24, "bold")


data_path = r"C:\learning\sic_pu_june\hackathon\data\clean_data.csv"
df = pd.read_csv(data_path)
available_sweets = sorted(df['item_name'].unique())


months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]


def show_welcome():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Kanti Sweets Analytics", bg='#fff4e6', fg='#4b2e2e', font=title_font).pack(pady=100)

    tk.Button(root, text="Start", bg='#d4af37', fg='black', font=font_style,
              command=show_analysis_options).pack(ipadx=10, ipady=5)


def show_analysis_options():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Select Analysis Graph", bg='#fff4e6', fg='#4b2e2e', font=("Calibri", 20, "bold")).pack(pady=20)

    tk.Button(root, text="Sweet Sales vs. Month", bg='#d4af37', fg='black', font=font_style,
              command=select_sweet).pack(pady=10, ipadx=10, ipady=5)

    tk.Button(root, text="Revenue vs. Month", bg='#d4af37', fg='black', font=font_style,
              command=lambda: run_script(r"C:\learning\sic_pu_june\hackathon\analyze_data\revenue_vs_month.py")).pack(pady=10, ipadx=10, ipady=5)

    tk.Button(root, text="Least Sold Sweet vs. Month", bg='#d4af37', fg='black', font=font_style,
              command=select_month_least_sold).pack(pady=10, ipadx=10, ipady=5)

    tk.Button(root, text="Top Selling Sweet vs. Month", bg='#d4af37', fg='black', font=font_style,
              command=select_month_top_sold).pack(pady=10, ipadx=10, ipady=5)

    tk.Button(root, text="Total Sales vs. Month (Top 5)", bg='#d4af37', fg='black', font=font_style,
              command=lambda: run_script(r"C:\learning\sic_pu_june\hackathon\analyze_data\total_sales_vs_month.py")).pack(pady=10, ipadx=10, ipady=5)

    tk.Button(root, text="Revenue vs. Branch (Top 5)", bg='#d4af37', fg='black', font=font_style,
              command=lambda: run_script(r"C:\learning\sic_pu_june\hackathon\analyze_data\revenue_vs_branch.py")).pack(pady=10, ipadx=10, ipady=5)

    # 🔥 New Sales Prediction button
    tk.Button(root, text="Sales Prediction (Prophet Forecast)", bg='#d4af37', fg='black', font=font_style,
              command=sales_prediction).pack(pady=10, ipadx=10, ipady=5)

    tk.Button(root, text="Back", bg='#c0c0c0', fg='black', font=font_style, command=show_welcome).pack(pady=20, ipadx=10, ipady=5)

# Sweet selection screen
def select_sweet():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Select Sweet", bg='#fff4e6', fg='#4b2e2e', font=("Calibri", 20, "bold")).pack(pady=20)

    sweet_var = tk.StringVar()
    sweet_var.set(available_sweets[0])
    tk.OptionMenu(root, sweet_var, *available_sweets).pack(pady=10, ipadx=10, ipady=5)

    tk.Button(root, text="Generate Graph", bg='#d4af37', fg='black', font=font_style,
              command=lambda: run_script_with_arg(r"C:\learning\sic_pu_june\hackathon\analyze_data\sweet_sales_values_vs_month.py", sweet_var.get())).pack(pady=20, ipadx=10, ipady=5)

    tk.Button(root, text="Back", bg='#c0c0c0', fg='black', font=font_style, command=show_analysis_options).pack(pady=20, ipadx=10, ipady=5)

# Month selection for least sold sweet
def select_month_least_sold():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Select Month", bg='#fff4e6', fg='#4b2e2e', font=("Calibri", 20, "bold")).pack(pady=20)

    month_var = tk.StringVar()
    month_var.set(months[0])
    tk.OptionMenu(root, month_var, *months).pack(pady=10, ipadx=10, ipady=5)

    tk.Button(root, text="Generate Graph", bg='#d4af37', fg='black', font=font_style,
              command=lambda: run_script_with_arg(r"C:\learning\sic_pu_june\hackathon\analyze_data\least_sold_sweet_vs_month.py", month_var.get())).pack(pady=20, ipadx=10, ipady=5)

    tk.Button(root, text="Back", bg='#c0c0c0', fg='black', font=font_style, command=show_analysis_options).pack(pady=20, ipadx=10, ipady=5)

# Month selection for top selling sweet
def select_month_top_sold():
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Select Month", bg='#fff4e6', fg='#4b2e2e', font=("Calibri", 20, "bold")).pack(pady=20)

    month_var = tk.StringVar()
    month_var.set(months[0])
    tk.OptionMenu(root, month_var, *months).pack(pady=10, ipadx=10, ipady=5)

    tk.Button(root, text="Generate Graph", bg='#d4af37', fg='black', font=font_style,
              command=lambda: run_script_with_arg(r"C:\learning\sic_pu_june\hackathon\analyze_data\top_selling_sweet_vs_month.py", month_var.get())).pack(pady=20, ipadx=10, ipady=5)

    tk.Button(root, text="Back", bg='#c0c0c0', fg='black', font=font_style, command=show_analysis_options).pack(pady=20, ipadx=10, ipady=5)


# Sales Prediction function
def sales_prediction():
    from prophet import Prophet
    import matplotlib.pyplot as plt

    data_path = r"C:\learning\sic_pu_june\hackathon\data\clean_data.csv"
    df = pd.read_csv(data_path)

    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.to_period('M')
    monthly_sales = df.groupby('month').size().reset_index(name='total_sales')
    monthly_sales['month'] = monthly_sales['month'].dt.to_timestamp()

    df_prophet = monthly_sales.rename(columns={'month':'ds', 'total_sales':'y'})

    model = Prophet()
    model.fit(df_prophet)

    future = model.make_future_dataframe(periods=12, freq='M')
    forecast = model.predict(future)

    # Plot forecast with peak month suggestion
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df_prophet['ds'], df_prophet['y'], 'ko-', label='Actual Sales')
    ax.plot(forecast['ds'], forecast['yhat'], 'b-', label='Predicted Sales')
    ax.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'],
                    color='skyblue', alpha=0.3, label='Confidence Interval')

    ax.set_title("Forecasted Sales for Next 12 Months", fontsize=14)
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Total Sales", fontsize=12)
    ax.legend()
    ax.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    future_forecast = forecast[forecast['ds'] > df_prophet['ds'].max()]
    if not future_forecast.empty:
        max_row = future_forecast.loc[future_forecast['yhat'].idxmax()]
        max_month = max_row['ds'].strftime('%B %Y')
        max_sales = max_row['yhat']

        suggestion_text = (f"🔮 Predicted peak month: {max_month}\n"
                           f"Expected sales: {max_sales:.0f} transactions")

        ax.text(0.02, -0.25, suggestion_text, fontsize=10, color='black',
                transform=ax.transAxes,
                bbox=dict(facecolor='lightyellow', alpha=0.5))

        print(suggestion_text)
    else:
        print("No future forecast data available.")

    plt.show()

# Script runners
def run_script(script_path):
    subprocess.run(['python', script_path])

def run_script_with_arg(script_path, arg):
    subprocess.run(['python', script_path, arg])

# Start UI
show_welcome()
root.mainloop()
