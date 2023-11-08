# Use the official Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
#RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install -r requirements.txt

# Copy the application code to the working directory
COPY . /app

# Expose the port on which the application will run
EXPOSE 80

# Define environment variable
ENV NAME app.py

# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "app:app", "--reload"]