'''
Phase 2 – Query Sub-menu: presenting data from SQL queries

Implement a “query” sub menu with the following options:

Query

---------------------------

1) List Brokers

2) List all Shares (should include company name)

3) Lookup trade by trade id (shows all trade details)

4) Search for trade (specifying one or more of the following: share_id, broker_id, date_range)

5) Return to main menu
'''

from datetime import datetime

# List Brokers
def get_brokers_list(db_connection):

    query = """
    SELECT * 
    FROM brokers;
    """

    cursor = db_connection.cursor()
    cursor.execute(query)
    header = [row[0] for row in cursor.description]
    brokers = cursor.fetchall()
    cursor.close()

    # Concat header with fetch rows
    brokers_list = [header] + brokers
    return brokers_list

# List all Shares (should include company name)
def get_shares_list(db_connection):

    query = """
    SELECT companies.company_id, name, share_id, currency_id 
    FROM shares 
    INNER JOIN companies;
    """

    cursor = db_connection.cursor()
    cursor.execute(query)
    header = [row[0] for row in cursor.description]
    shares = cursor.fetchall()
    cursor.close()

    # Concat header with fetch rows
    shares_list = [header] + shares
    return shares_list

# Lookup trade by trade id (shows all trade details)
def get_trade_list(db_connection):

    query = """
    SELECT t.trade_id, t.share_id, b.broker_id, 
        CONCAT(b.first_name, ' ', b.last_name) as full_name,
        t.stock_ex_id, s.name, t.transaction_time, 
        t.share_amount, t.price_total
    FROM trades AS t
    INNER JOIN brokers AS b ON t.broker_id = b.broker_id
    INNER JOIN stock_exchanges AS s ON t.stock_ex_id = s.stock_ex_id;
    """

    cursor = db_connection.cursor()
    cursor.execute(query)
    header = [row[0] for row in cursor.description]
    trades = cursor.fetchall()
    cursor.close()

    # Concat header with fetch rows
    trades_list = [header] + trades
    return trades_list

#Search for trade (specifying one or more of the following: share_id, broker_id, date_range)
def search_trade(db_connection, share_id, broker_id, date_range_min, date_range_max):

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

    if (share_id):
        query += f" AND share_id = {share_id}"

    if (broker_id):
        query += f" AND t.broker_id = {broker_id}"
    
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

    # Concat header with fetch rows
    trades_list = [header] + trades

    return trades_list
