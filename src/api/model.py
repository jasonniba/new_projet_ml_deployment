from pathlib import Path
import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
MODEL_PATH = BASE_DIR / "data" / "model.pkl"

model = joblib.load(MODEL_PATH)

GENRE_MAP = {
    "F": 0,
    "M": 1,
}

STATUT_MARITAL_MAP = {
    "Célibataire": 1,
    "Marié(e)": 2,
    "Divorcé(e)": 3,
}

FREQUENCE_DEPLACEMENT_MAP = {
    "Aucun": 1,
    "Frequent": 2,
    "Occasionnel": 3,
}

HEURE_SUPPLEMENTAIRES_MAP = {
    "Oui": 0,
    "Non": 1,
}

DEPARTEMENT_COLUMNS = {
    "Commercial": "departement_Commercial",
    "Consulting": "departement_Consulting",
    "Ressources Humaines": "departement_Ressources Humaines",
}

POSTE_COLUMNS = {
    "Assistant de Direction": "poste_Assistant de Direction",
    "Cadre Commercial": "poste_Cadre Commercial",
    "Consultant": "poste_Consultant",
    "Directeur Technique": "poste_Directeur Technique",
    "Manager": "poste_Manager",
    "Représentant Commercial": "poste_Représentant Commercial",
    "Ressources Humaines": "poste_Ressources Humaines",
    "Senior Manager": "poste_Senior Manager",
    "Tech Lead": "poste_Tech Lead",
}

DOMAINE_COLUMNS = {
    "Autre": "domaine_etude_Autre",
    "Entrepreunariat": "domaine_etude_Entrepreunariat",
    "Infra & Cloud": "domaine_etude_Infra & Cloud",
    "Marketing": "domaine_etude_Marketing",
    "Ressources Humaines": "domaine_etude_Ressources Humaines",
    "Transformation Digitale": "domaine_etude_Transformation Digitale",
}


def build_one_hot(selected_value: str, mapping: dict) -> dict:
    encoded = {column_name: 0 for column_name in mapping.values()}
    encoded[mapping[selected_value]] = 1
    return encoded


def predict_model(data):
    base_features = {
        "id_employee": data.id_employee,
        "age": data.age,
        "genre": GENRE_MAP[data.genre.value],
        "revenu_mensuel": data.revenu_mensuel,
        "statut_marital": STATUT_MARITAL_MAP[data.statut_marital.value],
        "nombre_experiences_precedentes": data.nombre_experiences_precedentes,
        "nombre_heures_travailless": data.nombre_heures_travailless,
        "annee_experience_totale": data.annee_experience_totale,
        "annees_dans_l_entreprise": data.annees_dans_l_entreprise,
        "annees_dans_le_poste_actuel": data.annees_dans_le_poste_actuel,
        "satisfaction_employee_environnement": data.satisfaction_employee_environnement,
        "note_evaluation_precedente": data.note_evaluation_precedente,
        "niveau_hierarchique_poste": data.niveau_hierarchique_poste,
        "satisfaction_employee_nature_travail": data.satisfaction_employee_nature_travail,
        "satisfaction_employee_equipe": data.satisfaction_employee_equipe,
        "satisfaction_employee_equilibre_pro_perso": data.satisfaction_employee_equilibre_pro_perso,
        "note_evaluation_actuelle": data.note_evaluation_actuelle,
        "heure_supplementaires": HEURE_SUPPLEMENTAIRES_MAP[data.heure_supplementaires.value],
        "augementation_salaire_precedente": data.augementation_salaire_precedente,
        "nombre_participation_pee": data.nombre_participation_pee,
        "nb_formations_suivies": data.nb_formations_suivies,
        "nombre_employee_sous_responsabilite": data.nombre_employee_sous_responsabilite,
        "distance_domicile_travail": data.distance_domicile_travail,
        "niveau_education": data.niveau_education,
        "ayant_enfants": int(data.ayant_enfants),
        "frequence_deplacement": FREQUENCE_DEPLACEMENT_MAP[data.frequence_deplacement.value],
        "annees_depuis_la_derniere_promotion": data.annees_depuis_la_derniere_promotion,
        "annes_sous_responsable_actuel": data.annes_sous_responsable_actuel,
        "Salary_increase_rate": data.salary_increase_rate,
        "relative_tenure": data.relative_tenure,
        "satisfaction_workload_ratio": data.satisfaction_workload_ratio,
    }

    departement_features = build_one_hot(data.departement.value, DEPARTEMENT_COLUMNS)
    poste_features = build_one_hot(data.poste.value, POSTE_COLUMNS)
    domaine_features = build_one_hot(data.domaine_etude.value, DOMAINE_COLUMNS)

    input_dict = {
        **base_features,
        **departement_features,
        **poste_features,
        **domaine_features,
    }

    input_df = pd.DataFrame([input_dict])

    if hasattr(model, "feature_names_in_"):
        input_df = input_df.reindex(columns=model.feature_names_in_)

    prediction = model.predict(input_df)[0]

    # 👉 AJOUT IMPORTANT
    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(input_df)[0][1]
    else:
        probability = None

    return int(prediction), probability