import allure

from methods.baseApp import BaseApp
from utils.allure_decorator import allure_step_decorator
from utils.constants import ORDER_TRACK_NUMBER, ORDER_URL


class OrderMethods:
    @staticmethod
    @allure.step("Создание заказа с корректными данными")
    def create_order(api_connection, data):
        data = data

        response = BaseApp.send_post_request(api_connection, data)

        return response


    @staticmethod
    @allure.step("Подтверждение принятия заказа")
    def apply_order(api_connection, order_track, courier_id):
        apply_order_url = f"{api_connection}{order_track}?courierId={courier_id}"

        response = BaseApp.send_put_request(apply_order_url)

        return response

    @staticmethod
    @allure_step_decorator("Получение трек-номера заказа")
    def get_order_track(api_connection, data):
        data = data

        response = BaseApp.send_post_request(api_connection, data)

        return response

    @staticmethod
    @allure_step_decorator("Получение трек-номера заказа")
    def get_order_id_by_track(order_track):
        get_order_id = f"{ORDER_TRACK_NUMBER}?t={order_track}"
        response = BaseApp.send_get_request(get_order_id)

        return response

    @staticmethod
    @allure_step_decorator("Получение списка заказов")
    def get_order_list(courier_id):
        get_order_id = f"{ORDER_URL}?courierId={courier_id}"
        response = BaseApp.send_get_request(get_order_id)

        return response
