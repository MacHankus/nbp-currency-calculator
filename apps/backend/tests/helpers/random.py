import random
import string


def get_random_string(length: int = 10) -> str:
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=length))

def get_random_float() -> float:
    return float(random.randrange(155, 389))/100