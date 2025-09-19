import pytest
from helpers.api_client import ScooterApiClient
from helpers.data_generator import generate_courier


@pytest.fixture(scope="session")
def api():
    return ScooterApiClient()


@pytest.fixture
def new_courier(api):
    courier_data = generate_courier()
    response = api.create_courier(courier_data)
    assert response.status_code in [201, 409]
    yield courier_data
    login_resp = api.login_courier({
        "login": courier_data["login"],
        "password": courier_data["password"]
    })
    if login_resp.status_code == 200:
        courier_id = login_resp.json()["id"]
        api.delete_courier(courier_id)
