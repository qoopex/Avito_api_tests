import pytest

class TestStatistics:
    def test_get_existing_statistics(self, client, created_item_id):
        response = client.get_statistics(created_item_id)
        print(f"Response: {response.status_code} - {response.text}")
        assert response.status_code == 200

    def test_get_nonexistent_statistics(self, client):
        response = client.get_statistics(999999)
        print(f"Response: {response.status_code} - {response.text}")
        assert response.status_code == 404