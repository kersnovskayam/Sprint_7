from methods.baseApp import BaseApp
from utils.allure_decorator import allure_step_decorator


class CourierLoginMethods:

    @staticmethod
    @allure_step_decorator("Авторизация с корректными данными")
    def login_courier(api_connection, login, password):

        data = {
            "login": login,
            "password": password
        }

        response = BaseApp.send_post_request(api_connection, data)

        return response

    @staticmethod
    @allure_step_decorator("Авторизация курьера и получение его ID")
    def get_courier_id(api_connection, login, password):
        data = {
            "login": login,
            "password": password,
        }

        response = BaseApp.send_post_request(api_connection, data)

        if response.status_code == 200:
            response_data = response.json()
            courier_id = response_data.get('id')
            if courier_id:
                return courier_id
            else:
                raise ValueError("ID курьера не получен в ответе сервера.")
        else:
            raise ConnectionError(f"Ошибка при выполнении запроса: {response.text}")
