import requests
import allure
from helpers.urls import BASE_URL


class ScooterApiClient:

    def create_courier(self, payload):
        with allure.step("Создание курьера"):
            return requests.post(f"{BASE_URL}/courier", json=payload)

    def login_courier(self, payload):
        with allure.step("Логин курьера"):
            return requests.post(f"{BASE_URL}/courier/login", json=payload)

    def delete_courier(self, courier_id):
        with allure.step(f"Удаление курьера {courier_id}"):
            return requests.delete(f"{BASE_URL}/courier/{courier_id}")

    def create_order(self, payload):
        with allure.step("Создание заказа"):
            return requests.post(f"{BASE_URL}/orders", json=payload)

    def get_orders_list(self):
        with allure.step("Получение списка заказов"):
            return requests.get(f"{BASE_URL}/orders")

    def accept_order(self, courier_id, order_id):
        with allure.step(f"Принятие заказа {order_id} курьером {courier_id}"):
            return requests.put(f"{BASE_URL}/orders/accept/{order_id}", params={"courierId": courier_id})

    def get_order_by_track(self, track):
        with allure.step(f"Получение заказа по треку {track}"):
            return requests.get(f"{BASE_URL}/orders/track", params={"t": track})
