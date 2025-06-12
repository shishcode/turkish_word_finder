import os
import re
from collections import Counter

def load_words(language='tr'):
    """Load the word list based on the selected language."""
    try:
        filename = 'words_en.txt' if language == 'en' else 'words.txt'
        filepath = os.path.join('data', filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            words = [word.strip() for word in file.readlines()]
            #print(f"Loaded {len(words)} words from {filename}")  # Debug print
            return words
    except FileNotFoundError:
        #print(f"Error: {filename} file not found!")  # Debug print
        return []
    except Exception as e:
        #print(f"Error reading {filename}: {str(e)}")  # Debug print
        return []

def parse_position_constraints(position_input):
    """Parse position constraints from input string."""
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

def search_words(params):
    """Search for words based on various criteria."""
    include_letters = [letter.strip().lower() for letter in params.get('include', '').split(',') if letter.strip()]
    exclude_letters = [letter.strip().lower() for letter in params.get('exclude', '').split(',') if letter.strip()]
    
    # Handle empty values for min and max length
    try:
        min_length = int(params.get('minLength', 0))
    except (ValueError, TypeError):
        min_length = 0
        
    try:
        max_length = int(params.get('maxLength', 0))
    except (ValueError, TypeError):
        max_length = 0
    
    contains = params.get('contains', '').strip().lower()
    starts_with = params.get('startsWith', '').strip().lower()
    ends_with = params.get('endsWith', '').strip().lower()
    position_constraints = parse_position_constraints(params.get('positionConstraints', ''))
    single_word = params.get('singleWord', False)
    language = params.get('language', 'tr')
    
    #print(f"Search request - Language: {language}, Include: {include_letters}, Exclude: {exclude_letters}, "
    #      f"Length: {min_length}-{max_length}, Starts: {starts_with}, Ends: {ends_with}, "
    #      f"Position Constraints: {position_constraints}, Single Word: {single_word}")
    
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

        # Skip if word doesn't contain the required substring
        if contains and contains.lower() not in word_lower:
            continue
            
        filtered_words.append(word)
    
    #print(f"Found {len(filtered_words)} matching words")  # Debug print
    return filtered_words 