import pytest
import allure
from helpers import data


@allure.epic("Заказы")
@allure.feature("Создание заказа")
class TestCreateOrder:

    @pytest.mark.parametrize("color", [
        ["BLACK"], ["GREY"], ["BLACK", "GREY"], []
    ])
    @allure.title("Создание заказа с разными вариантами цвета")
    def test_create_order_with_different_colors_returns_track(self, api, color):
        payload = data.default_order.copy()
        payload["color"] = color

        resp = api.create_order(payload)
        assert resp.status_code == 201
        assert "track" in resp.json()
        assert isinstance(resp.json()["track"], int)
