from random import sample
from string import ascii_letters, digits, punctuation


def generate_simple_password(size=8):
    password = sample(ascii_letters + digits, size)
    return "".join(password)