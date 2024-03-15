from methods.baseApp import BaseApp
from utils.allure_decorator import allure_step_decorator
from utils.constants import COURIER_URL


class CourierMethods:

    @staticmethod
    @allure_step_decorator("Метод по созданию курьера")
    def create_courier(url, login, password, first_name):
        data = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = BaseApp.send_post_request(url, data)

        return response

class CourierDeleteMethods:
    @staticmethod
    @allure_step_decorator("Метод по удалению курьера")
    def delete_courier(courier_id):
        courier_delete_url = f"{COURIER_URL}/{courier_id}"
        response = BaseApp.send_delete_request(courier_delete_url)

        return response
