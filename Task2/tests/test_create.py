import pytest

class TestCreateItemValidData:
    def test_valid_create_old_item(self, client, base_old_advert_payload):
        response = client.create_item(base_old_advert_payload)
        print(f"Response: {response.status_code} - {response.text}")
        assert response.status_code == 200

    def test_valid_create_new_item(self, client, base_new_advert_payload):
        response = client.create_item(base_new_advert_payload)
        print(f"Response: {response.status_code} - {response.text}")
        assert response.status_code == 200

class TestCreateItemInvalidData:
    def test_negative_values(self, client, negative_values_payload):
        response = client.create_item(negative_values_payload)
        print(f"Response: {response.status_code} - {response.text}")
        assert response.status_code == 400


    def test_too_big_values(self, client, too_big_values_payload):
        response = client.create_item(too_big_values_payload)
        print(f"Response: {response.status_code} - {response.text}")
        assert response.status_code == 400


    def test_invalid_types(self, client, invalid_types_payload):
        response = client.create_item(invalid_types_payload)
        print(f"Response: {response.status_code} - {response.text}")
        assert response.status_code == 400


    def test_zero_values(self, client, zero_values_payload):
        response = client.create_item(zero_values_payload)
        print(f"Response: {response.status_code} - {response.text}")
        assert response.status_code == 400

