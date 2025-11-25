import pynance as pn
import pandas as pd

def financial_metrics(df):
    df = df.copy()
    df['Returns'] = df['Close'].pct_change()
    df['Cumulative_Returns'] = (1 + df['Returns']).cumprod()
    
    df['20_Day'] = df['Returns'].rolling(window=20).std() * (252 ** 0.5)
    
    return df 