import os
import sys

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from config import config

# Create the application instance
app = create_app(config['production'])

# For debugging
if __name__ == '__main__':
    print("WSGI Application initialized")
    print(f"Python path: {sys.path}")
    print(f"Current directory: {os.getcwd()}") 