import pandas as pd
from src.model import Model
from src.preprocess import Preprocessor

def load_data():
    # Dataset fictif pour l'exemple
    data = pd.DataFrame({
        "feature1": [1, 2, 3, 4, 5],
        "feature2": [10, 20, 30, 40, 50],
        "feature3": [100, 200, 300, 400, 500],
        "target":   [0, 0, 1, 1, 1]
    })
    return data

def train_pipeline():
    data = load_data()

    X = data[["feature1", "feature2", "feature3"]]
    y = data["target"]

    preprocessor = Preprocessor()
    X_scaled = preprocessor.fit_transform(X)

    model = Model()
    model.train(X_scaled, y)

    model.save("models/model.joblib")
    print("Modèle entraîné et sauvegardé.")

if __name__ == "__main__":
    train_pipeline()