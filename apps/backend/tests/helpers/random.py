import decimal
import random
import string


def get_random_string(length: int = 10):
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=length))

def get_random_decimal():
    return decimal.Decimal(random.randrange(155, 389))/100