from flask import Flask, request, jsonify, render_template
from spellchecker import SpellChecker

app = Flask(__name__)
spell = SpellChecker()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/spell_check', methods=['POST'])
def spell_check():
    data = request.json
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    words = text.split()
    corrected_words = [spell.correction(word) if spell.correction(word) else word for word in words]

    # Identify corrected words and store them separately
    highlighted_text = []
    for original, corrected in zip(words, corrected_words):
        if original.lower() != corrected.lower():  # If the word was corrected
            highlighted_text.append(f'<span class="highlight">{corrected}</span>')
        else:
            highlighted_text.append(corrected)

    return jsonify({
        "original_text": text,
        "corrected_text": " ".join(corrected_words),
        "highlighted_text": " ".join(highlighted_text)
    })

if __name__ == '__main__':
    app.run(debug=True)
