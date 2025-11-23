import pytest

class TestDeleteItems:
    def test_delete_existing_item(self, client, created_item_id):
        response = client.delete_item(created_item_id)
        print(f"Response: {response.status_code} - {response.text}")
        assert response.status_code == 200

    def test_delete_nonexistent_item(self, client):
        response = client.delete_item(999999)
        print(f"Response: {response.status_code} - {response.text}")
        assert response.status_code == 400