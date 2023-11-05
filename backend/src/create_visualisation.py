'''
Implement a “reporting” sub menu which helps to plot charts with the following options:

Reporting

---------------------------

1) Number of trades per broker (histogram)

2) Share price history for a specified share_id (line chart / connected scatter graph)

3) Proportion of trades traded on each exchange (pie chart)

4) Return to main menu
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def get_trades_per_broker(db_connection):

    query = "SELECT * FROM trades"
    trades = pd.read_sql_query(query, db_connection)
    trades_broker_id = trades.groupby('broker_id')['trade_id'].count()
    ax = sns.histplot(data=trades_broker_id, bins=10)
    ax.set(xlabel='Number of Trades', ylabel='Number of Brokers', title='Number of Trades per Broker')

def get_shares_prices(db_connection):

    query = "SELECT * FROM trades"
    trades = pd.read_sql_query(query, db_connection)
    sns.lineplot(
        data=trades,
        x='transaction_time',
        y='price_total',
        hue='share_id',
        palette='husl',
        linewidth=2.5,  # Adjust the line width
        markers=True,  # Show markers at data points
        markersize=8,  # Customize marker size
    )

    # You can further customize the plot
    plt.title('Price Total Over Time by Share ID', fontsize=16)
    plt.xlabel('Transaction Time', fontsize=14)
    plt.ylabel('Price Total', fontsize=14)
    plt.legend(title='Share ID', fontsize=12, title_fontsize=12)

    plt.show()

def get_trades_stock_ex(db_connection):

    query = "SELECT * FROM trades"
    trades = pd.read_sql_query(query, db_connection)
    trades_stock_ex_id = trades.groupby('stock_ex_id')['trade_id'].count()
    plt.pie(trades_stock_ex_id, labels=trades_stock_ex_id.index, autopct='%1.1f%%', startangle=140)
    plt.title('Proportion of Trades by Exchange', fontsize=16)