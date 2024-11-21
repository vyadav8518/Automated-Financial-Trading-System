# 📈 Stock Market Analysis Tool

A Python script for analyzing and visualizing historical stock data for major tech companies using Yahoo Finance data.

## 📋 Features

- Downloads historical stock data for Microsoft, Apple, and Google
- Calculates daily returns
- Computes 50-day moving averages
- Generates visualization plots including:
  - Adjusted closing prices
  - Moving averages
  - Daily returns

## 🔧 Prerequisites

Make sure you have Python 3.x installed and the following packages:

```bash
pip install yfinance pandas numpy matplotlib
```

## 📦 Required Libraries

```python
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

## 🚀 Usage

1. Simply run the script:
```bash
python stock_analysis.py
```

2. The script will automatically:
   - Download stock data for Microsoft (MSFT), Apple (AAPL), and Google (GOOGL)
   - Generate plots for each company showing:
     - Stock prices with 50-day moving average
     - Daily returns

## 📊 Functions

### `download_stock_data(ticker, start_date, end_date)`
Downloads historical stock data for a given ticker symbol and date range.

```python
data = download_stock_data("MSFT", '2010-01-01', '2020-01-01')
```

### `calculate_daily_returns(data)`
Calculates the daily returns from adjusted closing prices.

```python
daily_returns = calculate_daily_returns(stock_data)
```

### `calculate_moving_average(data, window=50)`
Calculates the moving average with a specified window (default: 50 days).

```python
moving_avg = calculate_moving_average(stock_data)
```

### `plot_stock_data(data, company_name)`
Generates visualization plots for a company's stock data.

```python
plot_stock_data(stock_data["Microsoft"], "Microsoft")
```

## 📈 Sample Output

The script generates two plots for each company:
1. Stock price chart with 50-day moving average
2. Daily returns chart

## 🔧 Customization

You can modify the following parameters in the script:
- Date range (currently set to 2010-01-01 to 2020-01-01)
- Moving average window (currently set to 50 days)
- Companies and their tickers in the `companies` dictionary

```python
companies = {
    "Microsoft": "MSFT",
    "Apple": "AAPL",
    "Google": "GOOGL"
}
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⚠️ Disclaimer

This tool is for educational purposes only. Do not use it as financial advice for trading or investments.
