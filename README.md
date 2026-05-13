---
title: Projet ML Deploiement
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: gradio
app_file: app.py
pinned: false
---

# Projet ML Déploiement

Application de machine learning déployée avec Hugging Face Spaces.

## Description 

Ce projet a pour objectif de développer, tester et deployer une solution de Machine Learning qui va nous servir à prédire les départs de salariés dans une entreprise 

Le projet comprend :

- un modèle de Machine Learning entrainé
- une interface API pour exposer le modèle
- une base de données PostgreSQL pour enregistrer les inputs et outputs du modèle
- une interface Gradio pour le déploiement sur Hugging face
- une suite de tests unitaires et fonctionnels avec Pytest
- un rapport de couverture de tests avec Pytest-cov


# Architecture du projet

PROJET_ML_DEPLOIEMENT
|
|---app.py
|
|---README.md
|
|---requirements.txt
|
|---gitignore
|
|---data/
    |---model.pkl
|
|---src/
    |---api/
        |--- __init__.py
        |---main.py
        |---model.py
    |---db/
        |---create_db.py
        |---database.py
        |---models.py
|
|---tests/
    |---conftest.py
    |---test_api.py
    |---test_model.py
    |---test_validation.py