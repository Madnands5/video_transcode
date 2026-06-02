#!/bin/bash

# Apply database migrations
echo "Applying migrations..."
python manage.py migrate

# Start the command passed to the container
exec "$@"