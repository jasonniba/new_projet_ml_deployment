# Modèle ML

## Objectif
Prédire si un employé risque de quitter l'entreprise.

| Valeur | Label |
|-------|-------|
| 0     | Reste |
| 1     | Quitte |

## Fichier modèle
data/model.pkl chargé avec joblib

## Fonction principale
predict_model(data) dans src/api/model.py

## Étapes
1. Validation Pydantic
2. Encodage variables catégorielles
3. DataFrame Pandas
4. Alignement colonnes
5. Prédiction
6. Probabilité si disponible
