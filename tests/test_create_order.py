import pytest
import allure

@allure.epic("Заказы")
@allure.feature("Создание заказа")
class TestCreateOrder:

    @pytest.mark.parametrize("color", [
        ["BLACK"], ["GREY"], ["BLACK", "GREY"], []
    ])
    @allure.title("Создание заказа с разными вариантами цвета")
    def test_create_order_with_different_colors_returns_track(self, api, color):
        payload = {
            "firstName": "Иван",
            "lastName": "Иванов",
            "address": "Москва",
            "metroStation": 4,
            "phone": "+79990000000",
            "rentTime": 5,
            "deliveryDate": "2025-09-16",
            "comment": "test",
            "color": color
        }
        resp = api.create_order(payload)
        assert resp.status_code == 201
        assert "track" in resp.json()
