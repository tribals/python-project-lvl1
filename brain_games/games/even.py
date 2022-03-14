from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

_MAX_QUESTION_NUMBER = 9999

_ANSWER_YES = 'yes'
_ANSWER_NO = 'no'


def question_number():
    n = randint(1, _MAX_QUESTION_NUMBER)

    return (n, n)


def correct_answer(number):
    if _is_even(number):
        return _ANSWER_YES

    return _ANSWER_NO


def _is_even(n):
    return n % 2 == 0
