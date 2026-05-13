# API FastAPI

## Lancer l'API
uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8080

## Documentation Swagger
http://127.0.0.1:8080/docs

## Endpoints

### GET `/`
Vérifie que l'API fonctionne.
Exemple de réponse :
{
  "message": "API de prédiction attrition OK"
}

### POST `/predict`
Retourne la prédiction du modèle.
Exemple de réponse :
{
  "prediction": 0,
  "label": "Reste",
  "probability": "72.5%",
  "input_id": 1,
  "output_id": 1
}
