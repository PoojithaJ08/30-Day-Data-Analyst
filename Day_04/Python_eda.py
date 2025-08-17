# Install first (in terminal if needed): pip install prophet
import pandas as pd
import matplotlib.pyplot as plt 

from prophet import Prophet

# Load dataset
df = pd.read_csv("dataset/retail_store_inventory.csv")

# Clean column names
df.columns = df.columns.str.strip().str.replace(" ", "_").str.lower()

# Convert 'date' to datetime
df['date'] = pd.to_datetime(df['date'])

# Group by date to calculate total daily sales
daily_sales = df.groupby('date')['units_sold'].sum().reset_index()

# Plot sales trend
plt.figure(figsize=(12, 5))
plt.plot(daily_sales['date'], daily_sales['units_sold'], label='Daily Units Sold')
plt.title('Daily Units Sold')
plt.xlabel('Date')
plt.ylabel('Units Sold')
plt.grid(True)
plt.legend()
plt.show()

# Forecasting with Prophet
prophet_df = daily_sales.rename(columns={'date': 'ds', 'units_sold': 'y'})
model = Prophet()
model.fit(prophet_df)

# Forecast next 30 days
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

# Plot forecast
model.plot(forecast)
plt.title('30-Day Forecast of Units Sold')
plt.show()
