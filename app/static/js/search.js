async function searchWords() {
    const include = document.getElementById('include').value;
    const exclude = document.getElementById('exclude').value;
    const minLength = document.getElementById('minLength').value;
    const maxLength = document.getElementById('maxLength').value;
    const startsWith = document.getElementById('startsWith').value;
    const endsWith = document.getElementById('endsWith').value;
    const contains = document.getElementById('contains').value;
    const positionConstraints = document.getElementById('positionConstraints').value;
    const singleWord = document.getElementById('singleWord').checked;
    const language = document.getElementById('language').value;
    const resultsDiv = document.getElementById('results');
    const resultCount = document.getElementById('resultCount');
    
    try {
        const response = await fetch('/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 
                include, 
                exclude,
                minLength: minLength || 0,
                maxLength: maxLength || 0,
                startsWith,
                endsWith,
                contains,
                positionConstraints,
                singleWord,
                language
            })
        });
        
        const data = await response.json();
        
        // Update result count
        resultCount.textContent = `${data.count} words found`;
        
        // Clear previous results
        resultsDiv.innerHTML = '';
        
        // Display results
        if (data.words.length > 0) {
            data.words.forEach(word => {
                const wordElement = document.createElement('div');
                wordElement.className = 'p-3 bg-gray-50 rounded-md hover:bg-gray-100 transition-colors flex items-center justify-between';
                
                const wordText = document.createElement('span');
                wordText.className = 'text-lg font-medium text-gray-800';
                wordText.textContent = word;
                wordElement.appendChild(wordText);

                const translationButton = document.createElement('button');
                translationButton.className = 'text-blue-600 hover:text-blue-800 p-2 rounded-full hover:bg-blue-50 transition-colors relative group';
                translationButton.innerHTML = `
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path>
                    </svg>
                    <span class="absolute -top-8 right-0 bg-gray-800 text-white text-xs rounded py-1 px-2 opacity-0 group-hover:opacity-100 transition-opacity duration-200 whitespace-nowrap">
                        Show Translation
                    </span>
                `;
                translationButton.onclick = () => openTranslationModal(word);
                wordElement.appendChild(translationButton);
                
                resultsDiv.appendChild(wordElement);
            });
        } else {
            resultsDiv.innerHTML = '<div class="col-span-full text-gray-500 text-center py-4">No words found matching the criteria</div>';
        }
    } catch (error) {
        console.error('Error:', error);
        resultsDiv.innerHTML = '<div class="col-span-full text-red-500 text-center py-4">An error occurred while searching</div>';
    }
} 