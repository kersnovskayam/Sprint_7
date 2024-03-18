class TestData:
    EMPTY_LOGIN = "Qwe 123"
    EMPTY_PASSWORD = "Qwe 123"
    WRONG_LOGIN = ""
    WRONG_PASSWORD = ""
    INVALID_COURIER_ID = 99999
    WRONG_COURIER_ID = ""
    INVALID_ORDER_ID = 999999999
    WRONG_ORDER_ID = ""
    EXISTING_LOGIN = "existing_login"
    NONE_LOGIN = None
    NONE_PASSWORD = None

    ORDER_DATA_ONE = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }

    ORDER_DATA_TWO = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK",
            "GREY"
        ]
    }

    ORDER_DATA_THREE = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": []
    }
