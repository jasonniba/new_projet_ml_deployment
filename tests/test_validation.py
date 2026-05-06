def test_missing_required_field(client, valid_payload):
    del valid_payload["age"]

    response = client.post("/predict", json=valid_payload)

    assert response.status_code == 422


def test_invalid_genre(client, valid_payload):
    valid_payload["genre"] = "X"

    response = client.post("/predict", json=valid_payload)

    assert response.status_code == 422


def test_invalid_statut_marital(client, valid_payload):
    valid_payload["statut_marital"] = "Inconnu"

    response = client.post("/predict", json=valid_payload)

    assert response.status_code == 422


def test_invalid_ayant_enfants(client, valid_payload):
    valid_payload["ayant_enfants"] = 5

    response = client.post("/predict", json=valid_payload)

    assert response.status_code == 422