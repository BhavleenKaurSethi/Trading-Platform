'''
Export trades to excel (specifying zero or more of the following: share_id, broker_id, date_range) - > filters

Export Trade Data

---------------------------

1) Fetch Trades by Share_id

2) Fetch Trades by Broker_id

3) Fetch Trades by date_range

4) Return to Main menu
'''

import mysql.connector 
import pandas as pd
from datetime import datetime

def fethch_trade_share_id(db_connection):
    try:
        share_id = int(input('Enter share_id to search for a trade or press Enter: '))

        # Create a query
        query = f"SELECT * FROM trades WHERE share_id = {share_id}"

    except:
        print('Not a valid input.')
        print('Displaying all trade details')
        query = "SELECT * FROM trades"

    finally:

        # Use Pandas to read the query results
        result = pd.read_sql_query(query, db_connection)
        
        # Display the result
        return result


def fethch_trade_broker_id(db_connection):
    try:
        broker_id = int(input('Enter broker_id to search for a trade or press Enter: '))

        # Create a query
        query = f"SELECT * FROM trades WHERE broker_id = {broker_id}"

    except:
        print('Not a valid input.')
        print('Displaying all trade details')
        query = "SELECT * FROM trades"

    finally:

        # Use Pandas to read the query results
        result = pd.read_sql_query(query, db_connection)
        
        # Display the result
        return result

def fethch_trade_date_range(db_connection):
    try:
        date_range_min = input('Enter minimum limit for date_range to search trade or press enter')
        date_range_min = datetime.strptime(date_range_min, '%Y-%m-%d').date()

        date_range_max = input('Enter maximum limit for date_range to search trade or press enter')
        date_range_max = datetime.strptime(date_range_max, '%Y-%m-%d').date()

        # Create a query
        query = f"SELECT * FROM trades \
                WHERE transaction_time between '{date_range_min}' and '{date_range_max}'"

    except:
        print(date_range_min)
        print('Not a valid range.')
        print('Displaying all trade details')
        query = "SELECT * FROM trades"

    finally:

        # Use Pandas to read the query results
        result = pd.read_sql_query(query, db_connection)
        
        # Display the result
        return result