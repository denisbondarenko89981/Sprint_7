import allure

@allure.epic("Курьеры")
@allure.feature("Удаление курьера")
class TestDeleteCourier:

    @allure.title("Курьера можно удалить")
    def test_delete_courier_with_valid_id_returns_200(self, api, new_courier):
        login_resp = api.login_courier({
            "login": new_courier["login"],
            "password": new_courier["password"]
        })
        courier_id = login_resp.json()["id"]

        resp = api.delete_courier(courier_id)
        assert resp.status_code == 200
        assert resp.json()["ok"]

    @allure.title("Ошибка при удалении курьера без id")
    def test_delete_courier_without_id_returns_400(self, api):
        resp = api.delete_courier("")
        assert resp.status_code == 400 or resp.status_code == 404

    @allure.title("Ошибка при удалении курьера с несуществующим id")
    def test_delete_courier_with_invalid_id_returns_404(self, api):
        resp = api.delete_courier(999999)
        assert resp.status_code == 404
