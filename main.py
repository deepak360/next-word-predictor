from flask import Flask, request, jsonify, render_template
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # Set this in your environment

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('word_suggestion.html')

@app.route("/next-word", methods=["POST"])
def predict_next_word():
    data = request.get_json()
    prompt = data.get("prompt", "").strip()

    if not prompt:
        return jsonify({"error": "Prompt is required"})

    try:
        openai.api_key = 'OPENAPI_SECRET_KEY'
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an assistant that predicts the next word."},
                {"role": "user", "content": f"Predict only the next word in this sentence:\n\n{prompt}"}
            ],
            max_tokens=15,
            temperature=0.7
        )

        next_word = response['choices'][0]['message']['content'].strip()
        return jsonify({"next_word": next_word})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
