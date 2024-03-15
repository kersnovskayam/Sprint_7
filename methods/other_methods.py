import random
import string

from methods.baseApp import BaseApp
from utils.allure_decorator import allure_step_decorator
from utils.constants import COURIER_URL



class OtherMethods:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string

    @staticmethod
    def generation_data():
        login = OtherMethods.generate_random_string(10)
        password = OtherMethods.generate_random_string(10)
        first_name = OtherMethods.generate_random_string(10)

        return login, password, first_name



    @staticmethod
    @allure_step_decorator("Производим создание тестового пользователя")
    def register_new_courier_and_return_login_password():
        login_pass = []

        login = OtherMethods.generate_random_string(10)
        password = OtherMethods.generate_random_string(10)
        first_name = OtherMethods.generate_random_string(10)

        data = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = BaseApp.send_post_request(COURIER_URL, data)

        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        return login_pass