from random import sample
import string


def get_random_password(n) -> str:
    myline = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = sample(myline, n)
    password_str = "".join(password)
    return password_str


print(get_random_password(8))
