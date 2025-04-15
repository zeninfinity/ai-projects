# Use official Python image as base
FROM python:3.10-slim

# Set working directory in container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy your code
COPY . /app

# Command to run the app
CMD ["python", "run_model.py"]
