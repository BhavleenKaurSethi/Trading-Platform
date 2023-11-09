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
import os
from datetime import datetime, timedelta  
from google.cloud import storage
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    './trading-platform-404001-c56c24689187.json'
)

def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket and make it publicly readable."""
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)
    # Generate a signed URL for the blob that expires in one hour
    url = blob.generate_signed_url(expiration=timedelta(hours=1))

    return url

def get_trades_per_broker(db_connection):
    query = "SELECT * FROM trades"
    filename = 'trades_per_broker.png'
    trades = pd.read_sql_query(query, db_connection)
    trades_broker_id = trades.groupby('broker_id')['trade_id'].count()
    
    ax = sns.histplot(data=trades_broker_id, bins=10)
    ax.set(xlabel='Number of Trades', ylabel='Number of Brokers', title='Number of Trades per Broker')
    
    plt.savefig(filename)
    plt.close()

    bucket_name = 'trading_platform'
    destination_blob_name = f"charts/{filename}"
    
    # Upload the file to GCS
    public_url = upload_to_gcs(bucket_name, filename, destination_blob_name)
    
    # Optionally, remove the local file if you don't need to keep it
    os.remove(filename)

    return public_url

def get_shares_prices(db_connection, share_id):
    query = f"SELECT * FROM trades WHERE share_id = {share_id}"
    filename = f'prices_per_share_{share_id}.png'
    trades = pd.read_sql_query(query, db_connection)
    
    sns.lineplot(
        data=trades,
        x='transaction_time',
        y='price_total',
        hue='share_id',
        palette='husl',
        linewidth=2.5,
        markers=True,
        markersize=8,
    )

    plt.title('Price Total Over Time by Share ID', fontsize=16)
    plt.xlabel('Transaction Time', fontsize=14)
    plt.ylabel('Price Total', fontsize=14)
    plt.legend(title='Share ID', fontsize=12, title_fontsize=12)
    plt.savefig(filename)
    plt.close()

    bucket_name = 'trading_platform'
    destination_blob_name = f"charts/{filename}"
    
    # Upload the file to GCS
    public_url = upload_to_gcs(bucket_name, filename, destination_blob_name)
    
    # Optionally, remove the local file if you don't need to keep it
    os.remove(filename)

    return public_url

def get_trades_stock_ex(db_connection):
    query = "SELECT * FROM trades"
    filename = 'trades_per_stocks.png'
    trades = pd.read_sql_query(query, db_connection)
    trades_stock_ex_id = trades.groupby('stock_ex_id')['trade_id'].count()
    
    plt.pie(trades_stock_ex_id, labels=trades_stock_ex_id.index, autopct='%1.1f%%', startangle=140)
    plt.title('Proportion of Trades by Exchange', fontsize=16)
    plt.savefig(filename)
    plt.close()

    bucket_name = 'trading_platform'
    destination_blob_name = f"charts/{filename}"
    
    # Upload the file to GCS
    public_url = upload_to_gcs(bucket_name, filename, destination_blob_name)
    
    # Optionally, remove the local file if you don't need to keep it
    os.remove(filename)

    return public_url
