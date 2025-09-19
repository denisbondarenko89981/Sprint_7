import allure

@allure.epic("Курьеры")
@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Курьера можно создать")
    def test_create_courier_with_valid_data_returns_201(self, api):
        payload = {"login": "unique_login123", "password": "pass123", "firstName": "Иван"}
        resp = api.create_courier(payload)
        assert resp.status_code == 201
        assert resp.json()["ok"]

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_courier_with_existing_login_returns_409(self, api, new_courier):
        resp = api.create_courier(new_courier)
        assert resp.status_code == 409

    @allure.title("Ошибка при создании курьера без пароля")
    def test_create_courier_without_password_returns_400(self, api):
        payload = {"login": "login123", "firstName": "Иван"}
        resp = api.create_courier(payload)
        assert resp.status_code == 400
