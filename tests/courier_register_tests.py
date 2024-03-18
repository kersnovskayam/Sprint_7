from methods.courier_login_methods import CourierLoginMethods
from methods.courier_register_methods import CourierMethods, CourierDeleteMethods
from methods.other_methods import OtherMethods
from utils.allure_decorator import allure_step_decorator
from utils.constants import COURIER_URL, COURIER_LOGIN_URL
from utils.test_data import TestData



class TestRestApiRegisterCourier:

    @allure_step_decorator("Тест создания курьера с обязательными полями")
    def test_create_courier_with_required_fields(self):
        login, password, first_name = OtherMethods.generation_data()
        response = CourierMethods.create_courier(COURIER_URL, login, password, first_name)

        assert response.status_code == 201
        assert response.json() == {'ok': True}

    @allure_step_decorator("Тест создания курьера с повторяющимся логином")
    def test_duplicate_courier_creation(self):
        login = TestData.EXISTING_LOGIN
        _, password, first_name = OtherMethods.generation_data()
        response = CourierMethods.create_courier(COURIER_URL, login, password, first_name)

        assert response.status_code == 409
        assert response.json() == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}

    @allure_step_decorator("Тест создании курьера при передаче не всех обязательных полей")
    def test_required_fields_for_courier_creation(self):
        _, password, first_name = OtherMethods.generation_data()
        response = CourierMethods.create_courier(COURIER_URL, _, password, first_name)

        assert response.status_code == 201
        assert response.json() == {"ok": True}


    @allure_step_decorator("Тест удаления курьера с передачей id")
    def test_delete_courier_by_id(self):
        login, password, first_name = OtherMethods.generation_data()
        CourierMethods.create_courier(COURIER_URL, login, password, first_name)

        response = CourierLoginMethods.login_courier(COURIER_LOGIN_URL, login, password)

        response_data = response.json()
        courier_id = response_data['id']

        delete_response = CourierDeleteMethods.delete_courier(courier_id)

        assert delete_response.status_code == 200
        assert delete_response.json() == {'ok': True}


    @allure_step_decorator("Тест удаления курьера без передачи id")
    def test_delete_courier_without_id(self):
        courier_id = TestData.WRONG_COURIER_ID
        response = CourierDeleteMethods.delete_courier(courier_id)

        assert response.status_code == 404
        assert response.json() == {'code': 404, 'message': 'Not Found.'}

    @allure_step_decorator("Тест удаления курьера с передачей несуществующего id")
    def test_delete_courier_by_wrong_id(self):
        courier_id = TestData.INVALID_COURIER_ID
        response = CourierDeleteMethods.delete_courier(courier_id)

        assert response.status_code == 404
        assert response.json() == {'code': 404, 'message': 'Курьера с таким id нет.'}
        