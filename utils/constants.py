BASE_URL = "https://qa-scooter.praktikum-services.ru/"
API_VERS = "api/v1/"
COURIER_ENDPOINT = "courier/"
ORDER_ENDPOINT = "orders/"

# ==========================================================================
# Метод POST - создание курьера
COURIER_URL = f"{BASE_URL}{API_VERS}{COURIER_ENDPOINT}"

# Метод POST - Авторизация курьера
# Домолнительно можно использовать как DELETE  при передаче id в конце
COURIER_LOGIN_URL = f"{COURIER_URL}login/"


# ==========================================================================
# метод POST по созданию заказа
ORDER_URL = f"{BASE_URL}{API_VERS}{ORDER_ENDPOINT}"

# метод PUT по завершению заказа
ORDER_COMPLETE = f"{ORDER_URL}finish/{id}"

# метод PUT по отмене заказа
ORDER_CANCEL = f"{ORDER_URL}cancel/"

# метод GET по получению списку заказов
ORDER_LIST = f"{ORDER_URL}"

# метод GET по получению заказа по его трэк номеру
ORDER_TRACK_NUMBER = f"{ORDER_URL}/track"

# метод PUT по принятию заказа
ORDER_ACCEPT = f"{ORDER_URL}accept/"
# ==========================================================================
