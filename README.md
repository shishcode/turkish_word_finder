# Turkish Word Finder

A powerful web application for finding Turkish words based on various filtering criteria. This tool is particularly useful for word games, language learning, and word puzzle solving.

## Features

### Advanced Word Filtering
- **Position-Specific Constraints**: Specify allowed letters for specific positions (e.g., "1EF" means first letter must be E or F)
- **Include/Exclude Letters**: Filter words containing or excluding specific letters
- **Length Filter**: Set minimum and maximum word length
- **Prefix/Suffix Filter**: Find words starting or ending with specific letters
- **Case-Insensitive**: Works with both uppercase and lowercase letters
- **Turkish Character Support**: Fully supports Turkish alphabet and special characters

### User Interface
- Clean, modern web interface built with Flask and Tailwind CSS
- Real-time search results
- Responsive design for both desktop and mobile
- Scrollable results area with word count
- Clear input validation and error handling

## Usage Examples

### Position Constraints
```
1EF 4CED
```
- First letter must be E or F
- Fourth letter must be C, E, or D

### Letter Filters
```
Include: a,e,i
Exclude: x,y,z
```
- Words must contain all letters: a, e, and i
- Words must not contain any of: x, y, or z

### Length Filter
```
Minimum Length: 4
Maximum Length: 8
```
- Find words between 4 and 8 letters long

### Prefix/Suffix
```
Starts With: ab
Ends With: er
```
- Find words starting with "ab" and ending with "er"

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/turkish-word-finder.git
cd turkish-word-finder
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

## Requirements
- Python 3.6+
- Flask 3.0.2
- A words.txt file containing Turkish words (one word per line)

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details. 