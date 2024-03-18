import random
import string



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
