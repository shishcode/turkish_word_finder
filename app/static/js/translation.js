function openTranslationModal(word) {
    const modal = document.getElementById('translationModal');
    const frame = document.getElementById('translationFrame');
    document.body.classList.add('modal-open');
    frame.src = `https://tureng.com/tr/turkce-ingilizce/${word.toLowerCase()}`;
    modal.classList.add('show');
}

function closeTranslationModal() {
    const modal = document.getElementById('translationModal');
    document.body.classList.remove('modal-open');
    modal.classList.remove('show');
    const frame = document.getElementById('translationFrame');
    frame.src = 'about:blank';
} 