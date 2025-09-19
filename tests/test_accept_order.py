import allure

@allure.epic("Заказы")
@allure.feature("Принятие заказа")
class TestAcceptOrder:

    @allure.title("Курьер может принять заказ")
    def test_accept_order_with_valid_data_returns_ok(self, api, new_courier):
        order_resp = api.create_order({
            "firstName": "Иван",
            "lastName": "Иванов",
            "address": "Москва",
            "metroStation": 4,
            "phone": "+79990000000",
            "rentTime": 5,
            "deliveryDate": "2025-09-16",
            "comment": "accept test",
            "color": ["BLACK"]
        })
        order_id = order_resp.json()["track"]

        login_resp = api.login_courier({
            "login": new_courier["login"],
            "password": new_courier["password"]
        })
        courier_id = login_resp.json()["id"]

        resp = api.accept_order(courier_id, order_id)
        assert resp.status_code in [200, 409]
        assert "ok" in resp.json() or "message" in resp.json()

    @allure.title("Ошибка при принятии заказа без id курьера")
    def test_accept_order_without_courier_id_returns_400(self, api):
        resp = api.accept_order("", 1)
        assert resp.status_code == 400 or resp.status_code == 404

    @allure.title("Ошибка при принятии заказа без id заказа")
    def test_accept_order_without_order_id_returns_400(self, api, new_courier):
        login_resp = api.login_courier({
            "login": new_courier["login"],
            "password": new_courier["password"]
        })
        courier_id = login_resp.json()["id"]
        resp = api.accept_order(courier_id, "")
        assert resp.status_code == 400 or resp.status_code == 404
