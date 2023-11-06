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
from datetime import datetime

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
        
    # Save the result
    with open(filename, 'w') as f:
     
        # using csv.writer method from CSV package
        write = csv.writer(f)
        
        write.writerow(header)
        write.writerows(trades)

    return filename


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

    if (broker_id):
        query += f" AND broker_id = {broker_id}"

    cursor = db_connection.cursor()
    cursor.execute(query)
    header = [row[0] for row in cursor.description]
    trades = cursor.fetchall()
    cursor.close()
        
    # Save the result
    with open(filename, 'w') as f:
     
        # using csv.writer method from CSV package
        write = csv.writer(f)
        
        write.writerow(header)
        write.writerows(trades)

    return filename

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

    filename = 'trade_filtered_by_transaction_time.csv'

    if (date_range_min):
        date_range_min = datetime.strptime(date_range_min, '%Y-%m-%d').date()
        query += f" AND transaction_time >= '{date_range_min}'"
    
    if (date_range_max):
        date_range_max = datetime.strptime(date_range_max, '%Y-%m-%d').date()
        query += f" AND transaction_time <= '{date_range_max}'"

    cursor = db_connection.cursor()
    cursor.execute(query)
    header = [row[0] for row in cursor.description]
    trades = cursor.fetchall()
    cursor.close()
        
    # Save the result
    with open(filename, 'w') as f:
     
        # using csv.writer method from CSV package
        write = csv.writer(f)
        
        write.writerow(header)
        write.writerows(trades)

    return filename