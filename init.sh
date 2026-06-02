#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "🚀 Starting project initialization..."

# 1. Setup Backend environment file if it doesn't exist
if [ ! -f "backend/.env" ]; then
    echo "Creating backend/.env..."
    cp backend/.env.example backend/.env 2>/dev/null || touch backend/.env
    echo "SECRET_KEY=dev-secret-key" >> backend/.env
    echo "REDIS_URL=redis://redis:6379/0" >> backend/.env
fi

# 2. Setup Frontend environment file if it doesn't exist
if [ ! -f "frontend/.env" ]; then
    echo "Creating frontend/.env..."
    touch frontend/.env
    echo "API_URL=http://localhost:8000" >> frontend/.env
fi

# 3. Ensure the services/ directory exists in backend
mkdir -p backend/config/services
touch backend/config/services/__init__.py

# 4. Prepare Docker
echo "🏗 Building Docker containers..."
docker-compose build

# 5. Run initial migrations (optional, only if backend is ready)
echo "📦 Running database migrations..."
docker-compose run --rm backend python manage.py migrate

echo "✅ Initialization complete! Run 'docker-compose up' to start."