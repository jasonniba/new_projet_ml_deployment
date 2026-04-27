from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base


class EmployeeDataset(Base):
    __tablename__ = "employees_dataset"

    id = Column(Integer, primary_key=True, index=True)
    id_employee = Column(Integer, nullable=False, index=True)

    age = Column(Integer, nullable=False)
    genre = Column(String, nullable=False)
    revenu_mensuel = Column(Integer, nullable=False)
    statut_marital = Column(String, nullable=False)
    departement = Column(String, nullable=False)
    poste = Column(String, nullable=False)
    domaine_etude = Column(String, nullable=False)
    frequence_deplacement = Column(String, nullable=True)
    heure_supplementaires = Column(String, nullable=True)

    nombre_experiences_precedentes = Column(Integer, nullable=False)
    nombre_heures_travailless = Column(Integer, nullable=False)
    annee_experience_totale = Column(Integer, nullable=False)
    annees_dans_l_entreprise = Column(Integer, nullable=False)
    annees_dans_le_poste_actuel = Column(Integer, nullable=False)
    satisfaction_employee_environnement = Column(Integer, nullable=False)
    note_evaluation_precedente = Column(Integer, nullable=False)
    niveau_hierarchique_poste = Column(Integer, nullable=False)
    satisfaction_employee_nature_travail = Column(Integer, nullable=False)
    satisfaction_employee_equipe = Column(Integer, nullable=False)
    satisfaction_employee_equilibre_pro_perso = Column(Integer, nullable=False)
    note_evaluation_actuelle = Column(Integer, nullable=False)
    augementation_salaire_precedente = Column(Float, nullable=False)
    nombre_participation_pee = Column(Integer, nullable=False)
    nb_formations_suivies = Column(Integer, nullable=False)
    nombre_employee_sous_responsabilite = Column(Integer, nullable=False)
    distance_domicile_travail = Column(Integer, nullable=False)
    niveau_education = Column(Integer, nullable=False)
    ayant_enfants = Column(Integer, nullable=False)
    annees_depuis_la_derniere_promotion = Column(Integer, nullable=False)
    annes_sous_responsable_actuel = Column(Integer, nullable=False)
    salary_increase_rate = Column(Float, nullable=False)
    relative_tenure = Column(Float, nullable=False)
    satisfaction_workload_ratio = Column(Float, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())


class ModelInput(Base):
    __tablename__ = "model_inputs"

    id = Column(Integer, primary_key=True, index=True)
    id_employee = Column(Integer, nullable=False, index=True)

    age = Column(Integer, nullable=False)
    genre = Column(String, nullable=False)
    revenu_mensuel = Column(Integer, nullable=False)
    statut_marital = Column(String, nullable=False)
    departement = Column(String, nullable=False)
    poste = Column(String, nullable=False)
    domaine_etude = Column(String, nullable=False)
    frequence_deplacement = Column(String, nullable=False)
    heure_supplementaires = Column(String, nullable=False)

    nombre_experiences_precedentes = Column(Integer, nullable=False)
    nombre_heures_travailless = Column(Integer, nullable=False)
    annee_experience_totale = Column(Integer, nullable=False)
    annees_dans_l_entreprise = Column(Integer, nullable=False)
    annees_dans_le_poste_actuel = Column(Integer, nullable=False)
    satisfaction_employee_environnement = Column(Integer, nullable=False)
    note_evaluation_precedente = Column(Integer, nullable=False)
    niveau_hierarchique_poste = Column(Integer, nullable=False)
    satisfaction_employee_nature_travail = Column(Integer, nullable=False)
    satisfaction_employee_equipe = Column(Integer, nullable=False)
    satisfaction_employee_equilibre_pro_perso = Column(Integer, nullable=False)
    note_evaluation_actuelle = Column(Integer, nullable=False)
    heure_supplementaires = Column(String, nullable=False)
    augementation_salaire_precedente = Column(Float, nullable=False)
    nombre_participation_pee = Column(Integer, nullable=False)
    nb_formations_suivies = Column(Integer, nullable=False)
    nombre_employee_sous_responsabilite = Column(Integer, nullable=False)
    distance_domicile_travail = Column(Integer, nullable=False)
    niveau_education = Column(Integer, nullable=False)
    ayant_enfants = Column(Integer, nullable=False)
    frequence_deplacement = Column(String, nullable=False)
    annees_depuis_la_derniere_promotion = Column(Integer, nullable=False)
    annes_sous_responsable_actuel = Column(Integer, nullable=False)
    salary_increase_rate = Column(Float, nullable=False)
    relative_tenure = Column(Float, nullable=False)
    satisfaction_workload_ratio = Column(Float, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    output = relationship("ModelOutput", back_populates="model_input", uselist=False)


class ModelOutput(Base):
    __tablename__ = "model_outputs"

    id = Column(Integer, primary_key=True, index=True)
    input_id = Column(Integer, ForeignKey("model_inputs.id"), nullable=False)

    prediction = Column(Integer, nullable=False)
    label = Column(String, nullable=False)
    probability = Column(Float, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    model_input = relationship("ModelInput", back_populates="output")


class ApiLog(Base):
    __tablename__ = "api_logs"

    id = Column(Integer, primary_key=True, index=True)

    endpoint = Column(String, nullable=False)
    method = Column(String, nullable=False)

    input_id = Column(Integer, nullable=True)
    output_id = Column(Integer, nullable=True)

    request_payload = Column(Text, nullable=True)
    response_payload = Column(Text, nullable=True)

    status = Column(String, nullable=False)
    error_message = Column(Text, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())