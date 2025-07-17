document.addEventListener('DOMContentLoaded', function() {
    const container = document.querySelector('.falling-letters');
    const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const numLetters = 40;
    
    // Array of colors for the letters
    const colors = [
        '#FF6B6B', // Coral Red
        '#4ECDC4', // Turquoise
        '#45B7D1', // Sky Blue
        '#96CEB4', // Sage Green
        '#FFEEAD', // Cream Yellow
        '#D4A5A5', // Dusty Rose
        '#9B59B6', // Purple
        '#3498DB', // Blue
        '#E67E22', // Orange
        '#2ECC71'  // Green
    ];

    function getRandomColor() {
        return colors[Math.floor(Math.random() * colors.length)];
    }

    function createLetter() {
        const letter = document.createElement('div');
        letter.className = 'letter';
        letter.textContent = letters[Math.floor(Math.random() * letters.length)];
        letter.style.left = Math.random() * 100 + 'vw';
        letter.style.animationDuration = (Math.random() * 5 + 4) + 's';
        letter.style.opacity = Math.random() * 0.3 + 0.4;
        letter.style.color = getRandomColor();
        
        // Add some random rotation to the initial state
        const initialRotation = Math.random() * 360;
        letter.style.transform = `rotate(${initialRotation}deg)`;
        
        container.appendChild(letter);

        letter.addEventListener('animationend', () => {
            letter.remove();
            createLetter();
        });
    }

    // Create initial letters with staggered timing
    for (let i = 0; i < numLetters; i++) {
        setTimeout(() => {
            createLetter();
        }, i * 150);
    }

    // --- Falling Phrases Logic ---
    const phrases = [
        'WORDLE SOLVER',
        'WORD FINDER',
        'ANAGRAM FINDER',
        'REBUS HELPER',
        'CROSSWORD SOLVER',
        'SCRABBLE HELPER'
    ];

    // --- Dissolving Phrases Logic ---
    let currentPhraseIndex = 0;
    function showDissolvingPhrase() {
        // Use the navbar brand container for phrases
        const navbarBrand = document.getElementById('dissolving-phrases-navbar');
        if (!navbarBrand) return;
        // Remove any existing phrase
        const existing = navbarBrand.querySelector('.falling-phrase');
        if (existing) existing.remove();
        const phrase = document.createElement('span');
        phrase.className = 'falling-phrase';
        phrase.textContent = phrases[currentPhraseIndex];
        phrase.style.color = getRandomColor();
        phrase.style.opacity = 1;
        navbarBrand.appendChild(phrase);    

        // Prepare next phrase index
        currentPhraseIndex = (currentPhraseIndex + 1) % phrases.length;

        // Show for a while, then dissolve, then after dissolve, show next
        setTimeout(() => {
            phrase.classList.add('dissolve');
            phrase.addEventListener('animationend', () => {
                phrase.remove();
                setTimeout(showDissolvingPhrase, 100); // show next after dissolve
            }, { once: true });
        }, 1200); // show for 1.2s before dissolving
    }

    // Start the dissolve phrase loop
    showDissolvingPhrase();
}); 