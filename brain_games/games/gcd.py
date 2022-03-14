import random
import math


RULES = 'Find the greatest common divisor of given numbers.'

_MAX_QUESTION_NUMBER = 99


def question_gcd():
    a = _random_number()
    b = _random_number()

    return ((a, b), f'{a} {b}')


def _random_number():
    return random.randint(0, _MAX_QUESTION_NUMBER)


def correct_answer(gcd):
    (a, b) = gcd

    return str(math.gcd(a, b))
