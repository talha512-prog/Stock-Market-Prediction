import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import RangeSlider
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import seaborn as sns
import yfinance as yf


# Load the CSV file
def load_stock_data(file_path):
    return pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')

# Calculate Simple Moving Average (SMA)
def calculate_sma(data, window):
    return data['Close'].rolling(window=window).mean()

# Calculate daily returns
def calculate_returns(data):
    data['Daily Returns'] = data['Close'].pct_change() * 100
    return data

# Forecast future stock prices using linear regression
def forecast_stock_prices(data, forecast_days):
    data['Prediction'] = data['Close'].shift(-forecast_days)

    X = np.array(data['Close']).reshape(-1, 1)
    y = np.array(data['Prediction']).reshape(-1, 1)

    X = X[:-forecast_days]
    y = y[:-forecast_days]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    future_prices = model.predict(X[-forecast_days:])

    return model, future_prices.flatten()

# Plot Close Price vs 50-Day SMA with zoom slider
def plot_close_vs_sma50(data):
    sma_50 = calculate_sma(data, 50)
    
    fig, ax = plt.subplots(figsize=(14, 7))
    plt.subplots_adjust(bottom=0.25)
    l1, = ax.plot(data.index, data['Close'], label='Close Price', alpha=0.75, color='blue')
    l2, = ax.plot(data.index, sma_50, label='50-Day SMA', linestyle='--', alpha=0.75, color='orange')
    ax.set_title('Close Price vs 50-Day SMA')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()
    ax.grid(True)
    ax.set_xticks(data.index[::len(data)//10])
    ax.set_xticklabels([date.strftime('%Y-%m-%d') for date in data.index[::len(data)//10]], rotation=45)

    ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
    slider = RangeSlider(ax_slider, 'Zoom', valmin=data.index[0].value, valmax=data.index[-1].value,
                         valinit=(data.index[0].value, data.index[-1].value))

    def update(val):
        ax.set_xlim(pd.to_datetime(val))
        fig.canvas.draw_idle()

    slider.on_changed(update)
    plt.show()

# Plot Close Price vs 200-Day SMA with zoom slider
def plot_close_vs_sma200(data):
    sma_200 = calculate_sma(data, 200)
    
    fig, ax = plt.subplots(figsize=(14, 7))
    plt.subplots_adjust(bottom=0.25)
    l1, = ax.plot(data.index, data['Close'], label='Close Price', alpha=0.75, color='blue')
    l2, = ax.plot(data.index, sma_200, label='200-Day SMA', linestyle='--', alpha=0.75, color='green')
    ax.set_title('Close Price vs 200-Day SMA')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()
    ax.grid(True)
    ax.set_xticks(data.index[::len(data)//10])
    ax.set_xticklabels([date.strftime('%Y-%m-%d') for date in data.index[::len(data)//10]], rotation=45)

    ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
    slider = RangeSlider(ax_slider, 'Zoom', valmin=data.index[0].value, valmax=data.index[-1].value,
                         valinit=(data.index[0].value, data.index[-1].value))

    def update(val):
        ax.set_xlim(pd.to_datetime(val))
        fig.canvas.draw_idle()

    slider.on_changed(update)
    plt.show()

# Plot Close Price vs Forecasted Prices with zoom slider
def plot_close_vs_forecast(data):
    forecast_days = 30
    _, future_prices = forecast_stock_prices(data, forecast_days)
    future_dates = pd.date_range(start=data.index[-1], periods=forecast_days + 1, freq='B')[1:]
    
    fig, ax = plt.subplots(figsize=(14, 7))
    plt.subplots_adjust(bottom=0.25)
    l1, = ax.plot(data.index, data['Close'], label='Close Price', alpha=0.75, color='blue')
    l2, = ax.plot(future_dates, future_prices, label='Forecasted Prices', linestyle='--', alpha=0.75, color='red')
    ax.set_title(f'Close Price vs Forecasted Prices ({forecast_days} Days)')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()
    ax.grid(True)
    combined_dates = data.index.append(future_dates)
    ax.set_xticks(combined_dates[::len(combined_dates)//10])
    ax.set_xticklabels([date.strftime('%Y-%m-%d') for date in combined_dates[::len(combined_dates)//10]], rotation=45)

    ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
    slider = RangeSlider(ax_slider, 'Zoom', valmin=data.index[0].value, valmax=combined_dates[-1].value,
                         valinit=(data.index[0].value, combined_dates[-1].value))

    def update(val):
        ax.set_xlim(pd.to_datetime(val))
        fig.canvas.draw_idle()

    slider.on_changed(update)
    plt.show()

# Plot correlation heatmap 
def plot_correlation_heatmap(data): 
    correlation_matrix = data.corr() 
    fig, ax = plt.subplots(figsize=(10, 7)) 
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5, ax=ax) 
    ax.set_title("Correlation Heatmap") 
    plt.show()


    
data = load_stock_data("apple.csv")

data = calculate_returns(data)

plot_close_vs_sma50(data)
plot_close_vs_sma200(data)
plot_close_vs_forecast(data)
plot_correlation_heatmap(data)

# Print the forecasted future prices with actual dates in the terminal 
forecast_days = 30
_, future_prices = forecast_stock_prices(data, forecast_days)
future_dates = pd.date_range(start=data.index[-1], periods=forecast_days + 1, freq='B')[1:]

# Create a DataFrame for forecasted prices and save to CSV 
forecasted_data = pd.DataFrame({'Date': future_dates, 'Forecasted Price': future_prices}) 
forecasted_data.to_csv('forecasted_prices.csv', index=False) 
print("Forecasted prices saved to 'forecasted_prices.csv")


