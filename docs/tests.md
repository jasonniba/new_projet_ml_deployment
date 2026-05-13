# Tests

## Outils
- Pytest
- Pytest-cov
- FastAPI TestClient
- Pydantic

## Lancer les tests
python -m pytest tests

## Rapport de couverture
python -m pytest tests --cov=src --cov-report=html
Le rapport est dans htmlcov/index.html

## Types de tests
- Unitaires : prédiction valide, probabilité entre 0 et 1, reproductibilité
- Fonctionnels : endpoints `/` et `/predict`
- Validation : champs manquants ou invalides
