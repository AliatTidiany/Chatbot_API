# Chatbot_API
Création d'un chatbot en utilisant une  méthode de classification (API)

# Projet Chatbot avec FastAPI

Ce projet consiste à créer un chatbot en utilisant FastAPI pour fournir une interface API.

## Contenu du Projet

- **api.py**: Fichier contenant le code source de l'API FastAPI.
- **Chatbot_Exam.ipynb**: Notebook Jupyter contenant des exemples d'utilisation du chatbot.
- **chatbot_exam.py**: Script principal du chatbot.
- **docker-compose.yml**: Fichier de configuration pour Docker Compose.
- **Dockerfile**: Fichier Docker pour la construction de l'image Docker du projet.
- **index.html**: Page HTML pour une interface utilisateur de base.
- **intents.json**: Fichier contenant les intentions et les réponses du chatbot.
- **interact_fastapi.py**: Script pour interagir avec le chatbot via FastAPI.
- **interact.py**: Script pour interagir avec le chatbot localement.
- **model_pipeline.joblib**: Fichier contenant le pipeline de modèle pour le chatbot.
- **reponses.joblib**: Fichier contenant les réponses pré-enregistrées du chatbot.
- **requirements.txt**: Fichier contenant les dépendances Python du projet.
- **source_dir/**: Répertoire contenant les fichiers sources supplémentaires du projet.

## Configuration et Exécution

1. Cloner ce dépôt.
2. Installer les dépendances en exécutant `pip install -r requirements.txt`.
3. Lancer l'API FastAPI en exécutant `uvicorn api:app --reload`.
4. Accéder à l'interface utilisateur de l'API à `http://localhost:8000`.
5. Vous pouvez également interagir avec le chatbot en exécutant `python interact.py`.

## Auteur

Alioune MBODJI

