# Use the official Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code to the working directory
COPY . /app

# Install the Python dependencies
RUN pip install -r requirements.txt

# Expose the port on which the application will run
EXPOSE 8080

# Run command
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]

# Define environment variable
#ENV NAME app

# Create an entrypoint script to run multiple commands
#COPY entrypoint.sh /app/entrypoint.sh
#RUN chmod +x /app/entrypoint.sh

# Use the entrypoint script to run commands
#ENTRYPOINT ["/app/entrypoint.sh"]
