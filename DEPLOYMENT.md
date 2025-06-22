# Deployment Guide for Render.com

This guide covers the deployment process and troubleshooting for the Word Finder application on Render.com.

## Quick Fix for Current Error

The error you're seeing is because Render.com is using the wrong start command. Here's how to fix it:

### Option 1: Update Render.com Settings (Recommended)

1. Go to your Render.com dashboard
2. Navigate to your web service
3. Go to **Settings** → **Build & Deploy**
4. Update the **Start Command** to:
   ```
   gunicorn wsgi:app --workers 2 --bind 0.0.0.0:$PORT --timeout 120
   ```
5. Update the **Build Command** to:
   ```bash
   pip install -r requirements.txt && npm install && npm run build:css && python3 verify_build.py
   ```

### Option 2: Use render.yaml (Automatic)

The `render.yaml` file is already configured correctly. If you're using it, the deployment should work automatically.

## Build Process

The deployment process includes:

1. **Python Dependencies**: `pip install -r requirements.txt`
2. **Node.js Dependencies**: `npm install`
3. **Tailwind CSS Build**: `npm run build:css`
4. **Build Verification**: `python3 verify_build.py`
5. **Application Start**: `gunicorn wsgi:app`

## File Structure

```
├── wsgi.py              # WSGI entry point
├── app/
│   ├── __init__.py      # Flask app factory
│   ├── routes.py        # Application routes
│   └── static/css/
│       ├── main.css     # Built Tailwind CSS
│       └── tailwind.css # Tailwind directives
├── package.json         # Node.js dependencies
├── render.yaml          # Render.com configuration
└── Procfile            # Alternative deployment
```

## Troubleshooting

### Common Errors

#### 1. "Failed to find attribute 'app' in 'app'"
**Cause**: Wrong start command
**Solution**: Use `gunicorn wsgi:app` instead of `gunicorn app:app`

#### 2. CSS not loading
**Cause**: Tailwind CSS build failed
**Solution**: 
- Check build logs for npm errors
- Verify `package.json` exists
- Ensure Node.js version is >=18.0.0

#### 3. Health check failing
**Cause**: Missing health route
**Solution**: The `/health` route is now included in `app/routes.py`

### Manual Testing

Test locally before deploying:

```bash
# Install dependencies
pip install -r requirements.txt
npm install

# Build CSS
npm run build:css

# Verify build
python3 verify_build.py

# Test application
python3 -c "from wsgi import app; print('✅ App loaded')"

# Run locally
python3 run.py
```

### Environment Variables

Make sure these are set in Render.com:

- `PYTHON_VERSION`: 3.9.0
- `NODE_VERSION`: 20.11.1
- `FLASK_ENV`: production
- `SECRET_KEY`: (your secret key)

## Alternative Deployment Methods

### Using Procfile
If `render.yaml` doesn't work, you can use the `Procfile`:
```
web: gunicorn wsgi:app --workers 2 --bind 0.0.0.0:$PORT --timeout 120
```

### Manual Deployment Script
Run `./deploy.sh` for manual deployment preparation.

## Monitoring

After deployment, check:

1. **Build Logs**: Ensure all steps completed successfully
2. **Health Check**: Visit `/health` endpoint
3. **CSS Loading**: Check browser developer tools
4. **Application Logs**: Monitor for runtime errors

## Support

If you continue to have issues:

1. Check the build logs in Render.com dashboard
2. Verify all files are committed to your repository
3. Test the application locally first
4. Ensure all dependencies are properly specified 