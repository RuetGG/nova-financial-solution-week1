import matplotlib.pyplot as plt

def plot_price_and_moving_averages(df, title="Price vs SMA/EMA"):
    plt.figure(figsize=(14,5))
    plt.plot(df.index, df['Close'], label='Close', color='black')
    plt.plot(df.index, df['SMA_20'], label='SMA 20', color='blue')
    plt.plot(df.index, df['EMA_20'], label='EMA 20', color='red')
    plt.title(title)
    plt.legend()
    plt.show()

def plot_rsi(df, title="Relative Strength Index"):
    plt.figure(figsize=(14,3))
    plt.plot(df.index, df['RSI_14'], label='RSI 14', color='purple')
    plt.axhline(70, color='red', linestyle='--')
    plt.axhline(30, color='green', linestyle='--')
    plt.ylim(0,100)
    plt.title(title)
    plt.legend()
    plt.show()

def plot_macd(df, title="MACD"):
    plt.figure(figsize=(14,4))
    plt.plot(df.index, df['MACD'], label='MACD', color='blue')
    plt.plot(df.index, df['MACD_signal'], label='Signal', color='red')
    plt.bar(df.index, df['MACD_hist'], label='Histogram', color='grey')
    plt.title(title)
    plt.legend()
    plt.show()

def plot_all(df, stock_name="Stock"):
    import matplotlib.gridspec as gridspec

    plt.figure(figsize=(14,10))
    gs = gridspec.GridSpec(3,1, height_ratios=[3,1,2])

    ax0 = plt.subplot(gs[0])
    ax0.plot(df.index, df['Close'], label='Close', color='black')
    ax0.plot(df.index, df['SMA_20'], label='SMA 20', color='blue')
    ax0.plot(df.index, df['EMA_20'], label='EMA 20', color='red')
    ax0.set_title(f"{stock_name}: Price vs SMA/EMA")
    ax0.legend()

    ax1 = plt.subplot(gs[1], sharex=ax0)
    ax1.plot(df.index, df['RSI_14'], label='RSI 14', color='purple')
    ax1.axhline(70, color='red', linestyle='--')
    ax1.axhline(30, color='green', linestyle='--')
    ax1.set_ylim(0,100)
    ax1.set_title("RSI")
    ax1.legend()

    ax2 = plt.subplot(gs[2], sharex=ax0)
    ax2.plot(df.index, df['MACD'], label='MACD', color='blue')
    ax2.plot(df.index, df['MACD_signal'], label='Signal', color='red')
    ax2.bar(df.index, df['MACD_hist'], label='Histogram', color='grey')
    ax2.set_title("MACD")
    ax2.legend()

    plt.tight_layout()
    plt.show()