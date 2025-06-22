#!/usr/bin/env python3
"""
Build verification script for Tailwind CSS
Checks if the main.css file exists and contains Tailwind CSS content
"""

import os
import sys

def verify_css_build():
    """Verify that Tailwind CSS was built successfully"""
    css_file = "app/static/css/main.css"
    
    print("🔍 Verifying Tailwind CSS build...")
    
    # Check if file exists
    if not os.path.exists(css_file):
        print(f"❌ Error: {css_file} not found!")
        return False
    
    # Check file size
    file_size = os.path.getsize(css_file)
    print(f"📊 File size: {file_size} bytes")
    
    if file_size < 1000:  # Less than 1KB is suspicious
        print("⚠️  Warning: CSS file seems too small")
        return False
    
    # Check if file contains Tailwind CSS content
    try:
        with open(css_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check for Tailwind CSS indicators
        tailwind_indicators = [
            'tailwindcss',
            '--tw-',
            '.container',
            '.bg-',
            '.text-',
            '.p-',
            '.m-'
        ]
        
        found_indicators = sum(1 for indicator in tailwind_indicators if indicator in content)
        
        if found_indicators >= 3:
            print("✅ Tailwind CSS build verified successfully!")
            print(f"   Found {found_indicators} Tailwind CSS indicators")
            return True
        else:
            print("❌ Error: CSS file doesn't appear to contain Tailwind CSS")
            return False
            
    except Exception as e:
        print(f"❌ Error reading CSS file: {e}")
        return False

if __name__ == "__main__":
    success = verify_css_build()
    sys.exit(0 if success else 1) 