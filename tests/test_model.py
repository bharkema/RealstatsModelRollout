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

def test_Custom_request_unknown_request():
    model = Model()

    with pytest.raises(Exception) as exc:
        model.Custom_request(request_type="Faulty", pathing="path")
        assert "Request type not found please the following: get, put, post" in str(exc.value)

def test_Custom_request_get_request():
    model = Model()

    model.Model_URL = "https://google.com/"
    model.Model_port = ""

    response = model.Custom_request(request_type="get", pathing="info")
    assert response.status_code == 404

