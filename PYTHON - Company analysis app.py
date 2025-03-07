import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

class MarketAnalyzer:
    def __init__(self, ticker):
        """Initialize the analyzer with a stock ticker."""
        self.ticker = ticker
        self.stock = yf.Ticker(ticker)

    def get_stock_history(self, period="1y"):
        """Fetch historical stock prices."""
        history = self.stock.history(period=period)
        return history[['Close']]

    def get_financial_ratios(self):
        """Retrieve financial ratios like P/E, P/B, etc."""
        info = self.stock.info
        return {
            "Company Name": info.get("shortName", "N/A"),
            "Market Cap": info.get("marketCap", "N/A"),
            "P/E Ratio": info.get("trailingPE", "N/A"),
            "P/B Ratio": info.get("priceToBook", "N/A"),
            "Dividend Yield": info.get("dividendYield", "N/A"),
        }

    def plot_stock_trend(self, period="1y"):
        """Plot stock price trends."""
        history = self.get_stock_history(period)
        history.plot(title=f"Stock Price Trend: {self.ticker}")
        plt.xlabel("Date")
        plt.ylabel("Price (USD)")
        plt.show()

def compare_companies(tickers):
    """Compare multiple companies' stock trends."""
    plt.figure(figsize=(10, 5))
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        history = stock.history(period="1y")
        plt.plot(history.index, history['Close'], label=ticker)

    plt.title("Stock Price Comparison")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.show()

# Example Usage
if __name__ == "__main__":
    ticker = input("Enter stock ticker (e.g., AAPL): ").upper()
    analyzer = MarketAnalyzer(ticker)
    
    # Fetch financial ratios
    print("\nFinancial Ratios:")
    for key, value in analyzer.get_financial_ratios().items():
        print(f"{key}: {value}")

    # Plot stock trend
    analyzer.plot_stock_trend()

    # Compare companies
    tickers = input("\nEnter multiple tickers to compare (comma-separated): ").upper().split(",")
    if len(tickers) > 1:
        compare_companies(tickers) 
