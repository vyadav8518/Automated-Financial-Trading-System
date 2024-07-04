import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# Plotting function
def plot_stock_data(data, company_name):
    adj_price = data['Adj Close']
    mav = calculate_moving_average(data)
    daily_return = calculate_daily_returns(data)

    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(adj_price, label='Adjusted Close')
    plt.plot(mav, label='50-Day Moving Average')
    plt.title(f'{company_name} Stock Prices and Moving Average')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(daily_return, label='Daily Returns')
    plt.title(f'{company_name} Daily Returns')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Calculate and plot data for each company
for company, data in stock_data.items():
    plot_stock_data(data, company)
