import allure
from helpers import data


@allure.epic("Заказы")
@allure.feature("Принятие заказа")
class TestAcceptOrder:

    @allure.title("Курьер может принять заказ")
    def test_accept_order_with_valid_data_returns_ok(self, api, new_courier):
        order_resp = api.create_order(data.default_order)
        order_id = order_resp.json()["track"]

        login_resp = api.login_courier({
            "login": new_courier["login"],
            "password": new_courier["password"]
        })
        courier_id = login_resp.json()["id"]

        resp = api.accept_order(courier_id, order_id)
        assert resp.status_code == 200
        assert resp.json()["ok"] is True

    @allure.title("Ошибка при принятии заказа без id курьера")
    def test_accept_order_without_courier_id_returns_400(self, api):
        resp = api.accept_order("", 1)
        assert resp.status_code == 400
        assert "message" in resp.json()

    @allure.title("Ошибка при принятии заказа без id заказа")
    def test_accept_order_without_order_id_returns_400(self, api, new_courier):
        login_resp = api.login_courier({
            "login": new_courier["login"],
            "password": new_courier["password"]
        })
        courier_id = login_resp.json()["id"]
        resp = api.accept_order(courier_id, "")
        assert resp.status_code == 400
        assert "message" in resp.json()
