from flask import Flask, render_template, request, jsonify
import os
import re

app = Flask(__name__)

def load_words(language='tr'):
    try:
        filename = 'words_en.txt' if language == 'en' else 'words.txt'
        with open(filename, 'r', encoding='utf-8') as file:
            words = [word.strip() for word in file.readlines()]
            print(f"Loaded {len(words)} words from {filename}")  # Debug print
            return words
    except FileNotFoundError:
        print(f"Error: {filename} file not found!")  # Debug print
        return []
    except Exception as e:
        print(f"Error reading {filename}: {str(e)}")  # Debug print
        return []

def parse_position_constraints(position_input):
    constraints = {}
    if not position_input:
        return constraints
        
    # Split by spaces to handle multiple position constraints
    parts = position_input.strip().split()
    for part in parts:
        # Match pattern like "1ABC" or "4XYZ"
        match = re.match(r'(\d+)([A-Za-z]+)', part)
        if match:
            position = int(match.group(1))
            allowed_chars = set(match.group(2).lower())
            constraints[position - 1] = allowed_chars  # Convert to 0-based index
    return constraints

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    include_letters = [letter.strip().lower() for letter in data.get('include', '').split(',') if letter.strip()]
    exclude_letters = [letter.strip().lower() for letter in data.get('exclude', '').split(',') if letter.strip()]
    min_length = int(data.get('minLength', 0))
    max_length = int(data.get('maxLength', 0))
    starts_with = data.get('startsWith', '').strip().lower()
    ends_with = data.get('endsWith', '').strip().lower()
    position_constraints = parse_position_constraints(data.get('positionConstraints', ''))
    single_word = data.get('singleWord', False)
    language = data.get('language', 'tr')
    
    print(f"Search request - Language: {language}, Include: {include_letters}, Exclude: {exclude_letters}, Length: {min_length}-{max_length}, Starts: {starts_with}, Ends: {ends_with}, Position Constraints: {position_constraints}, Single Word: {single_word}")
    
    words = load_words(language)
    filtered_words = []
    
    for word in words:
        word_lower = word.lower()
        
        # Check if word contains spaces (for single word filter)
        if single_word and ' ' in word:
            continue
            
        # Check word length
        if min_length > 0 and len(word) < min_length:
            continue
        if max_length > 0 and len(word) > max_length:
            continue
            
        # Check if word starts with
        if starts_with and not word_lower.startswith(starts_with):
            continue
            
        # Check if word ends with
        if ends_with and not word_lower.endswith(ends_with):
            continue
            
        # Check position constraints
        position_valid = True
        for pos, allowed_chars in position_constraints.items():
            if pos >= len(word_lower) or word_lower[pos] not in allowed_chars:
                position_valid = False
                break
        if not position_valid:
            continue
            
        # Check if word contains all include letters
        if include_letters and not all(letter in word_lower for letter in include_letters):
            continue
            
        # Check if word contains any exclude letters
        if exclude_letters and any(letter in word_lower for letter in exclude_letters):
            continue
            
        filtered_words.append(word)
    
    print(f"Found {len(filtered_words)} matching words")  # Debug print
    
    return jsonify({
        'count': len(filtered_words),
        'words': filtered_words
    })

if __name__ == '__main__':
    app.run(debug=True) 