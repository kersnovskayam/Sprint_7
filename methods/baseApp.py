import logging

import requests

from utils.allure_decorator import allure_step_decorator


class BaseApp:

    @staticmethod
    @allure_step_decorator("Производим отправка POST запроса")
    def send_post_request(url, data):
        try:
            response = requests.post(url, json=data)
            logging.info(f"Отправлен запрос POST по {url}")
            return response
        except requests.exceptions.RequestException as e:
            logging.info(f"Ошибка при отправлении запроса POST по {url}: {e}")
            return None

    @staticmethod
    @allure_step_decorator("Производим отправка DELETE запроса")
    def send_delete_request(url):
        try:
            response = requests.delete(url)
            logging.info(f"Отправлен запрос DELETE по {url}")
            return response
        except requests.exceptions.RequestException as e:
            logging.info(f"Ошибка при отправлении запроса DELETE по {url}: {e}")
            return None

    @staticmethod
    @allure_step_decorator("Производим отправка PUT запроса")
    def send_put_request(url):
        try:
            response = requests.put(url)
            logging.info(f"Отправлен запрос PUT по {url}")
            return response
        except requests.exceptions.RequestException as e:
            logging.info(f"Ошибка при отправлении запроса PUT по {url}: {e}")
            return None

    @staticmethod
    @allure_step_decorator("Производим отправка GET запроса")
    def send_get_request(url):
        try:
            response = requests.get(url)
            logging.info(f"Отправлен запрос GET по {url}")
            return response
        except requests.exceptions.RequestException as e:
            logging.info(f"Ошибка при отправлении запроса GET по {url}: {e}")
            return None
