# Use an official Python runtime as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the entire Project_Vigilance directory into the container's /app directory
COPY Project_Vigilance /app

# Install the required Python libraries using pip
RUN pip install psycopg2 pandas psutil requests redis

# Set environment variables if needed
# ENV MY_VARIABLE=my_value

# Define the entry point for your application
CMD ["python3", "main.py"]
