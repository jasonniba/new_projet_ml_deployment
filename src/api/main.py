from fastapi import FastAPI, Depends
from enum import Enum
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
import psycopg2

from .model import predict_model
from src.db.database import Base, engine, SessionLocal
from src.db.models import ModelInput, ModelOutput

app = FastAPI(
    title="ML Prediction API",
    description="API de prédiction pour exposer un modèle de machine learning",
    version="1.0.0",
)

DB_USER = "postgres"
DB_PASSWORD = "TON_MOT_DE_PASSE"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "ml_project_db"


class GenreEnum(str, Enum):
    F = "F"
    M = "M"


class StatutMaritalEnum(str, Enum):
    celibataire = "Célibataire"
    marie = "Marié(e)"
    divorce = "Divorcé(e)"


class DepartementEnum(str, Enum):
    commercial = "Commercial"
    consulting = "Consulting"
    rh = "Ressources Humaines"


class PosteEnum(str, Enum):
    assistant_direction = "Assistant de Direction"
    cadre_commercial = "Cadre Commercial"
    consultant = "Consultant"
    directeur_technique = "Directeur Technique"
    manager = "Manager"
    representant_commercial = "Représentant Commercial"
    ressources_humaines = "Ressources Humaines"
    senior_manager = "Senior Manager"
    tech_lead = "Tech Lead"


class DomaineEtudeEnum(str, Enum):
    autre = "Autre"
    entrepreneuriat = "Entrepreunariat"
    infra_cloud = "Infra & Cloud"
    marketing = "Marketing"
    ressources_humaines = "Ressources Humaines"
    transformation_digitale = "Transformation Digitale"


class FrequenceDeplacementEnum(str, Enum):
    aucun = "Aucun"
    frequent = "Frequent"
    occasionnel = "Occasionnel"


class HeureSupplementairesEnum(str, Enum):
    oui = "Oui"
    non = "Non"


class OuiNonEnum(int, Enum):
    non = 0
    oui = 1


class InputData(BaseModel):
    id_employee: int = Field(default=1, description="Identifiant employé")
    age: int = Field(..., description="Âge")
    genre: GenreEnum = Field(..., description="Genre")
    revenu_mensuel: int = Field(..., description="Revenu mensuel")
    statut_marital: StatutMaritalEnum = Field(..., description="Statut marital")
    departement: DepartementEnum = Field(..., description="Département")
    poste: PosteEnum = Field(..., description="Poste")
    domaine_etude: DomaineEtudeEnum = Field(..., description="Domaine d'étude")
    frequence_deplacement: FrequenceDeplacementEnum = Field(..., description="Fréquence de déplacement")
    heure_supplementaires: HeureSupplementairesEnum = Field(..., description="Heures supplémentaires")

    nombre_experiences_precedentes: int
    nombre_heures_travailless: int
    annee_experience_totale: int
    annees_dans_l_entreprise: int
    annees_dans_le_poste_actuel: int
    satisfaction_employee_environnement: int
    note_evaluation_precedente: int
    niveau_hierarchique_poste: int
    satisfaction_employee_nature_travail: int
    satisfaction_employee_equipe: int
    satisfaction_employee_equilibre_pro_perso: int
    note_evaluation_actuelle: int
    augementation_salaire_precedente: float
    nombre_participation_pee: int
    nb_formations_suivies: int
    nombre_employee_sous_responsabilite: int
    distance_domicile_travail: int
    niveau_education: int
    ayant_enfants: OuiNonEnum = Field(..., description="0 = Non, 1 = Oui")
    annees_depuis_la_derniere_promotion: int
    annes_sous_responsable_actuel: int
    salary_increase_rate: float
    relative_tenure: float
    satisfaction_workload_ratio: float

    model_config = {
        "json_schema_extra": {
            "example": {
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
                "satisfaction_workload_ratio": 0.10
            }
        }
    }


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "API de prédiction attrition OK"}


@app.post("/create-db")
def create_database():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT,
        )
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (DB_NAME,))
        exists = cur.fetchone()

        if not exists:
            cur.execute(f'CREATE DATABASE "{DB_NAME}"')
            message = f"Base '{DB_NAME}' créée avec succès."
        else:
            message = f"Base '{DB_NAME}' existe déjà."

        cur.close()
        conn.close()

        return {"message": message}

    except Exception as e:
        return {"error": str(e)}


@app.post("/create-tables")
def create_tables():
    Base.metadata.create_all(bind=engine)
    return {"message": "Tables créées avec succès."}


@app.post("/predict")
def predict_attrition(data: InputData, db: Session = Depends(get_db)):
    db_input = ModelInput(
        id_employee=data.id_employee,
        age=data.age,
        genre=data.genre.value,
        revenu_mensuel=data.revenu_mensuel,
        statut_marital=data.statut_marital.value,
        departement=data.departement.value,
        poste=data.poste.value,
        domaine_etude=data.domaine_etude.value,
        frequence_deplacement=data.frequence_deplacement.value,
        heure_supplementaires=data.heure_supplementaires.value,
        nombre_experiences_precedentes=data.nombre_experiences_precedentes,
        nombre_heures_travailless=data.nombre_heures_travailless,
        annee_experience_totale=data.annee_experience_totale,
        annees_dans_l_entreprise=data.annees_dans_l_entreprise,
        annees_dans_le_poste_actuel=data.annees_dans_le_poste_actuel,
        satisfaction_employee_environnement=data.satisfaction_employee_environnement,
        note_evaluation_precedente=data.note_evaluation_precedente,
        niveau_hierarchique_poste=data.niveau_hierarchique_poste,
        satisfaction_employee_nature_travail=data.satisfaction_employee_nature_travail,
        satisfaction_employee_equipe=data.satisfaction_employee_equipe,
        satisfaction_employee_equilibre_pro_perso=data.satisfaction_employee_equilibre_pro_perso,
        note_evaluation_actuelle=data.note_evaluation_actuelle,
        augementation_salaire_precedente=data.augementation_salaire_precedente,
        nombre_participation_pee=data.nombre_participation_pee,
        nb_formations_suivies=data.nb_formations_suivies,
        nombre_employee_sous_responsabilite=data.nombre_employee_sous_responsabilite,
        distance_domicile_travail=data.distance_domicile_travail,
        niveau_education=data.niveau_education,
        ayant_enfants=int(data.ayant_enfants),
        annees_depuis_la_derniere_promotion=data.annees_depuis_la_derniere_promotion,
        annes_sous_responsable_actuel=data.annes_sous_responsable_actuel,
        salary_increase_rate=data.salary_increase_rate,
        relative_tenure=data.relative_tenure,
        satisfaction_workload_ratio=data.satisfaction_workload_ratio,
    )

    db.add(db_input)
    db.commit()
    db.refresh(db_input)

    # 👉 récupération prediction + proba
    prediction, probability = predict_model(data)

    label = "Quitte" if int(prediction) == 1 else "Reste"

    probability_percent = (
        round(float(probability) * 100, 2) if probability is not None else None
    )

    db_output = ModelOutput(
        input_id=db_input.id,
        prediction=int(prediction),
        label=label,
    )

    db.add(db_output)
    db.commit()
    db.refresh(db_output)

    return {
        "prediction": int(prediction),
        "label": label,
        "probability": f"{probability_percent}%" if probability_percent else None,
        "input_id": db_input.id,
        "output_id": db_output.id,
    }