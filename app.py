from fastapi import FastAPI
from query_implementation import *
import mysql.connector

app = FastAPI()

db_connection = mysql.connector.connect(user='root', password=password,
                              host='127.0.0.1',
                              database='trading_platform')

@app.get("/query/{option}")
async def read_item(option: int):
   
    if option == 1:
        return get_brokers_list(db_connection)
    if option == 2:
        return get_shares_list(db_connection)
    if option == 3:
        return get_trade_list(db_connection)
    return 'Invalid option'

