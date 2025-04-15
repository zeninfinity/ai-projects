# Use a Python base image
FROM python:3.10-slim

RUN apt-get update && apt-get install -y git

# Set working directory inside the container
WORKDIR /app

# Copy the local requirements.txt to the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the code to the container
COPY run_model.py /app/

# Run the model when the container starts
CMD ["python", "run_model.py"]
