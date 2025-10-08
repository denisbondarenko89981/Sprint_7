import allure
from helpers import data


@allure.epic("Заказы")
@allure.feature("Получение заказа по номеру")
class TestGetOrderById:

    @allure.title("Можно получить заказ по его номеру")
    def test_get_order_with_valid_track_returns_order(self, api):
        order_resp = api.create_order(data.default_order)
        track = order_resp.json()["track"]

        resp = api.get_order_by_track(track)
        assert resp.status_code == 200
        assert "order" in resp.json()

    @allure.title("Ошибка при запросе заказа без номера")
    def test_get_order_without_track_returns_400(self, api):
        resp = api.get_order_by_track("")
        assert resp.status_code == 400
        assert "message" in resp.json()

    @allure.title("Ошибка при запросе несуществующего заказа")
    def test_get_order_with_invalid_track_returns_404(self, api):
        resp = api.get_order_by_track(9999999)
        assert resp.status_code == 404
        assert "message" in resp.json()
