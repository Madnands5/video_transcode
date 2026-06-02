#!/bin/bash
# backend/entrypoint.sh

# Apply database migrations
echo "Applying migrations..."
python manage.py migrate

# Start the command passed to the container (e.g., gunicorn or celery)
exec "$@"