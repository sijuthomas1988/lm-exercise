# Use the official Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8080

# Run the FastAPI application using uvicorn server
CMD ["fastapi", "run", "app/main.py", "--port", "8080"]