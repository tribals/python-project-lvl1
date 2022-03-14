from random import randint

from brain_games.cli import base_main


_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

_MAX_QUESTION_NUMBER = 9999

_ANSWER_YES = 'yes'
_ANSWER_NO = 'no'


def main():
    base_main(_RULES, question_number, correct_answer)


def question_number():
    return randint(1, _MAX_QUESTION_NUMBER)


def correct_answer(number):
    if is_even(number):
        return _ANSWER_YES

    return _ANSWER_NO


def is_even(n):
    return n % 2 == 0
