def test_home_endpoint(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "API de prédiction attrition OK"}


def test_predict_endpoint(client, valid_payload):
    response = client.post("/predict", json=valid_payload)

    assert response.status_code == 200

    data = response.json()

    assert "prediction" in data
    assert "label" in data
    assert "probability" in data
    assert "input_id" in data
    assert "output_id" in data

    assert data["prediction"] in [0, 1]
    assert data["label"] in ["Quitte", "Reste"]