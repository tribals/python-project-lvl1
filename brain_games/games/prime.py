from random import randint

from brain_games.game import game


_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

_MAX_QUESTION_NUMBER = 99

_ANSWER_YES = 'yes'
_ANSWER_NO = 'no'

_PRIME_NUMBERS = (
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97,
)


def game_prime(user):
    game(_RULES, question_number, correct_answer, user)


def question_number():
    n = randint(1, _MAX_QUESTION_NUMBER)

    return (n, n)


def correct_answer(number):
    if _is_prime(number):
        return _ANSWER_YES

    return _ANSWER_NO


def _is_prime(n):
    return n in _PRIME_NUMBERS
