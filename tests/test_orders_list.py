import allure


@allure.epic("Заказы")
@allure.feature("Список заказов")
class TestOrdersList:

    @allure.title("Получение списка заказов")
    def test_get_orders_list_returns_orders_array(self, api):
        resp = api.get_orders_list()
        assert resp.status_code == 200
        assert "orders" in resp.json()
        assert isinstance(resp.json()["orders"], list)
