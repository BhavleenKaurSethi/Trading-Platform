from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from query_implementation import *
from fetch_trades import *
from create_visualisation import *
import mysql.connector
import os

app = FastAPI()

DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASS', 'password123')
DB_NAME = os.getenv('DB_NAME', 'trading_platform')
DB_SOCKET_DIR = os.getenv('DB_SOCKET_DIR', '/cloudsql')
INSTANCE_CONNECTION_NAME = os.getenv('INSTANCE_CONNECTION_NAME', 'trading-platform-404001:australia-southeast1:trading-db' )

def get_db_connection():
    connection = mysql.connector.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        unix_socket=f"{DB_SOCKET_DIR}/{INSTANCE_CONNECTION_NAME}",
        database=DB_NAME,
    )
    return connection

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

def db_connection():
    db = get_db_connection()
    try:
        yield db
    finally:
        db.close()

@app.get("/query/{option}")
async def read_item(option: int, share_id: int | None = None,
                    broker_id: int | None = None,
                    date_range_min: str | None = None,
                    date_range_max: str | None = None,
                    db: mysql.connector.connection = Depends(db_connection)):
   
    if option == 1:
        return get_brokers_list(db)
    if option == 2:
        return get_shares_list(db)
    if option == 3:
        return get_trade_list(db)
    if option == 4:
        return search_trade(db, share_id, broker_id, date_range_min, date_range_max)  
    return 'Invalid option'

@app.get("/export/{option}")
async def read_item(option: int, share_id: int | None = None,
                    broker_id: int | None = None,
                    date_range_min: str | None = None,
                    date_range_max: str | None = None,
                    db: mysql.connector.connection = Depends(db_connection)):
   
    if option == 1:
        return fetch_trade_share_id(db, share_id)
    if option == 2:
        return fetch_trade_broker_id(db, broker_id)
    if option == 3:
        return fetch_trade_date_range(db, date_range_min, date_range_max) 
    return 'Invalid option'

@app.get("/report/{option}")
async def read_item(option: int, db: mysql.connector.connection = Depends(db_connection)):
   
    if option == 1:
        return get_trades_per_broker(db)
    if option == 2:
        return get_shares_prices(db)
    if option == 3:
        return get_trades_stock_ex(db)
    return 'Invalid option'