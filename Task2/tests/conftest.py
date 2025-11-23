import pytest
import random
import string
from utils.API_client import APIClient


@pytest.fixture
def client():
    return APIClient()

#Положительные варианты значений

#Старое объявление(с просмотрами и тп)
@pytest.fixture()
def base_old_advert_payload():
    return {
        "sellerID": 121211,
        "name": "TestName",
        "price": random.randint(0, 1000),
        "statistics": {
            "likes": random.randint(0, 1000),
            "viewCount": random.randint(0, 1000),
            "contacts": random.randint(0, 1000)
        }
    }

#Новое объявление(без просмотров и тп)
@pytest.fixture()
def base_new_advert_payload():
    return {
        "sellerID": 121211,
        "name": "TestName",
        "price": 5700,
        "statistics": {
            "likes": 0,
            "viewCount": 0,
            "contacts": 0
        }
    }

#Фикстуры для создания тестовых данных(с примером старого объявления)
@pytest.fixture
def created_item_id(client, base_old_advert_payload):
    response = client.create_item(base_old_advert_payload)
    assert response.status_code == 200
    response_data = response.json()

    status_message = response_data.get("status", "")
    item_id = status_message.split(" - ")[-1]

    yield item_id

    if item_id:
        client.delete_item(item_id)


@pytest.fixture
def existing_seller_id(client, base_old_advert_payload):
    response = client.create_item(base_old_advert_payload)
    assert response.status_code == 200
    seller_id = base_old_advert_payload["sellerID"]

    response_data = response.json()
    status_message = response_data.get("status", "")
    item_id = status_message.split(" - ")[-1]

    yield seller_id

    if item_id:
        client.delete_item(item_id)


#Негативные варианты значений

#Отрицательные значения
@pytest.fixture(params=[
    {"sellerID": 121211, "name": "TestName", "price": -1000, "statistics": {"likes": 32, "viewCount": 0, "contacts": 14}},
    {"sellerID": 121211, "name": "TestName", "price": 1000, "statistics": {"likes": 32, "viewCount": -5, "contacts": 14}},
    {"sellerID": 121211, "name": "TestName", "price": 1000, "statistics": {"likes": 32, "viewCount": 0, "contacts": -10}},
    {"sellerID": 121211, "name": "TestName", "price": 1000, "statistics": {"likes": -1, "viewCount": 0, "contacts": 14}},
])
def negative_values_payload(request):
    return request.param

#Большие значения
@pytest.fixture(params=[
    {"sellerID": 121211, "name": "TestName", "price": 10**10, "statistics": {"likes": 32, "viewCount": 0, "contacts": 14}},
    {"sellerID": 121211, "name": "TestName", "price": 1000, "statistics": {"likes": 32, "viewCount": 10**10, "contacts": 14}},
    {"sellerID": 121211, "name": "TestName", "price": 1000, "statistics": {"likes": 32, "viewCount": 0, "contacts": 10**10}},
    {"sellerID": 121211, "name": "TestName", "price": 1000, "statistics": {"likes": 10**10, "viewCount": 0, "contacts": 14}},
])
def too_big_values_payload(request):
    return request.param

#Некорректные типы данных
@pytest.fixture(params=[
    {"sellerID": "", "name": "TestName", "price": 1000, "statistics": {"likes": 32, "viewCount": 12, "contacts": 14}},
    {"sellerID": 121211, "name": "TestName", "price": "", "statistics": {"likes": 32, "viewCount": 12, "contacts": 14}},
    {"sellerID": 121211, "name": 1, "price": 1000, "statistics": {"likes": 32, "viewCount": 12, "contacts": 14}},
])
def invalid_types_payload(request):
    return request.param

#Нулевые значения
@pytest.fixture(params=[
    {"sellerID": 121211, "name": "TestName", "price": 0, "statistics": {"likes": 32, "viewCount": 12, "contacts": 14}},
    {"sellerID": 121211, "name": "TestName", "price": 1000, "statistics": {"likes": 0, "viewCount": 12, "contacts": 14}},
    {"sellerID": 121211, "name": "TestName", "price": 1000, "statistics": {"likes": 32, "viewCount": 12, "contacts": 0}},
    {"sellerID": 121211, "name": "TestName", "price": 1000, "statistics": {"likes": 32, "viewCount": 0, "contacts": 14}},
])
def zero_values_payload(request):
    return request.param
