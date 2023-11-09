#!/bin/sh

# Start the cloud SQL proxy in the background
./cloud-sql-proxy trading-platform-404001:us-central1:trade-db -u=cloudsql &

# Run the FastAPI application using uvicorn with reload
uvicorn app:app --host 0.0.0.0 --port 80
