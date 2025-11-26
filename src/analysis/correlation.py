import pandas as pd
from scipy.stats import pearsonr

def calculate_daily_return(stock_df):
    stock_df = stock_df.copy()
    stock_df['Daily_Returns'] = stock_df['Close'].pct_change()
    return stock_df

def corr_senti_return(stock_df, daily_sentiment, ticker):
    daily_sentiment['Date'] = pd.to_datetime(daily_sentiment['Date'])
    stock_df['Date'] = pd.to_datetime(stock_df['Date'])


    df = pd.merge(stock_df, daily_sentiment, on='Date', how='inner')
    df = df.dropna(subset=['Daily_Returns', 'Sentiment'])
    if len(df) >= 2:
        corr, _ = pearsonr(df['Daily_Returns'].dropna(), df['Sentiment'])
    else:
        corr = None
        print(f"Not enough data to calculate correlation for {ticker}")
    return corr, df