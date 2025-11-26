def align_news_stock(stock_df, news_df, ticker):
    news_stock = news_df[news_df['stock'] == ticker].copy()
    
    news_stock['date_only'] = news_stock['date'].dt.date
    stock_only = stock_df['Date'].dt.date
    
    news_stock = news_stock[news_stock['date_only'].isin(stock_only)]
    return news_stock
