from flask import Flask, render_template, request
import json
import pickle
from preprocessor.cleaner import clean_text
from config import STOP_WORDS


app = Flask(__name__)


with open('model/vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)


with open('model/model.pkl', 'rb') as file:
    model = pickle.load(file)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/prediction', methods=['POST', 'GET'])
def predict_sentiment(data=None):
    if request.method == 'POST':
        text = request.form.get('api parammmmmmmmmmm')
        cleaned_text = clean_text(text, stop_words=STOP_WORDS)
        vector = vectorizer.transform([cleaned_text])
        result = model.predict(vector)[0]
        if result == -1:
            return "0"
        else:
            return "1"
    if request.method == 'GET':
        return "0"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
