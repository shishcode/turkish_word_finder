# Multi-Language Word Finder Application

A powerful word search application that helps users find words based on various criteria. The application supports Turkish, English, and French languages and includes a translation feature.

## Features

### Word Search Capabilities
- **Language Selection**: Switch between Turkish, English, and French word databases
- **Pattern Matching**:
  - Start with specific letters
  - Contains substring
  - End with specific letters
  - Include specific letters
  - Exclude specific letters
  - Position-based constraints
- **Length Control**:
  - Set minimum word length
  - Set maximum word length
- **Word Type Filtering**:
  - Option to show only single words (no spaces)
  - Filter out compound words or phrases

### User Interface
- **Modern Design**:
  - Clean and intuitive interface
  - Responsive layout
  - Beautiful falling letters animation in the background
  - Smooth transitions and animations
- **Layout Features**:
  - Centered main content (50% width)
  - Responsive design for all screen sizes
  - Smooth transitions between states

### Translation Integration
- **Built-in Translation**:
  - Direct integration with Tureng.com
  - Side panel translation view
  - Smooth panel transitions
  - Maintains context while translating

### Visual Effects
- **Dynamic Background**:
  - Colorful falling letters animation
  - Multiple color variations
  - Smooth rotation effects
  - Non-intrusive design
- **Responsive Layout**:
  - Main content adjusts to 66% width when translation panel is open
  - Smooth transitions between states
  - Mobile-friendly design

## Technical Details

### Frontend
- HTML5
- CSS3 with modern features
- JavaScript (ES6+)
- Tailwind CSS for styling
- Responsive design principles

### Backend
- Python
- Flask framework
- Efficient word processing algorithms

### Word Databases
- **Turkish**: 76,186 words (`data/words.txt`)
- **English**: 370,105 words (`data/words_en.txt`)
- **French**: 22,740 words (`data/words_fr.txt`)

## Tailwind CSS Setup

This project uses Tailwind CSS for styling with a robust build process optimized for deployment on Render.com.

### Local Development

1. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

2. **Start development mode (with CSS watching):**
   ```bash
   ./dev.sh
   ```

3. **Build CSS manually:**
   ```bash
   npm run build:css
   ```

4. **Verify the build:**
   ```bash
   python3 verify_build.py
   ```

### Production Deployment

The project is configured for automatic deployment on Render.com with the following features:

- **Automatic CSS Build**: Tailwind CSS is built during deployment
- **Build Verification**: Ensures CSS is properly generated
- **Fallback CDN**: Uses Tailwind CDN if build fails
- **Optimized Output**: Minified CSS for production

### Build Process

1. **Dependencies**: Uses `package.json` for Node.js dependency management
2. **Build Script**: `npm run build:css` compiles Tailwind CSS
3. **Verification**: `verify_build.py` checks build success
4. **Fallback**: Automatic CDN fallback if build fails

### File Structure

```
├── app/static/css/
│   ├── tailwind.css      # Tailwind directives
│   ├── main.css          # Generated CSS (built)
│   ├── style.css         # Custom styles
│   └── falling-letters.css
├── data/
│   ├── words.txt         # Turkish word database
│   ├── words_en.txt      # English word database
│   └── words_fr.txt      # French word database
├── package.json          # Node.js dependencies
├── tailwind.config.js    # Tailwind configuration
├── postcss.config.js     # PostCSS configuration
├── build_css.sh          # Build script
├── verify_build.py       # Build verification
└── render.yaml           # Render.com configuration
```

## Getting Started

1. Clone the repository
2. Install Python dependencies: `pip install -r requirements.txt`
3. Install Node.js dependencies: `npm install`
4. Build CSS: `npm run build:css`
5. Run the application: `python3 run.py`
6. Access through your web browser

## Usage

1. Select your preferred language (Turkish/English/French)
2. Enter your search criteria
3. Click "Search" to find matching words
4. Click the eye icon next to any word to see its translation
5. Use the translation panel to view detailed translations

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.

## License

This project is licensed under the MIT License.

## Author

FUZ SR 