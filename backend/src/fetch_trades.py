'''
Export trades to excel (specifying zero or more of the following: share_id, broker_id, date_range) - > filters

Export Trade Data

---------------------------

1) Fetch Trades by Share_id

2) Fetch Trades by Broker_id

3) Fetch Trades by date_range

4) Return to Main menu
'''

import csv
import os
from datetime import datetime, timedelta  
from google.cloud import storage
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    './trading-platform-404001-c56c24689187.json'
)

# Function to upload file to GCS and return the blob's public URL
def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket and make it publicly readable."""
    storage_client = storage.Client(credentials=credentials)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)
    # Generate a signed URL for the blob that expires in one hour
    url = blob.generate_signed_url(expiration=timedelta(hours=1))

    return url

def fetch_trade_share_id(db_connection, share_id):

    query = """
    SELECT t.trade_id, t.share_id, b.broker_id, 
        CONCAT(b.first_name, ' ', b.last_name) as full_name,
        t.stock_ex_id, s.name, t.transaction_time, 
        t.share_amount, t.price_total
    FROM trades AS t
    INNER JOIN brokers AS b ON t.broker_id = b.broker_id
    INNER JOIN stock_exchanges AS s ON t.stock_ex_id = s.stock_ex_id
    WHERE 1 = 1 
    """

    filename = 'trade_filtered_by_share_id.csv'

    if (share_id):
        query += f" AND share_id = {share_id}"

    cursor = db_connection.cursor()
    cursor.execute(query)
    header = [row[0] for row in cursor.description]
    trades = cursor.fetchall()
    cursor.close()

    bucket_name = 'trading_platform'  
    destination_blob_name = f"csv/{filename}" 
        
    # Save the result
    with open(filename, 'w') as f:
     
        # using csv.writer method from CSV package
        write = csv.writer(f)
        
        write.writerow(header)
        write.writerows(trades)

     # Upload the file
    public_url = upload_to_gcs(bucket_name, filename, destination_blob_name)
    
    # Optionally, remove the local file if you don't need to keep it
    os.remove(filename)

    return public_url


# This is just a modification for the fetch_trade_broker_id function
# You would need to make similar changes to the fetch_trade_date_range function as well.

def fetch_trade_broker_id(db_connection, broker_id):
    query = """
    SELECT t.trade_id, t.share_id, b.broker_id, 
        CONCAT(b.first_name, ' ', b.last_name) as full_name,
        t.stock_ex_id, s.name, t.transaction_time, 
        t.share_amount, t.price_total
    FROM trades AS t
    INNER JOIN brokers AS b ON t.broker_id = b.broker_id
    INNER JOIN stock_exchanges AS s ON t.stock_ex_id = s.stock_ex_id
    WHERE 1 = 1 
    """

    filename = 'trade_filtered_by_broker_id.csv'

    if broker_id:
        query += f" AND t.broker_id = {broker_id}"

    cursor = db_connection.cursor()
    cursor.execute(query)
    header = [row[0] for row in cursor.description]
    trades = cursor.fetchall()
    cursor.close()

    bucket_name = 'trading_platform'  
    destination_blob_name = f"csv/{filename}"

    # Save the result
    with open(filename, 'w', newline='') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)
        write.writerow(header)
        write.writerows(trades)

    # Upload the file to GCS
    public_url = upload_to_gcs(bucket_name, filename, destination_blob_name)
    
    # Optionally, remove the local file if you don't need to keep it
    os.remove(filename)

    return public_url

def fetch_trade_date_range(db_connection, date_range_min, date_range_max):
    
    query = """
    SELECT t.trade_id, t.share_id, b.broker_id, 
        CONCAT(b.first_name, ' ', b.last_name) as full_name,
        t.stock_ex_id, s.name, t.transaction_time, 
        t.share_amount, t.price_total
    FROM trades AS t
    INNER JOIN brokers AS b ON t.broker_id = b.broker_id
    INNER JOIN stock_exchanges AS s ON t.stock_ex_id = s.stock_ex_id
    WHERE 1 = 1 
    """

    filename = 'trade_filtered_by_date_range.csv'

    if date_range_min:
        date_range_min = datetime.strptime(date_range_min, '%Y-%m-%d').date()
        query += f" AND transaction_time >= '{date_range_min}'"
    
    if date_range_max:
        date_range_max = datetime.strptime(date_range_max, '%Y-%m-%d').date()
        query += f" AND transaction_time <= '{date_range_max}'"

    cursor = db_connection.cursor()
    cursor.execute(query)
    header = [row[0] for row in cursor.description]
    trades = cursor.fetchall()
    cursor.close()

    bucket_name = 'trading_platform'  
    destination_blob_name = f"csv/{filename}"

    # Save the result
    with open(filename, 'w', newline='') as f:
        # using csv.writer method from CSV package
        write = csv.writer(f)
        write.writerow(header)
        write.writerows(trades)

    # Upload the file to GCS
    public_url = upload_to_gcs(bucket_name, filename, destination_blob_name)
    
    # Optionally, remove the local file if you don't need to keep it
    os.remove(filename)

    return public_url
