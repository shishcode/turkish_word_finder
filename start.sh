#!/bin/bash

# Start script for Render.com
echo "Starting Word Finder application..."

# Set environment variables
export FLASK_ENV=production
export PYTHONPATH=/opt/render/project/src

# Start the application
exec gunicorn wsgi:app --workers 2 --bind 0.0.0.0:$PORT --timeout 120 --preload 