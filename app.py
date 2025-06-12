from flask import Flask, render_template, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.json
    text = data.get('text')
    target_lang = data.get('lang')

    try:
        translated = translator.translate(text, dest=target_lang)
        return jsonify({
            'translated_text': translated.text
        })
    except Exception:
        return jsonify({'error': 'Translation failed. Please check language code or internet connection.'}), 500

if __name__ == '__main__':
    app.run(debug=True)

