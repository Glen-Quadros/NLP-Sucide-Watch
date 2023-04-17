from django.shortcuts import render
from django.http import JsonResponse
import joblib
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import nltk
import re

final_model = joblib.load("/Users/glenquadros/Python/Internship Assignments/Cerina Internship/final_model.pkl")
vectorizer = joblib.load("/Users/glenquadros/Python/Internship Assignments/Cerina Internship/vectorizer.pkl")

def preprocess_text(text):
    tokens = nltk.word_tokenize(text.lower())
    stop_words = set(nltk.corpus.stopwords.words("english"))
    tokens = [token for token in tokens if token not in stop_words and token.isalnum()]
    lemmatizer = nltk.stem.WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return " ".join(tokens)

def home(request):
    return render(request, 'home.html')

def result(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            text = re.sub(r'http\S+', '', text)  # Remove URLs from text
            text = preprocess_text(text)  # Preprocess text
            X = vectorizer.transform([text])
            prediction = final_model.predict(X)[0]
            return render(request, 'result.html', {'prediction': prediction})
        else:
            return JsonResponse({'error': 'Please enter some text'})
    else:
        return JsonResponse({'error': 'Invalid request'})

