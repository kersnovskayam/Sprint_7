import pytest

from methods.courier_login_methods import CourierLoginMethods
from methods.courier_register_methods import CourierMethods
from methods.other_methods import OtherMethods
from utils.allure_decorator import allure_step_decorator
from utils.constants import COURIER_URL, COURIER_LOGIN_URL
from utils.test_data import TestData

@pytest.fixture(scope="class")
def setup_courier():
    login, password, first_name = OtherMethods.generation_data()
    response = CourierMethods.create_courier(COURIER_URL, login, password, first_name)
    assert response.status_code == 201
    assert response.json() == {'ok': True}

    yield login, password

class TestRestApiLoginCourier:

    @allure_step_decorator("Тест успешной авторизации курьера с корректными данными")
    def test_login_courier_with_valid_credentials(self):
        login, password, first_name = OtherMethods.generation_data()
        response = CourierMethods.create_courier(COURIER_URL, login, password, first_name)
        assert response.status_code == 201
        assert response.json() == {'ok': True}

        response = CourierLoginMethods.login_courier(COURIER_LOGIN_URL, login, password)
        assert response.status_code == 200
        assert "id" in response.json()

    @allure_step_decorator("Тест неуспешной авторизации курьера с некорректными данными")
    def test_login_courier_with_invalid_credentials(self):
        login, password = TestData.EMPTY_LOGIN, TestData.EMPTY_PASSWORD
        response = CourierLoginMethods.login_courier(COURIER_LOGIN_URL, login, password)

        assert response.status_code == 404
        assert response.json() == {"code": 404, "message": "Учетная запись не найдена"}

    @allure_step_decorator("Тест неуспешной авторизации курьера без обязательных параметров")
    def test_login_courier_without_required_fields(self):
        _, _, _ = OtherMethods.generation_data()
        response = CourierLoginMethods.login_courier(COURIER_LOGIN_URL, _, _)

        assert response.status_code == 404
        assert response.json() == {"code": 404, "message": "Учетная запись не найдена"}

    @allure_step_decorator("Тест неуспешной авторизации курьера под несуществующими данными")
    def test_login_courier_with_nonexistent_user(self):
        login, password = TestData.WRONG_LOGIN, TestData.WRONG_PASSWORD
        response = CourierLoginMethods.login_courier(COURIER_LOGIN_URL, login, password)

        assert response.status_code == 400
        assert response.json() == {"code": 400, "message": "Недостаточно данных для входа"}
