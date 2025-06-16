#!/bin/bash

# Install dependencies globally
npm install -g tailwindcss@latest postcss@latest autoprefixer@latest

# Create a temporary package.json for the build
echo '{
  "name": "temp-build",
  "version": "1.0.0",
  "private": true,
  "dependencies": {
    "tailwindcss": "latest",
    "postcss": "latest",
    "autoprefixer": "latest"
  }
}' > package.json

# Install dependencies
npm install

# Build CSS
npx tailwindcss -i ./app/static/css/tailwind.css -o ./app/static/css/main.css --minify

# Clean up
rm package.json
rm -rf node_modules

# Verify the build
if [ -f "app/static/css/main.css" ]; then
    echo "CSS build successful!"
    ls -l app/static/css/main.css
else
    echo "CSS build failed!"
    exit 1
fi

NODE_VERSION=20.11.1
NODE_ENV=production
TAILWIND_MODE=build 