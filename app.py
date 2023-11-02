from fastapi import FastAPI
from query_implementation import *
import mysql.connector

app = FastAPI()

db_connection = mysql.connector.connect(user='root', password='Harjas1703.',
                              host='127.0.0.1',
                              database='trading_platform')

@app.get("/query/{option}")
async def read_item(option: int, share_id: int | None = None,
                    broker_id: int | None = None,
                    date_range_min: str | None = None,
                    date_range_max: str | None = None):
   
    if option == 1:
        return get_brokers_list(db_connection)
    if option == 2:
        return get_shares_list(db_connection)
    if option == 3:
        return get_trade_list(db_connection)
    if option == 4:
        return search_trade(db_connection, share_id, broker_id, date_range_min, date_range_max)  
    return 'Invalid option'

