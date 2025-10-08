import allure


@allure.epic("Курьеры")
@allure.feature("Логин курьера")
class TestLoginCourier:

    @allure.title("Курьер может авторизоваться")
    def test_login_courier_with_valid_credentials_returns_id(self, api, new_courier):
        resp = api.login_courier({
            "login": new_courier["login"],
            "password": new_courier["password"]
        })
        assert resp.status_code == 200
        assert "id" in resp.json()

    @allure.title("Ошибка при авторизации с неверным паролем")
    def test_login_courier_with_wrong_password_returns_404(self, api, new_courier):
        resp = api.login_courier({
            "login": new_courier["login"],
            "password": "wrongpass"
        })
        assert resp.status_code == 404
        assert "message" in resp.json()

    @allure.title("Ошибка при авторизации без логина")
    def test_login_courier_without_login_returns_400(self, api, new_courier):
        resp = api.login_courier({
            "password": new_courier["password"]
        })
        assert resp.status_code == 400
        assert "message" in resp.json()

    @allure.title("Ошибка при авторизации без пароля")
    def test_login_courier_without_password_returns_400(self, api, new_courier):
        resp = api.login_courier({
            "login": new_courier["login"]
        })
        assert resp.status_code == 400
        assert "message" in resp.json()
