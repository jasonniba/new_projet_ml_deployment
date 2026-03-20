import joblib
from sklearn.linear_model import LogisticRegression

class Model:
    def __init__(self):
        self.model = LogisticRegression()

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def save(self, path="models/model.joblib"):
        joblib.dump(self.model, path)

    def load(self, path="models/model.joblib"):
        self.model = joblib.load(path)