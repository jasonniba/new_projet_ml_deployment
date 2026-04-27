from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)


def valid_payload():
    return {
        "id_employee": 1001,
        "age": 35,
        "genre": "M",
        "revenu_mensuel": 4500,
        "statut_marital": "Marié(e)",
        "departement": "Consulting",
        "poste": "Consultant",
        "domaine_etude": "Infra & Cloud",
        "nombre_experiences_precedentes": 3,
        "nombre_heures_travailless": 40,
        "annee_experience_totale": 10,
        "annees_dans_l_entreprise": 5,
        "annees_dans_le_poste_actuel": 3,
        "satisfaction_employee_environnement": 4,
        "note_evaluation_precedente": 3,
        "niveau_hierarchique_poste": 2,
        "satisfaction_employee_nature_travail": 4,
        "satisfaction_employee_equipe": 4,
        "satisfaction_employee_equilibre_pro_perso": 3,
        "note_evaluation_actuelle": 4,
        "heure_supplementaires": 1,
        "augementation_salaire_precedente": 0.12,
        "nombre_participation_pee": 1,
        "nb_formations_suivies": 2,
        "nombre_employee_sous_responsabilite": 4,
        "distance_domicile_travail": 12,
        "niveau_education": 3,
        "ayant_enfants": 1,
        "frequence_deplacement": 2,
        "annees_depuis_la_derniere_promotion": 1,
        "annes_sous_responsable_actuel": 2,
        "salary_increase_rate": 0.08,
        "relative_tenure": 0.45,
        "satisfaction_workload_ratio": 0.10
    }


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is running"}


def test_predict_returns_prediction():
    response = client.post("/predict", json=valid_payload())
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert data["prediction"] in [0, 1]


def test_predict_missing_field():
    payload = valid_payload()
    payload.pop("age")
    response = client.post("/predict", json=payload)
    assert response.status_code == 422


def test_predict_invalid_enum():
    payload = valid_payload()
    payload["genre"] = "X"
    response = client.post("/predict", json=payload)
    assert response.status_code == 422