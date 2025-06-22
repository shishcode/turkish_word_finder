#!/usr/bin/env python3
"""
Test script to verify Tailwind CSS is working properly
"""

import os
import re

def test_tailwind_classes():
    """Test that Tailwind CSS classes are present in the built CSS"""
    css_file = "app/static/css/main.css"
    
    if not os.path.exists(css_file):
        print("❌ CSS file not found!")
        return False
    
    with open(css_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Common Tailwind classes used in the app
    expected_classes = [
        'container',
        'bg-white',
        'text-gray-800',
        'rounded-lg',
        'shadow-md',
        'p-6',
        'mb-6',
        'grid',
        'flex',
        'items-center',
        'justify-between',
        'space-y-4',
        'gap-4',
        'w-full',
        'px-4',
        'py-2',
        'border',
        'border-gray-300',
        'focus:ring-2',
        'focus:ring-blue-500',
        'hover:bg-blue-700',
        'transition-colors'
    ]
    
    missing_classes = []
    for class_name in expected_classes:
        # Convert class name to CSS selector
        css_selector = '.' + class_name.replace(':', '\\:')
        if css_selector not in content:
            missing_classes.append(class_name)
    
    if missing_classes:
        print(f"⚠️  Missing classes: {', '.join(missing_classes)}")
        return False
    else:
        print("✅ All expected Tailwind classes found!")
        return True

def test_css_size():
    """Test that CSS file has reasonable size"""
    css_file = "app/static/css/main.css"
    
    if not os.path.exists(css_file):
        return False
    
    size = os.path.getsize(css_file)
    print(f"📊 CSS file size: {size} bytes ({size/1024:.1f} KB)")
    
    # Should be between 5KB and 100KB
    if 5000 <= size <= 100000:
        print("✅ CSS file size is reasonable")
        return True
    else:
        print("⚠️  CSS file size seems unusual")
        return False

if __name__ == "__main__":
    print("🧪 Testing Tailwind CSS setup...")
    
    test1 = test_css_size()
    test2 = test_tailwind_classes()
    
    if test1 and test2:
        print("🎉 All tests passed! Tailwind CSS is working properly.")
    else:
        print("❌ Some tests failed. Please check the CSS build.") 