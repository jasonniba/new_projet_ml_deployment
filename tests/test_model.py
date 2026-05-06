from src.api.main import InputData
from src.api.model import predict_model


def test_predict_model_returns_valid_result(valid_payload):
    data = InputData(**valid_payload)

    prediction, probability = predict_model(data)

    assert prediction in [0, 1]

    if probability is not None:
        assert 0 <= probability <= 1


def test_predict_model_is_reproducible(valid_payload):
    data = InputData(**valid_payload)

    prediction_1, probability_1 = predict_model(data)
    prediction_2, probability_2 = predict_model(data)

    assert prediction_1 == prediction_2
    assert probability_1 == probability_2