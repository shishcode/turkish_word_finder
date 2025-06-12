from flask import Blueprint, render_template, request, jsonify
from app.utils import search_words

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'version': '1.0.0'
    }), 200

@main.route('/search', methods=['POST'])
def search():
    data = request.get_json()
    words = search_words(data)
    
    return jsonify({
        'count': len(words),
        'words': words
    }) 