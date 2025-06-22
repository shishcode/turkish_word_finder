#!/bin/bash

# Deployment script for Render.com
# This script can be used as a reference or for manual deployment

set -e

echo "🚀 Starting deployment process..."

# Install Python dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Install Node.js dependencies
echo "📦 Installing Node.js dependencies..."
npm install

# Build Tailwind CSS
echo "🎨 Building Tailwind CSS..."
npm run build:css

# Verify the build
echo "✅ Verifying build..."
python3 verify_build.py

# Test CSS
echo "🧪 Testing CSS..."
python3 test_css.py

# Set permissions
echo "🔐 Setting permissions..."
chmod -R 755 app/static/css/

echo "🎉 Deployment preparation completed!"
echo "📝 To start the application, run:"
echo "   gunicorn wsgi:app --workers 2 --bind 0.0.0.0:\$PORT --timeout 120" 