# Architecture

## Flux utilisateur
Utilisateur
→ API FastAPI ou Gradio
→ Validation Pydantic
→ Modèle ML
→ Prédiction
→ Sauvegarde PostgreSQL
→ Logs API

## Choix techniques

| Outil      | Rôle                  |
|-----------|----------------------|
| FastAPI   | API REST              |
| Gradio    | Interface utilisateur |
| PostgreSQL| Stockage              |
| SQLAlchemy| ORM                   |
| Pytest    | Tests                 |
| Pytest-cov| Couverture            |
| MkDocs    | Documentation         |
