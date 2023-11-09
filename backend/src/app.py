from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from query_implementation import *
from fetch_trades import *
from create_visualisation import *
import mysql.connector

app = FastAPI()

origins = [
    "https://my-react-app-7fft7bnqha-ts.a.run.app",
    "http://localhost:3000",  
    "http://localhost:8000",  
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

db_connection = mysql.connector.connect(unix_socket= 'cloudsql/trading-platform-404001:us-central1:trade-db',
                                        user= 'root',
                                        password= 'Password123',
                                        database= 'trading_platform')


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

@app.get("/export/{option}")
async def read_item(option: int, share_id: int | None = None,
                    broker_id: int | None = None,
                    date_range_min: str | None = None,
                    date_range_max: str | None = None):
   
    if option == 1:
        return fetch_trade_share_id(db_connection, share_id)
    if option == 2:
        return fetch_trade_broker_id(db_connection, broker_id)
    if option == 3:
        return fetch_trade_date_range(db_connection, date_range_min, date_range_max) 
    return 'Invalid option'

@app.get("/report/{option}")
async def read_item(option: int):
   
    if option == 1:
        return get_trades_per_broker(db_connection)
    if option == 2:
        return get_shares_prices(db_connection)
    if option == 3:
        return get_trades_stock_ex(db_connection)
    return 'Invalid option'