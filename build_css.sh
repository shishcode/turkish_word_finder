#!/bin/bash

# Exit on any error
set -e

echo "Installing Node.js dependencies..."
npm install

echo "Building Tailwind CSS..."
npm run build:css

# Verify the build
if [ -f "app/static/css/main.css" ]; then
    echo "✅ CSS build successful!"
    echo "📁 Generated file: app/static/css/main.css"
    echo "📊 File size: $(du -h app/static/css/main.css | cut -f1)"
else
    echo "❌ CSS build failed!"
    exit 1
fi

# Set proper permissions
chmod -R 755 app/static/css/

echo "🎉 Build process completed successfully!" 