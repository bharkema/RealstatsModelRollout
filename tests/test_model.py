import pytest
from RealstatsModelRollout import Model


def test_Info_request_inactive():
    model = Model()

    with pytest.raises(Exception) as exc:
        model.Info_request()
        assert "Not able to get data from URL please check if model is running or online" in str(exc.value)


def test_Predict_request_inactive():
    model = Model()

    with pytest.raises(Exception) as exc:
        model.Predict_request(json_data={})
        assert "Not able to get data from URL please check if model is running or online" in str(exc.value)


def test_validate_request_inactive():
    model = Model()

    features = [
        'leefbaarheid_score',
        'score_wonen',
        'score_veiligheid',
        'score_voorzieningen',
        'leeftijdscategorie_0_15',
        'leeftijdscategorie_15_25',
        'leeftijdscategorie_25_45'
    ]

    best_param_values = {
        'boosting_type': 0,
        'colsample_by_tree': 0.42578475315406
    }

    payload = {
        "feature_array": features,
        "param_values": best_param_values,
        "target": "testing_price"
    }

    with pytest.raises(Exception) as exc:
        model.Validate_request(payload=payload)
        assert "Not able to get data from URL please check if model is running or online" in str(exc.value)


def test_load_request_inactive():
    model = Model()

    with pytest.raises(Exception) as exc:
        model.Load_model()
        assert "Not able to get data from URL please check if model is running or online" in str(exc.value)


def test_Custom_request_unknown_request():
    model = Model()

    with pytest.raises(Exception) as exc:
        model.Custom_request(request_type="Faulty", pathing="path")
        assert "Request type not found please the following: get, put, post" in str(exc.value)


def test_Custom_request_get_request():
    model = Model()

    model.Model_URL = "https://httpbin.org/"
    model.Model_port = ""

    response = model.Custom_request(request_type="get", pathing="get")
    assert response.status_code == 200
