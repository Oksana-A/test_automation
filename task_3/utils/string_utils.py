import string
import random


class StringUtils:

    @staticmethod
    def get_random_txt(length):
        return ''.join(random.choices(
            string.ascii_letters + string.digits, k=length))
