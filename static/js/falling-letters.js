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
}); 