# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy project files to the working directory
COPY requirements.txt ./
COPY main.py app.py best_heart_model.pkl start.sh ./

# Install required Python libraries from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make the start.sh script executable
RUN chmod +x start.sh

# Expose ports for FastAPI (8089) and Streamlit (8501)
EXPOSE 8089 8501

# Use the start.sh script to launch both FastAPI and Streamlit
CMD ["./start.sh"]
