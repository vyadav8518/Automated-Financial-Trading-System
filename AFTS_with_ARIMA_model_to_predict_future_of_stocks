import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Function to download stock data using yfinance
def download_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

# List of companies and their respective tickers
companies = {
    "Microsoft": "MSFT",
    "Apple": "AAPL",
    "Google": "GOOGL"
}

# Dictionary to hold data for each company
stock_data = {}

# Download data for each company
for company, ticker in companies.items():
    stock_data[company] = download_stock_data(ticker, '2010-01-01', '2020-01-01')

# Ensure the date index has a frequency
for company in stock_data:
    stock_data[company] = stock_data[company].asfreq('B')

# Function to calculate daily returns
def calculate_daily_returns(data):
    close_price = data['Adj Close']
    daily_return = close_price.pct_change()
    daily_return.fillna(0, inplace=True)
    return daily_return

# Function to calculate moving average
def calculate_moving_average(data, window=50):
    adj_price = data['Adj Close']
    mav = adj_price.rolling(window=window).mean()
    return mav

# Function to fit ARIMA model and predict future prices
def predict_future_prices(data, steps=30):
    model = ARIMA(data['Adj Close'], order=(5, 1, 0))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=steps)
    forecast_dates = pd.date_range(start=data.index[-1] + pd.Timedelta(days=1), periods=steps, freq='B')
    forecast_series = pd.Series(forecast, index=forecast_dates)
    return forecast_series

# Plotting function
def plot_stock_data(data, company_name, forecast):
    adj_price = data['Adj Close']
    mav = calculate_moving_average(data)
    daily_return = calculate_daily_returns(data)

    plt.figure(figsize=(14, 10))

    plt.subplot(3, 1, 1)
    plt.plot(adj_price, label='Adjusted Close')
    plt.plot(mav, label='50-Day Moving Average')
    plt.title(f'{company_name} Stock Prices and Moving Average')
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(daily_return, label='Daily Returns')
    plt.title(f'{company_name} Daily Returns')
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(adj_price, label='Historical Prices')
    plt.plot(forecast, label='Predicted Prices', linestyle='dashed')
    plt.title(f'{company_name} Stock Price Prediction')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Calculate and plot data for each company
for company, data in stock_data.items():
    forecast = predict_future_prices(data)
    plot_stock_data(data, company, forecast)
