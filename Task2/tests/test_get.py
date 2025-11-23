import pytest

class TestGetItems:
    def test_get_existing_item(self, client, created_item_id):
        response = client.get_item(created_item_id)
        print(f"Response: {response.status_code} - {response.text}")
        assert response.status_code == 200

    def test_get_nonexistent_item(self, client):
        response = client.get_item(999999)
        print(f"Response: {response.status_code} - {response.text}")
        assert response.status_code == 400

    def test_get_user_items(self, client, existing_seller_id):
        response = client.get_user_items(existing_seller_id)
        print(f"Response: {response.status_code} - {response.text}")
        assert response.status_code == 200