## Importation des paquets
import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from joblib import dump, load
import numpy as np
import random
import os
from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
nltk.download('punkt') 
## Stemming 
# Téléchargement des stopwords pour le français
stop_words = set(stopwords.words('french'))

# Initialisation du stemmer pour le français
stemmer = SnowballStemmer("french")
# Fonction Stemming
def french_stemmer(text):
    # Tokenization et stemming
    
    stemmed_words = [stemmer.stem(word) for word in word_tokenize(text, language='french')]
    
    # Suppression des stopwords
    filtered_words = [word for word in stemmed_words if word.lower() not in stop_words]
    
    return filtered_words
## Fonction pré-traitement
def pre_process_data(data):
    processed_data = []
    for question in data:
        stemmed_question = french_stemmer(question)
        processed_data.append(' '.join(stemmed_question))
    return processed_data
## Chargement du fichier JSON
intents_file = open("intents.json").read()
intents = json.loads(intents_file)
intentions = intents["intentions"]
## Extraction des Tag, Questions et des Réponses au niveau du fichier  
tags = []
questions = []
reponses_dic = {}
for intention in intentions:
    tag = intention["tag"]
    reponses_dic[tag] = intention.get("reponses")
    for question in intention["questions"]:
        questions.append(question)
        tags.append(tag)
## Création du dataframe 
df = pd.DataFrame({
    "label": tags,
    "questions": questions,
    "responses": [random.choice(reponses_dic[tag]) for tag in tags]
})
## Pré-traitement des données
df['processed_questions'] = pre_process_data(df['questions'])
## Vectorization de Questions
tfidf_vect = TfidfVectorizer()
quest_vect = tfidf_vect.fit_transform(df['processed_questions']).toarray()
## Encodage du label
encoder = LabelEncoder()
encoded_label = encoder.fit_transform(df['label'])
## Training et construction du Pipeline
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', MultinomialNB())
])

model.fit(df['questions'], df['label'])
## Enregistrement du model et des possibles réponses
# Save Model
dump(model, "model_pipeline.joblib")
# Save du dictionnaire des réponses
dump(reponses_dic, "reponses.joblib")
## Chatbox fonction
def chat(question):
    # Load du model et des réponses
    loaded_model = load("model_pipeline.joblib")
    loaded_reponses_dic = load("reponses.joblib")
    
    # Prediction
    predicted_tag = loaded_model.predict([question])[0]

    # Retourne la réponse, le score de confidence et le tag associé
    response = random.choice(loaded_reponses_dic[predicted_tag])
    confidence_score = np.max(loaded_model.predict_proba([question]))
    
    return response, confidence_score, predicted_tag
user_input = "Bonjour"
response, confidence_score, predicted_tag = chat(user_input)
print(f"Chatbot Response: {response}")
print(f"Confidence Score: {confidence_score}")
print(f"Predicted Tag: {predicted_tag}")
