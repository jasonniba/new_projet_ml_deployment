import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from fastapi.testclient import TestClient

from src.api.main import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
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
        "frequence_deplacement": "Frequent",
        "heure_supplementaires": "Oui",
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
        "augementation_salaire_precedente": 0.12,
        "nombre_participation_pee": 1,
        "nb_formations_suivies": 2,
        "nombre_employee_sous_responsabilite": 4,
        "distance_domicile_travail": 12,
        "niveau_education": 3,
        "ayant_enfants": 1,
        "annees_depuis_la_derniere_promotion": 1,
        "annes_sous_responsable_actuel": 2,
        "salary_increase_rate": 0.08,
        "relative_tenure": 0.45,
        "satisfaction_workload_ratio": 0.10,
    }