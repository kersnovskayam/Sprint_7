from methods.courier_login_methods import CourierLoginMethods
from methods.courier_register_methods import CourierMethods
from methods.order_methods import OrderMethods
from methods.other_methods import OtherMethods
from utils.allure_decorator import allure_step_decorator
from utils.constants import ORDER_URL, COURIER_LOGIN_URL, COURIER_URL, ORDER_ACCEPT
from utils.test_data import TestData


class TestRestApiOrderCreate:

    @allure_step_decorator("Тест успешного создания заказа с двумя цветами")
    def test_create_order_with_two_colors(self):
        data = TestData.ORDER_DATA_TWO
        response = OrderMethods.create_order(ORDER_URL, data)

        assert response.status_code == 201
        assert "track" in response.json()

    @allure_step_decorator("Тест успешного создания заказа без передачи цвета")
    def test_create_order_without_colors(self):
        data = TestData.ORDER_DATA_THREE
        response = OrderMethods.create_order(ORDER_URL, data)

        assert response.status_code == 201
        assert "track" in response.json()

    @allure_step_decorator("Тест успешного принятия заказа")
    def test_list_apply(self):
        login, password, first_name = OtherMethods.generation_data()
        CourierMethods.create_courier(COURIER_URL, login, password, first_name)

        # авторизация курьера и получение его id
        response = CourierLoginMethods.login_courier(COURIER_LOGIN_URL, login, password)
        response_data = response.json()
        courier_id = response_data['id']

        # создание заказа
        data = TestData.ORDER_DATA_ONE
        response = OrderMethods.create_order(ORDER_URL, data)

        response_data = response.json()
        order_track = response_data['track']

        response = OrderMethods.get_order_id_by_track(order_track)
        response_data = response.json()
        order_id = response_data['order']['id']

        response = OrderMethods.apply_order(ORDER_ACCEPT, order_id, courier_id)

        assert response.status_code == 200
        assert response.json() == {'ok': True}

    @allure_step_decorator("Тест принятия заказа без передачи id курьера")
    def test_list_apply_wrong_courier_id(self):
        courier_id = TestData.WRONG_COURIER_ID

        data = TestData.ORDER_DATA_ONE
        response = OrderMethods.create_order(ORDER_URL, data)

        response_data = response.json()
        order_track = response_data['track']

        response = OrderMethods.get_order_id_by_track(order_track)
        response_data = response.json()
        order_id = response_data['order']['id']

        response = OrderMethods.apply_order(ORDER_ACCEPT, order_id, courier_id)

        assert response.status_code == 400
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для поиска'}

    @allure_step_decorator("Тест принятия заказа с передачей некорректного id курьера")
    def test_list_apply_invalid_courier_id(self):
        courier_id = TestData.INVALID_COURIER_ID

        data = TestData.ORDER_DATA_ONE
        response = OrderMethods.create_order(ORDER_URL, data)

        response_data = response.json()
        order_track = response_data['track']

        response = OrderMethods.get_order_id_by_track(order_track)
        response_data = response.json()
        order_id = response_data['order']['id']

        response = OrderMethods.apply_order(ORDER_ACCEPT, order_id, courier_id)

        assert response.status_code == 404
        assert response.json() == {'code': 404, 'message': 'Курьера с таким id не существует'}

    @allure_step_decorator("Тест принятия заказа без передачи id заказа")
    def test_list_apply_wrong_order_id(self):
        order_id = TestData.WRONG_ORDER_ID

        login, password, first_name = OtherMethods.generation_data()
        CourierMethods.create_courier(COURIER_URL, login, password, first_name)

        response = CourierLoginMethods.login_courier(COURIER_LOGIN_URL, login, password)
        response_data = response.json()
        courier_id = response_data['id']

        response = OrderMethods.apply_order(ORDER_ACCEPT, order_id, courier_id)

        assert response.status_code == 404
        assert response.json() == {'code': 404, 'message': 'Not Found.'}

    @allure_step_decorator("Тест принятия заказа с передачей некорректного id заказа")
    def test_list_apply_invalid_order_id(self):
        order_id = TestData.INVALID_ORDER_ID

        login, password, first_name = OtherMethods.generation_data()
        CourierMethods.create_courier(COURIER_URL, login, password, first_name)

        response = CourierLoginMethods.login_courier(COURIER_LOGIN_URL, login, password)
        response_data = response.json()
        courier_id = response_data['id']

        response = OrderMethods.apply_order(ORDER_ACCEPT, order_id, courier_id)

        assert response.status_code == 404
        assert response.json() == {'code': 404, 'message': 'Заказа с таким id не существует'}


    @allure_step_decorator("Тест успешного получения информации заказа по трэк номеру")
    def test_list_apply_order(self):
        login, password, first_name = OtherMethods.generation_data()
        CourierMethods.create_courier(COURIER_URL, login, password, first_name)

        response = CourierLoginMethods.login_courier(COURIER_LOGIN_URL, login, password)
        response_data = response.json()
        courier_id = response_data['id']

        data = TestData.ORDER_DATA_ONE
        response = OrderMethods.create_order(ORDER_URL, data)

        response_data = response.json()
        order_track = response_data['track']

        response = OrderMethods.get_order_id_by_track(order_track)
        response_data = response.json()
        order_id = response_data['order']['id']

        OrderMethods.apply_order(ORDER_ACCEPT, order_id, courier_id)

        response = OrderMethods.get_order_list(courier_id)

        assert response.status_code == 200
        assert "orders" in response.json()
