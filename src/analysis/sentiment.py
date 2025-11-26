from textblob import TextBlob 
import pandas as pd

def compute_sentiment(news_df):
    news_df = news_df.copy()
    news_df['Sentiment'] = news_df['headline'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
    return news_df

def aggregate_daily_sentiment(news_df):
    news_df = news_df.copy()
    news_df['date'] = pd.to_datetime(news_df['date'])

    daily_sentiment = (
        news_df.groupby(news_df['date'].dt.date)['Sentiment']
        .mean()
        .reset_index()
        .rename(columns={'date': 'Date'})
    )

    daily_sentiment['Date'] = pd.to_datetime(daily_sentiment['Date'])

    return daily_sentiment


