# Base de données PostgreSQL

## Objectif
Sauvegarder inputs, outputs et logs.

## Création
python -m src.db.create_db

## Tables principales
- model_inputs : données envoyées
- model_outputs : prediction, label, probability, input_id
- api_logs : endpoint, méthode, payload, réponse, erreur éventuelle
- employees_dataset : dataset initial

## Vérification
SELECT * FROM model_inputs;
SELECT * FROM model_outputs;
SELECT * FROM api_logs;

## Sécurité
Utiliser .env pour les identifiants PostgreSQL en production.
