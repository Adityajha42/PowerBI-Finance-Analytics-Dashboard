# =================================================================
# THE ONLY PYTHON SCRIPT YOU NEED
# =================================================================
print("Script started. Attempting to import libraries...")
try:
    import pandas as pd
    import yfinance as yf
    from datetime import datetime
    print("SUCCESS: Libraries imported successfully.")
except ImportError as e:
    print(f"ERROR: Could not import a library. {e}")
    exit()

tickers = ['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'INFY.NS', 'ICICIBANK.NS']
benchmark = '^NSEI'
all_tickers_to_download = tickers + [benchmark]
start_date = '2023-01-01'
end_date = datetime.today().strftime('%Y-%m-%d')
print(f"\nAttempting to download data for: {all_tickers_to_download}")

try:
    historical_data = yf.download(all_tickers_to_download, start=start_date, end=end_date)
    if historical_data.empty:
        print("\nERROR: No data was downloaded. Check internet or tickers.")
        exit()
    print("SUCCESS: Data downloaded from Yahoo Finance.")
except Exception as e:
    print(f"\nERROR: An error occurred during download: {e}")
    exit()

try:
    print("\nProcessing and saving files...")

    processed_df = historical_data['Close'].stack().reset_index()
    processed_df.columns = ['Date', 'TickerSymbol', 'ClosePrice']
    processed_df.to_csv('historical_prices.csv', index=False)
    print("- historical_prices.csv created successfully.")

    transactions_data = {
        'TransactionDate': ['2023-01-15', '2023-02-20', '2023-03-10', '2023-04-05', '2023-05-25', '2024-01-10'],
        'TickerSymbol': ['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'INFY.NS', 'RELIANCE.NS', 'TCS.NS'],
        'TransactionType': ['BUY', 'BUY', 'BUY', 'BUY', 'BUY', 'SELL'],
        'Quantity': [10, 15, 25, 30, 5, 5],
        'PricePerShare': [2350.00, 3300.00, 1600.00, 1380.00, 2450.00, 4100.00]
    }
    transactions_df = pd.DataFrame(transactions_data)
    transactions_df.to_csv('transactions.csv', index=False)
    print("- transactions.csv created successfully.")

    stocks_data = {
        'TickerSymbol': ['RELIANCE.NS', 'TCS.NS', 'HDFCBANK.NS', 'INFY.NS', 'ICICIBANK.NS'],
        'CompanyName': ['Reliance Industries', 'Tata Consultancy Services', 'HDFC Bank', 'Infosys', 'ICICI Bank'],
        'Sector': ['Energy', 'IT', 'Financials', 'IT', 'Financials']
    }
    stocks_df = pd.DataFrame(stocks_data)
    stocks_df.to_csv('stocks.csv', index=False)
    print("- stocks.csv created successfully.")

    print("\nSUCCESS: All files are ready for import.")
except Exception as e:
    print(f"\nERROR: An error occurred during file processing: {e}")
