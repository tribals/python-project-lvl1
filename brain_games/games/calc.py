import random

from brain_games.game import game


_RULES = 'What is the result of the expression?'

_MAX_QUESTION_NUMBER = 99
_MAX_QUESTION_NUMBER_MULTIPLICATION = 10
_ALLOWED_OPERATORS = ('+', '-', '*')


def game_calc(user):
    game(_RULES, question_expression, correct_answer, user)


def question_expression():
    op = _random_operator()

    a = _random_number()
    b = _random_number_second(op)

    return ((a, op, b), f'{a} {op} {b}')


def _random_operator():
    return random.choice(_ALLOWED_OPERATORS)


def _random_number():
    return random.randint(0, _MAX_QUESTION_NUMBER)


def _random_number_second(op):
    if op == '*':
        return random.randint(0, _MAX_QUESTION_NUMBER_MULTIPLICATION)

    return random.randint(0, _MAX_QUESTION_NUMBER)


def correct_answer(expression):
    (a, op, b) = expression

    if op == '+':
        answer = a + b
    elif op == '-':
        answer = a - b
    elif op == '*':
        answer = a * b
    else:
        raise RuntimeError(f'Unknown operator: {op}')

    return str(answer)
