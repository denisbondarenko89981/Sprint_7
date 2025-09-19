import requests

BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"


class ScooterApiClient:

    def create_courier(self, payload):
        return requests.post(f"{BASE_URL}/courier", json=payload)

    def login_courier(self, payload):
        return requests.post(f"{BASE_URL}/courier/login", json=payload)

    def delete_courier(self, courier_id):
        return requests.delete(f"{BASE_URL}/courier/{courier_id}")

    def create_order(self, payload):
        return requests.post(f"{BASE_URL}/orders", json=payload)

    def get_orders_list(self):
        return requests.get(f"{BASE_URL}/orders")

    def accept_order(self, courier_id, order_id):
        return requests.put(f"{BASE_URL}/orders/accept/{order_id}", params={"courierId": courier_id})

    def get_order_by_track(self, track):
        return requests.get(f"{BASE_URL}/orders/track", params={"t": track})
