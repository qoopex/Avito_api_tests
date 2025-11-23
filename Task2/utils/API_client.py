import requests

BASE_URL = 'https://qa-internship.avito.com'

class APIClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = {"Content-Type": "application/json", "Accept": "application/json"}

    #для тест-сьюта 1
    def create_item(self, payload):
        url = f"{self.base_url}/api/1/item"
        return requests.post(url, json=payload, headers=self.headers)

    # для тест-сьюта 2
    def get_item(self, item_id):
        url = f"{self.base_url}/api/1/item/{item_id}"
        return requests.get(url, headers={"Accept": "application/json"})

    def get_user_items(self, seller_id):
        url = f"{self.base_url}/api/1/{seller_id}/item"
        return requests.get(url, headers={"Accept": "application/json"})

    #для тест-сьюта 3
    def get_statistics(self, item_id):
        url = f"{self.base_url}/api/2/statistic/{item_id}"
        return requests.get(url, headers={"Accept": "application/json"})

    # для тест-сьюта 4
    def delete_item(self, item_id):
        url = f"{self.base_url}/api/2/item/{item_id}"
        return requests.delete(url, headers={"Accept": "application/json"})