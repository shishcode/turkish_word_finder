#!/bin/bash

# Development script for local development
echo "🚀 Starting development environment..."

# Install dependencies if not already installed
if [ ! -d "node_modules" ]; then
    echo "📦 Installing Node.js dependencies..."
    npm install
fi

# Start Tailwind CSS in watch mode
echo "👀 Starting Tailwind CSS in watch mode..."
npm run watch:css &

# Store the background process ID
TAILWIND_PID=$!

# Function to cleanup on exit
cleanup() {
    echo "🛑 Stopping development environment..."
    kill $TAILWIND_PID 2>/dev/null
    exit 0
}

# Set up signal handlers
trap cleanup SIGINT SIGTERM

echo "✅ Development environment started!"
echo "📝 Tailwind CSS is watching for changes..."
echo "🌐 Start your Flask app with: python run.py"
echo "🛑 Press Ctrl+C to stop"

# Wait for the background process
wait $TAILWIND_PID 