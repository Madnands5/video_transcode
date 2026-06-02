# Use an official Python runtime
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (needed for ffmpeg)
RUN apt-get update && apt-get install -y build-essential libpq-dev ffmpeg && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .
COPY entrypoint.sh /usr/bin/
RUN chmod +x /usr/bin/entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["entrypoint.sh"]
# Expose Django port
EXPOSE 8000

# Start command (we will override this in docker-compose for the worker)
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]